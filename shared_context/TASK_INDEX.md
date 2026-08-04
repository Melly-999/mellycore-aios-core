# Task Index

Canonical index of MellyCore AIOS task identifiers. Status values:

- `COMPLETE` — task finished; may still be unpushed (local documentation
  commit) or merged (see the linked evidence for which).
- `IN_PROGRESS` — started, not complete.
- `ELIGIBLE` — a gate has cleared it for Operator authorization; it has not
  been authorized or started.
- `BLOCKED` — not eligible; a prior gate, review, or Operator authorization is
  outstanding.
- `PLANNED` — named in the roadmap; no gate has run yet.

This index does not itself authorize, start, or claim implementation of any
task. Full narrative detail lives in `shared_context/ROADMAP.md`,
`shared_context/RUN_QUEUE.md`, `shared_context/PROJECT_STATE.md`, and
`shared_context/PROJECT_HISTORY.md`; durable per-task evidence lives in
`docs/tasks/`.

## Global Pointer

| Task ID | Status | Notes |
|---|---|---|
| `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` | `IN_PROGRESS` | Global higher-priority pointer; independently governed; not reordered by any track below. See `RUN_QUEUE.md`'s "Current" section. |

## Agent Runtime Product Track

| Task ID | Status | Evidence |
|---|---|---|
| `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001` | `COMPLETE` (local, not pushed) | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`, `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md` |
| `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `FAIL_REMEDIATION_REQUIRED` | `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md` |
| `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001` | `COMPLETE` (local, not pushed) — unverified pending review | `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` |
| `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` | `COMPLETE` (local, not pushed) — gate `PASS_WITH_NON_BLOCKING_FINDINGS` | `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md` |
| `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` | `COMPLETE` (specification only, local, not pushed) — **unverified** | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md`, `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` |
| `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `FAIL_REMEDIATION_REQUIRED` (P0 0 / P1 1 / P2 3 / P3 3) | `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md`, `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md` |
| `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001` | `COMPLETE` (local, not pushed) — unverified pending review | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`; spec advanced to v1.1 |
| `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002` | `COMPLETE` (local, not pushed) — gate `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 3 / P3 4); all seven Review 001 findings `CLOSED`; spec v1.1 accepted as documentation contract only, no implementation | `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md`, `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002.md` |
| `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001` | `COMPLETE` (specification only, local, not pushed) — **unverified**; task ID minted by explicit Operator authorization (previously unidentified in the queue). Documentation only: no bridge, adapter, SDK, or framework integration exists | `docs/specs/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001.md`, `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001.md` |
| `MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 4 / P3 4); spec v1.0 accepted as documentation contract only, no adapter or framework integration exists | `docs/research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`, `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001.md` |
| `MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001` | `COMPLETE` (specification only, local, not pushed) — **unverified**; task ID minted by explicit Operator authorization for the queued plain-name item "Shared Context Bridge". Documentation only: no bridge, mutation engine, storage, memory service, or compression implementation exists | `docs/specs/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001.md`, `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001.md` |
| `MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 8 / P3 2); spec v1.0 accepted as documentation contract only; all 34 metric rows independently reproduced with zero discrepancies; all seven upstream P2 findings remain open and contained; no bridge, mutation engine, storage, database, vector store, memory service, compression, validation, or proposal-lifecycle runtime exists | `docs/research/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`, `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001.md` |
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-001` | `COMPLETE` (specification only, local, not pushed) — **unverified**; task ID minted by explicit Operator authorization for the queued plain-name item "Agent Runtime Scaffold (inert)" after a repository-wide search confirmed no conflicting identifier. Documentation only: **no scaffold code, module, Python package, test, Runtime, framework adapter, package loader, or provider/model integration exists**; all fifteen upstream P2 findings remain open and deferred | `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md`, `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-001.md` |
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001` | `ELIGIBLE` | Exact next task: independent, read-only review of the Agent Runtime Scaffold specification. Not started, not authorized. |
| Agent Runtime Scaffold implementation (inert code) | `BLOCKED` | Requires the specification review to pass **and** separate explicit Operator authorization. No framework process, provider call, credential, model call, tool execution, or deployment permitted even once started. |
| Scaffold Implementation Review | `BLOCKED` | Requires the inert scaffold implementation to exist first. |
| First Agent Package | `BLOCKED` | Requires Scaffold Review to pass. |
| Cross-Agent Smoke (inert modes only) | `BLOCKED` | Separate clean-worktree task per `RUN_QUEUE.md`'s "Deferred Work". |
| Integration Review | `BLOCKED` | Final gate of this track. |

