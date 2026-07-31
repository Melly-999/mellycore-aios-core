# Roadmap

## Canonical Direction

MellyCore AIOS is a local-first, operator-controlled **AI Operations
Observatory**. It makes models, agents, runs, context, memory, recommendations,
and approvals visible and auditable while keeping consequential action behind an
explicit operator gate.

Controlled improvement loop:

`observe → analyze → recommend → approve → implement → validate → record`

This roadmap distinguishes implemented foundations from planned capabilities.
Naming a module here does not authorize or claim its implementation.

## Current Foundation

- **Operational Trust:** closed. Loop Operations is implemented as report-only,
  with immutable run evidence and no scheduler or production-enabled loop.
- **One Brain / Context Gate:** implemented through I4. Guarded admission,
  canonical write-once records, content-free index, computed audit, and a
  read-only dashboard surface exist.
- **Local presentation:** static homepage and Live Cockpit V2 exist. The current
  dashboard is a legacy prototype, not the complete Observatory.
- **Holographic Source Arena:** the **static CSS/DOM renderer slice** is
  canonical on `main` via PR #17 (merge commit `537a84c8`) — a static
  holographic source map (source core, orbital nodes, orbit ring, command
  inspector) that replaced the prior social-feed primary UX. The broader
  holographic specification remains accepted-specification-only: its 390×844
  model-lens hero remains the lead visual direction, and the 3D/WebGL treatment
  is **not implemented**. The full renderer and the ADR's CSS-complete fallback
  renderer are **not complete**.
- **NASA Images:** executable runtime retired from `site/dashboard.html` /
  `site/js/dashboard.js` under `MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`
  and merged into canonical `main` via PR #15 (merge commit
  `e0cbc332ff90f8787d981c9d86be717633f22d4d`); replaced with a local,
  deterministic Source Archive. Historical task reports and release evidence
  remain untouched. It was never a current pillar, roadmap module, or core
  integration.

Durable completion evidence lives in `docs/tasks/`, release records, and Git
history rather than being duplicated here.

## Active Milestone — Operations Data Contract

The AI Operations Intelligence specification
(`MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001`,
`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`) is **integrated
into canonical `main` via PR #7**. Specification integration is not
implementation: the specification defines logical contracts and truth/safety
boundaries only, and claims no runtime adapters, approval execution, or
autonomous improvement; its modules remain `SPECIFIED`.

