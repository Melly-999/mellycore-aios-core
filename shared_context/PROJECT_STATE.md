# Project State

Project name: MellyCore AIOS

## Canonical Product Identity

MellyCore is a local-first, operator-controlled **AI Operating System**.

Its Command Center presents a cinematic AI Operations Observatory and
visually compelling AI Workspaces, while its runtime, provider, tool,
context, persistence, evidence, governance and safety planes remain
vendor-neutral, explicit, provenance-bearing and fail-closed.

This thesis (locked by `MELLYCORE-ROADMAP-LOCK-001B`) extends — it does not
reject — the accepted AI Operations Observatory / Control Plane identity. The
relationship is:

```
CONTROL PLANE / AI OPERATIONS OBSERVATORY
                ↓
        COMMAND CENTER UX
```

The Observatory continues to make models, agents, runs, context, memory,
recommendations, and approvals visible, inspectable, approval-gated, and
auditable. The Command Center is its product/navigation manifestation, not a
replacement architecture.

The controlled improvement loop is:

`observe → analyze → recommend → approve → implement → validate → record`

Consequential action requires explicit operator approval. The system does not
autonomously change safety rules, merge, deploy, execute recommendations, or
store provider secrets.

## Cinematic AIOS Product Structure — Locked (Product Vision, Not Implementation)

Locked by `MELLYCORE-ROADMAP-LOCK-001B`. The architecture and product inventory
in this section remain the locked **product vision and planned product
structure**. Their static M2 showcase representation does not implement a
workspace backend, connect a provider or runtime, authorize execution, mint a
new canonical data owner, or change an accepted architectural contract.
Existing Agent Runtime, Framework Bridge,
Provider Registry, Integration Gateway, and Shared Context contracts remain
authoritative.

There are exactly **two top-level product layers**
(`TOP_LEVEL_LAYER_COUNT = 2`):

### Layer 1 — Command Center

The Command Center is the product/navigation manifestation of the existing
control, observability, context, routing, and governance systems. Expected
product surfaces include: Overview / Mission Control, Knowledge & Operations
Graph, Context Management, Runtime Constellation, Agents, Runs, Models,
Providers, Model Routing, Tools / MCP, Shared Context, Memory, Artifacts,
Cost / Usage, Observability, Governance / Approvals, and Hardware / Local AI.

These are product/UI surfaces. They project canonical state; they do **not**
become new canonical data owners.

### Layer 2 — AI Workspaces

Exactly **ten canonical AI Workspaces** (`WORKSPACE_COUNT = 10`). Each now has
a truthful static M2 showcase representation in `site/index.html`; the
workspace product surfaces themselves remain **planned**, and none has a
workspace backend, provider/account connection, runtime activation, download,
or execution capability:

1. Deep Research
2. Compare Arena
3. Multi-Agent Crew
4. Email AI
5. Voice
6. Video Intelligence
7. Image Studio
8. Model Downloader
9. Ollama Manager
10. Coding / Runtime Studio

The following are **not** additional workspaces: Obsidian, Knowledge &
Operations Graph, Runtime Constellation, Source Arena, Model Arena, Local AI
Hub, Shared Context, and Mission Control. **Local AI Hub** may exist as a
presentation grouping containing Model Downloader and Ollama Manager; it is
not an eleventh workspace and not a new canonical service.

### Status truth

Workspace and surface status uses existing state semantics; no new universal
status enum is minted. The following distinctions are preserved and must not
be collapsed: visual != implemented; planned != implemented; implemented !=
tested; tested != connected; connected != authorized; supported != connected;
static demo != live telemetry; available != reliable; zero-cost != private.

### Flagship Command Center concepts (projections, not owners)

- **Runtime Constellation** — a flagship visual/product concept projecting the
  agent-runtime ecosystem (possible nodes include Claude Code, OpenAI Agents
  SDK, LangGraph, CrewAI, AutoGen, MellyCore Custom, the Codex ecosystem, and
  local execution). It is **not** a canonical runtime owner: Agent Runtime
  owns run/attempt lifecycle, Framework Bridge owns framework-neutral
  projection, and future Framework Adapters own framework-specific
  implementation. Displayed does not mean installed, supported, connected, or
  running.
- **Knowledge & Operations Graph** — a flagship Command Center surface
  extending the existing Living Context Graph, Shared Context, AI Operations,
  Run Ledger, and provider/tool/artifact projections. It is a **derived
  view** that may combine source knowledge, MellyCore system topology, and
  MellyCore operations topology; projected relationships preserve or
  reference SOURCE, AUTHORITY, PROVENANCE, REVISION, CONFIDENCE, and STATUS.
  It must not become a competing canonical graph truth owner, and the graph
  schema is unchanged by this lock.

### Obsidian — external context source (workspace impact: zero)

Obsidian is locked as a first-class **external context-source direction**,
not an AI Workspace (`OBSIDIAN_WORKSPACE_COUNT_IMPACT = 0`). No new Context
Gateway is introduced. The preferred conceptual boundary is: Obsidian Vault →
Obsidian Context Adapter → Shared Context Bridge / accepted exchange boundary
→ Context Gate → provenance + sensitivity + admission → canonical Shared
Context → Knowledge & Operations Graph / authorized consumers. Future phases:
O1 bounded read-only local Vault integration; O2 optional live plugin bridge;
O3 optional controlled writeback, which must remain
PROPOSE → DIFF → HUMAN APPROVAL → WRITE → VERIFY → AUDIT / EVIDENCE. No
Obsidian implementation exists or is authorized.

### Model economics and routing (direction, not enums)

The product direction supports multiple inference classes: **LOCAL**,
**ZERO-COST REMOTE**, **PAID REMOTE**, and **TRIAL / CREDIT**. No single
universal production enum is minted; canonical ownership remains separated —
Provider Registry (provider/model evidence: identity, credential
requirements, capabilities, availability, health, rate limits, quotas,
provider-side pricing evidence), Model Router (capability-first filtering,
policy precedence, selection, fallback, paid escalation), AI Operations /
Cost Observatory (cost class, estimates, actual cost, source, revision,
freshness), Integration Gateway (credential use, authorization,
provider-bound execution, data-handling controls). The Command Center owns
projection and explanation only.

Invariants: FREE IS NOT A PROVIDER. FREE IS NOT LOCAL. FREE IS NOT PRIVATE.
FREE IS NOT RELIABLE BY DEFINITION. FREE IS NOT NECESSARILY PERMANENT. TRIAL
CREDIT IS NOT PERMANENT FREE ACCESS. Capability compatibility precedes price
preference. Zero-cost-only routing must never silently escalate to paid
inference. Workspace code must not hard-code provider-specific routing.
LOCAL AI is distinct from ZERO-COST REMOTE AI even where monetary cost is
zero.

### Capability View and Hardware Capability Service (research directions)

No new universal canonical Capability Registry is created. The locked
requirement is a **federated, provenance-bearing Capability View** — a
derived view / platform-research direction referencing authoritative
capability owners (Provider Registry, Agent Runtime, Framework Bridge, future
Tool Gateway, Integration Gateway, Agent Package contracts, and a future
Hardware Capability Service). The **Hardware Capability Service** is a future
platform-research direction (hardware snapshots, runtime capabilities, model
requirements, hardware/model fit, estimator adapters, platform constraints,
measured benchmarks, recommendation explanations); it is not implemented, and
MellyCore is not hard-coupled to NVIDIA, Windows, Ollama, or llmfit.

## Durable Implemented State

- Static local homepage and Live Cockpit V2 prototype.
- Local M2 static-showcase implementation/polish chain through
  `b6e10a935f358582a02e5f43e19b0c9ec3f37ab5` (`feat: polish MellyCore
  showcase rhythm`), ready for formal Showcase Acceptance but not yet formally
  accepted. The six-commit linear chain materializes the first viewport,
  technical product proof, instrument language, signature surfaces, the exact
  ten-workspace ecosystem, and global rhythm in `site/`. It is local and
  unpushed in this lineage; it claims no merge, deployment, public release,
  provider connection, workspace backend, or runtime activation.
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

## Agent Package Contract Spec Review 001 — Gate FAILED, Remediation Required

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` is **complete as one
local documentation commit; not pushed.** Independent, read-only
architecture, ownership, and consistency review of
`MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001` commit `708e265`. Durable
evidence:
`docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md`,
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md`.

**Gate decision: `FAIL_REMEDIATION_REQUIRED`. P0 = 0, P1 = 1, P2 = 3, P3 =
3.** Every one of the specification's 24 self-reported metrics independently
recounts correctly — zero discrepancies, unlike the Agent Runtime
architecture's own first review. Twelve of thirteen ownership rows
independently confirm without qualification.

**`P1-01`** — the specification's package-lifecycle (§17) and trust-state
(§19) sections each claim a one-directional projection onto Control Plane's
six canonical status dimensions "exactly as `run_state` already does," but
provide no row-complete mapping table and no Control Plane amendment,
unlike the verified precedent that closed this exact seam for `run_state`.
Four of eleven package lifecycle states (`published`, `installed_reference`,
`deprecated`, `retired`) and five of seven trust-state categories (`local`,
`first_party`, `third_party`, `imported`, `generated`) have no legal target
value in Control Plane §8.1's closed enum sets.

**`P2-01`–`P2-03`** (non-blocking, each independently fail-closed):
Provider Registry §24.2's pattern cited by analogy outside its stated scope
in three locations; the evaluation point for `DEPENDENCY_UNRESOLVED`
ambiguous between this contract's own validation time and the Agent
Runtime's instantiation-eligibility time; reserved-command-collision
detection required by §14/§24 but not enumerated among §18's nine
validation layers.

**`P3-01`–`P3-03`**: a thin compatibility-table row; no dedicated error
class for command-collision rejection; one identity field's absence-
handling stated in prose rather than table form.

**No P0 exists.** No direct credential or provider path, cross-tenant
execution possibility, canonical-context mutation bypass, authorization or
approval bypass, secret exposure, or unsafe consequential retry was found.

**The reviewed specification itself was not edited by this review.**
Nothing implemented, connected, or executed: every one of the twelve
canonical cross-check sources was re-hashed after this task's commit and
confirmed byte-identical to its pre-review baseline.

**Validation.** Exactly eight files changed (two new, six edited); no
source or test file changed. `pytest`, black, flake8, and mypy were not run
and are not claimed passing.

