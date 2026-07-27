# Project State

Project name: MellyCore AIOS

## Canonical Product Identity

MellyCore AIOS is a local-first, operator-controlled **AI Operations
Observatory**. It exists to make models, agents, runs, context, memory,
recommendations, and approvals visible, inspectable, approval-gated, and
auditable.

The controlled improvement loop is:

`observe → analyze → recommend → approve → implement → validate → record`

Consequential action requires explicit operator approval. The system does not
autonomously change safety rules, merge, deploy, execute recommendations, or
store provider secrets.

## Durable Implemented State

- Static local homepage and Live Cockpit V2 prototype.
- Report-only Loop Operations Foundation: 9 registered loops, 1 exercised loop,
  0 production-enabled loops, and two human-invoked `project-health` runs.
- Context Gate through I4: guarded admission, 7 validated canonical records,
  content-free index, computed audit, and read-only dashboard Context surface.
- Current audit baseline: 0 findings, index current, 0 writes.
- Standard-library validation baseline: 245 tests.

## Vercel Static Showcase — Accepted Production Deployment

`https://mellycore-aios-core.vercel.app` is the **accepted production static
showcase host** for MellyCore AIOS. GitHub Pages
(`https://melly-999.github.io/mellycore-aios-core/`) remains
containment/maintenance-only, per `MELLYCORE-GITHUB-PAGES-CONTAINMENT-001`,
and is not a product host.

