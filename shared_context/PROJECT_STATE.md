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
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001`, is
**implemented on branch
`feat/mellycore-openrouter-model-observatory-static-snapshot-slice-001` (four
local commits, not pushed, not merged)**. It adds an Observatory tab to
`site/dashboard.html` with a local static fixture (`site/js/dashboard.js`)
covering eight representative model entries; all cost and context-window
fields are `null` pending a reviewed pricing source, so the Budget Estimator
correctly shows `INSUFFICIENT PRICING DATA` rather than inventing a number.
No fixture data implies live catalog access. Current status remains:
`LIVE_API_NOT_AUTHORIZED`, `ACCOUNT_USAGE_NOT_AUTHORIZED`, `NO_API_KEYS`,
`NO_BACKEND`, `NO_MODEL_CALLS`, `NO_DEPLOY`. No push, PR, merge, or deploy
occurred.

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REVIEW-001`
returned `NEEDS_FIXES_STATIC_SNAPSHOT_SLICE_REVIEW`: a P1 mobile
horizontal-page-scroll defect (`.obs-main { display: contents }` at the
mobile breakpoint let descendant grid/flex/table content inflate each
card's own rendered width past the viewport) and a P3 `obs-matrix-body`
class/id naming collision. Both are **fixed on the same branch** by
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-REMEDIATION-001`
(second local commit): every direct Observatory card is now pinned to
`width:100%; max-width:100%; min-width:0` at the mobile breakpoint, and the
matrix wrapper `<div>` was renamed off the `obs-matrix-body` string. Verified
zero horizontal page overflow at 320px and 375px, with desktop, Source
Arena, and all interactions unaffected.

Technical re-review returned `PASS_STATIC_SNAPSHOT_SLICE_REVIEW_002`.
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-001` then returned
`NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE`: the first viewport
was catalogue-first, the model constellation lacked a router-core/orbital
metaphor, mobile advice followed the full model list, and the mobile status
bar plus secondary mono copy needed refinement.

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-POLISH-001` is complete as the
third local commit on the same branch, not pushed or merged. The Observatory
now uses a CSS/DOM local router core with orbital model nodes; Route Advisor
appears in the first 1440×900 viewport; mobile DOM and visual order put
advice, selected model, estimator, and fallback before the compact model
list; 320px/375px remain width-contained.

Visual acceptance 002 returned
`NEEDS_POLISH_OPENROUTER_OBSERVATORY_VISUAL_ACCEPTANCE_002`: the Budget
Estimator began at y=851 while the fixed footer began at y=847, leaving no
budget state visible in the first desktop viewport.

`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-POLISH-002` is complete as the
fourth local commit, not pushed or merged. A desktop-only spacing adjustment
moves the grid from y=312 to y=241 and the Budget Estimator from y=851 to
y=780; its full header ends at y=839 above the footer at y=847. Mobile order,
width containment, interactions, data, safety wording, and provider boundary
remain unchanged.

The Source Arena post-merge docs sync prerequisite is canonical via PR #19
(merge commit `b72bcbdacb61435f7cbc150fffc50ff87d1f3db9`). The exact next task is
`MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-003`.

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