**Not reopened, not reordered.** The Agent Runtime architecture gate
(Review 002, `PASS_WITH_NON_BLOCKING_FINDINGS`) is not reopened. The Agent
Package Contract specification remains **not accepted**. Framework Bridge
Contract, Shared Context Bridge, Agent Runtime Scaffold, first Agent
Package, Cross-Agent Smoke, Integration Review, and all twelve Agent
Package follow-up contracts remain blocked. The global higher-priority
pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains
unchanged, in place, and independently governed.

**Exact next task:** `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001`
— remediate `P1-01` and, in the same pass, `P2-01`–`P2-03` and
`P3-01`–`P3-03`. Not started, not authorized by this entry.

## Agent Package Contract Spec Remediation 001 — All Review 001 Findings Addressed; Unverified Pending Review 002

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001` is **complete as
one local documentation commit; not pushed.** Remediates all seven findings
of Review 001 (`P1-01`; `P2-01`, `P2-02`, `P2-03`; `P3-01`, `P3-02`,
`P3-03`) in the reviewed specification, advancing it to **version 1.1**.
Durable report:
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`.

**`P1-01` resolved by removing the unsupported claim, not by amending
Control Plane.** Package lifecycle state (§17) and Package Trust State
(§19) are now stated explicitly as Agent Package domain concepts — typed
entity data under Control Plane §7.1's general allowance — with **no
projection defined onto any of Control Plane's six closed dimensions**. No
mapping table was invented and no already-existing legal canonical mapping
was found or used; the Control Plane owner contract was **not edited**
(re-verified byte-identical after this commit). Any future projection
remains explicitly deferred to a dedicated mapping contract or a
separately reviewed Control Plane amendment.

**`P2-01`–`P2-03` and `P3-01`–`P3-03` each closed with a targeted,
owner-preserving correction:** the three Provider Registry §24 analogies
were rephrased as explicit non-normative "modeled on" citations; the
`DEPENDENCY_UNRESOLVED` evaluation boundary is now deterministic (dependency
validation, §18.1 layer 4, is the exclusive owner; Runtime's instantiation
eligibility consumes, never re-derives, the determination); a new,
normative §14.1 enumerates all seven required command-namespace-collision
checks and a new `COMMAND_NAMESPACE_COLLISION` error class gives the
rejection a stable identity; the `claude_code` compatibility row and the
`license_metadata` identity field were corrected editorially.

**Nothing implemented.** No Agent Package Store, Package Registry, Package
Validator, loader, command runtime, hook runtime, plugin runtime, MCP
runtime, or batch runtime exists or was implemented by this task. No
Control Plane enum value was invented; no Provider Registry responsibility
was broadened.

**Validation.** Exactly eight files changed (one edited spec, one new task
report, six bounded state-sync edits); no source or test file changed.
Every canonical cross-check source — Agent Runtime, Control Plane, Provider
Registry, Integration Gateway, AI Operations Intelligence, Enterprise
Provider ADR, the seam-decision record, Shared Context contracts, the
Safety Contract, and both Review 001 artifacts — was re-hashed after this
commit and confirmed byte-identical to its pre-remediation baseline.
`pytest`, black, flake8, and mypy were not run and are not claimed passing.

**Gate remains failed; specification remains not accepted.** This task does
**not** claim Review 001's `FAIL_REMEDIATION_REQUIRED` gate has passed —
that gate remains historically recorded as failed until an independent
Review 002 runs and itself passes. No implementation gate has opened; no
downstream Agent Package implementation task is authorized by this entry.
Framework Bridge Contract, Shared Context Bridge, Agent Runtime Scaffold,
first Agent Package, Cross-Agent Smoke, Integration Review, and all twelve
Agent Package follow-up contracts remain blocked. The global
higher-priority pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`
remains unchanged, in place, and independently governed.

**Exact next task at the time of that remediation:**
`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002` — an independent,
read-only re-review of this remediation.

## Agent Package Contract Spec Review 002 — Gate PASS_WITH_NON_BLOCKING_FINDINGS; Specification Accepted As Documentation Only; Nothing Implemented

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002` is **complete as one
local documentation commit; not pushed.** An independent, read-only
re-review of the remediated specification (**version 1.1**, commit
`ad1d1fc`). Durable record:
`docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md`; task
report: `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002.md`.

**Gate decision: `PASS_WITH_NON_BLOCKING_FINDINGS`.** P0 = 0 and P1 = 0.
All seven Review 001 findings are independently `CLOSED`, with the single
P1 closed in full rather than partially. The outcome is not `PASS` solely
because the review introduced seven new non-blocking findings (P2 = 3,
P3 = 4).

**`P1-01` independently verified closed.** Every occurrence of
`lifecycle_status`, `evidence_state`, `approval_state`, and `run_state` in
the specification was audited in context; each is an explicit denial of
projection or a non-collision statement. Zero surviving projection claims,
no Control Plane enum member invented, no package state silently coerced.
Control Plane §7.1's typed-domain-field allowance is quoted **verbatim** and
is correctly scoped — it literally names "trust" among the fields that
remain typed entity data. **Every canonical owner document is byte-identical
to the baseline Review 001 recorded before the remediation ran**, which is
independent blob-ID proof — not a report assertion — that no owner contract
was edited to make this specification pass.

**`P2-01`–`P2-03` and `P3-01`–`P3-03` independently verified closed.** The
Provider Registry audit was extended beyond the three locations Review 001
named to all 17 occurrences: Provider Registry is nowhere presented as
owning package lifecycle, trust state, validation, dependency resolution,
activation, command namespaces, runtime authorization, installation, or
execution. The `DEPENDENCY_UNRESOLVED` evaluation boundary is deterministic
and owned exclusively by §18.1 layer 4. The command-namespace collision
rules of §14.1 are enumerated under §18.1 layer 1 with a dedicated
`COMMAND_NAMESPACE_COLLISION` rejection class, and §14.1 rule 3's target —
`ROADMAP.md`'s "Planned Commands" reservation — was verified to exist.

**Seven new non-blocking findings, none discarded.** P2: `NEW-P2-01` (§16
stage 7 and §17.1 direct implementers to §20 for a package-lifecycle
rendering field that §20.1 does not define); `NEW-P2-02` (§22 rule 2 still
declares the contract version "currently `1.0`" while the document is
version 1.1 and version 1.1 added mandatory rejection rules); `NEW-P2-03`
(§14.1 rule 6 imposes an absolute prohibition over "protected command
classes" that no document enumerates). P3: `NEW-P3-01` (§17.3 rule 1's bare
Provider Registry analogy — assessed independently and found technically
accurate and **not** an ownership overreach, recorded only for inconsistent
formatting relative to its three disclaimed siblings); `NEW-P3-02` (§21
prose says "Fifteen" against 16 table rows); `NEW-P3-03` (five inverted
normative modals in version-1.1-added text); `NEW-P3-04` (the Remediation
001 report's own Provider Registry audit undercounts 17 occurrences as
nine). Each of the three P2 findings must be corrected before the follow-up
contract that depends on its section.

**Specification accepted as a documentation contract only.**
`MELLYCORE_AGENT_PACKAGE_CONTRACT_001` version 1.1 is accepted as the
canonical documentation contract for the Agent Package track, under the
seven recorded non-blocking constraints. Acceptance fixes what a future
Agent Package must satisfy and **establishes no implementation whatsoever**.

**Nothing implemented.** Agent Package Store, Package Registry, Agent
Registry, Package Validator, and package loader remain `NOT_IMPLEMENTED`.
Agent Packages and package installations `NONE_EXIST`. Packages executed:
**zero**. No command, hook, plugin, or MCP execution exists; no batch
execution exists and Batch Orchestration remains unspecified and
unauthorized; no runtime, provider connection, credential, or deployment
exists. Cryptographic package signing remains `NOT_SPECIFIED` and
`NOT_IMPLEMENTED`. Migration triggers #1, #4, #5, #6, and #7 remain
uncrossed.

**Validation.** Exactly eight files changed (two new review artifacts, six
bounded state-sync edits); no source file, test file, configuration file, or
workflow YAML changed; no `.env` file changed and no secret or provider key
was introduced. `git diff --check` exit `0`; `py -3.9
scripts/validate_project_state.py` `PASS`. The reviewed specification was
**not edited** — its blob ID is identical before and after this commit —
and all fifteen immutable evidence and owner files were re-verified
unchanged after the commit. `pytest`, black, flake8, and mypy were not run
and are not claimed passing; a passing scaffold validator is not treated as
evidence of architectural correctness.

