# MellyCore Agent Runtime Architecture Spec

**Task ID:** MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001
**Contract ID:** MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_001
**Version:** 1.0
**Status:** ACCEPTED as an architecture-level specification only. **This status does not authorize Agent Runtime implementation, framework bridge implementation, agent execution, agent-framework installation or connection, model-provider calls, tool execution, provider authentication, credential configuration, MCP or integration-fabric connection, persistence, queueing, frontend work, or deployment.** It fixes the architecture a later, separately authorized implementation must satisfy.
**Scope:** Defines how MellyCore AIOS represents, coordinates, isolates, observes, and governs agents implemented with Claude Code, the OpenAI Agents SDK, LangGraph, CrewAI, AutoGen, and custom MellyCore-compatible agents — covering identity, packaging, lifecycle, execution envelopes, framework bridges, shared-context and memory access, handoffs, model routing, tool and provider governance, approvals, run ledger and provenance, tracing, cost, cancellation, retry, reconciliation, isolation, human oversight, observability information architecture, and fail-closed behavior.

---

## 1. Title and status

### 1.1 Status meaning (normative)

This is an **accepted architecture-level specification**, in the same sense as
`[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`,
`[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`, and
`[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]`.

Acceptance means only that the boundaries, identities, lifecycle, envelopes,
access rules, taxonomies, and containment behavior below are the canonical
target a future Agent Runtime must satisfy, and that any future implementation
deviating from them is non-conforming.

Acceptance does **not** mean any of: an implemented Agent Runtime; an
implemented framework bridge; an installed agent framework SDK; an executed
agent; a routed model request; an invoked tool; a connected provider; a
configured credential; a persisted run; or a deployment.

This specification **does not reorder, reprioritize, or reinterpret** the
global higher-priority task pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`. The Agent Runtime is a
separate product-development track.

### 1.2 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Agent Runtime implementation | `NOT_IMPLEMENTED` — no runtime process, scheduler, coordinator, or state machine code exists |
| Agent Registry implementation | `NOT_IMPLEMENTED` |
| Agent packages | `NONE_EXIST` — no package, manifest, or package store exists |
| Framework bridges | `NOT_IMPLEMENTED` for every framework in Section 11 |
| Agent framework SDKs | `NOT_INSTALLED` — Claude Code, OpenAI Agents SDK, LangGraph, CrewAI, and AutoGen are absent from this repository and its reviewed environment |
| Agents executed | **Zero.** No agent has ever been started, resumed, cancelled, or completed under this architecture |
| Model-provider calls | `NEVER_PERFORMED` |
| Tool invocations | `NEVER_PERFORMED` |
| Provider connections | `NOT_CONNECTED`; credentials `NOT_CONFIGURED` |
| Shared Context bridge | `NOT_IMPLEMENTED` |
| Memory backend | `NOT_IMPLEMENTED` |
| Run Ledger persistence | `NOT_IMPLEMENTED` — `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5 remains logical contract only |
| Queue / scheduler | `NOT_IMPLEMENTED` |
| Operator Console surfaces | `NOT_IMPLEMENTED` — Section 34 defines information architecture only |
| Evidence class for every flow below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by a documentation task. A validator that did not
run records `NOT_RUN`, never a defaulted pass.

### 1.3 Relationship to migration trigger #6

`shared_context/PROJECT_STATE.md`'s Model A contract lists nine blocking
migration triggers. Trigger **#6, "first execution-capable agent,"** is
directly implicated by any future Agent Runtime implementation that can start a
real agent. This specification does not cross that trigger, because it
implements nothing. Any future task that would make an agent execution-capable
is **blocked** until the Model B reconsideration required by that contract is
separately completed. Triggers #1 (first backend endpoint), #4 (first runtime
secret), #5 (first live provider connection), and #7 (first external
write-capable integration) are likewise implicated by later phases of this
architecture and are not crossed here.

## 2. Purpose

MellyCore AIOS is a local-first, operator-controlled AI Operations Observatory.
Its controlled improvement loop is
`observe → analyze → recommend → approve → implement → validate → record`.

Agents are the mechanism by which that loop is expected to do work. Today
MellyCore has an accepted **provider** foundation (Registry, Gateway, adapter
scaffold, one offline Cloudflare adapter) and an accepted **control-plane**
foundation (entities, statuses, modules, approvals), but **no accepted
architecture for the agents themselves**. Without one, each framework
integration would invent its own lifecycle, its own context access, its own
retry semantics, and its own idea of what "done" means — and the safety
separations the provider track spent five review cycles establishing would be
re-collapsed at the agent layer.

This specification supplies the missing layer: **one framework-neutral control
and coordination architecture** that every supported framework must be adapted
to, rather than adapted around.

## 3. Authority and source contracts

Precedence, extending
`[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §33:

```text
shared_context/SAFETY_CONTRACT.md
  > Enterprise-Provider ADR
  > Provider Registry contract
  > Integration Gateway contract
  > this Agent Runtime architecture
  > framework-specific bridge contract (stricter only)
  > agent package declaration (stricter only)
  > tenant policy (stricter only)
```

This specification is a **mandatory floor**. A framework bridge, agent package,
or tenant policy may add stricter requirements. It may not weaken any
requirement here; a weaker rule is void. Conflicts fail closed, the stricter
interpretation governs while unresolved, and affected runs are denied.

Consumed as canonical, reused rather than restated:

| Source | What this specification reuses |
| --- | --- |
| `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` | §7.1 common entity contract; §7.2 entity catalogue; §8 six orthogonal status dimensions; §9.3–9.7 module contracts; §16 approval contract; §17 secrets boundary; §18 provenance; §19 failure and unknown states |
| `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` | §7.5 three acting-identity types; §11 scope rules; §12.1 authentication targets; §13.2 nine credential-profile classes; §15.1 R0–R5 risk tiers; §21.1 eight independent facts |
| `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` | §6 trust model; §9 acting-identity chain; §17 policy-evaluation order; §18 approval binding; §25 error taxonomy; §26 retry and `INDETERMINATE` reconciliation; §27 concurrency; §28 external content; §29 two-stage audit; §32 seventeen-item runtime-enablement gate |
| `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` | §5 Unified Run Ledger record and token/cost semantics; §5.8 `operator_approved` is not authority; §9 approval contract; §10 provenance and sensitivity |
| `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` | Tenant isolation, identity/credential model, capability/risk/approval model, external-content posture |
| `[[../research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002]]` | Findings `P2-03`, `P2-04`, `P3-01`, carried forward as Sections 8.3, 22.5, and 33 constraints |
| `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md` | Safety boundaries, Model A migration triggers, live sequencing |

## 4. Scope

In scope: the runtime boundary; canonical agent and run identity; the
definition/package/instance separation; expectations placed on a future Agent
Package Contract; the framework-neutral bridge boundary and six framework
positions; the run lifecycle; run/attempt/step/sub-run/retry/replay semantics;
the eleven authorization facts; the execution envelope; Shared Context and
memory access; context-flow tracing; the handoff model; tool and provider
governance; the Model Router boundary; cost and token accounting; the Run
Ledger relationship; the normalized event model; cancellation, timeout, retry,
and reconciliation; concurrency and isolation; human-in-the-loop; the security
and threat model; external-content posture; the runtime error taxonomy;
operator observability information architecture; runtime modes; the inert v1
scaffold boundary; deterministic scenarios; and implementation sequencing.

Out of scope: everything in Section 5 and Section 39.

## 5. Explicit non-authorizations

This specification authorizes **none** of the following, and nothing in it may
be read as authorizing them:

1. Agent Runtime implementation of any kind.
2. Framework bridge implementation of any kind.
3. Installation, vendoring, or dependency declaration of Claude Code, the
   OpenAI Agents SDK, LangGraph, CrewAI, AutoGen, or any agent framework.
4. Execution of any agent, sub-agent, workflow, graph, crew, or conversation.
5. Any model-provider API call, including free-tier, trial, or read-only calls.
6. Any tool invocation, including local, read-only, and fixture-backed tools
   that reach outside the process.
7. Any provider connection, authentication, credential configuration,
   credential verification, OAuth flow, or token creation.
8. Any MCP server connection or MCP execution.
9. Any integration-fabric connection or webhook registration.
10. Persistence, database, or queue implementation.
11. Backend or frontend implementation.
12. Dependency installation, workflow YAML, release, or deployment.
13. Any push, pull request, merge, or remote branch.
14. Any MellyTrade interaction, trading, broker, or order behavior.

## 6. Design principles

1. **Coordination, not capability.** The runtime decides *whether* and *in what
   bounded form* something may happen; other systems own *how*.
2. **Every separation stays separated.** No field, flag, or convenience API may
   merge two independent facts.
3. **Fail closed on absence.** Missing, `unknown`, expired, malformed, or
   unresolved input denies. There is no default model, provider, tool,
   credential, identity, tenant, permission, or budget.
4. **Framework support is not framework execution.** Representing a framework's
   feature never enables it.
5. **Untrusted by default.** Model output, tool results, provider responses,
   file and web content, agent-generated code, plans, prompts, tool arguments,
   and other agents' output are data, never instructions to the runtime.
6. **Evidence over assertion.** A recorded state is a claim about evidence, not
   a claim about the world. Unknown external outcomes stay unknown.
7. **Append-oriented audit.** Corrections supersede; they never erase.
8. **Canonical bytes, not object identity.** Identity and digests derive from
   normalized byte representations, never from arbitrary object behavior.
9. **Operator is the only authority.** Agents propose; operators approve.
10. **MellyCore only.** MellyTrade, trading, broker, and order behavior are
    outside this boundary.

## 7. Runtime boundary

### 7.1 Definition

The **Agent Runtime** is a control and coordination layer. It decides which
agent may run, under which envelope, with which permissions, against which
context, with which budget, and it records what happened. It is the single
place where a run's identity, lifecycle, authorization, and evidence live.

### 7.2 What the Agent Runtime must not own

The Agent Runtime **must not own**:

- provider credentials, credential selection, or credential material of any
  kind;
- provider transport, endpoints, retries at the provider wire, or provider
  session state;
- model-provider SDK credentials or SDK-level configuration;
- canonical Shared Context truth;
- permanent trust in any external tool;
- deployment or hosting infrastructure;
- MellyTrade execution, or any trading, broker, or order behavior.

Additionally, it must not own the Run Ledger's canonical record definition
(that is `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5), the status
vocabulary (Control Plane §8), the eight provider facts (Registry §21.1), or
the provider policy-evaluation order (Gateway §17).

### 7.3 Adjacent systems and their relationships

