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
- **Holographic Source Arena:** accepted specification only. Its 390×844
  model-lens hero remains the lead visual direction; the 3D treatment is not
  implemented.
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

**Current blocker.** PR #17
(https://github.com/Melly-999/mellycore-aios-core/pull/17, branch
`feat/mellycore-source-arena-renderer-static-slice-001`, head
`08642089f9c062928c72d3968fd23843a5e9995d`) implements the static holographic
Source Arena renderer slice and its orbit-clipping fix, but is **blocked from
merge** by a failed Sourcery check flagging a possible XSS/static-analysis
finding around `innerHTML` in `site/js/dashboard.js:509` and
`site/js/dashboard.js:554-561`. The Source Arena static slice is **not
canonical** until PR #17 merges clean. No merge may occur until that finding
is triaged and resolved.

**Active task sequence** (supersedes any prior "first deploy" framing; this
section is the authoritative Option B ordering):

1. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-XSS-FINDING-TRIAGE-001` —
   resolve the failed Sourcery XSS/static-analysis finding on PR #17. No merge
   until clean.
2. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-MERGE-GATE-001` — merge PR
   #17 only if clean; verify canonical `main`.
3. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-001` —
   update living docs after PR #17 merge (local docs commit only).
4. `MELLYCORE-SOURCE-ARENA-RENDERER-STATIC-SLICE-POST-MERGE-STATE-SYNC-PUBLISH-001`
   — push, PR, review, merge that docs sync.
5. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-SPEC-001` — docs/spec only; define
   the Model Router Observatory UX; no API calls, no keys, no backend.
6. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-STATIC-SNAPSHOT-SLICE-001` —
   implement the static snapshot panel from a local fixture only; no live
   OpenRouter fetch, no API key, no model calls, no backend.
7. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-VISUAL-ACCEPTANCE-001` — visual/
   product review confirming it reads as a Model Router Observatory, not a
   table dump.
8. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-FINAL-REVIEW-001` — final
   technical review; transition to PR-ready if clean.
9. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-MERGE-GATE-001` — merge if clean;
   canonical-main verification.
10. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-POST-MERGE-STATE-SYNC-001` —
    update living docs after the OpenRouter static panel merges.
11. `MELLYCORE-OPENROUTER-MODEL-OBSERVATORY-POST-MERGE-STATE-SYNC-PUBLISH-001`
    — push, PR, review, merge that docs sync.
12. `MELLYCORE-STATIC-DEPLOYMENT-READINESS-001` — decide whether deploy is
    allowed; confirm deploy target; confirm no secrets, no provider calls, no
    backend, no false live claims.
13. `MELLYCORE-STATIC-SHOWCASE-DEPLOYMENT-001` — first static deploy, only if
    explicitly authorized; no backend, no provider keys, no runtime API.
14. `MELLYCORE-STATIC-SHOWCASE-POST-DEPLOY-VERIFY-001` — verify the deployed
    URL; desktop/mobile smoke; no NASA/OpenRouter/provider/model calls unless
    explicitly intended; no console errors; truthful-state copy.
15. `MELLYCORE-DEPLOYMENT-STATE-SYNC-001` — record deployed status and URL;
    update `README.md` / `PROJECT_STATE.md` / `ROADMAP.md` / `RUN_QUEUE.md` /
    `AGENT_HANDOFF.md`.

None of tasks 2–15 is started, active, or authorized by this roadmap entry
alone; each requires its own gate to pass in order.

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
authorized. The OpenRouter Observatory is a selected roadmap target only; it
is not implemented, and no OpenRouter API key, account, or live catalog call
is authorized by this roadmap entry.

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
