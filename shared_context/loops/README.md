# MellyCore Loop Registry

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Version:** 1.0
**Status:** Phase 1 — report-only foundation
**Scope:** Machine-readable definitions, state contracts, and budgets for recurring MellyCore agent workflows ("loops")

---

## 1. What This Directory Is

A loop is a recurring agent workflow that MellyCore may want to run repeatedly — checking project health, spotting contradictions in shared context, reporting on worktrees. This directory is the single source of truth for **which loops exist, what they may read, what they may never touch, when they must stop, and who must approve what**.

It is a set of contracts. It is not a runtime. Nothing in this directory runs on a timer, and nothing here can start itself.

## 2. What Phase 1 Actually Is

Phase 1 is **report-only**. Every enabled loop reads and reports. No loop writes to the repository, pushes, merges, deploys, comments on GitHub, installs anything, or calls a provider API.

Three loops (`ci-sweeper`, `dependency-sweeper`, `post-merge-cleanup`) are defined but `DISABLED`. They are written down so the boundary is explicit and reviewable — a disabled loop with a stated reason is easier to reason about than an undocumented gap. Each carries a `disabled_reason`.

**No loop has ever produced persisted evidence.** `runs/` does not exist yet. The `audit` command reports this honestly, and the example ledger is labelled as an example rather than as evidence. (One loop, `project-health`, has been hand-run once outside this repository — outcome `EXERCISED_EXTERNALLY_NOT_REGISTERED` — but that run was never persisted, so it still does not count; see `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md`.)

## 3. Files

| File | Purpose |
| --- | --- |
| `LOOP_REGISTRY.json` | The registry. Every loop, its scope, budgets, gates, and lifecycle state. |
| `LOOP_REGISTRY_SCHEMA.json` | Contract for the registry. |
| `LOOP_STATE_SCHEMA.json` | Contract for a per-loop state file — the loop's memory outside any conversation. |
| `RUN_LEDGER_SCHEMA.json` | Contract for a single run. The only input the circuit breaker trusts, and (once `completed_at`, `repository`, `branch`, `head_sha`, `outcome`, and the two Phase 1 counters are present) the only input `persist-run` will accept. |
| `RUN_LEDGER.example.json` | A hand-written example of the ledger shape. Not evidence of a run. |
| `LOOP_BUDGETS.json` | Global pause, kill switch, and the estimator's planning inputs. All estimates. |
| `LOOP_CONSTRAINTS.md` | The binding rules an agent must read before operating any loop. |
| `states/` | Per-loop state files. Templates until a loop's evidence is actually persisted. Always fully rebuilt from `runs/`, never hand-edited. |
| `runs/` | Per-loop, write-once, immutable run evidence: `runs/<loop-id>/<run-id>.json`. Does not exist until the first `persist-run --apply`. |

JSON is used rather than YAML so that nothing here requires a parsing dependency. MellyCore adds no runtime dependencies.

## 4. How To Read It

```powershell
py -3.9 -m scripts.loop_ops validate
py -3.9 -m scripts.loop_ops audit
py -3.9 -m scripts.loop_ops audit --json
py -3.9 -m scripts.loop_ops persist-run --ledger <path>
```

`validate` checks structure, unique IDs, lifecycle states, budgets, forbidden paths, and the Phase 1 report-only rule. `audit` reports what each loop's capability actually is, distinguishing *configured* from *exercised* — a file existing is not a capability; `exercised` requires a `run_history` entry in state whose `ledger_ref` resolves to a real, independently-validated evidence file under `runs/<loop-id>/`, not merely a claim in state.

`persist-run --ledger <path>` validates a candidate ledger and, by default, writes nothing (dry run). Persisting for real requires `--apply`, a non-empty `--operator-approval-id`, and an `--expected-head` matching the repository's actual current HEAD — all three are mandatory; any one missing fails closed. See `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md` for the full design and `docs/tasks/MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001.md` for what was actually implemented.

See `[[../../docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]` for the design and `[[../../docs/safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]` for the binding safety rules.

## 5. The Kill Switch

Creating the file `shared_context/loops/KILL_SWITCH` halts every loop. It does not exist by default, and its absence is **not** permission to act — it only means the global halt is not engaged. Permission comes from the registry status and the human gates.

`LOOP_BUDGETS.json` also carries `global.paused`, a softer operator-controlled stop.

## 6. Relationship To The Repo-Wide Contract

This directory extends `[[../SAFETY_CONTRACT]]` and `[[../../PROJECT_RULES]]`. It does not relax anything in either. Where this directory is silent, the repo-wide rules still apply. No loop may authorize an action that `PROJECT_RULES.md` forbids.

MellyCore AIOS remains separate from MellyTrade. No loop may read, report on, or touch MellyTrade execution or runtime paths, and no loop may introduce broker, order, buy, sell, execute, or connect-live behaviour.
