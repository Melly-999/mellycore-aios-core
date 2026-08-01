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

**Outstanding documentation work** (none started; remaining chain and
reconciliation with existing priority work:
`shared_context/ROADMAP.md`'s "Enterprise Provider Integration — Research
Direction" section and `shared_context/RUN_QUEUE.md`'s "Parallel Decision
Track — Enterprise Provider Integration"):
`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001`.
`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` may only be considered after that
full documentation-review gate passes and requires its own separate
explicit authorization.

Durable task report:
`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001.md`.
