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

The local dashboard's NASA Images browser GETs are **legacy prototype
implementation**, retained as historical evidence. NASA Images is not a current
product pillar, roadmap module, or intended core integration. This docs-only
positioning task does not claim that the legacy code was removed.

## Specified, Not Implemented

The accepted Holographic UI specification defines Source Arena as the leading
visual metaphor and first hero image: a 390×844 mobile model-lens composition.
Overview/core/orbit/hull remains supporting imagery only. The complete
holographic/3D Source Arena, real operational adapters, and approval-execution
surface are not implemented.

## Planned Direction

The Observatory roadmap includes Mission Control, Agent Activity, Context Pulse,
Model Router, Unified Run Ledger, Approval Queue, Memory & Recommendation Ledger,
AI Estate Inventory, Skill Gap Detector, and Memory Freshness Monitor. These are
planned domains, not current capability claims.

Next roadmap task: `MELLYCORE-AI-OPERATIONS-INTELLIGENCE-001` — specification
only. Detailed schema and implementation contracts are intentionally deferred to
that task and later separately approved work.

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
