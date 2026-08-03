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
non-draft, and unmerged**; GitHub reports **`CONFLICTING / DIRTY`**. It is
**intentionally paused** and **not authorized to merge**.

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

Independent of this pause, a separate governance chain —
`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001`, then
`-MODEL-DECISION-001`, then `-MODEL-A-CONTRACT-IMPLEMENTATION-001` — has
completed: the Operator has selected Model A (temporary, static-phase-only
combined merge/deployment authorization). See "Production Deployment
Authorization — Model A Contract (Temporary, Static-Phase Only)" below. This
selection does not unblock, waive, or otherwise affect PR #28's merge
status — PR #28's physical Gate B is an independent gate, unaffected by the
deployment-authorization model. At the time of this record, the next task
was `MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-REVIEW-001`; that task
has since completed. Current executable task sequencing is maintained in
`shared_context/RUN_QUEUE.md` and echoed in `shared_context/AGENT_HANDOFF.md`.

## Production Deployment Authorization — Confirmed Mismatch

`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-CONTRACT-REVIEW-001`
(2026-07-27) independently confirmed, via read-only Git/GitHub API evidence,
that merging a pull request into canonical `main` currently causes the
Vercel Git integration to create a public Production deployment
automatically — five consecutive recent `main` merges were each followed by
a successful Production deployment within 8–14 seconds, all created by
`vercel[bot]`. Feature branches deploy to `Preview` only. **There is no
separate human deployment-approval step after merge.**

Verified enforcement state: `main` has no branch protection (`gh api
branches/main/protection` → `"Branch not protected"`), the repository has no
rulesets (`gh api rulesets` → `[]`), and the Production GitHub environment
has no protection rules. No repository workflow YAML, `vercel.json`,
`.vercel`, or `package.json` exists; the deployment trigger is external
(`VERCEL_GIT_INTEGRATION`). **Merge authorization is procedural only;
deployment authorization is not separately technically enforced.**

This is a confirmed **operational control mismatch**, a **technical
enforcement gap**, and a prior **truthful-state overclaim** in this
repository's own documentation (this file's Safety Boundaries below,
`ROADMAP.md`'s Safety Gates, and `shared_context/SAFETY_CONTRACT.md`
previously stated or implied that deployment is separately authorized from
merge, without qualification). It is **not** an accepted permanent policy —
merge approval does **not** thereby permanently constitute deployment
approval — and the explicit-operator-control requirement for production
publication remains in force.

Pre-decision interim operating rule — superseded on 2026-07-27 by the
temporary Model A contract below and retained here as historical context:
every proposed merge into `main` must be treated as an immediate
public-publication request; no agent may recommend or perform a merge
unless immediate public publication is acceptable, and no agent may
describe merge and Production deployment as independently gated.

Two authorization models were presented by
`MELLYCORE-PRODUCTION-DEPLOYMENT-AUTHORIZATION-MODEL-DECISION-001` as
unresolved options: Model A (combined static-site authorization) and Model B
(separate merge and deployment authorization). **The Operator has since
selected Model A**, verbatim recorded in `shared_context/DECISIONS.md`
(2026-07-27). See "Production Deployment Authorization — Model A Contract
(Temporary, Static-Phase Only)" immediately below for the full selected
contract.

## Production Deployment Authorization — Model A Contract (Temporary, Static-Phase Only)

**Selected model:** Model A — combined static-site authorization. **Decision
authority:** the Operator (sole authority; verbatim statement in
`shared_context/DECISIONS.md`, 2026-07-27). **Scope:** strictly the current
static, non-sensitive, non-runtime showcase phase. This section is the
canonical detailed contract; `SAFETY_CONTRACT.md`, `ROADMAP.md`, `AGENTS.md`,
and `RUN_QUEUE.md` each carry a shorter pointer back to it.

**Per-merge authorization rule (binding):**

- Every merge into `main` requires explicit Operator approval for that
  **specific** pull request — never a blanket, standing, batch, inferred, or
  future authorization.
- Approval for one specific merge authorizes **only** the automatic Vercel
  Production publication caused by that specific merge — not any other
  merge, past or future.
- Every merge-authorization request must explicitly warn that merging into
  `main` immediately updates the public Production host.
- No agent may merge on its own initiative under any circumstance.
- Prior merge approvals never imply approval for a later merge.

**Post-merge Production verification (required, not permission to merge):**

- After an authorized merge, verify that the expected Production deployment
  actually completed and that the accepted public host
  (`https://mellycore-aios-core.vercel.app`) remains reachable.
- Where evidence permits, verify the live deployment corresponds to the
  expected canonical commit (e.g. via the GitHub deployments API, as done in
  this and prior sessions).
- Report verification honestly; do not claim Production deployment success
  without direct evidence.

**Rollback boundary:**

- Rollback must remain practical for the static-showcase phase (Vercel
  supports promoting a prior deployment; this is a capability note, not a
  claim that a rollback procedure has been configured or validated in this
  repository).
- Any concrete rollback action still requires its own separate, explicit
  Operator authorization — Model A does not pre-authorize rollback.
- No rollback mechanism is claimed as already configured or tested by this
  record.

**Branch-protection and technical-enforcement boundary:**

- Model A creates **no** branch protection, repository ruleset, environment
  protection rule, CI/required-check enforcement, or separate technical
  deployment gate. None of these exist today (independently reverified:
  `main` branch protection `404 "Branch not protected"`; rulesets `[]`;
  `Production`/`Preview` environment `protection_rules: []`).
- Current merge authorization remains **procedural only** — enforced by
  Operator discipline at merge time, not by any technical control.
- The absence of branch protection is accepted only as a **temporary**
  condition of the current sole-Operator boundary; it is not endorsed as a
  permanent state and is itself one of the migration triggers below
  (delegated merge authority or multiple active maintainers).

**Mandatory, blocking migration triggers (Model B reconsideration required before implementation or merge of any of the following):**

1. First backend endpoint.
2. First authentication flow.
3. First stored user data.
4. First runtime secret.
5. First live provider connection.
6. First execution-capable agent.
7. First external write-capable integration.
8. First financial or trading action.
9. Delegated merge authority or multiple active maintainers.

These triggers are **blocking, not advisory** — no agent may classify any of
them as optional polish or post-implementation cleanup. While any trigger
applies and the deployment-model migration gate is unresolved: no affected
implementation task may proceed to merge; Model A must not silently
continue past the trigger; a separate governance decision and
capability-research task (`MELLYCORE-PRODUCTION-DEPLOYMENT-SEPARATION-CAPABILITY-RESEARCH-001`,
per the prior decision task) are required before that implementation or
merge may proceed.

**PR #28 boundary:** Model A selection does **not** authorize, unblock,
waive, replace, defer, or otherwise weaken PR #28's gates. PR #28 remains
open, unmerged, and not authorized to merge; physical Android Chromium Gate
B remains `OPEN / NOT EXECUTED`; no physical-QA waiver or risk acceptance is
created by this decision. Any eventual PR #28 merge request must
independently satisfy every one of its own gates (including Gate B) and must
separately include the Model A Production-impact warning above.

