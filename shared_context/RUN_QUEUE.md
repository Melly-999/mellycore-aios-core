# Run Queue

1. `MELLYCORE-DOCS-ACCURACY-SYNC-001` — complete (committed as `6dedbef` on `docs/mellycore-design-system-homepage-spec`).
2. `MELLYCORE-FRONTEND-SCAFFOLD-001` — complete. Output: `docs/specs/MELLYCORE_FRONTEND_SCAFFOLD_PLAN_001.md`.
3. `MELLYCORE-FRONTEND-STATIC-SCAFFOLD-IMPLEMENTATION-001` — complete (committed as `484e5ee648ba9c7fdead7078a2b7cf1ad48c9616`). Static homepage implementation created from the approved scaffold plan.
4. `MELLYCORE-STATIC-VISUAL-QA-001` — complete (committed as `dbf296d880725bd5be7da0d9926ea1c0a3831283`). Static homepage passed visual QA at `375x812`, `768x1024`, `1024x768`, `1280x900`, and `1920x1080`. Evidence location: `C:\AI\MellyCore_Workspace\04_QA_Evidence\MELLYCORE-STATIC-VISUAL-QA-001\`.
5. `MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001` — complete (docs-only). Output: research/product/design/schema/safety specification package for the future "MellyCore Living Context Graph" / Knowledge Graph Console feature direction. See `docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-SPEC-001.md`. Static-first, human-reviewed-ingest posture; no runtime/database/MCP implementation authorized.
6. `MELLYCORE-GITHUB-REMOTE-SETUP-001` — complete. Clean canonical remote exists as `clean-origin https://github.com/Melly-999/mellycore-aios-core.git`; the static preview decision commit was pushed to `clean-origin/main` during `MELLYCORE-STATIC-SHOWCASE-EVIDENCE-AND-AUDIT-RUN-001`.
7. `MELLYCORE-CROSS-AGENT-CONTEXT-SMOKE-001` — deferred, not the immediate next action. Per `shared_context/BRANCH_INVENTORY_001.md`, run this from a separate clean `main` worktree rather than on the design/spec branch.
8. `MELLYCORE-CHATGPT-PROJECT-UPLOAD-001`
9. `MELLYCORE-CLAUDE-PROJECT-SETUP-001`
10. `MELLYCORE-OMNIROUTER-PROVIDER-MATRIX-001`
11. `MELLYCORE-ZED-WARP-VSCODE-AGENT-WORKSPACE-001`
12. `MELLYCORE-ROADMAP-3D-DESIGN-SYSTEM-001`
13. `MELLYCORE-WEBSITE-VISUAL-PROTOTYPE-001`
14. `MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-DRAFT-001` — complete (docs/shared_context only). Added `shared_context/CONTEXT_GRAPH_FIXTURE_001.md`, `shared_context/context_graph_fixture_001.json`, and `docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-DRAFT-001.md`.
15. `MELLYCORE-README-SHOWCASE-UPDATE-001` — complete (docs-only). README polished for the canonical clean MellyCore repository; static-first, safety-first, portfolio-ready positioning.
16. `MELLYCORE-GITHUB-PAGES-OR-STATIC-PREVIEW-DECISION-001` — complete (docs-only). Recommended local static preview plus screenshot/evidence-only publishing path for now; GitHub Pages deferred.
17. `MELLYCORE-STATIC-PREVIEW-EVIDENCE-PACK-001` — complete (docs-only). Added `docs/showcase/static_preview_evidence_pack_001.md`, final showcase audit, and README/shared-context links for the local static preview evidence pack.
18. `MELLYCORE-OBSIDIAN-3D-PAGE-SPEC-001` — future docs-only spec task; no Obsidian/MCP/runtime integration authorized.
19. `MELLYCORE-CLOUD-COMPUTE-READINESS-001` — future docs-only readiness task; no provider setup, deploy, workflow YAML, or secrets authorized.
20. `MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-REVIEW-001` — complete (docs/shared_context only). Reviewed Fixture 001, confirmed graph integrity, fixed stale count references, and added `docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-REVIEW-001.md`.
21. `MELLYCORE-KNOWLEDGE-GRAPH-FIXTURE-REVIEW-PUSH-001` — separate operator-approved push task: verify and push the review commit to `clean-origin/main` if requested; no old-origin push.
22. `MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SPEC-001` — complete (docs/shared_context only). Added `docs/specs/MELLYCORE_KNOWLEDGE_GRAPH_STATIC_UI_SPEC_001.md` and `docs/tasks/MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SPEC-001.md` to define the static UI model for the existing 8-cluster, 45-node, 66-edge fixture.
23. `MELLYCORE-KNOWLEDGE-GRAPH-STATIC-UI-SPEC-REVIEW-001` — immediate next recommended task: review the static UI spec before any scaffold task; docs-only, no site implementation.

Safety posture for queued tasks:

- Preserve the static-first showcase direction.
- Do not add secrets, `.env` values, provider keys, or account identifiers.
- Do not copy GLM workspace files.
- Do not add live, broker, order, trading, buy, sell, execute, or connect-live UX.
- Do not deploy without explicit approval.
- Do not modify workflow YAML unless explicitly approved.
