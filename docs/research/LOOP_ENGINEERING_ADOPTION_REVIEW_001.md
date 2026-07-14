# Loop Engineering — Adoption Review

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Version:** 1.0
**Status:** Research summary (docs-only)
**Scope:** Record which concepts from the external `loop-engineering` project MellyCore adopts, adapts, or refuses, and state exactly what was and was not copied.

---

## 1. Source And Provenance

**Source repository:** `https://github.com/cobusgreyling/loop-engineering`

**Reviewed commit:** **None observed.** No commit SHA is recorded because the repository was not fetched, cloned, browsed, or read during this task.

This needs stating plainly rather than glossed. This task's safety posture prohibits external calls, so the repository was **not accessed**. This review is therefore an adaptation of the *concepts as described in the task brief that commissioned this work* — recurring agent loops, persistent state outside conversations, maker/checker separation, deterministic circuit breakers, token budgets, worktree isolation, human escalation, machine-readable loop registries, and report-only phased rollout — not a review of that repository's source code.

The distinction matters. A reader might reasonably assume "adoption review" means someone read the code. Nobody did. Every design decision below was made on the merits of the concept as understood, and every claim about the external project's limitations (Section 4) is **inherited from the task brief and independently unverified by this task**.

**What was copied: nothing.** No runtime code, no configuration, no schema, no prompt text, no documentation, no file structure, and no assets were vendored from the external repository. Every file created by this task was written from scratch for MellyCore. There is no vendored-code list because there is no vendored code.

**No dependency was added.** No npm package, no Python package, no MCP server.

## 2. Licensing And Attribution

The external project is understood to be MIT-licensed. MIT permits reuse with attribution.

MellyCore's position is simpler than the licence requires: **because no code or text was copied, no MIT licence obligation is triggered.** Attribution is given here as a matter of intellectual honesty — the architectural ideas are not original to MellyCore — not because a licence compels it.

If any future task vendors code, prompt text, or documentation from that project, that task **must**:

1. record the exact commit SHA and retrieval date,
2. reproduce the MIT licence text and copyright notice alongside the vendored material,
3. list every vendored file explicitly in a review document like this one,
4. obtain operator approval before the vendoring, not after.

Until then, MellyCore's relationship to this project is conceptual only.

## 3. Concepts Adopted

| Concept | How MellyCore adapts it |
| --- | --- |
| **Machine-readable loop registry** | `[[../../shared_context/loops/LOOP_REGISTRY]]` — JSON, not YAML, so no parsing dependency. Every loop declares scope, budgets, gates, forbidden paths, and lifecycle state. |
| **State outside the conversation** | `[[../../shared_context/loops/LOOP_STATE_SCHEMA]]` — a loop's memory is a file. A conversation ends; the state persists. If a loop's memory lives only in a context window, the loop has no memory. |
| **Run ledger** | `[[../../shared_context/loops/RUN_LEDGER_SCHEMA]]` — append-only per-run record. The only input the circuit breaker trusts. |
| **Deterministic circuit breaker** | `scripts/loop_ops/guard.py` — reads a ledger, returns a decision, calls no model. An agent that has failed four times is exactly the agent most convinced the fifth will work; its judgment is not an input. |
| **Maker/checker separation** | `[[../../agent_prompts/loops/mellycore-loop-verifier]]` — the verifier never implements the fix it verifies, and defaults to REJECT. |
| **Token budgets** | Per-run and daily ceilings in the registry, enforced by the guard on **measured** usage only. |
| **Worktree isolation** | `scripts/loop_ops/worktrees.py` — read-only audit of collision risk across concurrent agent worktrees. |
| **Human escalation** | Every loop declares `escalation_condition` and at least one `human_gate`. Validation rejects a loop with no gate. |
| **Report-only phased rollout** | Phase 1 is report-only, enforced structurally by the validator rather than by convention. |
| **Lifecycle states** | DRAFT / REPORT_ONLY / ASSISTED / WAITING_HUMAN / PAUSED / BLOCKED / COMPLETED / DISABLED, with an explicit allowed-transition map. |

## 4. Limitations Identified In The External Approach

These limitations were supplied by the task brief. **This task did not verify any of them** — the repository was not read. They are recorded because each one shaped a MellyCore countermeasure, and the countermeasures stand on their own merits regardless of whether the criticism of the external project is accurate.

