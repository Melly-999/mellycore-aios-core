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
- **NASA Images:** retained only as legacy prototype code and historical release
  evidence. It is not a current pillar, roadmap module, or core integration.

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

The exact next task is **`MELLYCORE-OPERATIONS-DATA-CONTRACT-001`**, which
translates the approved logical contracts into fixture/schema artifacts and
validation requirements — still specification/fixture scope, not runtime
implementation. Its work exists on two separate, unmerged local branches
today: the original `docs/mellycore-operations-data-contract-001`
(2026-07-19), and a second pass, `docs/mellycore-operations-data-contract-001-v2`,
which defines eleven dashboard-facing fixture entities
(`operation_run`, `task_record`, `agent_identity`, `model_provider_usage`,
`token_cost_record`, `validation_result`, `artifact_record`,
`environment_capability_snapshot`, `approval_gate`, `safety_status`,
`recommendation_ledger_entry`) in
`docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`; see
`docs/tasks/MELLYCORE-OPERATIONS-DATA-CONTRACT-001.md`. Status in canonical
`main` for both branches: `NOT_PRESENT_PENDING_INTEGRATION`. This roadmap does
not claim either branch's content is canonical and does not reorder its track.

`MELLYCORE-OPERATIONS-DATA-CONTRACT-BRANCH-RECONCILIATION-001` has since
compared both branches and selected `-v2` as the canonical integration
candidate (no push, no merge); see that document's Section 6 in
`docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`. Four file pairs
from the original branch, covering AI Estate Inventory, Skill Gap Detector,
and Memory Freshness Monitor, were judged not superseded and remain deferred
to a further, separately authorized follow-up task.

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