**Prior gates preserved.** Review 001 remains historically recorded as
**failed** (`FAIL_REMEDIATION_REQUIRED`); Remediation 001 remains
**complete**; the Agent Runtime architecture's Review 002
(`PASS_WITH_NON_BLOCKING_FINDINGS`) is **not reopened**. The global
higher-priority pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`
remains unchanged, in place, not reordered, and not reinterpreted.

**Exact next task at the time of that review:** the next item then present in
canonical `RUN_QUEUE.md` for this track was the **Framework Bridge Contract**,
followed by Shared Context Bridge, Agent Runtime Scaffold (inert), Scaffold
Review, first Agent Package, Cross-Agent Smoke (inert modes only), Integration
Review, and then the twelve follow-up contracts of specification §26.

## Framework Bridge Contract Spec 001 — Specified, Documentation Only, Unverified

`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001` is **complete as one local
documentation commit; not pushed.** Specification:
`docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md` (version 1.0,
39 sections). Durable report:
`docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md`.

**Task identity minted by explicit Operator authorization.** The queue
previously carried only the plain English name "Framework Bridge Contract",
with **no task identifier anywhere in the repository**; an exhaustive search
for any `…FRAMEWORK-BRIDGE…` identifier returned zero matches. The run that
discovered this **stopped before mutation** rather than invent an identifier,
and the Operator then authorized
`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001`. This matches the established
convention — evidenced by Agent Runtime §40 and Agent Package Contract §26 —
that a task identifier is minted at the moment of Operator authorization, not
in advance.

**What the contract fixes.** The one-directional projection chain — MellyCore
canonical contract → framework-neutral bridge semantics → framework-specific
adapter projection — with the inverse explicitly prohibited. No framework may
redefine agent identity, package identity, capability states, permissions,
approvals, trust, provenance, lifecycle, run state, Shared Context ownership,
observability ownership, error taxonomy, or Operator authority, and **no
projected form is ever authoritative**. It defines the adapter declared
boundary (twelve fields, no code); identity, manifest, capability, permission,
prompt, tool, skill, command, hook, plugin, MCP, Shared Context, and memory
projections; a sixth **framework-supported** capability state that never
implies MellyCore authorization; thirteen deny-by-default permission categories
that framework defaults MUST NOT override, with permission flattening
prohibited; eleven distinct runtime-interaction stages in which adapter
selection confers nothing; the Model Router boundary that framework
configuration MUST NOT bypass; error translation consuming twelve existing
Agent Runtime classes and adding nine genuinely absent bridge classes; a
four-tier projection-loss taxonomy failing closed on safety-relevant loss; ten
Bridge Validation layers that explicitly do **not** authorize execution;
sixteen observability projections; six bounded per-framework profiles; and
fifteen security threats.

**Ownership preserved; no owner document edited.** The contract owns only
projection semantics, the adapter boundary, the projection-loss taxonomy, the
validation layers, and the per-framework profiles. It consumes unchanged Agent
Runtime §16's nine bridge operations, §11.2's six normative bridge rules,
§11.1's closed six-member framework set, and §33's error taxonomy; all Agent
Package concepts; Model Router decisions; Provider Registry facts; Gateway
capability, policy, and approval decisions; Shared Context canonical truth; and
Control Plane's six status dimensions. Only the canonical framework identifiers
appear — `claude_code`, `openai_agents_sdk`, `langgraph`, `crewai`, `autogen`,
`mellycore_custom` — with **no seventh identifier introduced**.

**All three open Agent Package P2 findings contained, not resolved.**
`NEW-P2-01`: no package-lifecycle rendering field is defined and no rule
depends on one. `NEW-P2-02`: **neither** package contract version 1.0 nor 1.1
is declared canonically current; adapters express compatibility as ranges.
`NEW-P2-03`: **no** protected command classes are defined or enumerated, and
the bridge never activates, owns, or resolves a command namespace. All three
remain open, are recorded as deferred dependencies owned by the Agent Package
Contract and the future Command Registry, and **the Agent Package Contract was
not edited by this task**.

**Honest limitation recorded.** Agent Runtime §11.3 and §35 require every
per-framework cell to be independently validated by this task, but empirical
validation requires installing and executing each framework, which this
authorization forbids. Those cells therefore remain **unvalidated planning
positions**; the contract defines the validation obligation and assigns it,
with recorded evidence, to each future per-framework adapter specification.

**Nothing implemented, integrated, installed, or connected.** Framework Bridge
`NOT_IMPLEMENTED`; Framework Adapters (all six) `NONE_EXIST`; SDKs and
frameworks `NOT_INSTALLED`, `NOT_IMPORTED`, `NOT_EXECUTED`; framework sessions
created **zero**; runtime handles issued **zero**. No Agent Runtime, package
loading, package execution, command, hook, plugin, MCP, or batch capability
exists; no provider connection, credential, model call, network operation, or
deployment. Migration triggers #1, #4, #5, #6, and #7 remain uncrossed.

**Validation.** Exactly eight files changed (two new documentation artifacts,
six bounded state-sync edits); no source, test, configuration, or workflow file
changed; no `.env`, secret, or provider key. `git diff --check` exit `0`;
`py -3.9 scripts/validate_project_state.py` `PASS`. All seventeen immutable
owner and prior-evidence files were re-verified byte-identical after the
commit. `pytest`, black, flake8, and mypy were not run and are not claimed
passing.

**That specification was unverified at the time of that entry.**

**Exact next task at the time of that specification:**
`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001`.

## Framework Bridge Contract Spec Review 001 — Gate PASS_WITH_NON_BLOCKING_FINDINGS; Accepted As Documentation Only; No Adapter Or Framework Integration

`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001` is **complete as one
local documentation commit; not pushed.** An independent, read-only
architecture, ownership, interoperability, and safety review of the Framework
Bridge Contract (**version 1.0**, commit `278eae0`). Durable record:
`docs/research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`; task
report: `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001.md`.

**Gate decision: `PASS_WITH_NON_BLOCKING_FINDINGS`.** P0 = 0 and P1 = 0. Eight
new non-blocking findings recorded (P2 = 4, P3 = 4). The outcome is not `PASS`
solely because the review introduced new findings.

**Method.** Owner lists were reconstructed mechanically from the owner
documents — Agent Runtime §11.1's closed framework set, §11.2's six bridge
rules, §16's nine bridge operations, §33's 55 error classes, and Agent Package
§10.1's five capability states — and then tested against the reviewed text,
rather than accepted from the specification's own claims. Every self-reported
metric was recounted directly. **Every canonical owner document is
byte-identical before and after this review.**

**Verified correct.** The closed six-member framework set is exact, with
`custom` **not** accepted as an alias for `mellycore_custom` and
`other`/`generic`/`auto` appearing only inside the prohibition sentence. All
six Runtime §11.2 rules are cited by number and none is weakened. The
canonical-versus-projected direction holds, with every projected form
non-authoritative and a framework SDK's schema requirement explicitly not a
canonical justification. Thirteen permission categories default deny, framework
defaults cannot override them, and permission flattening into a coarse
framework switch is prohibited. Shared Context writes are proposal-only with
mandatory return-path re-validation; five memory scopes stay separated and any
framework persistence feature is forced into bridge-local scope. Routing cannot
be bypassed by framework configuration. Safety-relevant projection loss fails
closed and ambiguity resolves to loss. Validation does not authorize execution.
No new Control Plane status dimension is created. All six framework profiles
are conceptual with **zero** overclaim, and `mellycore_custom` is explicitly no
bypass.

**Framework-validation obligation — assessed on its merits, not excused.**
Agent Runtime §11.3 and §35 scope the obligation to "before any bridge is
implemented". The contract states plainly that this task could not discharge
it, records the per-framework cells as **unvalidated planning positions**, and
assigns the obligation to each future per-framework adapter specification.
Verdict: **honest, owner-correct, and a permitted documentation-only
deferral** — not a P1 ownership failure and not a false validation claim.
**Empirical framework validation remains `NOT_PERFORMED`**; the Runtime
§11.3/§35 cells are unvalidated after this review exactly as before it.

**New P2 findings.** `NEW-P2-01` — four of Runtime §16's nine bridge operations
are never named, and `normalize_result` ("Contract unmet → `failed`, never a
coerced success") has **no counterpart rule anywhere**, leaving run-output
normalization unspecified. `NEW-P2-02` — `PROJECTION_UNSUPPORTED` overlaps the
Runtime-owned `BRIDGE_UNSUPPORTED_BEHAVIOR` with no stated discriminator.
`NEW-P2-03` — the contract silently renumbers the Agent Package Contract's
capability states, shifting owner rows 2–5 each by one, so "capability state 2"
resolves to different concepts in two live contracts. `NEW-P2-04` — the
framework-validation obligation is not wired into the ten Bridge Validation
layers or into Bridge Eligibility.

**New P3 findings.** `NEW-P3-01` — no document-metrics table, breaking the
convention both prior specifications follow and removing the count-drift safety
net that caught a defect in the Agent Package chain. `NEW-P3-02` — §37
criterion 1 says "All 37 sections" against a 39-section document. `NEW-P3-03` —
`LIFECYCLE_MISMATCH`'s coexistence with Runtime's mandatory `unmapped` event is
unstated. `NEW-P3-04` — the specification run's outcome code is recorded in no
tracked file.

**No duplicated Runtime error ownership.** Zero exact name collisions across 55
Runtime and 16 Agent Package classes; the contract correctly attributes all
twelve consumed classes to the Agent Runtime and claims none of them.

**Agent Package P2 containment confirmed.** All three findings remain
**contained and open**: the contract defines no package-lifecycle rendering
field, declares neither package contract version 1.0 nor 1.1 as canonically
current, and enumerates no protected command classes. **The Agent Package
Contract was not edited.**

**Specification accepted as a documentation contract only.**
`MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_001` version 1.0 is accepted under the
eight recorded non-blocking constraints. Acceptance fixes what a future
Framework Adapter must satisfy and **establishes no implementation of any
kind**.

**Nothing implemented.** Framework Bridge `NOT_IMPLEMENTED`; Framework Adapters
(all six) `NONE_EXIST`; SDKs and frameworks `NOT_INSTALLED`, `NOT_IMPORTED`,
`NOT_EXECUTED`; framework sessions created and runtime handles issued
**zero**. No Agent Runtime, package loading, package execution, command, hook,
plugin, MCP, or batch capability exists; no provider connection, credential,
model call, network operation, or deployment. Migration triggers #1, #4, #5,
#6, and #7 remain uncrossed.

**Validation.** Exactly eight files changed (two new review artifacts, six
bounded state-sync edits); no source, test, configuration, or workflow file
changed; no `.env`, secret, or provider key. `git diff --check` exit `0`;
`py -3.9 scripts/validate_project_state.py` `PASS`. The reviewed specification
was **not edited** — blob identical before and after — and all fourteen
immutable subject and owner files were re-verified unchanged after the commit.
The normative-modal scan found **zero** inverted constructions. `pytest`,
black, flake8, and mypy were not run and are not claimed passing; a passing
scaffold validator is not treated as evidence of architectural correctness.

**Exact next item:** the next entry already present in canonical
`RUN_QUEUE.md` for this track is the **Shared Context Bridge**, recorded there
as a **plain name with no task identifier**, followed by Agent Runtime Scaffold
(inert), Scaffold Review, first Agent Package, Cross-Agent Smoke, Integration
Review, the six per-framework adapter specifications, and the twelve Agent
Package follow-up contracts. Each remains **blocked**, requiring its own
specification, independent review, and separate explicit Operator
authorization. Consistent with the repository convention that a task identifier
is minted at the moment of Operator authorization, **no identifier was minted,
started, or authorized by that entry.** The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Shared Context Bridge Contract Spec 001 — Specified, Documentation Only, Unverified

`MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001` is **complete as one local
documentation commit; not pushed.** Specification:
`docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md` (version
1.0, 50 sections). Durable report:
`docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001.md`.

**Task identity minted by explicit Operator authorization** for the queued
plain-name item "Shared Context Bridge", after a repository-wide search
confirmed no conflicting identifier existed — matching the established
convention that an identifier is created at the moment of authorization.

**What the contract fixes.** The one-directional exchange chain — canonical
Shared Context → bounded selection → validated projection → execution-local or
framework-local context → returned proposal → validation, provenance, policy
and approval gates → optional canonical mutation **by the canonical owner
alone** — with the inverse direction prohibited outright. **No framework,
agent, package, provider, tool, plugin, hook, command, MCP server, adapter, or
batch worker may independently mutate canonical Shared Context.** It defines
the logical context envelope; purpose- and consumer-bounded selection; nine
projection prohibitions and twelve eligibility preconditions; ten per-consumer
read boundaries; five separated write/mutation concepts; a ten-phase proposal
lifecycle carrying **no** projection onto any Control Plane dimension;
thirteen mandatory return-path checks treating **all** returned context as
untrusted regardless of byte-identity; provenance preservation that never
collapses to the latest producer; ten namespace categories that are never
flattened; a secret boundary distinguishing reference from value; a
seven-prohibition compression envelope; eight transformation classes; six
context-loss classes of which four fail closed; nine quarantine conditions;
thirteen validation layers that authorize nothing; eleven mutation-eligibility
conditions distinct from mutation itself; nineteen observability projections;
nine audit-evidence questions; and twenty-one security threats.

**Ownership preserved; no owner document edited.** The contract owns only the
exchange boundary. It consumes unchanged Agent Runtime §17.1's seven context
operations **by name**, §17.2's ten record fields, §17.4's snapshot staleness
policy, §18's **six** memory categories, and §19's seventeen-field trace
record; `CONTEXT_GRAPH_SCHEMA.md`'s entities and nine relation types; the
Context Provenance and Sensitivity spec's provenance labels and
`sensitivity_level`; and the Context Gate and Ingestion Gate admission
workflow. **Memory scopes are mapped by semantic name, not renumbered** — the
eight bridge scopes map onto the six owner categories by name, creating no
seventh category, deliberately avoiding the defect recorded as Framework
Bridge `NEW-P2-03`.

**All seven upstream P2 findings contained, not resolved, and still open.**
Framework Bridge `NEW-P2-01`–`NEW-P2-04` and Agent Package
`NEW-P2-01`–`NEW-P2-03`: the contract owns no result normalization, resolves
no Framework Bridge error overlap, uses **no cross-document capability
ordinals**, treats no unvalidated framework profile as context-projection
eligible, defines no package lifecycle rendering field, declares no Agent
Package version canonically current, and enumerates no protected command
classes. **Neither upstream contract was edited.**

**A document-metrics table was included deliberately** (§48), addressing
Framework Bridge Review 001's finding `NEW-P3-01` that recorded its omission as
removing the repository's count-drift safety net. It caught two drafting drifts
corrected before commit — terminology 30→**31**, ownership rows 22→**20** — and
all 34 metric rows now reproduce independently.

**Nothing implemented.** Shared Context Bridge, canonical mutation engine,
context storage, database, vector store, memory service, compression,
validation, and proposal lifecycle are all `NOT_IMPLEMENTED`. Context envelopes
created, proposals submitted, and canonical mutations performed via this
bridge: **zero**. **Empirical framework validation remains `NOT_PERFORMED`.**
No Agent Runtime, Framework Adapter, package loading, provider connection,
credential, model call, network operation, or deployment exists. Migration
triggers #1, #4, #5, #6, and #7 remain uncrossed.

**Validation.** Exactly eight files changed (two new documentation artifacts,
six bounded state-sync edits); no source, test, configuration, workflow, or
storage-configuration file changed; no `.env`, secret, or provider key.
`git diff --check` exit `0`; `py -3.9 scripts/validate_project_state.py`
`PASS`. All nineteen immutable owner and upstream files were re-verified
byte-identical after the commit. `pytest`, black, flake8, and mypy were not run
and are not claimed passing.

**At the time of that specification task the contract was unverified and not
accepted, and no review had run.** That state is superseded by the review
recorded in the next section; this paragraph is retained as a historical record
of the specification task, not as a current-state claim.

**Exact next task at that point:**
`MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001` — since completed; see
below. Agent Runtime Scaffold (inert), Scaffold Review, first Agent Package,
Cross-Agent Smoke, Integration Review, the six per-framework adapter
specifications, the Context Compression and durable-memory contracts, and the
twelve Agent Package follow-up contracts each remain **blocked**, requiring their
own specification, independent review, and separate explicit Operator
authorization. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Shared Context Bridge Contract Review 001 — Gate PASS_WITH_NON_BLOCKING_FINDINGS, Documentation Only

`MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001` is **complete as one
local documentation commit on
`docs/mellycore-shared-context-bridge-contract-spec-review-001`; not pushed.**
Independent, read-only architecture, ownership, memory, security, and consistency
review of the Shared Context Bridge Contract (version 1.0, commit `d3f8b73`).
Durable record:
`docs/research/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`; task
report:
`docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001.md`.

**Gate decision: `PASS_WITH_NON_BLOCKING_FINDINGS`. P0 = 0, P1 = 0, P2 = 8,
P3 = 2.** `MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_001` version 1.0 is
**accepted as a documentation contract only**, under the ten constraints recorded
in the review record §12.

**Owner lists were reconstructed mechanically, not accepted from the
specification's claims.** Agent Runtime §17.1's seven operations, §17.2's ten
record fields, §17.4's six staleness conditions, §18's six memory categories,
§19's seventeen trace fields, and §33's 49 error classes;
`CONTEXT_GRAPH_SCHEMA.md` §5's nine relation types; Control Plane §7.1, §7.2,
§8.1, and §9.3; Integration Gateway §25.2; Agent Package §21; Framework Bridge
§23; and the Context Ingestion Gate's five validation outcomes and nine refusal
codes were each extracted from the owner document and tested against the reviewed
text. **All twenty-five immutable review subjects — the reviewed specification,
its task report, and every owner and prior-review artifact — are byte-identical
before and after this review.**

**All 34 document-metric rows reproduce independently, with zero discrepancies**,
and the 50-section structure recounts exactly (numbered 1–50, no gap or
duplicate). The §48 metrics table, added in response to Framework Bridge Review
001's `NEW-P3-01`, survives independent recount intact.

**Verified `PASS` on the load-bearing safety properties.** A full-document search
found **no direct or ambiguous canonical-write path**: no framework, agent,
package, provider, tool, plugin, hook, command, MCP server, adapter, or batch
worker may mutate canonical Shared Context, and only the canonical owner may,
after the eleven-condition mutation-eligibility intersection and explicit Operator
approval. Returned context stays untrusted against all five bypass temptations
including byte-identity; exactly three identities are minted and eleven
referenced; unrestricted project-context requests fail closed; provenance is
preserved across nine stages and never collapses to the latest producer; lineage
uses six of the Context Graph Schema's nine relations and invents none; ten
namespaces are never flattened; sensitivity does not decay and only a recorded
redaction may lower it; the secret boundary distinguishes reference from value
throughout; safety- and authority-relevant loss fails closed with **ambiguity
resolving to loss**; conflicts are surfaced and never adjudicated; leases do not
overreach into storage or concurrency control; external-deletion limits are
represented honestly as `unknown` rather than overclaimed; thirteen validation
layers authorize nothing; and **no new Control Plane status dimension is
created**. The overclaim scan is clean — every occurrence of "implement" is a
scope exclusion, prohibition, or `NOT_IMPLEMENTED` row, and every occurrence of
"trust" is a denial.

**Eight new P2 findings, all non-blocking and all fail-closed.** `NEW-P2-01`:
four owner-defined semantic neighbours — Gateway `CONTENT_QUARANTINED`, Runtime
`PROVENANCE_VERIFICATION_FAILED` and `ENVELOPE_INTEGRITY_FAILED`, and Framework
Bridge `PROJECTION_LOSS_UNACCEPTABLE` — are never audited or discriminated, each
appearing zero times, falsifying §29 rule 1's claim of a deterministic
discriminator per class. `NEW-P2-02`: `INJECTION_SUSPECTED` is attributed to
Agent Runtime §33, which explicitly states it is not restated there and remains
owned by Integration Gateway §25.2. `NEW-P2-03`: the ten proposal phases and
eleven rejection classes overlap the Context Ingestion Gate's five validation
outcomes and nine R1–R9 refusal codes, and §12's non-collision claim omits the
one owner that actually owns proposal admission. `NEW-P2-04`: seven of nine
quarantine conditions have a §13 check whose disposition is "Reject" with no
precedence rule, and §13 check 6 is explicitly "Reject or quarantine".
`NEW-P2-05`: two of eight memory scopes map to no Agent Runtime §18 category and
one collapses categories 5 and 6 without a discriminator, with Control Plane
§9.3's five memory layers unreconciled. `NEW-P2-06`: the fourteen-field context
envelope overlaps Control Plane §7.2/§9.3's `ContextPacket`, never cited or
distinguished. `NEW-P2-07`: the proposal-replay mitigation cites a lease
mechanism that governs projections only. `NEW-P2-08`: "subtractive or equal" is
normative and the sole cited mitigation for permission amplification, yet no
validation layer or eligibility precondition evaluates it. **Two P3 findings**:
a `30.14` sub-heading over absent subsections, and an undefined
`context_bridge_contract_version`.

**Zero exact error-class name collisions** were found across a mechanical union
index built from eight owner documents; the defect is semantic, not nominal, and
name-uniqueness was independently confirmed.

**All seven upstream P2 findings remain open and contained**, none silently
resolved, and no normative rule depends on any of them: the contract owns no
result normalization, emits neither overlapping class, uses no cross-document
capability ordinal, treats no unvalidated framework profile as
context-projection eligible, defines no package lifecycle rendering field,
declares no Agent Package version canonically current, and enumerates no
protected command class. **Neither the Agent Package Contract nor the Framework
Bridge Contract was edited.**

**Nothing implemented.** Shared Context Bridge, canonical mutation engine,
context storage, database, vector store, index, memory service, compression,
validation, and proposal lifecycle are all `NOT_IMPLEMENTED`. Context envelopes
created, proposals submitted, and canonical mutations performed via this bridge:
**zero**. **Empirical framework validation remains `NOT_PERFORMED`.** No Agent
Runtime, Framework Adapter, package loading, provider connection, credential,
model call, MCP connection, network operation, or deployment exists. Migration
triggers #1, #4, #5, #6, and #7 remain uncrossed.

**Validation.** Exactly eight files changed (two new documentation artifacts, six
bounded state-sync edits); no source, test, configuration, workflow, storage,
database, vector-store, or memory-configuration file changed; no `.env`, secret,
token, credential, or provider key. `git diff --check` exit `0`;
`py -3.9 scripts/validate_project_state.py` `PASS`, exit `0` — both at baseline
and post-commit. `pytest`, black, flake8, and mypy were not run and are not
claimed passing. The reviewed specification was **not edited** and this review
repaired nothing.

**Acceptance is of documentation only and authorizes no downstream task.** Per
canonical `RUN_QUEUE.md`, the next item in this track is recorded as the plain
name **"Agent Runtime Scaffold" (inert)** — no framework process, no provider
call, no credential, no model call, no tool execution, no deployment. It remains
**blocked** and requires its own specification, independent review, and separate
explicit Operator authorization; **no identifier was minted, started, or
authorized by this review.** Scaffold Review, first Agent Package, Cross-Agent
Smoke, Integration Review, the six per-framework adapter specifications, the
Context Compression and durable-memory contracts, and the twelve follow-up
contracts of the reviewed spec's §46 each remain blocked behind their own gate.
The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Agent Runtime Scaffold Spec 001 — Specified, Documentation Only, Unverified

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-001` is **complete as one local
documentation commit on `docs/mellycore-agent-runtime-scaffold-spec-001`; not
pushed.** Specification:
`docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` (version 1.0,
**44 sections**). Durable report:
`docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-001.md`.

