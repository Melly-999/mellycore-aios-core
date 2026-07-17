# Project State

Project name: MellyCore AIOS

Status: static homepage scaffold implemented (`site/`, visual-QA-passed) and a safety-first, report-only Loop Operations Foundation added as the project's first tooling capability; the reviewed persistence and token-semantics contract is now implemented and has recorded its first real, honestly-derived exercised run; still local-only, not published, no runtime

Local repo path: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`

Current branch: `publish/mellycore-main-001`

Current HEAD (before this task's commit): `4272e1b` (`feat(aios): add live dashboard preview`), on top of `87077b9` (`chore(aios): register first project health run`), on top of `708590b` (`feat(aios): add guarded loop evidence persistence`)

MellyCore AIOS is separate from MellyTrade. Do not import MellyTrade runtime code, broker credentials, execution routes, or trading UI.

The GLM/Z.ai workspace at `C:\AI\MellyCore_Workspace\03_Assets\glm_workspace_reference` is reference only. Do not use it as the main repo, copy it wholesale, import `.git`, import `.env`, import `db/custom.db`, or copy local runtime state.

Current visual direction: black-space background, purple/blue neon, orbital cube, HUD panels, glassmorphism, star field, roadmap orbit map, model-router constellation, OmniRouter provider hub, and cinematic command center website. The static `site/` scaffold (pure HTML/CSS, no JS, no packages) is visual-QA-passed across mobile/tablet/desktop/wide viewports and includes a Living Context Graph preview section.

## Loop Operations Foundation

Completed as the project's first tooling (non-site) capability: a machine-readable loop registry (9 loops: 6 `REPORT_ONLY`, 3 `DISABLED`), state/ledger JSON-schema contracts, a standard-library-only read-only `scripts/loop_ops/` CLI (`validate`, `audit`, `guard`, `estimate-cost`, `worktree-audit`, `redact-check`), a deterministic circuit breaker, and canonical loop skills under `agent_prompts/loops/`. Phase 1 is report-only; no loop has write scope.

**First external `project-health` run** (`MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001`): outcome `EXERCISED_EXTERNALLY_NOT_REGISTERED`. A real, schema-valid ledger was produced outside the repository (per that task's instructions) and processed by the deterministic guard, which returned `CONTINUE`. `audit --json` was byte-identical before and after, because the audit only recognizes evidence persisted under `shared_context/loops/states/`, which that task was forbidden to write to. The run surfaced a real defect: unmeasured tokens were recorded as numeric `0`, indistinguishable from a measured zero-cost run, which let a run with unmeasured cost report `per_run_budget: pass`.

**Persistence review** (`MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001`, docs-only): reviewed and specified the safe persistence contract and the token-semantics correction later implemented below. See `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md`.

**Persistence and token-contract implementation** (`MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001`): the reviewed contract is now implemented in code, together, as recommended:

- **Token semantics corrected** (`scripts/loop_ops/models.py`, `scripts/loop_ops/registry.py`, `scripts/loop_ops/guard.py`, `shared_context/loops/RUN_LEDGER_SCHEMA.json`): an unmeasured iteration must never carry a numeric `total`, not even zero — rejected at parse time. A measured iteration requires a real non-negative integer. Any unmeasured iteration in a run now makes that run's `per_run_budget` check `unenforceable`, never a partial pass computed only over the measured iterations.
- **`persist-run` CLI subcommand** (`scripts/loop_ops/persist.py`, new module): `py -3.9 -m scripts.loop_ops persist-run --ledger <path>` validates a candidate ledger and writes nothing by default. Persisting for real requires `--apply`, a non-empty `--operator-approval-id`, and an `--expected-head` matching the repository's actual current HEAD. Enforces write-once immutable evidence (identical bytes may recover an interrupted state update; different bytes are always refused), path/symlink/case-collision safety, redaction gate, timestamp validation, lifecycle-transition legality, and a Phase 1 rule that `repository_mutation_count` and `remote_action_count` must be zero.
- **Audit closes D4** (`scripts/loop_ops/readiness.py`): a `run_history` entry now counts as `exercised` only when its `ledger_ref` resolves to a real, independently-validated evidence file under `runs/<loop-id>/` whose content is internally consistent with the state's own claim — an orphan claim in state, with no backing evidence, no longer counts.
- 21 new/updated automated tests across `tests/test_loop_ops_guard.py`, `tests/test_loop_ops_tools.py`, and the new `tests/test_loop_ops_persist.py` (150 tests total, all passing).

**First registered `project-health` run** (`MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001`): the loop was hand-run for real (validators read, shared_context state read, no blocker found), its ledger built honestly with token usage marked unmeasured (this execution environment cannot measure real token spend, so `tokens.total: null`, never `0`), validated in dry-run, then persisted for real via `persist-run --apply` with operator approval `MELLYCORE-PROJECT-HEALTH-REGISTERED-RUN-001-APPROVED` and `--expected-head` matching the actual current HEAD. Evidence: `shared_context/loops/runs/project-health/project-health--20260715T195201Z--03d7b0224ae0.json`. State: `shared_context/loops/states/project-health.state.json`, rebuilt by `persist-run` itself. A repeat `--apply` with the identical ledger was confirmed idempotent: `evidence_status: "identical"`, byte-unchanged, no duplicate `run_history` entry. `per_run_budget` and `daily_budget` correctly report `unenforceable` (the run has an unmeasured iteration), not a false pass. `human_approval.granted` stays `false`; lifecycle stays `REPORT_ONLY`.

**Current audit state:** `configured: 9`, `validated: 9`, `exercised: 1` (`project-health` only), `human_approved: 0`, `production_enabled: 0`. This is the first loop in this repository with real persisted run evidence. Every other loop remains unexercised. Do not describe the Loop Operations Foundation as operational or unattended-ready — one exercised report-only loop is not production readiness.

## Live Dashboard Preview

Added a local, interactive dashboard preview (`MELLYCORE-AIOS-LIVE-DASHBOARD-PREVIEW-001`) at `site/dashboard.html`: a cinematic cockpit UI with Overview/Loops/Models/Evidence/Roadmap/Live tabs. It reads real local files live at page load (`ROADMAP.md`, `RUN_QUEUE.md`, `LOOP_REGISTRY.json`, `project-health.state.json`, the latest persisted `project-health` run ledger, `MODEL_ROUTING.md`, `SAFETY_CONTRACT.md`) plus one frozen snapshot of real CLI output (`site/data/dashboard_snapshot.json`, from `validate`/`audit --json`/the test suite). The Live tab's event stream and its pause/resume control are mock data, explicitly labeled `[MOCK]` in the UI — there is no scheduler, backend, or provider connection. This is the only page in `site/` that uses JavaScript; the original static homepage (`site/index.html`, pure HTML/CSS, no JS, no packages) is unchanged in scope. Any local server used to preview it must still bind only to `127.0.0.1`, per the rule below.

## Weekly L1 Pilot

The first weekly L1 pilot run (`MELLYCORE-L1-WEEKLY-PILOT-001`) is complete: `project-health` was hand-run and persisted a second time via `persist-run --apply`, additively. New evidence: `shared_context/loops/runs/project-health/project-health--20260717T011848Z--6b2e45cf7c51.json`. The first run's evidence file is untouched (write-once immutability held). `shared_context/loops/states/project-health.state.json` now lists both runs in `run_history`. `audit --json` still reports `exercised: 1` for `project-health` (the tier counts loops, not run count — this is expected). The live dashboard (`site/dashboard.html`) picked up the new run automatically with no code change, since its Evidence tab discovers the latest run by listing the `runs/project-health/` directory rather than hardcoding a filename. There is still no scheduler; each weekly run remains a separate, explicit, human-invoked action.

## Safety boundaries (current)

No remote contact, fetch, pull, or push from any automated task without explicit operator approval; no PR or merge; no deployment; no provider API keys or secrets in the repository; no MCP; no scheduler; no live trading capability; no changes to MellyTrade; no destructive git actions without explicit approval. Any local server started for preview purposes must bind only to `127.0.0.1` and must never be exposed to LAN or the internet.

## Localhost state

The static `site/` scaffold can be served locally with `py -3.9 -m http.server 4173 --bind 127.0.0.1 --directory site` (Python standard library only, no dependencies). See `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md` for the full quickstart.

Next tasks:

1. A weekly L1 pilot: run a report-only loop (`project-health` or another enabled L1 loop) on a recurring cadence and persist each run for real, still with no write scope for any loop. Remains a separate, not-yet-started task.
2. `MELLYCORE-GITHUB-REMOTE-SETUP-001` — prepare GitHub remote setup without pushing; any push requires explicit operator approval.
3. `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001` — deferred; run from a clean `main` worktree per `shared_context/BRANCH_INVENTORY_001.md`.
4. Package shared context files for ChatGPT Project upload.

Filename convention note: `docs/design/` and `docs/specs/` use underscore-separated filenames for major spec documents (e.g. `MELLYCORE_HOMEPAGE_SPEC_001.md`); `docs/tasks/` uses hyphenated task IDs for task reports (e.g. `MELLYCORE-HOMEPAGE-SPEC-001.md`), matching the task-ID convention used across the project. This split is intentional, not a broken reference.

