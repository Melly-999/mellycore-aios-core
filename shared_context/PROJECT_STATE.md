# Project State

Project name: MellyCore AIOS

Status: static homepage scaffold implemented (`site/`, commit `484e5ee`, operator-approved) and visual-QA-passed (`MELLYCORE-STATIC-VISUAL-QA-001`); still local-only, not published, no runtime

Local repo path: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`

Current branch: `docs/mellycore-design-system-homepage-spec`

HEAD prior to `MELLYCORE-DOCS-ACCURACY-SYNC-001`: `062135cd19d517f772c5ca4f289ecff516872601`

MellyCore AIOS is separate from MellyTrade. Do not import MellyTrade runtime code, broker credentials, execution routes, or trading UI.

The GLM/Z.ai workspace at `C:\AI\MellyCore_Workspace\03_Assets\glm_workspace_reference` is reference only. Do not use it as the main repo, copy it wholesale, import `.git`, import `.env`, import `db/custom.db`, or copy local runtime state.

Current visual direction: black-space background, purple/blue neon, orbital cube, HUD panels, glassmorphism, star field, roadmap orbit map, model-router constellation, OmniRouter provider hub, and cinematic command center website.

Design/spec gate status: `docs/design/MELLYCORE_DESIGN_SYSTEM_001.md`, `docs/specs/MELLYCORE_HOMEPAGE_SPEC_001.md`, and `docs/specs/MELLYCORE_UI_SECTIONS.md` are safety-sound (confirmed by `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` and re-confirmed by `MELLYCORE-DOCS-INTEGRATION-REVIEW-EVIDENCE-HARDENING-001`) but required an accuracy sync — a false "complete" claim about cross-agent smoke in the homepage spec, and stale handoff files — before the frontend scaffold gate could open. `MELLYCORE-DOCS-ACCURACY-SYNC-001` applies that fix. Static-first and safety-first posture is preserved throughout; no runtime, secrets, or GLM copy were introduced.

Next tasks:

1. `MELLYCORE-GITHUB-REMOTE-SETUP-001` — prepare GitHub remote setup without pushing; any push requires explicit operator approval.
2. `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001` — deferred; run from a clean `main` worktree per `shared_context/BRANCH_INVENTORY_001.md`.
3. Package shared context files for ChatGPT Project upload.

Filename convention note: `docs/design/` and `docs/specs/` use underscore-separated filenames for major spec documents (e.g. `MELLYCORE_HOMEPAGE_SPEC_001.md`); `docs/tasks/` uses hyphenated task IDs for task reports (e.g. `MELLYCORE-HOMEPAGE-SPEC-001.md`), matching the task-ID convention used across the project. This split is intentional, not a broken reference.

