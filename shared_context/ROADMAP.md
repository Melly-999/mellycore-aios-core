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
- **Completed: PR #33 governance state-sync merged.** Original state-sync
  commit `472fcd21…`, remediation 001 (`c0f69c5…`), and remediation 002
  (`ab5a6d7…`) were published, reconciled, and independently reviewed
  (`PASS_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_POST_MERGE_STATE_SYNC_PR_REVIEW_002`).
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-POST-MERGE-STATE-SYNC-MERGE-001`
  merged PR #33 at `2026-07-31T15:52:54Z` via GitHub merge commit
  `f118110181fe5428940ac86256dedc63f52282a6` (first parent
  `5e7628a72a22fc10ecd0f9a25515ab61eb7223b9`, second parent exact reviewed
  head `ab5a6d775ff86bc051788ca2927e17c3d8eab880`; merge tree
  `e49a392614b10be2e235dcb85ad374004bbced0b` identical to the reviewed-head
  tree). PR #33's exact three-commit, five-file documentation-only scope is
  now canonical on `main`; the static `site` tree remained unchanged at
  `5df8bb686ebeb5b13bcf1fe2ad2ef6bc796bfc5d`. The Codex thread
  (`discussion_r3690288402`) is resolved with a published evidence reply.
  The automatic Vercel Production deployment succeeded for the exact merge
  commit (GitHub deployment `5694313001`, `success`); the accepted host
  `https://mellycore-aios-core.vercel.app` returned HTTP 200; no manual
  deployment action or page-level visual acceptance occurred.
- **Final canonical reconciliation:**
  `MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-001`
  records this merged, Production-verified state as the durable Stage B
  governance baseline. At creation of its local documentation commit, that
  commit is local-only and unreviewed — a time-scoped creation fact. The
  exact immediate next task at creation time is
  `-RECONCILIATION-REVIEW-001`.
- **Required completion path after a PASS:** `-RECONCILIATION-PUSH-001`,
  then `-RECONCILIATION-PR-CREATION-001`, then `-RECONCILIATION-PR-REVIEW-001`,
  then `-RECONCILIATION-MERGE-001`. Once that reconciliation content is
  independently reviewed, merged into canonical `main`, and its automatic
  Production deployment is verified, the canonical state it describes is the
  final reconciled Stage B governance baseline — no further state-sync task
  is required solely to restate the PR #33 merge already recorded above.
- **Conditional later decision, only after the reconciliation chain
  completes:** `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` — a
  separate decision task, not live execution authorization.
- Task-record next-task fields are creation-time historical snapshots,
  superseded by this roadmap and `RUN_QUEUE.md`.

This state sync does not authorize Stage C or live Batch execution. Live
smoke remains a separate Operator decision; the hard `USD 0.01` boundary
remains unavailable until separately authorized; migration trigger #5
remains uncrossed; provider policy remains fail-closed. Neither the PR #32
merge nor the PR #33 merge changed any `site/**` file; both automatic
Production deployments published the unchanged static tree only.

## Enterprise Provider Integration — Research Direction (Proposed, Parallel Track)

This section records architectural research and a proposed direction for
future enterprise integration-fabric, cybersecurity-provider, and
marketing-provider work. It is **independent of, and does not reorder,**
the OpenAI Batch Controlled Activation sequence above or any other active
gate in this roadmap — analogous to the "Parallel Decision Track — Source
Arena Renderer" pattern in `shared_context/RUN_QUEUE.md`. Naming a
candidate here does not authorize its selection, connection, or
implementation.

