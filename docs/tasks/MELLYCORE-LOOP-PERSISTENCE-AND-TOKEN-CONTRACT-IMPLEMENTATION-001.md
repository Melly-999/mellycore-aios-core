# MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001

## Task ID

`MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001`

## Outcome

`PASS_PERSISTENCE_AND_TOKEN_CONTRACT_COMMITTED`

## Scope

Implement, together, the contract reviewed (design-only) by `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md`: the corrected measured/unmeasured token contract; write-once immutable run-evidence persistence; derived loop-state updates; a guarded `persist-run` CLI command; audit recognition of valid persisted evidence (closing Defect D4); recovery from an interrupted persist; and the acceptance tests the review specified. No real run was persisted by this task.

## Pre-Flight

- Repo: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Branch: `publish/mellycore-main-001`
- HEAD at task start: `ac27dc64901ed77837f77285fa5cc092397468fc` (confirmed prefix `ac27dc6`)
- Confirmed `27ccd9e` present in history (the persistence-review commit)
- Upstream: `clean-origin/main`
- Linked worktrees observed (unmodified by this task): `mellycore-aios-context-smoke-001`, `mellycore-aios-glm-reference-inventory-fix-001`, `mellycore-aios-public-polish-001`
- Worktree was clean at task start
- Baseline commands (`validate_project_state.py`, `loop_ops validate`, `loop_ops audit --json`, `unittest discover`, `git diff --check`) all passed before any change, with the expected baseline: `configured: 9`, `validated: 9`, `exercised: 0`, `production_enabled: 0`, 102 tests passing.

## Token-Contract Implementation

Implemented the invariants from the review's Section 5, exactly:

- **`measured: false`** — `tokens.total` must be `null`/absent; a numeric value, including `0`, is rejected at parse time (`scripts/loop_ops/registry.py::_parse_iteration`).
- **`measured: true`** — `tokens.total` is required and must be a non-negative integer; `0` is valid and means a real measured zero, distinct from "not measured."
- **`RunLedger.has_unmeasured_tokens`** (`scripts/loop_ops/models.py`) now keys off the `measured` flag alone, never inferred from the value — closing D2.
- **`guard.py`'s `per_run_budget` check**: any unmeasured iteration in a run now makes the whole run's `per_run_budget` `unenforceable`, unconditionally — never a partial pass computed only over the measured-only sum, even if that sum alone would already exceed the budget. Closes D1/D6.
- **`RUN_LEDGER_SCHEMA.json`**: `tokens.total`/`input`/`output` widened to `["integer", "null"]`; an `if`/`then`/`else` block documents the conditional rule for readability. As the schema's own header states, this is documentation — the real enforcement is the Python above, not a JSON Schema library.
- **`RUN_LEDGER.example.json`**: both illustrative iterations updated from `measured: false` with a nonzero numeric `total` (the exact ambiguous pattern the review named) to `total: null`, per the review's Section 9 migration note.

## Persistence Architecture

New module `scripts/loop_ops/persist.py` implements the three-layer separation from the review's Section 3, unchanged in shape:

1. **Immutable run evidence** — `shared_context/loops/runs/<loop-id>/<run-id>.json`. Write-once. A byte-identical resubmission is treated as recovery (see below); different bytes at an existing destination are always refused (`EVIDENCE_CONFLICT`).
2. **Derived loop state** — `shared_context/loops/states/<loop-id>.state.json`. Always fully rebuilt (`derive_state`) from the complete set of a loop's persisted evidence files, plus `human_approval`/`notes` carried forward verbatim from the prior state, since no ledger can ever imply those. This makes state reconstructible from evidence alone by construction, not by convention (acceptance test 20).
3. **Audit tiers** — unchanged in `readiness.py`'s structure; only the evidence required to earn `exercised` was tightened (see D4 closure below).

Two entry points only, matching the review's "persistence is a separate, explicit, human-approved action" rule:

- **`dry_run(ledger_path, ...)`** — validates everything, writes nothing.
- **`apply(ledger_path, operator_approval_id, expected_head, ...)`** — requires both arguments non-empty; `expected_head` must equal the repository's actual current HEAD at the moment of the call (`HEAD_MISMATCH` otherwise); re-runs every dry-run check before writing.

CLI: `py -3.9 -m scripts.loop_ops persist-run --ledger <path> [--apply --operator-approval-id <id> --expected-head <sha>] [--json]`. Default is dry-run.

The `--operator-approval-id` recorded in a persisted record is documented, explicitly, as audit metadata supplied by the CLI invoker — not cryptographic proof of operator identity — both in `persist.py`'s module docstring and in the persisted record's own `persisted_by.note` field.

