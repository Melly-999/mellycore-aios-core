# MellyCore Loop Safety Contract

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Version:** 1.0
**Status:** Binding safety specification
**Scope:** Safety rules governing every MellyCore loop, in every tool, at every phase

---

## 1. Relationship To The Repo-Wide Contract

This document **extends** `[[../../shared_context/SAFETY_CONTRACT]]` and `[[../../PROJECT_RULES]]`. It does not replace or relax either. Every rule there applies here in full.

Where this document is silent, the repo-wide rules still apply. Where a loop skill, registry entry, or agent appears to permit something `PROJECT_RULES.md` forbids, **PROJECT_RULES.md wins** and the permission is a defect to be fixed.

## 2. Default Posture: Report-Only

**Every enabled loop reads and reports. Nothing else.**

This is not a phase-in convenience or a starting default to be relaxed once things look stable. It is the operating posture until a separate, explicitly approved task changes it, with evidence.

Enforced structurally, not by convention: `validators.py` rejects any enabled loop with a non-empty `allowed_write_scope`, any enabled loop at an action-capable level, and any loop with `ASSISTED` status while `phase == 1`.

A policy only a human can violate is a policy. A policy the tool cannot violate is a property. These are properties.

## 3. Prohibited Absolutely

No loop, and no agent operating a loop, may:

**Repository and git**
- write to the repository (including "just updating state")
- commit, push, merge, rebase, reset, or delete a branch
- create, remove, prune, unlock, or clean a worktree
- force-push or rewrite history

**Delivery**
- deploy anything
- publish or tag a release
- create or modify workflow YAML
- activate a scheduler, cron entry, or hook

**External systems**
- comment on, open, edit, approve, or merge a GitHub PR or issue
- call a provider API
- make any network request
- install a dependency, package, or MCP server

**Secrets**
- read, write, create, or modify `.env` or `.env.*`
- access secrets, credentials, provider keys, or tokens
- write any secret into state, a ledger, a log, or a report

**MellyTrade**
- read, report on, or touch MellyTrade execution or runtime paths
- introduce broker, order, buy, sell, execute, or connect-live behaviour
- introduce any trading capability whatsoever

Concluding that one of these is *necessary* does not make it permitted. **That conclusion is the escalation.** Report it and stop.

## 4. No Auto-Push, No Auto-Merge, No Deploy

Stated separately because these are the failures that cost the most and are the easiest to rationalize in the moment.

- **No auto-push.** Not for a "safe" branch, not for a "trivial" doc fix.
- **No auto-merge.** Not on green CI, not on an approving review, not ever without explicit operator approval for that specific merge.
- **No deploy.** Under any condition.

These are enforced by absence: no module in `scripts/loop_ops` can push, merge, or deploy, and `pr-review-monitor` has no GitHub capability at all. **Do not add one, and do not reach for raw git to work around the gap.** The gap is the feature.

## 5. No Provider Keys, No Secrets

- No loop may access a provider key. Keys stay outside the repository — see `[[../../shared_context/PROVIDER_SETUP]]`, which is itself a forbidden path.
- No loop may create, read, or modify `.env` or `.env.*`.
- State files and ledgers are **committed**. Anything written into one is visible to every reader of this repository, permanently, in history.
- Never write a secret, key, token, cookie, account identifier, or raw provider response into state, a ledger, a log, or a report.

**When reporting a suspected secret: file, line, and category only. Never the value.** Repeating a secret in order to report it publishes the secret — to the terminal, the log, and the transcript. `redact-check` obeys this by construction (`RedactionFinding` has no value field), and so must every agent.

Detection is heuristic. A clean `redact-check` is **not proof** that no secret is present.

## 6. Forbidden Paths

Baseline, applying to every loop. Never read, written, quoted, or reported on — not even to observe that something looks wrong:

- `.env`, `.env.*`
- `secrets/**`
- `credentials/**`
- `auth/**`
- `payments/**`
- `billing/**`
- `migrations/**`
- `infra/production/**` — production infrastructure
- `.github/workflows/**` — GitHub workflow YAML
- `shared_context/PROVIDER_SETUP.md` and `**/provider_keys*` — provider-key configuration
- `**/MellyTrade/**`, `**/mellytrade/**` — MellyTrade execution and runtime paths

Every registry entry must repeat this baseline in its own `forbidden_paths`. `validators.py` enforces the superset rule, so drift becomes a validation failure rather than a silent gap.

Adding a path to this list is always allowed. Removing one requires an approved task that states why.

## 7. Maximum Attempts And Stopping