**Task identity minted by explicit Operator authorization** for the queued
plain-name item "Agent Runtime Scaffold (inert)", after a repository-wide search
for `MELLYCORE-AGENT-RUNTIME-SCAFFOLD` returned **zero matches**. The four
pre-existing `*SCAFFOLD*` identifiers — frontend, knowledge-graph static UI,
Obsidian 3D, and provider adapter — each own an unrelated concern, so **no
conflicting canonical identity exists.**

**The specification consumes Agent Runtime §37's "Inert v1 boundary"
unchanged.** §37 already owns what a first Agent Runtime Scaffold may implement
(data models, closed vocabularies, validators, the §12 lifecycle state machine,
a **disabled** bridge whose only outcome is `EXECUTION_BLOCKED`, a fixture
bridge under `fixture_only`, event types, Run Ledger interfaces, §8.3
serialization utilities, and tests), what it must not implement, and the rule
that **no execution-success outcome may be representable**. This specification
adds only the structural detail §37 leaves open, and its own §44 rule 6 states
that a change to §37 is **not** an amendment to this document.

**What the specification fixes.** The intended future repository boundary,
derived from inspected convention and labeled
`NON-NORMATIVE FUTURE LAYOUT — NOT IMPLEMENTED`; ten module responsibilities;
one explicit composition root that import never invokes; twelve import-safety
prohibitions and eight construction-safety rules; eight configuration
prohibitions admitting no secret, credential, auto-connect, or auto-execute
value; explicit dependency injection in which **no external dependency is
resolvable through hidden global state**; **fourteen typed runtime ports**,
where a declared port implies no implementation; six distinct dispositions —
no-op, unavailable, unsupported, denied, unimplemented, invalid configuration —
in which **a no-op never stands in for an operation whose absence matters**;
scaffold dispositions for **all sixteen** owner-defined operations (Agent
Runtime §17.1's seven context operations and §16's nine bridge operations),
**none of which performs an external side effect**; a fail-closed execution
boundary; twenty prohibited side-effect categories; ten ordered validation
layers that authorize nothing; twelve inert observability fields; library-safe
logging; a machine-testable inert-mode invariant; seventeen future testing
obligations; seven static validation techniques; and twenty security threats.