**Integration fabrics evaluated:** Composio, n8n, Pipedream Connect, Tray.ai
Agent Gateway, Workato, Zapier MCP, and OpenClaw (architectural reference
only, not a runtime dependency — full findings in `PROJECT_STATE.md`'s
"Enterprise Provider Integration" entry). **Accepted architecture
direction**, per
`docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
(`MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001`, decision/
specification level only — no fabric is configured, credentialed, or
connected by that ADR): Composio (managed
auth / agent-tool layer), private self-hosted n8n (deterministic workflow
layer), Pipedream (long-tail fallback), Tray.ai/Workato (later
enterprise-governance options), Zapier MCP (broad marketing/business
integration, not the cybersecurity execution boundary), and direct native
adapters for deterministic high-trust cybersecurity operations.

**Cybersecurity provider candidates** — P0: Microsoft Defender XDR /
Microsoft Graph Security, GitHub Advanced Security, Cloudflare, Okta.
P1/P2: Splunk, CrowdStrike Falcon, Snyk.

**Marketing provider candidates** — P0: HubSpot, Google Ads, Google
Analytics 4, Meta Marketing API, LinkedIn Marketing API, Twilio Segment.
Later/vertical: Salesforce Marketing Cloud, Braze, Klaviyo, Adobe Experience
Platform.

**Cloudflare** is proposed as a P0 cybersecurity-provider candidate under a
future `Cloudflare Application & API Security Provider` (API Shield, API
Discovery, Endpoint Management, Authentication Posture, Schema Validation
2.0, WAF Rulesets, audit events). The deprecated Firewall Rules API and
`/api_gateway/user_schemas/hosts` are excluded from any new integration;
the Rulesets API and Schema Validation 2.0 are the recorded future
direction. Full detail, legacy exclusions, and safety boundaries:
`PROJECT_STATE.md`'s "Enterprise Provider Integration — Architectural
Research Recorded (Not Implemented)". The canonical connector contract —
capabilities, risk tiers, approvals, credential profiles, rollout staging,
and verified legacy exclusions — is
`docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
(item 3 below).

**Documentation sequence** (reconciled against current canonical ordering at
the time each task starts; each item records its current state below):

1. `MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001` — this entry.
   **Complete as a local, unpushed documentation commit.**
2. `MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001` — canonical
   provider-selection and integration-fabric decision record. **Complete
   as a local, unpushed documentation commit.** Canonical decision:
   `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`.
3. `MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001` — Cloudflare
   capability, authorization, approval, audit, rollout, and
   legacy-exclusion contract. **Complete as a local, unpushed
   documentation commit.** Canonical contract:
   `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
   — specification-level acceptance only, authorizing no implementation,
   credential, provider authentication, Cloudflare API call (including
   read-only), MCP connection, or deployment.
4. `MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001` — extends the
   Provider Registry contract for enterprise SaaS, marketing, and
   cybersecurity systems (tenant identity, credentials, scopes, risk tiers,
   approvals, audit, data classification). **Complete as a local, unpushed
   documentation commit.** Canonical contract:
   `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
   — specification-level acceptance only, authorizing no registry
   implementation, adapter, credential, provider authentication, provider
   API call (including read-only), MCP or fabric connection, or deployment.
5. `MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` — trust boundary
   between MellyCore, direct adapters, MCP servers, integration fabrics,
   and delegated/service credentials. **Specification complete after
   recovery remediation and validation.** Canonical contract:
   `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
   — specification-level acceptance only, authorizing no Gateway
   implementation, adapter, credential, provider authentication, provider
   API call (including read-only), MCP or fabric connection, webhook
   registration, or deployment.
6. `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` — first read-only
   cybersecurity provider pack. **Specification complete as a local,
   unpushed documentation commit.** Canonical specification:
   `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md` — P0
   Microsoft Defender XDR / Microsoft Graph Security, GitHub Advanced
   Security, Cloudflare, and Okta; P1 Splunk and CrowdStrike Falcon; P2
   Snyk; R0-R2 only, with R3-R5 deferred. This acceptance authorizes no
   provider connection, credential, adapter, runtime, API call, MCP/fabric
   connection, webhook registration, or deployment.
7. `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` — first read-only
   marketing analytics/CRM provider pack. **Specification complete as a
   local, unpushed documentation commit.** Canonical specification:
   `docs/specs/MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md` — P0 HubSpot,
   Google Analytics 4, Google Ads, Meta Marketing API, LinkedIn Marketing
   API, and Twilio Segment; P1 Salesforce Marketing Cloud, Braze, and
   Klaviyo; P2 Adobe Experience Platform; R0-R2 only, with R3-R5 deferred.
   This acceptance authorizes no provider connection, credential, adapter,
   runtime, tracking, audience/campaign operation, API call, MCP/fabric
   connection, webhook registration, or deployment.
8. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001` — final
   integration review across 25 documents, 26 dimensions, and 12 scenarios.
   **Complete; `FAIL_REMEDIATION_REQUIRED` (P0 = 0, P1 = 4, P2 = 2,
   P3 = 3).** Canonical review:
   `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md`.
   Remediated by
   `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001`, which
   closes all nine findings and adds
   `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`.
9. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002` — independent
   post-remediation gate across 19 documents and 16 scenarios. **Complete;
   `FAIL_REMEDIATION_REQUIRED` (P0 = 0, P1 = 1, P2 = 0, P3 = 3).** Eight of the
   nine review-001 findings are independently verified closed; review-001
   `P1-003` is `PARTIALLY_CLOSED`. Blocking finding `P1-201`: Registry §13.2's
   closed eight-class credential catalogue cannot express the accepted
   Cloudflare contract's `CF_MCP_OPERATOR` profile, and Gateway §§34.1–34.6
   contradict Gateway §14.2. Canonical review:
   `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md`.
   The documentation gate has not passed.
10. `MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001`
    — **complete as one local documentation remediation; not a gate PASS.**
    Publishes a deterministic projection from Cloudflare requirement labels to
    nine canonical Registry classes, binds every concrete registration to one
    class before Gateway resolution, and routes the three P3 findings.
    `P1-201` closure remains unverified.
11. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003` — **complete;
    gate failed.** `FAIL_REMEDIATION_REQUIRED` (P0 = 0, P1 = 2, P2 = 1,
    P3 = 2) across 17 documents and 16 determinism scenarios. `P1-201` is
    `PARTIALLY_CLOSED`: the ninth canonical class, the one-class D4 binding,
    the derived non-normative `credential_class: investigation` value, and the
    `CF_READ` projection are independently verified closed; the operator-bound
    restricted-tool path is not expressible in the Gateway acting-identity
    model (`P1-301`) or under the Cloudflare provider record's required scope
    dimensions (`P1-302`). Both fail in the deny direction, and no safety
    regression was found. Canonical review:
    `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md`.
    The documentation gate has not passed.
12. `MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001`
    — **complete as one local documentation remediation; not a gate PASS.**
    Defines the Registry-owned three-value acting-identity vocabulary,
    `required_acting_identity_type`, capability-level scope applicability,
    authentication targets, and exact restricted-tool registration/scope.
    Gateway, Cloudflare D4, and the Cybersecurity Pack now consume the same
    contract. `P1-301` and `P1-302` closure remains unverified.
13. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004` — **complete;
    documentation gate passed with non-blocking findings.**
    `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 = 0, P1 = 0, P2 = 0, P3 = 3) across
    20 documents and 24 determinism scenarios, all 24 deterministic. All five
    Review 003 findings — `P1-301`, `P1-302`, `P2-301`, `P3-301`, `P3-302` —
    are independently verified `CLOSED`. Verified from contract text: one
    Registry-owned three-value acting-identity vocabulary; one canonical
    `required_acting_identity_type` selector bound before credential
    resolution; three authentication targets with mode and target separate;
    capability-level scope applicability whose `not_applicable` is permitted
    only where a provider contract explicitly allows it (Cloudflare: D4 only);
    `mellycore_operator` neither provider-account nor provider-API eligible and
    never a fallback; restricted-tool OAuth that cannot become provider OAuth;
    and Cloudflare's 58 capability and 13 prohibition rows byte-identical to
    the pre-remediation commit with D4 unchanged at three R0 capabilities.
    Three non-blocking P3 observations remain (`P3-401`, `P3-402`, `P3-403`);
    none changes a runtime decision. Canonical review:
    `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_004.md`.
