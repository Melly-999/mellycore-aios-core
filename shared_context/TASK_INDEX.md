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
| `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` | `IN_PROGRESS` | Repository-wide priority umbrella; independently governed and not reordered by PR #36. This pointer is not a live-execution authorization or a claim that a provider action is executable. Its internal current gate must be verified from its separate lineage and newest task/Git/GitHub evidence. |

## Cockpit Production Hotfix Closure

| Task ID | Status | Notes |
|---|---|---|
| `MELLYCORE-COCKPIT-FINAL-ACCEPTANCE-CLAUDE-REVIEW-001` | `COMPLETE` — `PASS_WITH_LIMITATIONS` | Historical review outcome preserved. Applicable F1 skip-link and F2 hero-CTA destination-focus limitations are closed by the Production-verified hotfix; no full WCAG claim. |
| `MELLYCORE-COCKPIT-SKIP-CTA-FOCUS-HOTFIX-CANONICAL-RECONCILE-001` | `COMPLETE` — `PASS` | Reconciled the two-file HTML/CSS focus hotfix onto canonical base `ed6de2d…`; resulting release commit `a6bb3f37679059a742e0f9d603f9f66c6ac5f5a1`. |
| `MELLYCORE-COCKPIT-SKIP-CTA-FOCUS-HOTFIX-CANONICAL-ACCEPTANCE-001` | `COMPLETE` — `PASS / ACCEPT_FOR_MERGE_CONSIDERATION` | Independent five-width acceptance: skip 25/25, hero CTA 25/25, command anchors 175/175; 696 tests passed. |
| `MELLYCORE-COCKPIT-SKIP-CTA-FOCUS-HOTFIX-MAIN-MERGE-002` | `COMPLETE` — `MERGED_AND_PUSHED` | Fast-forwarded exact base `ed6de2d…` to `a6bb3f3…` on canonical `clean-origin/main`; no force push or merge commit. |
| `MELLYCORE-COCKPIT-SKIP-CTA-FOCUS-HOTFIX-PRODUCTION-VERIFY-001` | `COMPLETE` — `PRODUCTION_VERIFIED` | GitHub Production deployment `5926788051` succeeded for exact SHA `a6bb3f3…`; public root and four CSS assets returned 200 and matched Git blobs; Chrome 305/305. |
| `MELLYCORE-COCKPIT-POST-PUBLICATION-STATE-SYNC-001B` | `COMPLETE` (local-only) — `SUPERSEDED` | Commit `52966763f915de6fe8a41de1abe5c02fd585a1de` is not in canonical lineage; its Claude-review `PENDING / NOT RECORDED` statement is stale. |
| `MELLYCORE-COCKPIT-POST-HOTFIX-PRODUCTION-STATE-SYNC-001` | `COMPLETE` (local docs-only commit; not pushed) | Supersedes the stale sync and records exact Production SHA, deployment, F1/F2 closure, browser/HTTP/blob evidence, static-product truth, and the bounded next-lane recommendation. No site/runtime/deployment behavior. |

Next recommendation only: plain-name Freelance/Profile ROI before M3;
alternative M3 Knowledge & Operations Graph specification. Neither name mints
a task identifier or authorizes work. This section does not reorder the Global
Pointer or another independent lane.

## Cinematic AIOS Roadmap — M0-M5 (MELLYCORE-TASK-INDEX-001)

Materializes the product-vision lock (`MELLYCORE-ROADMAP-LOCK-001B`, pinned
commit `8f72b66dc96031d046e4e88e4aaebdd35d756fb9`) into an executable
milestone sequence. This section is a **sequencing overlay**: it mints new
task IDs only where the roadmap names a concept with no existing identifier,
and otherwise points at the tracks already indexed above/below. It does not
reorder the Global Pointer row, the Agent Runtime Product Track, or the
Enterprise Provider Integration track — all three remain independently
governed. Full milestone narrative: `shared_context/RUN_QUEUE.md`'s
"Cinematic AIOS Roadmap Materialization" section.

