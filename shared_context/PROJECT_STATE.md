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
`fix/mellycore-source-arena-nasa-runtime-retirement-001` (PR #15: visual
acceptance complete — `PASS_WITH_NON_BLOCKING_NOTES`; the two P2 findings
(procedural swatch palette, mission-rail scrollbar theming) resolved in a
follow-up commit; ready for the final merge-gate review). The Source Arena
tab now renders a local, deterministic Source Archive dataset — zero
external requests, no API key. Historical NASA task reports and `v0.2.0`
release evidence remain untouched as the historical record. This status is
accurate for that branch/PR; canonical `main` reflects it only once the PR
is reviewed and merged.

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
runtime retirement (accepted by this ADR as a prerequisite) is implemented
locally on `fix/mellycore-source-arena-nasa-runtime-retirement-001` (PR #15,
visual acceptance complete, ready for final merge-gate review, not yet
merged); the renderer and vendoring themselves remain unimplemented and
require their own separately-authorized implementation task.

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