**Ownership preserved; no owner document edited.** Package, Framework Bridge,
Shared Context Bridge, Model Router, Provider Registry, Integration Gateway,
Control Plane, Tool Gateway, Run Ledger, cost, Git, and Batch boundaries each
keep their canonical owner. The scaffold **defines no error class of its own**,
consuming owner-defined classes instead — so no name or semantic collision is
possible. It emits neither `PROJECTION_UNSUPPORTED` nor
`BRIDGE_UNSUPPORTED_BEHAVIOR`, owns no part of `normalize_result`, uses **no
cross-document capability ordinal**, treats no framework profile as
runtime-eligible, invents no `run_state` value, creates no Control Plane status
dimension, and declares no Batch compatibility at all.

**Every execution request fails closed** with the owner-defined
`EXECUTION_BLOCKED`, and the refusal holds **across all combinations of the
eleven authorization facts, including the all-eleven-satisfied case**, per Agent
Runtime §37.

**All fifteen upstream P2 findings contained, not resolved, and still open.**
Three Agent Package, four Framework Bridge, and eight Shared Context Bridge
findings were each reconstructed by reading the canonical review records
directly and independently confirmed isolable; the specification depends
normatively on none of them and is recorded against each in its §40 deferred
dependencies. **No upstream contract or review artifact was edited.**

**A document-metrics table was included deliberately** (§42). It caught one
drafting drift corrected before commit — architectural ownership rows
25→**26** — and all 27 rows now reproduce independently.

**Nothing implemented.** No scaffold code, module, Python package, source file,
test, fixture, dependency, or configuration exists. No Agent Runtime, framework
adapter, package loader, policy engine, provider integration, or model routing
implementation exists. Agents executed, model calls, tool executions, provider
requests, and context mutations remain **zero**. Framework SDKs remain
`NOT_INSTALLED` / `NOT_IMPORTED` / `NOT_EXECUTED`. **Empirical framework
validation remains `NOT_PERFORMED`.** Migration triggers #1, #4, #5, #6, and #7
remain uncrossed.

**Validation.** Exactly eight files changed (two new documentation artifacts,
six bounded state-sync edits); **no source, test, Python package, dependency,
configuration, workflow, or runtime file changed**; no `.env`, secret, or
provider key. `git diff --check` exit `0`;
`py -3.9 scripts/validate_project_state.py` `PASS`, exit `0` — both at baseline
and post-commit. All thirty-one immutable owner, review, and convention files
were re-verified byte-identical after the commit. `pytest`, black, flake8, and
mypy were not run and are not claimed passing.

**This specification is unverified and not accepted.** No review has run.

**Exact next task:** `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001` — an
independent, read-only review of this specification. Not started, not authorized
by this entry. The **Agent Runtime Scaffold implementation** (inert code) is
**blocked**: it requires that review to pass **and** separate explicit Operator
authorization, and would receive its own file allowlist. Scaffold Implementation
Review, first Agent Package, Cross-Agent Smoke, Integration Review, the six
per-framework adapter specifications, and every deferred contract of the
specification's §40 each remain blocked behind their own gate. The global
higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Product Track — Units 1-9 and Governance Tail Integrated Locally (Not Pushed)

`MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001`,
state semantics remediated by
`MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-001`.

**Verified Governance-Tail integration checkpoint —
`16da3ec2df9b52b203bb16468f90258f2d7f540c`.** Verified against Git objects:
**44 commits** from canonical baseline
`947f33d27d5546775186e96bdc61e30db78c0b3d`, **0 merge commits**, every commit
single-parent. That is the 42-commit nine-unit Product Track plus the two
reviewed Governance Tail commits, reached **entirely by fast-forward** across
eleven advancements with **zero commits authored** by any integration task.

This is an **immutable property of that commit**, not a claim about where
`integration/mellycore-product-track-001` currently points. **When live tip
identity matters, resolve it from Git:**
`git rev-parse integration/mellycore-product-track-001`.

**Distinct states, not to be collapsed:**

| Concept | Value |
| --- | --- |
| Canonical baseline (remote `clean-origin/main`) | `947f33d27d5546775186e96bdc61e30db78c0b3d` |
| Verified Governance-Tail integration checkpoint | `16da3ec2df9b52b203bb16468f90258f2d7f540c` — 44 cumulative commits, 0 merges |
| Reconciliation candidate — 1st documentation-only descendant | `493dc86ba1f56d854876e7d2a741253d52283bef` |
| Remediation-001 — 2nd documentation-only descendant | `ea0d20ee7533b99360c76d1c5cee609dd2ce2aa1` |
| Remediation-002 — 3rd documentation-only descendant, independently reviewed | `6ccbbed5280997bc9e1141015eb9559551976529` — 47 cumulative commits, 0 merges |
| Remediation-003 — subsequent documentation-only descendant | *not self-declared; exact SHA and graph shape resolved from Git by the next independent review* |
| Live integration branch tip | *resolve from Git* |

Every cumulative count in that table is an **immutable property of the named
commit**: "N cumulative commits from baseline to `X`" remains true no matter what
is committed after `X`. None of those counts is a claim about where any branch
currently points, and none is a prediction of a final integrated total.

**At the time this section was last written**,
`integration/mellycore-product-track-001` pointed at the verified checkpoint and
no reconciliation-lineage descendant had been integrated — each sat on its own
separate local branch.

**Remote canonical `main` is separately gated.** `clean-origin/main` was
`947f33d27d5546775186e96bdc61e30db78c0b3d` at authoring time; it advances only
under a separately authorized publication sequence. No push, pull request,
remote mutation, or deployment has been performed by any task in this lineage.
This state is **local**.

**Mechanically verified reviewed lineage shape.** The lineage `16da3ec2…` →
`493dc86…` → `ea0d20ee…` → `6ccbbed…` was verified from Git objects by
`MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-REVIEW-002`:
**3 documentation/governance descendants after the checkpoint, 47 cumulative
commits from baseline, 0 merge commits.** That is a fact about the commit
`6ccbbed…` — not a forecast, and not a statement that any branch points there.

**Effect of a future authorized integration — total deliberately not predicted
here.** Remediation-003 adds a further descendant to this lineage, so any fixed
final total written into this document would be falsified by the very act of
writing it. The integrating task must therefore resolve the exact target SHA,
descendant count, cumulative count, and merge count **from Git at authorization
time**:

```
git rev-list --count        947f33d27d5546775186e96bdc61e30db78c0b3d..<target>
git rev-list --merges --count 947f33d27d5546775186e96bdc61e30db78c0b3d..<target>
git rev-list --count        16da3ec2df9b52b203bb16468f90258f2d7f540c..<target>
```

Integration remains ff-only, bounded, and separately authorized. No integration
is authorized by this record.

