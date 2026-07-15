# MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001

## Task ID

`MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001`

## Outcome

`PASS_PROJECT_HEALTH_REGISTERED_RUN_COMMITTED`

## Scope

Execute the first real, registered `project-health` loop run and persist its evidence using the guarded persistence contract implemented by `MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001`, proving the complete operational path end to end: real hand-run, valid ledger, dry-run gate, explicitly approved apply, immutable evidence, rebuilt state, and honest audit/readiness verification.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `708590b90181f43dce97cd0a27e7567d8dab1779` (prefix `708590b` confirmed)
- Worktree: clean (`git status --short` empty)
- Remotes: `clean-origin` and `origin`, both unchanged, neither contacted
- Baseline commands, all matching expectations exactly:

| Command | Exit | Result |
| --- | --- | --- |
| `py -3.9 -m compileall -q scripts/loop_ops tests` | 0 | OK |
| `py -3.9 scripts/validate_project_state.py` | 0 | PASS |
| `py -3.9 -m scripts.loop_ops validate` | 0 | PASS — 9 loops, 0 findings |
| `py -3.9 -m scripts.loop_ops audit --json` | 0 | `configured: 9, validated: 9, exercised: 0, human_approved: 0, production_enabled: 0` |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 0 | OK — 150 tests |
| `git diff --check` | 0 | PASS |

## 2. Registered Loop Contract

Extracted from `shared_context/loops/LOOP_REGISTRY.json`'s `project-health` entry:

- **Loop ID:** `project-health`
- **Lifecycle:** `REPORT_ONLY`, level `L1`, `trigger_type: manual`, `allowed_write_scope: []`
- **Read scope:** `shared_context/**`, `docs/**`, `scripts/**`, `README.md`
- **Forbidden paths:** `.env`, `.env.*`, `secrets/**`, `credentials/**`, `auth/**`, `payments/**`, `billing/**`, `migrations/**`, `infra/production/**`, `.github/workflows/**`, `shared_context/PROVIDER_SETUP.md`, `**/provider_keys*`, `**/MellyTrade/**`, `**/mellytrade/**`
- **Budgets:** `max_attempts: 3`, `stagnation_threshold: 2`, `no_progress_threshold: 2`, `per_run_token_budget: 60000`, `daily_token_budget: 180000`
- **Human gate:** `report_reviewed_by_operator`; `verifier_required: false`
- **Success condition:** "A health report is produced that names the current branch, the validator outcome, and any open blocker, with every claim traceable to a file that was actually read."
- **Persistence requirements** (from `scripts/loop_ops/persist.py`, per `MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001`): ledger must additionally carry `repository`, `branch`, `head_sha`, `completed_at`, `outcome`, `repository_mutation_count: 0`, `remote_action_count: 0` (Phase 1); `run_id` must match `^[a-z0-9][a-z0-9-]{0,63}--[0-9]{8}T[0-9]{6}Z--[0-9a-f]{12}$` and begin with the loop's own id; evidence path `shared_context/loops/runs/project-health/<run-id>.json`; state path `shared_context/loops/states/project-health.state.json`.
- **CLI:** `py -3.9 -m scripts.loop_ops persist-run --ledger <path> [--apply --operator-approval-id <id> --expected-head <sha>] [--json]`.

No file listed above was invented or guessed at — all were read directly before the ledger was built.

## 3. Real `project-health` Execution

One iteration, real timestamps, all within the loop's declared `read_scope`:

- **Started:** `2026-07-15T19:52:33Z`
- **Completed:** `2026-07-15T19:53:11Z`
- `py -3.9 scripts/validate_project_state.py` → PASS, exit 0
- `py -3.9 -m scripts.loop_ops validate` → PASS, 9 loops, 0 findings, exit 0
- `py -3.9 -m scripts.loop_ops audit --json` → confirmed baseline `configured: 9, validated: 9, exercised: 0, human_approved: 0, production_enabled: 0`
- Read `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`, `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`, `README.md`

**Finding (non-blocking):** `PROJECT_STATE.md`'s "Current HEAD" line described the implementation commit only by message, not by its short SHA (`708590b`). Not a validator failure and not treated as a blocker; corrected in this task's own Phase 7 documentation sync (see Section 11).

**No blocking issue was found.** The task-level baseline/final validation suite (full `unittest discover`, `compileall`, `git diff --check`) was run separately by the operator per this task's own Phase 0/Phase 6 requirements — those commands necessarily touch `tests/`, which is outside `project-health`'s own declared `read_scope`; that operator-level validation is distinct from, and not attributed to, the loop's own scope-restricted hand-run above.

**Distinction from the previous dry run:** `MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001` also hand-ran `project-health`, but its ledger was produced outside the repository and never persisted (`EXERCISED_EXTERNALLY_NOT_REGISTERED`). This task's run and ledger are new, real, produced inside this task, and persisted for the first time.

## 4. Token Contract Result

