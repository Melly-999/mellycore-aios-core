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
    — **exact next task (this entry).** Update living docs after the PR #21
    merge; local docs commit only, not pushed.
11. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
    — push, PR, review, merge that docs sync.
12. `MELLYCORE-STATIC-DEPLOYMENT-READINESS-001` — decide whether deploy is
    allowed; confirm deploy target; confirm no secrets, no provider calls, no
    backend, no false live claims.
13. `MELLYCORE-STATIC-SHOWCASE-DEPLOYMENT-001` — first static deploy, only if
    explicitly authorized; no backend, no provider keys, no runtime API.
14. `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001` — verify the deployed
    URL; desktop/mobile smoke; no NASA/OpenRouter/provider/model calls unless
    explicitly intended; no console errors; truthful-state copy.
15. `MELLYCORE-DEPLOYMENT-STATE-SYNC-001` — **complete.** This entry
    synchronized `PROJECT_STATE.md` / `ROADMAP.md` / `RUN_QUEUE.md` /
    `AGENT_HANDOFF.md` to the accepted Vercel deployment and PR #24 merge
    state (local docs commit only; publish is a separate task).

**Vercel static-root remediation, published, verified, and state-synced
(2026-07-24).** The static-root fetch defect at
`https://mellycore-aios-core.vercel.app` (task 14 above) is fixed by
`MELLYCORE-VERCEL-STATIC-SHOWCASE-ROOT-PATH-REMEDIATION-001`, reviewed
`PASS`, and merged into canonical `main` via PR #23 (merge commit
`177128cfc6513090b45491d16e9f0c594451636d`). Production redeploy smoke
passed (`MELLYCORE-VERCEL-STATIC-SHOWCASE-REDEPLOY-SMOKE-001`) and
post-deploy verification, including a screenshot artifact, is recorded by
`MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001`, merged into canonical
`main` via PR #24 (merge commit `be3ead9b1b27a80bb6029acb7acba0c98c6ba4c6`).
Vercel is the accepted production static showcase host; GitHub Pages
remains containment/maintenance only.

Tasks 4–15 are complete at the states recorded above; the OpenRouter
Observatory static snapshot slice, Vercel static-root remediation, and
post-deploy verification are all canonical on `main`. The exact next task
is `MELLYCORE-OMNIROUTER-INSPIRED-CONTROL-PLANE-SPEC-001` (specification
work only — no implementation, backend, provider integration, or deployment
is authorized by this roadmap entry). Queued after that spec, not yet
started or authorized: `MELLYCORE-3D-SCENE-FOUNDATION-001` (see the
Parallel Decision Track's item 4 below for its existing scope). No
OpenRouter live-API implementation, renderer expansion, or deployment is
authorized by this roadmap entry alone.

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

## Safety Gates

- Human approval is mandatory for consequential actions.
- No autonomous safety-rule changes, merge, deployment, or uncontrolled tool use.
- No provider keys, tokens, credentials, or private runtime state in the repository.
- No trading, broker, order, or MellyTrade runtime direction.
- No runtime adapter or execution milestone without specification, review,
  explicit authorization, validation, and durable evidence.

## Operator Command

`/roadmap` is the documentation-defined operator command for reading current
state. Its durable sources are this file, `PROJECT_STATE.md`, `RUN_QUEUE.md`,
`AGENT_HANDOFF.md`, `MODEL_ROUTING.md`, and `SAFETY_CONTRACT.md`. Full response
shape: `docs/runbooks/MELLYCORE_ROADMAP_COMMAND.md`.