| Checkpoint | SHA | Cumulative commits |
| --- | --- | ---: |
| Canonical baseline | `947f33d27d5546775186e96bdc61e30db78c0b3d` | 0 |
| Unit 1 — Enterprise Provider Documentation Foundation | `b32c81fa96b9f3f7542a93101b73a4fe038b033f` | 15 |
| Unit 2 — Provider Adapter Scaffold | `5c9616350536e614096b24a5559aa86ed59ab40f` | 17 |
| Unit 3 — Cloudflare API Shield Read-Only Adapter | `95a31316b0c4871343637a6b414f4aaa79dee76d` | 21 |
| Unit 4 — Agent Runtime Architecture | `bb2e216a9c3510a4dd6f37ab18eb62f8df1c374b` | 25 |
| Unit 5 — Agent Package Contract | `7fa3d8ad2d319312cc7785c4b4ef9f89a5a04776` | 30 |
| Unit 6 — Framework Bridge | `b26b330ccee7d9efba304ee66e6c3ccc4e1ae5e1` | 32 |
| Unit 7 — Shared Context Bridge | `3019a2303d794d89288edcf2f2ea201fef357f09` | 34 |
| Unit 8 — Runtime Scaffold Specification | `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5` | 40 |
| Unit 9 — Cross-Agent Context Pack | `a0b70ae6c45c640ede4889abeb1f169e5b5a6381` | 42 |
| Governance Tail (plan) | `14eb6c90ff3ffa7125b3f7b3ef077b17ce93d0c6` | 43 |
| Governance Tail (remediation) — **integration checkpoint** | `16da3ec2df9b52b203bb16468f90258f2d7f540c` | 44 |

The Governance Tail is **not Unit 10**. It does not change any Unit 1-9
boundary, SHA, count, or fast-forward proof, and the Product Track inventory
remains exactly 42 commits across nine logical units.

**`REVIEW_PINNED_GOVERNANCE_TAIL_SHA` =
`16da3ec2df9b52b203bb16468f90258f2d7f540c`**, published durably in
`docs/research/MELLYCORE_PRODUCT_TRACK_INTEGRATION_PLAN_REMEDIATION_REVIEW_001.md`
(imported here byte-for-byte, blob `3676e4155df8e11bce7eb7a5266f0480431a383e`,
from record commit `fefe65a38c8855271a1dab6dcb8c7178f3fb55b9`). That record
commit is **not** an ancestor of the integration branch and was never
cherry-picked or merged.

**Validation reproduced at the integrated tree:** `git diff --check` clean;
`py -3.9 -B scripts/validate_project_state.py` → `PASS`;
`py -3.9 -B -m unittest discover -s tests -p 'test*.py'` → **696 tests, OK**.
`black`, `flake8`, `mypy`, and `ruff` are **not installed** and were reported
`NOT RUN / UNAVAILABLE`, never as passing.

**Implementation state is unchanged by integration.** Integration moved
documentation into a branch; it implemented nothing. `NEW-P2-01` remains
amendment-affecting, `NEW-P2-02` remains **implementation-blocking**, and
implementation readiness remains `NOT_READY_IMPLEMENTATION_AFFECTING_FINDINGS`.
No scaffold code, Runtime, framework adapter, package loader, frontend, provider
connection, credential, or deployment exists or is authorized.

**`MELLYCORE-ROADMAP-LOCK-001` remains BLOCKED.** Integration Plan §13
conditions 1-10 are satisfied; condition 11 — a separate explicit Operator
authorization — is not.

**Open findings carried forward:** `GT-P3-02`, `CI-P3-01`, `CI-P3-02`,
`U9-P3-01`, and the two record-content P3 notes. Closed: `GT-P2-01` (durable pin
record), `GT-P2-02` and `GT-P3-01` (this reconciliation).

## Agent Runtime Scaffold Review 003 — Documentation Gate PASS_WITH_NON_BLOCKING_FINDINGS, Version 1.2 Accepted as Documentation Only; Implementation NOT READY

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003` is **complete as one local
documentation commit on `docs/mellycore-agent-runtime-scaffold-spec-review-003`;
not pushed.** Independent, read-only review of specification **version 1.2**.
Durable record:
`docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_003.md`; task report:
`docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003.md`.

**Two separate results are recorded, and neither substitutes for the other.**

**Documentation gate: `PASS_WITH_NON_BLOCKING_FINDINGS`** (P0 0 / P1 0 / **P2 2**
/ **P3 3**). Specification **version 1.2 is accepted as a documentation contract
only**, under nine acceptance constraints recorded in review record §25.2.

**Implementation readiness: `NOT_READY_IMPLEMENTATION_AFFECTING_FINDINGS`.**
**Implementation is not recommended and is not authorized.** One finding requires
an implementer to make an architectural determination the specification does not
supply.

**All seven Review 002 findings are independently disposed `CLOSED`** — each
traced to committed specification text, not accepted from the remediation report.
**All twelve Review 001 closures are independently confirmed preserved**, four
strengthened. **Agent Runtime Architecture §37 remains the sole canonical owner**
of the inert boundary, consumed unchanged: all eleven must-not and ten
may-implement items were traced, and every restatement is cited and subordinate.
**16/16 canonical Runtime operations remain covered** against an owner-derived
list. **All 32 metric rows reproduce with zero drift**, including the 32-property
Baseline Inert Invariant register and the 27 testing obligations. **No
false-success path exists** — the absence of a success member is structural.
**All fifteen upstream P2 findings remain open and contained.** The **1.1 → 1.2
increment is independently adjudicated valid** as a compatible corrective
increment under §44's own rules; no major bump is required.

**Five new non-blocking findings, three of them introduced by Remediation 002.**

- **`NEW-P2-01`** — §41 criterion 41 asserts that no normative citation depends on
  a mutable table row number. **Seven do**: §8 rule 4, §9.1 rule 3, §10 rule 5,
  §17 item 2, §34 obligations 25 and 26, and §41 criterion 4. **Obligations 25
  and 26 were added by the same commit that added criterion 41.** All seven
  resolve correctly today; the defect is a false self-report plus a latent
  fragility. **Blocking for any future amendment task.**
- **`NEW-P2-02`** — §27.1 rule 2 makes affirmative evidence conditional on "no
  §12 port has an injected implementation", but §26 treats "injected" and
  "approved-fixture" as distinct alternatives while §13 disposition 2 implies a
  fixture *is* injected. Whether a baseline inert composition containing an
  approved fixture may emit an affirmative record is **undetermined**. Both
  readings remain bounded by §27.1 rule 1's sentinel scoping, so no false-success
  path is created — but the implementer cannot choose without deciding a
  safety-relevant boundary. **Implementation-blocking.**
- **`NEW-P3-01`** — §44 rule 1 restates the current version as a literal while
  forbidding restatement "anywhere else", and instructs amendments to update only
  §44.1 and the header — so a compliant amendment leaves rule 1 stale,
  reproducing Review 002 `NEW-P2-01`. **Blocking for any future amendment task.**
- **`NEW-P3-02`** — §44.1's change-classification paragraph cites `§34.1`, which
  does not exist; the intended target is §31.1.1.
- **`NEW-P3-03`** — `EVIDENCE_INCOMPLETE` uses the owner error-class lexical
  convention, and because §27.1 rule 4 declares it not an error class, §24 rule 3
  does not apply and no rule constrains its representation. Advisory.

**Correction of record.** This review independently falsified the Remediation 002
claim, repeated in the section below and in `RUN_QUEUE.md` and `TASK_INDEX.md`,
that **every** positional `row N` citation was converted to a semantic reference.
Seven live positional citations remain (`NEW-P2-01`). The remediation artifact
itself was **not edited**; only this state record is corrected.

**Nothing is implemented.** No Scaffold source, module, Python package, test, or
fixture exists. Agent Runtime, framework adapters, Shared Context Bridge, package
loader, Package Validator, policy engine, Model Router, and provider integration
are all `NOT_IMPLEMENTED`. Runtime ports, composition roots, and no-op adapters
are **specified only; zero exist**. Agents executed, model calls, tool
executions, provider requests, and context mutations: **zero**. **Empirical
framework, provider, model, and runtime execution remains `NOT_PERFORMED`.**
Migration triggers #1, #4, #5, #6, and #7 remain uncrossed.

**Documentation acceptance is not implementation authorization.** The **Agent
Runtime Scaffold implementation** (inert code) remains a **plain-name item
carrying no task identifier** — none was minted by Review 002, Remediation 002,
or this review — and remains **blocked**, now additionally pending resolution of
`NEW-P2-02`, and still requiring separate explicit Operator authorization **and**
its own exact file allowlist. The recommended next step is a **bounded
remediation of `NEW-P2-02`**, preferably carrying the other four findings with
it; **this review neither minted nor authorized that task.** The global
higher-priority pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`
remains unchanged, in place, not reordered, and not reinterpreted.

