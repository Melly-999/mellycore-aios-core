# Project State

Project name: MellyCore AIOS

Status: static homepage scaffold implemented (`site/`, visual-QA-passed) and a safety-first, report-only Loop Operations Foundation added as the project's first tooling capability; the foundation has been hand-run once externally and its persistence contract reviewed and specified (not implemented); still local-only, not published, no runtime

Local repo path: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`

Current branch: `publish/mellycore-main-001`

Current HEAD: `27ccd9e` (`docs(aios): define loop evidence persistence contract`), on top of `6c67fc5bf28999882e26a45d12cc7eab639228e1` (`feat(aios): add safety-first loop operations foundation`)

MellyCore AIOS is separate from MellyTrade. Do not import MellyTrade runtime code, broker credentials, execution routes, or trading UI.

The GLM/Z.ai workspace at `C:\AI\MellyCore_Workspace\03_Assets\glm_workspace_reference` is reference only. Do not use it as the main repo, copy it wholesale, import `.git`, import `.env`, import `db/custom.db`, or copy local runtime state.

Current visual direction: black-space background, purple/blue neon, orbital cube, HUD panels, glassmorphism, star field, roadmap orbit map, model-router constellation, OmniRouter provider hub, and cinematic command center website. The static `site/` scaffold (pure HTML/CSS, no JS, no packages) is visual-QA-passed across mobile/tablet/desktop/wide viewports and includes a Living Context Graph preview section.

## Loop Operations Foundation

Completed as the project's first tooling (non-site) capability: a machine-readable loop registry (9 loops: 6 `REPORT_ONLY`, 3 `DISABLED`), state/ledger JSON-schema contracts, a standard-library-only read-only `scripts/loop_ops/` CLI (`validate`, `audit`, `guard`, `estimate-cost`, `worktree-audit`, `redact-check`), a deterministic circuit breaker, and canonical loop skills under `agent_prompts/loops/`. Phase 1 is report-only; no loop has write scope.

**First external `project-health` run** (`MELLYCORE-LOOP-REPORT-ONLY-DRY-RUN-001`): outcome `EXERCISED_EXTERNALLY_NOT_REGISTERED`. A real, schema-valid ledger was produced outside the repository (per that task's instructions) and processed by the deterministic guard, which returned `CONTINUE`. `audit --json` was byte-identical before and after, because the audit only recognizes evidence persisted under `shared_context/loops/states/`, which that task was forbidden to write to. The run surfaced a real defect: unmeasured tokens were recorded as numeric `0`, indistinguishable from a measured zero-cost run, which let a run with unmeasured cost report `per_run_budget: pass`.

**Persistence review** (`MELLYCORE-LOOP-STATE-PERSISTENCE-REVIEW-001`, docs-only, this task): reviewed and specified — but did not implement — a safe persistence contract: immutable run evidence at `shared_context/loops/runs/<loop-id>/<run-id>.json` (not yet created), derived mutable state at `shared_context/loops/states/<loop-id>.state.json` (schema unchanged), and purely-computed audit tiers (unchanged). Also specified the token-semantics correction (unmeasured must be `null`/absent, never numeric `0`; any unmeasured iteration must make a run's per-run budget `unenforceable`). See `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md`.

**Current audit state (unchanged by any of the above):** `configured: 9`, `validated: 9`, `exercised: 0`, `human_approved: 0`, `production_enabled: 0`. No loop has real persisted run evidence. Do not describe the Loop Operations Foundation as operational or unattended-ready.

## Safety boundaries (current)

No remote contact, fetch, pull, or push from any automated task without explicit operator approval; no PR or merge; no deployment; no provider API keys or secrets in the repository; no MCP; no scheduler; no live trading capability; no changes to MellyTrade; no destructive git actions without explicit approval. Any local server started for preview purposes must bind only to `127.0.0.1` and must never be exposed to LAN or the internet.

## Localhost state

The static `site/` scaffold can be served locally with `py -3.9 -m http.server 4173 --bind 127.0.0.1 --directory site` (Python standard library only, no dependencies). See `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md` for the full quickstart.

Next tasks:

1. `MELLYCORE-LOOP-PERSISTENCE-AND-TOKEN-CONTRACT-IMPLEMENTATION-001` — implement, together, the token-semantics correction and the `runs/`-based persistence path plus a `persist-run` CLI subcommand, per `docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md`.
2. `MELLYCORE-GITHUB-REMOTE-SETUP-001` — prepare GitHub remote setup without pushing; any push requires explicit operator approval.
3. `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001` — deferred; run from a clean `main` worktree per `shared_context/BRANCH_INVENTORY_001.md`.
4. Package shared context files for ChatGPT Project upload.

Filename convention note: `docs/design/` and `docs/specs/` use underscore-separated filenames for major spec documents (e.g. `MELLYCORE_HOMEPAGE_SPEC_001.md`); `docs/tasks/` uses hyphenated task IDs for task reports (e.g. `MELLYCORE-HOMEPAGE-SPEC-001.md`), matching the task-ID convention used across the project. This split is intentional, not a broken reference.

