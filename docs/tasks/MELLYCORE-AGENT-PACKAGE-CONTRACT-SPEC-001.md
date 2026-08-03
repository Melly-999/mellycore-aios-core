# MellyCore Agent Package Contract Spec 001 — Task Report

## 1. Purpose

Create the canonical Agent Package Contract specification: the
provider-agnostic portable package boundary for agents executed, inspected,
validated, routed, and observed by MellyCore AIOS — what an Agent Package is,
what it may contain, how it declares capabilities and dependencies, how it
interacts with the Agent Runtime and Shared Context, and how MellyCore would
validate it without implementing runtime execution.

This is a documentation and specification task only. No Agent Package Store,
Package Registry, package validator, loader, Skill/Hook/Command/Plugin/MCP
registry, provider call, credential, secret, network operation, or
deployment was created.

The prior task in this session
(`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` documentation-synchronization
pass, commit `9575bce`) explicitly stated it was **not** the specification
itself. This task completes the actual specification work that entry
deferred.

## 2. Phase 0 — repository identity gate (read-only preflight)

| Check | Result |
| --- | --- |
| Repository root | `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` — matches expected |
| Branch (before creation) | `docs/mellycore-agent-runtime-architecture-spec-review-002` |
| HEAD (full) | `9575bce8ae4aff2517838143f767a3a3979c77f8` |
| HEAD (short) | `9575bce` — matches expected baseline exactly |
| Latest commit subject | `docs: record Developer Platform and Agent Package Ecosystem direction` |
| `git status --short` | empty — worktree clean, no unexpected staged or unstaged files |
| Remotes | `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git`; `origin` → `https://github.com/Melly-999/mellycore-aios.git` |
| Canonical documentation files | `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md` all present |
| Planned Agent Package spec file | Absent before this task (`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md`) |
| Planned Agent Package task file | Absent before this task (`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md`) |
| Target branch `docs/mellycore-agent-package-contract-spec-001` | Absent before this task (`git branch --list` returned nothing) |

Baseline matched exactly. **No fetch, pull, push, or network operation
occurred during this gate or at any point in this task.**

## 3. Branch creation