## Agent Runtime Scaffold Spec Remediation 002 — Version 1.2, Documentation Only, Unverified

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002` is **complete as one
local documentation commit on
`docs/mellycore-agent-runtime-scaffold-spec-remediation-002`; not pushed.** It
remediated **all seven** findings recorded by Review 002 (P0 0 / P1 0 / **P2 1 /
P3 6**) and advanced
`docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` from version 1.1 to
**version 1.2**. Durable report:
`docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002.md`.

**The contract-version inconsistency is resolved structurally.** New **§44.1** is
an authoritative version-history table and the **single source of truth** for
`runtime_scaffold_spec_version`; §44 rule 1 now names `1.2`, cites §44.1, and
forbids restating the current version elsewhere as a drift-prone literal — the
exact mechanism that produced `NEW-P2-01`. Header, rule, history, report, and
state documents all read **1.2**.

**Most positional citations were made semantic.** Twenty-six `row N`
cross-references were converted to reference prohibitions and categories by
topic. **Correction, per Review 003 `NEW-P2-01`: this task's claim that *every*
positional citation was converted is false — seven remain** (§8 rule 4, §9.1
rule 3, §10 rule 5, §17 item 2, §34 obligations 25 and 26, §41 criterion 4), two
of them introduced by this remediation. All seven resolve correctly; the residual
fragility is recorded against a future amendment task. The two defective threat
citations are fixed at the source: threat 8
now cites §8's hook-registration prohibition by name, and threat 19 cites **§8
rule 3**, the actual environment-access owner. New acceptance criterion 41 makes
semantic referencing a standing requirement.

**The invariant test obligation is now complete and drift-proof.** New
**§31.1.1** is a **Baseline Inert Invariant property register of 32 enumerable
properties** — every side-effect category plus identifier generation, registry
and service-locator absence, fail-closed execution, absence of a success
representation, and absence of a live Runtime handle. §34 obligation 18 must
assert **every** row and derive its list mechanically, so adding a register row
without an assertion fails the obligation rather than silently narrowing it.
Obligations 25, 26, and 27 were added; testing obligations 24 → **27**.

**Scaffold Zero-Execution Evidence is now affirmative-only.** The contradiction
between "must not be emitted when evidence is incomplete" and "must render
`unknown`" is resolved in the stricter direction: incomplete evidence —
including whenever any port is injected — yields **no zero-execution record at
all**, and the run records the distinct non-affirmative **`EVIDENCE_INCOMPLETE`**
outcome instead. That outcome is explicitly **not** zero-execution evidence, not
a Runtime result, not Runtime success, not a Control Plane status, and **not an
error class** — §24's owner-owned taxonomy is unchanged. **Incomplete evidence ≠
affirmative zero-execution evidence.**

**Cancellation is deterministic.** §26 gained a normative selection order — a
malformed reference yields *invalid handle*; otherwise, with no injected
implementation, **implementation unavailable is the inert default**; only
owner-supplied input reaches the remaining states. §14's operation disposition,
§26, the outcome mapping, and new obligation 27 all express the same rule, and
successful cancellation of active work remains unreachable. The last bare owner
`§37` reference is fully qualified.

**Version 1.2 is a compatible corrective increment, not a major bump.** Every
change is a citation correction with no normative effect, a strict addition, or
the resolution of an internal contradiction toward the stricter branch. **No
prohibition, boundary, port, disposition, side-effect category, or owner
constraint is removed, narrowed, or made more permissive**, and §3.1's
precedence chain is untouched.

**All twelve Review 001 closures are preserved** — four strengthened — and
**Agent Runtime Architecture §37 remains the sole canonical owner**, consumed
unchanged. **16/16 canonical Runtime operations remain covered**; **all fifteen
upstream P2 findings remain open and contained**; and the original task report,
both Review 001 artifacts, the Remediation 001 report, both Review 002
artifacts, and every owner document are **byte-identical**.

**Nothing is implemented.** Agent Runtime Scaffold code, Agent Runtime, framework
adapters, Shared Context Bridge, package loader, Package Validator, policy
engine, Model Router, and provider integration are all `NOT_IMPLEMENTED`.
Runtime ports, composition roots, and no-op adapters are **specified only; zero
exist**. Agents executed, model calls, tool executions, provider requests, and
context mutations: **zero**. **Empirical framework, provider, model, and runtime
execution remains `NOT_PERFORMED`.** Migration triggers #1, #4, #5, #6, and #7
remain uncrossed.

**Version 1.2 is unverified.** This remediation corrected findings recorded
against its own subject; no independent party has confirmed the closures, and
**the Review 002 gate is not re-opened by this task**. **Exact next task:**
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003` — an independent, read-only
review of version 1.2. Not started, not authorized by this entry. The **Agent
Runtime Scaffold implementation** (inert code) remains a **plain-name item
carrying no task identifier** and remains **blocked**, requiring Review 003 to
pass **and** separate explicit Operator authorization **and** its own exact file
allowlist. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Agent Runtime Scaffold Review 002 — Gate PASS_WITH_NON_BLOCKING_FINDINGS, Version 1.1 Accepted as Documentation Only

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002` is **complete as one local
documentation commit on
`docs/mellycore-agent-runtime-scaffold-spec-review-002`; not pushed.** Gate
**`PASS_WITH_NON_BLOCKING_FINDINGS`** — **P0 0 / P1 0 / P2 1 / P3 6**. Durable
record: `docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_002.md`;
task report: `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002.md`.

`MELLYCORE_AGENT_RUNTIME_SCAFFOLD_001` **version 1.1 is accepted as a
documentation contract only.** The review treated the remediation report as an
unverified claim set: **all twelve Review 001 findings (P2 7 / P3 5) were
independently disposed `CLOSED`**, each traced to specific committed
specification text rather than accepted from the report.

**Agent Runtime Architecture §37 remains the sole canonical owner** of the inert
Runtime boundary. The owner section was extracted verbatim and decomposed; all
eleven "must not implement" items — including **queues**, the item Review 001
found missing — are now traced into the specification, and the single
restatement (§8 rule 4) is explicitly cited and marked subordinate. **No
competing owner is created and no owner requirement is broadened.**

**16/16 canonical Runtime operations** carry a scaffold disposition, verified
against an operation set derived from the owner's §16 (nine bridge) and §17.1
(seven context) rather than from the specification. **All 30 document metric
rows reproduce with zero drift.** **No false-success path exists** — no
execution-success outcome is representable, and every one of the sixteen
operations refuses. The **Baseline Inert Invariant** (§31.1) is coherently
scoped and makes no claim about injected components; **Injected Component
Eligibility** (§31.2) requires seven separate validations and treats an
unvalidated component as unavailable. Executable configuration is rejected
fail-closed across three independent barriers; nineteen deferred-effect
mechanisms are bound exactly as constructors are; queue safety spans eight
surfaces; logging and randomness are treated as side effects; and **Scaffold
Zero-Execution Evidence** is derived, correlation-scoped, explicitly
non-canonical, and never a Runtime result or a Control Plane status dimension.

**Seven new non-blocking findings** were recorded. The single **P2**
(`NEW-P2-01`) is §44 rule 1 declaring the specification version "currently
`1.0`" while the header reads 1.1 — consistent at v1.0 and invalidated by the
remediation, the same defect class the Agent Package track adjudicated P2. Of
the six **P3** findings, **two are citation-level regressions introduced by
Remediation 001**: §37 threat 8's `§8 row 10` citation was broken by the 12→19
import-table renumbering, and §43.1 retains a bare `§37` against the document's
own new convention. The remaining four concern obligation 18's conjunct
enumeration, an evidence-record emission conflict, a cancellation default-state
disagreement between §14 and §26, and a pre-existing mis-citation Review 001 did
not detect. **None weakens a prohibition; none creates a permissive path; every
one is fail-closed in each of its readings.**

**All fifteen upstream P2 findings remain open and contained** — reconstructed
independently from the Agent Package (3), Framework Bridge (4), and Shared
Context Bridge (8) review records, none silently resolved, and no normative
scaffold rule depends on any of them. **No upstream contract, review artifact,
remediation report, source file, test, dependency, or configuration file was
edited.**

**Nothing is implemented.** Agent Runtime Scaffold code, Agent Runtime,
framework adapters, Shared Context Bridge, package loader, Package Validator,
policy engine, Model Router, and provider integration are all `NOT_IMPLEMENTED`.
Runtime ports, composition roots, and no-op adapters are **specified only; zero
exist**. Agents executed, model calls, tool executions, provider requests, and
context mutations: **zero**. **Empirical framework, provider, model, and runtime
execution remains `NOT_PERFORMED`.** Migration triggers #1, #4, #5, #6, and #7
remain uncrossed.

**Review passing is not implementation authorization.** The **Agent Runtime
Scaffold implementation** (inert code) is the **exact next plain-name item and
carries no task identifier — Review 002 minted none**. It requires **separate
explicit Operator authorization** and its own exact file allowlist before it may
begin, and permits no framework process, provider call, credential, model call,
tool execution, or deployment even once started. Four findings are **blocking
for that task** and should be closed first: `NEW-P2-01`, `NEW-P3-03`,
`NEW-P3-04`, and `NEW-P3-05`. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Agent Runtime Scaffold Spec Remediation 001 — Version 1.1, Documentation Only, Unverified

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001` is **complete as one
local documentation commit on
`docs/mellycore-agent-runtime-scaffold-spec-remediation-001`; not pushed.** It
remediated **all twelve** findings recorded by Scaffold Review 001 (P0 0 / P1 0 /
P2 7 / P3 5) and advanced
`docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` from version 1.0 to
**version 1.1**. Durable report:
`docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001.md`.

**Outcome-code history, now recorded in tracked state.** The specification run's
outcome was **`AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED`** — the pre-review
state of version 1.0. Review 001 subsequently issued
`PASS_WITH_NON_BLOCKING_FINDINGS`, accepting version 1.0 as documentation only
under eleven constraints. This remediation addressed those constraints. Review
001's evidence was **not rewritten**; both its artifacts are byte-identical.

**The inert-mode invariant was split into two distinct properties.** New **§31.1
Baseline Inert Invariant** applies to a *baseline inert composition* — default
inert configuration, **no live external implementation injected**, and only
repository-approved inert fixtures or unavailable ports present — and guarantees
zero side effects across all twenty-four §32 categories, no execution-success
representation, a fail-closed refusal of every execution request, no live Runtime
Handle, and no framework, provider, model, package, tool, MCP, or Shared Context
action. Its scope is now **exact**: it makes no claim about a composition
containing an injected live implementation. New **§31.2 Injected Component
Eligibility** states that an injected component **inherits nothing from
satisfying a Python interface** and requires seven separate validations —
side-effect declaration, import safety, construction safety, capability boundary,
permission boundary, fixture identity, observability behavior — before
participating in any future authorized mode; an unvalidated component is treated
as **unavailable**. **No live-mode invariant was invented.** The single property
holding regardless of injection is the §15 execution refusal.

**Queue safety now spans the whole boundary.** Creating an in-process, async, or
worker queue; enqueueing background work; consuming queued work; starting a queue
processor; registering a queue callback; and creating scheduler-backed, delayed,
or deferred jobs are prohibited at import (§8 row 16), at construction and in
every deferred-effect mechanism (§9.1 row 18), in the side-effect inventory (§32
row 21), in the invariant (§31.1), in future tests (§34 obligation 22), in
security (§37 threat 20), and in non-goals (§39 item 19) — closing the omission
of one of Agent Runtime Architecture §37's eleven must-not items. The scaffold
implements no queue inspection and no queue runtime behavior.

**"Zero-execution confirmation" was renamed Scaffold Zero-Execution Evidence**
and given normative §27.1 with eight required properties: derived from observed
attempts and side-effect sentinels rather than asserted; scoped to exactly one
correlation identifier or validation run; explicitly non-canonical; not a Control
Plane status dimension; limited to its own evidence boundary; **not** a Runtime
run result; **not** equivalent to Runtime success; and **not emitted when
evidence is incomplete**. It renders `unknown` for every category an injected
port could affect, and fabricates no live run identifier.