## Path And Immutability Protections

- **Run ID contract**: canonical pattern `^[a-z0-9][a-z0-9-]{0,63}--[0-9]{8}T[0-9]{6}Z--[0-9a-f]{12}$`, validated in full before any path is constructed (`validate_run_id_format`), plus a check that the run_id's own loop-id segment matches the ledger's `loop_id` field.
- **Path containment**: `resolve_run_path`/`resolve_state_path` resolve the candidate path and verify it stays under the canonical `runs/`/`states/` root via `Path.resolve().relative_to(...)` — defense in depth, since the run_id/loop_id patterns already exclude `/`, `\`, and `..` on their own.
- **Symlink checks**: every path component from the canonical root down to the destination is checked for `is_symlink()` before any write; the destination itself is checked too.
- **Case-collision checks** (Windows): before creating a loop directory or evidence file, existing sibling entries are checked case-insensitively so a directory/file differing only in case cannot collide.
- **Overwrite protection**: `check_existing_evidence` compares the embedded `ledger` object of any existing evidence file against the new submission; identical content returns `"identical"` (recovery path, existing file untouched); different content raises `EVIDENCE_CONFLICT`; absence returns `"absent"`.
- **No correction and no `--force` mechanism exist in Phase 1**, per the review's explicit non-goal.

## Atomicity And Recovery

- Both the evidence file and the state file are written via `_atomic_write_bytes`: content is written to a sibling temp file in the same directory, `fsync`'d, then moved into place with `os.replace` (atomic on both POSIX and Windows).
- Write order is always evidence, then state.
- If the state write fails after evidence was successfully written, `apply` raises `PartialPersistenceError` naming the run and the evidence path that was written, and instructs a retry with the identical ledger. The evidence file is never deleted automatically.
- Because `readiness.py` only counts a run as `exercised` when a state `run_history` entry's `ledger_ref` resolves to real evidence (see below), a state-less evidence file is correctly invisible to the audit until state is repaired — there is no window where a partial persist can misreport as exercised.
- A retry with the identical ledger finds the existing evidence (`evidence_status: "identical"`) and completes only the missing state, without ever rewriting the evidence file.

## Audit Classification (Closes D4)

`scripts/loop_ops/readiness.py::_entry_is_real_run` replaces the old face-value trust in a `run_history` entry. A `run_history` entry now counts toward `exercised` only when **all** of the following hold:

1. It has `run_id`, `finished_at`, and a `ledger_ref` string.
2. `ledger_ref` starts with `shared_context/loops/runs/<this-loop-id>/`.
3. The file it names exists and parses as a JSON object.
4. Its `final_classification` is `"PERSISTED"`.
5. Its embedded `ledger.loop_id` and `ledger.run_id` match the state entry's own claim.
6. Its `ledger.completed_at` matches the state entry's `finished_at`.
7. `ledger.repository` and `ledger.head_sha` are both present.
8. `ledger.repository_mutation_count` and `ledger.remote_action_count` are both exactly `0`.
9. The embedded ledger independently passes `registry.parse_ledger` (the same base validation `guard` and `persist-run` both rely on).

An orphan `run_history` entry (no matching evidence, or evidence that fails any of the above) is not exercised. An orphan evidence file with no state entry pointing to it is likewise not exercised, since the audit never scans `runs/` directly — it only ever reads `run_history` in state. Neither condition is sufficient for `human_approved`, `production_enabled`, `L2`, or `ASSISTED` — those remain strictly separate, operator-only facts that persisting a run never sets.

## Files Changed

- `scripts/loop_ops/persist.py` (new)
- `scripts/loop_ops/models.py` — `Iteration.tokens_total` default, `has_unmeasured_tokens`
- `scripts/loop_ops/registry.py` — `_parse_iteration` token validation
- `scripts/loop_ops/guard.py` — `per_run_budget` unenforceable-on-any-unmeasured logic
- `scripts/loop_ops/readiness.py` — `_entry_is_real_run`, `_real_run_count` (D4 closure)
- `scripts/loop_ops/cli.py` — `persist-run` subcommand
- `shared_context/loops/RUN_LEDGER_SCHEMA.json` — conditional token type, run_id pattern, persist-only field docs
- `shared_context/loops/RUN_LEDGER.example.json` — corrected unmeasured totals to `null`
- `shared_context/loops/README.md` — `runs/`, `persist-run`, corrected exercised description
- `shared_context/loops/LOOP_CONSTRAINTS.md` — one clarifying sentence on the token contract
- `tests/loop_ops_fixtures.py` — `make_iteration` default fix, new `make_run_id`/`make_persistable_ledger`
- `tests/test_loop_ops_guard.py` — fixed one stale test, added `TokenContractTests` and three budget tests
- `tests/test_loop_ops_tools.py` — fixed two stale readiness tests, added one D4-regression test
- `tests/test_loop_ops_persist.py` (new) — 37 tests covering path safety, immutability, atomicity, gating, timestamps, redaction, and audit integration
- `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`, `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`
- `docs/tasks/MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001.md` (new, this file)

## Tests And Exit Codes

| Command | Exit | Result |
| --- | --- | --- |
| `py -3.9 scripts/validate_project_state.py` | 0 | PASS |
| `py -3.9 -m scripts.loop_ops validate` | 0 | PASS — 9 loops, 0 findings |
| `py -3.9 -m scripts.loop_ops audit --json` | 0 | `configured: 9`, `validated: 9`, `exercised: 0`, `human_approved: 0`, `production_enabled: 0` |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 0 | OK — 150 tests (102 baseline + 11 new/fixed in `test_loop_ops_guard.py` and `test_loop_ops_tools.py` + 37 new in `test_loop_ops_persist.py`) |
| `py -3.9 -m compileall -q scripts/loop_ops tests` | 0 | OK |
| `git diff --check` | 0 | PASS |

A real dry-run smoke test was also run against this repository's actual `project-health` loop with a hand-built temporary ledger file (`--ledger`, no `--apply`): it validated cleanly, recomputed the guard decision (`CONTINUE`), and proposed correct destination paths. `git status --short` before and after confirmed nothing was written. `--apply` was then exercised twice against the same temp ledger, once with no flags and once with only `--expected-head`, and both failed closed with `MISSING_APPROVAL` / `MISSING_EXPECTED_HEAD` respectively, writing nothing.

## Real Repository State Confirmation

- `shared_context/loops/runs/` does not exist in this repository after this task.
- No file under `shared_context/loops/states/` was created or modified by this task in the real repository (all persistence tests operate against temporary directories via `root=` overrides).
- `audit --json`'s summary is unchanged from the pre-task baseline: `exercised: 0`, `human_approved: 0`, `production_enabled: 0`.
- No `project-health` (or any loop) run was persisted by this task.

## Safety Confirmation

- Standard library only (`json`, `os`, `re`, `subprocess`, `tempfile`, `datetime`, `pathlib`) — no new dependency added, no `requirements`/lockfile touched (none exists).
- No network request; no provider or model call; no MCP; no scheduler; no GitHub connector or remote git operation (the only git use is local, read-only `rev-parse` calls to read the current branch/HEAD for identity comparison).
- No push, PR, merge, or deploy.
- No automatic loop persistence — persistence is only ever invoked explicitly via the CLI.
- No automatic commit from the CLI.
- No loop may write its own evidence — `persist-run` is a separate, explicitly human-invoked command, never a side effect of `guard` or any loop run.
- No lifecycle promotion beyond `REPORT_ONLY` — `status_after in ("ASSISTED",)` is refused outright (`LIFECYCLE_PROMOTION_FORBIDDEN`).
- No change to `allowed_write_scope` anywhere.
- No loop became `production_enabled`.
- No MellyTrade file touched.
- No frontend, `site/`, or localhost-quickstart change.
- No real run ledger persisted; the previous dry run's scratchpad ledger was not touched, referenced, or persisted.
- No destructive git action taken.

## Local Commit

One local commit was created after all validations passed:

```
feat(aios): add guarded loop evidence persistence
```

Not pushed.

## Remaining Tasks To Milestone A

- A registered `project-health` run: hand-run the loop again to produce a real ledger with the persistence-only fields populated, then have an operator invoke `persist-run --apply` to persist it for real — the first time `audit` will honestly report `exercised: 1`.
- A weekly L1 pilot (a report-only loop run on a recurring cadence) remains pending and unblocked by this task's scope; still no write scope for any loop.

## Recommended Next Task

A registered `project-health` run, exactly as specified above. It is docs/evidence-producing work plus one explicit `persist-run --apply` invocation by a named operator — no new code should be required unless the real ledger surfaces a gap this task's tests did not anticipate.

## Related Documents

- `[[../research/LOOP_STATE_PERSISTENCE_REVIEW_001]]`
- `[[MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001]]`
- `[[../../shared_context/loops/README]]`
- `[[../../shared_context/PROJECT_STATE]]`
- `[[../../shared_context/ROADMAP]]`
