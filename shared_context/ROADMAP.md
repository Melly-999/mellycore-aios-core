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
  (branch `fix/mellycore-source-arena-nasa-runtime-retirement-001`, draft PR
  open, pending review); replaced with a local, deterministic Source Archive.
  Historical task reports and release evidence remain untouched. It was never
  a current pillar, roadmap module, or core integration.

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