**Configuration gained fourteen executable-content prohibitions** (8 → **22**):
import-by-string implementation paths, executable callbacks, serialized
callables, pickled objects, dynamic expressions, template expressions, shell
commands, subprocess arrays, plugin entry points, framework auto-import
directives, module-level factory names, arbitrary code snippets, deserialization
hooks, and environment interpolation resolving secrets or executable targets.
Configuration validation **rejects executable content fail-closed** (§30 layer
5); "declared injected port names" is now **inert descriptive metadata, never a
resolution mechanism**; and a static symbolic reference is permitted only when it
cannot trigger an import, construction, or code invocation, remains inert
metadata, and requires future explicit resolution by a separately authorized
owner.

**Construction safety gained §9.1**, binding **nineteen deferred-effect
mechanisms** — `__post_init__`, lazy and cached properties, descriptors,
class-level registration, metaclass hooks, default factories, callable defaults,
dependency factories, finalizers, sync and async context-manager entry,
background and scheduled callbacks, deferred imports, deferred socket, thread,
process and queue creation, and first-method-call initialization — to §32 exactly
as constructors are bound. Postponing a prohibited action to first property
access, first method call, context entry, or destruction is **the same
violation**.

**Import safety separated reads from writes** (12 → **19** prohibitions): reading
a file, scanning a directory, and probing for SDK, package, distribution, or
entry-point presence by file test, metadata query, or package-manager access are
each prohibited, while metadata already supplied by the import system may be
inspected because it performs no additional access. **Cancellation reachability**
is now explicit per state, with successful cancellation of active work,
cancellation of a live operation, and any outcome implying work was stopped named
**unreachable**, and mutable live-operation state prohibited. **Logging and
randomness** became side-effect categories in their own right (20 → **24**):
default console, stdout, and stderr output prohibited; implicit randomness
prohibited, with identifiers and timestamps sourced only from injected ports or
fixed fixtures.

**Agent Runtime §37 ownership is preserved and strengthened.** Every
cross-document reference is now written in full as **"Agent Runtime Architecture
§37"**, with a normative convention that a bare `§37` denotes this document's own
§37; the previously uncited restatement in §8 rule 4 now opens "Per Agent Runtime
Architecture §37 … the following subordinate implementation constraint applies",
and §17 prohibition 2 cites the owner rather than the local rule. **No owner
document was edited.**

**Validation.** All **30** metric rows reproduce mechanically with **zero drift**
and the 44-section structure recounts exactly; **16/16 canonical Runtime
operations remain covered** against an owner-derived list; **all fifteen upstream
P2 findings remain open and contained**; the original specification task report
and **both Review 001 artifacts are byte-identical**; and the aggregate digest of
every tracked `.py` under `scripts/` and `tests/` is unchanged at
`4e6028746b186b09` with the tracked count unchanged at 71. Exactly eight files
changed. `git diff --check` exit `0`; `py -3.9 scripts/validate_project_state.py`
`PASS`, exit `0` — both at baseline and post-commit. `pytest`, black, flake8, and
mypy were not run and are not claimed passing.

**Nothing implemented.** Agent Runtime Scaffold code, Agent Runtime, framework
adapters, Shared Context Bridge, package loader, Package Validator, policy
engine, Model Router, and provider integration are all `NOT_IMPLEMENTED`.
Runtime ports, composition roots, and no-op adapters **specified only; zero
exist**. Agents executed, model calls, tool executions, provider requests, and
context mutations: **zero**. **Empirical framework, provider, model, and runtime
execution remains `NOT_PERFORMED`.** Migration triggers #1, #4, #5, #6, and #7
remain uncrossed.

**Version 1.1 is unverified.** This remediation corrected its own reviewed
findings; no independent party has confirmed the closures, and **the Review 001
gate is not re-opened by this task**. **Exact next task:**
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002` — an independent, read-only
re-review. Not started, not authorized by this entry. The **Agent Runtime
Scaffold implementation** (inert code) remains **blocked**, requiring Review 002
to pass **and** separate explicit Operator authorization **and** its own exact
file allowlist. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.

## Agent Runtime Scaffold Review 001 — Gate PASS_WITH_NON_BLOCKING_FINDINGS, Documentation Only

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001` is **complete as one local
documentation commit on
`docs/mellycore-agent-runtime-scaffold-spec-review-001`; not pushed.**
Independent, read-only architecture, fail-closed, import-safety, and
cross-contract review of the Agent Runtime Scaffold Specification (version 1.0,
commit `f11e4c1`). Durable record:
`docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_001.md`; task
report: `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001.md`.

**Gate decision: `PASS_WITH_NON_BLOCKING_FINDINGS`. P0 = 0, P1 = 0, P2 = 7,
P3 = 5.** `MELLYCORE_AGENT_RUNTIME_SCAFFOLD_001` version 1.0 is **accepted as a
documentation contract only**, under the eleven constraints recorded in the
review record §13.

**Two verifications were performed against primary sources rather than the
specification's own descriptions.** First, the canonical operation set was
derived from the owner by locating every table in the Agent Runtime
specification carrying an `Operation` header column — **exactly two exist**,
§16's nine bridge operations and §17.1's seven context operations — which
establishes the sixteen-operation set as **canonical, not an author-created
aggregation**. All sixteen are named explicitly with a scaffold disposition,
**zero invented and zero omitted**, and not one can return successful
execution. Second, the Provider Adapter Scaffold precedent was checked against
the actual Python source: `OperationOutcome` contains **no success member**,
`ExecutionState` is a single-member `DISABLED` enum, `ImplementationState`,
`NetworkBehavior`, and `CredentialSupport` are likewise single-member, the
disabled adapter validates its static manifest at construction and returns
`provider_request_occurred=False`, and `tests/test_provider_adapters.py`
already patches `socket.socket.connect` and scans package source for prohibited
tokens. **All eight precedent claims are accurate.**

**Agent Runtime §37 is genuinely consumed, not duplicated.** §37 was decomposed
into twenty-four discrete requirements and each traced into the reviewed text.
Twenty-two are cited, structurally elaborated, or covered by a deliberately
distinct taxonomy; §44 rule 6 — "a change to Runtime §37 is not an amendment to
this document" — is the correct structural guard. **No second owner is
created.** The "all eleven authorization facts" requirement was independently
confirmed canonical against Agent Runtime §14.

**All 27 document-metric rows reproduce independently, with zero
discrepancies**, and the 44-section structure recounts exactly (numbered 1–44,
contiguous). **No false-success path exists** — independently searched across
the execution outcome vocabulary, the §29 data records, and the §27
observability fields. **Zero capability ordinal citations** were found, and the
canonical six-member framework vocabulary is used exactly, with `other`,
`generic`, `auto`, and `custom` appearing only inside the prohibition.

**Seven new P2 findings, all non-blocking and all fail-closed.** `NEW-P2-01`:
§31 rule 2 ("regardless of … injected ports") contradicts the inert-mode
invariant's own precondition ("no externally injected implementations"), making
the specification's primary acceptance target self-contradictory in the
stricter direction. `NEW-P2-02`: the invariant is asserted by no specified
test — §31 rule 3 cites obligation 12 (zero-context-mutation), the
specification's own task report says 13, and filesystem reads and logging have
no obligation at all. `NEW-P2-03`: §8 rule 4 restates Runtime §37's "no
framework SDK import on any reachable path" without citation, contradicting §3
row 1's own prohibition on restating §37, and §17 then cites §8 rule 4 rather
than the owner. `NEW-P2-04`: **"queues" — one of §37's eleven must-not-implement
items — appears nowhere in the specification**, and §32 has no queue category,
so a passive in-memory queue would trip none of the twenty categories the
invariant is closed over. `NEW-P2-05`: §27 field 12 "zero-execution
confirmation" is stated as an unscoped claim about the world and could become
false once a real port implementation is injected. `NEW-P2-06`: §10's
configuration prohibitions omit executable content — dotted import paths,
callbacks, dynamic expressions, shell commands — while permitting "declared
injected port names"; only §7 rule 3 currently closes the path. `NEW-P2-07`:
§9's construction-safety rules omit deferred-effect mechanisms — lazy and
cached properties, `__del__` finalizers, default factories, descriptors, and
class-creation hooks. **Five P3 findings** are editorial, including that the
specification run's outcome code
`AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED` is recorded in **no tracked
file** — a Phase 0 baseline mismatch reported before mutation, and the same
defect class Framework Bridge Review 001 recorded as its own `NEW-P3-04`.

**All fifteen upstream P2 findings remain open and contained**, none silently
resolved, none required normatively, and none converted into a scaffold-owned
decision. **No upstream contract or review artifact was edited.**

**Nothing implemented.** Agent Runtime Scaffold code, Agent Runtime, framework
adapters, Shared Context Bridge, package loader, Package Validator, policy
engine, Model Router, and provider integration are all `NOT_IMPLEMENTED`.
Runtime ports, composition roots, and no-op adapters **specified only; zero
exist**. Agents executed, model calls, tool executions, provider requests, and
context mutations: **zero**. Framework SDKs remain `NOT_INSTALLED` /
`NOT_IMPORTED` / `NOT_EXECUTED`. **Empirical framework, provider, model, and
runtime execution remains `NOT_PERFORMED`.** Migration triggers #1, #4, #5, #6,
and #7 remain uncrossed.

**Validation.** Exactly eight files changed (two new documentation artifacts,
six bounded state-sync edits); **no source, test, Python package, dependency,
configuration, workflow, or runtime file changed** — the aggregate digest of
every tracked `.py` under `scripts/` and `tests/` is byte-identical before and
after, and the tracked file count is unchanged at 71. `git diff --check` exit
`0`; `py -3.9 scripts/validate_project_state.py` `PASS`, exit `0` — both at
baseline and post-commit. `pytest`, black, flake8, and mypy were not run and are
not claimed passing. The reviewed specification was **not edited** and this
review repaired nothing.

**Acceptance is of documentation only and authorizes no downstream task.** Per
canonical `RUN_QUEUE.md`, the next item in this track is the **Agent Runtime
Scaffold implementation (inert code)**, recorded there as a plain-name item
carrying no task identifier. It remains **blocked** and requires this review's
acceptance, **separate explicit Operator authorization**, and its own exact file
allowlist; **no identifier was minted, started, or authorized by this review.**
Scaffold Implementation Review, first Agent Package, Cross-Agent Smoke,
Integration Review, the six per-framework adapter specifications, and every
deferred contract of the specification's §40 each remain blocked behind their
own gate. The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, in
place, not reordered, and not reinterpreted.
