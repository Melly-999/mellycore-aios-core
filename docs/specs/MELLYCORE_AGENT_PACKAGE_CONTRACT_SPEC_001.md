# MellyCore Agent Package Contract Spec

**Task ID:** MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001
**Contract ID:** MELLYCORE_AGENT_PACKAGE_CONTRACT_001
**Version:** 1.1 — remediates the one P1, three P2, and three P3 findings of
`[[../research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001]]` under
`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001`.
**Verification status:** Remediation claims in this version are **unverified**
pending `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002`. Version 1.1 does
not re-open or re-claim a passed gate; the gate remains failed
(`FAIL_REMEDIATION_REQUIRED`) until that independent review passes, in the
same sequence used for `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`
(spec → review → remediation → review).
**Status:** Drafted, specification-level only, pending independent Review 002.
This document is **not accepted**.
**This status does not authorize:** Agent Package Store implementation,
Agent Registry implementation, Package Registry implementation, package
loader implementation, package validator implementation, package
installation, package execution of any kind, any command, hook, plugin, or
MCP execution, batch execution, frontend or dashboard implementation, backend
implementation, provider calls, live model integration, network operations,
credential configuration, or deployment. It fixes the contract a later,
separately authorized implementation must satisfy.
**Scope:** Defines the Agent Package — the canonical, provider-agnostic,
portable unit through which MellyCore AIOS describes an agent and its
declarative assets — covering identity, boundary, layout, manifest
relationships, capability and permission declarations, dependencies,
framework-compatibility projection, Skill/Command/Hook/Plugin/MCP asset
boundaries, Shared Context interaction, Agent Runtime interaction, lifecycle,
validation, trust and provenance, observability, error taxonomy, versioning,
Batch Orchestration compatibility, security considerations, and follow-up
contracts.

---

## 1. Title and status

### 1.1 Status meaning (normative)

This is a **drafted, not-yet-accepted specification**, in the same procedural
class `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` occupied before its
own Review 001. Drafting means only that the boundaries, identities,
declarations, and fail-closed rules below are a **proposed** canonical target
for a future Agent Package Store, Package Registry, and package validator to
satisfy. Drafting does **not** mean any of: an implemented package format
parser; an implemented validator; an implemented registry; an installed
package; an executed agent; a loaded skill, hook, command, plugin, or MCP
declaration; or a deployment.

This specification **does not reorder, reprioritize, or reinterpret** the
global higher-priority task pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`, and it **does not
reopen** the Agent Runtime architecture gate
(`[[../research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002]]`,
`PASS_WITH_NON_BLOCKING_FINDINGS`). It consumes that gate's `NEW-P3-01`
eligibility finding, which named exactly this task as eligible for Operator
authorization; Operator direction was given in chat session 2026-08-03 (see
`shared_context/AGENT_HANDOFF.md`'s Latest Update at the time of this task).

### 1.2 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Agent Package Store | `NOT_IMPLEMENTED` — no storage, indexing, or artifact-hosting code exists |
| Package Registry | `NOT_IMPLEMENTED` — no discovery, index, or trust-state service exists |
| Package Validator | `NOT_IMPLEMENTED` — no structural, schema, dependency, capability, compatibility, safety, provenance, or policy validation code exists |
| Package loader | `NOT_IMPLEMENTED` and explicitly out of scope (§25) |
| Agent Packages | `NONE_EXIST` — no package, manifest, or artifact exists anywhere in this repository |
| Skill, Hook, Command, Plugin, MCP Registries | `NOT_IMPLEMENTED` — named only as follow-up contracts (§26) |
| Package installations | `NONE_EXIST` |
| Packages executed | **Zero.** No package has ever been discovered, validated, installed, instantiated, or executed |
| Cryptographic package signing | `NOT_SPECIFIED`, `NOT_IMPLEMENTED` — §19 does not claim a signing mechanism exists |
| Agent Runtime | Unchanged by this task. Remains `PASS_WITH_NON_BLOCKING_FINDINGS` per Review 002; still `NOT_IMPLEMENTED` |
| Evidence class for every flow below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by this documentation task. A validator that did
not run records `NOT_RUN`, never a defaulted pass.

### 1.3 Relationship to migration triggers

This specification implements nothing, so it crosses no migration trigger in
`shared_context/PROJECT_STATE.md`'s Model A contract. Trigger **#6, "first
execution-capable agent,"** remains uncrossed: nothing here makes any agent,
package, or bridge execution-capable. Triggers **#1** (first backend
endpoint), **#4** (first runtime secret), **#5** (first live provider
connection), and **#7** (first external write-capable integration) remain
uncrossed for the same reason a future Package Registry, Package Validator,
or loader implementation would need its own separate authorization and, for
at least trigger #6, its own Model B reconsideration before proceeding.

### 1.4 Document metrics (normative)

Every count below was **recomputed from this document's own tables during
`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001`**, not carried
forward from version 1.0. A future amendment that changes a table MUST
recompute and restate the corresponding row; a divergence between this
table and its section is a defect in this document, exactly as required by
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §1.4.

| Dimension | Count | Authoritative section |
| --- | --- | --- |
| Specification sections | 29 | §1–§29 |
| Terminology entries | 21 | §4 |
| Architectural ownership rows | 13 | §5 |
| Prohibited package contents | 7 | §6 |
| Package identity fields | 12 | §7 |
| Reused Agent Runtime package-metadata fields | 18 | §7.3, citing Runtime §10.1 |
| Asset categories in the layout model | 9 | §8 |
| Manifest relationship rows | 6 | §9 |
| Capability states | 5 | §10 |
| Permission/approval categories | 12 | §11 |
| Framework compatibility rows | 6 | §13 |
| Asset-type boundary rows (§14) | 5 | §14 |
| Command collision-detection rules | 7 | §14.1 (added in v1.1) |
| Shared Context rules | 8 | §15 |
| Runtime-interaction stages | 9 | §16 |
| Package lifecycle states | 11 | §17 |
| Validation layers | 9 | §18 |
| Trust-state categories | 7 | §19 |
| Observability projections | 11 | §20 |
| Error/rejection classes | **16** (added `COMMAND_NAMESPACE_COLLISION` in v1.1) | §21 |
| Batch eligibility declarations | 7 | §23 |
| Security threats | 12 | §24 |
| Non-goals | 12 | §25 |
| Follow-up contracts | 12 | §26 |
| Acceptance criteria | 14 | §27 |

## 2. Purpose and scope

### 2.1 The problem this contract solves

MellyCore AIOS accepts an Agent Runtime architecture
(`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`) that coordinates,
authorizes, and observes agent runs across six frameworks, but that
architecture **deliberately deferred** one question: what exactly is the
portable thing MellyCore coordinates? Runtime §10 fixed only the minimum
metadata the Runtime requires from a package, and named the rest **"deferred
to its own task"** — this task.

Without a canonical package boundary, each framework integration, each
skill/hook/command/plugin author, and each future Package Registry
implementation would invent its own idea of what an agent "is," re-collapsing
the definition/package/instance separation (Runtime §9) and the
declaration-is-not-a-grant discipline (Runtime §10.2 rule 1) that the Runtime
architecture spent two review cycles establishing.

This contract supplies that missing layer: **one provider-agnostic
description format** for an agent and its declarative assets, and the
validation, trust, and lifecycle vocabulary MellyCore uses to reason about
that format — without implementing any of it.

### 2.2 In scope

The Agent Package as a described, versioned, declarative artifact: its
identity, permitted and prohibited contents, logical layout, relationship to
the Agent Manifest and to Skill/Command/Hook/Plugin/MCP declarations,
capability and permission declaration model, dependency model,
framework-compatibility projection, Shared Context interaction boundary,
Agent Runtime interaction boundary (discovery through termination
projection, without runtime behavior), lifecycle states (not a full
transition-rule contract — see §26), validation layers (not a validator
implementation), trust and provenance vocabulary (not a signing mechanism),
observability projections (information architecture only), an error and
rejection taxonomy, versioning and compatibility rules, Batch Orchestration
compatibility declarations, and the security threat model a package boundary
must resist.

### 2.3 Explicitly out of scope

1. Agent Runtime implementation of any kind (owned by
   `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`, unchanged by this
   task).
2. Package loader, unpacker, sandbox, or import-path implementation.
3. Package Registry, Agent Package Store, or Package Validator
   implementation.
4. Execution of any package, agent, skill, command, hook, plugin, or MCP
   server.
5. Cryptographic signing infrastructure, key management, or trust-root
   implementation.
6. A package distribution transport, marketplace, or CLI.
7. Full transition-rule, event, and evidence contracts for Package Lifecycle,
   Package Validation, and Package Distribution — named and bounded here
   (§26), specified in full only by their own future, separately gated
   tasks.
8. Full Skill Registry, Hook Registry, Command Registry, Plugin Registry, and
   MCP Registry contracts — bounded here (§14), specified in full only by
   their own future tasks.
9. Any provider connection, credential configuration, or model-provider call.
10. Batch Orchestration implementation (§23 defines only package-side
    eligibility declarations).
11. Any push, pull request, merge, or remote branch operation.
12. Any MellyTrade interaction, trading, broker, or order behavior.

## 3. Authority and source contracts

This contract occupies the **"agent package declaration"** rung
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §3 already reserved for
it, one level below the Agent Runtime architecture and above tenant policy:

```text
shared_context/SAFETY_CONTRACT.md
  > Enterprise-Provider ADR
  > Provider Registry contract
  > Integration Gateway contract
  > Agent Runtime architecture
  > framework-specific bridge contract (stricter only)
  > this Agent Package Contract (stricter only)
  > tenant policy (stricter only)