| System | Owner | Agent Runtime's relationship |
| --- | --- | --- |
| Agent Registry | Future, separate | Runtime **reads** registered agent records; never registers, never edits |
| Agent Package Store | Future, separate | Runtime **references** a verified, installed package revision; never verifies, never installs |
| Framework Bridges | Future Framework Bridge Contract | Runtime **drives** bridges through one neutral interface; bridges never call the runtime's internals or bypass its policy |
| Shared Context Layer | `shared_context/**`, Context Gate, Control Plane §9.3 | Runtime **reads snapshots** and **submits proposals**; never writes canonical state |
| Memory Layer | This specification (categories), future Shared Context Bridge (mechanism) | Runtime **scopes and isolates**; never promotes memory to canonical automatically |
| Model Router | Future, separate (Control Plane §9.2 Routing Policy Center is its control surface) | Runtime **requests** a routing decision and **consumes** an explained decision; never selects a model itself |
| Provider Registry | Registry contract | Runtime **reads** the eight facts; never registers, never mutates |
| Integration Gateway | Gateway contract | Runtime **submits** bounded operation proposals; never bypasses, never proxies |
| Tool Gateway | Future, separate (this specification fixes its boundary in Section 21) | Runtime **submits** validated tool requests; never invokes a tool directly |
| Run Ledger | AI Operations Intelligence §5 | Runtime **emits** append-only records; never rewrites |
| Cost Observatory | Control Plane §9.7 | Runtime **emits** estimates and actuals separately; never reconciles billing |
| Operator Console | Control Plane §9.10, §12 | Runtime **exposes** read models and **waits** on operator decisions |
| Audit and provenance | Gateway §29, Control Plane §18, `shared_context/context_provenance/**` | Runtime **appends**; never redacts history |

### 7.4 Ownership matrix (canonical owners, reused not re-decided)

| Concern | Canonical owner |
| --- | --- |
| Provider access, credentials, provider policy order | `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` |
| Provider records, the eight facts, acting identities, credential classes | `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` |
| Model routing control surface, status dimensions, entity catalogue, approval binding | `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` |
| Shared Context admission, provenance, sensitivity | `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`, `shared_context/context_provenance/**` |
| Run Ledger record, token and cost semantics | `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5 |
| Permissions and approval semantics | Control Plane §16 + Gateway §18 |
| Task state and live sequencing | `shared_context/RUN_QUEUE.md`, echoed in `shared_context/AGENT_HANDOFF.md` |
| Agent packages | **Deferred** — future Agent Package Contract (Section 10) |
| Agent runtime coordination | **This specification** |

## 8. Canonical identity model

### 8.1 Identifier catalogue

| Identifier | Identifies | Assigned by | Stability |
| --- | --- | --- | --- |
| `agent_definition_id` | A logical agent, independent of packaging | Agent Registry | Permanent |
| `agent_package_id` | A packaging line for one definition | Agent Package Store | Permanent |
| `package_revision_id` | One exact immutable package revision | Agent Package Store | Permanent; never reused, never re-pointed |
| `installed_agent_id` | One installation of one package revision into one tenant and environment | Agent Registry | Permanent for the installation's life |
| `runtime_instance_id` | One runtime coordinator instance | Agent Runtime | Permanent per instance |
| `run_id` | One logical unit of agent work | Agent Runtime | Permanent |
| `attempt_id` | One execution attempt of one run | Agent Runtime | Permanent; new per attempt |
| `step_id` | One ordered step within one attempt | Agent Runtime | Permanent |
| `sub_run_id` | One delegated child run | Agent Runtime | Permanent; also a `run_id` |
| `handoff_id` | One handoff envelope | Agent Runtime | Permanent |
| `context_snapshot_id` | One immutable context snapshot | Shared Context Layer | Permanent |
| `tool_invocation_id` | One tool request/result pair | Tool Gateway | Permanent |
| `model_invocation_id` | One model request/response pair | Model Router | Permanent |
| `provider_operation_proposal_id` | One bounded provider operation proposal | Agent Runtime | Permanent |
| `trace_id` | One end-to-end causal trace | Agent Runtime | Permanent |

### 8.2 Identifier rules (normative)

1. **Immutable.** An identifier's value never changes and is never reassigned.
2. **Tenant-scoped.** Every identifier resolves only within one tenant. Cross-
   tenant resolution is denied, not merely empty.
3. **Opaque.** Identifiers MUST NOT encode mutable state, permissions,
   sensitivity, model names, provider names, or authorization outcomes
   (Control Plane §7.1).
4. **No fuzzy matching.** Lookup is exact-match only. Prefix, suffix,
   case-insensitive, whitespace-tolerant, Unicode-normalizing, similarity, and
   "nearest" resolution are prohibited at every trust boundary.
5. **No runtime aliases.** Human-facing display names and slugs are labels.
   They are never accepted as identifiers in an envelope, handoff, approval
   binding, ledger record, or audit record.
6. **Revision identity is preserved.** `package_revision_id` is carried through
   every envelope, handoff, approval, ledger record, and audit record. A run
   authorized against one revision is never executed against another
   (Scenario 31).
7. **No `repr()`-derived identity.** See Section 8.3.

### 8.3 Canonical serialization, type discipline, and digests

This section carries forward Cloudflare Review 002 finding **`P2-03`** — a
Python `str` subclass passed fixture validation, escaped normalization into
normalized reference fields, and, because the digest was computed over
`repr()`, produced a demonstrated collision between two different fixtures.

Normative rules at every Agent Runtime trust boundary:

1. **Exact built-in primitive types only.** A value declared as a string,
   integer, boolean, or byte string MUST be exactly that built-in type.
   `type(value) is str` — not `isinstance` — is the required discipline for
   string-typed fields, and the analogous exact-type check applies to every
   other primitive.
2. **Subclasses are rejected or canonically converted.** A primitive subclass
   MUST be either rejected with `INVALID_CANONICAL_TYPE` or converted to an
   exact built-in primitive **before** any normalization, comparison,
   reference construction, or digest input. Conversion is explicit and
   recorded; it is never implicit.
3. **Serialization is independent of object behavior.** Canonical
   serialization MUST NOT call `repr()`, `str()`, `__format__`, `__hash__`,
   `__eq__`, or any other overridable object protocol on an untrusted value.
   It emits a deterministic encoding of the value's exact canonical type and
   its normalized bytes.
4. **Deterministic hashing over normalized bytes.** Every digest is computed
   over a UTF-8 (or explicitly declared) byte encoding of the canonical
   serialization, using a collision-resistant algorithm (SHA-256 or stronger).
5. **Type-tagged fields.** Wherever a field could hold more than one canonical
   type, or where a string could be confused with a number, boolean, null, or
   binary value, the serialization carries an explicit type tag so that two
   distinct inputs cannot serialize identically (Scenario 28).
6. **Canonical form is total and unambiguous.** Map key order, numeric form,
   string normalization form, absent-versus-null distinction, and container
   framing are fixed by the canonical encoding, so exactly one byte sequence
   corresponds to one logical value and one logical value to one byte
   sequence.
7. **No identity from arbitrary representations.** Run fingerprints, context-
   block hashes, artifact references, handoff envelopes, tool-result
   identities, model-response identities, audit records, replay records,
   provenance, deduplication keys, cache keys, and idempotency keys MUST NOT
   be derived from arbitrary object representations.
8. **Digest collisions are security events.** Two distinct canonical byte
   sequences producing one digest, or two distinct logical values producing one
   canonical byte sequence, is a `DIGEST_COLLISION_SUSPECTED` security event:
   both inputs are quarantined, the affected records are marked
   `evidence_state:unknown`, and dependent runs are blocked pending operator
   review (Scenario 28).

These rules apply, without exception, to: run fingerprints, context-block
hashes, artifact references, handoff envelopes, tool-result identities,
model-response identities, audit records, and replay records.

## 9. Agent definition versus runtime instance

Nine separated states. **No state implies the next.** Each is established,
evidenced, and revoked independently.

| # | State | Meaning | Established by | Absence means |
| --- | --- | --- | --- | --- |
| 1 | **Agent defined** | A definition record exists | Agent Registry | Unknown agent — deny |
| 2 | **Package artifact exists** | A build artifact exists for a revision | Agent Package Store | No artifact — deny |
| 3 | **Package verified** | Integrity, provenance, and declaration checks passed | Future Agent Package Contract | Unverified — deny |
| 4 | **Package installed** | The verified revision is installed for one tenant and environment | Agent Registry | Not installed — deny |
| 5 | **Agent registered** | A conforming, current agent record binds definition to installed revision | Agent Registry | Unregistered — deny |
| 6 | **Runtime enabled** | Explicit runtime enablement for this tenant and environment | Operator, recorded | Not enabled — deny |
| 7 | **Agent instantiated** | A runtime instance holds an isolated agent instance | Agent Runtime | Nothing to run — deny |
| 8 | **Run authorized** | A valid authorization exists for this exact run | Operator/policy, recorded | Unauthorized — deny |
| 9 | **Run active** | The run is executing under an accepted envelope | Agent Runtime | No execution evidence |

Prohibited designs: any `ready`, `enabled`, `installed`, `ok`, `healthy`, or
`status: active` field standing for two or more of these; any derivation of a
later state from an earlier one; any UI or API that presents them as one
progress bar without exposing each independently.

## 10. Agent package relationship

The **Agent Package Contract is deferred** to its own task. This section fixes
only what the Agent Runtime requires from it, so the two cannot drift.

### 10.1 Required package metadata (minimum)

| Field | Purpose | Fail-closed behavior when absent or invalid |
| --- | --- | --- |
| `agent_definition_id` | Canonical agent identity | Deny — `PACKAGE_MISMATCH` |
| `package_revision_id` | Exact immutable revision | Deny |
| `framework_type` | Exactly one value from Section 11's closed set | Deny — `UNSUPPORTED_FRAMEWORK` |
| `entrypoint_reference` | Opaque, bridge-interpreted entry reference | Deny |
| `declared_capabilities` | Closed set of capability classes the agent claims | Deny; an undeclared capability is never granted |
| `declared_tools` | Exact tool contract identifiers and revisions | Deny; an undeclared tool is never invocable |
| `required_context_classes` | Context classes the agent needs to read | Deny; unlisted classes are unreadable |
| `produced_context_classes` | Context classes the agent may propose | Deny; unlisted classes are unproposable |
| `model_requirements` | Capability class, context window, modality, quality floor | Deny; never a model name binding |
| `permission_requirements` | Permissions the agent requires | Deny; requirement is never a grant |
| `provider_requirements` | Provider capability IDs the agent may propose against | Deny; requirement is never authorization |
| `resource_limits` | Declared step, depth, wall-clock, token, and cost ceilings | Deny; runtime limits are the stricter of package and policy |
| `supported_environments` | Environments the revision is valid in | Deny |
| `sensitivity_posture` | Maximum sensitivity the agent may handle, from the canonical vocabulary | Deny; defaults never widen |
| `external_content_posture` | How the agent handles untrusted content | Deny |
| `cancellation_support` | Declared, bridge-corroborated cancellation semantics | Treated as unsupported — `constrained` (Section 27) |
| `deterministic_replay_support` | Whether replay is meaningful for this agent | Treated as unsupported |
| `package_provenance` | Source, build, signer, digest, and verification evidence | Deny — `PACKAGE_UNVERIFIED` |

### 10.2 Rules

1. A declaration is a **requirement statement, never a grant**. Every declared
   capability, tool, context class, permission, and provider requirement must
   still be independently authorized (Section 14).
2. Declarations are **intersected downward** with tenant policy, agent record,
   run authorization, and gateway limits. The effective permission set is the
   intersection, never the union.
3. **Executable package loading is out of scope here.** This specification
   defines no loader, no sandbox mechanism, no import path, and no unpacking
   behavior.
4. A package revision's declarations are **immutable**. A changed declaration
   is a new revision, and invalidates approvals bound to the old one
   (Scenario 31).

## 11. Supported framework model

### 11.1 The closed framework set

`framework_type` is a closed vocabulary with exactly six members:
`claude_code`, `openai_agents_sdk`, `langgraph`, `crewai`, `autogen`,
`mellycore_custom`. An unknown value denies with `UNSUPPORTED_FRAMEWORK`. There
is no `other`, `generic`, or `auto` member.

### 11.2 One framework-neutral bridge interface

Every framework is reached through **one** bridge interface. A bridge is an
adapter *into* the runtime's model, not a passthrough *out of* it.

Normative rules binding on every bridge:

1. **No policy bypass.** A framework-native convenience API that would select a
   model, invoke a tool, reach a provider, read memory, write state, or spawn a
   sub-agent outside the runtime's decisions MUST be disabled, intercepted, or
   the framework MUST be classified `unsupported in v1` for that behavior.
2. **No direct provider access.** A bridge never holds, reads, requests,
   derives, or forwards a provider credential, and never opens a provider
   connection.
3. **No direct model access.** A bridge never constructs a model client from
   its own configuration; model calls are satisfied only through the Model
   Router boundary (Section 23).
4. **No canonical writes.** A bridge never writes Shared Context canonical
   state.
5. **Honest capability reporting.** A bridge MUST report unsupported behavior
   explicitly (`BRIDGE_UNSUPPORTED_BEHAVIOR`) rather than emulating it,
   silently degrading it, or claiming success.
6. **Framework-native state is not canonical.** Framework threads, checkpoints,
   graph state, crew memory, and conversation history are bridge-local until
   explicitly normalized and admitted.

### 11.3 Per-framework integration boundaries

Each row below is an **architectural planning position** derived from each
framework's publicly described design characteristics. **No framework was
installed, imported, connected, or executed during this task**, so no row is a
verified capability test. Every row MUST be independently validated by the
future Framework Bridge Contract task before any bridge is implemented.

| Dimension | `claude_code` | `openai_agents_sdk` | `langgraph` | `crewai` | `autogen` | `mellycore_custom` |
| --- | --- | --- | --- | --- | --- | --- |
| Integration boundary | Process/CLI-session boundary | In-process SDK object boundary | In-process graph-execution boundary | In-process crew/task boundary | In-process conversational-agent boundary | Defined by MellyCore; narrowest boundary |
| Lifecycle translation | Session start/turn/stop mapped to run/step | Agent run and turn mapped to run/step | Graph invocation and node transition mapped to run/step | Crew kickoff and task mapped to run/step | Chat initiation and turn mapped to run/step | Native — mapped 1:1 |
| Tool-call translation | Framework tool request → runtime tool proposal | Same | Same | Same | Same | Native runtime tool proposal |
| Model-call translation | Framework model request → routing request | Same | Same | Same | Same | Native routing request |
| Handoff translation | Sub-agent request → `sub_run` proposal | Handoff/agent-transfer → handoff envelope | Graph edge to another agent node → handoff envelope | Task delegation → handoff envelope | Speaker transition / group chat → handoff envelope | Native handoff envelope |
| Cancellation limitation | `constrained` — cooperative at best; in-flight external effects not guaranteed stopped | `constrained` | `constrained` | `constrained` | `constrained` | `architecturally supported` — designed for cooperative cancellation with acknowledgement |
| State persistence posture | Framework-local; not canonical | Framework-local; not canonical | Checkpointer state is framework-local; not canonical | Crew state is framework-local; not canonical | Conversation state is framework-local; not canonical | Runtime-owned; still not canonical Shared Context |
| Streaming posture | Normalized to runtime events; partial output is never a completion claim | Same | Same | Same | Same | Same |
| Framework-native memory | **Restricted.** Never canonical, never cross-run, never cross-tenant, never auto-promoted | Same | Same | Same | Same | Same |
| Direct provider access | **Prohibited** | **Prohibited** | **Prohibited** | **Prohibited** | **Prohibited** | **Prohibited** |
| Direct credential access | **Prohibited** | **Prohibited** | **Prohibited** | **Prohibited** | **Prohibited** | **Prohibited** |

## 12. Runtime lifecycle

### 12.1 Terminology reconciliation (normative)

Control Plane §8.1 fixes six orthogonal status dimensions, and §7.1 states that
domain fields "remain typed entity data and are not additional status
dimensions." Accordingly:

- `run_state` is a **typed entity field owned by this specification**, not a
  seventh status dimension.
- Its machine identity is the field-qualified pair, e.g.
  `{field: "run_state", value: "blocked"}`. An unqualified raw value is not a
  valid contract.
- The same human labels may legally appear in `lifecycle_status` and
  `run_state` without ambiguity, exactly as Control Plane §8.1 permits across
  dimensions.
- An agent run additionally carries the applicable canonical dimensions:
  `lifecycle_status`, `evidence_state`, `freshness_state`, and
  `approval_state`.

### 12.2 The seventeen run states

| `run_state` | Terminal? | Meaning | Projects to `lifecycle_status` |
| --- | --- | --- | --- |
| `proposed` | No | A run has been requested; nothing validated | `draft` |
| `validated` | No | Envelope, package, and declarations are structurally valid | `planned` |
| `authorized` | No | All eleven facts (Section 14) hold | `ready` |
| `queued` | No | Admitted for scheduling; not started | `queued` |
| `starting` | No | Instantiation and bridge preparation in progress | `active` |
| `running` | No | The agent is executing a step | `active` |
| `waiting_for_model` | No (waiting) | Blocked on a routing decision or model response | `active` |
| `waiting_for_tool` | No (waiting) | Blocked on a tool result | `active` |
| `waiting_for_agent` | No (waiting) | Blocked on a handoff or sub-run | `active` |
| `waiting_for_operator` | No (waiting) | Blocked on a human decision | `blocked` |
| `cancellation_requested` | No | Cancellation requested; not yet acknowledged or settled | `active` |
| `reconciliation_required` | No | An external outcome is unknown and must be reconciled | `blocked` |
| `completed` | **Yes** | The run finished and its output contract was satisfied | `completed` |
| `failed` | **Yes** | The run finished without satisfying its output contract | `failed` |
| `cancelled` | **Yes** | Cancellation completed with **no** unknown external effect | `cancelled` |
| `timed_out` | **Yes** | A limit was reached with **no** unknown external effect | `failed` |
| `blocked` | **Yes** | The run was refused and will not proceed under this authorization | `blocked` |

The four non-terminal **waiting** states are `waiting_for_model`,
`waiting_for_tool`, `waiting_for_agent`, and `waiting_for_operator`.
`cancellation_requested` and `reconciliation_required` are non-terminal
**pending** states, not waiting states.

### 12.3 Allowed transitions

| From | Allowed to |
| --- | --- |
| `proposed` | `validated`, `blocked` |
| `validated` | `authorized`, `blocked` |
| `authorized` | `queued`, `blocked` |
| `queued` | `starting`, `cancellation_requested`, `blocked`, `timed_out` |
| `starting` | `running`, `failed`, `cancellation_requested`, `blocked` |
| `running` | `waiting_for_model`, `waiting_for_tool`, `waiting_for_agent`, `waiting_for_operator`, `cancellation_requested`, `reconciliation_required`, `completed`, `failed`, `timed_out`, `blocked` |
| `waiting_for_model` | `running`, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` |
| `waiting_for_tool` | `running`, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` |
| `waiting_for_agent` | `running`, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` |
| `waiting_for_operator` | `running`, `cancellation_requested`, `failed`, `timed_out`, `blocked` |
| `cancellation_requested` | `cancelled`, `reconciliation_required`, `failed`, `completed` |
| `reconciliation_required` | `completed`, `failed`, `cancelled`, `blocked` |
| `completed`, `failed`, `cancelled`, `timed_out`, `blocked` | **none** |

