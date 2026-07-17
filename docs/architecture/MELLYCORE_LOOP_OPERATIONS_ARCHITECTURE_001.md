# MellyCore Loop Operations Architecture

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Version:** 1.0
**Status:** Phase 1 architecture (report-only foundation)
**Scope:** The architecture of recurring MellyCore agent workflows: components, lifecycle, controls, and the boundary between what exists and what is deferred.

---

## 1. What A Loop Is

A **loop** is a recurring agent workflow: check project health, look for contradictions in shared context, report on worktrees. It recurs, so it needs memory. It is executed by a model, so it needs limits. It touches a repository, so it needs a scope.

A loop is **not** a background service. Nothing described here runs on a timer or starts itself.

## 2. What Exists Today

This is the honest boundary, stated before the design so nothing below is mistaken for a running system:

| Component | State |
| --- | --- |
| Registry, state, and ledger contracts | Exist |
| Read-only CLI (validate, audit, guard, estimate-cost, worktree-audit, redact-check) | Exists, tested |
| Deterministic circuit breaker | Exists, tested |
| Canonical agent skills | Exist |
| Scheduler / trigger | **Does not exist.** Every run is started by a human |
| Implementer (an agent that changes code) | **Does not exist.** Phase 1 has no write path |
| GitHub connector | **Does not exist** |
| Loop runs | **None. No loop has ever been run** |

The pipeline below describes the **designed** shape. Sections marked *deferred* are design intent, not implementation.

## 3. Pipeline

```
   Schedule / Event
   (DEFERRED - Phase 1 has no scheduler; a human starts every run)
          |
          v
   +--------------+     reads     +---------------------+
   |    Triage    |<------------->|   Persistent State  |
   | (report-only)|               | states/<id>.json    |
   +--------------+               +---------------------+
          |                                 ^
          v                                 |
   +--------------------+                   |
   | Worktree Isolation |                   |
   | (audit only today) |                   |
   +--------------------+                   |
          |                                 |
          v                                 |
   +--------------+   (DEFERRED - no write path exists in Phase 1)
   | Implementer  |
   +--------------+
          |
          v
   +--------------+   independent agent; defaults to REJECT
   |   Verifier   |
   +--------------+
          |
          v
   +--------------+   append-only, per run
   |  Run Ledger  |
   +--------------+
          |
          v
   +------------------+   deterministic; no model
   | Circuit Breaker  |--> CONTINUE | ESCALATE_HUMAN | PAUSE_BUDGET | BLOCK_INVALID_STATE
   +------------------+
          |
          v
   +--------------+   every loop declares at least one gate
   |  Human Gate  |
   +--------------+
```

Cross-cutting: **cost controls**, **collision prevention**, and the **kill switch** apply at every stage.

## 4. Components

### 4.1 Schedule / Event Input — *deferred*

Each loop declares `trigger_type` (`manual`, `schedule`, `event`) and `suggested_cadence`. These record **intent only**. No scheduler, cron entry, hook, or workflow YAML exists or is authorized. A loop marked `schedule` is still started by a human.

A loop that starts itself removes the human from the loop, and the human is the control.

### 4.2 Triage

Reads within `read_scope`, decides what deserves attention, reports. Never acts. Backed by `[[../../agent_prompts/loops/mellycore-loop-triage]]`.

### 4.3 Persistent State

`shared_context/loops/states/<loop-id>.state.json`, per `[[../../shared_context/loops/LOOP_STATE_SCHEMA]]`.

State lives in a file because conversations end, contexts fill, and sessions get cleared. A fresh reader with no history must be able to reconstruct where a loop stands from this file alone.

State records lifecycle status, consecutive failures, last progress marker, last error signature, any open escalation, explicit human approval, and pointers to run ledgers. It is committed, so it must never contain a secret.

**No state file exists today**, because no loop has run. Every entry sets `state_file_is_template: true`. Pre-creating them would manufacture the appearance of history and make the audit's *exercised* signal meaningless.

### 4.4 Worktree Isolation

Concurrent agents work in separate linked worktrees. `scripts/loop_ops/worktrees.py` audits them read-only and reports collision risk: duplicate branch, duplicate task ownership, dirty, detached, stale, missing path.