`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`, which translates the approved
logical contracts into fixture/schema artifacts and validation requirements,
is **integrated into canonical `main` via PR #13**
(https://github.com/Melly-999/mellycore-aios-core/pull/13), merge commit
`e0db28f06613d29028df96a2d651b6dfdf2f2aa8`, from branch
`docs/mellycore-operations-data-contract-001-v2` (tip `44dde78`). Integration
is documentation/schema/fixture scope, not runtime implementation: the
fourteen dashboard-facing fixture entities (`operation_run`, `task_record`,
`agent_identity`, `model_provider_usage`, `token_cost_record`,
`validation_result`, `artifact_record`, `environment_capability_snapshot`,
`approval_gate`, `safety_status`, `recommendation_ledger_entry`, plus
`ai_estate_asset`, `skill_gap_candidate`, `memory_freshness_record`) defined
in `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` now exist on
canonical `main`, alongside their `shared_context/operations/` schema and
example fixtures.

`MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001` had already
selected `-v2` as the canonical integration candidate ahead of this merge;
see that document's Section 6 in
`docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`. The original,
differently-scoped `docs/mellycore-operations-data-contract-001` branch
(2026-07-19) remains unmerged, unpushed, and superseded — its three
adoptable entities (AI Estate Inventory, Skill Gap Detector, Memory
Freshness Monitor) plus its Truthful-State Labels reference had already been
folded into `-v2` before this merge by
`MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`. Full
merge evidence: durable report
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-001.md`.

Planned subject areas (all remain planned; the specification does not implement
them):

1. Mission Control
2. Agent Activity
3. Context Pulse
4. Model Router
5. Unified Run Ledger
6. Approval Queue
7. Memory & Recommendation Ledger
8. AI Estate Inventory
9. Skill Gap Detector
10. Memory Freshness Monitor

All ten remain **planned** unless a later evidence-backed task changes their
status. Real adapters, runtime execution, and guarded operations are later,
separately approved milestones.

## Visual Direction

Source Arena remains the intended leading holographic experience and first hero
image. The accepted visual rules in
`docs/specs/MELLYCORE_HOLOGRAPHIC_UI_SPEC_001.md` remain binding: mobile 390×844
model-lens composition first; Overview/core/orbit/hull supporting only; honest
real/simulated/planned labels throughout. The accepted specification is not an
implementation claim.

An accepted Hybrid renderer decision — `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`,
status **ACCEPTED** (2026-07-20, decision/specification level only, not
implemented) — narrowly permits a WebGL-enhanced renderer (one pinned,
vendored Three.js module) as progressive enhancement over a mandatory,
complete CSS/DOM fallback, without changing any visual rule above. Its
remaining task sequence (NASA runtime retirement, the 3D scene foundation,
accessibility/performance QA, integration review) runs as a parallel track
recorded in `shared_context/RUN_QUEUE.md` and does not reorder the Operations
Data Contract sequence below; none of those tasks is implemented, active, or
authorized by this acceptance alone.

## Option B Deploy Path — Static AIOS Showcase + OpenRouter Observatory

The operator selected **Option B** for the first public/static deploy: the
first deploy target is no longer the cinematic showcase alone. It now
bundles the Source Arena static renderer slice, an OpenRouter Model/Cost
Observatory as a **static snapshot only**, and truthful safety-state labels.
No live provider calls, no API keys, no backend, and no model execution are
authorized by this decision.

**Source Arena static slice — merged and canonical.** PR #17
(https://github.com/Melly-999/mellycore-aios-core/pull/17, branch
`feat/mellycore-source-arena-renderer-static-slice-001`, reviewed head
`4af0402d9ded634ba65d14f2013d7280b46296db`) is **merged into canonical `main`**
via merge commit `537a84c8132bcb5fec568b1776bc4c656af3f0c2`, merged
2026-07-23T11:41:42Z. It delivered the static holographic Source Arena renderer
slice, removed the prior social-feed primary UX, fixed the orbit-clipping
defect, and remediated the Sourcery XSS/static-analysis `innerHTML` finding
(former `site/js/dashboard.js:509` and `:554-561`) by rebuilding both flagged
sinks with DOM APIs. The earlier blocker on this PR is closed.

The slice is **CSS/DOM-only**. The full renderer and the ADR's CSS-complete
fallback renderer remain **not complete**; WebGL, Three.js, and Canvas remain
**not implemented**. This merge authorized no deploy, release, provider,
backend, or OpenRouter work.

**Active task sequence** (supersedes any prior "first deploy" framing; this
section is the authoritative Option B ordering):

1. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-XSS-FINDING-TRIAGE-001` —
   **complete.** The Sourcery XSS/static-analysis finding on PR #17 was
   remediated by rebuilding both flagged `innerHTML` sinks with DOM APIs.
2. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-MERGE-GATE-001` —
   **complete.** PR #17 merged into canonical `main` via merge commit
   `537a84c8132bcb5fec568b1776bc4c656af3f0c2` (2026-07-23T11:41:42Z).
3. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-001` —
   **complete (local docs commit only, not pushed).** Updated living docs after
   the PR #17 merge; report
   `docs/tasks/MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-001.md`.
4. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
   — **complete.** Published and merged via PR #19, merge commit
   `b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`.
5. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-001` — docs/spec only; define
   the Model Router Observatory UX; no API calls, no keys, no backend.
   **Complete as a local docs commit only, not pushed.** Artifact:
   `docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md`.
6. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-PUBLISH-001` — **complete.**
   Merged into canonical `main` via PR #20, merge commit
   `f1e177e38a26cfc80e047c8481d7932ad4419487`.
7. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001` —
   **complete.** Static snapshot panel from a local fixture only; no live
   OpenRouter fetch, no API key, no model calls, no backend. All cost/context
   fields are `null` pending a reviewed price source.
7a. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REVIEW-001`
   — **complete.** Outcome `NEEDS_FIXES_STATIC_SNAPSHOT_SLICE_REVIEW`: a P1
   mobile horizontal-page-scroll defect and a P3 class/id naming collision.
7b. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REMEDIATION-001`
   — **complete.** Fixed both findings: every direct Observatory card is now
   pinned to `width:100%; max-width:100%; min-width:0` at the mobile
   breakpoint, and the matrix wrapper `<div>` was renamed off the
   `obs-matrix-body` string. Verified zero horizontal page overflow at
   320px/375px.
7c. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REVIEW-002`
   — **complete.** Outcome `PASS_STATIC_SNAPSHOT_SLICE_REVIEW_002`.
8. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-001` — visual/
   product review confirming it reads as a Model Router Observatory, not a
   table dump. **Complete:** outcome
   `NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE`.
8a. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-POLISH-001` —
    **complete.** Added the CSS/DOM router-core/orbital composition, restored
    desktop first-viewport decision hierarchy, corrected mobile DOM/visual
    order, reduced the mobile status bar, and improved secondary mono copy
    without changing logic/data.
8b. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-002` —
    **complete.** Outcome
    `NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_002`: the Budget
    Estimator began behind the fixed footer at 1440×900.
8c. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-POLISH-002` —
    **complete.** A desktop-only spacing adjustment exposes the complete
    Budget Estimator header above the footer without changing mobile, logic,
    data, or safety.
8d. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-003` —
    **complete.** Outcome `PASS_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_003`.
9. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-PUBLISH-001`
   — **complete.** Pushed the four-commit branch, opened, reviewed, and
   merged [PR #21](https://github.com/Melly-999/mellycore-aios-core/pull/21)
   into canonical `main` via merge commit
   `6897b5f31528c47f1a5186de4f854484dc3d71de` (2026-07-23T16:19:42Z). This
   superseded the originally planned separate `-FINAL-REVIEW-001`/
   `-MERGE-GATE-001` tasks, which were not separately invoked — the passed
   `-REVIEW-002` and `-VISUAL-ACCEPTANCE-003` outcomes served as the
   equivalent technical/visual gates before this single publish task pushed,
   opened the PR, and merged it. The OpenRouter Observatory static snapshot
   is now canonical on `main`, not merely branch/PR-scoped.
10. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-001`
    — **historical; superseded.** Updated living docs after the PR #21
    merge as a local docs commit. No standalone publish task report for
    this exact task ID was found in `docs/tasks/`; its purpose (keeping
    shared context current) was carried out repeatedly by the later
    state-sync tasks recorded in this file and in `AGENT_HANDOFF.md`. This
    is no longer "the exact next task" — that stale label is corrected
    here.
11. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
    — **historical; superseded.** No standalone task report for this exact
    task ID was found in `docs/tasks/`; considered superseded by the
    deployment chain (items 13–15) that followed.
12. `MELLYCORE-STATIC-DEPLOYMENT-READINESS-001` — **historical; superseded.**
    No standalone task report for this exact task ID was found in
    `docs/tasks/`; the deployment-readiness decision was superseded in
    practice once the production Vercel deployment (item 13's real-world
    equivalent) was accepted.
13. `MELLYCORE-STATIC-SHOWCASE-DEPLOYMENT-001` — **superseded by the
    accepted production deployment.** No standalone task report for this
    exact task ID was found in `docs/tasks/`, but the actual production
    Vercel deployment exists and is accepted: static-root remediation
    reviewed `PASS` and merged via PR #23 (merge commit
    `177128cfc6513090b45491d16e9f0c594451636d`), with production redeploy
    smoke passing (`MELLYCORE-VERCEL-STATIC-SHOWCASE-REDEPLOY-SMOKE-001`).
14. `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001` — **complete and
    merged.** Verified the deployed URL with zero console errors and a
    screenshot artifact; merged into canonical `main` via PR #24 (merge
    commit `be3ead9b1b27a80bb6029acb7acba0c98c6ba4c6`).
15. `MELLYCORE-DEPLOYMENT-STATE-SYNC-001` — **complete and merged.** This
    entry synchronized `PROJECT_STATE.md` / `ROADMAP.md` / `RUN_QUEUE.md` /
    `AGENT_HANDOFF.md` to the accepted Vercel deployment and PR #24 merge
    state as a local docs commit
    (`2ee50b7ae3a256d830598a6bf384483f09538f5e`), was published as
    [PR #25](https://github.com/Melly-999/mellycore-aios-core/pull/25), had
    two documentation-consistency findings independently verified and
    corrected (`MELLYCORE-DEPLOYMENT-STATE-SYNC-REMEDIATION-001`, commit
    `4a6d200d6581d048dc4a7917bf3a470f84a3b4d3`), and merged into canonical
    `main` via PR #25 (merge commit
    `ca1f762a0cdd43b80282b885bfd7885d2740288a`, 2026-07-24T13:51:58Z).

**Vercel static-root remediation, published, verified, and state-synced
(2026-07-24).** The static-root fetch defect at
`https://mellycore-aios-core.vercel.app` (item 13 above) is fixed by
`MELLYCORE-VERCEL-STATIC-SHOWCASE-ROOT-PATH-REMEDIATION-001`, reviewed
`PASS`, and merged into canonical `main` via PR #23 (merge commit
`177128cfc6513090b45491d16e9f0c594451636d`). Production redeploy smoke
passed and post-deploy verification, including a screenshot artifact, is
recorded by `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001`, merged into
canonical `main` via PR #24 (merge commit
`be3ead9b1b27a80bb6029acb7acba0c98c6ba4c6`). The deployment-state
synchronization itself is recorded and merged via PR #25 (merge commit
`ca1f762a0cdd43b80282b885bfd7885d2740288a`). Vercel is the accepted
production static showcase host; GitHub Pages remains
containment/maintenance only.