`cancellation_requested → completed` is legal and required for the honest case
in which the run finished before cancellation took effect. It is never used to
report a cancelled run as successful.

### 12.4 Forbidden transitions (normative)

1. Any transition out of a terminal state.
2. `proposed`, `validated`, or `queued` directly to `running`.
3. Any transition to `authorized` without all eleven facts of Section 14.
4. `cancellation_requested → cancelled` when any external effect is unknown;
   the required transition is `reconciliation_required`.
5. `waiting_for_*` or `running` → `timed_out` when any external effect is
   unknown; the required transition is `reconciliation_required`.
6. `reconciliation_required` → any terminal state without a recorded
   reconciliation outcome.
7. Any transition asserted by an agent, a model, a tool result, a bridge, or
   external content. Only the runtime transitions a run.
8. Any transition to `completed` when a sub-run, handoff, or required
   validation is unresolved.
9. Any transition performed without the evidence record of Section 12.5.

### 12.5 Transition evidence

Every transition appends an immutable record carrying: `run_id`, `attempt_id`,
`from_state`, `to_state`, `reason_code` (Section 33), `actor` (exactly one of
`runtime`, `operator`, `policy`, `bridge_report`, `scheduler` — never `agent`,
`model`, `tool`, or `provider`), `observed_at`, `recorded_at`,
`evidence_refs`, `trace_id`, and the canonical digest of the transition input
(Section 8.3).

`observed_at` is when the runtime observed the condition; `recorded_at` is when
the record was durably appended. They are separate fields and are never merged.
When `observed_at` cannot be established it is `null`, never substituted with
`recorded_at`.

## 13. Run, attempt, step, sub-run, retry, replay

| Concept | Definition |
| --- | --- |
| **Logical run** | One unit of agent work with one `run_id`, one authorization, one budget envelope, and one output contract |
| **Execution attempt** | One bounded execution of a run with one `attempt_id`. A run has one or more attempts |
| **Step** | One ordered unit within an attempt with one `step_id` — a model turn, a tool request, a context read, a handoff, or an operator wait |
| **Sub-run** | A delegated child run with its own `run_id` **and** a `sub_run_id`, its own authorization, and its own budget carved from the parent's |
| **Retry** | A **new attempt** of the same run under the same authorization |
| **Replay** | A **new run** that reproduces a prior run's inputs for comparison |

Normative rules:

1. **A retry never overwrites the original attempt.** The original attempt's
   states, events, evidence, and ledger records remain intact and addressable.
2. **Attempt identity is unique and monotonic** within a run. Attempt numbers
   are never reused, even after failures.
3. A retry inherits the run's authorization; it never creates one. If the
   authorization expired, drifted, or was revoked, the retry is denied
   (Scenario 32).
4. **A replay is a distinct run** and must record: `source_run_id`,
   `source_package_revision_id`, `changed_inputs`, `changed_models`,
   `changed_tools`, `changed_policies`, and a `replay_fidelity` classification
   of `exact`, `divergent`, or `not_comparable`.