It has **no mutation path and must never gain one**. Removal, pruning, unlocking, resetting, and cleaning are operator decisions. A worktree that looks abandoned may hold the only copy of someone's work.

### 4.5 Implementer — *deferred*

The component that would change code. **It does not exist.** Phase 1 has no write path, and validation rejects any enabled loop declaring a write scope.

### 4.6 Verifier

An **independent** agent that checks the maker's claims against evidence it observed itself. Two rules are absolute: it never implements the fix it verifies, and it defaults to **REJECT**.

The REJECT default is deliberate. A verifier that accepts unless something is obviously wrong is a rubber stamp, and a rubber stamp is worse than no verifier because it manufactures confidence nobody earned. See `[[../../agent_prompts/loops/mellycore-loop-verifier]]`.

### 4.7 Human Gate

Every loop declares at least one `human_gate`; validation rejects a loop with none. A gate is a point where a human must act before the loop proceeds. Gates are not advisory.

### 4.8 Run Ledger

Append-only, one per run, per `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]`. Records each attempt's outcome, error signature, progress marker, measured tokens, and verifier verdict.

Parse-time integrity rules:

- iteration indexes must be unique and strictly increasing — a rewritten ledger could edit a failure out of history;
- a failed iteration must carry an `error_signature` — without one, stagnation detection silently stops working while appearing to run.

### 4.9 Circuit Breaker

`scripts/loop_ops/guard.py`. Reads a ledger, applies the registry's limits, returns a decision. **Deterministic. Calls no model. Makes no network request.** The same ledger always yields the same decision.

This is the design's centre of gravity. An agent is the worst available judge of whether it should keep going — the agent that has failed four times is precisely the one most convinced the fifth attempt will succeed. So the decision is taken away from it and given to arithmetic.

| Decision | Exit | Trigger |
| --- | --- | --- |
| `CONTINUE` | 0 | No limit reached |
| `ESCALATE_HUMAN` | 2 | Max attempts, stagnation, consecutive failures, no progress, verifier REJECT, kill switch |
| `PAUSE_BUDGET` | 2 | Measured tokens over a budget |
| `BLOCK_INVALID_STATE` | 1 | Unknown loop, disabled loop, forbidden transition, unparseable ledger |

Precedence, strongest first: **invalid state → kill switch → escalation → budget**. Invalid state is decided first because no other check can be trusted against input that does not parse. The kill switch outranks the rest because it is the operator saying stop now.

It **fails closed**: an unexpected error yields `BLOCK_INVALID_STATE`, never `CONTINUE`.

### 4.10 Cost Controls

Per-run and daily token ceilings per loop; a global daily ceiling and `max_parallel_loops` in `[[../../shared_context/loops/LOOP_BUDGETS]]`.

The load-bearing distinction: **the guard enforces budgets only on measured tokens** — a ledger iteration with `tokens.measured = true`. Unmeasured values report `unenforceable`, never `pass`, because "I could not check" and "it passed" are different claims and only one is true.

`estimate-cost` produces planning figures for four scenarios (no-op, report, assisted action, and a weighted realistic mix), with maker/checker and parallel-agent multipliers. Every output carries `basis: ESTIMATE_NOT_MEASURED`. An estimate can neither trip nor satisfy a budget check. MellyCore has no measured token spend, because no loop has run.

### 4.11 Collision Prevention

`max_parallel_loops` is 1 in Phase 1 — concurrency is a collision risk Phase 1 does not attempt to manage. The worktree audit reports duplicate branch and duplicate task ownership so an operator can spot two agents claiming the same work.

### 4.12 Kill Switch

Creating `shared_context/loops/KILL_SWITCH` halts every loop. The guard checks the file's existence *and* the ledger's `kill_switch_engaged` flag; **either alone is sufficient to halt**, so the two never need to agree in order to stop. `LOOP_BUDGETS.json` also carries `global.paused` as a softer operator stop.

Absence of the kill switch is **not permission to act**. It only means the global halt is not engaged. Permission comes from registry status and human gates.

No loop may opt out: a `kill_switch` field that does not match the global switch is a validation error.

## 5. Lifecycle

