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
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 7 / P3 5); spec v1.0 accepted as documentation contract only; all 27 metric rows independently reproduced with zero discrepancies; Agent Runtime §37 verified **consumed, not duplicated**; **16/16 canonical Runtime operations covered** against an owner-derived list; **no false-success path found**; all fifteen upstream P2 findings remain open and contained; no scaffold code, module, Python package, test, Runtime, framework adapter, package loader, or provider/model integration exists | `docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_001.md`, `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001.md` |
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001` | `COMPLETE` (local, not pushed) — **unverified pending Review 002**; remediated **all twelve** Review 001 findings (P2 7 / P3 5) and advanced the specification to **version 1.1**. The pre-review specification outcome was `AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED`; Review 001 then returned `PASS_WITH_NON_BLOCKING_FINDINGS`. Documentation only: **no scaffold code, module, Python package, test, Runtime, framework adapter, package loader, or provider/model integration exists**; all fifteen upstream P2 findings remain open | `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` (v1.1), `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001.md` |
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002` | `COMPLETE` (local, not pushed) — gate `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 1 / P3 6); spec **v1.1** accepted as documentation contract only; **all twelve Review 001 findings independently disposed `CLOSED`**; all 30 metric rows independently reproduced with zero drift; Agent Runtime Architecture §37 verified **consumed, not duplicated**, with all eleven must-not items traced; **16/16 canonical Runtime operations covered** against an owner-derived list; **no false-success path found**; two citation-level regressions introduced by the remediation recorded as P3; all fifteen upstream P2 findings remain open and contained; no scaffold code, module, Python package, test, Runtime, framework adapter, package loader, or provider/model integration exists | `docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_002.md`, `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002.md` |
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002` | `COMPLETE` (local, not pushed) — **unverified pending Review 003**; remediated **all seven** Review 002 findings (P2 1 / P3 6) and advanced the specification to **version 1.2**. Resolved the contract-version inconsistency via a new authoritative §44.1 version history; converted twenty-six positional `row N` citations to semantic references (**correction, per Review 003 `NEW-P2-01`: this task's claim that *every* positional citation was converted is false — seven remain**, two introduced by this remediation); replaced §34 obligation 18's partial enumeration with the new **§31.1.1 Baseline Inert Invariant property register (32 properties)** asserted in full; made Scaffold Zero-Execution Evidence **affirmative-only** with a distinct non-affirmative `EVIDENCE_INCOMPLETE` outcome; gave cancellation a normative selection order with *implementation unavailable* as the inert default; and fully qualified the last owner §37 reference. **All twelve Review 001 closures preserved**, four strengthened. Documentation only: **no scaffold code, module, Python package, test, Runtime, framework adapter, package loader, or provider/model integration exists**; all fifteen upstream P2 findings remain open | `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` (v1.2), `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002.md` |
| `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003` | `COMPLETE` (local, not pushed) — **documentation gate `PASS_WITH_NON_BLOCKING_FINDINGS`** (P0 0 / P1 0 / **P2 2** / **P3 3**); spec **v1.2** accepted as a documentation contract only under nine constraints. **Implementation readiness reported separately as `NOT_READY_IMPLEMENTATION_AFFECTING_FINDINGS`** — the gate result does not authorize implementation. **All seven Review 002 findings independently disposed `CLOSED`**; **all twelve Review 001 closures independently confirmed preserved**, four strengthened; Agent Runtime Architecture §37 verified **sole owner, consumed unchanged** (all eleven must-not and ten may-implement items traced); **16/16 canonical Runtime operations covered** against an owner-derived list; **all 32 metric rows reproduced with zero drift**; **no false-success path found**; 1.1 → 1.2 independently adjudicated a valid compatible corrective increment; all fifteen upstream P2 findings remain open and contained. Five new findings, three introduced by Remediation 002: `NEW-P2-01` (seven surviving positional citations falsify §41 criterion 41; amendment-blocking), `NEW-P2-02` (§27.1 rule 2's evidence-completeness test indeterminate for an approved fixture at a §12 port; **implementation-blocking**), `NEW-P3-01`, `NEW-P3-02`, `NEW-P3-03`. No scaffold code, module, Python package, test, Runtime, framework adapter, package loader, or provider/model integration exists | `docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_003.md`, `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003.md` |
| Bounded remediation of Review 003 findings | `PLANNED` | Recommended next step: resolve `NEW-P2-02` (implementation-blocking), preferably carrying `NEW-P2-01`, `NEW-P3-01`, `NEW-P3-02`, and `NEW-P3-03`. **No identifier minted by Review 003.** Requires explicit Operator authorization. |
| Agent Runtime Scaffold implementation (inert code) | `BLOCKED` | Plain-name item carrying no task identifier — none minted by Review 002, Remediation 002, or Review 003. Requires **`NEW-P2-02` resolved**, **separate explicit Operator authorization**, and its own exact file allowlist. Review 003's passing documentation gate does **not** authorize it. No framework process, provider call, credential, model call, tool execution, or deployment permitted even once started. |
| Scaffold Implementation Review | `BLOCKED` | Requires the inert scaffold implementation to exist first. |
| First Agent Package | `BLOCKED` | Requires Scaffold Review to pass. |
| Cross-Agent Smoke (inert modes only) | `BLOCKED` | Separate clean-worktree task per `RUN_QUEUE.md`'s "Deferred Work". |
| Integration Review | `BLOCKED` | Final gate of this track. |

## Product Track Integration & Governance Tail

Local integration only. **Remote canonical `main` has not advanced**;
`clean-origin/main` remains `947f33d27d5546775186e96bdc61e30db78c0b3d`.
Integration branch `integration/mellycore-product-track-001` is at
`16da3ec2df9b52b203bb16468f90258f2d7f540c` — 44 commits, 0 merges, fast-forward
only, zero authored commits.

| Task ID | Status | Evidence |
|---|---|---|
| `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-001` | `COMPLETE` (local, not pushed) — plan created; authorized nothing | `docs/tasks/MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-001.md` |
| `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `FAIL_REMEDIATION_REQUIRED` (P0 0 / P1 1 / P2 1 / P3 0) | `docs/research/MELLYCORE_PRODUCT_TRACK_INTEGRATION_PLAN_REVIEW_001.md` |
| `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-001` | `COMPLETE` (local, not pushed) — both findings remediated; added the post-Unit-9 Governance Tail (not Unit 10); did not self-declare its own SHA | `docs/tasks/MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-INTEGRATION-EXECUTION-001` | `COMPLETE` (local, not pushed) — Units 1-8 integrated to `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5`; 40 commits via 8 fast-forwards; 0 merges | integration branch reflog; `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-COMPOSED-INTEGRATION-REVIEW-001` | `COMPLETE` (local, not pushed) — `ACCEPT` (P0 0 / P1 0 / P2 0 / P3 2). New findings `CI-P3-01`, `CI-P3-02`; scaffold blockers and `NOT_READY` verified preserved | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-UNIT-9-FRESHNESS-REVIEW-001` | `COMPLETE` (local, not pushed) — `PASS_WITH_NOTES` (P3 1: `U9-P3-01`); decision `UNIT_9_SAFE_TO_ADVANCE_TO_SEPARATE_INTEGRATION_TASK` | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-UNIT-9-INTEGRATION-001` | `COMPLETE` (local, not pushed) — Unit 9 integrated to `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`; 42 commits; ff-only | integration branch reflog |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-FRESHNESS-REVIEW-001` | `COMPLETE` (local, not pushed) — `FAIL_REMEDIATION_REQUIRED`; blocking finding `GT-P2-01` (pin record absent); non-blocking `GT-P2-02`, `GT-P3-01`, `GT-P3-02` | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-REVIEW-001` | `COMPLETE` (local, not pushed) — `ACCEPT_MELLYCORE_PRODUCT_TRACK_INTEGRATION_PLAN_REMEDIATION_001`; published `REVIEW_PINNED_GOVERNANCE_TAIL_SHA = 16da3ec2df9b52b203bb16468f90258f2d7f540c`; **`GT-P2-01` CLOSED**. Two non-blocking record-content P3 notes remain open | `docs/research/MELLYCORE_PRODUCT_TRACK_INTEGRATION_PLAN_REMEDIATION_REVIEW_001.md` (record commit `fefe65a38c8855271a1dab6dcb8c7178f3fb55b9`, blob `3676e4155df8e11bce7eb7a5266f0480431a383e`) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECORD-TIP-REVIEW-001` | `COMPLETE` (local, not pushed) — `PASS_WITH_NOTES`; both record-content gaps classified **P3 non-blocking**; `PREFERRED_INTEGRATION_TARGET = 16da3ec2df9b52b203bb16468f90258f2d7f540c` per Integration Plan §14 | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-INTEGRATION-001` | `COMPLETE` (local, not pushed) — Governance Tail integrated to `16da3ec2df9b52b203bb16468f90258f2d7f540c`; 44 commits; ff-only; record tip `fefe65a3…` deliberately **not** integrated | integration branch reflog |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001` | `COMPLETE` (local, not pushed) — durable evidence recorded and canonical state reconciled; imported the pin artifact byte-for-byte; **`GT-P2-02` and `GT-P3-01` CLOSED** | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REVIEW-001` | `ELIGIBLE` | Independent read-only review of the reconciliation commit. Not authorized, not started. |
| Publication (push / PR / PR review / canonical merge) | `BLOCKED` | Plain-name item; no identifier minted. Requires separate explicit Operator authorization per Integration Plan §12. |
| `MELLYCORE-ROADMAP-LOCK-001` | `BLOCKED` | Integration Plan §13 conditions 1-10 satisfied; condition 11 (separate explicit Operator authorization) outstanding. Not minted, drafted, or executed. |

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