5. A replay **never** re-executes a consequential external operation. A replay
   that would require one is denied with `UNSAFE_RETRY_REFUSED`.
6. **A successful sub-step is not run completion.** A run completes only when
   its output contract is satisfied and every sub-run and handoff is resolved.

## 14. The eleven authorization facts

Registry §21.1's **eight provider facts remain exactly eight, unmodified**.
This section adds runtime-layer facts and states which system owns each. All
eleven are **conjunctive** and **independently established, evidenced, and
revoked**.

| # | Fact | Owner | Absence means |
| --- | --- | --- | --- |
| 1 | Agent defined | Agent Registry | Unknown agent — deny |
| 2 | Package verified | Future Agent Package Contract | Unverified — deny |
| 3 | Package installed | Agent Registry | Not installed — deny |
| 4 | Agent registered | Agent Registry | Unregistered — deny |
| 5 | Tenant authorized | Provider Registry custody / tenant policy | Not authorized — deny |
| 6 | Capability authorized | Tenant-capability authorization record | Not authorized — deny |
| 7 | Runtime enabled | Explicit runtime enablement for tenant + environment | Not enabled — deny |
| 8 | Run authorized | Recorded run authorization bound to this exact run and revision | Unauthorized — deny |
| 9 | Tool authorized | Tool Gateway authorization (Section 21) | Not authorized — deny |
| 10 | Provider authorized | The eight Registry facts, evaluated by the Gateway | Not authorized — deny |
| 11 | Operation approved | Operator approval for the exact bound operation, where required | Not approved — deny |

Rules:

1. **No `ready` boolean.** No single field, computed property, aggregate,
   score, or cached view may stand for two or more facts. A schema doing so is
   non-conforming.
2. **No fact implies another.** Runtime enabled does not authorize a run; run
   authorized does not authorize a tool; tool authorized does not authorize a
   provider; provider authorized does not approve an operation.
3. Fact 10 **delegates entirely** to Registry §21.1 and Gateway §17. The Agent
   Runtime never re-implements, caches past its inputs, summarizes, or
   second-guesses the eight provider facts.
4. Facts 1–10 are standing state; fact 11 is **per-operation** and bound to one
   exact typed, versioned, digest-bound target (Control Plane §16.1, Gateway
   §18).
5. An `authorization_status` view MAY be computed at evaluation time. It is
   never stored as a grant, never cached past its inputs, and never writable.

## 15. Execution envelope

The execution envelope is the **immutable, framework-neutral** description of
one authorized attempt. A bridge receives a translation of it; it never
receives more.

### 15.1 Fields

| Group | Fields |
| --- | --- |
| Identity | `run_id`, `attempt_id`, `runtime_instance_id`, `trace_id`, `parent_run_id` (nullable), `sub_run_id` (nullable) |
| Isolation | `tenant_id`, `environment`, `context_namespace_id`, `memory_namespace_id` |
| Agent | `agent_definition_id`, `installed_agent_id`, `package_revision_id`, `framework_type`, `bridge_contract_revision` |
| Intent | `requested_capability`, `output_contract_ref`, `stop_conditions` |
| Routing | `model_routing_request_ref` (a request, never a model binding), `model_routing_decision_ref` (nullable until decided) |
| Context | `context_snapshot_refs[]`, `context_access_scope`, `redaction_policy_ref` |
| Memory | `memory_scope_refs[]`, `memory_write_scope` |
| Permissions | `tool_permission_refs[]`, `provider_permission_refs[]` |
| Limits | `max_steps`, `max_depth`, `max_wall_clock`, `max_input_tokens`, `max_output_tokens`, `max_concurrent_steps` |
| Authorization | `authorization_refs[]` (facts 1–10), `approval_refs[]` (fact 11) |
| Audit | `audit_intent_ref`, `audit_reservation_ref` |
| Cost | `cost_budget_ref`, `reserved_budget` |
| Behavior | `cancellation_policy_ref`, `retry_policy_ref`, `external_content_posture` |
| Integrity | `envelope_digest` (canonical, per Section 8.3), `schema_version` |

### 15.2 Prohibited envelope contents (normative)

The envelope MUST NOT contain: credentials of any kind; raw secrets;
environment variables; provider tokens, keys, or session identifiers; OAuth
grants or codes; account identifiers; connection strings; or complete
sensitive context bodies where a reference is sufficient.

Sensitive context is carried **by reference**, resolved at the point of use
under the run's access scope, and never inlined into an envelope, a handoff, a
log, an event payload, an error message, or an audit record.

### 15.3 Immutability

An envelope is immutable once an attempt starts. Any change requires a new
attempt with a new `attempt_id` and a re-evaluation of Section 14. An envelope
whose `envelope_digest` does not reproduce is rejected with
`ENVELOPE_INTEGRITY_FAILED`; it is never repaired in place.

## 16. Framework bridge contract boundary

The **Framework Bridge Contract is deferred** to its own task. This section
fixes only the minimum operation set and the rules binding it.

| Operation | Responsibility | Fail-closed behavior |
| --- | --- | --- |
| `validate_package_compatibility` | Confirm a package revision is expressible in this framework at this bridge revision | Incompatible → `PACKAGE_MISMATCH` |
| `prepare_invocation` | Build framework-local, inert invocation state from the envelope | Failure → `failed`; no execution |
| `translate_envelope` | Project the neutral envelope into framework-native structures, dropping nothing required and adding nothing | Any unrepresentable required field → `BRIDGE_UNSUPPORTED_BEHAVIOR` |
| `start_execution` | Start execution **only** in the mode the runtime specifies (Section 36); inert modes must not reach a framework runtime | Unauthorized mode → `EXECUTION_BLOCKED` |
| `stream_events` | Emit normalized runtime events (Section 26) | Unmappable event → emit an explicit `unmapped` event; never silently drop |
| `request_cancellation` | Forward a cancellation request and report acknowledgement honestly | Unsupported → `CANCELLATION_UNSUPPORTED`; runtime escalates per Section 27 |
| `normalize_result` | Map framework output to the run's output contract | Contract unmet → `failed`, never a coerced success |
| `normalize_failure` | Map framework failure to Section 33 classes without inventing detail | Unmappable → `BRIDGE_FAILURE_UNCLASSIFIED` |
| `report_unsupported_behavior` | Declare what this bridge cannot do, before it is asked | Silence is not a capability claim |

**Bridge implementation is not authorized by this task.**

## 17. Shared Context access

Shared Context canonical truth is owned by the Shared Context Layer
(`shared_context/**`, the Context Gate, Control Plane §9.3). **Agents never
write it.**

### 17.1 Seven separate operations

| Operation | Effect | Authority required |
| --- | --- | --- |
| `read_snapshot` | Read an immutable, addressable snapshot | Context read scope for the class |
| `propose_update` | Submit a proposal for review; changes nothing | Produced-class declaration + propose scope |
| `append_evidence` | Append immutable evidence to an append-only surface | Evidence-append scope; never mutates existing records |
| `create_derived_context` | Create run-scoped derived context from readable sources | Read scope for every source |
| `request_canonical_mutation` | Request a governed canonical change | Operator approval, bound per Control Plane §16.1 |
| `create_handoff_context` | Build a bounded context bundle for a handoff | Read scope + handoff authorization |
| `invalidate_derived_context` | Mark derived context unusable | Runtime or operator only |

`propose_update` and `request_canonical_mutation` are **distinct**: a proposal
is a reviewable artifact; a mutation request enters an approval path. Neither
mutates canonical state on its own.

### 17.2 Context classes and required metadata

Every context record carries: `context_class`, `access_scope`, `tenant_id`,
`source_provenance`, `freshness_state`, `confidence`, `sensitivity_level` (the
canonical vocabulary, not a parallel scale), `retention_policy`,
`mutation_authority`, and `conflict_state`.

### 17.3 Rules

1. **Availability is not authorization.** A readable snapshot reference does
   not grant read access; scope is evaluated at the point of use (Scenario 13).
2. **Tenant boundary is absolute.** Cross-tenant context resolution denies,
   and the denial does not reveal existence.
3. **Conflicts are never silently resolved.** Conflicting proposals surface
   both claims with provenance and precedence; the runtime never picks a winner
   (Scenario 26).
4. **Snapshots are immutable and versioned.** A stale snapshot never silently
   refreshes; a run holding one is told (Scenario 25).
5. **Sensitivity does not decay.** Derived context inherits the highest
   sensitivity of its sources unless an explicit, recorded redaction
   transformation lowers it.

## 18. Memory architecture

Six separated categories. **No category is promoted to another automatically.**

| # | Category | Read | Write | Propose | Persist | Share | Discard |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Immutable run context** | Yes, within run | No | No | Yes, as evidence | By reference only | Never |
| 2 | **Short-term working memory** | Yes, within attempt | Yes, within attempt | n/a | No | No | At attempt end |
| 3 | **Agent-local memory** | Yes, within agent + tenant | Yes, within agent + tenant | n/a | Yes, tenant-scoped | **No** | On retention expiry |
| 4 | **Shared derived memory** | Yes, within authorized scope | No direct write | Yes | Yes, after acceptance | Yes, within tenant | On invalidation |
| 5 | **Canonical project context** | Yes, within scope | **Never by an agent** | Yes, via §17 | Yes | Yes | Never — superseded only |
| 6 | **Operator-approved long-term memory** | Yes, within scope | **Never by an agent** | Yes | Yes, after approval | Yes, within scope | Operator only |

Rules:

1. **Existence is not permission.** A memory record's existence never implies
   permission to read or write it.
2. **Framework-native memory is category 2 at most.** LangGraph checkpoints,
   CrewAI crew memory, AutoGen conversation history, OpenAI Agents SDK session
   state, and Claude Code session context are bridge-local. They never become
   canonical automatically, never cross a run boundary without an explicit
   normalized admission, and never cross a tenant boundary at all.
3. **Categories are never conflated.** No field, store, or API may treat two
   categories as one.
4. Promotion 2→3, 3→4, 4→5, and 4→6 each require an explicit, separately
   authorized step with its own evidence.

## 19. Context-flow tracing

Every context transfer — between agents, between runs, into a handoff, or into
a derived record — appends an immutable trace record:

`source_agent_id`, `destination_agent_id`, `source_run_id`, `source_step_id`,
`context_class`, `source_reference`, `canonical_hash`, `transformation_id`,
`redaction_applied`, `sensitivity_level`, `access_decision`,
`acceptance_state` (`accepted` | `rejected`), `rejection_reason` (nullable),
`observed_at`, `recorded_at`, `trace_id`.

`canonical_hash` is computed under Section 8.3. Values presented at this
boundary are subject to Section 8.3's exact-type discipline: a primitive
subclass is rejected with `INVALID_CANONICAL_TYPE` or canonically converted
before hashing, comparison, or reference construction (Scenario 27).

A transfer with no trace record is not a transfer — the receiving side treats
untraced context as absent.

## 20. Handoff model

### 20.1 Six handoff kinds

