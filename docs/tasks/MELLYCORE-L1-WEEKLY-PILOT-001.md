# MELLYCORE-L1-WEEKLY-PILOT-001

## Task ID

`MELLYCORE-L1-WEEKLY-PILOT-001`

## Outcome

`PASS_L1_WEEKLY_PILOT_COMMITTED`

## Scope

Run the first weekly L1 pilot for `project-health`: a second real hand-run, persisted additively through the existing guarded `persist-run` flow, proving the loop can be run repeatedly without overwriting prior evidence and that the live dashboard discovers new evidence with zero code changes.

## 1. Preflight

- Repo root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (confirmed canonical)
- Branch: `publish/mellycore-main-001`
- Starting HEAD: `4272e1b5bd91919b203fcb34515db1ba98d6c773`
- Worktree: clean (`git status --short` empty)
- Dashboard files confirmed present: `site/dashboard.html`, `site/js/dashboard.js`, `site/css/dashboard.css`, `site/data/dashboard_snapshot.json`
- Loop registry/state/runs confirmed present: `shared_context/loops/LOOP_REGISTRY.json`, `shared_context/loops/states/project-health.state.json`, one existing evidence file under `shared_context/loops/runs/project-health/`
- No stop condition triggered: repo root canonical, no unrelated dirty files, no expected-HEAD mismatch, no secret/provider requirement, nothing touched `C:\.git` or the MellyTrade workspace.

## 2. Health check performed

- Confirmed `shared_context/loops/KILL_SWITCH` absent.
- `py -3.9 scripts/validate_project_state.py` → PASS
- `py -3.9 -m scripts.loop_ops validate` → PASS, 9 loops, 0 findings
- `py -3.9 -m scripts.loop_ops audit --json` baseline → `configured: 9, validated: 9, exercised: 1, human_approved: 0, production_enabled: 0`
- Read `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`, `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`, `README.md` (within `project-health`'s declared `read_scope`)
- No blocker found. One minor, non-blocking finding, a repeat of the one surfaced by the first registered run: `PROJECT_STATE.md`'s "Current HEAD" line was stale (still showed `708590b`). Corrected in this task's own documentation sync, not by the hand-run itself.

## 3. Ledger and persistence

- Run ID: `project-health--20260717T011848Z--6b2e45cf7c51`
- Ledger built by hand from the health check above, following `shared_context/loops/RUN_LEDGER_SCHEMA.json` and `RUN_LEDGER.example.json`.
- First `persist-run` attempt (dry-run) hit `FUTURE_TIMESTAMP`: an initial `completed_at` guess landed a few seconds after the tool's own wall clock at validation time. Corrected by re-checking `date -u` immediately before building the final ledger and using a `finished_at`/`completed_at` at or before that instant. This is exactly the kind of refusal the persistence contract is designed to produce — no evidence was written on the failed attempt.
- Dry-run (no `--apply`): `guard_decision: CONTINUE`, `evidence_path` pointed at a new, non-colliding filename, `proposed_state.run_history` showed the new run correctly **appended after** the existing one, zero warnings.
- Apply: `py -3.9 -m scripts.loop_ops persist-run --ledger <path> --apply --operator-approval-id MELLYCORE-L1-WEEKLY-PILOT-001-APPROVED --expected-head 4272e1b5bd91919b203fcb34515db1ba98d6c773 --json` → `evidence_written: true`, `evidence_status: "absent"` (new file, not a duplicate), `guard_decision: CONTINUE`.

## 4. Token contract

- The single iteration's `tokens` object: `{"input": null, "output": null, "total": null, "measured": false}` — real token spend was not measurable in this execution environment, recorded honestly, never faked as `0`.
- `daily_tokens_used: null` for the same reason.
- Guard correctly classified `per_run_budget` and `daily_budget` as `unenforceable`, not `pass`, matching the corrected contract in `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md` Section 5.

## 5. Immutability and state verification

- `git diff --stat -- shared_context/loops/runs/project-health/project-health--20260715T195201Z--03d7b0224ae0.json` → empty. The first run's evidence is byte-unchanged.
- New evidence file exists at `shared_context/loops/runs/project-health/project-health--20260717T011848Z--6b2e45cf7c51.json`.
- `shared_context/loops/states/project-health.state.json` rebuilt with `run_history` containing **both** runs, in order, each pointing at its own `ledger_ref`.
- Post-persist `py -3.9 -m scripts.loop_ops audit --json` → summary unchanged: `configured: 9, validated: 9, exercised: 1, human_approved: 0, production_enabled: 0`. `exercised` counts loops with at least one real run, not run count, so this is the expected, correct result — not a regression.

## 6. Dashboard discovery smoke test

- Started a local static server: `python -m http.server 8792 --bind 127.0.0.1` from the repo root.
- `curl http://127.0.0.1:8792/shared_context/loops/runs/project-health/` → directory listing includes both evidence filenames.
- Confirmed lexicographic sort of the two filenames places the new run last (`20260717...` > `20260715...`), matching exactly what `site/js/dashboard.js`'s `findLatestEvidenceFile()` does with `Array.sort()` + take-last.
- `curl` the new evidence file directly and parsed it: `ledger.run_id`, `ledger.outcome`, `guard_evaluation.decision`, `guard_evaluation.checks.per_run_budget`, and `ledger.iterations[0].tokens.total` all present in the exact shape `renderEvidence()` in `dashboard.js` already reads. No dashboard code change was needed or made.
- `curl -o /dev/null -w "%{http_code}"` on `site/dashboard.html` → `200`.

## 7. Validation

| Command | Result |
| --- | --- |
| `py -3.9 -m scripts.loop_ops validate` | PASS, 9 loops, 0 findings |
| `py -3.9 -m unittest discover -s tests -p "test_loop_ops*.py"` | 150 tests, OK (no regression) |
| Dashboard directory-discovery smoke test (curl-based) | New run discoverable, correct shape, no code change needed |

## 8. Files changed

- `shared_context/loops/runs/project-health/project-health--20260717T011848Z--6b2e45cf7c51.json` (new, immutable evidence)
- `shared_context/loops/states/project-health.state.json` (rebuilt, both runs listed)
- `shared_context/RUN_QUEUE.md` (entry 45 added)
- `shared_context/PROJECT_STATE.md` (stale HEAD line corrected; new "Weekly L1 Pilot" section added)
- `docs/tasks/MELLYCORE-L1-WEEKLY-PILOT-001.md` (this file)

No dashboard code, loop registry, schema, or CLI file was modified. No `.env`, secret, or credential file was read or written. No scheduler was installed.

## 9. Safety posture confirmed

- Lifecycle stayed `REPORT_ONLY` throughout; `human_approval.granted` stayed `false`; `production_enabled` stayed `0`.
- No write scope granted to any loop; no repository mutation from the loop itself (`repository_mutation_count: 0`, `remote_action_count: 0` in the ledger).
- No provider/network/MCP call. No secrets read or written.
- No scheduler installed — this remains a separate, explicit, human-invoked run each time.
- No push. No destructive git command. Nothing touched `C:\.git` or the MellyTrade workspace.