The static-root fetch defect (repository-only `/shared_context/*` requests
returning 404 and logging a dashboard console error under `site/` as
Vercel's root) was fixed by
`MELLYCORE-VERCEL-STATIC-SHOWCASE-ROOT-PATH-REMEDIATION-001`: repository-only
reads are optional on 404, the two public frozen snapshots under `site/data/`
remain required, and affected panels render honest degraded copy
("not published with this static deployment") rather than implying internal
context is public. Reviewed `PASS`
(`MELLYCORE-VERCEL-STATIC-SHOWCASE-ROOT-PATH-REMEDIATION-REVIEW-001`) and
merged into canonical `main` via
[PR #23](https://github.com/Melly-999/mellycore-aios-core/pull/23), merge
commit `177128cfc6513090b45491d16e9f0c594451636d`.

Production redeploy smoke passed
(`MELLYCORE-VERCEL-STATIC-SHOWCASE-REDEPLOY-SMOKE-001`): the GitHub
deployments API confirms the live Production deployment's SHA matches the
merge commit exactly; homepage and dashboard load with zero console errors;
Source Arena, Model Arena, and OpenRouter Observatory are all visible and
populated; safety labels are present; all 18 observed network requests stay
on the app's own origin (no external OpenRouter/NASA/provider/model/broker
calls); mobile 320px/375px show no overflow.

Post-deploy verification record, including a screenshot artifact
(`docs/screenshots/mellycore-vercel-static-showcase-post-deploy-20260724.png`),
is captured in `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001` and merged
into canonical `main` via
[PR #24](https://github.com/Melly-999/mellycore-aios-core/pull/24), merge
commit `be3ead9b1b27a80bb6029acb7acba0c98c6ba4c6`.
`MELLYCORE-DEPLOYMENT-STATE-SYNC-001` synchronized this file, `ROADMAP.md`,
`RUN_QUEUE.md`, and `AGENT_HANDOFF.md` to that accepted state, then was
published and, after a documentation-consistency remediation
(`MELLYCORE-DEPLOYMENT-STATE-SYNC-REMEDIATION-001`), **merged into
canonical `main`** via
[PR #25](https://github.com/Melly-999/mellycore-aios-core/pull/25), merge
commit `ca1f762a0cdd43b80282b885bfd7885d2740288a` (2026-07-24T13:51:58Z).
The deployment-state synchronization and remediation chain is complete; no
deployment-state remediation or merge-retry task remains pending. No live
provider routing, live model execution, live OpenRouter data, backend
integration, account-usage tracking, or trading/broker execution is claimed
by any of this chain. The OmniRouter-inspired Control Plane specification was
authored and published on branch
`docs/mellycore-omnirouter-inspired-control-plane-spec-001` in
[PR #27](https://github.com/Melly-999/mellycore-aios-core/pull/27):
`docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` defines the
operator-facing coordination/governance layer, its strict separation from a
future Data Plane, ten module contracts, entity/status/workflow contracts,
desktop/mobile behavior, provenance, approvals, security metadata, static
fixtures, accessibility, and performance budgets. It implements no frontend,
backend, provider connection, runtime, secrets path, deployment, or 3D work.
Independent review identified two specification blockers; the targeted
remediation was published as commit `ea662ab…`, and its targeted review
returned
`PASS_WITH_NOTES_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC_REMEDIATION_REVIEW`
with all required checks passing. At the time of that update, PR #27 was
reviewed and merge-ready but not yet merged. It subsequently merged into
canonical `main` as `e7c8ce5f116e93a11a591ee539272f223af110d1`. Its separately
gated product successor, `MELLYCORE-3D-SCENE-FOUNDATION-001`, is implemented
in [PR #28](https://github.com/Melly-999/mellycore-aios-core/pull/28); see
"3D Scene Foundation — PR #28 Paused State" below for its current, paused
acceptance state. No automatic post-merge synchronization is required unless a
concrete live canonical statement becomes false.

## 3D Scene Foundation — PR #28 Paused State

`MELLYCORE-3D-SCENE-FOUNDATION-001` is implemented on branch
`feat/mellycore-3d-scene-foundation-001` and published as
[PR #28](https://github.com/Melly-999/mellycore-aios-core/pull/28) (head
`57bb841e67e9a5d557f88bf096537eba78df1cd8`, base `main`, two commits, twelve
changed files, locally vendored Three.js r164). PR #28 remains **open,
non-draft, unmerged, and mergeable**; it is **intentionally paused**, not
merged, and **not authorized to merge**.

Accepted evidence:

- `PASS_WITH_NOTES_3D_SCENE_FOUNDATION_REVIEW` — independent foundation
  review outcome. Repository-verified (recorded in this file and
  `RUN_QUEUE.md` prior to this sync).
- Desktop accessibility/performance Gate A — passed (~30 seconds, ~59.93 FPS
  average, minimum one-second bucket 59 FPS, zero frames above 33.3 ms or
  50 ms, nine draw calls, 2,120 triangles, one canvas, one animation loop,
  zero scene-originated errors). Repository-verified.
- `PASS_WITH_NOTES_3D_SCENE_FOUNDATION_REMEDIATION_REVIEW` — recorded as
  **operator-confirmed external/session evidence, dated 2026-07-27**. The
  operator communicated this outcome directly in this operating session; no
  corresponding PR review, commit, or `docs/tasks/` report exists in this
  repository evidencing it independently, and this paused-state sync is the
  **first canonical repository record** of that outcome.
- `PASS_WITH_NOTES_3D_SCENE_INTEGRATION_REVIEW` — recorded on the same basis:
  **operator-confirmed external/session evidence, dated 2026-07-27**, not
  independently repository-verified, first recorded here.

Open gate: physical Android Chromium **Gate B remains `OPEN / NOT EXECUTED`**.
Current outcome: `BLOCKED_3D_SCENE_QA_REFERENCE_DEVICE_UNAVAILABLE` — the
operator does not currently own or have access to a named physical Android
Chromium reference device. Repeated attempts have produced no new evidence.
This is an **environmental/process blocker**, not an application defect, not
evidence of correctness, and not risk acceptance. Emulated or desktop-browser
evidence remains provisional only and must not be presented as physical-device
evidence.

Resume condition: Gate B execution must not resume until a named physical
Android phone with Chrome/Chromium is confirmed available for approximately
15–20 minutes of testing. Until then: do not rerun Gate B, do not start QA
servers for it, and do not repeatedly request an unavailable device.

Governance: per `RECOMMEND_KEEP_PREMERGE_BLOCKER_3D_SCENE_PHYSICAL_QA`, no
repository-defined waiver process exists, Gate B remains a strict pre-merge
blocker, and no waiver, deferment, risk acceptance, merge, or deployment is
authorized for PR #28. PR #28 is intentionally paused rather than actively
queued for repeated execution.

Independent of this pause, a separate governance review —
`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001` — is the
next executable task: a read-only review of whether the current Vercel
setup's automatic publish-on-merge-to-`main` behavior is truly separate from
merge authorization, as ADR wording describes. It does not unblock, waive, or
otherwise affect PR #28's merge status.

The local dashboard's former NASA Images browser GETs have been retired from
`site/dashboard.html` / `site/js/dashboard.js` under
`MELLYCORE-SOURCE-ARENA-NASA-RUNTIME-RETIREMENT-001`, implemented on branch
`fix/mellycore-source-arena-nasa-runtime-retirement-001` and merged into
canonical `main` via PR #15 (merge commit
`e0cbc332ff90f8787d981c9d86be717633f22d4d`, reviewed head
`1478b95c82cb85fd5e0efdf433e928ca92cac69b`). Visual acceptance returned
`PASS_WITH_NON_BLOCKING_NOTES`; the two P2 findings (procedural swatch
palette, mission-rail scrollbar theming) were resolved before merge. The
Source Arena tab now renders a local, deterministic Source Archive dataset —
zero external requests, no API key. Historical NASA task reports and
`v0.2.0` release evidence remain untouched as the historical record. This
status is now canonical on `main`, not merely branch/PR-scoped.

## Specified, Not Implemented

The accepted Holographic UI specification defines Source Arena as the leading
visual metaphor and first hero image: a 390×844 mobile model-lens composition.
Overview/core/orbit/hull remains supporting imagery only. The complete
holographic/3D Source Arena, real operational adapters, and approval-execution
surface are not implemented.

The AI Operations Intelligence specification
(`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`) is **integrated
into canonical `main` via PR #7**; it defines the logical contracts for the
AI Estate Inventory, Unified Run Ledger, Skill Gap Detector, Memory Freshness
Monitor, Recommendation Ledger, exact operator-approval, and the controlled
improvement loop. It is specification only — no backend, adapter, runtime, or UI
is implemented or claimed by it; its modules remain `SPECIFIED`, not
runtime-implemented.

An accepted Source Arena Hybrid renderer decision
(`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`, status:
**ACCEPTED**, 2026-07-20, decision/specification level only) narrowly permits
a WebGL-enhanced renderer — one pinned, vendored Three.js ESM module, paired
with a mandatory complete CSS/DOM fallback — for Source Arena's central stage
only. Neither renderer is implemented; no dependency has been vendored. NASA
runtime retirement (accepted by this ADR as a prerequisite) is merged into
canonical `main` via PR #15 (merge commit
`e0cbc332ff90f8787d981c9d86be717633f22d4d`); the renderer and vendoring
themselves remain unimplemented and require their own separately-authorized
implementation task.

## Operator Decision — Option B Deploy Path

The operator selected **Option B**: the first deploy target now bundles the
cinematic showcase, the Source Arena static renderer slice, and an OpenRouter
Model/Cost Observatory as a **static snapshot only** (local fixture, no API
key, no backend, no live fetch, no model call). Full sequence and OpenRouter
Level 1/2/3 gating: `shared_context/ROADMAP.md`'s "Option B Deploy Path"
section; actionable next step: `shared_context/RUN_QUEUE.md`.

The OpenRouter Observatory spec
(`docs/specs/MELLYCORE_OPENROUTER_MODEL_OBSERVATORY_SPEC.md`) defining the
static-snapshot cockpit, local data contract, routing lanes, estimator,
safety labels, and future gates is **merged into canonical `main` via PR #20**
(merge commit `f1e177e38a26cfc80e047c8481d7932ad4419487`).

A first static-snapshot implementation slice,
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001`, adds an
Observatory tab to `site/dashboard.html` with a local static fixture
(`site/js/dashboard.js`) covering eight representative model entries; all
cost and context-window fields are `null` pending a reviewed pricing source,
so the Budget Estimator correctly shows `INSUFFICIENT PRICING DATA` rather
than inventing a number. No fixture data implies live catalog access.

Its review/remediation/polish chain, all on branch
`feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001`:
`-REVIEW-001` returned `NEEDS_FIXES` on a P1 mobile horizontal-page-scroll
defect and a P3 `obs-matrix-body` class/id naming collision;
`-REMEDIATION-001` fixed both (every direct Observatory card pinned to
`width:100%; max-width:100%; min-width:0` at the mobile breakpoint, matrix
wrapper renamed); `-REVIEW-002` returned `PASS`. Visual acceptance then found
two rounds of polish needed — `-VISUAL-POLISH-001` added a CSS/DOM router
core with orbital model nodes and reordered mobile content so advice,
selected model, estimator, and fallback precede the compact model list;
`-VISUAL-POLISH-002` closed the remaining desktop spacing gap so the Budget
Estimator's full header is visible above the fixed footer at 1440×900.
Visual acceptance 003 passed.

**This static snapshot slice is now merged into canonical `main` via
[PR #21](https://github.com/Melly-999/mellycore-aios-core/pull/21)**, merge
commit `6897b5f31528c47f1a5186de4f854484dc3d71de`, merged
2026-07-23T16:19:42Z (four commits: `84faf5b6…`, `1ae5283…`, `bebb032c…`,
`6076e12…`). The OpenRouter Observatory static snapshot is canonical, not
merely branch/PR-scoped. Current status remains:
`LIVE_API_NOT_AUTHORIZED`, `ACCOUNT_USAGE_NOT_AUTHORIZED`, `NO_API_KEYS`,
`NO_BACKEND`, `NO_MODEL_CALLS`, `NO_DEPLOY`. No live OpenRouter call, account
usage, backend/provider implementation, or deployment has occurred at any
point in this chain; Level 2 (public catalog) and Level 3 (account usage)
remain future-gated behind separate approval.

The Source Arena post-merge docs sync prerequisite is canonical via PR #19
(merge commit `b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`). At that historical
point, the next step was
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`;
that pointer is completed and superseded, not the current product task. The
current product phase remains the Control Plane specification gate stated
above.

## Source Arena Static Renderer Slice — Canonical

`MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-001` is **merged into canonical
`main` via PR #17** (https://github.com/Melly-999/mellycore-aios-core/pull/17,
branch `feat/mellycore-source-arena-renderer-static-slice-001`, reviewed head
`4af0402d9ded634ba65d14f2013d7280b46296db`), merge commit
`537a84c8132bcb5fec568b1776bc4c656af3f0c2`, merged 2026-07-23T11:41:42Z. The
Source Arena static renderer slice is now canonical on `main`, not merely
branch/PR-scoped.

Canonical outcomes of that merge:

- The Source Arena stage renders a static **holographic source map** — central
  source core, orbital source nodes (one per filtered local record), connecting
  line, orbit ring, and a command inspector panel; it flattens to a stacked
  command-panel list on mobile.
- The prior TikTok/Reels-style social-feed primary UX — engagement rail,
  `@handle`, hashtag row, and swipe/wheel/touch feed navigation — is removed.
  Selection is by node click, source queue, dot selector, or prev/next stepper.
- The orbit-clipping defect is fixed (verified in-bounds at 1440×900,
  1440×800, and 2560×1440).
- The Sourcery XSS/static-analysis `innerHTML` finding (former
  `site/js/dashboard.js:509` and `:554-561`) is remediated: both flagged sinks
  were rebuilt with DOM APIs (`createElement`/`textContent`/`setAttribute`/
  `replaceChildren`).
- Option B roadmap content merged by PR #18 is preserved; the pre-merge
  `shared_context/AGENT_HANDOFF.md` conflict was resolved before merge.
- No external, provider, backend, or deploy expansion accompanied it.

Boundaries that remain unchanged by this merge: the implementation is
**CSS/DOM-only**. The full Source Arena renderer is **not complete**; the ADR's
CSS-complete fallback renderer is **not complete**; WebGL, Three.js, and Canvas
remain **not implemented** and Three.js remains **not vendored**. NASA runtime
remains retired and the Source Archive remains local deterministic showcase
data. OpenRouter remains not implemented. No deployment or release has been
performed, and none is authorized ahead of the readiness sequence recorded in
`ROADMAP.md`.

## Planned Direction

The Observatory roadmap includes Mission Control, Agent Activity, Context Pulse,
Model Router, Unified Run Ledger, Approval Queue, Memory & Recommendation Ledger,
AI Estate Inventory, Skill Gap Detector, and Memory Freshness Monitor. These are
planned domains, not current capability claims.

`MELLYCORE-OPERATIONS-DATA-CONTRACT-001` — translating the approved logical
contracts into fixture/schema artifacts and validation requirements — is
**integrated into canonical `main` via PR #13**
(https://github.com/Melly-999/mellycore-aios-core/pull/13), merge commit
`e0db28f06613d29028df96a2d651b6dfdf2f2aa8`, from branch
`docs/mellycore-operations-data-contract-001-v2` (tip `44dde78`). Integration
is documentation/schema/fixture scope only: the fourteen dashboard-facing
fixture entities defined in
`docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`, and their
companion JSON Schema and example fixtures in `shared_context/operations/`,
now exist on canonical `main`. No adapter, backend execution, runtime-consumed
schema, or safety-rule change was implemented or authorized by this merge.

`MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001` had already
selected `-v2` as the canonical integration candidate ahead of this merge;
the original, differently-scoped `docs/mellycore-operations-data-contract-001`
branch (2026-07-19) remains unmerged, unpushed, and superseded — its
adoptable content (AI Estate Inventory, Skill Gap Detector, Memory Freshness
Monitor entities and its Truthful-State Labels reference) had already been
folded into `-v2` before this merge by
`MELLYCORE-OPERATIONS-DATA-CONTRACT-AI-ESTATE-SKILLGAP-MEMORY-001`, bringing
it to fourteen entities total.

Full merge evidence and validation: durable report
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-POST-MERGE-STATE-SYNC-001.md`.
The original task report,
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md`, is a historical
snapshot of local-only, unpushed state prior to reconciliation and merge; it
is not a current-state claim. Real adapters, backend execution, and guarded
runtime work remain deferred to later, separately approved work.

## Release and Historical Integrity

`v0.2.0` remains the official historical release of Live Cockpit V2 / Social
Source Arena. PR #4 subsequently merged the accepted documentation-only
Holographic UI specification. Exact release, PR, branch, and commit evidence
lives in Git history and completed reports under `docs/tasks/`; it is not copied
throughout current shared context.

Earlier graph, loop, Context Gate, cockpit, provider-demo, release, and UI-spec
milestones remain preserved in their task reports and repository history.

## Safety Boundaries

- MellyCore AIOS is separate from MellyTrade; no trading or broker operations.
- No provider keys, credentials, `.env` values, account identifiers, or private
  runtime state in the repository.
- No autonomous merge, deployment, safety-rule mutation, or uncontrolled tool use.
- No production backend or recommendation execution is claimed.
- Remote mutation, implementation, deployment, and release work require separate
  explicit authorization.