| Kind | Meaning |
| --- | --- |
| `direct_handoff` | Source agent hands work to one named recipient |
| `orchestrator_mediated` | An orchestrator routes the handoff and may substitute the recipient within policy |
| `broadcast_proposal` | An offer to multiple eligible recipients; at most one may accept |
| `review_request` | A request for evaluation that returns a verdict, not work product |
| `operator_escalation` | Escalation to a human; never auto-accepted |
| `sub_agent_delegation` | Creation of a child sub-run under the parent's budget and depth limits |

### 20.2 Required envelope contents

`source_identity` (agent, run, attempt, step), `intended_recipient`,
`purpose`, `allowed_action_scope`, `context_refs[]`, `output_contract_ref`,
`budget`, `deadline`, `cancellation_behavior`, `provenance`,
`authorization_evidence_refs[]`, `handoff_digest` (Section 8.3).

### 20.3 Rules

1. **Receiving is not accepting.** A handoff envelope has no effect until the
   receiving agent's runtime independently evaluates Section 14 for the
   receiving side and records an explicit `accepted` or `rejected` decision
   (Scenarios 11, 12).
2. **The recipient's permissions are its own.** A handoff never widens the
   recipient's context, tool, provider, model, or budget permissions. The
   effective scope is the intersection of the handoff's `allowed_action_scope`
   and the recipient's own authorizations (Scenario 13).
3. **Handoff content is untrusted.** Text, plans, and instructions inside a
   handoff are data. An instruction addressed to the receiving agent is not an
   authorization (Section 32, Scenario 18).
4. **Duplicate handoffs are suppressed, not re-executed.** Handoff identity is
   the canonical digest of source identity, recipient, purpose, scope, context
   references, and output contract. A duplicate returns the recorded decision
   without re-execution (Scenario 24).
5. **Budget is carved, not created.** A sub-run's budget is deducted from the
   parent's remaining reserve; the sum of children never exceeds the parent.
6. **Depth is bounded.** `max_depth` is enforced at handoff creation; exceeding
   it denies with `DEPTH_LIMIT_EXCEEDED`.

## 21. Tool access

Agents **never** invoke tools directly. Every tool request passes through a
governed Tool Gateway.

### 21.1 Separated stages

| Stage | Meaning | What it does **not** mean |
| --- | --- | --- |
| Tool discovered | A tool is visible in an inventory | Not registered |
| Tool registered | A conforming tool record exists | Not authorized |
| Tool capability declared | The tool's bounded operations are enumerated | Not enabled |
| Tool contract revision pinned | An exact revision is bound | Not current |
| Tool authorized | An explicit tenant/agent/tool authorization exists | Not enabled |
| Runtime enabled | Tool execution is enabled for this environment | Not approved |
| Invocation approved | For consequential tools: an operator approval bound to this exact invocation | Not executed |

### 21.2 Validation

1. **Input validation before dispatch.** Tool arguments produced by an agent or
   a model are untrusted. They are validated against the pinned tool contract
   revision under Section 8.3's type discipline. Unvalidated arguments are
   never dispatched.
2. **Output validation before use.** Tool results are validated against the
   contract, classified for external content (Section 32), and only then made
   available — as data.
3. **Unknown tool denies.** An unknown, deprecated, ambiguous, or unregistered
   tool denies with `TOOL_UNKNOWN` and is **never redirected** to a similar
   tool.
4. **Consequential tool actions require reconciliation on unknown outcome.** A
   timeout or ambiguous result from a consequential tool yields
   `EXTERNAL_OUTCOME_UNKNOWN` and `run_state:reconciliation_required`, never a
   blind retry (Scenarios 20, 23).

## 22. Provider access

### 22.1 The only path

Every provider operation flows: **Agent → Agent Runtime → Provider Registry
resolution → Integration Gateway → accepted provider adapter → provider.**
There is no other path, no fallback path, and no emergency path.

### 22.2 Agent Runtime prohibitions (normative)

The Agent Runtime MUST NOT: select credentials; read, request, derive, cache,
or forward provider secrets; execute a provider-native fallback; infer a
provider authentication mode; bypass provider scope validation; re-implement
Gateway policy evaluation; or present a provider proposal as an executed
operation.

### 22.3 Proposal, not execution

An agent produces a **provider operation proposal** with a
`provider_operation_proposal_id`. A proposal is a bounded, typed, digest-bound
description of one capability against one scope. It carries no credential and
performs nothing. The Gateway independently re-derives every authorization
input from authoritative records; it never forwards the runtime's claims
(Gateway §6.1).

### 22.4 Delegation of the eight facts

Provider authorization is fact 10 of Section 14 and is satisfied only by the
Gateway's evaluation of Registry §21.1's eight facts. The runtime records the
Gateway's decision; it never computes, caches past its inputs, or summarizes it
into a boolean.

### 22.5 Cloudflare Review 002 `P2-04` — carried forward, not resolved

Cloudflare Review 002 recorded that Provider Registry §26.1 declares
Cloudflare's `supported_auth_modes` as scoped `api_token` for the provider API,
while the delegated capability class requires `delegated_oauth`, and no
Cloudflare-track contract enumerates `delegated_oauth`.

This specification:

- **does not resolve** that provider-specific issue;
- **does not assume** Cloudflare delegated authentication is available;
- **does not treat** any provider descriptor as registered or executable;
- **does not bind** any agent to a Cloudflare authentication mode;
- **requires** every provider operation to pass through the Provider Registry
  and the Integration Gateway;
- **requires** registration-time compatibility validation before any runtime
  use;
- **keeps** all live provider operations blocked.

**`P2-04` must be resolved or formally adjudicated before**: provider
registration; credential configuration; credential verification; live
Cloudflare transport; and delegated Cloudflare execution. An Agent Runtime
implementation task must not treat this constraint as discharged (Scenario 29).

## 23. Model routing

### 23.1 The boundary

The Agent Runtime **requests**; the Model Router **decides**; the runtime
**records and enforces** the decision. The runtime never selects a model.

### 23.2 What the runtime may request

`capability_class`, `context_window_requirement`, `latency_tier`,
`quality_tier`, `modality`, `cost_ceiling`, `allowed_provider_set`,
`data_governance_constraints` (including `sensitivity_level` and residency
requirements).

The runtime MUST NOT request a specific model by name as an authorization
shortcut, and MUST NOT accept a model that is not in an authorized set.

### 23.3 Routing artifacts

| Artifact | Contents |
| --- | --- |
| Routing request | The Section 23.2 fields, `run_id`, `attempt_id`, `step_id`, `tenant_id` |
| Routing decision | Selected model, provider, decision digest, decision timestamp, authorization references |
| Routing explanation | Selected candidate; rejected alternatives with per-candidate reasons; applied rules and precedence; estimated cost and its basis; confidence and basis; fallback route and trade-offs; override status |
| Fallback authorization | An explicit authorization for a named fallback set — never implicit |
| Substitution policy | The exact conditions under which one authorized model may replace another |
| Operator override | An exact, scoped, time-bound, auditable operator decision |
| Cost estimate | Section 24 |

### 23.4 Fallback prohibitions (normative)

No automatic fallback may cross a **sensitivity boundary**, a **provider
boundary**, a **quality floor**, a **cost ceiling**, or the **approved-model
set**. Crossing any of these requires a new routing decision and, where policy
demands, a new approval.

### 23.5 No permitted model

If routing yields no permitted model, the result is `NO_PERMITTED_MODEL` and
`run_state:blocked`. It is never "best available," never a silent downgrade,
and never an unrouted execution (Scenario 14).

### 23.6 Ties

If routing yields multiple equally-ranked permitted candidates, the router
applies a **declared, deterministic tie-breaker** recorded in the explanation.
If no declared tie-breaker resolves the tie, the result is
`ROUTING_TIE_UNRESOLVED` and `run_state:waiting_for_operator` — never a random
or arbitrary pick (Scenario 15).

## 24. Cost and token accounting

**Estimates and actuals are separate fields, separately sourced, and never
merged.**

| Group | Fields |
| --- | --- |
| Estimates | `estimated_input_tokens`, `estimated_output_tokens`, `estimated_tool_cost`, `estimated_provider_cost`, `estimation_basis`, `estimate_confidence` |
| Reservation | `reserved_budget`, `reservation_ref`, `reservation_expires_at` |
| Actuals | `actual_input_tokens`, `actual_output_tokens`, `actual_cache_tokens`, `actual_model_cost`, `actual_tool_cost`, `actual_provider_cost`, `measurement_source` |
| Reconciliation | `variance`, `variance_basis`, `currency`, `pricing_source_revision`, `pricing_verified_at`, `pricing_valid_until` |

Rules:

1. **An estimate is not a billing fact.** No view, aggregate, or export may
   present an estimate as a confirmed cost.
2. **Unknown pricing stays unknown.** A missing price is `null` with an
   explicit `INSUFFICIENT_PRICING_DATA` state. It is never `0`, never omitted
   silently, and never inferred from a similar model.
3. **A budget over unknown pricing is unenforceable** and must be labelled so
   (Control Plane §19).
4. **Expired pricing evidence is not authority.** Pricing outside its declared
   validity window is `freshness_state:expired`; runs depending on it for a
   budget decision block rather than proceed.
5. **Estimate exceeding budget denies before execution**, not after
   (Scenario 16).
6. Token semantics reuse `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]`
   §5.2 unchanged; this section adds no competing token vocabulary.

## 25. Run ledger