Real token usage was not measurable in this execution environment. The single iteration's `tokens` object is `{"input": null, "output": null, "total": null, "measured": false}` — never a fabricated or estimated number, and never `0` as a stand-in for "unavailable." As a direct, honest consequence:

- `guard.evaluate` classified `per_run_budget: "unenforceable"` and `daily_budget: "unenforceable"` — not `"pass"`.
- `guard_decision.decision: "CONTINUE"` (no limit reached; unenforceable is not a failure).

This was verified independently three times: via `registry.parse_ledger` + `guard.evaluate_or_block` in a Python snippet, via `py -3.9 -m scripts.loop_ops guard --ledger <path> --json`, and again inside the persisted evidence's own `guard_evaluation` block after apply — all three agree.

## 5. Run Ledger

- **Run ID:** `project-health--20260715T195201Z--03d7b0224ae0` (matches the canonical pattern; the loop-id segment matches `loop_id`)
- **Temporary input location:** the ledger was built at `C:\Users\highe\AppData\Local\Temp\project-health-run-ledger.json`, outside any repository evidence directory, and was never placed manually into `shared_context/loops/runs/`
- **Ledger integrity confirmed:** valid JSON; passes `registry.parse_ledger` (schema version, required fields, strictly-increasing iteration index, corrected token contract); `repository`, `branch`, `head_sha`, `completed_at`, `outcome`, `repository_mutation_count: 0`, `remote_action_count: 0` all present and valid per `persist.validate_ledger_for_persistence`; `status_before`/`status_after` both `REPORT_ONLY` (no lifecycle change); no secret-shaped content (confirmed by the redaction gate during dry-run)

## 6. Persistence Dry-Run

`py -3.9 -m scripts.loop_ops persist-run --ledger <path> --json` (no `--apply`):

- Proposed evidence path: `shared_context/loops/runs/project-health/project-health--20260715T195201Z--03d7b0224ae0.json`
- Proposed state path: `shared_context/loops/states/project-health.state.json`
- Guard decision recomputed: `CONTINUE`
- `warnings: []` — the ledger's declared `repository`/`branch`/`head_sha` matched the actual repository identity exactly, so no mismatch note was recorded
- **Confirmed nothing was written:** `git status --short` was empty both before and after; `shared_context/loops/runs/` and the state file did not exist after the dry-run; `audit --json` was re-run and still reported `exercised: 0`

## 7. Persistence Apply