```

This contract is a **mandatory floor** for any future package. It MUST NOT
weaken any requirement of the six documents above it. A framework bridge may
add requirements stricter than this contract; this contract may add
requirements stricter than the Agent Runtime architecture; neither may
subtract. Conflicts fail closed and affected packages are denied pending
resolution.

Consumed as canonical, reused rather than restated:

| Source | What this contract reuses |
| --- | --- |
| `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` | §8.1 canonical identifiers (`agent_definition_id`, `agent_package_id`, `package_revision_id`); §9 nine package/runtime separation states; §10.1 eighteen required package-metadata fields; §10.2 declaration rules; §11 six-framework closed set and bridge prohibitions; §14 eleven authorization facts; §18 six memory categories; §27 explicit non-authorizations pattern |
| `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` | §7.1 common entity contract; §7.2 entity catalogue (`Skill`, `Tool`, `Agent`, `Integration` entities remain byte-identical and are this contract's downstream projection targets, not its source of truth); §8 six orthogonal status dimensions; §9.4 Agent Runtime Directory; §9.8 Batch Run and Artifact Queues; §16 approval contract; §17 secrets boundary; §18 provenance; §19 failure and unknown states |
| `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` | §21.1 eight independent provider-authorization facts (unchanged, not restated as package facts); §24 MCP server registration, suspension, deprecation, and retirement (canonical owner of MCP server records; this contract only references them) |
| `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` | §12 capability resolution (one capability, one bounded operation); §17 policy-evaluation order; §18 approval binding; §21 MCP security contract; §25 error-taxonomy pattern (outward coarse, inward precise) |
| `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` | §5 Unified Run Ledger record identity, for cost-attribution references only |
| `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` | Tenant isolation, external-content posture |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`, `shared_context/context_provenance/**` | Shared Context admission, provenance, and sensitivity rules |
| `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`, `TASK_INDEX.md` | Safety boundaries, Model A migration triggers, live sequencing, task identifiers |

## 4. Terminology

Normative definitions. Where a term is already canonically defined elsewhere,
this section cites the owner instead of redefining it.

