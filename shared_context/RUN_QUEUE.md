# Run Queue

This file contains actionable sequencing and gates. Completed-task detail belongs
in `docs/tasks/` and Git history, not duplicated here.

## Vercel Static Root — Accepted, Verified, Published, State-Synced, Merged

`https://mellycore-aios-core.vercel.app` is the accepted production static
showcase host. The static-root fetch defect is fixed, reviewed `PASS`, and
merged into canonical `main` via PR #23 (merge commit
`177128cfc6513090b45491d16e9f0c594451636d`). Production redeploy smoke
passed and post-deploy verification (including a screenshot artifact) is
recorded in `docs/tasks/MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001.md`,
merged into canonical `main` via PR #24 (merge commit
`be3ead9b1b27a80bb6029acb7acba0c98c6ba4c6`). The deployment-state
synchronization itself (`MELLYCORE-DEPLOYMENT-STATE-SYNC-001`), after a
documentation-consistency remediation
(`MELLYCORE-DEPLOYMENT-STATE-SYNC-REMEDIATION-001`), merged into canonical
`main` via PR #25 (merge commit
`ca1f762a0cdd43b80282b885bfd7885d2740288a`, 2026-07-24T13:51:58Z). This
deployment/verification/state-sync chain is complete; no deployment-state
remediation or merge-retry task remains pending. GitHub Pages remains
containment/maintenance only, not a product host.

The Control Plane specification task,
`MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-001`, completed authoring
and publication on branch
`docs/mellycore-omnirouter-inspired-control-plane-spec-001` in
[PR #27](https://github.com/Melly-999/mellycore-aios-core/pull/27). Its initial
review identified two specification blockers; targeted remediation commit
`ea662ab…` resolved them and corrected the status-dimension count. Publication,
initial review, targeted remediation, remediation publication, and targeted
re-review are complete. The targeted re-review outcome was
`PASS_WITH_NOTES_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC_REMEDIATION_REVIEW`,
with no blocking finding and all required checks passing.

At the time of this update, PR #27 was open, reviewed, remediation-complete,
and merge-ready, but not yet merged or canonical on `main`.

**Current task-local operation (at the time of this update):**
`MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-MERGE-001` — perform final
acceptance gates and, only if they pass, merge PR #27 normally. The durable
product successor after successful specification acceptance is
`MELLYCORE-3D-SCENE-FOUNDATION-001`, still not started or authorized.

The Control Plane specification and this lifecycle correction define no
frontend, backend, provider integration, runtime, secrets flow, deployment,
or 3D implementation. A successful merge does not automatically require a
post-merge synchronization task; another sync is warranted only if a concrete
live canonical statement becomes false.

## Historical Option B Deploy Path — Completed

The operator selected Option B: first deploy bundles the Source Arena static
renderer slice, an OpenRouter Model/Cost Observatory (static snapshot only,
no live calls/keys/backend), and safety-state labels. Full sequence and
gating detail: `shared_context/ROADMAP.md`'s "Option B Deploy Path" section.

**Closed steps.** PR #17 (branch
`feat/mellycore-source-arena-renderer-static-slice-001`, reviewed head
`4af0402d9ded634ba65d14f2013d7280b46296db`) is **merged into canonical `main`**
via merge commit `537a84c8132bcb5fec568b1776bc4c656af3f0c2`
(2026-07-23T11:41:42Z). The Sourcery XSS/static-analysis finding was remediated
before merge, so both the XSS triage and the merge gate are closed. The
post-merge living-docs sync is canonical via PR #19, merge commit
`b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`. The OpenRouter Observatory spec is
**merged into canonical `main` via PR #20**, merge commit
`f1e177e38a26cfc80e047c8481d7932ad4419487`.

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001` added the
Observatory tab (Model Constellation, Cost Radar, Route Advisor, Budget
Estimator, Capability Matrix, Fallback Chain, Safety Boundary Strip) against
a local static fixture in
`site/js/dashboard.js`/`site/dashboard.html`/`site/css/dashboard.css` only.
All cost/context-window fields are `null` (no reviewed pricing source on
file) — the estimator correctly shows `INSUFFICIENT PRICING DATA` throughout,
per spec.

Its full gate chain, all on branch
`feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`:
`-REVIEW-001` returned `NEEDS_FIXES` (one P1 mobile horizontal-page-scroll
defect caused by `.obs-main { display: contents }` breaking width
containment for descendant grids/flex rows/tables; one P3
`obs-matrix-body` class/id naming collision) → `-REMEDIATION-001` fixed both
(every direct Observatory card pinned to `width:100%; max-width:100%;
min-width:0` at the mobile breakpoint; matrix wrapper renamed) →
`-REVIEW-002` returned `PASS_STATIC_SNAPSHOT_SLICE_REVIEW_002` →
`-VISUAL-ACCEPTANCE-001` returned
`NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE` (catalogue-like
constellation, routing decision too low, mobile catalogue before advisor) →
`-VISUAL-POLISH-001` fixed it with a CSS/DOM router core, orbital model
lanes, restored first-viewport decision hierarchy, and corrected mobile
order → `-VISUAL-ACCEPTANCE-002` returned
`NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_002` (Budget Estimator
began behind the fixed footer at 1440×900) → `-VISUAL-POLISH-002` fixed it
with a desktop-only spacing rule → `-VISUAL-ACCEPTANCE-003` returned
`PASS_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_003`.

**`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-PUBLISH-001`
is complete: pushed the four-commit branch, opened, reviewed, and merged
[PR #21](https://github.com/Melly-999/mellycore-aios-core/pull/21) into
canonical `main` via merge commit
`6897b5f31528c47f1a5186de4f854484dc3d71de` (2026-07-23T16:19:42Z).** The
OpenRouter Observatory static snapshot slice is now canonical, not merely
branch/PR-scoped. No live API, key, backend, or deploy work occurred at any
point in this chain.

Historical next task at that point:
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-001`
(that docs-sync entry, since completed). This pointer is retained only as
historical sequencing evidence and is **not** the current repository-wide
next task — see the "Vercel Static Root" section above for the current
pointer.