`git checkout -b docs/mellycore-agent-package-contract-spec-001` from the
verified local HEAD `9575bce`. The branch did not previously exist, so no
inspection-before-reuse was required. Worktree confirmed clean immediately
after creation; HEAD unchanged at `9575bce` (branch creation alone does not
move HEAD's commit).

## 4. Authoritative source discovery

Read-only inspection of every canonical owner document plausibly touching an
Agent Package concern, by exact section, not by filename assumption.

### 4.1 Owner map

| Concept | Canonical owner document | Relationship to Agent Package Contract |
| --- | --- | --- |
| Agent identity, run identity, package/runtime separation states (§9), required package metadata (§10), six-framework closed set (§11), authorization facts (§14), memory categories (§18) | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` | **Canonical, consumed verbatim.** Runtime §10 already reserved "Agent package relationship" as deferred to this task; this contract fills exactly that reservation without editing Runtime |
| Architecture-gate history and the `NEW-P3-01` eligibility finding that authorizes this task | `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md`, `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` | **Canonical precedent** for how a seam is resolved (existing owner wins unless it provably cannot represent the semantics); reused as method, not reopened |
| Provider identity, eight authorization facts, credential profiles, MCP server registration/suspension/deprecation/retirement (§24) | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | **Canonical, consumed unchanged.** MCP Declarations in the new contract reference §24 records by ID and revision; they never register or redefine one |
| Trust model, capability resolution (§12), policy-evaluation order (§17), approval binding (§18), MCP security contract (§21), error taxonomy (§25) | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | **Canonical, consumed unchanged.** Package capability declarations are requests only; the Gateway remains sole resolver and enforcer |
| Six orthogonal status dimensions (§8), entity catalogue including `Skill`/`Tool`/`Agent`/`Integration` (§7.2), Batch Run and Artifact Queues (§9.8), safety/approval model (§16), secrets boundary (§17), provenance (§18) | `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | **Canonical, consumed unchanged.** The new contract's package-lifecycle states and trust states project one-directionally onto the six dimensions, exactly as `run_state` already does (per the seam decision above); no seventh dimension is created; `Skill`/`Tool`/`Agent` entities remain that spec's frontend projection target, not redefined here |
| Unified Run Ledger record identity, cost/token semantics (§5) | `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | **Canonical, consumed unchanged.** Used only for a cost-attribution reference in observability (§20) |
| Fourteen dashboard-facing fixture entities | `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` | **Complementary**, not touched |
| Tenant isolation, credential model, external-content posture | `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | **Canonical, inherited unchanged** |
| Shared Context admission, provenance, sensitivity | `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`, `shared_context/context_provenance/**` | **Canonical, consumed unchanged** — same reuse the Agent Runtime spec itself already made; not reopened |
| Read-only repo digest tool concept | `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md` | **Unrelated** — a different, unimplemented tool concept; no overlap with package content |
| Cybersecurity / Marketing Provider Pack specs | `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`, `MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md` | **Terminology-adjacent, not owning.** "Provider Pack" (a provider-capability-mapping bundle) and "Agent Package" (a portable agent unit) share the English word "pack/package" only; recorded as a non-conflict in the new contract's terminology section |
| Safety boundaries, migration triggers, live sequencing, task identifiers | `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md` | **Canonical**, updated only as bounded state synchronization (§7 below), never re-authored |
| Existing spec-writing convention (Title/Status/Metrics header, Authority/precedence chain, normative MUST/MUST NOT language, document-metrics self-count table) | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` §1–§4 | **Convention reused**, not a new house style invented |
| Existing task-report convention (owner map, ownership-decisions table, files-changed list, validation section, explicit non-authorizations, no-push status) | `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md` | **Convention reused** for this report |

### 4.2 Conflict check

**No two canonical owner documents own an Agent Package concern
incompatibly.** Every concern above resolved to exactly one owner. The two
apparent overlaps investigated in depth — (a) Control Plane's `Skill`/`Tool`
entity catalogue versus this contract's Skill/Command/Hook/Plugin/MCP asset
declarations, and (b) "Package Registry" (this task's assigned term)
versus the Agent Runtime spec's existing "Agent Package Store" placeholder —
are **not conflicts**: (a) resolves because Control Plane §7.3 already states
its entity model "is conceptual and frontend-facing; it is not a production
database schema," so it is a downstream projection target, never a
competing package-declaration format; (b) resolves by terminology
reconciliation (new contract §4), assigning "Package Registry" the
discovery/index/trust-state responsibility and leaving "Agent Package Store"
(Runtime's existing, unmodified term) the artifact-storage responsibility —
one future system, two named responsibilities, no renaming. **No stop
condition was triggered.**

## 5. Ownership decisions

| Concern | Canonical owner | This contract's role |
| --- | --- | --- |
| Package format, identity, boundary, declarations | **This Agent Package Contract** | Owner |
| Agent/run identity, package/runtime separation states, execution envelope | Agent Runtime spec | Consumes verbatim |
| Package artifact storage | Agent Package Store (future) | Defines required contents, not storage mechanism |
| Package discovery/index/trust lookup | Package Registry (future) | Defines what is indexed, not the registry |
| Package/agent installation and registration | Agent Registry (future) | Not this contract's concern |
| Package verification ("Package verified" state) | **This Agent Package Contract** | Owner of the validation-layer vocabulary; validator engineering is a named follow-up |
| Provider facts, credential classes, MCP registration | Provider Registry contract | Consumed unchanged; MCP Declarations reference only |
| Capability resolution, policy order, approval binding, MCP security contract | Integration Gateway contract | Consumed unchanged |
| Six status dimensions, entity catalogue, Batch queue surface | Control Plane spec | Consumed unchanged; declarations are inputs to it |
| Safety and approval layers | Safety Contract, Control Plane §16, Gateway §18 | Consumed unchanged |
| Skill/Hook/Command/Plugin/MCP Registries, Package Validation, Package Lifecycle, Package Distribution, Package Repository | Twelve named follow-up contracts | Bounded here; not specified in full |
| Batch Orchestration | Future, separate task | Package-side eligibility declarations only |

## 6. Specification created

`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` — 29 sections.

1. Title and status (status meaning, current implementation state,
   migration-trigger relationship, document metrics)
2. Purpose and scope
3. Authority and source contracts
4. Terminology (21 entries)
5. Architectural ownership (13 rows)
6. Package boundary (7 prohibited content categories)
7. Package identity (12 fields, 18 Runtime fields reused unchanged)
8. Package layout model (9 asset categories, illustrative tree)
9. Manifest relationship (6 boundary rows, each deferring its full contract)
10. Capability declarations (5-state separation: declared → runtime-supported
    → policy-allowed → operator-approved → active)
11. Permission and approval model (12 categories, default-deny)
12. Dependency model
13. Provider-agnostic compatibility (6-framework projection, no framework
    named canonical owner)
14. Skills, commands, hooks, plugins, and MCP (5 asset types, each with
    ownership boundary, validation expectation, activation boundary,
    security implication, and future registry)
15. Shared Context interaction (8 rules; existing Context Gate unweakened)
16. Runtime interaction (9 stages: discovery → validation → compatibility
    projection → policy evaluation → instantiation eligibility → activation
    gating → lifecycle projection → observability projection →
    termination/suspension projection)
17. Package lifecycle (11 states; full transition-rule contract deferred)
18. Validation model (9 layers; validation success ≠ execution authorization)
19. Trust and provenance (7 categories; no cryptographic signing claimed)
20. Observability (11 projections; information architecture only)
21. Error and rejection taxonomy (15 stable classes)
22. Versioning and compatibility
23. Batch Orchestration compatibility (7 package-side declarations; no
    implicit PR/push/merge/deploy permission)
24. Security considerations (12 threats, each with a mitigation posture)
25. Non-goals (12 items)
26. Follow-up contracts (12 named)
27. Acceptance criteria (14 items)
28. References
29. Amendment and supersession

### 6.1 Key architectural decisions

- **Reuse over invention.** Every identifier, field, state, and closed
  vocabulary the Agent Runtime spec already fixed (`agent_definition_id`,
  `package_revision_id`, `framework_type`, the eighteen §10.1 fields, the
  nine §9 separation states) is reused verbatim; this contract adds only the
  declarations Runtime §10 explicitly left for it.
- **Five-state capability separation** (declared / runtime-supported /
  policy-allowed / operator-approved / active) mirrors Runtime §9's "no state
  implies the next" discipline at the capability level, so a package can
  never self-grant by declaration alone.
- **Eleven-state package lifecycle**, deliberately distinct in name and count
  from Runtime's seventeen `run_state` values and from Control Plane's six
  status dimensions, to avoid the exact seam collision Review 001 found and
  Remediation 001 fixed for `run_state` versus `lifecycle_status`. Package
  states may project one-directionally onto the canonical dimensions; they
  create no seventh dimension.
- **MCP Declarations are references, never registrations.** Provider
  Registry §24 remains the sole owner of MCP server records; a package may
  only cite an existing `mcp_server_id` and `tool_contract_revision`.
- **No signing claimed.** §19 defines a trust-state vocabulary without
  asserting any cryptographic mechanism exists; every package defaults to
  `unsigned_or_unverified` in the cryptographic sense.
- **Twelve items deliberately deferred** (§26) rather than specified in
  full, per the task brief's explicit instruction not to fully specify
  contracts belonging to planned follow-up documents.

## 7. State synchronization

Bounded synchronization only, recording that specification work is complete
while implementation remains absent:

- `shared_context/PROJECT_STATE.md` — new section recording the
  specification's completion, unverified status, and next task.
- `shared_context/ROADMAP.md` — Agent Runtime Product Track item 5 updated
  from "in progress" to "specification drafted, pending review"; the
  Developer Platform section's follow-up list cross-referenced to §26 of the
  new spec.
- `shared_context/RUN_QUEUE.md` — same item 5 update; next task pointer set
  to `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001`.
- `shared_context/AGENT_HANDOFF.md` — new Latest Update entry; prior entry
  renamed Previous Update.
- `shared_context/PROJECT_HISTORY.md` — one new ledger entry recording the
  spec's creation.
- `shared_context/TASK_INDEX.md` — `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001`
  row status updated to `COMPLETE` (specification only); new row added for
  `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` as `ELIGIBLE`.

None of the following was marked implemented, and this task asserts none of
it: package runtime, package loading, package registry, package
installation, package execution, package marketplace, batch execution.

## 8. Files changed

Exactly eight:

1. `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (new)
2. `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` (new)
3. `shared_context/PROJECT_STATE.md` (modified)
4. `shared_context/ROADMAP.md` (modified)
5. `shared_context/RUN_QUEUE.md` (modified)
6. `shared_context/AGENT_HANDOFF.md` (modified)
7. `shared_context/PROJECT_HISTORY.md` (modified)
8. `shared_context/TASK_INDEX.md` (modified)

No source file, test file, workflow YAML, `.env` file, or unrelated
documentation file was changed.

## 9. Validation

- `git diff --check` — recorded in the final execution report.
- `py -3.9 scripts/validate_project_state.py` — recorded in the final
  execution report.
- Duplicate task-ID check: `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001`
  appears consistently across all eight changed files with one meaning; no
  second, differently-scoped task reused the ID.
- Broken local cross-reference check: every `[[...]]` reference in the new
  specification resolves to an existing repository file (including the two
  corrected to their actual `../research/` path).
- Required-section check: all 29 sections present; all items the task brief
  required (25 numbered topics plus title/status, references, and
  amendment/supersession) are addressed.
- Prohibited-term / overclaim review: every occurrence of `implemented`,
  `installed`, `supported`, `enabled`, `available`, `executable`, and `live`
  in the new specification was reviewed in context; each is either a negated
  claim (`NOT_IMPLEMENTED`, `NONE_EXIST`), a reused field/state name from an
  already-accepted spec (`supported_environments`, `runtime-enabled`), or a
  hypothetical description inside a document-wide non-implementation frame.
  One instance ("an available Runtime Adapter") was tightened to "an
  eligible Runtime Adapter" to remove any reading of the Control Plane
  `availability_status:available` enum value. Zero occurrences of
  `production-ready`, `operational`, or `deployed`.
- Secret and environment-file scope check: no `.env` file changed; no key or
  token material introduced; no provider configuration added. Confirmed by
  direct review of every changed file's content.
- Changed-file allowlist check: the eight files in §8 are exactly the
  changed-file list `git status --short` reports; none falls outside the
  authorized documentation scope.
- Document self-consistency check: every row of the new specification's
  §1.4 metrics table was recomputed against its cited section by direct
  count (not carried forward from drafting intent); two counting errors
  found during this pass (terminology 22→21, ownership rows 12→13, identity
  fields 11→12, follow-up contracts 11→12, and one now-removed
  self-contradictory footnote) were corrected before commit.
- `pytest`: `NOT_RUN` — no source or test file changed; the existing suite
  produces no evidence about a documentation-only change and is not claimed
  passing. Black, flake8, and mypy: not run, not claimed passing.

## 10. Known limitations

1. This specification is **unverified**. No independent architecture,
   security, or consistency review has run against it.
2. The six-framework compatibility projection (§13) restates, and does not
   re-verify, the Agent Runtime spec's own already-recorded caveat that no
   framework was installed, imported, connected, or executed.
3. Twelve follow-up contracts (§26) remain unspecified beyond the boundary
   this document fixes; none is authorized to begin its own specification
   work by this task.
4. No cryptographic signing mechanism is specified; §19's trust-state
   vocabulary is deliberately signing-agnostic pending a future Package
   Distribution contract.
5. The illustrative package layout tree (§8.2) is non-binding; no on-disk
   format is implemented or required by this document.

## 11. Exact next task

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001` — an independent,
read-only architecture, security, and consistency review of this
specification, in the same sequence Review 001/Remediation 001/Review 002
already applied to the Agent Runtime architecture. Not started, not
authorized by this task.

## 12. Explicit non-authorizations

This task authorizes none of: Agent Package Store implementation; Package
Registry implementation; Package Validator implementation; package loader,
sandbox, or import-path implementation; Skill/Hook/Command/Plugin/MCP
Registry implementation; any package, agent, skill, command, hook, plugin,
or MCP execution; any cryptographic signing infrastructure; any provider
connection, credential configuration, or model-provider call; Batch
Orchestration implementation; any push, pull request, merge, or remote
branch; or any MellyTrade interaction.

The Agent Runtime architecture gate (Review 002,
`PASS_WITH_NON_BLOCKING_FINDINGS`) is not reopened. Framework Bridge
Contract, Shared Context Bridge, Agent Runtime Scaffold, first Agent
Package, Cross-Agent Smoke, and Integration Review remain blocked, as does
Agent Runtime implementation. Live provider work remains deferred and
blocked. Migration triggers #1, #4, #5, #6, and #7 remain uncrossed. The
global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted.

## 13. No-push status

One local documentation commit was created on
`docs/mellycore-agent-package-contract-spec-001`. It was **not** pushed. No
pull request, merge, remote branch, amend, reset, restore, stash, clean,
rebase, squash, cherry-pick, force operation, or deployment occurred.
Commit SHA is reported in the final execution report.