| Reported limitation | MellyCore's countermeasure |
| --- | --- |
| Readiness scores may overrate a project based mainly on file presence | `scripts/loop_ops/readiness.py` separates *configured*, *validated*, *exercised*, *human_approved*, and *production_enabled*, and never infers a stronger tier from a weaker one. A registry entry proves authorship, nothing more. `audit` currently reports **0 exercised**, because that is the truth. |
| `loop-init` can overwrite existing state or configuration | MellyCore ships **no init/scaffold command at all**. Every command is read-only. A tool that cannot write cannot overwrite. State files are created by real runs, not generated to look like history. |
| Token costs are estimates presented as spend | Every estimator output carries `basis: ESTIMATE_NOT_MEASURED`. The guard enforces budgets **only** on ledger values with `tokens.measured = true`; unmeasured values report `unenforceable`, never `pass`. An estimate can neither trip nor satisfy a budget. |
| Some auto-fix interfaces are incomplete | MellyCore ships **no auto-fix**. `ci-sweeper` and `dependency-sweeper` are DISABLED with stated reasons. A half-built auto-fix is worse than none: it invites trust it has not earned. |
| Documented no-auto-merge policy inconsistent with dogfood workflow | The policy is enforced in code, not documentation. No module can push, merge, or comment; `pr-review-monitor` has no GitHub capability whatsoever. A policy only a human can violate is a policy; a policy the tool cannot violate is a property. |
| Failure stories are teaching material, not verified production evidence | Treated as teaching examples only. No MellyCore document cites them as evidence, and `RUN_LEDGER.example.json` is labelled an example rather than a run. |

## 5. Concepts Rejected

| Rejected | Why |
| --- | --- |
| **Scheduler / cron activation** | A loop that starts itself removes the human from the loop. Phase 1 loops declare `trigger_type` as intent only; every run is started by a human. |
| **Unattended (L3) operation** | Not designed, not configured, not reachable. `production_enabled` is structurally false while `phase == 1`, even for a loop that is exercised, approved, and verifier-backed — as a test asserts. |
| **Autonomous code mutation** | No loop writes to the repository. Enabled loops must have an empty `allowed_write_scope`, enforced by validation. |
| **Auto-fix on CI failure** | Deferred. An agent fixing CI unattended optimizes for green, not for correct. |
| **GitHub connectors / PR automation** | No API calls, comments, approvals, or merges. Reporting only. |
| **MCP server installation** | Out of scope; adds an attack surface and a dependency, and Phase 1 needs neither. |
| **YAML configuration** | JSON avoids a parsing dependency. MellyCore adds no runtime dependencies. |
| **Auto-pruning stale worktrees** | Destructive and not reversible by the tool. A worktree that looks abandoned may hold the only copy of in-progress work. The audit reports; the operator decides. |
| **Agent self-assessed readiness** | Readiness is evidence-gated, not self-reported. |

## 6. MellyCore-Specific Adaptations

Beyond the countermeasures above:

- **Fail closed everywhere.** An unexpected error in the guard yields `BLOCK_INVALID_STATE`, never `CONTINUE`. An unreadable state file is treated as absent, never as evidence.
- **Append-only ledgers, enforced.** Duplicate or out-of-order iteration indexes are refused at parse time, so a failure cannot be quietly edited out of the record.
- **A failed iteration must carry an error signature.** Without one, stagnation detection would silently stop working while appearing to run.
- **Forbidden paths are per-loop and enforced as a superset** of the global baseline, so drift becomes a validation failure rather than a silent gap.
- **No loop may opt out of the global kill switch** — a mismatched `kill_switch` field is a validation error.
- **The redaction scanner cannot leak.** `RedactionFinding` has no value field by construction, so a detected secret cannot be printed even by mistake. It reports file, line, and category.
- **MellyTrade separation is a forbidden path**, not a guideline. No loop may touch MellyTrade runtime or execution surfaces, and no loop may introduce broker, order, buy, sell, execute, or connect-live behaviour.
- **Canonical skills live in one place** (`[[../../agent_prompts/loops/README]]`) with tool wrappers referencing them, so Claude and Codex cannot drift into two different rulebooks.

## 7. Honest Assessment Of What This Task Produced

A **foundation**, not an operating system:

- 9 loops are defined; 6 are REPORT_ONLY, 3 are DISABLED.
- **0 loops have been run.** There is no run evidence, no measured token spend, and no exercised capability.
- The CLI is validated by 102 passing tests and by its own `validate` command against the shipped registry.
- Nothing here is authorized to act, and nothing here can act.

This foundation should not be described as operational, autonomous, production-ready, or unattended-ready. It is a set of contracts and read-only tools that make those things *possible to build safely later*, with the gates already in place.

## 8. Related Documents

- `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`
- `[[../safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`
- `[[../../shared_context/loops/README]]`
- `[[../../shared_context/loops/LOOP_CONSTRAINTS]]`