Tasks 4–9, 14, and 15 are complete and merged into canonical `main`; items
10–12 were not separately invoked as discrete task reports and are
considered superseded by the deployment chain that followed; item 13 is
superseded by the accepted production deployment described above. No
deployment-state remediation or merge-retry task remains pending.
`MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-001` completed authoring and
was published on branch
`docs/mellycore-omnirouter-inspired-control-plane-spec-001` in
[PR #27](https://github.com/Melly-999/mellycore-aios-core/pull/27). Its
specification artifact,
`docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`, specifies
the Control Plane as an operator-facing coordination/governance surface and
keeps provider calls, runtime execution, persistence, authentication, and
network communication in a separately gated future Data Plane. Initial review,
targeted remediation, remediation publication, and targeted re-review are
complete; the re-review outcome was
`PASS_WITH_NOTES_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC_REMEDIATION_REVIEW`.
At the time of this update, PR #27 was merge-ready but not yet merged or
canonical. The remaining task-local gate at that time was
`MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-MERGE-001`. The durable
product successor after successful specification acceptance is
`MELLYCORE-3D-SCENE-FOUNDATION-001` — implemented in paused, open, unmerged
PR #28, currently `CONFLICTING / DIRTY`, not merged, not accepted, and
blocked by physical Android Chromium Gate B (`OPEN / NOT EXECUTED`);
canonical `main` has no accepted
implementation (see the Parallel Decision Track's item 4 below for its
existing scope). No automatic
post-merge state sync, OpenRouter live-API implementation, Control Plane
implementation, renderer expansion, or deployment is authorized by this
roadmap entry alone; another sync is warranted only if a concrete live
canonical statement becomes false.

**Deploy target.** MellyCore Static AIOS Showcase + Source Arena + OpenRouter
Model Observatory: cinematic AI command-center identity, the Source Arena
holographic command stage, the local deterministic Source Archive, the
OpenRouter static model/cost observatory, a route-advisor / model-purpose
matrix, and safety-state labels throughout — no live model execution, no
account usage, no secrets, no backend.

**OpenRouter safety levels.** The OpenRouter panel is future-gated across
three levels; only Level 1 is in scope for the first deploy:

- **Level 1 — Static Snapshot** (allowed for first deploy): local fixture,
  static prices, static capabilities, no API key, no backend, no live fetch,
  no model call.
- **Level 2 — Public Catalog Readiness** (future-gated): public model catalog
  review, freshness labels, cache strategy, no account usage, no API key in
  the frontend, separate approval required.
- **Level 3 — Account Usage / Real Costs** (strictly future-gated): requires
  backend, secrets management, authentication, a usage/cost security review,
  a deployment security review, and explicit approval.

Levels 2 and 3 are excluded from the first deploy unless separately
authorized. Level 1 (static snapshot) is now implemented and merged into
canonical `main` via PR #21. Levels 2 and 3 remain not implemented; no
OpenRouter API key, account usage, or live catalog call is authorized by
this roadmap entry.

## OpenAI Batch Controlled Activation — Post-Merge State

- **Completed:** `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-MERGE-001`.
  PR #32 merged via GitHub merge commit
  `5e7628a72a22fc10ecd0f9a25515ab61eb7223b9` at
  `2026-07-30T22:19:15Z`. Canonical `main` contains the exact reviewed tree
  and all seven reviewed commits.
- **Published state-sync:** original state-sync commit `472fcd21…` was
  independently reviewed locally, its branch was published, and PR #33 was
  created. PR #33 remains open, non-draft, unmerged, and not
  merge-authorized.
- **PR review 001:** returned
  `REMEDIATION_REQUIRED_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_POST_MERGE_STATE_SYNC_PR_REVIEW_001`.
  Codex P2 finding `Advance the canonical queue past the completed review`
  identified stale present-tense workflow state across `PROJECT_STATE.md`,
  `AGENT_HANDOFF.md`, this roadmap, and `RUN_QUEUE.md`. At the start of that
  remediation, its single thread (`discussion_r3690288402`) was unresolved.
  Local remediation commit `c0f69c5…` addressed this finding.
- **Remediation review 001:** returned
  `PASS_WITH_NOTES_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_POST_MERGE_STATE_SYNC_PR_REMEDIATION_REVIEW_001`.
  The Codex P2 defect was confirmed resolved; the sole factual note was an
  invalid 38-character static `site` subtree identifier in
  `AGENT_HANDOFF.md` and `RUN_QUEUE.md`, plus two non-blocking consistency
  notes (an inconsistent Stage B state code and an unnamed merge task).
  Local remediation commit
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-PR-REMEDIATION-002`
  corrects all three.
- **Time-scoped remediation gate:** at creation of the local remediation-002
  commit, that commit is local-only and unreviewed. The exact immediate next
  task is
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-PR-REMEDIATION-002-REVIEW-001`.
- **Required completion path after a PASS:**
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-PR-REMEDIATION-PUSH-001`
  must push the exact reviewed final local head — the full three-commit
  chain built on the currently published one-commit head `472fcd21…` — by
  normal SHA-to-ref fast-forward, discovering the final commit's SHA only
  after it exists. It must verify the remote and PR heads then show three
  commits, update and re-fetch the PR body to list both remediation commits
  and the exact final head while preserving the cumulative five-file scope
  and validation provenance, correct the published static-site subtree
  evidence, describe the P2 finding and both remediation steps, reply with
  exact published evidence, resolve the thread only after verification,
  verify checks and Preview, and leave PR #33 open, unmerged, and without
  auto-merge. Push without complete metadata and thread reconciliation is
  partial or blocked. Only then may a fresh independent
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-PR-REVIEW-002`
  run; only its PASS may permit the separately authorized merge task
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-MERGE-001`.
- **Conditional later decision, only after reviewed, merged, and canonically
  reconciled state sync:**
  `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`.
- Task-record next-task fields are creation-time historical snapshots,
  superseded by this roadmap and `RUN_QUEUE.md`.

This remediation and roadmap state do not authorize PR #33 merge, Stage C,
or live Batch execution. Live smoke remains a separate Operator decision; the
hard `USD 0.01` boundary remains unavailable until separately authorized;
migration trigger #5 remains uncrossed; provider policy remains fail-closed.
The PR #32 merge changed no `site/**` file, and its automatic Production
deployment published the unchanged static tree only.

## Safety Gates

- Human approval is mandatory for consequential actions.
- No autonomous safety-rule changes, merge, or uncontrolled tool use by an
  agent or operator without explicit approval.
- No provider keys, tokens, credentials, or private runtime state in the repository.
- No trading, broker, order, or MellyTrade runtime direction.
- No runtime adapter or execution milestone without specification, review,
  explicit authorization, validation, and durable evidence.
- **Production deployment note — Model A selected (Operator decision,
  2026-07-27):** merging into canonical `main` causes automatic public
  Production publication via the Vercel Git integration, with no separate,
  technically-enforced deployment-approval step. The Operator has selected
  **Model A** — temporary, static-phase-only combined merge/deployment
  authorization — as recorded verbatim in `shared_context/DECISIONS.md` and
  detailed in full in `shared_context/PROJECT_STATE.md`'s "Production
  Deployment Authorization — Model A Contract (Temporary, Static-Phase
  Only)". Each individual merge approval authorizes only the Production
  publication that specific merge causes — never blanket authorization —
  and every merge-authorization request must warn that it immediately
  affects the public Production host. Nine canonical, blocking migration
  triggers (first backend endpoint, authentication flow, stored user data,
  runtime secret, live provider connection, execution-capable agent,
  external write-capable integration, financial/trading action, or
  delegated merge authority/multiple maintainers) require Model B
  reconsideration before any affected implementation or merge proceeds.

## Operator Command

`/roadmap` is the documentation-defined operator command for reading current
state. Its durable sources are this file, `PROJECT_STATE.md`, `RUN_QUEUE.md`,
`AGENT_HANDOFF.md`, `MODEL_ROUTING.md`, and `SAFETY_CONTRACT.md`. Full response
shape: `docs/runbooks/MELLYCORE_ROADMAP_COMMAND.md`.
