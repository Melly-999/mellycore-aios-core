# Run Queue

1. `MELLYCORE-DOCS-ACCURACY-SYNC-001` — complete (committed as `6dedbef` on `docs/mellycore-design-system-homepage-spec`).
2. `MELLYCORE-FRONTEND-SCAFFOLD-001` — complete. Output: `docs/specs/MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001.md`.
3. `MELLYCORE-FRONTEND-STATIC-SCAFFOLD-IMPLEMENTATION-001` — complete (committed as `484e5ee648ba9c7fdead7078a2b7cf1ad48c9616`). Static homepage implementation created from the approved scaffold plan.
4. `MELLYCORE-STATIC-VISUAL-QA-001` — complete (committed as `dbf296d880725bd5be7da0d9926ea1c0a3831283`). Static homepage passed visual QA at `375x812`, `768x1024`, `1024x768`, `1280x900`, and `1920x1080`. Evidence location: `C:\AI\MellyCore_Workspace\04_QA_Evidence\MELLYCORE-STATIC-VISUAL-QA-001\`.
5. `MELLYCORE-GITHUB-REMOTE-SETUP-001` — immediate next recommended task. Remote setup only; do not push unless explicitly approved in that task.
6. `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001` — deferred, not the immediate next action. Per `shared_context/BRANCH_INVENTORY_001.md`, run this from a separate clean `main` worktree rather than on the design/spec branch.
7. `MELLYCORE-CHATGPT-PROJECT-UPLOAD-001`
8. `MELLYCORE-CLAUDE-PROJECT-SETUP-001`
9. `MELLYCORE-OMNIROUTER-PROVIDER-MATRIX-001`
10. `MELLYCORE-ZED-WARP-VSCODE-AGENT-WORKSPACE-001`
11. `MELLYCORE-ROADMAP-3D-DESIGN-SYSTEM-001`
12. `MELLYCORE-WEBSITE-VISUAL-PROTOTYPE-001`

Safety posture for queued tasks:

- Preserve the static-first showcase direction.
- Do not add secrets, `.env` values, provider keys, or account identifiers.
- Do not copy GLM workspace files.
- Do not add live, broker, order, trading, buy, sell, execute, or connect-live UX.
- Do not deploy without explicit approval.
- Do not modify workflow YAML unless explicitly approved.