## Developer Platform & Agent Package Ecosystem (Planned)

All rows `PLANNED` unless noted. None is authorized, started, or implemented
by this index. Each requires its own specification, independent review, and
explicit Operator authorization before implementation, exactly like the Agent
Runtime track above.

| Task ID | Status | Notes |
|---|---|---|
| `MELLYCORE-SHARED-CONTEXT-EXPANSION-001` | `PLANNED` | Expands Shared Context contracts to carry Agent Package metadata and Developer Platform registries. |
| `MELLYCORE-MULTI-AGENT-WORKFLOW-001` | `PLANNED` | Cross-agent handoff and coordination workflows, built on the accepted Agent Runtime handoff model. |
| `MELLYCORE-COMMANDS-LAYER-SPEC-001` | `PLANNED` | Command Registry: provider-agnostic slash-command contract. |
| `MELLYCORE-SKILLS-LAYER-SPEC-001` | `PLANNED` | Skill Registry: packaged, reusable workflow contract. |
| `MELLYCORE-HOOKS-LAYER-SPEC-001` | `PLANNED` | Hook Registry: event-driven automation contract. |
| `MELLYCORE-PLUGIN-LAYER-SPEC-001` | `PLANNED` | Plugin Registry: bundles of commands/skills/hooks/agents/MCP servers. |
| `MELLYCORE-MCP-LAYER-SPEC-001` | `PLANNED` | MCP Registry: Model Context Protocol server registration and discovery, provider-agnostic. |
| `MELLYCORE-DEVELOPER-PLATFORM-SPEC-001` | `PLANNED` | Umbrella spec unifying the five registries above with Package Validation, Package Lifecycle, and Package Distribution. |
| `MELLYCORE-PACKAGE-ECOSYSTEM-SPEC-001` | `PLANNED` | Distribution, discovery, and trust model for third-party Agent Packages. |

### Agent Package Contract Follow-Ups (Named by Spec §26; No Task ID Assigned Yet)

`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` §26 names twelve
follow-up contracts. Five overlap in scope with the rows above (Skill, Hook,
Command, Plugin, and MCP Registries); six are net-new concepts not yet named
with a task ID anywhere else in this repository, listed here as `PLANNED`
concepts only, per the same rule this index applies elsewhere — no row here
is a task ID until `ROADMAP.md` or `RUN_QUEUE.md` names one:

- Agent Manifest contract
- Capability Contract
- Package Validation
- Package Lifecycle
- Package Distribution
- Package Repository (the Agent Package Store / Package Registry
  implementation itself)

Plus one review: the Batch Orchestration compatibility review named in §26,
which requires a Batch Orchestration contract to exist first.

## Completed Milestones (Pre-Agent-Runtime)

See `shared_context/PROJECT_HISTORY.md` for the full chronological ledger.
Summary pointer only:

| Milestone | Status |
|---|---|
| Context Gate I1–I4 | `COMPLETE` (implemented) |
| Operational Trust / Loop Operations | `COMPLETE` (report-only, closed) |
| AI Operations Intelligence spec | `COMPLETE` (merged, PR #7) — `SPECIFIED`, not implemented |
| Operations Data Contract | `COMPLETE` (merged, PR #13) — schema/fixture scope |
| Source Arena Hybrid Renderer ADR | `COMPLETE` (merged, PR #8) — `ACCEPTED`, not implemented |
| Source Arena static CSS/DOM renderer slice | `COMPLETE` (merged, PR #17) |
| NASA runtime retirement | `COMPLETE` (merged, PR #15) |
| Cloudflare API Shield read-only adapter | `COMPLETE` (local) — review 002 `PASS_WITH_NON_BLOCKING_FINDINGS` |
| Vercel Static Root | `COMPLETE` (merged, published) |
| OpenAI Batch Stage B | `COMPLETE` (merged) — Stage C `BLOCKED` |

## How to Extend This Index

Add a row when a task ID is first named in `ROADMAP.md` or `RUN_QUEUE.md`.
Update its status in place as gates resolve. Never mark a row `COMPLETE`
without a durable evidence link, and never mark a row as implemented when the
linked evidence states specification-only or documentation-only scope.
