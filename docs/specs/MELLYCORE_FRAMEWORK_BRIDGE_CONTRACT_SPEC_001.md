# MellyCore Framework Bridge Contract Spec

**Task ID:** MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-001
**Contract ID:** MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_001
**Version:** 1.0 — first draft.
**Verification status:** **Unverified.** No independent review has run. This
document is **not accepted** until
`MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001` completes with a passing
gate decision, in the same sequence used for
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` and
`[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` (spec → review → remediation →
review).
**Status:** Drafted, specification-level only, pending independent review.
**This status does not authorize:** Framework Bridge implementation, framework
adapter implementation of any kind, SDK installation, SDK integration, any
framework process, Agent Runtime implementation, package loading, package
execution, command execution, hook execution, plugin loading, MCP connection,
Batch Orchestration, provider calls, model calls, network operations,
credential configuration, frontend, backend, or deployment. It fixes the
contract a later, separately authorized adapter specification and
implementation must satisfy.
**Scope:** Defines the **Framework Bridge** — the provider-agnostic,
framework-neutral projection boundary through which MellyCore Agent Package and
Agent Runtime concepts MAY be represented inside a supported agent framework,
without any framework becoming the canonical owner of MellyCore architecture.

---

## 1. Purpose and scope

### 1.1 The problem this contract solves

`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §16 states plainly that the
**"Framework Bridge Contract is deferred to its own task"**, and fixes only a
minimum operation set. `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` §13
defines a package's `framework_type` as selecting a **compatibility
projection** whose per-framework detail is likewise deferred "via the future
Framework Bridge Contract only". This document is that task.

Without this contract, each framework integration would independently decide
what a MellyCore agent "is" inside that framework — and the framework's own
native model (its agent object, its graph state, its crew memory, its session
file) would become the de facto definition. That is the exact inversion this
contract exists to prevent.

### 1.2 In scope

The framework-neutral **projection semantics** between MellyCore's canonical
domain model and any supported framework: adapter boundary and metadata,
identity projection, manifest projection, capability projection, permission and
approval projection, prompt and instruction projection, tool projection, and
bounded projection semantics for skills, commands, hooks, plugins, and MCP
declarations; Shared Context and memory projection; framework-session, adapter,
and bridge-evaluation lifecycles; runtime interaction stages; model and provider
routing interaction; error translation; projection loss and unsupported
semantics; a bridge validation model; observability projections; per-framework
projection profiles; the security threat model a bridge boundary MUST resist;
non-goals; deferred dependencies; and acceptance criteria.

### 1.3 Explicitly out of scope

1. Any Framework Adapter implementation, in any language, for any framework.
2. Any SDK installation, import, integration, or invocation.
3. Agent Runtime implementation (owned by
   `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`, unchanged here).
4. Agent Package Store, Package Registry, or Package Validator implementation.
5. Package loading, installation, activation, or execution.
6. Command, hook, plugin, skill, or MCP runtime of any kind.
7. Batch Orchestration.
8. Provider connection, credential configuration, model call, or network
   operation.
9. Frontend, backend, or deployment.
10. The full per-framework adapter specifications (§36).
11. Any push, pull request, merge, or remote branch operation.
12. Any MellyTrade interaction, trading, broker, or order behavior.

### 1.4 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Framework Bridge | `NOT_IMPLEMENTED` — no bridge interface, code, or process exists |
| Framework Adapters (all six) | `NONE_EXIST` — no adapter for any framework exists anywhere in this repository |
| SDKs / frameworks | `NOT_INSTALLED`, `NOT_IMPORTED`, `NOT_EXECUTED` |
| Framework sessions created | **Zero** |
| Runtime handles issued | **Zero** |
| Agent Runtime | Unchanged by this task; still `NOT_IMPLEMENTED` |
| Agent Package Contract | Unchanged by this task; v1.1, accepted as documentation only, `NOT_IMPLEMENTED` |
| Evidence class for every flow below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by this documentation task. A validator that did
not run records `NOT_RUN`, never a defaulted pass.

### 1.5 Relationship to migration triggers

This specification implements nothing, so it crosses no migration trigger in
`shared_context/PROJECT_STATE.md`'s Model A contract. Trigger **#6, "first
execution-capable agent,"** remains uncrossed: nothing here makes any agent,
package, adapter, or bridge execution-capable. Triggers **#1**, **#4**, **#5**,
and **#7** remain uncrossed for the same reason.

## 2. Terminology

Normative definitions. Where a term is already canonically defined elsewhere,
this section cites the owner instead of redefining it.

| Term | Definition |
| --- | --- |
| **Framework Bridge** | The single framework-neutral projection boundary defined by this contract. Exactly one bridge interface exists (Runtime §11.2); a bridge is "an adapter *into* the runtime's model, not a passthrough *out of* it" (Runtime §11.2). |
| **Framework Adapter** | The (future, unimplemented) framework-specific implementation that realizes the Framework Bridge for exactly one `framework_type`. This contract defines an adapter's declared boundary and metadata (§6), never its code. |
| **Canonical Agent** | The MellyCore-owned agent, identified by `agent_definition_id` (Runtime §8.1) and described by an Agent Package (Package §4). The Canonical Agent is the only authoritative agent. |
| **Framework-Native Agent** | Whatever object, graph, crew, or conversational participant a framework calls an "agent". It is a **projection artifact**, never authoritative, and never a Canonical Agent. |
| **Compatibility Projection** | A one-directional, deliberately lossy representation of a canonical MellyCore concept inside a framework. Projection never reverses: no framework-native value is ever read back as canonical (§4). |
| **Capability Projection** | The representation of a package's `declared_capabilities` (Runtime §10.1) inside a framework, preserving all six capability states of §9. |
| **Context Projection** | The bounded, proposal-only representation of Shared Context data inside a framework (§18). |
| **Lifecycle Projection** | The representation of *framework-session*, *adapter*, and *bridge-evaluation* lifecycles (§20). It explicitly excludes canonical package lifecycle rendering, which remains the Agent Package Contract's (§20.4). |
| **Tool Projection** | The representation of a runtime-governed tool as a framework-native tool definition (§12). |
| **Command Projection** | The bounded representation of a package's declared command *existence* inside a framework (§14). It never activates, registers, or resolves a command. |
| **Hook Projection** | The bounded representation of a package's declared hook and its correspondence to a framework lifecycle event (§15). It never activates a hook. |
| **Plugin Projection** | The bounded representation of plugin metadata (§16). It never loads a plugin. |
| **MCP Projection** | The bounded representation of a package's MCP Declaration — itself a reference to a Provider Registry §24 record (§17). It never registers, connects, or tunnels. |
| **Runtime Handle** | An opaque, MellyCore-owned reference through which the Agent Runtime addresses one prepared framework-local invocation state. A Runtime Handle is **not** an authorization, **not** a run, and **not** proof a framework process exists. |
| **Framework Session** | Framework-local execution or conversation state (a CLI session, an SDK run object, a graph invocation, a crew kickoff, a chat). It is bridge-local and non-canonical (Runtime §11.2 rule 6), and is **never** a MellyCore run. |
| **Bridge Validation** | The ten-layer evaluation of §25 that determines whether a projection is expressible and safety-preserving. It establishes expressibility only, never execution authorization (§25.11). |
| **Bridge Eligibility** | The state in which an adapter's declared boundary, versions, and projections have passed Bridge Validation for one exact package revision, tenant, and environment. Eligibility is **not** activation and **not** run authorization (Runtime §14). |
| **Projection Loss** | Any canonical detail that a framework cannot represent. Loss MUST be declared, classified, and — where safety-relevant — MUST fail closed (§24). |
| **Unsupported Semantic** | A canonical MellyCore concept a framework cannot express at all. The Runtime already owns the rejection class `BRIDGE_UNSUPPORTED_BEHAVIOR` (Runtime §16, §33); this contract classifies the semantic, it does not re-own the error. |
| **Adapter Provenance** | Source, build, signer, and digest evidence for a Framework Adapter, following the shape of `package_provenance` (Runtime §10.1). This contract claims **no** signing mechanism exists (§6.4). |

## 3. Architectural ownership

No concern below is owned by more than one document. Where this contract
*consumes* another owner's concept, it is named "consumes", never "owns".

| Concern | Canonical owner | This contract's role |
| --- | --- | --- |
| Framework-neutral projection semantics, adapter declared boundary, projection-loss taxonomy, bridge validation layers, per-framework projection profiles | **This Framework Bridge Contract** | Owns |
| The nine bridge operations and their fail-closed outcomes | `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §16 | Consumes verbatim; adds projection semantics around them, never a tenth operation |
| The six normative bridge rules | Runtime §11.2 | Consumes as a binding floor; MAY add stricter rules, MUST NOT weaken any |
| Closed `framework_type` set | Runtime §11.1 | Consumes unchanged; adds no seventh member (§5) |
| Per-framework planning positions | Runtime §11.3 and §35 | Consumes as **unvalidated planning positions**; defines the validation obligation (§27.2), does not discharge it |
| Agent and run identity, `run_state`, execution envelope, eleven authorization facts, runtime lifecycle | Runtime §8, §12, §14, §15 | Consumes; projects read-only; never redefines |
| Runtime error taxonomy | Runtime §33 | Consumes existing classes; adds only genuinely absent bridge-projection classes (§23) |
| Package identity, boundary, capability/permission/dependency declarations, package lifecycle, trust state | `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` | Consumes; projects read-only; defines no package concept |
| Model selection and routing decisions | Model Router (Runtime §23; control surface Control Plane §9.2; `shared_context/MODEL_ROUTING.md`) | Consumes; routes framework model requests through it; never selects a model |
| Provider authorization facts, credential classes, MCP server registration | `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` §21.1, §24 | Consumes unchanged; references records, never registers or connects |
| Capability resolution, policy-evaluation order, approval binding, MCP security contract | `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §12, §17, §18, §21 | Consumes unchanged; preserves decisions across projection; grants nothing |
| Shared Context canonical truth, admission, provenance, sensitivity | Shared Context Layer; `shared_context/CONTEXT_GRAPH_SCHEMA.md`; `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` | Consumes; projection is proposal-only and never writes canonical state |
| Six orthogonal status dimensions, entity catalogue | `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §7.1, §8.1 | Consumes unchanged; every bridge field below is **typed entity data** under §7.1's allowance, never a seventh dimension |
| Safety and approval authority | `shared_context/SAFETY_CONTRACT.md`, Control Plane §16, Gateway §18 | Consumes unchanged; adds no approval authority |
| Cost attribution and run ledger identity | `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5; Runtime §24, §25 | Consumes; references records, defines no cost schema |
| Full Skill, Command, Hook, Plugin, and MCP registry contracts | Future registries (Package §26) | Bounded here (§13–§17); not specified in full; ownership untouched |
| Framework-specific adapter specifications | Future, separate tasks (§36) | Named and bounded; not written, not authorized |

### 3.1 Precedence

This contract occupies the rung **below** the Agent Runtime architecture and
**beside** the Agent Package Contract, both of which it MUST NOT weaken:

```text
shared_context/SAFETY_CONTRACT.md
  > Enterprise-Provider ADR
  > Provider Registry contract
  > Integration Gateway contract
  > Agent Runtime architecture
  > this Framework Bridge Contract (stricter only)
  > Agent Package Contract (stricter only, on package concerns)
  > framework-specific adapter specification (stricter only)
  > tenant policy (stricter only)
```

A Framework Adapter MAY add requirements stricter than this contract; this
contract MAY add requirements stricter than the Agent Runtime architecture;
neither may subtract. Conflicts fail closed and the affected projection is
denied pending resolution.

## 4. Canonical versus projected state

### 4.1 The direction rule (normative)

The relationship MUST be:

```text
MellyCore canonical contract
        ↓
Framework-neutral bridge semantics
        ↓
Framework-specific adapter projection
```

It MUST NOT be:

```text
Framework-native model
        ↓
MellyCore architecture
```

### 4.2 Rules

1. **Projection is one-directional.** A canonical value MAY be projected into a
   framework. A framework-native value MUST NOT be read back as canonical.
2. **A framework requirement is not a canonical justification.** A
   framework-native representation MUST NOT become canonical merely because a
   framework SDK, configuration file, or schema requires it. If a framework
   demands a shape MellyCore does not own, the adapter MUST construct that shape
   locally as a projection artifact and MUST NOT promote it.
3. **Framework-native state is bridge-local** (Runtime §11.2 rule 6). Framework
   threads, checkpoints, graph state, crew memory, session files, and
   conversation history remain bridge-local until explicitly normalized and
   admitted through the owning gate.
4. **No framework may redefine** any of: agent identity; package identity;
   capability states; permissions; approvals; trust; provenance; lifecycle; run
   state; Shared Context ownership; observability ownership; error taxonomy; or
   Operator authority.
5. **Round-trip is not identity.** That a projected value can be read back out
   of a framework unchanged does not make the framework's copy authoritative.

### 4.3 Canonical versus projected register

| Concept | Canonical owner and field | May be projected? | Projected form is authoritative? |
| --- | --- | --- | --- |
| Agent identity | Runtime §8.1 `agent_definition_id` | Yes, read-only (§7) | **No** |
| Package identity | Runtime §8.1 `agent_package_id`, `package_revision_id` | Yes, read-only (§7) | **No** |
| Capability states | Package §10.1 + §9 here | Yes, as declared/denied labels | **No** |
| Permissions and approvals | Gateway §18, Control Plane §16 | Decision **references** only | **No** |
| Trust state, provenance | Package §19; Runtime §10.1 `package_provenance` | Yes, read-only | **No** |
| `run_state` | Runtime §12 | Yes, read-only | **No** |
| Package lifecycle state | Agent Package Contract §17 | **Deferred — see §20.4** | **No** |
| Shared Context canonical records | Shared Context Layer | Bounded read projection only (§18) | **No** |
| Framework session state | Framework | n/a — already framework-local | **No** — never canonical |
| Framework memory | Framework | n/a | **No** (§19) |
| Routing decision | Model Router (Runtime §23.3) | Decision **reference** only | **No** |

## 5. Supported framework identifiers

### 5.1 The closed set (consumed, unchanged)

`framework_type` is owned by Runtime §11.1 as a closed vocabulary with exactly
six members:

| # | Canonical identifier | Profile section |
| --- | --- | --- |
| 1 | `claude_code` | §28 |
| 2 | `openai_agents_sdk` | §29 |
| 3 | `langgraph` | §30 |
| 4 | `crewai` | §31 |
| 5 | `autogen` | §32 |
| 6 | `mellycore_custom` | §33 |

### 5.2 Rules

1. This contract adds **no** seventh member and renames none. An unknown value
   denies with `UNSUPPORTED_FRAMEWORK` (Runtime §11.1, §33).
2. There is no `other`, `generic`, or `auto` member (Runtime §11.1).
3. **Naming note (normative).** The custom-agent profile's canonical identifier
   is **`mellycore_custom`**, exactly as Runtime §11.1 fixes it. Where planning
   language elsewhere refers informally to "custom agents", the canonical value
   remains `mellycore_custom`; this contract introduces no alias, and "custom"
   alone is not a valid `framework_type` value.
4. Adding a framework identifier requires an amendment to Runtime §11.1 by its
   owner. This contract MUST NOT anticipate one.

## 6. Framework adapter boundary

### 6.1 Declared adapter fields

A Framework Adapter MUST declare the following. These are **declarations**,
never grants, and every field is typed entity data under Control Plane §7.1.

| # | Field | Meaning |
| --- | --- | --- |
| 1 | `adapter_id` | Stable, opaque identity for one adapter line. MUST NOT encode mutable state (Control Plane §7.1). |
| 2 | `adapter_revision_id` | One exact immutable adapter revision. Permanent; never reused or re-pointed. |
| 3 | `adapter_version` | The adapter author's own semantic version. |
| 4 | `framework_type` | Exactly one member of §5.1. An adapter MUST NOT declare two. |
| 5 | `supported_bridge_contract_range` | The range of **this** contract's versions the adapter conforms to (§6.3). |
| 6 | `supported_package_contract_range` | The range of Agent Package Contract versions the adapter can project (§6.3). |
| 7 | `framework_compatibility_range` | The framework versions the adapter claims to target, as a declared range only. |
| 8 | `projection_capabilities` | Which projections of §7–§19 the adapter claims to support. |
| 9 | `declared_limitations` | Every projection the adapter **cannot** perform, declared **before** it is asked (Runtime §16, `report_unsupported_behavior`). |
| 10 | `required_runtime_features` | Runtime features the adapter requires; absence denies eligibility. |
| 11 | `adapter_provenance` | Source, build, signer, digest evidence (§6.4). |
| 12 | `validation_state` | The Bridge Validation outcome (§25). Absent or `unknown` denies. |

### 6.2 Rules

1. **Declaration is not capability.** A declared `projection_capabilities` entry
   is a claim requiring validation (§25), never a grant.
2. **Silence is not a capability claim** (Runtime §16). An adapter that omits a
   limitation has not thereby acquired the capability; unvalidated projections
   deny.
3. An adapter MUST NOT self-assert `validation_state`, trust, or approval.
4. A changed `adapter_revision_id` invalidates every prior Bridge Eligibility
   determination bound to the previous revision.
5. This contract defines **no executable adapter code**, no interface
   signatures in any programming language, and no build or packaging format.

### 6.3 Version independence (normative)

`adapter_version`, `bridge_contract_version`, `package_contract_version`, and
`framework_compatibility_range` are **four independent** version axes and MUST
NOT be conflated.

- The **bridge contract version** of this document is **1.0**.
- The Agent Package Contract's own current-version declaration is **disputed
  and unresolved** under its Review 002 finding `NEW-P2-02`. Accordingly this
  contract **declares no value** as the Agent Package Contract's canonically
  current version, and an adapter MUST express package-contract compatibility
  as a **range** resolved against the Agent Package Contract owner's own
  declaration once that owner corrects it. See §20.4 and §36.

### 6.4 No adapter signing claimed

This contract defines the **vocabulary** for adapter provenance, not a signing
mechanism. No key management, signature format, or trust-root implementation
exists or is authorized by this document. Until a future contract introduces
one, every adapter is at best `unsigned_or_unverified` in the cryptographic
sense, regardless of origin.

## 7. Agent identity projection

1. Canonical identifiers — `agent_definition_id`, `agent_package_id`,
   `package_revision_id`, `runtime_instance_id` (Runtime §8.1) — MUST be
   projected **read-only** and MUST NOT be replaced, renamed, re-minted,
   re-encoded with meaning, or reassigned by any adapter.
2. Where a framework requires its own agent name or identifier, the adapter MUST
   construct a **framework-local label** and MUST maintain an explicit mapping
   back to the canonical identifier. The framework-local label MUST NOT be
   accepted as identity at any trust boundary (Runtime §8.2 rule 5).
3. Framework-local labels MUST NOT collide across tenants or environments, and
   MUST NOT be derived in a way that leaks tenant identity into a framework
   surface.
4. An adapter MUST NOT reuse a framework-local label across two different
   `package_revision_id` values.
5. Identity fields carry no mutable state, permission, sensitivity, or
   authorization outcome (Runtime §8.2 rule 3), and projection MUST NOT add any.

## 8. Manifest projection

An Agent Package or Agent Manifest MAY be projected into framework-native
configuration, subject to the following.

### 8.1 Prohibitions (normative)

The framework projection MUST NOT:

1. add any capability the package did not declare;
2. remove, relax, or omit any restriction the package declared;
3. grant any permission;
4. enable, authorize, or select any provider;
5. install, fetch, or resolve any dependency;
6. activate any command;
7. activate any hook;
8. load any plugin;
9. connect to any MCP server;
10. mutate Shared Context canonical state.

### 8.2 Rules

1. Projection is **subtractive or equal, never additive** with respect to
   authority: the projected configuration MUST express a subset of what the
   canonical manifest permits, never a superset.
2. A required manifest field the framework cannot represent is an unsupported
   semantic and MUST fail closed with `BRIDGE_UNSUPPORTED_BEHAVIOR` (Runtime
   §16, `translate_envelope`).
3. An adapter MUST NOT synthesize a manifest field that the canonical manifest
   omits in order to satisfy a framework schema; it MUST instead declare the
   projection unsupported.
4. Framework-native configuration produced by projection is a **derived
   artifact**. It MUST NOT be committed to the repository as canonical, and MUST
   NOT be treated as the package.

## 9. Capability projection

### 9.1 Six separated states

The Agent Package Contract §10.1 fixes five capability states. Framework
support is a **sixth, independent** state introduced by this contract, inserted
without collapsing any existing one. **No state implies any other.**

| # | State | Established by | Absence means |
| --- | --- | --- | --- |
| 1 | **Declared** | The package manifest (`declared_capabilities`, Runtime §10.1) | Undeclared — never grantable |
| 2 | **Framework-supported** | The framework, via the adapter's validated `projection_capabilities` (§6) | Not projectable — deny, `PROJECTION_UNSUPPORTED` (§23) |
| 3 | **Runtime-supported** | Agent Runtime / adapter, independent of the package | Unsupported — deny, `UNSUPPORTED_CAPABILITY` (Runtime §33) |
| 4 | **Policy-allowed** | Integration Gateway policy evaluation (Gateway §17) | Policy-denied — deny |
| 5 | **Operator-approved** | Explicit Operator approval (Control Plane §16, Gateway §18) | Unapproved — deny |
| 6 | **Active** | Agent Runtime, for the lifetime of one authorized run only | Not active — no effect |

### 9.2 Rules

1. A capability is usable only when **all six** states hold simultaneously for
   the exact package revision, adapter revision, tenant, environment, and run.
2. The effective capability set is the **intersection**, never the union.
3. **A framework's ability to perform an action MUST NOT be interpreted as
   MellyCore authorization.** That a framework exposes a filesystem helper, a
   shell tool, or a network client establishes state 2 at most, and states 3–6
   remain independently required.
4. Conversely, framework support is **necessary but not sufficient**: a
   capability that is declared, runtime-supported, policy-allowed, approved, and
   active is still unusable through a framework that cannot express it.
5. An adapter MUST NOT report a capability as active outside an authorized run.
6. This contract defines **no capability vocabulary of its own**; capability
   names remain Gateway §12's concern.

## 10. Permission and approval projection

### 10.1 Category treatment

All thirteen categories default **DENY**. **Framework defaults MUST NOT
override MellyCore deny-by-default policy** in any category.

| # | Category | Bridge projection rule |
| --- | --- | --- |
| 1 | Filesystem read | Project only the exact declared, approved paths; a framework's default working-directory access MUST be constrained or the projection declared unsupported |
| 2 | Filesystem write | Project only exact declared writable-file ownership; unbounded framework write access MUST be constrained or unsupported |
| 3 | Shell execution | `operator_only` by default (Package §11.1 row 3); a framework-native shell tool MUST be disabled or intercepted (Runtime §11.2 rule 1) |
| 4 | Network access | Bounded to declared `provider_requirements` / MCP targets; framework-native HTTP helpers MUST be disabled or intercepted |
| 5 | Provider access | Provider Registry's eight facts (§21.1) plus Gateway resolution; **no direct provider access** (Runtime §11.2 rule 2) |
| 6 | Secret access | **Denied by construction.** A bridge never holds, reads, requests, derives, or forwards a credential (Runtime §11.2 rule 2); no projection may carry secret material |
| 7 | Git mutation | Operator approval; no adapter or framework may self-authorize a git mutation |
| 8 | PR operations | Operator approval; no adapter may open, comment on, or merge a PR |
| 9 | MCP access | Provider Registry §24 registration + Gateway §21; reference only (§17) |
| 10 | Plugin loading | Operator approval + validation; no adapter self-loads a plugin (§16) |
| 11 | Hook execution | Bound to fixed lifecycle events; Operator/policy approval for any side-effecting hook (§15) |
| 12 | Batch execution | Package §23; Operator approval; no implicit PR, push, merge, or deployment permission |
| 13 | Deployment | Operator approval; never implied by any projection, adapter, or framework capability |

### 10.2 Rules

1. Approval binds to one exact
   `(package_revision_id, adapter_revision_id, tenant, environment, capability)`
   tuple. It is never blanket, standing, or inferred.
2. A changed package revision **or** adapter revision invalidates all approvals
   bound to the prior tuple.
3. Missing, expired, `unknown`, or malformed approval evidence **denies**.
4. **Permission flattening is prohibited.** An adapter MUST NOT collapse
   distinct MellyCore permission categories into one coarse framework
   permission (for example a single "allow tools" switch). If a framework offers
   only coarse permissions, the adapter MUST either constrain them to the
   narrowest declared category or declare the projection unsupported.
5. A projected permission MUST carry a **reference** to the authorizing decision
   (Gateway §18), never a copy of the authority itself.

## 11. Prompt and instruction projection

1. **System instruction projection.** A package's declared prompts and the
   runtime's policy instructions MAY be projected into a framework's system
   instruction surface. The projection MUST preserve MellyCore's instructions
   intact and MUST NOT truncate, summarize, or reorder them to fit a framework
   limit; if they do not fit, the projection is unsupported and fails closed.
2. **Package prompt projection.** Package prompt content is **untrusted data**
   under Runtime §31 and Package §24. It MUST NOT be treated as instructions to
   the Runtime, the adapter, or the Validator.
3. **Precedence (normative, highest first).** Safety Contract and MellyCore
   policy → Operator instruction → Agent Runtime envelope → package-declared
   prompt → framework-native default instruction. A framework-native default
   MUST NOT displace anything above it.
4. **Operator instruction precedence.** An Operator instruction MUST NOT be
   overridden, weakened, or reordered by a framework-native configuration file,
   project-level instruction file, or SDK default.
5. **Policy injection boundary.** Policy text projected into a framework is a
   **constraint**, not content the agent may edit, summarize, or negotiate. An
   adapter MUST NOT expose policy text to framework-native rewriting.
6. **Bypass prevention.** A framework-native instruction mechanism that could
   introduce instructions MellyCore did not authorize MUST be disabled,
   intercepted, or the projection declared unsupported (Runtime §11.2 rule 1).
   Framework-native instruction sources MUST NOT acquire authority by virtue of
   the framework loading them automatically.

## 12. Tool projection

1. A tool is represented to a framework only as a **proposal surface**: a
   framework tool call becomes a **runtime tool proposal** (Runtime §11.3), never
   a direct invocation.
2. **Tool availability in a framework MUST NOT equal tool authorization in
   MellyCore.** Rendering a tool definition into a framework establishes
   visibility only; authorization remains Runtime §21 and Gateway §12/§17/§18.
3. An adapter MUST NOT register a framework-native tool that MellyCore did not
   authorize for that exact run, and MUST NOT leave framework built-in tools
   enabled by default.
4. **Tool substitution is prohibited.** The tool a framework invokes MUST be the
   exact tool MellyCore authorized. Name-similarity, nearest-match, or
   framework-side re-binding MUST fail closed.
5. Unknown or denied tools use the Runtime's existing classes `TOOL_UNKNOWN` and
   `TOOL_DENIED` (Runtime §33). This contract adds no competing tool error.
6. Tool results are **untrusted external content** under Runtime §32 and MUST
   NOT be treated as instructions.
7. Every projected tool MUST be observable per §26.

## 13. Skills projection

1. A Skill declaration (Package §14) MAY be projected as a framework-native
   reusable unit **where a structurally similar concept exists**, as a
   **declaration only**.
2. Projection MUST NOT self-activate a skill. Activation requires the full
   six-state chain of §9.
3. Skill content is untrusted data (§11 rule 2).
4. A skill declaring an undeclared capability fails Package validation before
   any projection is attempted; the bridge MUST NOT repair it.
5. **Full Skill Registry semantics remain deferred** to the future Skill
   Registry (Package §26 item 3). This contract fixes only the projection
   boundary and adds no skill vocabulary.

## 14. Commands projection

This section is deliberately **high-level** and is constrained by an open
upstream finding (§20.4, §36).

### 14.1 Prohibitions (normative)

The Framework Bridge MUST NOT:

1. activate any package-declared command;
2. decide, claim, or transfer command namespace ownership;
3. resolve command collisions;
4. override, shadow, or re-point any reserved command;
5. register a command into any framework's command surface as a consequence of
   projection alone.

### 14.2 Rules

1. A Command Projection MAY represent that a package **declares** a command,
   for observability and compatibility evaluation only.
2. **Command declaration ≠ command activation.** Package §14.1 rule 7 already
   fixes that package-local declaration confers no namespace ownership; this
   contract preserves that boundary unchanged across projection.
3. **This contract defines no protected command classes and enumerates none.**
   The Agent Package Contract's protected-command-class taxonomy is the subject
   of its open Review 002 finding `NEW-P2-03` and remains **unresolved by its
   owner**. This contract therefore MUST NOT translate, evaluate, enumerate, or
   act upon any protected command class, and no normative rule here depends on
   one.
4. Full command namespace ownership, activation, and collision resolution remain
   the **future Command Registry's exclusive concern** (Package §26 item 5).
5. Because commands are never activated by projection, a framework's own command
   or slash-command mechanism MUST NOT be populated from package declarations
   without a separate, future, separately gated authorization.

## 15. Hooks projection

1. **Declaration projection.** A Hook declaration MAY be projected as a
   declaration only, describing the canonical lifecycle event it binds to.
2. **Correspondence.** Hooks bind only to Agent Runtime lifecycle events already
   fixed by Runtime §12 and §26. This contract creates **no** new event
   vocabulary, and MUST NOT bind a hook to a framework-native event that has no
   canonical counterpart.
3. **Activation gate.** A projected hook is **inert**. Activation requires the
   full chain of §9 plus Operator approval for any side-effecting hook (Package
   §11.1 row 11).
4. **Ordering limitations.** Where a framework does not guarantee hook ordering,
   the adapter MUST declare the limitation (§6.1 field 9) and MUST NOT emulate
   ordering it cannot guarantee. Order-dependent safety behavior MUST fail
   closed rather than rely on unspecified ordering.
5. **Failure behavior.** A hook projection failure MUST fail closed. A hook
   whose failure is silently swallowed by a framework is an unsupported
   semantic.
6. **No automatic activation.** A framework mechanism that would auto-discover
   and auto-run hooks MUST be disabled or intercepted (Runtime §11.2 rule 1).
7. Full Hook Registry semantics remain deferred (Package §26 item 4).

## 16. Plugin projection

1. **Metadata projection.** Plugin metadata — identity, revision, bundled
   declaration references, provenance — MAY be projected as metadata only.
2. **Adapter versus plugin (normative).** A **Framework Adapter** implements
   this bridge contract for one framework and is MellyCore-authored
   infrastructure. A **Plugin** is package-declared content bundled by a
   package author (Package §4). They are different concepts with different trust
   treatments and MUST NOT be conflated: a plugin never becomes an adapter, and
   an adapter never acquires a plugin's package-declared permissions.
3. **Availability ≠ approval.** That a plugin is discoverable, listed, or
   present in a framework's plugin surface establishes nothing. Loading requires
   Operator approval plus validation (Package §11.1 row 10).
4. **Isolation expectations.** A projected plugin MUST NOT gain access beyond
   the intersection of its own declared capabilities and the run's authorized
   set. Bundling grants nothing (Package §14).
5. **Failure and rejection.** A plugin that cannot be projected without
   expanding authority MUST be rejected, not degraded.
6. **No automatic loading.** A framework mechanism that would auto-discover and
   auto-load plugins MUST be disabled or intercepted.
7. Full Plugin Registry semantics remain deferred (Package §26 item 6).

## 17. MCP projection

1. **Declaration projection.** A package's MCP Declaration is itself only a
   *reference* to an already-registered MCP server record (Provider Registry
   §24). The projection carries the reference — `mcp_server_id` and
   `tool_contract_revision` — and **never** a registration payload.
2. **Tool, resource, and prompt exposure.** MCP-exposed tools, resources, and
   prompts are subject to §12 in full: exposure is visibility, never
   authorization, and all MCP output carries `output_trust_level: untrusted`
   (Provider Registry §24.2).
3. **Authorization boundary.** Governed entirely by Provider Registry §24.2
   defaults and Gateway §21. This contract adds no MCP authority and no new MCP
   threat surface.
4. **Transport neutrality.** The projection MUST be expressed without reference
   to any transport mechanism. This contract names no transport, no port, no
   socket, no URL, and no process-spawn method.
5. **Secret and credential boundary.** No MCP projection may carry, embed,
   template, or reference credential material. A bridge never holds or forwards
   a credential (Runtime §11.2 rule 2).
6. **No automatic connection.** Projection MUST NOT open, initiate, negotiate,
   or maintain any MCP connection.
7. **No implicit tunnel creation.** Projection MUST NOT create, request, or
   imply any tunnel, relay, proxy, or port-forward.
8. Full MCP Registry semantics remain deferred (Package §26 item 7); server
   records remain Provider Registry's.

## 18. Shared Context projection

1. **Read projection.** Only the context classes a package declares in
   `required_context_classes` (Runtime §10.1) MAY be projected into a framework,
   and only after the Context Gate's own admission rules have been satisfied.
   An unlisted class is unreadable.
2. **Write projection is proposal-only.** A framework MUST NOT obtain
   unrestricted write access to Shared Context. A bridge **never writes Shared
   Context canonical state** (Runtime §11.2 rule 4). Framework-produced context
   becomes at most a **proposal** submitted by the Agent Runtime (Runtime §17.1).
3. **Namespace isolation.** Context projected into a framework MUST be isolated
   per tenant, per environment, and per run. Cross-tenant or cross-run context
   visibility is a `TENANT_ISOLATION_VIOLATION` (Runtime §33).
4. **Provenance.** Every projected record MUST retain its `source_refs`
   provenance, and any proposal returning from a framework MUST carry provenance
   back to the exact `package_revision_id` and `adapter_revision_id`, exactly as
   `CONTEXT_GRAPH_SCHEMA.md` §2.1 already requires.
5. **Context transformation.** Any transformation applied to fit a framework's
   shape MUST be declared and MUST NOT alter meaning, sensitivity
   classification, or provenance.
6. **Lossy projection.** Where projection drops detail, the loss MUST be
   recorded per §24. Sensitivity or provenance loss is **safety-relevant** and
   MUST fail closed.
7. **Execution-local state.** Framework working state, intermediate reasoning,
   and scratch data remain execution-local and MUST NOT be promoted to canonical
   Shared Context automatically.
8. **Return-path validation.** Content returning from a framework MUST be
   re-validated as untrusted external content (Runtime §32) before any admission
   is even proposed. A projected value returning unchanged does **not** bypass
   validation.
9. **Context poisoning prevention.** A framework MUST NOT be able to admit its
   own canonical context, and no projection may create a package-scoped or
   adapter-scoped shortcut around the Context Gate.

## 19. Memory projection

Five memory scopes MUST remain separated. **No scope silently becomes
another.**

| # | Scope | Owner | Rules |
| --- | --- | --- | --- |
| 1 | Framework session memory | Framework, bridge-local | Never canonical, never cross-run, never cross-tenant, never auto-promoted (Runtime §11.3) |
| 2 | Execution-local memory | Agent Runtime, per run | Discarded at run end unless explicitly normalized |
| 3 | Package-declared memory | Agent Package Contract | Declares categories only; reuses Runtime §18's six categories unchanged |
| 4 | MellyCore Shared Context | Shared Context Layer | Proposal-only from a framework (§18) |
| 5 | Durable MellyCore memory | Runtime §18 | Never written by a bridge |

Rules:

1. **Framework memory MUST NOT silently become canonical project memory.**
   Promotion from scope 1 to scope 4 or 5 requires explicit normalization plus
   the owning gate's admission — never a framework's own persistence feature.
2. A framework's automatic memory, history, or checkpoint feature MUST be
   treated as scope 1 regardless of how the framework labels it.
3. A bridge declares **no new memory category** (Runtime §18).
4. Memory contamination across tenants or runs is a safety failure and MUST fail
   closed.

## 20. Lifecycle treatment

### 20.1 Framework-session lifecycle (bridge-owned)

`session_absent` → `session_prepared` (inert) → `session_started` (only in an
authorized mode) → `session_streaming` → `session_completed` /
`session_failed` / `session_cancelled` / `session_lost`.

A Framework Session is bridge-local and non-canonical. **A framework session is
never a MellyCore run**; the run remains Runtime `run_state` (Runtime §12).

### 20.2 Adapter lifecycle (bridge-owned)

`declared` → `validated` (§25) → `eligible` (Bridge Eligibility) →
`deprecated` → `retired`. `retired` is terminal and an `adapter_revision_id` is
never reused. No adapter lifecycle state authorizes execution.

### 20.3 Bridge-evaluation lifecycle (bridge-owned)

`not_evaluated` → `evaluating` → `projection_accepted` /
`projection_rejected` / `projection_partial_declared`. `projection_partial_declared`
records declared, non-safety-relevant loss (§24) and is **not** an authorization.

All three lifecycles above are **typed entity data** under Control Plane §7.1's
allowance. This contract defines **no projection** of any of them onto any
Control Plane §8.1 dimension.

### 20.4 Canonical package lifecycle — explicitly deferred (normative)

**This contract does not define, invent, supply, or work around the Agent
Package Contract's missing package-lifecycle rendering field.**

The Agent Package Contract's Review 002 recorded finding `NEW-P2-01`: its §16
stage 7 and §17.1 direct implementers to §20 for a package-lifecycle rendering
field that its §20.1 does not define. That gap is **owned by the Agent Package
Contract** and remains open.

Accordingly:

1. This contract defines **no** canonical package-lifecycle rendering field.
2. No normative rule in this document depends on one existing.
3. A Framework Adapter MUST NOT render, synthesize, or infer canonical package
   lifecycle state, and MUST NOT substitute a bridge lifecycle (§20.1–§20.3) for
   it.
4. Any future contract requiring canonical package-lifecycle rendering **MUST
   wait** for the Agent Package Contract owner's correction of `NEW-P2-01`.

## 21. Runtime interaction

Eleven distinct stages. Each is a decision boundary; **none is executed,
connected, or implemented by this document.** No stage authorizes execution.

| # | Stage | What it decides | Owner |
| --- | --- | --- | --- |
| 1 | Package discovery | A package revision exists to consider | Package Registry (future) |
| 2 | Package validation | The package passes Agent Package Contract §18 | Package Validator (future) |
| 3 | Bridge compatibility evaluation | The package is expressible in this framework at this adapter revision (`validate_package_compatibility`, Runtime §16) | **This contract** |
| 4 | Adapter selection | Which validated, eligible adapter revision projects this `framework_type` | Agent Runtime |
| 5 | Policy evaluation | Declared capabilities and permissions pass Gateway policy | Integration Gateway |
| 6 | Instantiation eligibility | All prerequisite Runtime §9 states hold | Agent Runtime |
| 7 | Activation gating | Run authorization exists (Runtime §9 state 8, §14 eleven facts) | Agent Runtime / Operator |
| 8 | Run creation | A MellyCore run exists with `run_state` | Agent Runtime |
| 9 | Observation | Normalized events stream (Runtime §26); unmappable events emit an explicit `unmapped` event, never silently dropped | Agent Runtime / Control Plane |
| 10 | Suspension | A run or adapter revision is suspended | Agent Runtime / Operator |
| 11 | Termination | A run ends; cancellation acknowledgement is reported honestly (`CANCELLATION_UNSUPPORTED`, Runtime §27) | Agent Runtime |

Rules:

1. **Adapter selected ≠ runtime authorized.** Stage 4 confers nothing; stage 7
   alone gates whether a run may begin, and it is owned entirely by the already
   accepted Agent Runtime architecture.
2. The bridge participates in stages 3 and 9 and is **consumed** at every other
   stage. It creates no parallel authorization path.
3. Inert runtime modes (Runtime §36) MUST NOT reach a framework runtime
   (`EXECUTION_BLOCKED`, Runtime §16).

## 22. Model and provider routing

1. **The runtime requests; the Model Router decides** (Runtime §23.1). A bridge
   never selects a model.
2. **No direct model access.** A bridge MUST NOT construct a model client from
   its own or a framework's configuration (Runtime §11.2 rule 3). A
   framework-native model request becomes a **routing request** (Runtime §11.3).
3. **No direct provider access and no credentials.** A bridge never holds,
   reads, requests, derives, or forwards a provider credential, and never opens
   a provider connection (Runtime §11.2 rule 2).
4. **Framework configuration MUST NOT bypass canonical routing.** A framework's
   own model name, default model, API-key field, base-URL field, or provider
   client MUST be disabled, intercepted, or the projection declared unsupported.
   A model name present in framework configuration is **not** an authorization.
5. A bridge MUST NOT request a specific model by name as an authorization
   shortcut, and MUST NOT accept a model outside an authorized set (Runtime
   §23.2).
6. **Routing policy, cost policy, provider availability, and Operator
   authorization** are evaluated by their owners; the bridge carries a **routing
   decision reference** (Runtime §23.3), never a decision it made.
7. Fallback prohibitions (Runtime §23.4) apply unchanged: no automatic fallback
   may cross a sensitivity boundary, provider boundary, quality floor, cost
   ceiling, or approved-model set.
8. **Provider selectable ≠ provider authorized.** Provider authorization remains
   Provider Registry §21.1's eight independent facts.

## 23. Error translation

### 23.1 Principles

1. Framework-native errors MUST be translated into MellyCore-owned categories
   **without erasing the original source error**. The original framework error
   text, type, and any framework code MUST be preserved as attached detail.
2. Translation MUST NOT invent detail the framework did not supply (Runtime §16,
   `normalize_failure`).
3. **Error suppression is prohibited.** An unmappable framework failure uses the
   Runtime's existing `BRIDGE_FAILURE_UNCLASSIFIED`, never silence and never a
   coerced success.
4. Outward responses stay coarse; internal records stay precise (Gateway §25.3).

### 23.2 Consumed classes — owned by the Agent Runtime (§33), not re-owned here

| Category | Existing canonical class |
| --- | --- |
| Unsupported semantic | `BRIDGE_UNSUPPORTED_BEHAVIOR` |
| Unmappable framework failure | `BRIDGE_FAILURE_UNCLASSIFIED` |
| Unsupported capability | `UNSUPPORTED_CAPABILITY` |
| Denied permission | `AUTHORIZATION_DENIED` / `CAPABILITY_AUTHORIZATION_DENIED` |
| Unknown framework identifier | `UNSUPPORTED_FRAMEWORK` |
| Package/framework mismatch | `PACKAGE_MISMATCH` |
| Execution attempted in an unauthorized mode | `EXECUTION_BLOCKED` |
| Cancellation unsupported | `CANCELLATION_UNSUPPORTED` |
| Tool unknown / denied | `TOOL_UNKNOWN` / `TOOL_DENIED` |
| Context access denied | `CONTEXT_ACCESS_DENIED` |
| Tenant isolation breach | `TENANT_ISOLATION_VIOLATION` |
| Model unauthorized / none permitted | `MODEL_UNAUTHORIZED` / `NO_PERMITTED_MODEL` |

### 23.3 Bridge-owned classes — genuinely absent from every existing taxonomy

| Class | Triggered by |
| --- | --- |
| `ADAPTER_INVALID` | Adapter identity, revision, or declared boundary fails §25 layers 1–2 |
| `ADAPTER_UNVERIFIED` | `validation_state` absent, `unknown`, or self-asserted (§6.2 rule 3) |
| `BRIDGE_CONTRACT_VERSION_INCOMPATIBLE` | Adapter's `supported_bridge_contract_range` excludes this contract's version (§6.3) |
| `PROJECTION_UNSUPPORTED` | A required projection is outside the adapter's validated `projection_capabilities` (§9.1 state 2) |
| `PROJECTION_LOSS_UNACCEPTABLE` | Safety-relevant projection loss detected (§24) |
| `FRAMEWORK_INITIALIZATION_FAILED` | The framework-local invocation state could not be prepared (`prepare_invocation`, Runtime §16) |
| `CONTEXT_PROJECTION_FAILED` | Context projection could not preserve class bounds, provenance, or sensitivity (§18) |
| `TOOL_PROJECTION_FAILED` | A tool could not be projected without altering identity or authority (§12) |
| `LIFECYCLE_MISMATCH` | A framework lifecycle event has no canonical counterpart and cannot be normalized (§20, §21 stage 9) |

No class above is claimed implemented. This table defines stable names for a
future adapter and runtime to emit, not code that emits them.

## 24. Projection loss and unsupported semantics

### 24.1 Classification

| Class | Meaning | Required behavior |
| --- | --- | --- |
| **Lossless** | Every canonical detail is representable | Proceed |
| **Declared non-safety loss** | Detail lost, none safety-relevant (e.g. a cosmetic label) | MUST be declared and recorded (§26); MAY proceed as `projection_partial_declared` |
| **Safety-relevant loss** | Loss touches capability, permission, approval, trust, provenance, sensitivity, tenant isolation, identity, or cancellation | **MUST fail closed** with `PROJECTION_LOSS_UNACCEPTABLE` |
| **Unsupported semantic** | The concept cannot be expressed at all | **MUST fail closed** with `BRIDGE_UNSUPPORTED_BEHAVIOR` (Runtime §16) |

### 24.2 Rules

1. **The bridge MUST fail closed for safety-relevant semantic loss.** There is
   no default-proceed state.
2. **Semantic-loss concealment is prohibited.** An adapter MUST NOT emulate,
   silently degrade, approximate, or claim success for a behavior it cannot
   perform (Runtime §11.2 rule 5).
3. Loss MUST be declared **before** it is encountered where knowable
   (`report_unsupported_behavior`, Runtime §16), and recorded when encountered.
4. Ambiguity resolves to loss: if it cannot be determined whether a detail
   survived projection, it MUST be treated as lost.
5. Declared non-safety loss MUST NOT accumulate into safety-relevant loss
   unnoticed; each projection is evaluated on its total loss, not incrementally.

## 25. Validation model

### 25.1 Ten layers

1. **Structural validation** — the adapter declaration parses and every §6.1
   field is present and correctly typed.
2. **Adapter identity validation** — `adapter_id` and `adapter_revision_id` are
   stable, opaque, and encode no mutable state; the revision is not retired.
3. **Version compatibility validation** — `supported_bridge_contract_range`,
   `supported_package_contract_range`, and `framework_compatibility_range` are
   internally consistent and admit this contract's version (§6.3).
4. **Capability projection validation** — every projection the adapter claims is
   expressible, and the six capability states of §9 remain separated.
5. **Permission preservation validation** — no projected permission is broader
   than its canonical grant; no flattening (§10.2 rule 4); default-deny intact.
6. **Context projection validation** — class bounds, provenance, sensitivity,
   and tenant isolation survive projection (§18).
7. **Tool projection validation** — projected tool identity is exact; no
   substitution; no unauthorized framework built-ins enabled (§12).
8. **Provenance validation** — `adapter_provenance` is present and internally
   consistent. This layer does **not** claim cryptographic verification exists
   (§6.4).
9. **Safety validation** — no credential material, no undeclared network path,
   no policy-bypass surface, no auto-activation mechanism enabled. Fails closed
   regardless of any other layer's result.
10. **Observability validation** — every §26 projection is producible; an
    adapter that cannot be observed cannot be eligible.

### 25.2 Validation is not authorization

Passing all ten layers establishes **Bridge Eligibility** only. It does **not**
establish instantiation eligibility, activation, run authorization, or
execution. **Validation MUST NOT authorize execution.** A validated adapter is
still denied execution absent every later state of §21.

Correspondingly: `validated ≠ trusted`, `validated ≠ executable`, and
`compatible ≠ enabled`.

## 26. Observability

Information architecture only, inheriting Control Plane §7.1's common entity
contract. No surface, dashboard, or UI is implemented by this document. Every
field below is **typed entity data**, not a Control Plane §8.1 status dimension.

| # | Projection |
| --- | --- |
| 1 | Canonical package ID (`agent_package_id`, `package_revision_id`) |
| 2 | Canonical agent ID (`agent_definition_id`) |
| 3 | Framework ID (`framework_type`, §5) |
| 4 | Adapter ID and version (`adapter_id`, `adapter_revision_id`, `adapter_version`) |
| 5 | Bridge-contract version |
| 6 | Package-contract version **range** the adapter declares (§6.3) |
| 7 | Requested projection |
| 8 | Accepted projection |
| 9 | Rejected semantics, with the reason class from §23 |
| 10 | Denied capabilities, per §9 state that failed |
| 11 | Projection loss, classified per §24.1 |
| 12 | Policy decision reference (Gateway §18) — a reference, never a copy of authority |
| 13 | Runtime handle |
| 14 | Framework session reference |
| 15 | Failure reason, drawn from §23 |
| 16 | Cost-attribution reference — a pointer to a Run Ledger record (AI Operations §5); this contract defines no cost schema |

### 26.1 Rendering rules

1. Bridge fields MUST be labeled as bridge-domain data and MUST NOT be displayed
   as though they were a `lifecycle_status`, `evidence_state`, or
   `approval_state` value.
2. No projection may synthesize a universal "healthy", "active", or green state
   across more than one dimension.
3. `NOT_RUN` / `NOT_IMPLEMENTED` never renders as pass.
4. Rejected semantics and projection loss MUST be rendered, never collapsed into
   a single success boolean.

## 27. Framework-specific projection profiles

### 27.1 Status of every profile (normative)

Each profile in §28–§33 is a **bounded, conceptual, non-implementation
correspondence**, derived solely from repository-owned contracts —
principally Runtime §11.3 and §35 — and from deliberately high-level
architectural reasoning.

**No framework was installed, imported, connected, configured, or executed
during this task. No online documentation was consulted. No SDK behavior is
asserted.** No profile is implemented, tested, installed, available, or
operational, and no profile may be cited as evidence of any framework's actual
behavior.

### 27.2 The outstanding validation obligation (normative, honest)

Runtime §11.3 and §35 state that every per-framework cell "MUST be
independently validated by the future Framework Bridge Contract task before any
bridge is implemented."

**This task cannot discharge that obligation.** Empirical validation requires
installing, importing, and executing each framework, which this task's
authorization explicitly forbids. Accordingly:

1. Runtime §11.3's and §35's cells remain **unvalidated planning positions**.
2. This contract **defines the validation obligation** and assigns it: each
   future per-framework adapter specification (§36) MUST validate its own
   framework's cells with recorded evidence before any adapter for that
   framework may be implemented.
3. No profile below upgrades, confirms, or weakens any Runtime §35 cell.
4. A future task that installs or executes a framework requires its own separate
   Operator authorization and, where it would make an agent execution-capable,
   the Model B reconsideration of migration trigger #6.

### 27.3 Required content per profile

Each profile states: conceptual correspondence; known semantic mismatch;
unsupported or deferred concepts; safety boundary; required adapter
responsibilities.

## 28. `claude_code` profile

**Conceptual correspondence (non-normative, unverified).** Claude Code is
described by Runtime §11.3 as a **process/CLI-session** integration boundary.
The Agent Package Contract §13.2 already records a shape parallel between this
contract's declared asset types and Claude Code counterparts — skill, hook,
slash command, plugin, MCP server reference — and states plainly that the
correspondence is a **naming and shape parallel only**. Project-level
instruction files (of the `CLAUDE.md` kind), settings, and subagents are
framework-native configuration surfaces, not canonical MellyCore artifacts.

**Known semantic mismatch.** A session/process boundary constrains in-process
control and cancellation granularity (Runtime §35). Framework-native
instruction files load automatically by framework convention, which conflicts
with MellyCore's precedence rule (§11.3).

**Unsupported or deferred concepts.** Framework-native persistence is `U1`
(Runtime §35) — MellyCore will not rely on it. Commands remain projection-only
and are never activated (§14). Subagent spawning MUST be re-expressed as a
governed `sub_run` proposal (Runtime §11.3), never a framework-native spawn.

**Safety boundary.** A project instruction file, settings file, or auto-loaded
plugin/MCP entry MUST NOT acquire authority merely because the framework loads
it. Such content is **untrusted data** (§11 rule 2) and MUST NOT displace the
Safety Contract, Operator instruction, or runtime envelope. **Claude Code
remains one projection target, not the canonical architecture.**

**Required adapter responsibilities.** Constrain or disable auto-loaded
instruction, settings, command, hook, plugin, and MCP surfaces; re-express
subagent requests as `sub_run` proposals; declare cancellation as `constrained`;
normalize session events to Runtime §26 events; declare all limitations up front.

## 29. `openai_agents_sdk` profile

**Conceptual correspondence (non-normative, unverified).** Runtime §11.3
describes an **in-process SDK object** boundary: agent run and turn map to
run/step; handoff or agent-transfer maps to a governed handoff envelope; tool
requests map to runtime tool proposals; model requests map to routing requests.
Sessions, guardrails, and tracing are framework-native surfaces whose canonical
counterparts are, respectively, framework session state (§20.1, non-canonical),
policy evaluation (Gateway §17, canonical elsewhere), and Runtime §26 events.

**Known semantic mismatch.** Runtime §35 records that in-process convenience
APIs "must be constrained to prevent direct model/tool paths". A framework
guardrail is **not** a MellyCore policy decision and MUST NOT be counted as one.

**Unsupported or deferred concepts.** Framework-native persistence is `U1`.
Deterministic replay is `RR` — this specification declines to assert a position
without evidence.

**Safety boundary.** Any SDK convenience path that would select a model, invoke
a tool, reach a provider, read memory, write state, or spawn a sub-agent outside
the runtime's decisions MUST be disabled, intercepted, or classified unsupported
(Runtime §11.2 rule 1). No API call is made or claimed by this document.

**Required adapter responsibilities.** Intercept convenience APIs; route every
model request through the Model Router; convert handoffs to governed envelopes;
map tracing to Runtime §26 events without treating framework traces as canonical
evidence.

## 30. `langgraph` profile

**Conceptual correspondence (non-normative, unverified).** Runtime §11.3
describes an **in-process graph-execution** boundary: graph invocation and node
transition map to run/step; a graph edge to another agent node maps to a
governed handoff envelope; tool nodes map to runtime tool proposals.

**Known semantic mismatch — the central one.** Runtime §35 states that "graph
state and checkpointing must not become canonical". **Graph state MUST NOT be
equated with Shared Context.** Graph state is framework-local memory scope 1
(§19) regardless of how durable or structured it appears. Persistence is the one
dimension Runtime §35 rates `C` rather than `U1` for this framework, which
constrains reliance — it does not confer canonicality.

**Unsupported or deferred concepts.** Checkpoints MUST NOT be treated as
canonical run history, evidence, or replay authority. Deterministic replay is
`RR`.

**Safety boundary.** A checkpoint restore MUST NOT resurrect a capability,
permission, approval, or context class that is no longer authorized. State
returning from a checkpoint is untrusted external content (§18 rule 8).

**Required adapter responsibilities.** Keep graph state bridge-local; normalize
node transitions to Runtime §26 events; re-validate all authorization on
resume; declare checkpoint semantics as declared limitations.

## 31. `crewai` profile

**Conceptual correspondence (non-normative, unverified).** Runtime §11.3
describes an **in-process crew/task** boundary: crew kickoff and task map to
run/step; task delegation maps to a governed handoff envelope. Agents are
framework-native participants; crews are framework-native groupings; tools map
to runtime tool proposals; processes are framework-native orchestration.

**Known semantic mismatch.** Runtime §35 states that "crew-level delegation must
be re-expressed as governed handoffs" — a framework's own delegation is not a
MellyCore handoff and confers no authority on the delegate. Streaming is rated
`C` (constrained).

**Unsupported or deferred concepts.** Crew memory is framework-local memory
scope 1 (§19) and MUST NOT become canonical. Framework-native persistence is
`U1`.

**Safety boundary.** A delegated task MUST NOT inherit a capability the
delegating agent held unless that capability is independently authorized for the
delegate — delegation is not capability transfer.

**Required adapter responsibilities.** Convert every delegation into a governed
handoff envelope; keep crew memory bridge-local; declare streaming constraints;
enforce per-agent capability intersection rather than crew-wide union.

## 32. `autogen` profile

**Conceptual correspondence (non-normative, unverified).** Runtime §11.3
describes an **in-process conversational-agent** boundary: chat initiation and
turn map to run/step; speaker transition or group chat maps to a governed
handoff envelope; tools map to runtime tool proposals.

**Known semantic mismatch.** Runtime §35 states that "multi-speaker transitions
must be re-expressed as governed handoffs". A group-chat speaker change is not
an authorization event. Streaming is rated `C`.

**Unsupported or deferred concepts.** Conversation state is framework-local
memory scope 1 (§19). Framework-native persistence is `U1`. Termination
conditions are framework-local heuristics and MUST NOT substitute for Runtime
§27 cancellation or Runtime §12 terminal states.

**Safety boundary.** Message routing between framework participants MUST NOT
move context across a tenant, run, or capability boundary. A framework
termination condition firing is not a MellyCore run completion.

**Required adapter responsibilities.** Re-express speaker transitions as
governed handoffs; bound message routing to the authorized context classes;
normalize termination to Runtime §12 states honestly; declare streaming and
cancellation constraints.

## 33. `mellycore_custom` profile

This is the canonical identifier for the custom-agent profile (§5.2 rule 3).
Runtime §11.3 and §35 rate it as the **narrowest surface by construction**, with
native 1:1 mapping and no known limitations.

**Minimum conformance requirements for a custom framework adapter.** A custom
adapter MUST:

1. declare all twelve §6.1 adapter fields;
2. implement no behavior outside the nine bridge operations of Runtime §16;
3. honor all six normative bridge rules of Runtime §11.2 without exception;
4. preserve all six capability states of §9 without collapsing any;
5. preserve default-deny across all thirteen permission categories of §10.1;
6. treat all framework state as bridge-local (§4.2 rule 3, §19);
7. route every model request through the Model Router (§22) and hold no
   credential;
8. submit Shared Context changes as proposals only (§18);
9. fail closed on safety-relevant projection loss (§24);
10. declare every limitation before it is asked (§6.1 field 9);
11. pass all ten Bridge Validation layers (§25);
12. produce every observability projection of §26.

Being "custom" confers **no** relaxation. `mellycore_custom` is still subject to
every rule in this contract, exactly as Package §13.2 already states for its own
compatibility row.

## 34. Security considerations

| Threat | Mitigation posture |
| --- | --- |
| Framework-native prompt injection | Framework content, tool results, memory, and instruction files are untrusted data (Runtime §31, §32; §11 rule 2); never treated as instructions to the Runtime, adapter, or Validator |
| Adapter impersonation | `adapter_id` + `adapter_revision_id` + `adapter_provenance` (§6) must be validated (§25 layers 2, 8); an adapter cannot self-attest `validation_state` (§6.2 rule 3) |
| Capability amplification | Six-state separation (§9) with intersection semantics; projection is subtractive or equal, never additive (§8.2 rule 1) |
| Permission flattening | Explicitly prohibited (§10.2 rule 4); coarse framework permissions must be constrained to the narrowest declared category or declared unsupported |
| Policy bypass | Any framework convenience path around runtime decisions must be disabled, intercepted, or classified unsupported (Runtime §11.2 rule 1); framework configuration cannot bypass routing (§22.4) |
| Tool substitution | The invoked tool must be exactly the authorized tool; name-similarity and framework-side re-binding fail closed (§12.4) |
| Command or hook activation | Projection never activates either (§14.1, §15.3, §15.6); auto-discovery mechanisms must be disabled |
| Plugin loading | No automatic loading (§16.6); availability ≠ approval (§16.3) |
| MCP credential exfiltration | No projection may carry credential material; a bridge never holds or forwards a credential (§17.5, Runtime §11.2 rule 2); no automatic connection or tunnel (§17.6–§17.7) |
| Context poisoning | Writes are proposal-only and class-bounded; return-path re-validation is mandatory (§18.2, §18.8, §18.9) |
| Memory contamination | Five separated scopes; no silent promotion; cross-tenant or cross-run contamination fails closed (§19) |
| Provider-routing bypass | Model Router decides; no direct model or provider client; framework model configuration is not authorization (§22) |
| Semantic-loss concealment | Emulation, silent degradation, and coerced success are prohibited; safety-relevant loss fails closed (§24.2) |
| Error suppression | Unmappable failures use `BRIDGE_FAILURE_UNCLASSIFIED`, never silence; original framework error is preserved (§23.1) |
| Provenance spoofing | Provenance validation checks internal consistency (§25 layer 8); this contract claims no cryptographic non-repudiation (§6.4) |

## 35. Non-goals

1. Framework Adapter implementation, in any language, for any framework.
2. SDK integration, import, or invocation.
3. Framework installation or environment provisioning.
4. Provider integration or credential configuration.
5. Runtime execution of any kind.
6. Package loading, installation, or activation.
7. Dependency installation or resolution.
8. Command activation.
9. Hook activation.
10. Plugin loading.
11. MCP connection or tunnel creation.
12. Batch Orchestration.
13. Frontend or backend implementation.
14. Deployment.
15. Any push, PR, merge, or destructive git operation.
16. Any MellyTrade interaction, trading, broker, or order behavior.

## 36. Deferred dependencies

Each below is required before the corresponding downstream work may proceed.
None is started or authorized by this document.

| # | Deferred dependency | Owner | Why this contract does not resolve it |
| --- | --- | --- | --- |
| 1 | Agent Package `NEW-P2-01` — missing package-lifecycle rendering field | Agent Package Contract | §20.4: this contract defines no such field and depends on none |
| 2 | Agent Package `NEW-P2-02` — contract-version self-contradiction | Agent Package Contract | §6.3: this contract declares no value as the package contract's current version and uses ranges only |
| 3 | Agent Package `NEW-P2-03` — protected command classes unenumerated | Agent Package Contract, then Command Registry | §14.2 rule 3: this contract defines, enumerates, and evaluates none |
| 4 | Agent Manifest Contract | Future (Package §26 item 1) | §8 fixes only the projection boundary |
| 5 | Capability Contract | Future (Package §26 item 2) | §9.2 rule 6: no capability vocabulary defined here |
| 6 | Skill Registry | Future (Package §26 item 3) | §13.5 |
| 7 | Command Registry | Future (Package §26 item 5) | §14.2 rule 4 |
| 8 | Hook Registry | Future (Package §26 item 4) | §15.7 |
| 9 | Plugin Registry | Future (Package §26 item 6) | §16.7 |
| 10 | MCP Registry | Future (Package §26 item 7) | §17.8 |
| 11 | Package Validation contract | Future (Package §26 item 8) | §21 stage 2 is consumed, not defined |
| 12 | Per-framework adapter specifications (six) | Future, separately gated | §27.2: each MUST discharge its own framework's Runtime §35 validation obligation with recorded evidence |

## 37. Acceptance criteria

This specification task is complete when all of the following hold:

1. All 37 sections are present and each required topic is addressed.
2. Terminology (§2) defines at least the twenty terms the task brief named.
3. No concern is owned by more than one document (§3); every consumed concept
   cites its canonical owner.
4. The projection direction rule (§4.1) is stated and no rule anywhere inverts
   it.
5. Only the six canonical `framework_type` members appear (§5); no seventh
   identifier is introduced.
6. The six capability states (§9) are separated and no stage collapses them.
7. All thirteen permission categories (§10.1) default deny and no framework
   default overrides them.
8. Every projection section states that projection grants nothing.
9. Shared Context projection (§18) is proposal-only and does not weaken the
   Context Gate.
10. The five memory scopes (§19) are separated with no silent promotion.
11. Error translation (§23) consumes existing Runtime classes and introduces
    only genuinely absent bridge classes.
12. Safety-relevant projection loss fails closed (§24).
13. Bridge Validation (§25) explicitly does not authorize execution.
14. All six framework profiles (§28–§33) are present, each labeled
    non-implementation and unverified.
15. The Runtime §35 validation obligation is honestly recorded as **not
    discharged** (§27.2).
16. All fifteen security threats (§34) are addressed with a section-citing
    mitigation.
17. Non-goals (§35) and deferred dependencies (§36) are internally consistent
    with the rest of the document.
18. **P2 containment holds:** the document defines no package-lifecycle
    rendering field, declares neither package contract version 1.0 nor 1.1 as
    canonically current, and defines no protected command classes — and no
    normative rule depends on any of the three.
19. No implementation, execution, installation, integration, connection,
    credential, or deployment is claimed anywhere (§1.4).

## 38. References

### 38.1 Repository (canonical)

- `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`
- `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]`
- `[[../research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002]]` (research)
- `[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]`
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`
- `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]`
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]`
- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`
- `shared_context/CONTEXT_GRAPH_SCHEMA.md`,
  `shared_context/context_provenance/**`
- `shared_context/MODEL_ROUTING.md`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md`

### 38.2 External

**None.** No external standard, SDK version, API, or online documentation was
consulted or is claimed. Framework treatment derives solely from
repository-owned contracts and deliberately high-level conceptual reasoning
(§27.1).

## 39. Amendment and supersession

This document may be amended only additively unless a major
`bridge_contract_version` bump is explicitly declared. An amendment MUST NOT
weaken any rule in §3.1's precedence chain, and MUST NOT resolve, restate, or
work around any deferred dependency of §36 that belongs to another owner. This
document does not supersede, rename, or absorb any canonical owner document
cited in §3 or §38.1; every citation remains that document's unmodified,
unweakened text unless a separate, explicitly authorized amendment task states
otherwise.