At the time of this record, the next task was
`MELLYCORE-PRODUCTION-DEPLOYMENT-MODEL-A-CONTRACT-REVIEW-001` — an
independent, read-only review verifying this contract's implementation, not
a publication, merge, or deployment task, and not related to closing PR
#28's physical Gate B. That task has since completed. Current executable
task sequencing is maintained in `shared_context/RUN_QUEUE.md` and echoed
in `shared_context/AGENT_HANDOFF.md`.

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
only. Canonical `main` has no accepted renderer implementation and no
canonical vendored dependency. NASA runtime retirement (accepted by this ADR
as a prerequisite) is merged into canonical `main` via PR #15 (merge commit
`e0cbc332ff90f8787d981c9d86be717633f22d4d`); the renderer and vendored
Three.js module are implemented on paused, open, unmerged PR #28 (see "3D
Scene Foundation — PR #28 Paused State" above) but remain non-canonical,
unmerged, and blocked by physical Android Chromium Gate B
(`OPEN / NOT EXECUTED`).

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
**CSS/DOM-only**. The full Source Arena renderer is **not complete on
canonical `main`**; the ADR's CSS-complete fallback renderer is **not
complete on canonical `main`**; WebGL, Three.js, and Canvas remain **not
accepted on canonical `main`**, which has no vendored Three.js dependency.
The renderer and vendored Three.js module are implemented on paused, open,
unmerged PR #28 (see "3D Scene Foundation — PR #28 Paused State" above), but
remain non-canonical, unmerged, and blocked by physical Android Chromium
Gate B (`OPEN / NOT EXECUTED`). NASA runtime remains retired and the Source
Archive remains local deterministic showcase data. OpenRouter remains not
implemented. No deployment or release has been performed, and none is
authorized ahead of the readiness sequence recorded in `ROADMAP.md`.

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
- No autonomous merge, safety-rule mutation, or uncontrolled tool use by an
  agent or operator without explicit approval. **Note:** per the Operator's
  Model A selection (2026-07-27, see "Production Deployment Authorization —
  Model A Contract" above), each individual merge approval also authorizes
  only the automatic Production publication that specific merge causes —
  this is not blanket authorization, and Production deployment remains
  procedurally, not technically, enforced.
- No production backend or recommendation execution is claimed.
- Remote mutation, implementation, and release work require separate
  explicit authorization. Deployment currently follows an authorized merge
  automatically via the Vercel Git integration, with no additional
  technical gate; per Model A this is the Operator's accepted temporary
  policy for the static-showcase phase only — see "Production Deployment
  Authorization — Model A Contract" above for the full contract and
  migration triggers.

## OpenAI Batch API — Stage B Merged, Stage C Unauthorized

[PR #32](https://github.com/Melly-999/mellycore-aios-core/pull/32) merged the
Stage B controlled-activation foundation into canonical `main` at
`2026-07-30T22:19:15Z` using GitHub's merge-commit method. Canonical `main`
now points to merge commit
`5e7628a72a22fc10ecd0f9a25515ab61eb7223b9`, whose parents are, in order,
`81b1baf9da5363ef088fe236de93d6cd3713b659` and
`2b08a2c18f85e07cb1b6ade3ba79f01b2424395b`. The merge tree is identical to
the reviewed-head tree. All seven reviewed PR commits, from `8bd40b4…`
through `2b08a2c…`, are therefore part of canonical `main`.

PR #32 changed exactly 13 authorized files: five files under
`scripts/mellycore_batch/`, five Batch test files, and the three governance
documents `shared_context/AGENT_HANDOFF.md`, `shared_context/PROJECT_STATE.md`,
and `shared_context/SAFETY_CONTRACT.md`. It changed no `site/**` file.
The `site` tree remained exactly
`5df8bb686ebeb5b13bcf1fe2ad2ef6bc796bfc5d` across the merge.

The merge triggered an automatic Vercel Git deployment to Production:
GitHub deployment `5683195625`, Vercel deployment
`dpl_Bvijm1GRww7nVaLG4TwnUWBkZmuw`, deployment SHA
`5e7628a72a22fc10ecd0f9a25515ab61eb7223b9`. GitHub reported `success`;
Vercel reported `READY`; the accepted public host
`https://mellycore-aios-core.vercel.app` returned HTTP 200. No manual
promotion, redeployment, cancellation, or other deployment mutation occurred.
No page-level visual acceptance was performed or claimed. Because the static
tree was unchanged, this deployment added no provider-secret dependency,
backend route, serverless function, or Batch execution surface.

`scripts/mellycore_batch/activation.py` is a local-only, fail-closed
activation-control layer on top of the already-merged Batch foundation
(`feat/mellycore-openai-batch-api-foundation-001`, head
`d19dd2417d1a1008e976608c5560d858b5fb9574`). Stage B is now merged, but it
remains planning and validation only: it does not connect to OpenAI, does not
import the `openai` SDK in any reachable path, and does not cross migration
trigger #5. No provider connection, credentialed request, upload, Batch
operation, or paid action occurred during implementation review, merge, or
this local documentation state sync. The OpenAI SDK remained absent from the
reviewed environment.

**Governance chain:**

- Capability research: `MELLYCORE-PRODUCTION-DEPLOYMENT-SEPARATION-CAPABILITY-RESEARCH-001`
  returned `PASS_WITH_REQUIRED_CONTROLS_DEPLOYMENT_SEPARATION_CAPABILITY_RESEARCH_001` and
  selected **LOCAL OPERATOR-ONLY EXECUTION** as the deployment-separation
  architecture for any future live Batch activity: a human operator runs the
  CLI locally, with credentials in their own local environment only, never
  in Vercel, GitHub Actions, or any other hosted execution surface.
- Pricing evidence: `MELLYCORE-OPENAI-BATCH-PRICING-EVIDENCE-001` returned
  `PASS_WITH_CONSERVATIVE_LIMITS_MELLYCORE_OPENAI_BATCH_PRICING_EVIDENCE_001`,
  `verified_at: 2026-07-28T22:00:34Z`, `valid_until: 2026-08-27T22:00:34Z`.
  `scripts/mellycore_batch/openai_batch_pricing.json` records this evidence
  with a SHA-256 integrity digest over its own content. The digest detects
  content changes that have not been deliberately re-digested; independent
  Python constants additionally dual-lock every reviewed pricing,
  provenance, validity-window, capability, and envelope field so recomputing
  the digest cannot make substituted evidence authoritative. `activation.py`
  refuses to plan at or after `valid_until`.
- Model B reconsideration: `MELLYCORE-MODEL-B-LIVE-PROVIDER-TRIGGER-5-DECISION-002`
  returned `APPROVE_CONSTRAINED_MODEL_B_TRIGGER_5_TRANSITION_002` with status
  `STAGE_B_IMPLEMENTATION_AUTHORIZED`. That decision explicitly did **not**
  authorize Stage C: `STAGE_C_LIVE_BATCH_SMOKE_NOT_AUTHORIZED`,
  `MIGRATION_TRIGGER_5_NOT_YET_CROSSED`, and
  `USD_0_01_SPEND_NOT_AUTHORIZED_BY_THIS_DECISION` all remain true after the
  Stage B merge.

**What Stage B is:** exact-model enforcement (`gpt-5.4-nano-2026-03-17`
only); a hard request/input/output envelope (max 3 requests, max 65,536
input bytes, max 512 output tokens per request, max 1,536 total output
tokens); Decimal-only cost estimation against a hard `USD 0.01` cap (the
worst-case envelope estimates to `USD 0.0075136`, about 75% of the cap);
rejection of tools, web/file search, code interpreter, image/file/audio
input, external URLs, and any request-body field outside an explicit
allowlist; a one-time, non-secret local authorization-artifact schema and a
fixed production consumption ledger derived with the Windows Local AppData
Known Folder API at
`<LocalAppData>\MellyCore\batch\authorizations`. Callers, CLI arguments,
environment variables, configuration, and authorization artifacts cannot
select or override that root. Repository paths, repository ancestors,
children, `.git`, and worktree administrative paths are explicitly excluded
with case-insensitive component comparisons. The only root-taking helper is
private and retained for isolated filesystem tests; production calls resolve
the fixed root internally. Before marker access, the implementation opens and
validates a non-reparse local directory boundary; marker creation is relative
to that directory handle and exclusive (create-once; reuse rejected), so
symlinks, junctions, and other Windows reparse points are refused rather than
followed. A hardcoded Stage C kill switch
(`stage_c_live_execution_authorized = False`) that no manifest,
authorization artifact, CLI flag, or environment variable this package reads
can set to `True`.

**What Stage B is not:** it does not construct an OpenAI client, does not
upload a file, does not create/poll/cancel a Batch, and does not spend any
money. `scripts/mellycore_batch/policy.py`'s hardcoded
`live_provider_connections_allowed = false` and the
`LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5` block (exit code
`78`) are unchanged and remain the sole, independent gate in front of every
provider-backed CLI command (`submit`, `status`, `list`, `download`,
`cancel`); Stage B's `activation-preflight` command is a separate, additive
local-planning command, not a replacement for that gate.

**Trigger #5 status:** migration trigger #5 ("first live provider
connection") is **not** crossed by the merge and is only ever crossed by an
actual, successful, credentialed connection to the OpenAI API — something
this Stage B layer is explicitly designed never to perform. Stage C (an
actual live Batch smoke test) remains a separate, not-yet-authorized future
decision task: `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`.
The hard `USD 0.01` spend boundary is likewise unavailable until separately
authorized.

**Production separation:** the reviewed Stage B change touched only files
under `scripts/mellycore_batch/`, `tests/`, and the minimal
`shared_context/` delta described above. Nothing under `site/**`,
`vercel.json`, or `.github/**` changed, so the existing static Production
boundary (Vercel Root Directory `site`, static-only, no provider
SDK/credential/backend route/serverless function/Batch execution capability)
remains intact.

**Requirements-live.txt SDK version:** the Operator supplied the exact,
local-only declaration `openai==2.48.0`. It is recorded as the sole line in
`scripts/mellycore_batch/requirements-live.txt`; Stage B neither installs nor
imports it. A previous worker performed a prohibited read-only
`pip index versions openai` lookup. That policy violation is disclosed in
the task completion report, and its output is not treated as authority for
this pin. The pin's authority is the Operator's direct instruction.

**Finite pricing authority:** pricing evidence was verified at
`2026-07-28T22:00:34Z` and expires at `2026-08-27T22:00:34Z`. It remains
authoritative only within that stated validity window and must be revalidated
when the policy requires it, including at or after expiry and before any
separately authorized live-smoke decision that depends on current pricing.

**Independent adjacent state:** PR #28 remains open, non-draft, unmerged,
intentionally paused, and currently `CONFLICTING / DIRTY` at
`57bb841e67e9a5d557f88bf096537eba78df1cd8`; auto-merge remains absent.
Physical Android Chromium Gate B remains `OPEN / NOT EXECUTED`. PR #32 and
this state-sync task did not modify PR #28 or execute Gate B.

**Review observations and incident:** F1 and N1–N7 remain deferred
non-blocking observations. The prior prohibited PyPI lookup remains
disclosed; its output is not authority for the dependency pin. Neither the
merge nor this state sync closes, suppresses, or upgrades those observations.

**PR #33 — merged.** Original state-sync commit
`472fcd21e828a71f5d5cc6fbd8ab8bc4573e12d4` was independently reviewed
locally, published, and opened as
[PR #33](https://github.com/Melly-999/mellycore-aios-core/pull/33). After
remediation 001 (`c0f69c5a4e6aa41e738d0c271c70e1e8ec585d3c`), remediation 002
(`ab5a6d775ff86bc051788ca2927e17c3d8eab880`), publication/reconciliation, and
independent review 002
(`PASS_MELLYCORE_OPENAI_BATCH_API_CONTROLLED_ACTIVATION_POST_MERGE_STATE_SYNC_PR_REVIEW_002`),
PR #33 was merged at `2026-07-31T15:52:54Z` using GitHub's merge-commit
method. The exact reviewed head `ab5a6d775ff86bc051788ca2927e17c3d8eab880`
is the second parent of merge commit
`f118110181fe5428940ac86256dedc63f52282a6`; first parent is
`5e7628a72a22fc10ecd0f9a25515ab61eb7223b9`. The merge tree
(`e49a392614b10be2e235dcb85ad374004bbced0b`) is identical to the reviewed-head
tree, and canonical `main` now points to the merge commit. PR #33 retained
its exact three-commit, five-file documentation-only scope and changed no
`site/**` file; the static `site` tree remained
`5df8bb686ebeb5b13bcf1fe2ad2ef6bc796bfc5d` across the merge. The source
branch `docs/mellycore-openai-batch-post-merge-state-sync-001` is preserved,
unmerged mergeability is no longer applicable, and the one Codex thread
(`discussion_r3690288402`) is resolved with a published evidence reply
matching the merged state.

The automatic Vercel Git deployment succeeded in Production for the exact
merge commit: GitHub deployment `5694313001`, SHA
`f118110181fe5428940ac86256dedc63f52282a6`, state `success`, source
automatic Git deployment. The accepted public host
`https://mellycore-aios-core.vercel.app` returned HTTP 200. No manual
deployment action, promotion, redeploy, or cancellation occurred, and no
page-level visual acceptance was performed or claimed. The exact Vercel
deployment ID was not obtainable from the read-only sources available to the
reconciliation task (no authenticated Vercel CLI/API access in that
environment); it is recorded as not independently verified rather than
invented.

**Final canonical reconciliation.** This record
(`MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-001`)
is the durable Stage B governance baseline reflecting the merged, deployed
state above. At the creation of its local documentation commit
(`docs: reconcile final Batch activation state`, parent
`f118110181fe5428940ac86256dedc63f52282a6`), that commit is local-only and
unreviewed — a time-scoped creation-time fact, not a permanent claim about
this file's own content. The exact immediate next task at creation time is
`MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-FINAL-CANONICAL-STATE-RECONCILIATION-REVIEW-001`.
Only a PASS there may advance to
`-RECONCILIATION-PUSH-001`, then `-RECONCILIATION-PR-CREATION-001`, then
`-RECONCILIATION-PR-REVIEW-001`, then `-RECONCILIATION-MERGE-001`. Once that
chain independently reviews, merges, and Production-verifies this
reconciliation content into canonical `main`, the canonical state it
describes is the final reconciled Stage B governance baseline and no further
state-sync task is required solely to restate the PR #33 merge recorded
above. The next eligible task then becomes
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` — a separate decision
task, not live execution authorization. None of this authorizes Stage C,
provider connection, migration trigger #5, or USD 0.01 spend. Task-record
next-task fields remain creation-time historical snapshots, superseded by
this file, `AGENT_HANDOFF.md`, and `RUN_QUEUE.md`.

## Enterprise Provider Integration — Architectural Research Recorded (Not Implemented)

`MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001` records, for the first time
in this repository, architectural research and a proposed direction covering
enterprise integration fabrics, cybersecurity providers, marketing
providers, Cloudflare, and the OpenClaw gateway reference. This entry is a
**documentation-only synchronization**: it records completed research and
proposed direction, not implementation, credentials, or runtime. It is
**independent of, and does not reorder, reprioritize, or supersede,** the
OpenAI Batch API Controlled Activation track above (see "OpenAI Batch API —
Stage B Merged, Stage C Unauthorized" below) or any other active gate in
this file.

**Integration fabrics evaluated:** Composio, n8n, Pipedream Connect, Tray.ai
Agent Gateway, Workato, Zapier MCP, and OpenClaw (architectural reference
only). **Accepted architecture direction**, per the canonical decision
record
(`docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`,
`MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001`, decision/
specification level only):
Composio as a developer-first managed-authentication and agent-tool
candidate; private self-hosted n8n as a deterministic workflow/automation
candidate; Pipedream as a possible long-tail API fallback; Tray.ai or
Workato as later enterprise-governance candidates; Zapier MCP for broad
marketing/business integrations, not as the cybersecurity execution
boundary; direct native adapters preferred for deterministic, high-trust
cybersecurity operations. None of these fabrics is connected, authenticated,
or authorized for use.

**OpenClaw — architectural reference, not a runtime dependency.** OpenClaw's
gateway assumes a trusted-operator boundary; a shared operator-level gateway
must not be treated as hostile multi-tenant isolation. Session keys are
routing/context selectors, not authorization. Operator-level
OpenResponses-style endpoints must not be exposed directly to an untrusted
frontend. Every MellyCore tenant requires separately enforced identity,
credentials, scopes, policy, and audit boundaries. Provider output and
external content are treated as untrusted and potentially prompt-injected.
Read and write credentials must be separated; write credentials must never
enter model context. Consequential operations require policy evaluation,
approval, attribution, idempotency protection, and read-after-write
verification. These findings inform MellyCore AIOS's own future
integration-gateway design; no OpenClaw code, service, or dependency is
adopted, vendored, or connected by this record.

**Cybersecurity provider candidates.** P0: Microsoft Defender XDR /
Microsoft Graph Security, GitHub Advanced Security, Cloudflare, Okta.
P1/P2: Splunk, CrowdStrike Falcon, Snyk. No cybersecurity provider is
connected, authenticated, or authorized for any action, including
read-only access.

**Marketing provider candidates.** P0: HubSpot, Google Ads, Google
Analytics 4, Meta Marketing API, LinkedIn Marketing API, Twilio Segment.
Later/vertical: Salesforce Marketing Cloud, Braze, Klaviyo, Adobe Experience
Platform. No marketing provider is connected, authenticated, or authorized
for any action.

**Cloudflare — promoted to a P0 cybersecurity-provider candidate.** A future
`Cloudflare Application & API Security Provider` is proposed, scoped to API
Shield, API Discovery, Endpoint Management, endpoint labels, Authentication
Posture, Schema Validation 2.0, WAF Rulesets, and audit/security events,
under controlled MCP-assisted investigation only. This is a candidate
definition, not an implemented connector: no Cloudflare API has been
called, no Cloudflare credential exists in this repository or its
environment, and no Cloudflare MCP server is connected. Recorded legacy
exclusions and forward direction, binding on any future connector-contract
task: the deprecated Firewall Rules API must not be used for new
integration — the Rulesets API is the future WAF custom-rule direction;
`/api_gateway/user_schemas/hosts` must not be used for new integration —
Schema Validation 2.0 surfaces are preferred; managed-label replacement
operations are consequential bulk mutations; the Schema Validation `block`
action is a production-impacting security action; full unrestricted
Cloudflare MCP execution must not be exposed to autonomous agents; direct
native APIs are preferred over MCP for deterministic production security
operations; any future Cloudflare MCP use is restricted to a strict
capability allowlist behind a MellyCore approval broker.

**Safety boundaries recorded by this entry** (additive to, not a
replacement for, this file's "Safety Boundaries" section above and
`shared_context/SAFETY_CONTRACT.md`): research and provider prioritization
do not authorize implementation, credentials, or execution; initial
provider access, if ever authorized, must be read-only by default;
marketing send/publish/activation/audience/budget/deletion actions are
consequential; cybersecurity isolation/blocking/remediation/
credential-revocation/WAF-mutation/schema-blocking/incident-resolution
actions are critical; every tenant requires an isolated authorization
boundary; service-account credentials must not silently replace delegated
user identity; provider credentials must never enter model context; session
identifiers are never authorization; external provider content is always
untrusted; tool output can never override system, operator, or repository
safety rules; every mutation requires policy evaluation, approval,
idempotency protection, attribution, and read-after-write verification.

**Implementation status.** No Cloudflare, cybersecurity, marketing,
integration-fabric, or OpenClaw-derived connector has been implemented. No
provider credential has been configured. No provider API has been
authenticated or called. No provider MCP server is connected. No runtime
provider gateway is authorized. No marketing campaign action is authorized.
No cybersecurity remediation action is authorized. Provider adapter
scaffolding remains blocked until the documentation and integration-review
gates below pass and are separately authorized.

**Canonical architecture decision — complete.**
`MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001` locked provider
integration classes, integration-fabric selection, cybersecurity/marketing
provider tiers, the Cloudflare decision, OpenClaw findings, tenant
isolation, identity/credential model, capability/risk/approval model,
audit/verification model, and external-content posture as **architecture
and sequencing direction only** — it authorizes no implementation,
credentials, provider authentication, API execution, or deployment.
Canonical decision:
`docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`.
Durable report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001.md`.

**Cloudflare connector contract — complete.**
`MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001` defined the
canonical Cloudflare Application & API Security Provider connector
contract: four authorization domains, 58 capability IDs (16 read-only,
16 proposal-only, 23 approval-required mutations, 3 operator-investigation)
plus 13 explicitly prohibited capabilities, R0–R5 classification with no
R3 capability, credential profiles with strict read/write separation, a
mandatory 17-stage Schema Validation rollout in which zone-wide `block` is
always R5, WAF Rulesets mutation safety, Endpoint Management deletion as an
R5 irreversible action, complete-diff label replacement, documentation-only
MCP, mandatory read-after-write verification, and non-optional audit. Its
verified legacy exclusions are the Firewall Rules API, the Filters API,
Classic Schema Validation, and `/api_gateway/user_schemas/hosts`. This is
**specification-level acceptance only** — it authorizes no implementation,
credential, provider authentication, Cloudflare API call (including
read-only), MCP connection, or deployment. Canonical contract:
`docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`.
Durable report:
`docs/tasks/MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001.md`.

**Document-integrity remediation — complete.**
`MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001`
corrected fifteen stale internal section cross-references in the accepted
ADR (a numbering defect, not an architectural conflict — no risk tier,
capability, credential, or gate content changed) and recorded the
Cloudflare task's single unpublished-commit amend as a classified
procedural deviation (`PASS_WITH_PROCEDURAL_DEVIATION`) via a new,
append-only commit — no existing commit was amended, reset, rebased, or
squashed. This is a documentation-integrity correction, not a new
architectural milestone. Durable report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md`.

**Provider Registry contract extension — complete.**
`MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001` defined the canonical
registry contract enabling any enterprise, cybersecurity, marketing,
integration-fabric, or restricted-MCP provider to be described through one
fail-closed record structure. Its core rule is that **registration is not
authorization**: provider registered, adapter implemented, credential
configured, credential verified, tenant authorized, capability authorized,
runtime enabled, and operation approved are **eight independent,
conjunctive facts**, and no field may collapse them. Lifecycle is split
across three orthogonal axes (record governance, adapter implementation,
and the authorization facts), so no lifecycle state can imply credentials
or production use. It reuses the existing canonical `sensitivity_level`
vocabulary rather than inventing a parallel scale, extends — without
modifying — the Control Plane spec's §7.2 entity catalogue and §9.1
Provider Registry module, and represents the Cloudflare contract's 58
capabilities and legacy exclusions with no weakening (recording Cloudflare
as `contract_defined`, not `conformance_verified`, because that contract's
own open `UNVERIFIED` items remain). This is **specification-level
acceptance only** — it authorizes no registry implementation, adapter,
credential, provider authentication, provider API call (including
read-only), MCP or fabric connection, or deployment. Canonical contract:
`docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`.
Durable report:
`docs/tasks/MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001.md`.

**Integration Gateway security contract — specification complete after recovery remediation.**
`MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` defined the
enforcement boundary between MellyCore and every external system. Its
central decision is that **the Gateway is a policy-enforcement boundary,
not a proxy**: it never forwards a caller's request, but re-derives every
authorization input from authoritative records and constructs a new bounded
provider request. Every caller claim and every provider response is
untrusted. It fixes a twelve-identity model, a ten-link acting-identity
chain that may never be broken, merged, or substituted, a **deterministic
26-step policy-evaluation order** in which no later step may compensate for
a failed earlier one and credentials are never resolved before
authorization passes, twelve-element approval binding extending the Control
Plane's four-field core, mandatory `INDETERMINATE` reconciliation instead
of blind mutation retry, **six independent delivery statuses** never
collapsed into one `success`, a durable audit-intent reservation before
R3–R5 external mutation followed by a separate completion append, and the rule
that no inbound webhook or provider event can cause MellyCore to act on
that provider. It is the Data Plane architecture and threat model that the
Control Plane spec's §3.2 requires, and extends that spec's §9.6 display
module without modifying it. Cloudflare conformance was demonstrated across
six representative flows with **no weakening detected**. This is
**specification-level acceptance only** — it authorizes no Gateway
implementation, adapter, credential, provider authentication, provider API
call (including read-only), MCP or fabric connection, webhook
registration, or deployment. Canonical contract:
`docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.
Durable report:
`docs/tasks/MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001.md`.

**Cybersecurity Provider Pack — specification complete.**
`MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` defines the first
read-oriented provider pack across P0 Microsoft Defender XDR / Microsoft
Graph Security, GitHub Advanced Security, Cloudflare, and Okta; P1 Splunk
and CrowdStrike Falcon; and P2 Snyk. It establishes thirteen normalized
security entities, stable common capability families, provider-specific
read mappings, explicit normalization-loss and uncertainty handling, and
an initial **R0-R2 ceiling**. All R3-R5 provider mutation, containment,
identity, policy, remediation, repository-write, and remote-response
surfaces remain deferred and unauthorized. Pack membership and provider
tier are sequencing metadata only and do not collapse or satisfy the
Provider Registry's eight independent facts. The Integration Gateway
remains the enforcement boundary, and the accepted Cloudflare connector
contract remains authoritative. This is specification-level acceptance
only: no provider was connected; no credential, adapter, runtime, or
webhook was configured; no provider API, MCP, or fabric operation occurred;
and no deployment was authorized. Canonical specification:
`docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`. Durable
report:
`docs/tasks/MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001.md`.

**Marketing Provider Pack — specification complete.**
`MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` defines a zero-trust,
read-oriented provider pack across P0 HubSpot, Google Analytics 4, Google
Ads, Meta Marketing API, LinkedIn Marketing API, and Twilio Segment; P1
Salesforce Marketing Cloud, Braze, and Klaviyo; and P2 Adobe Experience
Platform. It establishes 22 separate normalized marketing entity kinds,
stable read/report/proposal capability families, provider-specific mappings,
and explicit identity, tenant, consent, purpose, sensitivity, metric,
attribution, provenance, and normalization-loss requirements. Initial scope
is strictly **R0-R2**; all R3-R5 tracking, mutation, audience activation,
campaign/send, CRM/identity/consent change, and export surfaces remain
deferred and unauthorized. Pack membership and provider tier are sequencing
metadata only and do not satisfy the Provider Registry's eight independent
facts. This is specification-level acceptance only: no provider was
connected; no credential, adapter, runtime, tracking, audience, campaign,
webhook, protected API, MCP/fabric operation, or deployment was authorized
or performed. Canonical specification:
`docs/specs/MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md`. Durable report:
`docs/tasks/MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001.md`.

**Enterprise-provider documentation integration review — complete; gate
failed.** `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001`
reviewed the complete local chain across 25 documents, 26 integration
dimensions, and 12 determinism scenarios. The result is
`FAIL_REMEDIATION_REQUIRED`: P0 = 0, P1 = 4, P2 = 2, P3 = 3. Blocking
incompatibilities concern Cybersecurity Pack provider IDs, the conflicting
Cloudflare provider projection, unmapped pack credential classes, and the
missing/misdirected integration-fabric comparison prerequisite. Canonical
review:
`docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md`.
Durable review report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md`.

The exact next task on this parallel track is
`MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001`.

**Enterprise-provider documentation integration remediation — complete.**
`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001` closes all
nine review-001 findings: canonical provider IDs and Cloudflare identity;
Registry-owned reusable credential classes and authorization records;
Gateway-owned deterministic resolution/evaluation; a new file-backed Fabric
Comparison and native-equivalence standard; and the three reference/narrative
repairs. Canonical new specification:
`docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`. Durable report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md`.
This is documentation-only and makes no claim that review-002 has passed.

**Enterprise-provider documentation integration review 002 — complete; gate
failed.** `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002`
independently re-ran the documentation gate against the remediated chain across
19 documents and 16 determinism scenarios. Result:
`FAIL_REMEDIATION_REQUIRED` with P0 = 0, P1 = 1, P2 = 0, P3 = 3. Eight of the
nine review-001 findings are independently verified `CLOSED`; review-001
`P1-003` (credential-class mapping) is `PARTIALLY_CLOSED`. The remaining
blocker is `P1-201`: the remediation made Provider Registry §13.2 a closed,
mandatory eight-value credential-profile-class catalogue binding on
provider-specific contracts, but the already-accepted Cloudflare connector
contract still declares `CF_READ`, `CF_WRITE_CONTROLLED`, `CF_CONTAIN`, and
`CF_MCP_OPERATOR` with no projection onto those eight —
`CF_MCP_OPERATOR` maps to none of them — and Integration Gateway §§34.1–34.6
still label those values "Credential class" although Gateway §14.2 now denies
anything that is not one exact Registry §13.2 identifier. Three P3 maintenance
findings also remain. Canonical review:
`docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md`.
Durable review report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md`.
The documentation gate has **not** passed. No provider is connected,
authenticated, credentialed, enabled, live, deployed, or implemented, and no
credential exists.

**Enterprise-provider credential-class conformance remediation — complete;
closure unverified.**
`MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001`
publishes one deterministic model: Registry §13.2 owns nine canonical classes;
Gateway §14.2 resolves exactly one concrete profile; Cloudflare `CF_*` values
are provider-specific requirement labels projected before runtime; and
`CF_MCP_OPERATOR` maps to the operator-bound, documentation/investigation-only,
non-provider-access class `restricted_operator_investigation`. Zero or multiple
compatible profiles deny. No best-available selection, delegated-user to
service-account fallback, or read-to-write widening exists. The three Review
002 P3 maintenance findings are also routed in their canonical documents.

This documentation-only remediation is **not** a documentation-gate PASS.

**Enterprise-provider documentation integration review 003 — complete; gate
failed.** `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003`
independently verified the credential-class remediation across 17 documents and
16 determinism scenarios. Result: `FAIL_REMEDIATION_REQUIRED` with P0 = 0,
P1 = 2, P2 = 1, P3 = 2. `P1-201` is `PARTIALLY_CLOSED`: four of its six
sub-defects are independently verified closed — the ninth canonical class
exists, D4 binds exactly one class, the residual `credential_class:
investigation` value is derived and non-normative with no runtime use anywhere,
and `CF_READ` now resolves to exactly one read class before runtime. Two
sub-defects remain open, both concerning the operator-bound restricted
documentation/investigation path:

- `P1-301` — Integration Gateway §9.2, Rule 16.7, §17 step 13, and the §23
  request envelope admit only `delegated_user` or `service_account` as the
  acting identity, so a request bound to `restricted_operator_investigation`,
  whose Registry-declared `identity_type` is `mellycore_operator`, has no
  resolvable acting identity — while Gateway §34.6 and Cloudflare §25.2 present
  a reachable D4 path.
- `P1-302` — Registry §26.1 declares `required_scope_dimensions: tenant,
  account, zone` for provider `cloudflare` and §11.2 rule 2 fails closed on a
  missing required dimension, while Cloudflare §11.2 rule 2 requires the D4
  label to carry an empty account, zone, and resource binding.

Both findings fail in the deny direction. No safety regression was found: the
58 Cloudflare capability rows and 13 prohibition rows are byte-identical to the
pre-remediation commit, all risk classifications are intact, the eight
authorization facts remain separate, and the documentation-only class carries
no provider account, provider API, or mutation authority. Canonical review:
`docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md`.
Durable review report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003.md`.

The documentation gate has **not** passed. At the time of Review 003, the exact
next enterprise-provider task was
`MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001`,
which must reconcile the Gateway acting-identity model and the Registry
provider-record scope model with the ninth canonical class without weakening
any fail-closed default, and route the remaining P2 and P3 findings. A further
independent review must follow it. No provider runtime, credential, provider
API, MCP/fabric connection, mutation, or scaffold is authorized.

**Enterprise-provider restricted-tool path conformance remediation — complete;
closure unverified.**
`MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001`
defines one Registry-owned acting-identity vocabulary (`delegated_user`,
`service_account`, `mellycore_operator`), the canonical
`required_acting_identity_type` field, capability-level scope applicability,
the separate authentication-target vocabulary, and exact restricted-tool
registration/scope. Gateway now represents the constrained operator identity
through evaluation, envelope, and audit. Cloudflare D4 binds
`mellycore_operator`, `restricted_operator_investigation`, target
`restricted_tool`, provider-native account/zone/resource explicitly
`not_applicable`, and exact tool scope. `mcp_oauth_grant`, if used, is a
tool/server grant only and cannot become Cloudflare authentication.

This documentation-only remediation is **not** a documentation-gate PASS.
`P1-301` and `P1-302` remain unverified until an independent Review 004. No
restricted tool is connected, no MCP execution is authorized, no provider
runtime or API is authorized, and no credential exists. At the time of that
remediation, the exact next enterprise-provider task was
`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004`.

**Enterprise-provider documentation integration review 004 — complete;
documentation gate passed with non-blocking findings.**
`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004` independently
verified the restricted-tool-path remediation commit
`b90ce82ab497469ea3c8b8c0f3c8be8ce8717dbd`. Outcome:
`PASS_WITH_NON_BLOCKING_FINDINGS`. Finding counts: P0 0, P1 0, P2 0, P3 3.
All five Review 003 findings — `P1-301`, `P1-302`, `P2-301`, `P3-301`, and
`P3-302` — are independently verified `CLOSED`; none is partially closed.

Verified independently from contract text, not from the remediation's claims:
Provider Registry §7.5 is the sole owner of exactly three canonical
acting-identity types; `required_acting_identity_type` is the single canonical
selector, bound before credential resolution and immutable for one evaluation;
Registry §12.1 owns exactly three authentication targets, with mode and target
as independent fields; scope applicability is capability-level with exactly
three values, and `not_applicable` is permitted only where a provider contract
explicitly allows it — for Cloudflare, Domain 4 alone. `mellycore_operator` is
neither provider-account nor provider-API eligible and is never a fallback.
Restricted-tool OAuth cannot become provider OAuth. Cloudflare retains 58
capability rows and 13 prohibition rows, byte-identical to the pre-remediation
commit, with Domain 4 unchanged at three R0 documentation-only capabilities.
All 24 replayed scenarios resolve deterministically; none requires
architectural interpretation.

Three non-blocking P3 observations remain: `P3-401` (Registry §7.5's table has
a malformed delimiter row and may not render as a table; its raw text is
complete and unambiguous), `P3-402` (two intra-Registry references were not
updated for the §14.1 renumbering), and `P3-403` (no non-provider-operated
restricted-tool OAuth authority is identified, so `mcp_oauth_grant` may be
unselectable in practice for Domain 4). None changes any runtime decision.

Canonical review record:
`docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_004.md`.
Durable review report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004.md`.

**Provider Adapter Scaffold 001 — complete as an inert local code scaffold.**
`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` consumed Review 004's
`PASS_WITH_NON_BLOCKING_FINDINGS` gate and created a standard-library Python
3.9 package under `scripts/provider_adapters/`. The package defines closed
canonical vocabularies, immutable provider/capability/scope/envelope/fact
contracts, typed sanitized failures, static manifest and envelope validation,
a provider-neutral protocol, and a disabled adapter. Tests provide one
fixture-only in-memory adapter. The scaffold uses Review 004 §36's four
constraints directly: raw Registry §7.5 vocabulary values, field names rather
than ordinals, no selectable restricted-tool OAuth mode, and an execution state
that remains disabled under Gateway Rule 32.1.

The scaffold implements no real provider adapter and creates no provider
registration. No credential is configured or verified; no tenant or capability
is authorized; no runtime is enabled; no operation is approved; no network
transport, provider access, provider SDK, credential lookup, OAuth flow, MCP
execution, integration-fabric connection, or execution-success path exists.
Adapter existence remains distinct from every one of the eight authorization
facts. At the time of that record, the exact next enterprise-provider task was
`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-REVIEW-001`. Every concrete provider
adapter remained blocked, unimplemented, and unauthorized pending that
independent review and separate Operator authorization.

**Provider adapter scaffold review 001 — complete; scaffold gate passed with
non-blocking findings.** `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-REVIEW-001`
independently reviewed scaffold commit `311ee3f…` against the accepted Registry,
Gateway, Cloudflare, provider-pack, fabric-comparison, and ADR contracts and
against Review 004 §36. Outcome: `PASS_WITH_NON_BLOCKING_FINDINGS`. P0 = 0,
P1 = 0, P2 = 6, P3 = 5.

Verified independently rather than from the scaffold's claims: the nine
credential-profile classes, three acting identities, three authentication
targets, three scope-applicability values, and R0–R5 are exact, closed, and free
of alias, case, whitespace, or fuzzy coercion; the provider-ID grammar is
byte-identical to Registry §7; the class→identity and class→target closures
reproduce Registry §13.2 verbatim; Registry §11's scope rules each deny
independently and a missing declaration never becomes `not_applicable`; the
eight authorization facts are eight separate fields with no aggregate or derived
member; 26 of 27 adversarial envelope paths and 15 of 15 manifest paths deny with
stable typed codes; every model is frozen and no field is declared with a mutable
container type; a 90-combination redaction sweep produced zero leaks; static AST
analysis and a runtime import audit confirm zero network, environment,
subprocess, dynamic-import, or provider-SDK behavior; and 129 execution probes,
including all 128 standing-fact combinations and the all-eight-satisfied case,
produced only `EXECUTION_DISABLED`. No execution-success outcome is
representable. Both claimed test counts reproduce exactly: 62 focused and 636
full, with compile exit `0` and the project validator `PASS`.

The six P2 findings are recorded constraints, not blockers: the runtime-enable
reference is never required even when fact 7 is `satisfied`; the disabled
guarantee is not sealed against subclassing; the fixture sensitive-text screen is
narrower than validation's; several security-relevant validation branches are
untested; `authentication_mode` has no representation; and `event_verification`
capabilities are unrepresentable. Each fails closed.

The scaffold gate is passed. `MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-001`
is **eligible for separate authorization** under the seven constraints recorded
in the review record. It is not authorized, not started, not implemented, not
connected, not authenticated, not enabled, and not live. The review itself starts
and authorizes no concrete adapter. No provider is registered, no credential is
configured or verified, no tenant or capability is authorized, no runtime is
enabled, no operation is approved, and no provider connection exists.

The exact next enterprise-provider task is
`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-001`.

This result does
not reorder the global OpenAI Batch pointer, which remains
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`.

Durable task reports:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001.md` and
`docs/tasks/MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-REVIEW-001.md`. Canonical
review: `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md`.

## Cloudflare API Shield Read-Only Adapter 001 — Local Implementation Complete, Review Required

`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-001` is complete on its
local implementation branch. A transportless Cloudflare provider descriptor,
two identity-specific 16-entry read-only manifests, immutable operation plans,
Cloudflare scope enforcement, and bounded synthetic fixture normalization now
exist over the unchanged provider-neutral scaffold. All 58 accepted Cloudflare
capabilities are classified: 16 D1 reads included; 16 D2 proposals, 19 D3
mutations, 4 D3 containment capabilities, and 3 D4 restricted-tool capabilities
excluded.

This code is concrete only in provider semantics and remains inert in execution.
No network transport or endpoint exists; no Cloudflare endpoint was contacted;
no SDK was added; no credential was configured or verified; no provider
authentication occurred; no tenant or capability was authorized; no runtime was
enabled; no operation was approved; and no MCP, fabric, webhook, proposal,
mutation, containment, or execution-success path exists. Fixture normalization
is local evidence only and cannot claim a provider request.

Current validation: 42 Cloudflare-focused tests, 62 neutral-scaffold tests, and
678 full-suite tests pass; compile exits `0`; the project validator reports
`PASS`. The exact next enterprise-provider task is
`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-001`. Any live
Cloudflare transport, credential, authentication, deployment, or runtime work
remains blocked pending that independent review and separate Operator
authorization. The pre-existing global higher-priority task pointer is
unchanged, not reordered, and not reinterpreted.

## Cloudflare API Shield Read-Only Adapter Review 001 — Failed, Remediation Required

`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-001` independently
reviewed commit `3de6a4961a6ba4d20b7bc133298292ff1f0fc71c`. Decision:
`FAIL_REMEDIATION_REQUIRED`; P0 = 0, P1 = 1, P2 = 2, P3 = 0.

The contract-derived 58-row classification is complete and matches the code:
16 D1 reads included and 42 proposal, mutation, containment, and D4 restricted-
tool capabilities excluded. Both fixed identity manifests remain transportless
and execution-disabled; all required tests replayed successfully and independent
AST/import/execution probes found no network, credential, provider, SDK, OAuth,
MCP, webhook, mutation, or success path.

The gate nevertheless fails. P1-01 records that no concrete capability/profile
pins the authentication mode required by Provider Registry Section 13.2. The
delegated entries bind `read_only_delegated`, whose compatible mode is
`delegated_oauth`, while the implementation supplies only global non-runtime
`api_token` metadata. Scaffold Review 001 required an explicit descriptor
extension and binding rules; treating metadata as sufficient would require
forbidden architectural interpretation. P2-01 records unflagged acceptance of
an endpoint-URL-shaped fixture host. P2-02 records incomplete independent
contract-oracle coverage in the focused tests.

The offline adapter is unaccepted and the provider-foundation checkpoint remains
incomplete. Live provider work remains blocked; the Agent Runtime pivot waits.
The exact next task is
`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REMEDIATION-001`.
The pre-existing global higher-priority pointer remains unchanged and is not
reordered or reinterpreted.

## Cloudflare API Shield Read-Only Adapter Remediation 001 — Local Implementation Complete, Review 002 Required

`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REMEDIATION-001` remediates
Review 001 findings P1-01, P2-01, and P2-02. Each of the 16 delegated entries
now binds `delegated_oauth`; each of the 16 service entries binds scoped
`api_token`. Provider-specific frozen validation closes mode/class/identity/
target compatibility and rejects missing, unknown, aliased, case/whitespace-
varied, or mismatched values. Global metadata names both variants separately,
and operation plans preserve the concrete mode. No generic scaffold or envelope
change was required.

Synthetic fixture hosts now use a closed reserved-host grammar. URL schemes,
userinfo, path/query/fragment material, slashes, controls, whitespace,
sensitive-shaped text, and excessive length deny locally without echo. Focused
tests contain an independent literal 58-row contract oracle and expanded
authentication, scope, fixture, plan, subclass, execution, and error coverage.
The production 58-row classification remains unchanged: 16 D1 reads included
and 42 proposal, mutation, containment, and restricted-tool rows excluded.

This remediation remains transportless, credentialless, unauthenticated, and
execution-disabled. Its claims remain unverified until independent Review 002;
provider foundation remains incomplete, live Cloudflare remains blocked, and
Agent Runtime remains blocked. The exact next task is
`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002`.
The pre-existing global higher-priority pointer remains unchanged and is not
reordered or reinterpreted.

## Cloudflare API Shield Read-Only Adapter Review 002 — Passed With Non-Blocking Findings; Provider-Foundation Checkpoint Complete

`MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002` independently
reviewed remediation commit `1a9acd2f1ad7b4597bce795d5d626424f34466e2` without
trusting its report and without repairing anything. The outcome is
`PASS_WITH_NON_BLOCKING_FINDINGS` with P0 = 0, P1 = 0, P2 = 2, P3 = 1. The
record is `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md`.

All three Review 001 findings are independently verified `CLOSED`. For `P1-01`,
all 32 concrete entries collapse to exactly one tuple per identity variant —
delegated binds `delegated_oauth` with `read_only_delegated` / `delegated_user`
/ `provider_account`, service binds `api_token` with `read_only_service` /
`service_account` / `provider_account` — the mode enum is closed at two members
with no `_missing_` hook and no case, whitespace or raw-string coercion,
descriptor and plan modes agree for all 32, and 15 descriptor, 5 plan and 4
global-metadata adversarial constructions all deny. Both mode values are
determined by the closed Registry and Cloudflare tables rather than chosen, so
no architectural interpretation was required. For `P2-01`, the fixture-host
grammar is fail-closed across 46 host strings and 6 hostile objects, and no
denial echoes its input. For `P2-02`, the 58-row test oracle is a distinct
literal object that detects missing, extra, renamed, recategorized and
risk-drifted capabilities.

No regression was found. Review 001's own 58-row table matches current
production classification exactly; manifest, plan, scope, fixture,
execution-disabled and sensitive-data behaviour are unchanged; and the neutral
scaffold, canonical contracts, Scaffold Review 001, Review 001 and the
remediation report are byte-identical by SHA-256. Validation: 60
Cloudflare-focused, 62 neutral-scaffold and 696 full-suite tests pass; compile
and the project validator pass; Black, flake8 and mypy are `NOT_AVAILABLE` and
are not claimed passing.

Three new non-blocking findings are recorded. `P2-03`: a `str` subclass passes
every fixture gate and escapes normalization into `host`, `canonical_ref` and
`provider_native_ref`, and because `_state_digest` calls `repr()`, a crafted
subclass produced a demonstrated digest collision between two different
fixtures; it must close before `state_digest` or normalized string fields are
consumed downstream. `P2-04`: Registry §26.1 records Cloudflare
`supported_auth_modes` as scoped `api_token` for the provider API and no
Cloudflare-track contract enumerates `delegated_oauth`, leaving an open
registration-time question that must resolve before any Cloudflare provider
record or credential profile is created; it does not block here because
registration is `not_registered`, credentials are `unsupported`, and execution
is disabled. `P3-01`: structurally malformed references are denied with a
sensitive-value error code.

The offline Cloudflare adapter checkpoint is accepted and the provider-
foundation checkpoint is complete for the current milestone, under those
constraints. Further live-provider development is deferred. Live Cloudflare
transport, credentials, authentication, OAuth, token creation, MCP connection,
webhook, provider API access including read-only calls, mutation, containment,
registration, runtime enablement and deployment all remain blocked and
unauthorized.

At the time of that review, the exact next main product task was
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001`, eligible for separate
authorization and then not started, not authorized, not approved, not active,
and not implemented. That statement is a creation-time historical record; the
task has since completed as an architecture specification — see "Agent Runtime
Architecture Spec 001" below. The pre-existing global higher-priority pointer
remains unchanged and is not reordered or reinterpreted.

## Agent Runtime Architecture Spec 001 — Architecture Specified, Nothing Implemented

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001` is **complete as one local
documentation commit; not pushed.** It creates the canonical architecture
specification for the MellyCore Agent Runtime:
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`. Durable report:
`docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md`.

The specification defines the Agent Runtime as a **control and coordination
layer** that must not own provider credentials, provider transport,
model-provider SDK credentials, canonical Shared Context truth, permanent
external tool trust, deployment infrastructure, or MellyTrade execution. It
covers six frameworks as a closed vocabulary — Claude Code, the OpenAI Agents
SDK, LangGraph, CrewAI, AutoGen, and custom MellyCore-compatible agents —
across 43 sections: fifteen canonical identifiers; nine separated
definition-to-instance states; expected Agent Package Contract metadata; one
framework-neutral bridge boundary; seventeen `run_state` values with allowed,
forbidden, and evidence-bearing transitions; separated run, attempt, step,
sub-run, retry, and replay semantics; **eleven conjunctive authorization
facts**; an immutable digest-bound execution envelope; seven Shared Context
operations; six memory categories; context-flow tracing; six handoff kinds;
seven tool stages; the single governed provider path; the Model Router
boundary; separated cost estimates and actuals; the Run Ledger producer
relationship; twelve event categories; honest cancellation and timeout
semantics; retry and reconciliation rules; eight isolation boundaries;
human-in-the-loop requirements; sixteen threats with prevention, detection,
fail-closed result, and audit evidence; the external-content posture; 38
Agent Runtime-layer error classes; operator observability information
architecture; a 6 × 13 framework compatibility matrix; seven runtime modes;
the inert v1 scaffold boundary; and **32 deterministic scenarios**.

Canonical ownership is reused, not re-decided. Provider Registry §21.1's
**eight independent facts remain exactly eight**; the eleven runtime facts add
runtime-layer facts without collapsing any of them, and provider authorization
delegates entirely to the Registry and the Integration Gateway. The Gateway's
§25.2 error classes are adopted unchanged rather than fragmented. The Run
Ledger record remains owned by
`docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` §5. The Control
Plane's six status dimensions are unmodified: `run_state` is declared a typed
entity field, not a seventh dimension, consistent with that spec's §7.1.

**Cloudflare Review 002 constraints are carried forward, not adjudicated.**
`P2-03` becomes a canonical-serialization and digest discipline: exact built-in
primitive types at trust boundaries, rejection or canonical conversion of
primitive subclasses, serialization independent of `repr()` and every other
overridable object protocol, deterministic hashing over normalized bytes,
type-tagged fields, no identity from arbitrary object representations, and
collision-resistant digest rules — binding on run fingerprints, context-block
hashes, artifact references, handoff envelopes, tool-result identities,
model-response identities, audit records, and replay records. `P2-04` is
recorded explicitly as a provider-registration constraint that **must be
resolved or formally adjudicated before** provider registration, credential
configuration, credential verification, live Cloudflare transport, and
delegated Cloudflare execution; no Cloudflare delegated authentication is
assumed and no agent is bound to a Cloudflare authentication mode. `P3-01`
becomes distinct error semantics: structurally malformed input is never
collapsed into a sensitive-data error.

**Implementation status: nothing was implemented.** No Agent Runtime, agent
registry, agent package, framework bridge, or scaffold exists. No agent
framework is installed, imported, connected, or executed — Claude Code, the
OpenAI Agents SDK, LangGraph, CrewAI, and AutoGen are absent from this
repository and its reviewed environment. Zero agents have been executed. No
model provider is connected and no model-provider call has occurred. No tool is
connected and no tool has been invoked. No provider is connected, registered,
authenticated, or enabled. No credential is configured. No context or memory
backend is implemented. No queue is implemented. No frontend is implemented.
The framework compatibility matrix is an architectural planning position, not
verified capability testing, and every cell must be independently validated by
the future Framework Bridge Contract task.

Migration triggers #1, #4, #5, #6, and #7 are implicated by later phases of
this architecture and are **not** crossed by this documentation task. Trigger
#6 ("first execution-capable agent") blocks any future task that would make an
agent execution-capable until the Model B reconsideration required by the
Model A contract is separately completed.

**Exact next task at the time of that specification:**
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` — an independent,
read-only architecture review. That statement is a creation-time historical
record; the review has since completed with
`FAIL_REMEDIATION_REQUIRED` — see "Agent Runtime Architecture Spec Review 001"
below. Live provider work remains deferred and blocked. The pre-existing global
higher-priority pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`
remains unchanged and is not reordered or reinterpreted.

## Agent Runtime Architecture Spec Review 001 — Architecture Gate Failed, Remediation Required

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` is **complete as one
local documentation commit; not pushed.** It is an independent, read-only
architecture, security, consistency, and implementability review of
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` at commit
`17da8603fbe8b75082cfea44223745b3c63f14de`. Review record:
`docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md`. Durable
report: `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001.md`.

**Gate decision: `FAIL_REMEDIATION_REQUIRED`. P0 = 0, P1 = 4, P2 = 5, P3 = 5.**

The reviewer did not author the specification and treated every architectural
claim as unverified. Every numeric dimension was recounted directly from the
specification text; all 17 lifecycle states, 11 authorization facts, and 6
frameworks were accounted for; all 32 original scenarios and 10 additional
adversarial scenarios were replayed; and 20 ownership concerns were assessed
independently against the canonical owners, yielding 13 `CONSISTENT`, 2
`COMPLEMENTARY`, 2 `AMBIGUOUS`, and **3 `CONFLICTING`**.

**No P0 exists.** No direct credential or provider path, no cross-tenant
execution possibility, no canonical-context mutation bypass, no authorization or
approval bypass, no secret exposure, and no unsafe consequential retry was
found. The canonical serialization and digest discipline carrying Cloudflare
`P2-03`, the package/runtime separation, the framework-bridge prohibitions, the
memory categories, the handoff acceptance model, the single governed provider
path, the cancellation honesty model, the retry and reconciliation rules, the
isolation boundaries, the approval properties, the security model, the
external-content posture, the runtime modes, and the inert v1 boundary all
passed independent review without a finding.

**Four blocking findings:**

- `P1-01` — §12.2 projects six `run_state` values to `lifecycle_status:active`,
  which Control Plane §8.2 states MUST NOT describe a running agent; the two
  Control Plane modules that render Runs (§9.5, §9.7) enumerate a Run lifecycle
  set containing neither `active`, `queued`, `draft`, nor `ready`.
- `P1-02` — Authorization facts 5 and 6 duplicate Provider Registry facts 5 and
  6. Registry §21.3 defines both record types as provider-scoped and requiring a
  `provider_id`, while runtime fact 10 already delegates entirely to all eight
  Registry facts; the capability vocabulary fact 6 evaluates is unstated.
- `P1-03` — Multiple attempts per `run_id` with per-attempt ledger evidence
  contradicts AI Operations Intelligence §5.9 (deduplication by `run_id`) and
  §5.1 (one `outcome`/`model`/`provider` per run), which the Agent Runtime, as a
  declared non-owner, cannot amend.
- `P1-04` — §23.6 mandates `run_state:waiting_for_operator` for an unresolved
  routing tie, but §12.3 does not permit that transition from
  `waiting_for_model`, the state §12.2 assigns to awaiting a routing decision.

Non-blocking findings: `P2-01` undefined stale-snapshot policy; `P2-02`
`model_routing_decision_ref` inside an immutable, digest-bound envelope; `P2-03`
agent-run identity not reconciled with the existing run-ledger `run_id` form or
with loop runs; `P2-04` concurrent broadcast acceptance unspecified; `P2-05`
runtime-instance restart with an attempt in an unknown state unaddressed; and
five editorial findings `P3-01`–`P3-05`, including three count discrepancies
(context-flow trace is 16 fields not 17; handoff envelope contents are 12 not
11; 38 error rows carry 40 distinct class names).

**Cloudflare constraints are unchanged by this review.** `P2-03` is correctly
carried forward and materially strengthened; `P2-04` is correctly carried
forward and explicitly **not** resolved or adjudicated; `P3-01` is correctly
discharged in structure. The provider checkpoint is correctly not treated as
live-provider readiness.

**Implementation status: nothing implemented, connected, or executed.** No Agent
Runtime, agent registry, agent package, framework bridge, or scaffold exists. No
agent framework was installed, imported, connected, or executed by this review.
Zero agents have been executed. No model provider, tool, or provider is
connected. No credential is configured. No context or memory backend, queue, or
frontend is implemented. Exactly one network operation occurred during the
review: one authorized read-only `git fetch clean-origin`.

**Agent Package eligibility:** `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` is
**not eligible** for authorization. Agent Package Contract, Framework Bridge
Contract, Shared Context Bridge, Agent Runtime Scaffold, first Agent Package,
Cross-Agent Smoke, and Integration Review **remain blocked**. Agent Runtime
implementation remains blocked.

**Exact next task at the time of that review:**
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001`. That statement is a
creation-time historical record; the remediation has since completed — see
"Agent Runtime Architecture Spec Remediation 001" below.

Live provider work remains deferred and blocked. Migration triggers #1, #4, #5,
#6, and #7 remain uncrossed. The pre-existing global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged and is
not reordered or reinterpreted.

## Agent Runtime Architecture Spec Remediation 001 — Seams Resolved, Verification Pending

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001` is **complete as one
local documentation commit; not pushed.** It remediates all fourteen findings of
Architecture Review 001 (P1 = 4, P2 = 5, P3 = 5; P0 was 0).

**A canonical seam-decision record was created before any owner document was
edited:** `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md`.
Durable report:
`docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001.md`.

Three of the four blocking findings were seam conflicts across three owners. The
governing rule applied throughout: the existing owner wins unless it provably
cannot represent the required semantics, and a seam is never hidden by
redefining another subsystem's vocabulary inside the Agent Runtime document.

**`P1-01` — lifecycle projection.** The Control Plane's lifecycle enum contained
no member meaning "executing", and §8.2 explicitly forbids `active` for a running
agent. Four conforming alternatives were tested and rejected. The Control Plane
was **minimally amended**: one additive enum member `running`, one §8.2 clause
defining it, and the Run lifecycle sets in §9.5, §9.7, and §9.10 extended. The
`active` prohibition is preserved verbatim. The Agent Runtime now publishes a
complete 17-row projection table; six states project to `running`, two to
`blocked`, and **none to `active`**.

**`P1-02` — authorization facts.** Resolved **entirely inside the Agent
Runtime**; the Provider Registry is **byte-identical** and its eight facts remain
exactly eight. Facts 5 and 6 became runtime-scoped
(`tenant_agent_runtime_authorization`, `tenant_agent_capability_authorization`)
with an agent capability vocabulary explicitly disjoint from the provider
capability vocabulary, and normative rules in both directions preventing either
record type from satisfying the other's fact. Evaluation points were fixed:
facts 1–8 are run-admission facts; facts 9–11 are per-invocation.

**`P1-03` — Run Ledger identity.** Deduplication keyed on `run_id` alone cannot
preserve two attempts of one run, so AI Operations Intelligence §5 was
**minimally amended**: `ledger_record_id` as the deduplication identity, optional
`attempt_id`, optional `run_kind`, and a §5.9 rule that records differing in
`attempt_id` are distinct and **MUST NOT be deduplicated**, with logical-run
summaries derived and never replacing attempt evidence. All fields are optional
with defined absent semantics, so existing loop run ledgers remain conforming
**unmodified** and the higher-precedence loop schemas were not edited.

**`P1-04` — routing tie.** Resolved inside the Agent Runtime: the three
in-flight waiting states may now escalate to `waiting_for_operator`, the
transition table is declared closed, and new §12.3.1 fixes predecessors,
triggers, evidence, and release conditions.

**P2 closures:** a deterministic six-condition stale-snapshot policy (§17.4); an
immutable envelope revision chain with an explicit 8-step authorization sequence
(§15.4); `run_kind` identity namespacing that keeps agent runs and loop runs
unconfusable without renaming or absorbing the Loop Operations model (§8.4);
single-winner atomic broadcast acceptance where no recipient gains scope by
racing (§20.4); and a 16-row restart-recovery matrix in which no unknown attempt
is ever blindly redispatched (§29.3).

**P3 closures:** all counts recalculated from the document's own tables and
recorded as normative metrics in new §1.4 — context-flow trace is **17** fields,
handoff envelope contents **12**, error taxonomy **49 rows and 49 distinct class
names** under a new one-class-per-row invariant, and **42** deterministic
scenarios (32 original + 10 additional, added as §38.1).
`INSUFFICIENT_PRICING_DATA` was given an owner and definition, the nine-state ↔
eleven-fact mapping was stated (§9.1), and normative wording was made
implementation-neutral.

**Canonical owners amended: two, both additively** — the Control Plane and AI
Operations Intelligence. **Unchanged and byte-identical:** Provider Registry,
Integration Gateway, Operations Data Contract, Loop Operations Architecture, all
loop schemas, all Shared Context contracts, the Safety Contract, Validation, the
Enterprise Provider ADR, both prior reviews, and both original task reports.

**Remediation claims are unverified.** This task remediated its own reviewed
findings; no independent party has confirmed the closures, and the architecture
gate is **not** re-opened by this task.

**Implementation status: nothing implemented, connected, or executed.** No Agent
Runtime, agent registry, agent package, framework bridge, or scaffold exists. No
agent framework is installed, imported, connected, or executed. Zero agents have
been executed. No model provider, tool, or provider is connected. No credential
is configured. No context or memory backend, queue, or frontend is implemented.
Exactly one network operation occurred: one authorized read-only
`git fetch clean-origin`.

**Exact next task:** `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` — an
independent, read-only re-review of the remediated architecture, the
seam-decision record, and both owner amendments.

**Agent Package Contract remains blocked** pending Review 002, as do the
Framework Bridge Contract, Shared Context Bridge, Agent Runtime Scaffold, first
Agent Package, Cross-Agent Smoke, and Integration Review. Agent Runtime
implementation remains blocked. Live provider work remains deferred and blocked.
Migration triggers #1, #4, #5, #6, and #7 remain uncrossed. The pre-existing
global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged and is
not reordered or reinterpreted.

## Agent Runtime Architecture Spec Review 002 — Architecture Gate Passed With Non-Blocking Findings

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` is **complete as one
local documentation commit; not pushed.** It is an independent, read-only
re-review of remediation commit `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` by a
party that did not author the remediation. Every remediation claim was treated
as unverified until independently reproduced. Durable evidence:
`docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md` and
`docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002.md`.

**Gate decision: `PASS_WITH_NON_BLOCKING_FINDINGS`.** P0 = 0, P1 = 0, P2 = 0,
P3 = 1 (new). **All fourteen Review 001 findings are independently `CLOSED`** —
none partially closed, none reopened, no regression introduced.

**The remediation's claims held under independent replay.** `P1-01` — the
Control Plane amendment adds exactly one lifecycle member `running`, leaves the
`active` bullet unchanged with its prohibition explicitly reaffirmed, and the
recounted 17-row projection uses `active` **zero** times. `P1-02` — facts 5 and
6 are now runtime-scoped record types with rules in both directions preventing
either from satisfying the other's fact, and a run proposing no provider
operation needs facts 1–8 only and never a `provider_id`. `P1-03` — AI
Operations §5.9 now makes records differing in `attempt_id` distinct and
non-deduplicable, and a full-document sweep found no surviving clause implying
one outcome per `run_id`. `P1-04` — the transition is listed, the transition
table is declared closed, and Scenario 15 resolves by a single listed transition
with no intermediate hop.

**Both owner amendments are minimal, additive, and bounded.** The Control Plane
extension of §9.5/§9.7 to nine lifecycle values is exactly what the projection
requires — `draft`, `queued`, and `ready` are the projections of rows 1, 4, and
3 — and §9.8 correctly did **not** receive `running`, because its key entities
are `QueueItem`/`Task`/`Artifact` with no `Run`. A repository sweep confirmed no
JSON schema or Python module enforces a `lifecycle_status` enum and no JSON file
contains an `"active"` enum value, so no validator, schema, or fixture is
invalidated.

**Provider Registry is byte-identical** and remains the sole owner of provider
authorization. Integration Gateway, Operations Data Contract, Loop Operations
Architecture, all loop schemas, all Shared Context contracts, the Safety
Contract, Validation, and Architecture Review 001 are likewise byte-identical.
Loop compatibility holds without a schema change: `RUN_LEDGER_SCHEMA.json` sets
`"additionalProperties": true`, and absent `run_kind`/`attempt_id` reproduce
existing loop behavior exactly.

**Counts were recalculated mechanically, not accepted from prose.** Two count
findings were fixed **structurally**: `P3-01` by adding a genuinely required
17th context-flow trace field (`destination_run_id`), and `P3-03` by splitting
the multi-class error row under a normative one-class-per-row invariant —
independently counted as 49 rows and 49 distinct class names with zero
duplicates. All **42** deterministic scenarios resolve, IDs 1–42, no gaps or
duplicates.

**One new non-blocking finding, `NEW-P3-01`:** the specification's §12.2
projection note 5 claims every projected value is renderable by Control Plane
§9.5, §9.7, **and §9.10**; it holds for the two Run-bearing modules but not for
§9.10, whose lifecycle set omits `draft` and `cancelled`. This is an inaccurate
completeness claim in a non-normative note, not a semantic incompatibility —
§9.10 is an explicitly cross-dimensional summary that did not enumerate
`cancelled` before the amendment either, and §34 independently requires operator
surfaces to display `run_state` rather than only the projection. It is recorded,
not repaired; this review repaired nothing.

**Architecture accepted** as the canonical foundation for the Agent Runtime
track, under that single non-blocking constraint. **All eighteen Agent Package
concerns are specifiable without architectural invention**, including the two
Review 001 blocked on.

**Implementation status: nothing implemented, connected, or executed.** No Agent
Runtime, agent registry, agent package, framework bridge, or scaffold exists. No
agent framework is installed, imported, connected, or executed. Zero agents have
been executed. No model provider, tool, or provider is connected. No credential
is configured. Exactly one network operation occurred: one authorized read-only
`git fetch clean-origin`.

**Exact next task:** `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` — a
documentation-only Agent Package Contract specification, now **eligible for
separate Operator authorization** under the `NEW-P3-01` constraint. Eligibility
is not authorization: it is not started and is not authorized by this review.

Agent Runtime implementation, the Framework Bridge Contract, the Shared Context
Bridge, the Agent Runtime Scaffold, the first Agent Package, Cross-Agent Smoke,
and Integration Review all **remain blocked**. Live provider work remains
deferred and blocked; Gateway §32's seventeen-item enablement gate still governs
and none of it passes. Cloudflare Review 002 `P2-04` remains carried forward and
unresolved. Migration triggers #1, #4, #5, #6, and #7 remain uncrossed. The
pre-existing global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged and is
not reordered or reinterpreted.

## Agent Package Contract Spec 001 — Developer Platform Direction Recorded (Documentation Synchronization, Not Implemented)

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` moved from `ELIGIBLE` to
`IN_PROGRESS` in this entry. Operator direction was given directly in this
chat session (2026-08-03), which is the explicit authorization this task
required — `NEW-P3-01`'s eligibility finding from Review 002 (above) is the
gate that made this task nameable at all.

**Scope of this entry is documentation synchronization, not the Agent
Package Contract specification itself.** This entry updates
`shared_context/ROADMAP.md` (new "Developer Platform & Agent Package
Ecosystem — Planned Direction" section), `shared_context/RUN_QUEUE.md`
(Agent Runtime Product Track item 5 marked in progress, follow-on layers
queued), this file, and adds two new canonical files:
`shared_context/PROJECT_HISTORY.md` (chronological milestone ledger) and
`shared_context/TASK_INDEX.md` (task-identifier status index). The full,
independently reviewable Agent Package Contract specification document (in
the section-by-section style of
`docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`) is **not
drafted by this entry** and remains the next step under this same task ID,
subject to its own independent review and gate.

**Architectural direction recorded, all planned, none specified in detail
and none implemented:** Shared Context Expansion, Multi-Agent Workflow,
Commands Layer, Skills Layer, Hooks Layer, Plugin Layer, MCP Layer, the
Developer Platform umbrella (Skill Registry, Hook Registry, Command
Registry, Plugin Registry, MCP Registry, Package Validation, Package
Lifecycle, Package Distribution), and the Package Ecosystem. Nineteen
command names (`/roadmap` existing, eighteen new) are reserved in
documentation only, following the existing `/roadmap` pattern
(`docs/runbooks/MELLYCORE_ROADMAP_COMMAND.md`); none is implemented, and no
CLI, agent, or runtime parses or executes any of them.

**Provider-agnostic by design, not a Claude Code dependency.** The
Developer Platform borrows a shape similar to Claude Code (Skills, Hooks,
Commands, Plugins, MCP Servers) as a familiar reference point, but every
registry it names must remain expressible across the Agent Runtime's full
six-framework compatibility matrix (Claude Code, OpenAI Agents SDK,
LangGraph, CrewAI, AutoGen, custom MellyCore-compatible agents) and must not
assume, wrap, or require any single framework.

**Nothing implemented.** No registry, package validator, CLI command,
plugin loader, MCP client, or Shared Context schema change exists as a
result of this entry. No agent framework is installed, imported, connected,
or executed; no agent has been executed; no model provider, tool, or
credential is connected or configured. No deployment, push, pull request, or
merge occurred; this entry is a local documentation commit only.

**Validation.** Files changed by this entry are exactly the six named
above (four edits, two new files); no source or test file changed.
`pytest`, black, flake8, and mypy were not run and are not claimed passing —
none applies to a documentation-only change with no source or test files
touched.

**Not reopened, not reordered.** The Agent Runtime architecture gate
(Review 002, `PASS_WITH_NON_BLOCKING_FINDINGS`) is not reopened by this
entry. Framework Bridge Contract, Shared Context Bridge, Agent Runtime
Scaffold, first Agent Package, Cross-Agent Smoke, and Integration Review
remain blocked, as does Agent Runtime implementation. The nine Developer
Platform layer specs above remain unauthorized to begin their own
specification work. The pre-existing global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, and independently governed.

**Exact next step under this task ID:** draft the Agent Package Contract
specification document itself, scoped to the Agent Package Contract
concerns Review 002 found eligible (not the full nine-layer Developer
Platform set), then route it through the same independent-review and
remediation cycle used for the Agent Runtime architecture above.

## Agent Package Contract Spec 001 — Specification Drafted, Unverified, Pending Independent Review

The exact next step recorded immediately above is now complete. The
canonical Agent Package Contract specification exists:
`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (29 sections).
Durable report: `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md`.
Complete as one local documentation commit on
`docs/mellycore-agent-package-contract-spec-001`; **not pushed**.

**This specification is unverified.** No independent architecture, security,
or consistency review has run against it, exactly as
`MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001` was unverified before its own
Review 001. It is **not accepted**.

**What the specification defines.** The Agent Package: identity (reusing
`agent_definition_id`, `package_revision_id`, `framework_type`, and all
eighteen Runtime §10.1 fields verbatim), a permitted/prohibited content
boundary, a nine-category asset layout, manifest relationships to a future
Agent Manifest and to Skill/Command/Hook/Plugin/MCP declarations, a
five-state capability separation (declared → runtime-supported →
policy-allowed → operator-approved → active), a twelve-category
permission/approval model (default-deny), a dependency model, a
six-framework compatibility projection that names no framework canonical
owner, boundary definitions for five asset types (Skill, Command, Hook,
Plugin, MCP Declaration), an eight-rule Shared Context interaction boundary,
a nine-stage Runtime interaction contract (discovery through
termination/suspension projection), an eleven-state package lifecycle
(distinct from Runtime's seventeen `run_state` values and Control Plane's
six status dimensions, projecting onto them one-directionally, creating no
seventh dimension), a nine-layer validation model, a seven-category trust
vocabulary (no signing mechanism claimed), eleven observability projections,
a fifteen-class error taxonomy, versioning rules, seven Batch Orchestration
eligibility declarations, twelve security-threat mitigation postures, twelve
non-goals, and twelve named follow-up contracts.

**No concern is duplicated.** MCP Declarations reference Provider Registry
§24 server records; they never register or redefine one. Package capability
declarations are requests only; the Integration Gateway remains sole
resolver and enforcer. Package lifecycle and trust states project onto the
Control Plane's six existing status dimensions one-directionally, exactly as
`run_state` already does, and create no new dimension. Control Plane's
`Skill`/`Tool`/`Agent` entities remain byte-identical downstream projection
targets, not redefined.

**Nothing implemented.** No Agent Package Store, Package Registry, Package
Validator, loader, Skill/Hook/Command/Plugin/MCP registry, or signing
mechanism exists. No package, manifest, or artifact exists anywhere in this
repository. No agent framework is installed, imported, connected, or
executed; no credential is configured; no provider is connected. No
deployment, push, pull request, or merge occurred.

**Validation.** Exactly eight files changed (two new, six edited); no
source or test file changed. The document's own §1.4 metrics table was
recomputed against its cited sections and four counting errors were
corrected before commit. Every cross-reference resolves to an existing
repository file. `pytest`, black, flake8, and mypy were not run and are not
claimed passing — none applies to a documentation-only change touching no
source or test file.

**Not reopened, not reordered.** The Agent Runtime architecture gate
(Review 002, `PASS_WITH_NON_BLOCKING_FINDINGS`) is not reopened. Framework
Bridge Contract, Shared Context Bridge, Agent Runtime Scaffold, first Agent
Package, Cross-Agent Smoke, and Integration Review remain blocked, as does
Agent Runtime implementation. The twelve named follow-up contracts remain
unauthorized to begin their own specification work. The global
higher-priority pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`
remains unchanged, in place, and independently governed.

**Exact next task:** `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` — an
independent, read-only review of this specification. Not started, not
authorized by this entry.