```
        DRAFT
          |
          v
    REPORT_ONLY <-------------------+
       |    |                       |
       |    +--> ASSISTED (Phase 2+, gated)
       |            |               |
       v            v               |
   WAITING_HUMAN <--+               |
       |  |                         |
       |  +--> PAUSED --------------+
       |  |
       |  +--> BLOCKED
       |          |
       |          v
       |     WAITING_HUMAN  (BLOCKED may not resume directly)
       v
   COMPLETED --> DISABLED --> DRAFT
```

| State | Meaning |
| --- | --- |
| `DRAFT` | Defined, not operating |
| `REPORT_ONLY` | Reads and reports. No mutation. The only enabled state in Phase 1 |
| `ASSISTED` | Proposes changes behind a human gate. **Forbidden in Phase 1** |
| `WAITING_HUMAN` | Blocked on a human decision |
| `PAUSED` | Stopped by budget or operator |
| `BLOCKED` | Stopped by an unresolved problem |
| `COMPLETED` | Finished its purpose |
| `DISABLED` | Off. Requires a stated `disabled_reason` |

Two transition rules are deliberately strict, enforced by `ALLOWED_TRANSITIONS`:

- **DRAFT may not jump to ASSISTED.** A loop earns action capability by first proving itself report-only.
- **BLOCKED may not resume directly.** It must pass through WAITING_HUMAN, because a human decided it was blocked and a human decides it is not.

## 6. Levels And The Phase 1 Gate

| Level | Meaning | Phase 1 |
| --- | --- | --- |
| `L0` | Manual | May be enabled |
| `L1` | Report-only | May be enabled |
| `L2` | Assisted; proposes changes | **Must be DISABLED or DRAFT** |
| `L3` | Unattended | **Not designed, not reachable** |

Enforced structurally by `validators.py`, not by convention:

- `ASSISTED` status is rejected outright while `phase == 1`;
- an enabled loop with a non-empty `allowed_write_scope` is rejected;
- an enabled loop at L2/L3 is rejected.

**L3 is not production-ready merely because configuration for it could exist.** `readiness.py` makes `production_enabled` structurally false while `phase == 1` — even for a loop that is validated, exercised, operator-approved, and verifier-backed. A test asserts exactly that.

## 7. Capability Tiers

The audit refuses the file-counting shortcut:

| Tier | Earned by |
| --- | --- |
| `configured` | A registry entry exists. **Proves authorship only** |
| `validated` | Passes validation |
| `exercised` | A real run recorded in state. An example file never counts |
| `human_approved` | An operator recorded explicit approval, with a name |
| `production_enabled` | All of the above, plus an independent verifier and an approved enabling task |

No tier is inferred from a weaker one, and every `false` states its reason.

**Today: 9 configured, 9 validated, 0 exercised, 0 approved, 0 production-enabled.**

## 8. Registered Loops

| Loop | Level | Status |
| --- | --- | --- |
| `project-health` | L1 | REPORT_ONLY |
| `context-drift` | L1 | REPORT_ONLY |
| `safety-posture` | L1 | REPORT_ONLY |
| `pr-review-monitor` | L1 | REPORT_ONLY |
| `worktree-hygiene` | L1 | REPORT_ONLY |
| `changelog-drafter` | L1 | REPORT_ONLY |
| `ci-sweeper` | L2 | DISABLED |
| `dependency-sweeper` | L2 | DISABLED |
| `post-merge-cleanup` | L2 | DISABLED |

Every enabled loop has an empty `allowed_write_scope`. Every disabled loop states why.

## 9. Rollout

- **Phase 1 (this task).** Contracts, read-only tooling, canonical skills. Report-only. No runs.
- **Phase 2 (not authorized).** Actually run a report-only loop by hand, produce a real ledger, and see whether the guard behaves as designed against real input. This is what converts *configured* into *exercised*.
- **Phase 3+ (not authorized).** Only after real evidence: consider ASSISTED behind a human gate, with an independent verifier.

Each phase requires a separate approved task. No phase is entered because the previous one produced files.

## 10. Related Documents

- `[[../safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`
- `[[../research/LOOP_ENGINEERING_ADOPTION_REVIEW_001]]`
- `[[../../shared_context/loops/README]]`
- `[[../../shared_context/loops/LOOP_CONSTRAINTS]]`
- `[[../../agent_prompts/loops/README]]`
