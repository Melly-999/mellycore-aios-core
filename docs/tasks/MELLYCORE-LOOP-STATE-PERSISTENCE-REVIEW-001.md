# MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001

## Task ID

`MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001`

## Outcome

PASS_REVIEW_DOCS_ONLY_NO_CODE_CHANGE

## Scope

Design and document a safe persistence contract for real report-only loop run evidence, and specify the correction for the token-measurement ambiguity (`total: 0` vs. genuinely unmeasured) that `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` surfaced. **Documentation and design only.** No implementation, schema, or state file was changed.

## Source Run

`MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` → outcome `EXERCISED_EXTERNALLY_NOT_REGISTERED`. That run's Section 7 finding — the guard reported `per_run_budget: pass` for a run whose tokens were explicitly unmeasured (`total: 0, measured: false`) — is the specific defect this review formalizes and specifies a fix for (not implements).

## Decisions Made

1. **Three-layer separation adopted:** immutable run evidence (`shared_context/loops/runs/<loop-id>/<run-id>.json`, proposed, does not exist yet) / derived mutable state (`shared_context/loops/states/<loop-id>.state.json`, schema unchanged) / purely-computed audit tiers (unchanged, stays computed-only, never persisted).
2. **Location for evidence:** `shared_context/loops/runs/<loop-id>/<run-id>.json` — chosen because `LOOP_STATE_SCHEMA.json`'s existing `run_history[].ledger_ref` field already implies evidence lives outside the state file; this review names and specifies that location rather than inventing a new concept.
3. **Persistence stays a separate, explicit, human-approved action** (a future `persist-run` CLI subcommand, not built here) — never a side effect of running a loop or of `guard`.
4. **Token contract correction specified:** `measured: false` must never carry a numeric `total` of `0`; unmeasured must be `null`/absent. `measured: true` requires a real non-negative number. The guard must key "unmeasured" off the `measured` flag alone, and any unmeasured iteration must make the whole run's per-run budget `unenforceable` — not a partial pass on the measured sum.
5. **Guard vs. semantic escalation vs. operator approval formalized as three distinct authorities** that must never be conflated in a report or a future implementation: mechanical limits, the loop's own judgment about `status_after`, and a named human's approval.
6. **Recommendation: ADOPT WITH REVISIONS** — adopt the persistence architecture, but only in the same implementation task that also fixes the token-semantics defects (D1/D2/D6 in the review); shipping persistence on the current ambiguous semantics would enshrine the ambiguity permanently.

## Unresolved Questions

Left explicitly open for the operator and the next implementation task:

1. Whether `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001`'s existing scratchpad ledger should ever be persisted once the corrected contract ships, or whether it should be discarded as pre-correction evidence and re-run cleanly.
2. The exact `run_id` format pattern (Defect D5) — this review specifies that one is needed and where it must be enforced, but does not fix the exact regex; the future task should align it with `loop_id`'s existing pattern conventions.
3. Whether `repository_mutation_count` / `remote_action_count` (used ad hoc in the dry-run ledger) should become formally required schema fields for every ledger, or remain optional/`additionalProperties`-only. This review recommends formalizing them but leaves the exact requiredness decision to the schema-editing task.
4. Whether a correction to an already-persisted ledger (Section 3's "no-overwrite" rule) should use a `<run-id>-correction-N` naming convention as sketched, or a different mechanism — sketched, not finalized.

## Files Created And Modified

**Created:**
- `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md`
- `docs/tasks/MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001.md`

**Modified (minimal, project-convention only):**
- `shared_context/RUN_QUEUE.md` — appended one queue entry recording this review's completion and recommended next task.
- `shared_context/AGENT_HANDOFF.md` — appended one handoff entry per repository convention ("update AGENT_HANDOFF.md after every meaningful task").

**Explicitly not modified, per this task's constraints:** `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`, any file under `scripts/loop_ops/`, any `.json` schema file, `shared_context/loops/LOOP_REGISTRY.json`, any file under `tests/`, and no file under `shared_context/loops/runs/` or `shared_context/loops/states/` (neither directory's contents changed; `runs/` still does not exist).

## Validation

Run from `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` on branch `publish/mellycore-main-001`, HEAD `6c67fc5bf28999882e26a45d12cc7eab639228e1` at task start.

| Command | Exit | Result |
| --- | --- | --- |
| `py -3.9 scripts/validate_project_state.py` | 0 | PASS |
| `py -3.9 -m scripts.loop_ops validate` | 0 | PASS — 9 loops, 0 findings |
| `py -3.9 -m scripts.loop_ops audit --json` | 0 | Unchanged from prior baseline: configured=9, validated=9, **exercised=0**, human_approved=0, production_enabled=0 |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 0 | OK — 102 tests (unchanged; no test files added or modified) |
| `git diff --check` | 0 | PASS |

No implementation was changed to make any of these pass — they already passed before this task and were unaffected by it, since only two new doc files and two minimal doc-index appends were made.

## Confirmation: No Runtime Capability Changed

- `shared_context/loops/runs/` does not exist after this task, same as before.
- No file under `scripts/loop_ops/` changed.
- No `.json` schema file changed.
- `project-health` is not marked exercised; `audit --json` summary is identical to the pre-task baseline.
- The prior dry run's scratchpad ledger was not persisted, copied, or referenced from any tracked file.
- No loop's lifecycle state, write scope, or level changed.
- No scheduler, workflow YAML, MCP, provider, or network capability was added.
- No push, merge, deploy, or remote contact occurred.

## Recommended Next Task

**`MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001`** — implement, together in one task (per this review's Section 13 recommendation, so the fix and the feature ship as one unit): the token-semantics correction (Section 5 / Defects D1, D2, D6) in `models.py`, `registry.py`, `guard.py`, and `RUN_LEDGER_SCHEMA.json`; the `runs/<loop-id>/<run-id>.json` persistence path and a `persist-run` CLI subcommand per Sections 3–7; and the acceptance tests enumerated in Section 11. Remains Phase 1: report-only loops stay report-only, persistence stays a separate human-approved action, and no loop gains write scope.

Not implemented here.

## Related Documents

- `[[../research/LOOP_STATE_PERSISTENCE_REVIEW_001]]`
- `[[MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001]]`
- `[[../../shared_context/loops/README]]`