- **Operator approval ID:** `MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001-APPROVED`
- **Expected HEAD:** `708590b90181f43dce97cd0a27e7567d8dab1779` (the actual current HEAD at the moment of the call — captured via `git rev-parse HEAD` in the same command, not hand-typed)
- **Same validated ledger** used in the dry-run; not regenerated or mutated between dry-run and apply
- **Result:** `evidence_written: true`, `evidence_status: "absent"` (fresh write); exactly one evidence file created; state rebuilt with exactly one `run_history` entry pointing to it; no temp files (`*.tmp-*`) remained afterward
- **Atomicity:** evidence file confirmed byte-consistent with the validated ledger; state's `ledger_ref` matches the evidence path exactly; guard decision and exit code recorded inside the persisted evidence, computed at persist time, not trusted from the input
- **Identical-resubmission recovery check:** the identical `--apply` command was re-run with the same ledger, approval ID, and expected-head. Result: `evidence_status: "identical"`, `evidence_written: false`. SHA-256 of the evidence file was confirmed byte-for-byte unchanged (`367c0eee7225c5ba7e7f7b8899df67dd8ca923f12a674484e25a4ee957af2c6e` before and after). `run_history` still contained exactly one entry — no duplication. The differing-bytes-overwrite rejection path was **not** re-tested against this real evidence (per this task's own instruction); that path is covered by `tests/test_loop_ops_persist.py::ApplyTests::test_duplicate_conflicting_run_id_is_refused`.

## 8. Audit And Readiness Result

| | Before | After |
| --- | --- | --- |
| `configured` | 9 | 9 |
| `validated` | 9 | 9 |
| `exercised` | 0 | **1** (`project-health` only) |
| `human_approved` | 0 | 0 |
| `production_enabled` | 0 | 0 |

`project-health`'s `highest_earned_tier` is now `"exercised"`, with evidence text `"1 recorded run(s) in shared_context/loops/states/project-health.state.json"`. Every other loop's tiers are unchanged. `human_approved` and `production_enabled` were never set by this run — both remain strictly operator-only facts, confirmed unset in both the evidence and the rebuilt state.

## 9. Tests And Validators

Run after persistence:

| Command | Exit | Result |
| --- | --- | --- |
| `py -3.9 scripts/validate_project_state.py` | 0 | PASS |
| `py -3.9 -m scripts.loop_ops validate` | 0 | PASS — 9 loops, 0 findings |
| `py -3.9 -m scripts.loop_ops audit --json` | 0 | `exercised: 1`, `production_enabled: 0` (see above) |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` (first run) | 1 | **1 failure**: `ShippedRegistryAuditTests.test_no_shipped_loop_is_production_enabled` asserted `exercised == 0` against the real shipped registry — the exact fact this task was designed to change. Not a source-code defect; see Section 11. |
| `tests/test_loop_ops_tools.py` fix applied (narrowed the assertion to its actual named invariant, `production_enabled == 0`) | — | — |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` (re-run) | 0 | OK — 150 tests |
| `py -3.9 -m unittest tests.test_loop_ops_persist` | 0 | OK — 37 tests |
| `py -3.9 -m compileall -q scripts/loop_ops tests` | 0 | OK |
| `git diff --check` | 0 | PASS |

## 10. Real Repository State Confirmation

- Exactly one file under `shared_context/loops/runs/`: `project-health/project-health--20260715T195201Z--03d7b0224ae0.json`.
- Exactly one state file under `shared_context/loops/states/` beyond `README.md`: `project-health.state.json`.
- No other loop's `runs/` or state file was created.
- No temp/partial files (`*.tmp-*`) remained under either directory.
- `status: "REPORT_ONLY"` in both the registry entry and the rebuilt state.
- `human_approval.granted: false` in the rebuilt state.
- No network, provider, or scheduler behavior was introduced; the only external process invoked was the local, read-only `git rev-parse` used to read the current branch/HEAD.

## 11. Files Changed

- `shared_context/loops/runs/project-health/project-health--20260715T195201Z--03d7b0224ae0.json` (new) — the immutable run evidence
- `shared_context/loops/states/project-health.state.json` (new) — the rebuilt loop state, referencing the evidence above
- `tests/test_loop_ops_tools.py` — narrowed `ShippedRegistryAuditTests.test_no_shipped_loop_is_production_enabled` to assert only its named invariant (`production_enabled == 0`); it no longer asserts `exercised == 0`, since this task's entire purpose was to make that honestly false for the first time. This is a test-assumption update, not a source-code defect — nothing in `scripts/loop_ops/` was touched.
- `shared_context/PROJECT_STATE.md` — corrected the stale "Current HEAD" line (Section 3 finding) and recorded the real registered run, evidence path, state path, and the new audit numbers
- `shared_context/ROADMAP.md` — Milestone A: marked the registered run complete, moved the weekly L1 pilot to "next"
- `shared_context/RUN_QUEUE.md` — marked entry 42 complete with the real run's details; queued the weekly L1 pilot as entry 43
- `shared_context/AGENT_HANDOFF.md` — new handoff entry for this task
- `shared_context/loops/README.md` — updated the "no loop has ever produced persisted evidence" line to reflect the one real exercised loop
- `docs/tasks/MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001.md` (new, this file)

## 12. Safety Confirmation

- Lifecycle remains `REPORT_ONLY` for `project-health`, confirmed in both the registry and the rebuilt state.
- `production_enabled: 0`, confirmed in `audit --json` both before and after, and structurally blocked regardless (Phase 1).
- No provider, network, or scheduler integration was added or invoked; no automation was installed; this remains a single, explicit, human-invoked run.
- No secrets, no `.env` value, anywhere in the ledger, evidence, or state — confirmed by the redaction gate during dry-run (zero findings) and by manual review of the persisted files.
- No frontend, `site/`, or MellyTrade file was touched.
- No deploy, no push, no PR, no merge. `git status --short` at task end shows only the intended local changes; nothing was sent to any remote.

## 13. Local Commit

One local commit, created after all validation passed:

```
chore(aios): register first project health run
```

Not pushed.

## 14. Remaining Work

The weekly L1 pilot (running a report-only loop on a recurring cadence and persisting each real run) remains a separate, not-yet-started task. This task did not begin it, configure a scheduler, or install any automation — each future run still requires its own explicit hand-run and its own explicit `persist-run --apply`.

## 15. Limitations And Honest Notes

- Real token usage could not be measured in this execution environment; the run's single iteration is honestly recorded as unmeasured, and `per_run_budget`/`daily_budget` are correctly `unenforceable` as a direct consequence — not artificially forced to `unenforceable`, and not misreported as `pass`.
- The differing-bytes overwrite-rejection path of `persist-run --apply` was intentionally not re-tested against this real, now-persisted evidence, per this task's own instruction to avoid risking the canonical artifact; that behavior is covered by existing automated tests instead.
- One pre-existing test's assumption (`exercised == 0` against the real shipped registry) was invalidated by design, since making that fact honestly false was this task's entire purpose; it was narrowed rather than deleted, so it continues to protect the invariant it was actually meant to protect (`production_enabled == 0`).
- This task registers one run for one loop. It does not establish a schedule, a recurring habit, or any claim of ongoing operational readiness beyond what the honest audit numbers above state.

## Related Documents

- `[[../research/LOOP_STATE_PERSISTENCE_REVIEW_001]]`
- `[[MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001]]`
- `[[../../shared_context/loops/README]]`
- `[[../../shared_context/PROJECT_STATE]]`
- `[[../../shared_context/ROADMAP]]`