| Term | Definition |
| --- | --- |
| **Agent Package** | One immutable, versioned, declarative description of an agent and its assets, identified by `(agent_definition_id, package_revision_id)` (Runtime §8.1). A package is data, never executable payload it self-authorizes to run. |
| **Package Manifest** | The package's top-level declaration file: identity (§7), the eighteen Runtime-required fields (§3), asset references (§8), and the capability/permission/dependency declarations (§10–§12). One package has exactly one Package Manifest. |
| **Agent Manifest** | The behavioral description of the agent itself — role, instructions, model requirements, tool bindings — referenced *from* the Package Manifest by `entrypoint_reference` (Runtime §10.1). Its full contract is a named follow-up (§26); this document fixes only the reference boundary (§9). |
| **Asset** | Any declared file or logical unit inside a package: a prompt, a Skill declaration, a Command declaration, a Hook declaration, a Plugin declaration, an MCP Declaration, a fixture, a test declaration, or documentation (§8). |
| **Capability** | A named class of behavior a package requests (e.g., `filesystem.read`, `network.egress`). A capability the package *declares* is a request, never a grant (§10); a capability the Integration Gateway *resolves* is "one capability, one bounded operation" (Gateway §12) — the two uses are related but not identical, and this contract never redefines the Gateway's. |
| **Permission** | An approval-gated authorization for one declared capability, issued only through the Operator/policy approval boundary (§11). Permission is never self-issued by a package. |
| **Dependency** | A declared requirement on another package, a runtime capability, a provider capability, or a compatibility range (§12). A dependency is a requirement statement, never an automatic installation or activation. |
| **Runtime Adapter** | The framework-specific bridge implementation (owned by the future Framework Bridge Contract, Runtime §16) that a package's `framework_type` selects a compatibility projection for (§13). This contract names it only as a reference target. |
| **Provider Adapter** | The existing provider-adapter concept already established by `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` and the Provider Registry/Gateway track. A package's `provider_requirements` field (Runtime §10.1) references Provider Adapter capability classes; it never binds to one adapter instance. |
| **Skill** | A packaged, reusable, triggerable declared workflow unit (§14). Full contract: future Skill Registry (§26). Related, not identical, to the Control Plane's `Skill` entity (§7.2), which is that entity's frontend/observability projection, not its source of truth. |
| **Command** | A packaged, named, invokable declared operation (§14), generalizing the existing documentation-defined `/roadmap` operator command pattern (`ROADMAP.md`'s "Operator Command"). Full contract: future Command Registry (§26). |
| **Hook** | A packaged, event-bound declared automation unit (§14), bound only to Agent Runtime lifecycle events already fixed by Runtime §12 and §26. Full contract: future Hook Registry (§26). |
| **Plugin** | A packaged bundle of Skills, Commands, Hooks, agents, and MCP Declarations distributed and versioned as one unit (§14). Full contract: future Plugin Registry (§26). |
| **MCP Declaration** | A package's declared *reference* to an already-registered MCP server record (Provider Registry §24) and its security contract (Gateway §21). An MCP Declaration never registers, re-registers, or redefines a server record (§14). |
| **Package Validator** | The (future, unimplemented) mechanism that evaluates a package against the validation layers of §18 and produces the `validated` / `validation_failed` lifecycle state (§17). Its engineering contract is the future Package Validation task (§26); this document fixes only what "verified" must mean. |
| **Package Registry** | The (future, unimplemented) discovery, index, and trust-state service for known Agent Packages. Terminology reconciliation: the Agent Runtime spec's adjacency table (§7.3) already names a future **Agent Package Store** as the owner of package artifact existence and of the verified/installed revision the Runtime references. This document uses **Package Registry** for that same future system's discovery/index/trust-state responsibility and **Agent Package Store** (Runtime's existing term, unchanged) for its artifact-storage responsibility — one future system, two named responsibilities, neither term renames the other. |
| **Package Instance** | One activation-eligible reference to an installed package revision within one tenant and environment — the artifact a future Agent Registry installation record points at (Runtime §9 state 4, "Package installed"). A Package Instance is distinct from, and precedes, the Agent Runtime's `runtime_instance_id` (Runtime §8.1), which identifies a live coordinator instance, not an installed reference. |
| **Package Provenance** | The `package_provenance` field already required by Runtime §10.1: source, build, signer, and digest evidence. This contract adds no second provenance field; §19 defines the trust-state vocabulary built on top of it. |
| **Package Trust State** | The categorical classification (§19) a Package Instance holds along the local / first-party / third-party / imported / generated / unsigned-or-unverified / revoked-or-blocked vocabulary. This is an **Agent Package domain concept, typed entity data under Control Plane §7.1's general allowance** ("domain fields such as outcome, verdict, trust, basis, and configuration state remain typed entity data and are not additional status dimensions") — **not** a seventh Control Plane status dimension, and **this contract defines no projection of Package Trust State onto `evidence_state`, `approval_state`, or any other Control Plane §8.1 dimension.** Unlike the Agent Runtime's `run_state`, which projects onto `lifecycle_status` through a verified, row-complete mapping table and an explicit, additive Control Plane amendment (`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`), Package Trust State has received neither, so this contract makes no equivalent claim. Any future rendering of Package Trust State alongside Control Plane's dimensions requires its own dedicated mapping contract or an explicit, separately reviewed Control Plane amendment — neither of which this document performs. |
| **Contract Version** | The version of *this specification* a package declares conformance to (§22), independent of the package's own `package_version`. |
| **Provider Pack** | An unrelated, already-existing, canonical concept (`[[MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001]]`, `[[MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001]]`): a bundle of *provider capability mappings* for a domain, owned by the Provider Registry track. It shares the word "pack" with "package" by coincidence of English, not of architecture; an Agent Package never contains, wraps, or supersedes a Provider Pack, and neither document amends the other. |

## 5. Architectural ownership

No concern below is owned by more than one document. Where this contract
*consumes* another owner's concept, it is named "consumes," never "owns."

| Concern | Canonical owner | This contract's role |
| --- | --- | --- |
| Package format, identity, boundary, declarations (this document's actual subject) | **This Agent Package Contract** | Owns |
| Agent identity, run identity, package/runtime separation states, execution envelope, run lifecycle | `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` | Consumes verbatim; supplies the package-side declarations Runtime §10 already reserved for it |
| Package artifact existence and storage | Agent Package Store (future, named by Runtime §7.3) | This contract defines what a stored artifact must contain, not how it is stored |
| Package discovery, index, trust-state lookup | Package Registry (future, §4) | This contract defines what the registry indexes, not the registry itself |
| Package/agent installation and registration | Agent Registry (future, named by Runtime §7.3 and §9) | Not this contract's concern; consumes a verified package revision as input |
| Package verification ("Package verified" state) | **This Agent Package Contract** (Runtime §9 row 3 names it as this task's owner) | Owns the validation-layer vocabulary (§18); the Package Validator's engineering contract is a named follow-up (§26) |
| Provider authorization facts, credential classes, MCP server registration | `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` | Consumed unchanged; MCP Declarations reference, never redefine, §24 records |
| Provider access execution, capability resolution, approval binding, policy-evaluation order, MCP security contract | `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` | Consumed unchanged; package capability declarations are requests only |
| Model routing | Model Router (future, control surface at Control Plane §9.2) | Consumed via Runtime §23's boundary; this contract adds no routing behavior |
| Six status dimensions, entity catalogue (`Skill`, `Tool`, `Agent`, `Integration`), Batch queue surface | `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` | Consumed unchanged; this contract's declarations are inputs to those entities, never a competing definition. **Package lifecycle state (§17) and Package Trust State (§19) are Agent Package domain concepts under Control Plane §7.1's typed-domain-field allowance; this contract defines no projection of either onto any of Control Plane's six closed dimensions** (§4) |
| Safety and approval layers | `shared_context/SAFETY_CONTRACT.md`, Control Plane §16, Gateway §18 | Consumed unchanged; this contract adds no new approval authority |
| Package Registry (as a future implementation) | Future, separate task | Named and bounded here (§4, §16); not implemented, not authorized to begin implementation by this document |
| Batch Orchestration | Future, separate task; consuming surface Control Plane §9.8 | This contract defines only package-side eligibility declarations (§23) |

## 6. Package boundary

### 6.1 What an Agent Package MAY contain

A Package Manifest; an Agent Manifest reference; prompts; Skill, Command,
Hook, Plugin, and MCP **declarations** (never their registries); capability,
permission, and dependency declarations; declared fixtures and test
declarations; declared documentation; provenance metadata; and any asset
category listed in §8.

### 6.2 What an Agent Package MUST NOT contain

1. **Embedded secrets** of any kind (API keys, tokens, passwords, private
   keys).
2. **Provider credentials** or credential material, in any form.
3. **`.env` files**, or any file matching the Safety Contract's blocklist
   patterns.
4. **Undeclared executable payloads** — any binary, script, or code path not
   named in the manifest's declared assets.
5. **Hidden network dependencies** — any network destination not declared
   under `provider_requirements` or an MCP Declaration.
6. **Unbounded filesystem access** — a package MUST declare exact,
   bounded, writable-file ownership (§11.1) rather than requesting
   unrestricted read/write.
7. **Self-authorized runtime permissions** — no manifest field may set its
   own capability, permission, or trust state to granted, approved, or
   trusted (§10 rule 1 restated for packages).

A package violating any rule above fails structural or safety validation
(§18) and is denied (`PACKAGE_BOUNDARY_VIOLATION`, §21) before any other
check runs.

## 7. Package identity

### 7.1 Canonical identity fields

| Field | Source | Purpose |
| --- | --- | --- |
| `agent_definition_id` | Runtime §8.1 (reused, unchanged) | The logical agent this package packages |
| `agent_package_id` | Runtime §8.1 (reused, unchanged) | The packaging line for one definition |
| `package_revision_id` | Runtime §8.1 (reused, unchanged) | One exact immutable revision |
| `display_name` | This contract | Human-facing label; never accepted as an identifier (Runtime §8.2 rule 5) |
| `package_version` | This contract (§22) | The package author's own semantic version |
| `contract_version` | This contract (§22) | The version of this specification the package declares conformance to |
| `publisher_or_origin` | This contract | First-party, third-party, or generated origin reference (§19), never a trust grant by itself |
| `package_type` | This contract | One of the asset categories in §8.1 that best classifies the package's primary purpose |
| `description` | This contract | Human-facing summary |
| `license_metadata` | This contract | License reference, where applicable (§7.2 rule 4) |
| `created_at` / `modified_at` | This contract | Timestamps; unknown is `null`, never fabricated (Control Plane §7.1) |
| `package_provenance` | Runtime §10.1 (reused, unchanged) | Source, build, signer, digest, and verification evidence |

### 7.2 Rules

1. `package_revision_id` is permanent and never reused or re-pointed
   (Runtime §8.2 rule 6); a changed manifest is a new revision (§22).
2. `display_name` and `package_type` are labels; they are never accepted as
   identity at any trust boundary (Runtime §8.2 rule 5).
3. Identity fields carry no mutable state, permission, sensitivity, or
   authorization outcome (Runtime §8.2 rule 3), applied identically to
   package identity.
4. `license_metadata`'s absence is legal metadata, never a security fact,
   and MUST NOT be treated as a validation, trust, or capability signal by
   any layer of §18 or §19.

### 7.3 Reused Runtime package-metadata fields

The eighteen fields `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §10.1
already requires — `agent_definition_id`, `package_revision_id`,
`framework_type`, `entrypoint_reference`, `declared_capabilities`,
`declared_tools`, `required_context_classes`, `produced_context_classes`,
`model_requirements`, `permission_requirements`, `provider_requirements`,
`resource_limits`, `supported_environments`, `sensitivity_posture`,
`external_content_posture`, `cancellation_support`,
`deterministic_replay_support`, `package_provenance` — are this contract's
**minimum required fields**, unchanged in name, meaning, or fail-closed
behavior. This contract adds the identity fields of §7.1 and the
declarations of §8–§12 around them; it does not restate or narrow them.

## 8. Package layout model

### 8.1 Asset categories

1. Package Manifest (exactly one, required).
2. Agent Manifest reference (exactly one, required).
3. Prompts (zero or more).
4. Skill declarations (zero or more, §14).
5. Command declarations (zero or more, §14).
6. Hook declarations (zero or more, §14).
7. Plugin declarations (zero or more, §14 — a package MAY declare itself a
   Plugin bundling other declared assets; it MUST NOT declare a second,
   nested Package Manifest).
8. MCP Declarations (zero or more, §14).
9. Fixtures, test declarations, and documentation (zero or more).

### 8.2 Illustrative layout (non-normative)

The tree below illustrates one possible on-disk shape. **It is illustrative
only, not implemented, and not a binding storage format.** A future Agent
Package Store MAY use a different physical layout as long as it can produce
the logical asset categories above.

```text
example-agent-package/            # illustrative, not implemented
  package.manifest.json           # Package Manifest (§7, §10-12)
  agent.manifest.json              # Agent Manifest reference target (§9)
  prompts/
    system.md
  skills/
    example-skill.declaration.json
  commands/
    example-command.declaration.json
  hooks/
    example-hook.declaration.json
  mcp/
    example-server.declaration.json
  fixtures/
    example.fixture.json
  docs/
    README.md
```

## 9. Manifest relationship

| Relationship | Boundary this contract fixes | Full contract owner |
| --- | --- | --- |
| Package Manifest → Agent Manifest | Package Manifest carries exactly one `entrypoint_reference` (Runtime §10.1) resolving to one Agent Manifest; the Agent Manifest is never inlined into the Package Manifest | Future Agent Manifest contract (§26) |
| Package Manifest → Capability Contract | Package Manifest carries `declared_capabilities` (Runtime §10.1) as capability-class references; the capability vocabulary itself is owned elsewhere (§5, Gateway §12) | Future Capability Contract (§26) |
| Package Manifest → Skill declarations | Package Manifest lists zero or more Skill declaration references by asset path and revision; a Skill declaration's internal shape is bounded, not fully specified, in §14 | Future Skill Registry (§26) |
| Package Manifest → Hook declarations | Same reference pattern as Skills, bound to Runtime lifecycle events only (§14) | Future Hook Registry (§26) |
| Package Manifest → Command declarations | Same reference pattern as Skills, generalizing the existing `/roadmap` pattern (§4) | Future Command Registry (§26) |
| Package Manifest → Plugin / MCP declarations | Plugin declarations reference bundled Skill/Command/Hook/agent/MCP declarations by revision; MCP Declarations reference registered Provider Registry §24 records only | Future Plugin Registry, Future MCP Registry (§26) |

This contract does **not** fully specify any right-hand column above. It
fixes only that a reference exists, what it must minimally carry (an
identifier and a revision), and who owns the full contract.

## 10. Capability declarations

### 10.1 Five separated states

A capability name (e.g., `filesystem.read`, `network.egress`,
`shell.execute`) passes through five independently established states. **No
state implies the next**, mirroring the discipline of Runtime §9:

| # | State | Established by | Absence means |
| --- | --- | --- | --- |
| 1 | **Declared capability** | The package's own manifest (`declared_capabilities`, Runtime §10.1) | Undeclared — never grantable at any later state |
| 2 | **Runtime-supported capability** | Agent Runtime / Runtime Adapter, independent of the package | Unsupported — deny, `RUNTIME_CAPABILITY_UNSUPPORTED` |
| 3 | **Policy-allowed capability** | Integration Gateway policy evaluation (Gateway §17) | Policy-denied — deny |
| 4 | **Operator-approved capability** | Explicit Operator approval (Control Plane §16, Gateway §18) | Unapproved — deny |
| 5 | **Active capability** | Agent Runtime, for the lifetime of one authorized run only | Not active — no effect regardless of the other four |

### 10.2 Rules

1. A capability is usable only when **all five** states hold simultaneously
   for the exact package revision, tenant, environment, and run in question.
2. Declaring a capability is a **request statement**, never a grant (Runtime
   §10.2 rule 1, applied identically here).
3. The effective capability set is the **intersection**, never the union, of
   declared, supported, allowed, and approved sets (Runtime §10.2 rule 2).
4. A package MUST NOT claim, project, or display any capability as active
   outside an authorized run (§10.1 row 5).
5. This contract defines no capability vocabulary of its own; capability
   *names* are Gateway §12's concern, referenced here, never redefined.

## 11. Permission and approval model

### 11.1 Categories and approval authority

All twelve categories default **DENY** absent explicit, current, exact-scope
Operator or policy approval. None is self-authorized by a package
declaration.

| # | Category | Approval authority |
| --- | --- | --- |
| 1 | Filesystem read | Gateway policy + Operator approval; bounded to declared paths only |
| 2 | Filesystem write | Same, stricter; a package MUST declare exact writable-file ownership |
| 3 | Shell execution | Operator approval required; `operator_only` by default. *(Non-normative: this default is modeled on, but not owned or governed by, Provider Registry §24.2's `operator_only` pattern for MCP/restricted-tool records — §24 does not itself extend to generic package shell execution.)* |
| 4 | Network access | Gateway policy; bounded to declared `provider_requirements` / MCP targets only |
| 5 | Provider access | Provider Registry's eight facts (§21.1, unchanged) plus Gateway resolution |
| 6 | Git operations | Operator approval; no package may self-authorize a git mutation |
| 7 | PR operations | Operator approval; no package may open, comment on, or merge a PR |
| 8 | Secrets access | Denied by construction — no package may declare a secrets-access capability (§6.2 rule 1) |
| 9 | MCP access | Provider Registry §24 registration + Gateway §21 security contract; package only references |
| 10 | Plugin loading | Operator approval + Package Validator pass (§18); no package self-loads another |
| 11 | Hook activation | Bound to Runtime lifecycle events only (§14); Operator/policy approval required for any side-effecting hook |
| 12 | Parallel or batch execution | §23; Operator approval; no implicit PR, push, merge, or deployment permission |

### 11.2 Rules

1. Approval is bound to one exact `(package_revision_id, tenant, environment,
   capability)` tuple, mirroring Control Plane §7.3's `Approval` entity
   binding rule; it is never blanket, standing, or inferred.
2. A changed package revision invalidates all approvals bound to the prior
   revision (Runtime §10.2 rule 4, applied identically here).
3. Missing, expired, `unknown`, or malformed approval evidence denies; there
   is no default-allow state.

## 12. Dependency model

### 12.1 Declaration

A package declares: required dependencies (other `agent_package_id` +
compatible revision range); optional dependencies; `contract_version`
compatibility range (§22); `model_requirements` and `provider_requirements`
(Runtime §10.1, reused); and `resource_limits` (Runtime §10.1, reused) as the
runtime requirement floor.

### 12.2 Rules

1. A dependency is a **requirement statement**, never an automatic
   installation, activation, or capability grant. **This contract defines no
   dependency-installation or dependency-resolution mechanism; a validation
   failure never itself installs, fetches, activates, or resolves anything.**
2. **Evaluation boundary (normative, deterministic).** `DEPENDENCY_UNRESOLVED`
   (§21) MUST be raised, if at all, exclusively by **§18.1 layer 4
   (Dependency validation)** — this contract's own owned validation stage —
   never by Reference validation (§18.1 layer 3, which checks only that a
   reference *resolves to an existing target*, not that a *dependency
   constraint is satisfiable*) and never by the Agent Runtime's
   instantiation-eligibility stage (§16 stage 5). Dependency validation
   (§18.1 layer 4) MUST run, and MUST reach a determination, **before**
   package verification (Runtime §9 state 3) can be established, which is
   itself a precondition every later Runtime §9 state (4–9) — including
   instantiation eligibility (§16 stage 5) and activation gating (§16 stage
   6) — requires. Runtime's instantiation-eligibility stage **consumes**
   this contract's "Package verified" determination as one input among
   Runtime §9's prerequisite states 1–7; it does **not** independently
   re-derive, re-evaluate, or override a dependency-resolution outcome this
   contract's own validation already reached. This contract, not the Agent
   Runtime, is the sole owner of the `DEPENDENCY_UNRESOLVED` determination
   itself (§5).
3. An unresolved **required** dependency denies package verification with
   `DEPENDENCY_UNRESOLVED` (§21) at dependency-validation time (rule 2); it
   does not silently degrade, substitute another revision, or defer the
   denial to a later stage.
4. Optional dependencies whose absence is tolerated MUST be explicitly
   marked optional; an unmarked dependency is treated as required. An
   unresolved **optional** dependency MUST NOT raise `DEPENDENCY_UNRESOLVED`
   and MUST NOT block package verification; it narrows the package's
   effective declared capability or feature set (whatever that optional
   dependency would have supplied) and MUST NOT be silently treated as
   present, active, or satisfied.
5. Compatibility constraints are evaluated against `contract_version` and
   declared `supported_environments` (Runtime §10.1); a package MUST NOT
   assume compatibility outside its declared range.

## 13. Provider-agnostic compatibility

### 13.1 Compatibility is a projection, not ownership

`framework_type` (Runtime §10.1) selects one of the six closed values Runtime
§11.1 already defines: `claude_code`, `openai_agents_sdk`, `langgraph`,
`crewai`, `autogen`, `mellycore_custom`. This contract adds no seventh value
and no framework-specific ownership. A package's compatibility with a
framework is a **projection** computed against Runtime §11.3's per-framework
integration boundaries — the same "architectural planning position,
independently validated by the future Framework Bridge Contract" caveat
Runtime §11.3 already states applies here unchanged.

### 13.2 Projection table (illustrative structure, not a verified capability test)

| Framework | This contract's compatibility concern |
| --- | --- |
| `claude_code` | Each of this contract's five declared asset types (§14) has a structurally similar Claude Code counterpart — Skill declaration ↔ skill, Hook declaration ↔ hook, Command declaration ↔ slash command, Plugin declaration ↔ plugin, MCP Declaration ↔ MCP server reference — but the correspondence is a **naming and shape parallel only**: this contract's activation boundary (§10, §14), permission model (§11), and validation layers (§18) govern regardless of framework, and no Claude Code-native mechanism satisfies or bypasses any of them |
| `openai_agents_sdk` | Package's `declared_tools` maps to SDK tool definitions via the future Framework Bridge Contract only |
| `langgraph` | Package's lifecycle projects onto graph-node transitions via the bridge only |
| `crewai` | Package's Skill declarations project onto crew task definitions via the bridge only |
| `autogen` | Package's Hook declarations project onto conversational turn events via the bridge only |
| `mellycore_custom` | Native 1:1 mapping; still subject to every rule in this contract |

No row above is implemented, verified, or authorized to be implemented by
this document.

## 14. Skills, commands, hooks, plugins, and MCP

For each asset type: declarative purpose, ownership boundary, validation
expectation, activation boundary, security implications, and relationship to
its future dedicated registry.

| Asset type | Declarative purpose | Ownership boundary | Validation expectation | Activation boundary | Security implications | Future registry |
| --- | --- | --- | --- | --- | --- | --- |
| **Skill** | Declares a packaged, reusable, triggerable workflow with declared inputs, outputs, and required capabilities | This contract fixes only the reference boundary (§9); full behavior contract is the registry's | Structural + capability + dependency validation (§18); a Skill declaring an undeclared capability fails validation | Never self-activating; requires runtime-supported + policy-allowed + operator-approved + active (§10) | Prompt injection via Skill content is an untrusted-content concern (§24); a Skill is data until activated | Skill Registry |
| **Command** | Declares a named, invokable operation, generalizing `/roadmap` | Command *names* may collide with reserved operator commands (`ROADMAP.md`'s Planned Commands); this contract requires collision detection at validation (§14.1), not resolution rules | Structural validation, §18.1 layer 1, per the collision rules of §14.1 | Never self-invoking; invocation requires the same four-state chain as any capability | Command shadowing (a package declaring a command name that shadows a canonical one) is a named threat (§24), fully bounded by §14.1 | Command Registry |
| **Hook** | Declares an event-bound automation unit | Bound only to already-fixed Agent Runtime lifecycle events (Runtime §12); this contract creates no new event vocabulary | Structural + event-reference validation (an unknown event name fails validation) | Never self-activating; a side-effecting Hook additionally requires Operator approval (§11.1 row 11) | Malicious hooks are a named threat (§24); a Hook is inert until an authorized run's lifecycle event triggers policy evaluation | Hook Registry |
| **Plugin** | Declares a bundle of Skill/Command/Hook/agent/MCP declarations distributed as one unit | A Plugin is a manifest-level grouping, not a second Package Manifest (§8.1 rule 7) | Every bundled declaration validates independently; a Plugin's validity is the conjunction, not a separate check | Bundled assets activate independently, each through their own four-state chain; a Plugin grants nothing by bundling | Plugin impersonation (a Plugin claiming another's identity) is a named threat (§24), addressed by `package_provenance` | Plugin Registry |
| **MCP Declaration** | Declares a package's intended reference to one already-registered MCP server record | Owned by Provider Registry §24 (registration) and Gateway §21 (security contract); this contract's declaration carries only `mcp_server_id` and `tool_contract_revision` as a reference, never a registration payload | Reference-existence validation only: the referenced record must exist, be un-suspended, and be un-retired (Provider Registry §24.3) | Governed entirely by Provider Registry §24.2 defaults (no unrestricted search-and-execute, no autonomous generic execution, `output_trust_level: untrusted` always) | Every threat already named in Gateway §21 and Provider Registry §24 applies unchanged; this contract adds no new MCP threat surface | MCP Registry (indexes package-side references only; server records remain Provider Registry's) |

### 14.1 Command namespace and collision detection (normative)

This subsection fixes the exact fail-closed validation requirement §14's
Command row and §24's "command shadowing" threat both depend on. It is
enumerated explicitly under **§18.1 layer 1 (Structural validation)**, so
no future Package Validator implementation can miss it, and it rejects with
`COMMAND_NAMESPACE_COLLISION` (§21).

A package's declared command identifiers and aliases MUST be validated
against all of the following, and **any** match denies the package at
structural-validation time, before any other layer runs:

1. **Duplicate command identifiers within one package.** Two command
   declarations in the same package MUST NOT declare the same command
   identifier.
2. **Duplicate aliases within one package.** Two command declarations in
   the same package MUST NOT declare the same alias, and no alias MUST
   equal another command's primary identifier within that package.
3. **Collisions with reserved MellyCore commands.** No declared command
   identifier or alias MUST match any reserved operator command name
   (`ROADMAP.md`'s Planned Commands, including `/roadmap` itself).
4. **Collisions with already-authorized runtime command namespaces.** No
   declared command identifier or alias MUST match a command namespace an
   Operator has already authorized for this tenant and environment,
   regardless of which package originally declared it.
5. **Deceptive Unicode or normalization-equivalent names.** A declared
   command identifier or alias MUST be validated in its Unicode-normalized
   (NFKC) form; a name that normalizes to an identical or
   visually-indistinguishable string as a reserved command, an
   already-authorized command, or another declaration in the same package
   is treated as a collision under rules 1–4, not as a distinct name.
6. **Attempts to override protected command classes.** No declared command
   identifier or alias MUST match, alias, or shadow a command in the
   safety, validation, approval, Git, provider, or deployment classes,
   regardless of tenant or environment authorization state — this
   prohibition is absolute and MUST NOT be lifted by any package-level
   declaration, capability, or approval.
7. **Package-local declaration is not environment-wide activation.**
   Declaring a command inside a package (§8.1, §9) creates a reference
   candidate only; it MUST NOT be read as registering, activating, or
   granting namespace ownership of that command identifier in any tenant
   or environment. Namespace ownership, activation, and conflict
   resolution across multiple installed packages remain the future
   Command Registry's exclusive concern (§26); this contract fixes only
   the pre-registration rejection rules above.

Rules 1–6 are validation-time rejections this contract itself requires;
rule 7 is a declaration-versus-activation boundary this contract fixes so
the future Command Registry cannot be designed to treat a package-local
declaration as an implicit grant.

## 15. Shared Context interaction

1. **What may enter Shared Context.** Only package identity fields (§7),
   validation results (§18), trust state (§19), and provenance references —
   never asset content bodies (prompt text, Skill/Hook/Command/Plugin
   internals) — may be admitted as Shared Context metadata, and only through
   the existing admission gate (`shared_context/CONTEXT_GRAPH_SCHEMA.md`,
   `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`,
   `shared_context/context_provenance/**`), unchanged by this contract.
2. **What must remain execution-local.** Asset content bodies, dependency
   resolution intermediate state, and validator working state remain
   local to the Package Registry / Package Validator process and are never
   promoted to canonical Shared Context automatically.
3. **Provenance requirement.** Every admitted package-derived Shared Context
   record carries a `source_refs` entry back to the exact
   `package_revision_id`, exactly as `CONTEXT_GRAPH_SCHEMA.md` §2.1 already
   requires for any `ContextNode`.
4. **Context isolation.** A package's declared `required_context_classes`
   and `produced_context_classes` (Runtime §10.1) are the complete, closed
   set of context classes it may read or propose; an unlisted class is
   unreadable and unproposable, unchanged from Runtime §10.2.
5. **Context write permissions.** A package never writes Shared Context
   canonical state directly. Only the Agent Runtime "submits proposals"
   (Runtime §17.1); this contract's declarations bound what may be proposed,
   never how a proposal is admitted.
6. **Memory boundaries.** Reuses the Agent Runtime's six memory categories
   (Runtime §18) unchanged; a package declares no new memory category.
7. **Prevention of undeclared context mutation.** A context write proposal
   referencing a class outside `produced_context_classes` is denied,
   `CONTEXT_CLASS_UNDECLARED` (§21), before it reaches the admission gate.
8. **No package-level bypass of context provenance.** Nothing in this
   contract creates a package-scoped shortcut around the Context Gate; every
   rule of the cited owner documents applies to package-derived context
   exactly as it applies to any other source.

## 16. Runtime interaction

This section defines the **contract**, not the implementation, between an
Agent Package and the Agent Runtime, following the nine stages below in
order. Every stage is a decision boundary the Runtime (or its future
adjacent systems) evaluates; none is executed, connected, or implemented by
this document.

| # | Stage | What it decides | Owner |
| --- | --- | --- | --- |
| 1 | **Discovery** | A Package Registry entry exists referencing an Agent Package Store artifact | Package Registry (future) |
| 2 | **Validation** | The package passes all nine validation layers (§18) | Package Validator (future), per this contract |
| 3 | **Compatibility projection** | The package's `framework_type` and declared requirements project onto an eligible Runtime Adapter (§13) | Future Framework Bridge Contract |
| 4 | **Policy evaluation** | Declared capabilities, permissions, and dependencies pass Gateway policy (§10, §17 of Gateway) | Integration Gateway |
| 5 | **Instantiation eligibility** | All prerequisite Runtime §9 states (1–7) hold for this exact revision | Agent Runtime |
| 6 | **Activation gating** | Run authorization exists (Runtime §9 state 8, §14 eleven facts) | Agent Runtime / Operator |
| 7 | **Lifecycle rendering** | The package's own lifecycle state (§17) is rendered for observability (§20) as its own typed field — **not** projected onto any Control Plane §8.1 dimension (§4, §17.1) — and never substituted for `run_state` | Agent Runtime, Control Plane |
| 8 | **Observability projection** | Package-level fields render per §20 | Control Plane |
| 9 | **Termination or suspension projection** | A package's revision may be suspended, deprecated, or retired, independent of any in-flight run's own cancellation semantics (Runtime §27). *(Non-normative: this state shape is modeled on, but not owned or governed by, Provider Registry §24.3, which is scoped to provider and MCP-server records, not generic Agent Packages.)* | Agent Registry / Package Registry (future) |

No stage above authorizes execution. Stage 6 alone gates whether a run may
begin, and it is owned entirely by the Agent Runtime architecture already
accepted — this contract adds no parallel authorization path.

## 17. Package lifecycle

### 17.1 Eleven package-scoped states

These states describe a **Package Instance's** (§4) lifecycle. They are
package-scoped, not run-scoped, and MUST NOT be confused with the Agent
Runtime's seventeen `run_state` values (Runtime §12.2) or with Control
Plane's six canonical status dimensions (Control Plane §8.1). Package
lifecycle state is an **Agent Package domain concept, typed entity data
under Control Plane §7.1's general allowance for domain fields** (the same
allowance that already covers "trust," "outcome," "verdict," and "basis"
elsewhere in Control Plane's own entity catalogue) — it is **not** a
Control Plane status dimension, and **this contract defines no projection
of package lifecycle state onto `lifecycle_status`, `approval_state`, or
any other Control Plane §8.1 dimension.** §4's `Package Trust State` note
states the identical position for the reasoning behind this choice. No
package lifecycle state below MUST be silently coerced into, rendered as,
or displayed under any Control Plane §8.1 enum value; an implementer
needing a cross-referenced view of package lifecycle alongside Control
Plane's dimensions MUST treat package lifecycle state as its own
independently rendered field (§20), not as a value within any Control Plane
dimension:

1. `draft`
2. `submitted_for_validation`
3. `validation_failed`
4. `validated`
5. `awaiting_operator_approval`
6. `approved`
7. `published`
8. `installed_reference` (an Agent Registry installation exists; installation
   itself remains Agent Registry's concern, not this contract's)
9. `deprecated`
10. `revoked`
11. `retired`

### 17.2 Ownership and boundary (full transition contract deferred)

This section fixes **the states and their non-collision with Runtime's
lifecycle**, not their full transition-rule, evidence, and event contract.
The complete Package Lifecycle contract — predecessor/successor tables,
mandatory evidence, and release conditions, in the depth of Runtime §12.3 —
is a named follow-up (§26). Until that contract exists, a Package Registry
implementation MUST treat every transition above as requiring explicit,
evidenced, Operator-visible justification, and MUST NOT infer a transition
from the absence of one.

### 17.3 Rules

1. `retired` is terminal: a retired `package_revision_id` is never reused
   (mirroring Provider Registry §24.3's `provider_id` rule).
2. `revoked` denies immediately from any state, requires no step-wise
   progression, and does not delete prior approvals — they become inert.
   *(Non-normative: this behavior is modeled on, but not owned or governed
   by, Provider Registry §24.3's `suspended` behavior for provider and
   MCP-server records; §24 does not itself extend to generic Agent Package
   revocation.)*
3. No state above authorizes execution; only Runtime §9 state 8 ("Run
   authorized") does, and it is independent of every state here.

## 18. Validation model

### 18.1 Nine layers

1. **Structural validation** — the manifest parses and every required field
   (§7.3) is present and correctly typed, **and** every declared command
   identifier and alias passes the seven collision-detection rules of
   §14.1, rejecting with `COMMAND_NAMESPACE_COLLISION` (§21) on any match.
2. **Schema/contract validation** — the manifest conforms to this
   contract's declared shapes (§8–§12) and to the referenced
   `contract_version` (§22).
3. **Reference validation** — every asset reference (§9), dependency
   reference (§12), and MCP Declaration reference (§14) resolves to an
   *existing target*. This layer does not evaluate whether a resolved
   dependency's *constraint* is satisfiable — that is layer 4's exclusive
   concern (§12.2 rule 2).
4. **Dependency validation** — the exclusive owner of the
   `DEPENDENCY_UNRESOLVED` determination (§12.2 rule 2): every required
   dependency is resolvable and compatible; an unresolved optional
   dependency narrows the feature set without failing this layer (§12.2
   rule 4).
5. **Capability validation** — every `declared_capabilities` entry is a
   recognized capability class (Gateway §12); an unrecognized class fails
   closed.
6. **Compatibility validation** — `framework_type` and
   `supported_environments` (Runtime §10.1) are internally consistent with
   declared dependencies.
7. **Safety validation** — the package boundary rules of §6.2 hold; a
   detected secret, undeclared executable, or hidden network dependency
   fails closed regardless of any other layer's result.
8. **Provenance validation** — `package_provenance` (Runtime §10.1) is
   present and internally consistent; this layer does not claim
   cryptographic verification exists (§19).
9. **Policy validation** — declared capabilities, permissions, and
   dependencies are evaluable against current Gateway policy (§10, §11);
   this layer records evaluability, not approval, which remains a separate
   act (§10.1 row 4).

### 18.2 Validation success is not execution authorization

Passing all nine layers establishes only Runtime §9 state 3, "Package
verified." It does **not** establish states 4–9 (installed, registered,
runtime-enabled, instantiated, authorized, active). A validated package is
still denied execution absent every later state, exactly as Runtime §9.1
already separates "what exists" from "what is permitted."

## 19. Trust and provenance

### 19.1 Seven trust-state categories

1. **Local package** — authored and validated entirely within this
   repository's own worktree; no external origin claim.
2. **First-party package** — authored by the Operator or an authorized
   MellyCore contributor, with `publisher_or_origin` (§7.1) attesting so.
3. **Third-party package** — authored outside MellyCore's own authorship,
   with `publisher_or_origin` naming the external author.
4. **Imported package** — brought in from an external source without
   modification; provenance MUST record the import source and date.
5. **Generated package** — produced by an automated or agent-assisted
   process; provenance MUST record the generating process, distinct from
   authored-by-a-human provenance.
6. **Unsigned or unverified package** — no cryptographic signature exists or
   none has been checked. **This is the default state for every package
   under this contract**, because §19.2 claims no signing mechanism exists.
7. **Revoked or blocked package** — explicitly denied by Operator decision or
   by a Package Validator safety-layer failure (§18.1 layer 7); revocation
   is immediate and does not require prior states to be unwound (§17.3
   rule 2).

### 19.2 No cryptographic signing claimed

This contract defines the trust-state **vocabulary**, not a signing
mechanism. No key management, signature format, or trust-root
implementation exists or is authorized by this document. A future Package
Validation or Package Distribution contract (§26) may introduce signing;
until it does, every package is at best `unsigned_or_unverified` in the
cryptographic sense, regardless of its first-party/third-party
classification above.

## 20. Observability

### 20.1 Package-level projections

Information architecture only, inheriting Control Plane §7.1's common entity
contract and §8's six status dimensions. No surface, dashboard, or UI is
implemented by this document.

1. Package ID and version (`agent_package_id`, `package_version`).
2. Selected Runtime Adapter / `framework_type` projection (§13).
3. Declared capabilities (§10.1 state 1).
4. Allowed capabilities (§10.1 states 2–3 combined view).
5. Denied capabilities (any capability failing states 2–4).
6. Validation result (§18), per layer, never collapsed to one boolean.
7. Trust state (§19).
8. Provenance (`package_provenance`, Runtime §10.1).
9. Activation status (§10.1 state 5, `active` — never implying authorization
   by itself).
10. Failure reason, when applicable, drawn from the taxonomy of §21.
11. Cost-attribution reference — a pointer to a Run Ledger record (AI
    Operations Intelligence §5) for any run this package's instance
    produced; this contract defines no new cost schema.

### 20.2 Rendering rules

Every projection above that carries a genuine Control Plane §8.1 status
dimension value states that dimension explicitly (Control Plane §8.2).
Projections 6 (validation result) and 7 (trust state) are **package-typed
fields, not Control Plane dimension values** (§4, §17.1, §19) and MUST be
labeled as package-domain data, never displayed as though they were a
`lifecycle_status`, `evidence_state`, or `approval_state` value. No
projection may synthesize a universal "healthy," "active," or green state
across more than one dimension. `NOT_RUN` / `NOT_IMPLEMENTED` never renders
as pass, mirroring Control Plane's `ValidatorResult` rule (§7.2).

## 21. Error and rejection taxonomy

Fifteen stable rejection classes. Outward responses stay coarse; internal
records stay precise, reusing Gateway §25.3's "outward coarse, inward
precise" principle rather than duplicating its exact class list.

| Class | Triggered by |
| --- | --- |
| `PACKAGE_MISMATCH` | Required identity field absent or inconsistent (Runtime §10.1) |
| `UNSUPPORTED_FRAMEWORK` | `framework_type` outside the six-member closed set (§13.1) |
| `PACKAGE_UNVERIFIED` | Validation (§18) not yet passed, or provenance missing |
| `PACKAGE_BOUNDARY_VIOLATION` | A prohibited content category found (§6.2) |
| `MANIFEST_MALFORMED` | Structural validation failure (§18.1 layer 1) |
| `SCHEMA_VIOLATION` | Contract/schema validation failure (§18.1 layer 2) |
| `REFERENCE_UNRESOLVED` | Asset, dependency, or MCP Declaration reference does not resolve (§18.1 layer 3) |
| `DEPENDENCY_UNRESOLVED` | Required dependency unresolved or incompatible (§12.2) |
| `CAPABILITY_UNDECLARED` | A requested capability was never declared (§10.2) |
| `RUNTIME_CAPABILITY_UNSUPPORTED` | Declared capability has no supporting Runtime Adapter (§10.1 state 2) |
| `POLICY_DENIED` | Gateway policy evaluation denies a declared capability or permission (§11) |
| `TRUST_STATE_INSUFFICIENT` | Package Instance's trust state (§19) is below the minimum a policy requires |
| `CONTEXT_CLASS_UNDECLARED` | Shared Context proposal outside `produced_context_classes` (§15 rule 7) |
| `CONTRACT_VERSION_INCOMPATIBLE` | Package's `contract_version` outside this document's declared compatibility range (§22) |
| `REVISION_IMMUTABILITY_VIOLATION` | An attempt to mutate a published `package_revision_id` in place, rather than publish a new revision (§7.2 rule 1, §22) |
| `COMMAND_NAMESPACE_COLLISION` | A declared command identifier or alias fails any of §14.1's seven collision-detection rules (duplicate identifier/alias, reserved-command collision, authorized-namespace collision, Unicode-normalization collision, or an attempt to override a protected safety/validation/approval/Git/provider/deployment command) |

No class above is claimed implemented; this table defines stable names for a
future Package Validator and Agent Runtime to emit, not code that emits them.

## 22. Versioning and compatibility

1. **`package_version`** is the package author's own semantic version,
   independent of this contract.
2. **`contract_version`** is the version of *this specification* (currently
   `1.0`) a package declares conformance to. A Package Validator MUST reject
   a package declaring an unrecognized `contract_version` with
   `CONTRACT_VERSION_INCOMPATIBLE`.
3. **Compatibility range.** A dependency (§12) MAY declare a compatible
   `package_version` range for another package; ranges are evaluated, never
   assumed.
4. **Breaking changes** to this contract (removing a required field,
   narrowing a previously permissive rule) require a new major
   `contract_version` and MUST NOT be back-applied to packages declaring an
   older version.
5. **Additive changes** (a new optional field, a new non-conflicting asset
   category) may land as a minor `contract_version` bump, following the same
   "minimal, additive" discipline the Agent Runtime remediation used for its
   own owner amendments
   (`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`).
6. **Deprecated fields** remain readable for one full major version and are
   never silently repurposed for a different meaning.
7. **Migration expectations.** A package changing `contract_version` is a
   new `package_revision_id` (§7.2 rule 1); there is no in-place migration
   of a published revision.

## 23. Batch Orchestration compatibility

This section defines only the package-side declarations a future `/batch`
workflow would need; **Batch Orchestration itself is not specified,
implemented, or authorized by this document.** The consuming surface remains
Control Plane §9.8 ("Batch Run and Artifact Queues"), unchanged.

Seven required package-side declarations for batch eligibility:

1. **Isolated execution eligibility** — a boolean declaring whether this
   package's runs may execute concurrently with others without shared
   mutable state.
2. **Explicit writable-file ownership** — the exact, bounded file or path
   set this package's runs may write, reusing the filesystem-write category
   of §11.1; an unbounded claim fails validation (§18.1 layer 7).
3. **Declared side effects** — an exhaustive list of external effects a run
   may cause (network calls, file writes, provider operations); an
   undeclared side effect occurring at runtime is a Gateway-level concern
   (Gateway §25), not authorized by this contract.
4. **Bounded resource requirements** — reuses `resource_limits` (Runtime
   §10.1) as the batch scheduler's floor, never a ceiling it may exceed.
5. **Validation command references** — a pointer to how this package's
   validators are invoked (§18), never the validator implementation itself.
6. **Integration ownership** — Batch Orchestration's own future contract
   (§26) owns scheduling, queuing, and dispatch; this contract owns only the
   declarations above.
7. **No implicit PR, push, merge, or deployment permission** — a batch
   eligibility declaration MUST NOT be read as authorizing any git or
   deployment action; those remain separately gated per §11.1 rows 6, 7,
   and 12.

## 24. Security considerations

| Threat | Mitigation posture |
| --- | --- |
| Prompt injection through package assets | Package content (prompts, Skill/Hook text) is untrusted data under Runtime §31's "untrusted by default" principle; never treated as instructions to the Runtime or Validator |
| Malicious hooks | Hooks bind only to fixed lifecycle events (§14) and require Operator approval for side effects (§11.1 row 11); a Hook cannot self-activate |
| Command shadowing | Structural validation (§18.1 layer 1) MUST reject any of §14.1's seven collision classes — duplicate identifiers/aliases, reserved-command collisions, authorized-namespace collisions, Unicode-normalization collisions, and attempts to override protected safety/validation/approval/Git/provider/deployment commands — with `COMMAND_NAMESPACE_COLLISION` (§21), and fail closed |
| Dependency confusion | Dependencies resolve only by exact `agent_package_id` + revision range (§12); no name-similarity or "nearest match" resolution, mirroring Runtime §8.2 rule 4 |
| Undeclared network access | Denied by construction (§6.2 rule 5); any network destination must appear under `provider_requirements` or an MCP Declaration |
| Secret exfiltration | Denied by construction (§6.2 rules 1–2); safety validation (§18.1 layer 7) fails closed on any detected secret pattern |
| Filesystem escape | Writable-file ownership must be exact and bounded (§11.1 row 2, §23 item 2); an unbounded or path-traversal declaration fails validation |
| Privilege escalation | The five-state capability separation (§10.1) prevents any single state from implying the next; declaration alone never elevates |
| Plugin impersonation | `package_provenance` and trust state (§19) must be checked before a Plugin is treated as first-party; a Plugin cannot self-attest its own trust state |
| Provenance spoofing | Provenance validation (§18.1 layer 8) checks internal consistency; this contract does not yet claim cryptographic non-repudiation (§19.2) |
| Context poisoning | Shared Context writes remain proposal-only and class-bounded (§15 rules 4, 5, 7); a package cannot admit its own canonical context |
| Validator bypass | Validation success is explicitly not execution authorization (§18.2); no capability, permission, or approval may be inferred from validation alone |

## 25. Non-goals

1. Package loader, unpacker, or sandbox implementation.
2. Package Registry, Agent Package Store, or Package Validator
   implementation.
3. Cryptographic signing infrastructure or key management.
4. A package distribution transport, CLI, or marketplace.
5. Execution of any package, agent, Skill, Command, Hook, Plugin, or MCP
   server.
6. Full Skill/Command/Hook/Plugin/MCP Registry contracts (bounded, not
   specified in full — §26).
7. Full Package Lifecycle transition-rule contract (bounded, not specified
   in full — §17.2, §26).
8. Full Package Validation engineering contract (bounded, not specified in
   full — §18, §26).
9. Batch Orchestration implementation (§23 bounds only package-side
   declarations).
10. Any provider connection, credential, or live model call.
11. Any push, PR, merge, deployment, or destructive git operation.
12. Any MellyTrade interaction, trading, broker, or order behavior.

## 26. Follow-up contracts

Each below requires its own specification, independent review, remediation
where needed, and explicit Operator authorization before it begins — the
same gated sequence this contract itself is subject to. Task identifiers are
not yet assigned pending Operator sequencing; see `shared_context/TASK_INDEX.md`.

1. **Agent Manifest contract** — full behavioral description format (§9).
2. **Capability Contract** — the capability-name vocabulary itself (§10,
   consumed here from Gateway §12, never redefined).
3. **Skill Registry** — full Skill declaration and activation contract
   (§14).
4. **Hook Registry** — full Hook declaration and activation contract (§14).
5. **Command Registry** — full Command declaration and activation contract
   (§14).
6. **Plugin Registry** — full Plugin bundling and distribution contract
   (§14).
7. **MCP Registry** — package-side MCP reference index (§14; server
   registration remains Provider Registry §24's).
8. **Package Validation** — the Package Validator's full engineering
   contract (§18.2, §21).
9. **Package Lifecycle** — the full transition-rule, evidence, and event
   contract for the eleven states of §17.
10. **Package Distribution** — transport, discovery, and (if introduced)
    signing mechanism (§19.2).
11. **Package Repository** — the Agent Package Store / Package Registry
    implementation itself (§4, §5).
12. **Batch Orchestration compatibility review** — an independent review of
    §23 once a Batch Orchestration contract exists.

## 27. Acceptance criteria

This specification task is complete when all of the following hold:

1. All 29 sections (§1–§29) are present and each required topic from the
   task brief is addressed.
2. Terminology (§4) defines at least the nineteen terms the task brief named.
3. No concern is owned by more than one document (§5); every consumed
   concept cites its canonical owner.
4. Every prohibited package content category (§6.2) is stated and each maps
   to a validation layer (§18) and an error class (§21).
5. Every capability, permission, and dependency declaration is explicitly a
   request, never a grant (§10, §11, §12).
6. The five-state capability separation (§10.1) and eleven-state package
   lifecycle (§17.1) are internally consistent and do not collide with
   Runtime's nine states or seventeen `run_state` values.
7. Provider-agnostic compatibility (§13) names no framework as canonical
   owner of the package model.
8. Every asset type in §14 states its ownership boundary, validation
   expectation, activation boundary, and security implication.
9. Shared Context interaction (§15) does not weaken the existing Context Gate.
10. Batch Orchestration compatibility (§23) declares package-side
    requirements only and claims no implementation.
11. Security considerations (§24) address all twelve threats named in the
    task brief.
12. Non-goals (§25) and follow-up contracts (§26) are each internally
    consistent with the rest of the document (nothing marked a non-goal is
    also claimed complete elsewhere).
13. No implementation, execution, connection, credential, or deployment is
    claimed anywhere in the document (§1.2).
14. The document's own metrics table (§1.4) matches the actual row/entry
    counts in its cited sections.

## 28. References

### 28.1 Repository (canonical)

- `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`
- `[[../research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001]]` (research)
- `[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`
- `[[../research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002]]` (research)
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]`
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`
- `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]`
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]`
- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`
- `[[MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001]]`,
  `[[MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001]]`
- `shared_context/CONTEXT_GRAPH_SCHEMA.md`,
  `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`,
  `shared_context/context_provenance/**`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md`

### 28.2 External

None. This contract makes no claim about any external standard, SDK, or
protocol version beyond the framework names already fixed by
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §11.1.

## 29. Amendment and supersession

This document may be amended only additively unless a major
`contract_version` bump is explicitly declared (§22). An amendment MUST
recompute §1.4's document metrics and MUST NOT weaken any rule in §3's
precedence chain. This document does not supersede, rename, or absorb any
canonical owner document cited in §3, §5, or §28.1; every citation above
remains that document's unmodified, unweakened text unless a separate,
explicitly authorized amendment task states otherwise.