14. `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` — **complete as one inert,
    provider-neutral local scaffold; not pushed.** Standard-library Python 3.9
    contracts now represent the canonical provider ID grammar, nine credential
    classes, three acting identities, three authentication targets, three scope
    applicability values, R0-R5, immutable descriptors/envelopes, and all eight
    independent authorization facts. Static validation, sanitized typed errors,
    a disabled adapter, and fixture-only in-memory tests exist. No real provider,
    transport, credential, OAuth, MCP/fabric, registration, runtime enablement,
    or execution-success path exists.
15. `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-REVIEW-001` — **complete; scaffold gate
    passed with non-blocking findings.** Independent review of scaffold commit
    `311ee3f…` against the accepted Registry, Gateway, provider contracts/packs,
    Review 004 §36, and the scaffold's own tests. Outcome:
    `PASS_WITH_NON_BLOCKING_FINDINGS`; P0 = 0, P1 = 0, P2 = 6, P3 = 5. Canonical
    vocabularies are exact and closed, validation fails closed with stable typed
    codes, every model is meaningfully immutable, no network/credential/
    environment/SDK/OAuth/MCP/fabric behavior exists, and no execution-success
    outcome is representable. Both claimed test counts reproduce (62 focused,
    636 full). Canonical review:
    `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md`.
16. `MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-001` — **complete in one
    local implementation commit; not pushed.** Added a transportless,
    credentialless, execution-disabled Cloudflare descriptor; separate delegated
    and service 16-entry D1 manifests; immutable read-operation plans; explicit
    scope projection; a complete 58-row classification; and bounded synthetic
    API Shield fixture normalization. Excluded all proposal, mutation,
    containment, D4 restricted-tool, MCP, webhook, and event-verification paths.
    No provider was contacted or authenticated and no runtime was enabled.
17. `MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-001` — **exact
    review completed; gate failed and remediation is required.** Outcome:
    `FAIL_REMEDIATION_REQUIRED`; P0 = 0, P1 = 1, P2 = 2, P3 = 0. The complete
    58-row classification and inert execution posture passed review, but the
    concrete capability/profile authentication mode required by the Registry is
    absent. Endpoint-URL-shaped fixture host text is also accepted unflagged,
    and focused tests are not a complete independent contract oracle. The
    provider-foundation checkpoint remains incomplete.
18. `MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REMEDIATION-001` — **exact
    remediation completed in one local implementation commit; not pushed.**
    Concrete delegated/service entries now bind exact compatible non-runtime
    modes; global metadata no longer conflates variants; fixture hosts use a
    closed synthetic grammar; and focused tests include a literal 58-row
    contract oracle plus expanded adversarial coverage. No generic scaffold,
    transport, credential, authentication, provider, or runtime path changed.
    Remediation claims remain unverified pending Review 002.
19. `MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002` — **complete in
    one local documentation commit; not pushed.** Outcome
    `PASS_WITH_NON_BLOCKING_FINDINGS`: P0 = 0, P1 = 0, P2 = 2, P3 = 1. Review
    001's `P1-01`, `P2-01` and `P2-02` are each independently verified `CLOSED`
    against the canonical contracts, the implementation, the tests, and direct
    probes; no capability classification, scope, manifest, plan, fixture or
    execution-disabled regression was found; and the neutral scaffold,
    canonical contracts and prior reviews are byte-identical. New non-blocking
    findings `P2-03`, `P2-04` and `P3-01` are recorded in
    `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md`.
    The offline Cloudflare adapter checkpoint is accepted and the
    provider-foundation checkpoint is complete for this milestone under those
    findings' constraints. Live Cloudflare work remains blocked and
    unauthorized.
20. `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001` — **exact next main product
    task; eligible for separate authorization.** Not started, not authorized,
    not approved, not active, and not implemented. Its architecture depends on
    no unresolved Cloudflare provider behaviour, because the adapter exposes no
    runtime, transport, credential or authentication path.

No credentials, provider runtime, restricted-tool or MCP connection,
MCP execution, Cloudflare API call,
marketing action, or cybersecurity remediation is authorized by this
section. Live sequencing for this track: `shared_context/RUN_QUEUE.md`'s
"Parallel Decision Track — Enterprise Provider Integration".

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