Every loop declares `max_attempts`, `stagnation_threshold`, and `no_progress_threshold`. Validation requires all to be greater than zero.

The deterministic circuit breaker stops a loop on: max attempts, the same normalized error recurring, consecutive failures, no progress, measured budget exhaustion, verifier REJECT, the kill switch, or a forbidden lifecycle transition.

**Obeying the guard is mandatory.** An agent may not retry past it, re-run it hoping for a different answer, edit a ledger to change its verdict, lower a threshold, or start a fresh run to reset the counters. Each of those defeats the breaker, and defeating the breaker is the specific failure this design exists to prevent.

**Stopping when told to stop is a successful outcome.**

## 8. Independent Verifier

When `verifier_required` is true:

- the verifier **must not** be the agent that produced the work;
- the verifier **must not** implement the fix it verifies — the moment it does, it is the maker and nobody is checking the fix;
- the verifier's default verdict is **REJECT**, moving to ACCEPT only on evidence it observed first-hand;
- **unverifiable is REJECT**, never a pass.

An agent may not self-certify its independence. If you authored the work, say so and stop.

## 9. Worktree Isolation

Concurrent agents work in separate linked worktrees. The audit is **read-only**.

Forbidden without exception: `git worktree remove`, `git worktree prune`, `git worktree unlock`, `git reset`, `git clean`, branch deletion, and any command modifying a worktree or working tree.

There is no exception for "obviously stale" or "clearly abandoned". **A worktree you believe is abandoned may hold the only copy of in-progress work, and prune is not reversible by you.** Cleanup is an operator decision, always.

## 10. Human Escalation Triggers

Escalate immediately when:

- a safety rule is implicated;
- a loop would need a capability it does not have;
- evidence is ambiguous and a claim cannot be substantiated;
- the guard returns `ESCALATE_HUMAN`, `PAUSE_BUDGET`, or `BLOCK_INVALID_STATE`;
- a suspected real credential appears anywhere;
- a `.env` file appears in the working tree;
- a MellyTrade execution surface appears inside MellyCore;
- two worktrees appear to own the same task.

Escalation means: **stop, write down what was found and what is unresolved, and wait.** It does not mean proceed carefully.

Every loop declares at least one `human_gate`; a loop with none fails validation.

## 11. Global Pause And Kill Switch

- **Kill switch:** creating `shared_context/loops/KILL_SWITCH` halts every loop. The guard treats either the file's existence or the ledger's `kill_switch_engaged` flag as sufficient to halt — the two never need to agree in order to stop. This fails safe.
- **Soft pause:** `global.paused` in `[[../../shared_context/loops/LOOP_BUDGETS]]`.
- **No opt-out.** A `kill_switch` field that does not match the global switch is a validation error.

**Absence of the kill switch is not permission to act.** It means only that the global halt is not engaged. Permission comes from registry status and human gates.

## 12. Honesty Rules

Violating these is a safety failure, not a style problem: every one of them causes a human to trust something that has not earned trust.

- **Estimates are not measurements.** A token figure is measured only if it came from a ledger iteration with `tokens.measured = true`. Everything in `LOOP_BUDGETS.json` and every `estimate-cost` output is an estimate and must be labelled one.
- **Unrun is not passed.** Unavailable, timed out, blocked, and passed are four outcomes. Report the one that happened.
- **Configured is not exercised.** A file existing proves someone wrote a file.
- **Do not report a run that did not happen.** No MellyCore loop has been run. `RUN_LEDGER.example.json` is an example, not evidence.
- **Do not claim readiness** without executed validation, real run evidence, independent verifier evidence, and explicit human approval — all four.
- **Cite or drop it.** A claim you cannot tie to a file and line is not a finding.
- **Do not resolve a contradiction by choosing a side.** Report both with evidence; the operator decides.

## 13. MellyTrade Separation

MellyCore AIOS is a standalone command-center and shared-context project. It is **separate from MellyTrade** and contains no trading execution.

No loop may: read or touch MellyTrade runtime, execution, or broker code; introduce buy, sell, order, execute, broker, or connect-live capability; or add trading UI, trading logic, or market-data execution paths.

MellyTrade paths are forbidden paths (Section 6). This is a structural boundary, not a preference.

## 14. Related Documents

- `[[../../shared_context/SAFETY_CONTRACT]]`
- `[[../../shared_context/loops/LOOP_CONSTRAINTS]]`
- `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`
- `[[../research/LOOP_ENGINEERING_ADOPTION_REVIEW_001]]`
- `[[../../agent_prompts/loops/README]]`