The Run Ledger record is owned by
`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5. The Agent Runtime is a
**producer**, not an owner.

Append-only record kinds emitted: run creation; authorization decision; every
state transition; model routing requests and decisions; tool requests and
results; provider operation proposals and Gateway decisions; context reads;
context proposals; handoff creation, acceptance, and rejection; operator
decisions; errors; cancellation requests and outcomes; reconciliation outcomes;
and completion.

Rules:

1. **Append-only.** Records are never edited or deleted. Corrections are new
   records that reference and supersede.
2. **The ledger is evidence, not necessarily canonical business state.** A
   ledger record asserts what the runtime observed and recorded, not what is
   true in an external system.
3. **`operator_approved` is not authority** (AI Operations Intelligence §5.8).
   Authority is the approval record's complete validated binding.
4. **Ledger unavailability blocks consequential work.** Consistent with Gateway
   §29, when a durable audit reservation cannot be created, no consequential
   external operation proceeds (`AUDIT_RESERVATION_FAILED`).

## 26. Event model

### 26.1 Categories

`lifecycle`, `model`, `tool`, `provider`, `context`, `memory`, `handoff`,
`operator`, `security`, `cost`, `trace`, `error`.

### 26.2 Required properties

Every event carries: `event_id`, `schema_version`, `category`, `event_type`,
`source_identity` (exactly one of `runtime`, `bridge`, `router`, `tool_gateway`,
`integration_gateway`, `operator`, `scheduler`), `run_id`, `attempt_id`,
`step_id` (nullable), `trace_id`, `sequence`, `observed_at`, `recorded_at`,
`payload_summary_ref`, `redaction_state`, and `canonical_digest`.

### 26.3 Rules

1. **Stable schemas.** Event types are versioned; a changed shape is a new
   version, never a silent field change.
2. **No raw secrets, ever** — in payloads, summaries, errors, or references.
3. **Ordering evidence is explicit.** `sequence` is monotonic per attempt.
   Gaps are reported as `evidence_state:partial` with the last confirmed
   sequence; a gap is never rendered as quiet (Control Plane §19).
4. **Observed time and recorded time are distinct fields** and are never
   merged, substituted, or back-filled.
5. **Unmappable framework events are emitted as `unmapped`** with the bridge's
   raw category recorded as untrusted data. They are never dropped.

## 27. Cancellation and timeout

### 27.1 The honest model

| Concept | Meaning |
| --- | --- |
| Cancellation request | The runtime has asked for cancellation. Nothing is guaranteed yet |
| Cancellation acknowledgement | The bridge reports the request was received and acted upon locally |
| Framework cancellation support | Declared per framework and per bridge revision; `constrained` or `unsupported` are legitimate values |
| External-effect uncertainty | Whether any in-flight model call, tool call, or provider operation may still complete |
| Forced local stop | The runtime stops consuming and coordinating locally |
| Reconciliation required | The terminal-blocking state when external effects are unknown |

### 27.2 Rules (normative)

1. **A cancellation request is not a stop.** The runtime never records
   `run_state:cancelled` on the strength of a request alone.
2. **A forced local stop is not proof external effects stopped.** It is
   recorded exactly as what it is.
3. `cancellation_requested → cancelled` is permitted **only** when every
   in-flight external effect is confirmed not to have occurred or confirmed to
   have been reverted. Otherwise the transition is to
   `reconciliation_required` (Scenarios 19, 20).
4. **Timeout follows the same rule.** A timeout with any unknown external
   outcome is `reconciliation_required`, not `timed_out` (Scenario 21).
5. **No overclaiming.** The runtime never asserts a cancellation guarantee that
   the framework, tool, or provider cannot provide. A bridge reporting
   `CANCELLATION_UNSUPPORTED` results in a forced local stop plus
   `reconciliation_required` if anything was in flight (Scenario 30).

## 28. Retry and reconciliation

| Concept | Definition |
| --- | --- |
| **Safe retry** | A new attempt of a read-only or provably idempotent operation whose prior attempt is known not to have taken effect |
| **Unsafe retry** | Any retry of a consequential operation whose outcome is unknown, or whose idempotency cannot be established |
| **Idempotent operation** | An operation with a declared idempotency key and provider- or gateway-guaranteed at-most-once effect |
| **Unknown external result** | Timeout, ambiguous response, or transport failure after transmission |
| **Duplicate suppression** | Returning a recorded terminal outcome for a replayed key without re-execution |
| **Attempt identity** | The unique `attempt_id` distinguishing every attempt's evidence |
| **Reconciliation task** | A required follow-up establishing what actually happened externally |

Rules:

1. **No consequential provider or tool action is retried blindly.** This mirrors
   Gateway §26.2–26.3 and is not weakened here.
2. **On unknown outcome:** perform a fresh authoritative read; compare against
   the approved after-state; if applied, record success **with verification
   evidence**; if not applied, a **new proposal and new approval** are
   required; if partially applied, report `PARTIAL_APPLICATION` with the exact
   partial state.
3. **A retry is not permission to repeat a consequential action.** Fact 11
   (operation approved) is evaluated afresh for each consequential attempt.
4. Idempotency keys are derived under Section 8.3's canonical rules and are
   never shared across tenants, runs, or intended actions.
5. A run in `reconciliation_required` is **not** a failure and **not** a
   success. It is an open obligation, visible to operators until resolved.

## 29. Concurrency and isolation

### 29.1 Eight isolation boundaries

| Boundary | Requirement |
| --- | --- |
| Tenant isolation | Absolute. No identifier, context, memory, cache, budget, event, or error crosses tenants. Cross-tenant resolution denies without revealing existence |
| Run isolation | Runs share no mutable state. A run's failure never mutates another run |
| Agent-local state isolation | Agent-local memory is scoped to `(agent, tenant)` and never shared across agents |
| Framework-process isolation | Framework execution is contained so that a framework's global state, monkey-patching, or crash cannot alter the runtime's decisions or another run's state |
| Context namespace isolation | Each run resolves context only within its `context_namespace_id` |
| Memory isolation | Each run writes only within its `memory_namespace_id`, per Section 18 |
| Tool-session isolation | Tool sessions are never reused across runs or tenants |
| Provider-session isolation | Provider sessions are Gateway-owned and never shared across tenants; the runtime holds none |

### 29.2 Race and conflict behavior

| Condition | Required behavior |
| --- | --- |
| Concurrent context proposals | Both recorded; neither auto-applied; conflict surfaced with provenance and precedence (Scenario 26) |
| Race on a shared derived record | Optimistic concurrency with an expected-version precondition; a failed precondition yields `STALE_STATE`, never a silent overwrite |
| Stale snapshot | Detected by digest/version comparison; the run is told and blocks or re-reads under policy; never silently refreshed (Scenario 25) |
| Duplicate handoff | Suppressed by handoff digest; the recorded decision is returned (Scenario 24) |
| Competing approvals | At most one approval may be effective for one exact target binding; a second is rejected as `APPROVAL_CONFLICT` and both are audited |
| Cancellation race | If a run completes before cancellation takes effect, the honest terminal state is `completed` with the cancellation request recorded; if any effect is unknown, `reconciliation_required` |

## 30. Human-in-the-loop

### 30.1 When operator interaction is required

Approval for a consequential action; clarification of an underspecified
objective; resolution of ambiguity the runtime cannot resolve deterministically;
any provider operation with external consequence (R3–R5); any
security-sensitive action; any budget increase; any policy override; any
conflicting context requiring adjudication; any uncertain external outcome
requiring reconciliation; and any routing tie no declared tie-breaker resolves.

### 30.2 Approval properties (normative)

Operator approval MUST be **scoped** (exact allowed and prohibited actions),
**time-bound** (explicit expiry), **revision-bound** (exact
`package_revision_id`, `target_version`, and `target_digest`), **action-bound**
(one exact typed target, never a class), and **auditable** (append-only record
with operator identity, decision, and rationale reference).

Reused unchanged from Control Plane §16.2 and Gateway §18.3: no self-approval,
no blanket approval, no inferred consent, no approval replay, no hidden side
effect, no autonomous safety-policy change, no permission widening. Approval to
prepare or approve a configuration does not authorize its execution.

An approval bound to an older package revision does not authorize a run on a
newer one; the run blocks and a fresh decision is required (Scenario 32).

## 31. Security model

Each threat below has a prevention rule, a detection rule, a fail-closed
result, and an audit obligation. Fail-closed results use Section 33 classes.

| Threat | Prevention | Detection | Fail-closed result | Audit evidence |
| --- | --- | --- | --- | --- |
| **Prompt injection** | All model, tool, provider, file, web, and agent content is data; instructions in content never alter runtime policy | Instruction-shaped-content classification on every untrusted payload | `INJECTION_SUSPECTED` recorded; content continues to be treated as data; no policy change | Security event with content-free classification, source, and trace |
| **Tool-result injection** | Tool output validated against the pinned contract before use; never interpreted as authorization | Contract mismatch and instruction-shape detection | `EXTERNAL_CONTENT_REJECTED` or quarantine | Security event + tool invocation reference (Scenario 17) |
| **Context poisoning** | Admission gate, provenance, sensitivity, and conflict state on every context record | Provenance verification failure, conflict detection, digest mismatch | Proposal rejected; dependent runs blocked | Content-free provenance and conflict record |
| **Malicious agent package** | Package verification (fact 2), immutable revisions, provenance and signer evidence, declaration intersection | Digest mismatch, provenance failure, undeclared behavior at the bridge boundary | `PACKAGE_UNVERIFIED` / `PACKAGE_MISMATCH`; installation and run denied | Package identity, revision, verification result |
| **Framework bridge drift** | `bridge_contract_revision` pinned in the envelope; compatibility validated per package revision | Revision mismatch, unmappable required fields | `CONTRACT_CONFLICT`; run blocked | Bridge and contract revisions, failing field |
| **Model substitution** | Routing decision is bound and recorded; substitution policy is explicit; §23.4 boundaries | Decision digest mismatch; model outside authorized set | `MODEL_UNAUTHORIZED`; step blocked | Routing request, decision, explanation, rejected candidates |
| **Tenant confusion** | Tenant-scoped identifiers; namespace isolation; no cross-tenant resolution | Any cross-tenant reference attempt | `TENANT_ISOLATION_VIOLATION`; deny without revealing existence | Precise inward denial reason; coarse outward class |
| **Credential exfiltration** | Runtime and bridges never hold credentials; §15.2 prohibitions; redaction before rendering | Secret-shaped-value screening on envelopes, events, errors, and exports | `SENSITIVE_VALUE_REJECTED`; value never echoed | Content-free rejection record |
| **Excessive context disclosure** | Least-privilege context scope; reference-not-body; redaction policy | Scope evaluation at point of use; sensitivity comparison | `CONTEXT_ACCESS_DENIED` | Access decision with class and scope, no content |
| **Unsafe retry** | Consequential retries require fresh fact 11; §28 rules | Unknown-outcome detection; idempotency key state | `UNSAFE_RETRY_REFUSED`; `reconciliation_required` | Attempt identity, key state, reconciliation obligation |
| **Forged provenance** | Provenance is signed/verified evidence, never a self-asserted field | Verification failure; supersession and conflict checks | `PROVENANCE_VERIFICATION_FAILED`; record quarantined | Verification result and source |
| **Digest collision** | Canonical serialization, type tags, collision-resistant algorithm (§8.3) | Two distinct canonical byte sequences producing one digest, or two logical values producing one byte sequence | `DIGEST_COLLISION_SUSPECTED`; both inputs quarantined; dependents blocked | Both canonical encodings by reference, algorithm, and trace |
| **Malicious primitive subclass** | Exact built-in type checks at every trust boundary (§8.3 rules 1–2) | `type(value) is <builtin>` failure | `INVALID_CANONICAL_TYPE`; value rejected or canonically converted | Field path and rejection class, no value echo (Scenario 27) |
| **Arbitrary object representation** | Serialization never calls overridable object protocols (§8.3 rule 3) | Non-canonical encoding path detected in review or validation | `INVALID_CANONICAL_TYPE`; operation denied | Field path and encoder identity |
| **Cost exhaustion** | Hard budgets, reservations, per-run and per-tenant ceilings, estimate-before-execute | Estimate exceeding budget; actuals approaching reservation | `BUDGET_EXCEEDED`; run blocked before execution | Estimate, basis, budget, reservation |
| **Infinite agent loops** | `max_steps`, `max_depth`, `max_wall_clock`, handoff-cycle detection, duplicate-handoff suppression | Step/depth/time counters; repeated-state detection | `STEP_LIMIT_EXCEEDED`, `DEPTH_LIMIT_EXCEEDED`, or `LOOP_DETECTED`; run blocked | Counter values and detected cycle |

## 32. External-content posture

**All** model output, tool results, provider responses, file content, web
content, and other agents' output are **untrusted until classified and
validated**.

Every untrusted payload carries: `content_origin`, `trust_state`
(`untrusted` | `validated` | `quarantined`), `sensitivity_level`,
`instruction_bearing_content` (boolean), `sanitization_applied`,
`transformation_id`, `validation_result`, `acceptance_state`.

Rules:

1. **Agent-to-agent content is not automatically trusted.** A peer agent's
   output is external content with respect to the receiving run.
2. **Instruction-bearing content is never an authorization.** Detecting it sets
   a flag and records a security event; it never changes policy, permissions,
   routing, budgets, or run state.
3. **Sanitization is recorded, not assumed.** An untransformed payload is
   `untrusted`, not `validated`.
4. **Quarantine is terminal for that payload.** Quarantined content is never
   processed, never re-submitted automatically, and never inlined into an
   error, event, or audit record.
5. **Agent-generated code, prompts, plans, and tool arguments remain untrusted
   until validated** against their contracts.

## 33. Error taxonomy

Gateway §25.2 classes are **adopted unchanged** for the provider boundary and
are not restated or fragmented here. The classes below are Agent Runtime-layer
classes added only where the Gateway set has no equivalent. Outward classes are
coarse; audit records carry the precise inward `denial_reason`, the failing
evaluation step, and the resolved facts (Gateway §25.3).

Per Cloudflare Review 002 finding **`P3-01`**, structurally malformed input and
sensitive-value detection have **distinct** classes. A structurally invalid
reference MUST NOT be reported as a sensitive-data error.

| Class | Meaning | Retry? |
| --- | --- | --- |
| `INVALID_REFERENCE_SHAPE` | A reference is structurally malformed | No |
| `INVALID_CANONICAL_TYPE` | A value is not the exact required built-in primitive type, or is a primitive subclass | No |
| `SENSITIVE_VALUE_REJECTED` | A value matched a secret-shaped screen and was refused without echo | No |
| `UNSUPPORTED_VALUE` | A structurally valid value outside a closed vocabulary | No |
| `UNSUPPORTED_FRAMEWORK` | `framework_type` is not one of the six | No |
| `UNSUPPORTED_CAPABILITY` | The requested capability is not expressible for this agent or bridge | No |
| `PACKAGE_UNVERIFIED` | Fact 2 unmet | No |
| `PACKAGE_MISMATCH` | Package revision, declarations, or digest do not match the authorization | No |
| `AGENT_UNREGISTERED` | Fact 4 unmet | No |
| `AUTHORIZATION_DENIED` | A runtime authorization fact (1, 3, 5, 6, 8) is unmet | No |
| `RUN_AUTHORIZATION_EXPIRED` | Fact 8 held but has expired or been revoked | No |
| `CONTEXT_ACCESS_DENIED` | Context scope evaluation denied | No |
| `TOOL_DENIED` | Fact 9 unmet | No |
| `TOOL_UNKNOWN` | Unknown, deprecated, ambiguous, or unregistered tool | No |
| `PROVIDER_DENIED` | Fact 10 unmet; the Gateway's precise class is recorded inward | No |
| `RUNTIME_DISABLED` | Fact 7 unmet for this tenant and environment | No |
| `PROVIDER_DISABLED` | Provider execution is disabled independently of runtime enablement | No |
| `EXECUTION_BLOCKED` | Execution refused by mode, policy, or the inert-v1 boundary | No |
| `APPROVAL_REQUIRED` | Fact 11 unmet for a consequential operation | No |
| `MODEL_UNAUTHORIZED` | A model outside the authorized set was selected or requested | No |
| `NO_PERMITTED_MODEL` | Routing produced no permitted candidate | No |
| `ROUTING_TIE_UNRESOLVED` | Multiple equal candidates and no declared tie-breaker | No |
| `TIMEOUT` | A declared limit was reached with **no** unknown external effect | Policy-bounded |
| `CANCELLATION_UNSUPPORTED` | The bridge cannot honor cancellation | n/a |
| `CANCELLATION_INCOMPLETE` | Local stop achieved; external effects unresolved | No |
| `EXTERNAL_OUTCOME_UNKNOWN` | A consequential external outcome cannot be established | **No blind retry** |
| `RECONCILIATION_REQUIRED` | An open reconciliation obligation exists | No |
| `UNSAFE_RETRY_REFUSED` | A retry would repeat a consequential action without authority | No |
| `EXTERNAL_CONTENT_REJECTED` | Untrusted content failed validation or was quarantined | No |
| `BUDGET_EXCEEDED` | An estimate or actual exceeded a budget or reservation | No |
| `STEP_LIMIT_EXCEEDED` / `DEPTH_LIMIT_EXCEEDED` / `LOOP_DETECTED` | A containment limit was reached | No |
| `TENANT_ISOLATION_VIOLATION` | A cross-tenant reference was attempted | No |
| `ENVELOPE_INTEGRITY_FAILED` | `envelope_digest` did not reproduce | No |
| `DIGEST_COLLISION_SUSPECTED` | A canonical-identity collision was detected | No |
| `PROVENANCE_VERIFICATION_FAILED` | Provenance evidence did not verify | No |
| `APPROVAL_CONFLICT` | Two approvals contend for one exact target binding | No |
| `BRIDGE_UNSUPPORTED_BEHAVIOR` | A required behavior is unrepresentable in this bridge | No |
| `BRIDGE_FAILURE_UNCLASSIFIED` | A bridge failure could not be mapped | No |

**No error message, event payload, summary, export, or audit record may contain
a raw sensitive value.** Rejection records the field path and class, never the
value.

## 34. Observability — information architecture only

This section defines **what an operator must be able to see**. It defines no
component, no route, no framework, and no styling, and **implements no frontend
work**. It extends Control Plane §9.4, §9.5, §9.7, and §9.10 without modifying
them.

| View | Must expose | Must never imply |
| --- | --- | --- |
| Active runs | `run_state`, agent, package revision, tenant, environment, elapsed, budget consumed, current step | That an active run is an approved run |
| Queued runs | Position, authorization references, reserved budget, admission constraints | That queued means started |
| Blocked runs | Exact blocking class, the unmet fact, and what would unblock it | That blocked means failed |
| Waiting states | Which of the four waiting states, since when, and on what | That waiting is progress |
| Agent graph | Agents, handoffs, sub-runs, acceptance and rejection decisions | That an edge means accepted work |
| Context flow | Section 19 trace records, redactions, access decisions | Any context body beyond its sensitivity |
| Model usage | Routing requests, decisions, explanations, rejected candidates | That availability equals authorization |
| Tool usage | Invocations, contract revisions, validation outcomes | That registration equals authorization |
| Provider proposals | Proposals, Gateway decisions, coarse outward classes | That a proposal is an executed operation |
| Costs | Estimates and actuals as separate columns, unknown as `—` | That an estimate is a billing fact |
| Errors | Section 33 class, trace, and remediation obligation | Any raw sensitive value |
| Approvals | Complete bound identity: target type, ID, version, digest, scope, expiry, provenance | That display constitutes authority |
| Security events | Category, classification, trace, containment outcome | Any quarantined content |

Every view carries the applicable canonical status dimensions and an explicit
source mode (`canonical`, `static_demo`, `simulated`, `future_live`, `partial`,
`unknown`). No view synthesizes a universal "healthy," "active," or green state.

## 35. Framework compatibility matrix

Statuses: **AS** architecturally supported · **BR** bridge required ·
**C** constrained · **U1** unsupported in v1 · **RR** requires research.

**Every cell is an architectural planning position, not a verified capability
test.** No framework was installed, imported, connected, or executed during
this task. Each cell MUST be independently validated by the Framework Bridge
Contract task before any bridge is implemented, and no cell may be cited as
evidence of a framework's behavior.

| Dimension | `claude_code` | `openai_agents_sdk` | `langgraph` | `crewai` | `autogen` | `mellycore_custom` |
| --- | --- | --- | --- | --- | --- | --- |
| Lifecycle mapping | BR | BR | BR | BR | BR | AS |
| Streaming | BR | BR | BR | C | C | AS |
| Tools | BR | BR | BR | BR | BR | AS |
| Handoffs | BR | BR | BR | BR | BR | AS |
| Memory | C | C | C | C | C | AS |
| Cancellation | C | C | C | C | C | AS |
| Retries | C | C | C | C | C | AS |
| Persistence | U1 | U1 | C | U1 | U1 | AS |
| Human approval | BR | BR | BR | BR | BR | AS |
| Tracing | BR | BR | BR | BR | BR | AS |
| Deterministic replay | RR | RR | RR | RR | RR | C |
| Isolation | RR | RR | RR | RR | RR | AS |
| Known limitations | Session/process boundary constrains in-process control and cancellation granularity | In-process convenience APIs must be constrained to prevent direct model/tool paths | Graph state and checkpointing must not become canonical | Crew-level delegation must be re-expressed as governed handoffs | Multi-speaker transitions must be re-expressed as governed handoffs | None known; narrowest surface by construction |

`U1` for persistence means MellyCore will not rely on framework-native
persistence in v1 — not that the framework lacks it. `RR` means this
specification declines to assert a position without evidence.

## 36. Runtime modes

`runtime_mode` is a closed vocabulary. Exactly one applies per attempt.

| Mode | Reaches a framework runtime? | Reaches a model? | Reaches a tool? | Reaches a provider? |
| --- | --- | --- | --- | --- |
| `validation_only` | No | No | No | No |
| `dry_run` | No | No | No | No |
| `simulated` | No | No | No | No |
| `fixture_only` | No | No | No — fixture results only | No |
| `locally_executable` | Yes | No | Local, authorized tools only | No |
| `externally_connected` | Yes | Yes | Yes | Yes, Gateway-mediated |
| `production_enabled` | Yes | Yes | Yes | Yes, Gateway-mediated |

Rules:

1. **v1 distinguishes all seven.** Collapsing any two is non-conforming.
2. **Inert modes must be visibly inert.** `validation_only`, `dry_run`,
   `simulated`, and `fixture_only` MUST carry a persistent, non-dismissible
   source-mode label and MUST NOT produce output, events, ledger records, or UI
   states that resemble live execution.
3. **A fixture result is never a provider request, a model response, or a tool
   result.** It is `evidence_state:static_demo` and is labelled as such
   everywhere it appears.
4. **Mode is never inferred.** An absent or unknown mode denies with
   `EXECUTION_BLOCKED`.
5. `externally_connected` and `production_enabled` require the Gateway §32
   seventeen-item runtime-enablement gate, none of which currently passes
   (Gateway Rule 32.1).

## 37. Inert v1 boundary

The first **Agent Runtime Scaffold** — when and only when separately authorized
— MUST remain inert.

**It may implement:** data models and closed vocabularies; validators; the
lifecycle state machine of Section 12; a **disabled** bridge whose only outcome
is `EXECUTION_BLOCKED`; a **fixture** bridge returning deterministic local
fixtures under `fixture_only`; event types; Run Ledger interfaces (interfaces,
not persistence); canonical serialization and digest utilities per Section 8.3;
and tests.

**It must not implement:** live framework processes; any framework SDK import
on any reachable path; live provider calls; credentials or credential lookup;
model API calls; tool execution reaching outside the process; network
transport; persistence; queues; frontend components; or deployment.

Consistent with the accepted Provider Adapter Scaffold precedent, **no
execution-success outcome may be representable** in an inert scaffold, and the
disabled guarantee must hold across all combinations of the eleven facts —
including the all-eleven-satisfied case.

## 38. Deterministic scenarios

Each scenario resolves without architectural interpretation. `Reconciliation`
records whether an open external obligation results.

| # | Scenario | Relevant facts | Expected `run_state` | Decision | Reason class | Audit record | Reconciliation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Valid definition, package unverified | Fact 1 ✓, fact 2 ✗ | `blocked` | Deny | `PACKAGE_UNVERIFIED` | Denial + package identity/revision | No |
| 2 | Verified package, agent unregistered | Facts 2–3 ✓, fact 4 ✗ | `blocked` | Deny | `AGENT_UNREGISTERED` | Denial + revision | No |
| 3 | Registered agent, runtime disabled | Facts 1–6 ✓, fact 7 ✗ | `blocked` | Deny | `RUNTIME_DISABLED` | Denial + tenant/environment | No |
| 4 | Runtime enabled, run unauthorized | Facts 1–7 ✓, fact 8 ✗ | `blocked` | Deny | `AUTHORIZATION_DENIED` | Denial + missing authorization ref | No |
| 5 | Authorized run, unauthorized model | Facts 1–8 ✓; model outside authorized set | `blocked` | Deny step; no model call | `MODEL_UNAUTHORIZED` | Routing request, rejected candidate, decision | No |
| 6 | Authorized run, unauthorized tool | Facts 1–8 ✓, fact 9 ✗ | `blocked` | Deny; no dispatch | `TOOL_DENIED` | Tool request + denial | No |
| 7 | Authorized run, unauthorized provider | Facts 1–9 ✓, fact 10 ✗ | `blocked` | Deny; no provider request | `PROVIDER_DENIED` (Gateway class recorded inward) | Proposal + Gateway decision | No |
| 8 | Agent requests a provider credential directly | Any | `blocked` | Deny; **never** satisfied | `SENSITIVE_VALUE_REJECTED` + security event | Content-free security event, no value echoed | No |
| 9 | Agent attempts a direct canonical context write | Any | `running` continues; write refused | Refuse; no mutation | `CONTEXT_ACCESS_DENIED` | Access decision, class, scope | No |
| 10 | Agent proposes a context update | Produced-class declared ✓, propose scope ✓ | `running` | Accept the **proposal**; canonical state unchanged | n/a — proposal recorded | Proposal record + provenance | No |
| 11 | Cross-agent handoff accepted | Recipient's facts 1–8 ✓; scope intersection non-empty | Recipient run `authorized` | Accept explicitly | n/a | Handoff + explicit acceptance record | No |
| 12 | Cross-agent handoff rejected | Recipient evaluates and declines | Source `running`; recipient none | Reject | Recorded `rejection_reason` | Handoff + explicit rejection record | No |
| 13 | Recipient lacks required context permission | Handoff grants scope the recipient does not hold | Recipient `blocked` | Deny; handoff does **not** widen scope | `CONTEXT_ACCESS_DENIED` | Intersection result, denied classes | No |
| 14 | Routing returns no permitted model | Facts 1–8 ✓; candidate set empty after policy | `blocked` | Deny; no "best available" | `NO_PERMITTED_MODEL` | Request + all rejected candidates and reasons | No |
| 15 | Routing returns multiple equal candidates | No declared tie-breaker resolves | `waiting_for_operator` | Escalate; no arbitrary pick | `ROUTING_TIE_UNRESOLVED` | Request, tied candidates, escalation | No |
| 16 | Cost estimate exceeds budget | Estimate > budget or reservation | `blocked` | Deny **before** execution | `BUDGET_EXCEEDED` | Estimate, basis, budget, reservation | No |
| 17 | Tool output contains prompt injection | Untrusted tool result, instruction-shaped | `running` | Flag; continue treating as data; no policy change | `INJECTION_SUSPECTED`; quarantine → `EXTERNAL_CONTENT_REJECTED` | Content-free security event + tool invocation ref | No |
| 18 | Agent output contains instructions for another agent | Untrusted agent-to-agent content | Recipient `running` | Treat as data; not an authorization | `INJECTION_SUSPECTED` | Context-flow trace + security event | No |
| 19 | Cancellation during a model call | Request sent; response state unknown | `reconciliation_required` | Local stop; **not** `cancelled` | `CANCELLATION_INCOMPLETE` + `EXTERNAL_OUTCOME_UNKNOWN` | Cancellation request, ack state, in-flight refs | **Yes** |
| 20 | Cancellation during an external tool call | Consequential tool in flight | `reconciliation_required` | Local stop; **not** `cancelled` | `CANCELLATION_INCOMPLETE` | Same, plus tool invocation ref | **Yes** |
| 21 | Timeout with unknown external outcome | Limit reached; effect unknown | `reconciliation_required` | **Not** `timed_out` | `EXTERNAL_OUTCOME_UNKNOWN` | Limit, elapsed, in-flight refs | **Yes** |
| 22 | Safe idempotent retry | Read-only or provably idempotent; prior effect known absent | `running` | New attempt under the same authorization | n/a | New `attempt_id`; original attempt intact | No |
| 23 | Unsafe consequential retry | Consequential; outcome unknown | `reconciliation_required` | Refuse retry | `UNSAFE_RETRY_REFUSED` | Key state, prior attempt, obligation | **Yes** |
| 24 | Duplicate handoff | Identical handoff digest already decided | Unchanged | Return recorded decision; no re-execution | n/a — duplicate suppressed | Duplicate-suppression record referencing the original | No |
| 25 | Stale context snapshot | Snapshot digest/version no longer current | `blocked` or re-read per policy | Do **not** silently refresh | `STALE_STATE` | Held vs. current digest | No |
| 26 | Conflicting context proposals | Two proposals contend | `waiting_for_operator` | Surface both; auto-apply neither | n/a — conflict recorded | Both proposals, provenance, precedence | No |
| 27 | Malicious `str` subclass at a digest boundary | Value passes shape checks; `type(v) is str` fails | `blocked` | Reject, or canonically convert **before** hashing | `INVALID_CANONICAL_TYPE` | Field path + class; **no value echo** | No |
| 28 | Two distinct inputs attempt a digest collision | Distinct canonical bytes → one digest, or two values → one encoding | `blocked` | Quarantine both; block dependents | `DIGEST_COLLISION_SUSPECTED` | Both encodings by reference, algorithm, trace | No |
| 29 | Provider authentication mode unresolved (`P2-04`) | Registry mode vs. required class unreconciled | `blocked` | Deny; do **not** infer a mode | `PROVIDER_DENIED` with `CONTRACT_CONFLICT` inward | Registry ref, required class, unresolved-finding ref | No |
| 30 | Bridge reports unsupported cancellation | `CANCELLATION_UNSUPPORTED` returned | `reconciliation_required` if anything in flight, else `cancelled` | Forced local stop; no guarantee claimed | `CANCELLATION_UNSUPPORTED` | Bridge report + in-flight inventory | **Yes**, if in flight |
| 31 | Package revision changes after authorization | Authorized revision ≠ installed revision | `blocked` | Deny; never silently upgrade | `PACKAGE_MISMATCH` | Both revision IDs and digests | No |
| 32 | Operator approval targets an older revision | Approval binding version/digest ≠ current | `blocked` | Deny; require a fresh decision | `APPROVAL_STALE` (Gateway class) | Complete approval binding vs. current target | No |

## 39. Non-goals

Explicitly excluded from this specification: concrete framework SDK code; live
model invocation; credential storage or retrieval; provider transport; UI
implementation; database selection; queue-vendor selection; deployment
topology; billing implementation; and MellyTrade runtime integration.

## 40. Implementation sequence

The recommended next bounded documents and gates. **Only item 1 is the
authorized next task. Items 2–9 are recommendations and are not authorized by
this specification.**

| # | Task | Kind | Gate before proceeding |
| --- | --- | --- | --- |
| 1 | `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` | Independent read-only review | — (the exact next task) |
| 2 | Agent Package Contract | Documentation | Item 1 PASS |
| 3 | Framework Bridge Contract | Documentation | Item 2 accepted |
| 4 | Shared Context Bridge | Documentation | Item 3 accepted |
| 5 | Agent Runtime Scaffold (inert, Section 37) | Inert local code | Items 2–4 accepted **and** separate Operator authorization |
| 6 | Scaffold Review | Independent review | Item 5 complete |
| 7 | First Agent Package | Inert local code | Item 6 PASS **and** separate authorization |
| 8 | Cross-Agent Smoke (inert modes only) | Validation | Item 7 accepted |
| 9 | Integration Review | Independent review | Item 8 complete |

Any item that would make an agent execution-capable additionally requires the
Model B reconsideration of migration trigger #6 (Section 1.3) before it may
proceed to implementation or merge.

## 41. Open questions

### 41.1 Blocking for this specification

None. Runtime boundary, identity, lifecycle, authorization facts, envelope,
bridge boundary, context and memory separation, handoff acceptance, routing
boundary, tool and provider gateways, cost separation, cancellation honesty,
isolation, error taxonomy, and runtime modes are decided.

### 41.2 Non-blocking, resolved by later bounded tasks

- The exact package format, signing scheme, and loader (Agent Package Contract).
- The exact bridge interface signatures and per-framework validation evidence
  (Framework Bridge Contract).
- The concrete Shared Context read/propose transport (Shared Context Bridge).
- Which `RR` cells in Section 35 resolve to `AS`, `C`, or `U1`.

### 41.3 Deferred and separately gated

- Framework-process isolation mechanism (process, container, or interpreter
  boundary).
- Run persistence, scheduling, and queue architecture.
- Multi-operator approval and delegated approval authority.
- Live provider execution, which remains blocked (Gateway Rule 32.1).
- Cloudflare `P2-04` resolution or formal adjudication (Section 22.5).

No deferred question authorizes implementation or weakens a safety rule.

## 42. Amendment and supersession

This specification is amended only by an explicit, Operator-approved successor
document that names it and states exactly what changes. A weakening amendment
additionally requires an ADR amendment under Gateway §33 rule 5. Superseded
content is retained and marked, never deleted.

## 43. References

### 43.1 Repository (canonical)

- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]`
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`
- `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]`
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`
- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`
- `[[../research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002]]`
- `[[../research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001]]`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `VALIDATION.md`,
  `CONTEXT_GRAPH_SCHEMA.md`, `MODEL_ROUTING.md`

### 43.2 External

None. No external source was fetched, and no framework documentation, SDK, or
service was consulted, installed, or contacted during this task.