Historical sequence, in order (all subsequently completed):

1. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
   — push, PR, review, merge this docs sync.
2. `MELLYCORE-STATIC-DEPLOYMENT-READINESS-001`
3. `MELLYCORE-STATIC-SHOWCASE-DEPLOYMENT-001` (only if explicitly authorized)
4. `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001`
5. `MELLYCORE-DEPLOYMENT-STATE-SYNC-001`

At the time this sequence was queued, no later gate had started and each
still required its own pass in order. This is historical sequencing context;
the sequence has since closed as recorded above. No WebGL/Three.js or
OpenRouter live-API implementation was authorized ahead of those gates.

## Integration Status (AI Operations Intelligence)

`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001` is **integrated into canonical
`main` via PR #7**. This gate is closed; it is recorded here only as history,
not as a pending step.

## Operations Data Contract — Integration Status

`MELLYCORE-OPERATIONS-DATA-CONTRACT-001` (branch
`docs/mellycore-operations-data-contract-001-v2`, tip commit `44dde78`) is
**integrated into canonical `main` via PR #13**
(https://github.com/Melly-999/mellycore-aios-core/pull/13), merge commit
`e0db28f06613d29028df96a2d651b6dfdf2f2aa8`. This gate is closed; it is
recorded here only as history, not as a pending step.

Integration is documentation/schema/fixture scope only: the fourteen
entities defined in `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`,
and their companion JSON Schema and example fixtures in
`shared_context/operations/`, now exist on canonical `main`. No adapters,
backend execution, autonomous improvement, runtime-consumed schema,
scheduler, or safety-rule mutation was implemented or authorized by this
merge; no script in `scripts/` reads, imports, or validates these files (see
`shared_context/operations/README.md`).

`MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001` had already
selected `docs/mellycore-operations-data-contract-001-v2` as the canonical
integration candidate ahead of this merge (see spec Section 6). The original,
differently-scoped `docs/mellycore-operations-data-contract-001` branch
(2026-07-19) was never merged, rebased, deleted, or pushed and remains a
superseded local branch; its adoptable content (`AI_ESTATE`,
`SKILL_GAP_CANDIDATE`, `MEMORY_FRESHNESS` schema/example pairs, and
`TRUTHFUL_STATE_LABELS.md`) had already been folded into `-v2` before this
merge by `MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`.

Full merge evidence and validation: durable report
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-001.md`.
The original task report,
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md`, is a historical
snapshot of local-only state prior to reconciliation and merge; it is not a
current-state claim.

Exact next task:
`MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-REVIEW-001`
(independent re-review of this state sync; not started). No Operations Data
Contract implementation, adapter, backend, or runtime task is authorized by
this entry.

## Later Roadmap Domains

After a reviewed intelligence specification, separately approved work may address
real adapters, guarded operations, observability UI, and validation evidence.
No implementation task is authorized by this queue entry.

## Parallel Decision Track — Source Arena Renderer

This track is independent of, and does not reorder, the primary roadmap
sequence above. `MELLYCORE-OPERATIONS-DATA-CONTRACT-001` integration has
**no ordering relationship** with this track: it is not a prerequisite, gate,
blocker, dependency, sequencing step, or required prior task for this track
or for `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`, and it does not
supersede this track. This track's work may be independently authorized and
reviewed on its own gates regardless of whether that contract's integration
is pending, in progress, or complete.

1. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001` — complete (docs-only).
   Records `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`, status
   PROPOSED.
2. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-001` — independent
   review complete. Outcome: **`NEEDS_FIXES`** (findings HR-01 through HR-06).
2a. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-001` — complete.
   Closed HR-01 through HR-06 in the ADR, the Holographic UI Spec amendment
   notice, this file, and other shared-context files; ADR status remained
   PROPOSED.
2b. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-002` — independent
   re-review complete. Outcome: **`NEEDS_FIXES`** on two residual findings
   (RF-01, RF-02); HR-01 through HR-06 confirmed closed.
2c. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REMEDIATION-002` — complete
   (this commit, docs-only). Closed RF-01 (corrected
   `docs/runbooks/MELLYCORE_LOCALHOST_QUICKSTART.md`'s "What this serves"
   section, which previously described the whole `site/` scaffold as having
   no JavaScript) and RF-02 (added an Appendix A §A.1 row mapping the
   Holographic UI Spec §6.2.4 planned README truthfulness-table entry to its
   future provider-neutral replacement); ADR status remains PROPOSED. Exact
   next task: `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003`
   (independent re-review; not started). Implementation remains blocked
   pending that review's PASS and separate operator acceptance of the ADR.
2d. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-REVIEW-003` — independent
   re-review complete. Outcome: **`PASS_HYBRID_RENDERER_ADR_REVIEW_003_COMPLETE`**;
   RF-01 and RF-02 confirmed closed alongside HR-01 through HR-06; three valid
   signed commits; exact scope confirmed; 245/245 tests passing.
2e. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-001` — complete
   (docs-only). The operator explicitly accepted the ADR on
   2026-07-20 at reviewed baseline `b95a741231d18ef712379837c7167aa22b37d42f`.
   ADR status became **ACCEPTED** (decision/specification level only — see
   `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`'s acceptance
   record). No Three.js implementation, dependency acquisition, or NASA
   retirement was authorized by this acceptance.
2f. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REVIEW-001` —
   independent re-review. Outcome: `NEEDS_FIXES` — two persisted gating-text
   contradictions in ADR Section 7's table header and Appendix A's NASA-row.
2g. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REMEDIATION-001` —
   closed both findings with two localized wording corrections; no
   architecture, scope, or status change.
2h. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-ACCEPTANCE-REVIEW-002` —
   independent re-review. Outcome:
   **`PASS_HYBRID_RENDERER_ADR_ACCEPTANCE_REVIEW_002_COMPLETE`**.
2i. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-001` — pushed the branch to
   canonical `clean-origin` and opened draft PR
   [#8](https://github.com/Melly-999/mellycore-aios-core/pull/8). No merge,
   implementation, or NASA action.
2j. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-REVIEW-001` — independent
   PR review. Outcome: `PASS_HYBRID_RENDERER_ADR_PR_REVIEW_COMPLETE`.
2k. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-READY-001` — marked PR #8
   ready for review. Sourcery's ready-state check did not trigger a fresh run
   (its own external weekly diff-character quota was already exhausted);
   recorded as `WAIVED_UNAVAILABLE_BY_OPERATOR` /
   `EXTERNAL_WEEKLY_RATE_LIMIT_NOT_CODE_FAILURE`, never reported as passing.
   `main` has no branch protection or required status checks.
2l. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-PR-MERGE-001` — merged PR #8
   into canonical `main` via merge commit
   `f93be7018a1da3bba50eb66346b1f9e627a46dd2` (parents
   `06a7a421a06abbe38450d276af94985da8ddeba0` and
   `dcfcd8db2089e6f27b5aea59446244bf964f4aea`), confirmed by independent
   pre- and post-merge fresh-clone validation (245/245 tests each). ADR
   status is now **`ACCEPTED_CANONICAL_MAIN`**. No renderer implementation,
   Three.js vendoring, NASA retirement, or release/deployment occurred.
2m. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-001` —
   synchronized current documentation to the merged state and resolved a
   non-blocking Codex clarity finding in ADR Section 31. Its independent
   review did not remain "not started": it ran to completion through the
   chain recorded in 2n–2r below.
2n. Independent post-merge canonical-state review (read-only) — after PR #9
   merged 2m into canonical `main` at `c7e24b8207598c600bb168a07959aeec7bebe003`,
   this review found `shared_context/AGENT_HANDOFF.md` self-contradictory on
   whether Operations Data Contract integration gates
   `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`. Outcome: `NEEDS_FIXES`.
2o. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-002`
   — fixed that contradiction (docs-only); its own review
   (`-REVIEW-001`) passed; opened PR
   [#10](https://github.com/Melly-999/mellycore-aios-core/pull/10);
   `-PR-REVIEW-001` found no blocking issue, but the pre-merge gate check
   (`-MERGE-001`) itself surfaced a new Codex P2 finding — residual "does not
   begin before" wording still readable as an ordering constraint — and
   stopped with `NEEDS_FIXES` before merging.
2p. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-003`
   — removed that residual wording, replacing it with an explicit
   "no ordering relationship" statement; its own review (`-REVIEW-001`)
   passed; pushed to PR #10 (`-PUSH-001`); `-PR-REVIEW-002` found no
   blocking issue; `-MERGE-001` passed every gate and merged PR #10 into
   canonical `main` via merge commit
   `b3b4f8b0124b8ee10c8ab6e5334cd35cf059fc88` (parents
   `c7e24b8207598c600bb168a07959aeec7bebe003` and
   `416a6f2ef1a69dd53c957e6a77cc5cd9633c1ad4`).
2q. A fresh independent canonical-state review of that merged state returned
   `NEEDS_FIXES`: residual "does not begin before" wording persisted in this
   file (above) and in ADR Section 31; `AGENT_HANDOFF.md`'s living
   "Exact next task" pointer still named the already-completed PR #9
   publication task; and this file's own item 2m still described its review
   as "not started" after it had, in fact, completed (2n above).
2r. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-004`
   — removed the residual ordering wording from this file and ADR Section
   31, corrected `AGENT_HANDOFF.md`'s stale task pointer, and corrected this
   file's stale review-status claim. No renderer, CSS fallback, Three.js,
   NASA, runtime, release, or deployment change. That entry's then-next-task
   did not remain "not started": it ran to completion, recorded in 2s–2t
   below.
2s. Independent review of `-P2-REMEDIATION-004` returned `NEEDS_FIXES`: a
   further stale, unqualified "exact next task" pointer to the
   already-completed `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`
   remained in this file's Deferred Work summary for the renderer ADR
   (above).
2t. `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-P2-REMEDIATION-005`
   — this entry (docs-only): corrected that pointer. No renderer, CSS
   fallback, Three.js, NASA, runtime, release, or deployment change. That
   entry's then-next-task ran to completion, recorded in 2u below.
2u. `-P2-REMEDIATION-005-REVIEW-001` returned `PASS` (no blocking finding) →
   `-PUBLISH-001` pushed the branch to `clean-origin` and opened
   [PR #11](https://github.com/Melly-999/mellycore-aios-core/pull/11) →
   `-PR-REVIEW-001` found no blocking review (Sourcery and Codex both
   `COMMENTED`, non-blocking) → `-MERGE-001` merged PR #11 into canonical
   `main` via merge commit `cad4e07f73f80c5794f9af2897fc10d922637ab3`
   (parents `b3b4f8b0124b8ee10c8ab6e5334cd35cf059fc88` and
   `48c1622610f0d3ac258c0f5c2b1b3a2b63209032`) → `-POST-MERGE-VERIFY-001`
   confirmed the merge commit, parentage, and changed-file scope
   independently. `-P2-CLOSEOUT-001` (this entry's closeout) closes this
   documentation-remediation chain: no renderer, CSS fallback, Three.js,
   NASA, runtime, release, or deployment change occurred at any step. Exact
   next task: `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` (docs/spec-scope
   review; not started).
3. `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001` — remove active NASA
   API calls and `nasa-*` active runtime handles from the Source Arena surface,
   preserving historical evidence. Status: `MERGED_INTO_CANONICAL_MAIN` —
   implemented on branch `fix/mellycore-source-arena-nasa-runtime-retirement-001`,
   merged via PR #15, merge commit `e0cbc332ff90f8787d981c9d86be717633f22d4d`
   (reviewed head `1478b95c82cb85fd5e0efdf433e928ca92cac69b`). Replaced the
   executable NASA Images fetch/parse/boot path in `site/js/dashboard.js`
   with a local, deterministic Source Archive dataset (zero external
   requests, no API key) and renamed the `nasa-*` runtime namespace to
   `source-arena-*` per this ADR's Appendix A mapping. Visual acceptance
   (`...-FINAL-REVIEW-001`) returned `PASS_WITH_NON_BLOCKING_NOTES`; VA-01
   (procedural swatch palette) and VA-02 (mission-rail scrollbar) were
   resolved before merge; VA-03 through VA-09 remain deferred, non-blocking
   backlog polish. Does not implement task 4 (the 3D scene foundation),
   vendor Three.js, or touch the CSS-fallback/renderer boundary. Exact next
   task: `MELLYCORE-SOURCE-ARENA-NASA-RETIREMENT-POST-MERGE-STATE-SYNC-PUBLISH-001`
   (push this docs-sync commit, open a PR, review, and merge if clean).
4. `MELLYCORE-3D-SCENE-FOUNDATION-001` — implement the shared state, complete
   CSS fallback, vendored/pinned Three.js enhanced renderer, lifecycle,
   context-loss recovery, and mobile-first Source Arena. Not started.
5. `MELLYCORE-3D-SCENE-ACCESSIBILITY-PERFORMANCE-QA-001` — keyboard/screen-reader
   parity, reduced-motion, forced-fallback, context-loss, memory/RAF cleanup,
   mobile and desktop performance. Not started.
6. `MELLYCORE-3D-SCENE-INTEGRATION-REVIEW-001` — independent final review
   before any merge or release claim. Not started.

Task 3 (NASA runtime retirement) is `MERGED_INTO_CANONICAL_MAIN` via PR #15,
merge commit `e0cbc332ff90f8787d981c9d86be717633f22d4d` (see item 3 above). Tasks 4–6 remain
`NOT_STARTED` and are not implemented, active, or authorized by this entry
alone. Task 1 (the ADR decision) is accepted at the decision/specification
level and its architecture milestone is now `CLOSED_IN_CANONICAL_MAIN` —
merged into canonical `main` via PR #8 (2l above). This does not implement,
vendor, or release anything; the 3D scene foundation (task 4) remains
`NOT_STARTED`.

A narrow, separate precursor — `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-001`
— is `MERGED_INTO_CANONICAL_MAIN` (branch
`feat/mellycore-source-arena-renderer-static-slice-001`, reviewed head
`4af0402d9ded634ba65d14f2013d7280b46296db`, merged via PR #17, merge commit
`537a84c8132bcb5fec568b1776bc4c656af3f0c2`, 2026-07-23T11:41:42Z). It restyles
the Source Arena stage into a static CSS/DOM holographic source map (orbital
source nodes around a central core, command inspector), replacing the prior
social-feed-style media card. It is CSS/DOM only: it does not start task 4,
vendor Three.js, add WebGL/Canvas, or implement the ADR's CSS-complete
fallback spec — all of which remain `NOT_IMPLEMENTED`/`NOT_STARTED`.

## Deferred Work

- Cross-agent context smoke testing remains a separate clean-worktree task.
- Provider/runtime integrations, deployment, releases, and Holographic UI
  implementation remain separately gated.
- Legacy NASA prototype cleanup is a future implementation decision, not part of
  the current product roadmap and not performed by the positioning task.

## Completed Milestone Index

- Static homepage and Living Context Graph prototype — historical reports under
  `docs/tasks/` and showcase evidence under `docs/showcase/`.
- Operational Trust / Loop Operations — closed; architecture and task evidence
  under `docs/architecture/`, `docs/research/`, and `docs/tasks/`.
- Context Gate I1–I4 — implemented; canonical evidence under
  `shared_context/context_provenance/` and completed reports under `docs/tasks/`.
- Live Cockpit V2 / `v0.2.0` — historical release and legacy prototype evidence.
- Holographic UI specification / PR #4 — accepted documentation; Source Arena
  hero contract preserved, implementation not claimed.
- Positioning refresh — integrated into canonical main; durable report at
  `docs/tasks/MELLYCORE-POSITIONING-REFRESH-001.md`.
- AI Operations Intelligence specification — integrated into canonical `main`
  via PR #7; durable report at
  `docs/tasks/MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001.md`.
- Source Arena Hybrid renderer ADR — status **`ACCEPTED_CANONICAL_MAIN`**
  (decision/specification level only); merged into canonical `main` via PR #8,
  merge commit `f93be7018a1da3bba50eb66346b1f9e627a46dd2`, 2026-07-20; durable
  report at
  `docs/tasks/MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-001.md`. Full review
  chain (all durable reports under `docs/tasks/`): review 001 `NEEDS_FIXES` →
  remediation 001 → review 002 `NEEDS_FIXES` → remediation 002 → review 003
  `PASS` → operator acceptance → acceptance review 001 `NEEDS_FIXES` →
  acceptance remediation 001 → acceptance review 002 `PASS` → pushed and
  opened as PR #8 → PR review `PASS` → marked ready (Sourcery waived as
  unavailable, not passed) → merged. No Three.js implementation, dependency
  vendoring, NASA runtime retirement, or release/deployment exists. That
  entry's then-next-task,
  `MELLYCORE-SOURCE-ARENA-HYBRID-RENDERER-ADR-POST-MERGE-STATE-SYNC-REVIEW-001`,
  has since completed (see the Parallel Decision Track above, items 2n–2r),
  as has the subsequent `-P2-REMEDIATION-005` review/publish/merge chain
  (items 2s–2u): PR #11 merged into canonical `main` via merge commit
  `cad4e07f73f80c5794f9af2897fc10d922637ab3`. No Three.js implementation,
  dependency vendoring, NASA runtime retirement, or release/deployment
  exists at any point in this chain. The current exact next task is
  `MELLYCORE-DOCS-INTEGRATION-REVIEW-001`.

## Standing Safety Gate

No push, PR, merge, force operation, rebase, squash, branch deletion, tag,
release, deploy, workflow mutation, trading behavior, credential storage, or
retired-remote contact without explicit operator authorization.