| Task ID | Milestone | Status | Notes |
|---|---|---|---|
| `MELLYCORE-ROADMAP-LOCK-001B` | M0 | `COMPLETE` | Locked cinematic AIOS product vision; commit `8f72b66dc9…`. Not reopened. |
| `MELLYCORE-TASK-INDEX-001` | M1 | `COMPLETE` (included in pushed PR #36 lineage) | This materialization. Evidence: this file, `RUN_QUEUE.md`, `docs/tasks/MELLYCORE-TASK-INDEX-001.md`. |
| `MELLYCORE-CLAUDE-DESIGN-HANDOFF-REVIEW-001` | M1 | `PLANNED` | Reviews/canonicalizes the externally generated Claude Design System handoff (tokens, components, site/cockpit UI kits, `SKILL.md`) currently observed as untracked/foreign state (`.agents/`, `.claude/skills/`, `skills-lock.json`) on `design/mellycore-claude-design-sync-001`. Design input only until reviewed; not canonical, not implemented. Task ID newly minted by this materialization; no conflicting identifier found. |
| `MELLYCORE-HERO-DIRECTION-DECISION-001` | M1 | `PLANNED`, `BLOCKED` on `MELLYCORE-CLAUDE-DESIGN-HANDOFF-REVIEW-001` | Decision gate comparing hero directions A (Source Arena-led), B (Orbital Command Center-led), C (Hybrid), D (Instrument/Calibration Plate — existing Claude Design candidate). Does not select a winner by naming it here. Task ID newly minted. |
| `MELLYCORE-DESIGN-SYSTEM-CINEMATIC-AMENDMENT-001` | M1 | `PLANNED`, `BLOCKED` on `MELLYCORE-HERO-DIRECTION-DECISION-001` | Amends `shared_context/DESIGN_SYSTEM.md` (protected owner; not touched by this task) with the selected hero direction and any accepted Claude Design tokens/components. Task ID newly minted. |
| `MELLYCORE-CINEMATIC-HOMEPAGE-SPEC-RECONCILIATION-001` | M1 | `COMPLETE` (included in pushed PR #36 lineage) | Reconciled the existing homepage specification against `MELLYCORE-ROADMAP-LOCK-001B`; evidence: `docs/tasks/MELLYCORE-CINEMATIC-HOMEPAGE-SPEC-RECONCILIATION-001.md`, commit `053850f2946f6a18bc4f3eb733d4b396479ed5d8`. |
| `MELLYCORE-DOCS-INTEGRATION-REVIEW-001` | M1 | `PLANNED`/`ELIGIBLE` | Named as the exact next task by the Source Arena Hybrid Renderer ADR closeout (`RUN_QUEUE.md` item 2u) but never independently executed as its own task record (absent from `docs/tasks/` and this index prior to this row). Docs/spec-scope review across the Cinematic AIOS lock, the Claude Design handoff review outcome, and the reconciled homepage spec. Existing identifier reused, not newly minted. |
| `MELLYCORE-M2-FOUNDATION-FIRST-VIEWPORT-001` | M2 | `COMPLETE` (included in pushed PR #36 lineage) | Foundation/first viewport implementation; commit `5685d4c30701126adcf73cd92da5b6305d39dde4`. |
| `MELLYCORE-M2-TECHNICAL-PRODUCT-PROOF-001` | M2 | `COMPLETE` (included in pushed PR #36 lineage) | Technical product proof implementation; commit `9f022cecaf6f12825e42208515c0fd8bdbe6a5a1`. |
| `MELLYCORE-M2-INSTRUMENT-LANGUAGE-POLISH-001` | M2 | `COMPLETE` (included in pushed PR #36 lineage) | Instrument-language implementation/polish; commit `fe63741defac857311dc5d9a521ebf0c76771408`. |
| `MELLYCORE-M2-SIGNATURE-SURFACES-POLISH-001` | M2 | `COMPLETE` (included in pushed PR #36 lineage) | Signature-surface polish; commit `62d3531fcad885ce3f7c25f18ce1ecc6ef0c2387`. |
| `MELLYCORE-M2-ECOSYSTEM-CONVERSION-001` | M2 | `COMPLETE` (included in pushed PR #36 lineage) | Materialized the truthful static ecosystem for exactly ten workspaces; commit `b8b5c2fe3706d923c03660262be63afaacbcd71c`. No workspace backend or activation. |
| `MELLYCORE-M2-GLOBAL-RHYTHM-POLISH-001` | M2 | `COMPLETE` (included in pushed PR #36 lineage) — `PASS_WITH_LIMITATIONS` | Final visual rhythm/polish implementation; commit `b6e10a935f358582a02e5f43e19b0c9ec3f37ab5`. Prior review found no further visual polish required before Acceptance; disclosed non-blocking limitations remain recorded in `AGENT_HANDOFF.md`. |
| `MELLYCORE-M2-SHOWCASE-ACCEPTANCE-001` | M2 | `COMPLETE` (final independent rerun `MELLYCORE-M2-SHOWCASE-ACCEPTANCE-003`; included in PR #36 lineage) — `ACCEPTED_WITH_NON_BLOCKING_LIMITATIONS` | Formal acceptance chain completed at candidate `8264d29712396fa71101aedb578f5d5a13f33d8d`; M2 is complete and `SHOWCASE_READY = YES`. Accepted release SHA `a71846f1800b921b509995ac2b65b317fcf290bf` was incorporated through PR #36, which subsequently merged into canonical `main`. This acceptance record does not authorize provider/runtime activation. |
| `MELLYCORE-M2-PUBLIC-SHOWCASE-RELEASE-001` | M2 | `COMPLETE` | Originally pushed the accepted release and opened PR #36. The later verified lifecycle supersedes that creation-time boundary: remediated PR head `d0c05cffd4791b6d896fbb7851ccbdf6323c3284` merged as `b7ebd116f9cdfcd0d34e1b93cef58660a1ac90d9`, and GitHub deployment `5847256173` for that exact merge commit succeeded in `Production`. |
| `MELLYCORE-PR36-COMPOSED-INTEGRATION-REVIEW-001` | M2 release gate | `COMPLETE` — `NEEDS_REMEDIATION` (historical gate) | Full 63-commit / 110-file review found `PR36-INT-001`, P1 living canonical-state truth drift. Its pre-merge finding led to the bounded remediation below; it is not a current gate after PR #36's merge. |
| `MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-001` | M2 release gate | `COMPLETE` | Governance-only remediation commit `d0c05cffd4791b6d896fbb7851ccbdf6323c3284` became PR #36's head and was incorporated into merge commit `b7ebd116f9cdfcd0d34e1b93cef58660a1ac90d9`. Evidence: `docs/tasks/MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-001.md`. |
| `MELLYCORE-PR36-COMPOSED-INTEGRATION-REMEDIATION-REVIEW-001` | M2 release gate | `ELIGIBLE` — historical pre-merge entry, superseded by merge | Previously named as the next gate after the local remediation. PR #36 has since merged and its exact merge commit deployed successfully to `Production`; this entry is not a current executable task and no review completion is inferred. |
| M3 Flagship Command Center product-surface tasks | M3 | `PLANNED` | Sixteen product/UI projection surfaces (Mission Control/Overview, Knowledge & Operations Graph, Context Management, Runtime Constellation, Agents, Runs, Models, Providers, Model Routing, Tools/MCP, Shared Context, Memory, Artifacts, Cost/Usage, Observability, Governance/Approvals, Hardware/Local AI). No task IDs minted; each requires its own spec/review pass after M2. |
| M4 static-showcase completion for all ten workspaces | M4 | `PLANNED` | See "Ten AI Workspaces — Static Showcase Plan" below. No task IDs minted. |
| M5 public-production gates | M5 | `PLANNED` | Responsive, mobile, accessibility, reduced-motion, truthfulness, performance, security/privacy, production-build-readiness, merge-authorization, and deployment-authorization gates. No task IDs minted; none authorizes merge or deployment by naming it here. |

### Ten AI Workspaces — Static Showcase Plan

Exactly ten workspaces (`WORKSPACE_COUNT = 10`, locked by
`MELLYCORE-ROADMAP-LOCK-001B`); no eleventh. Each has a truthful static M2
representation; the deeper M4 workspace surface remains `PLANNED`. No row
claims a workspace backend, connection, runtime activation, or authorization.

| Workspace | M2 representation / M4 stage | Activation wave (`RUN_QUEUE.md`) | Major dependencies |
|---|---|---|---|
| Coding / Runtime Studio | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 1 | Agent Runtime Product Track (spec-only; scaffold implementation still `BLOCKED`) |
| Deep Research | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 1 | Model Router direction (`PROJECT_STATE.md` model-economics section) |
| Compare Arena | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 1 | OpenRouter Observatory Level 1 (existing, canonical) |
| Multi-Agent Crew | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 1 | Agent Runtime handoff model (spec-only) |
| Email AI | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 2 | Marketing/Enterprise Provider Pack specs (docs-only, not connected) |
| Video Intelligence | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 2 | Deeper workspace surface remains planned |
| Voice | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 2 | Deeper workspace surface remains planned |
| Image Studio | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 3 | Deeper workspace surface remains planned |
| Model Downloader | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 3 | Hardware Capability Service (future research direction, not implemented) |
| Ollama Manager | M2 static representation `COMPLETE`; M4 `PLANNED` | Wave 3 | Hardware Capability Service (future research direction, not implemented) |

Activation priority (Wave 1/2/3) governs the order workspaces receive deeper
static product surfaces after M2; it is independent of, and does not imply,
implementation order. `Local AI Hub` is a presentation grouping over Model
Downloader + Ollama Manager, not an eleventh workspace.

### Parallel Lanes (safe concurrency)

These lanes touch disjoint canonical owners and may proceed simultaneously;
none blocks another unless stated:

- **GOVERNANCE** — `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-REVIEW-003` (Agent Runtime Product Track, below) and the OpenAI Batch reconciliation chain (`RUN_QUEUE.md` "Current" section). Owns `docs/decisions/`, `docs/research/`, and the reconciliation-lineage branches only.
- **DESIGN** — `MELLYCORE-CLAUDE-DESIGN-HANDOFF-REVIEW-001` → `MELLYCORE-HERO-DIRECTION-DECISION-001` → `MELLYCORE-DESIGN-SYSTEM-CINEMATIC-AMENDMENT-001`. Owns `shared_context/DESIGN_SYSTEM.md` (future amendment only) and the design-handoff worktree/branch it reviews — not this task's worktree or the primary checkout.
- **IMPLEMENTATION / M2 RELEASE** — M2 implementation and Showcase Acceptance are complete. PR #36 merged into canonical `main` as `b7ebd116f9cdfcd0d34e1b93cef58660a1ac90d9`, and GitHub deployment `5847256173` for that exact merge commit succeeded in `Production`. The former PR #36 remediation-review pointer is historical, not a current executable task. The current branch gate is independent exact-head review of PR #38 after its bounded lifecycle-state remediation; PR #38 merge remains separately authorized.
- **PLATFORM / RESEARCH** — Enterprise Provider Integration parallel track (below) and 3D Scene Foundation PR #28 (blocked on physical Gate B). Owns their respective spec/decision documents and paused PR only; neither is required for M2.

GOVERNANCE, DESIGN, and PLATFORM/RESEARCH may run concurrently today.
IMPLEMENTATION is gated on one DESIGN-track output (the reconciled homepage
spec) but not on GOVERNANCE or PLATFORM/RESEARCH completing first.

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

Local only. Remote canonical `main` (`clean-origin/main`) was
`947f33d27d5546775186e96bdc61e30db78c0b3d` at authoring time and advances only
under its own authorization.

**Verified Governance-Tail integration checkpoint:**
`16da3ec2df9b52b203bb16468f90258f2d7f540c` — 44 commits from baseline, 0 merges,
fast-forward only, zero authored commits. That is a permanent property of the
checkpoint commit; **resolve the live tip of
`integration/mellycore-product-track-001` from Git** when current tip identity
matters. Documentation-only descendants exist on separate local branches.
Through the independently reviewed remediation-002 tip
`6ccbbed5280997bc9e1141015eb9559551976529` the lineage is
`16da3ec2…` → `493dc86ba1f56d854876e7d2a741253d52283bef` →
`ea0d20ee7533b99360c76d1c5cee609dd2ce2aa1` → `6ccbbed…` — **three descendants
after the checkpoint, 47 cumulative commits from baseline, 0 merges**, immutable
properties of `6ccbbed…`. A further remediation descendant exists beyond that
reviewed tip; its SHA and resulting graph counts are resolved from Git by the
next independent review and are deliberately not predicted here. No
reconciliation-lineage descendant was integrated at authoring time.

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
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `FAIL_REMEDIATION_REQUIRED` (P0 0 / P1 0 / **P2 1 blocking** / P3 2); `PREFERRED_RECONCILIATION_INTEGRATION_TARGET = AMENDMENT_REQUIRED`; established `PIN_EQUALITY_SCOPE = GOVERNANCE_TAIL_ADMISSION_ONLY`. Blocking `RC-P2-01` (integrating the candidate would falsify five canonical current-state assertions); non-blocking `RC-P3-01`, `RC-P3-02`. Confirmed `GT-P2-02` and `GT-P3-01` genuinely closed and all other findings preserved | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` (§ Subsequent independent review / remediation) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-001` | `COMPLETE` (local, not pushed) — replaced live-tip assertions with integration-invariant checkpoint semantics across the five canonical documents; corrected this index's stale review row; imported pin artifact left byte-identical. `RC-P2-01` and `RC-P3-01` `CLOSED_PENDING_INDEPENDENT_REVIEW`; commit SHA deliberately not self-declared | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` (§ Subsequent independent review / remediation) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-REVIEW-001` | `COMPLETE` (local, not pushed) — gate `FAIL_REMEDIATION_REQUIRED_MELLYCORE_PRODUCT_TRACK_GOVERNANCE_TAIL_RECONCILIATION_REMEDIATION_REVIEW_001`; blocking `RR-P2-01` (two residual State-B-stale assertions: `PROJECT_STATE.md` "current HEAD" label, `ROADMAP.md` unconditional "Neither is integrated"); `RC-P3-01` `CLOSED`, `RC-P3-02` `OPEN_NONBLOCKING` | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` (§16) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-002` | `COMPLETE` (local, not pushed) — fixed both `RR-P2-01` assertions with integration-invariant/time-anchored wording; `RR-P2-01` = `REMEDIATED_PENDING_INDEPENDENT_REVIEW`; commit SHA deliberately not self-declared | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` (§16) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-REVIEW-002` | `COMPLETE` (local, not pushed) — gate `FAIL_REMEDIATION_REQUIRED_MELLYCORE_PRODUCT_TRACK_GOVERNANCE_TAIL_RECONCILIATION_REMEDIATION_REVIEW_002` (P0 0 / P1 0 / **P2 1 blocking** / P3 3); `PREFERRED_RECONCILIATION_INTEGRATION_TARGET = AMENDMENT_REQUIRED`. Resolved the remediation-002 tip as `6ccbbed5280997bc9e1141015eb9559551976529` and verified 3 descendants / 47 cumulative / 0 merges. Blocking `RRR-P2-01` (canonical docs still modelled two descendants / 46 commits); non-blocking `RRR-P3-01`, `RRR-P3-02`, `RRR-P3-03`. Confirmed both `RR-P2-01` named fixes genuinely applied but disposed `RR-P2-01` `PARTIALLY_CLOSED`; `RC-P2-01` `CLOSED_BY_REMEDIATION_LINEAGE`, `RC-P3-01` `CLOSED` | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` (§17) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-003` | `COMPLETE` (local, not pushed) — corrected lineage cardinality to three reviewed descendants, replaced fixed future-total projections with commit-relative counts plus a Git-resolution rule, repaired `RRR-P3-01` and `RRR-P3-02`; `RRR-P2-01` = `REMEDIATED_PENDING_INDEPENDENT_REVIEW`; commit SHA deliberately not self-declared | `docs/tasks/MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-DURABLE-EVIDENCE-RECONCILIATION-001.md` (§17) |
| `MELLYCORE-PRODUCT-TRACK-GOVERNANCE-TAIL-RECONCILIATION-REMEDIATION-REVIEW-003` | `ELIGIBLE` | Independent read-only review of the remediation-003 tip; must resolve its exact SHA and mechanically derive descendant, cumulative, and merge counts from Git. Per `RRR-P3-03` it must run in a fresh session or by a different agent. Not authorized, not started. |
| Reconciliation-lineage integration (exact reviewed tip, ff-only) | `BLOCKED` | Plain-name item; no identifier minted. Requires a passing remediation review and separate explicit Operator authorization naming the exact SHA. |
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
