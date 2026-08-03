# MellyCore Agent Runtime Architecture Spec

**Task ID:** MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001
**Remediated by:** MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001
**Contract ID:** MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_001
**Version:** 1.1 — remediates the four P1, five P2, and five P3 findings of
`[[../research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001]]` under
`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`.
**Verification status:** Remediation claims in this version are **unverified**
pending `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002`. Version 1.1 does
not re-open the architecture gate; the gate remains failed until that
independent review passes.
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

### 1.4 Document metrics (normative)

Every count below was **recalculated from this document's own tables** during
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001`, not carried
forward. Review 001 recorded three count discrepancies as findings, so these
figures are normative: a future amendment that changes a table MUST recompute
and restate the corresponding row here, and any divergence between this table
and the referenced section is a defect in this document.

| Dimension | Count | Authoritative section |
| --- | --- | --- |
| Specification sections | 43 | §1–§43 |
| Framework types | 6 | §11.1 |
| Canonical identifiers | 15 | §8.1 |
| Package/runtime separation states | 9 | §9 |
| Run lifecycle states | 17 | §12.2 |
| — terminal / waiting / pending | 5 / 4 / 2 | §12.2 |
| Lifecycle transition rows | 13 | §12.3 |
| `waiting_for_operator` predecessors | 4 | §12.3.1 |
| Forbidden-transition rules | 12 | §12.4 |
| Authorization facts | 11 | §14 |
| — run-admission / per-invocation | 8 / 3 | §14.1 / §14.2 |
| Execution-envelope field groups | 14 | §15.1 |
| Authorization sequencing steps | 8 | §15.4 |
| Framework Bridge operations | 9 | §16 |
| Shared Context operations | 7 | §17.1 |
| Staleness conditions | 6 | §17.4 |
| Memory categories | 6 | §18 |
| Context-flow trace fields | **17** | §19 |
| Handoff kinds | 6 | §20.1 |
| Handoff envelope contents | **12** | §20.2 |
| Broadcast acceptance conditions | 7 | §20.4 |
| Tool-access stages | 7 | §21.1 |
| Routing request dimensions | 8 | §23.2 |
| Routing artifacts | 7 | §23.3 |
| Ledger record kinds | 14 | §25 |
| Runtime event categories | 12 | §26.1 |
| Isolation boundaries | 8 | §29.1 |
| Race and conflict behaviors | 8 | §29.2 |
| Recovery matrix rows | 16 | §29.3 |
| Human-approval triggers | 10 | §30.1 |
| Security threats | 16 | §31 |
| Error taxonomy **rows** | **49** | §33 |
| Error taxonomy **distinct class names** | **49** | §33 |
| Operator views | 13 | §34 |
| Framework compatibility matrix | 6 × 13 | §35 |
| Runtime modes | 7 | §36 |
| Deterministic scenarios | **42** (32 original + 10 additional) | §38, §38.1 |

Row and class counts for §33 are stated separately and are equal by
construction: the table carries exactly one class per row, and §33 requires that
property to be preserved.

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

1. **Exact primitive types only.** A value declared as a string, integer,
   boolean, or byte string MUST be exactly that primitive type. The required
   discipline is an **exact-type identity check**, not a subtype- or
   interface-compatible check: a value whose type is a *subtype* of the declared
   primitive does not satisfy the declaration. This applies to every primitive
   and is language-neutral; each implementation language binds it to its own
   exact-type test. *(Non-normative illustration: in Python the required test is
   `type(value) is str`, never `isinstance(value, str)`.)*
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

### 8.4 Run identity namespaces

MellyCore has more than one kind of run. A **loop run** is owned by
`[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]` and
`shared_context/loops/**`; an **agent run** is owned by this specification.
They are different concepts with different owners, different lifecycles, and
different identity forms, and they must never be confused.

`run_kind` is a closed vocabulary at the ledger boundary
(`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.1) with the members
`loop_run` and `agent_run`. Normative rules for the Agent Runtime:

| Rule | Requirement |
| --- | --- |
| Namespace | `run_id` uniqueness is scoped **within** one `run_kind`. Identity is the pair `(run_kind, run_id)`; a bare `run_id` is not a complete run reference at any trust boundary |
| Discriminator is mandatory | Every agent run identifier the runtime emits — in envelopes, handoffs, events, ledger records, audit records, and operator projections — carries `run_kind: agent_run` |
| Form | An agent `run_id` is opaque per §8.2 rule 3. It **MUST NOT** be constructed in, parsed as, or validated against the loop run-ledger form, and the loop form is neither adopted nor extended here |
| Forbidden substitution | An agent run is never represented as, projected onto, resolved as, counted as, or substituted for a loop run, and the reverse is equally prohibited. A cross-kind lookup denies with `RUN_KIND_MISMATCH`; it does not fall back or return empty |
| Collision prevention | Because uniqueness is per-namespace, two runs of different kinds may never collide; a value that would resolve in both namespaces is a `DIGEST_COLLISION_SUSPECTED`-class integrity event, not a match |
| Linkage, not reuse | A loop that causes an agent run records an explicit typed reference `triggering_run_ref = (run_kind, run_id)`. Identity is **referenced**, never **reused**. The agent run keeps its own identity, lifecycle, budget, and authorization |
| Ownership | This specification does not rename, absorb, extend, or supersede the Loop Operations model. Loop run identity, loop state, and the loop guard contracts remain exactly as their owners define them |

Sub-runs (§13) are agent runs and carry `run_kind: agent_run`; they are
distinguished from their parent by `sub_run_id` and explicit parentage, never by
a different kind.

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

### 9.1 Relationship to the authorization facts (normative)

These nine states and the eleven authorization facts of Section 14 answer
different questions and are **not** a one-to-one mapping. A separation state
asks *what exists*; an authorization fact asks *what is permitted*. The exact
correspondence is:

| # | Separation state | Corresponding fact | Note |
| --- | --- | --- | --- |
| 1 | Agent defined | Fact 1 | 1:1 |
| 2 | Package artifact exists | **none** | Existence of a build artifact is a precondition of verification, never an authorization. There is deliberately no fact 2 for it |
| 3 | Package verified | Fact 2 | 1:1 |
| 4 | Package installed | Fact 3 | 1:1 |
| 5 | Agent registered | Fact 4 | 1:1 |
| 6 | Runtime enabled | Fact 7 | 1:1 |
| 7 | Agent instantiated | **none** | Instantiation is a runtime mechanic performed only after facts 1–8 hold; it authorizes nothing |
| 8 | Run authorized | Fact 8 | 1:1 |
| 9 | Run active | **none** | Activity is observed evidence, never an authorization |

Facts 5, 6, 9, 10, and 11 have no separation state because they authorize a
tenant, a capability, a tool, a provider, and an operation rather than an
artifact's existence. The absence of a fact for states 2, 7, and 9 is
deliberate: it prevents an existence signal from being read as a grant.

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

**Projection direction and authority.** The Control Plane owns the
`lifecycle_status` vocabulary; this specification owns `run_state`. The mapping
in §12.2 projects `run_state` **onto** `lifecycle_status` in one direction only.
It is deliberately **lossy** — several `run_state` values legitimately share one
`lifecycle_status` — and `run_state` remains the authoritative field for every
runtime decision. No `lifecycle_status` value is ever reversed into a
`run_state`, and no runtime decision, authorization, transition, or gate is
taken on a projected value.

**Control Plane dependency (normative).** Every projected value in §12.2 is a
member of the Control Plane §8.1 lifecycle enum, and every projection respects
Control Plane §8.2. In particular, an executing agent run projects to
`lifecycle_status:running`, **never** to `lifecycle_status:active`, which §8.2
reserves for an effective policy or configuration and explicitly forbids for a
running agent. The `running` member was added to the Control Plane enum by
`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]` §6
because that vocabulary contained no member capable of expressing a live
execution; this specification defines no status value of its own, adds no
dimension, and introduces no local alias.

### 12.2 The seventeen run states

Every row states one Control Plane dimension and one canonical value from that
dimension's §8.1 enum. No row is ambiguous, and no row uses a value in a sense
its owner forbids.

| # | `run_state` | Terminal? | Meaning | Control Plane dimension | Canonical projected value | Owner evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `proposed` | No | A run has been requested; nothing validated | `lifecycle_status` | `draft` | CP §8.1 — progression not yet planned |
| 2 | `validated` | No | Envelope, package, and declarations are structurally valid | `lifecycle_status` | `planned` | CP §8.1 |
| 3 | `authorized` | No | The eight run-admission facts (§14) hold | `lifecycle_status` | `ready` | CP §8.1 — prepared, not started |
| 4 | `queued` | No | Admitted for scheduling; not started | `lifecycle_status` | `queued` | CP §8.1 |
| 5 | `starting` | No | Instantiation and bridge preparation in progress | `lifecycle_status` | `running` | CP §8.2 — live execution in progress |
| 6 | `running` | No | The agent is executing a step | `lifecycle_status` | `running` | CP §8.2 |
| 7 | `waiting_for_model` | No (waiting) | Awaiting a routing decision or model response | `lifecycle_status` | `running` | CP §8.2 — execution in progress, awaiting a machine result |
| 8 | `waiting_for_tool` | No (waiting) | Awaiting a tool result | `lifecycle_status` | `running` | CP §8.2 |
| 9 | `waiting_for_agent` | No (waiting) | Awaiting a handoff decision or sub-run | `lifecycle_status` | `running` | CP §8.2 |
| 10 | `waiting_for_operator` | No (waiting) | Awaiting a human decision | `lifecycle_status` | `blocked` | CP §8.1 — progression halted pending an external decision |
| 11 | `cancellation_requested` | No (pending) | Cancellation requested; not yet acknowledged or settled | `lifecycle_status` | `running` | CP §8.2 — the run has not stopped; nothing is settled |
| 12 | `reconciliation_required` | No (pending) | An external outcome is unknown and must be reconciled | `lifecycle_status` | `blocked` | CP §8.1 — an open obligation halts progression |
| 13 | `completed` | **Yes** | The run finished and its output contract was satisfied | `lifecycle_status` | `completed` | CP §8.1 |
| 14 | `failed` | **Yes** | The run finished without satisfying its output contract | `lifecycle_status` | `failed` | CP §8.1 |
| 15 | `cancelled` | **Yes** | Cancellation completed with **no** unknown external effect | `lifecycle_status` | `cancelled` | CP §8.1 |
| 16 | `timed_out` | **Yes** | A limit was reached with **no** unknown external effect | `lifecycle_status` | `failed` | CP §8.1 — no distinct timeout member; `run_state` carries the distinction |
| 17 | `blocked` | **Yes** | The run was refused and will not proceed under this authorization | `lifecycle_status` | `blocked` | CP §8.1 |

Projection notes, normative:

1. **Six `run_state` values project to `running`** — rows 5, 6, 7, 8, 9, and 11
   (`starting`, `running`, `waiting_for_model`, `waiting_for_tool`,
   `waiting_for_agent`, `cancellation_requested`). They are distinct runtime
   states and are never merged in `run_state`, in events, in the ledger, or in
   any operator view; only the coarse Control Plane dimension is shared.
2. **`waiting_for_operator` and `reconciliation_required` both project to
   `blocked`** and remain distinct `run_state` values with distinct meanings,
   distinct exits, and distinct operator obligations. §34 requires both to be
   displayed by `run_state`, never only by projection.
3. **`timed_out` projects to `failed`** because the Control Plane enum has no
   timeout member. The `run_state` retains the honest distinction, and §12.4
   rule 5 still forbids `timed_out` whenever an external outcome is unknown.
4. **No value projects to `active`.** `lifecycle_status:active` remains reserved
   for an effective policy or configuration (Control Plane §8.2) and is never
   produced by an agent run.
5. Every projected value is renderable by Control Plane §9.5, §9.7, and §9.10,
   whose Run lifecycle sets were extended for exactly this purpose.

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
| `waiting_for_model` | `running`, **`waiting_for_operator`**, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` |
| `waiting_for_tool` | `running`, **`waiting_for_operator`**, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` |
| `waiting_for_agent` | `running`, **`waiting_for_operator`**, `cancellation_requested`, `reconciliation_required`, `failed`, `timed_out`, `blocked` |
| `waiting_for_operator` | `running`, `cancellation_requested`, `failed`, `timed_out`, `blocked` |
| `cancellation_requested` | `cancelled`, `reconciliation_required`, `failed`, `completed` |
| `reconciliation_required` | `completed`, `failed`, `cancelled`, `blocked` |
| `completed`, `failed`, `cancelled`, `timed_out`, `blocked` | **none** |

**This table is closed.** A transition that does not appear in it is forbidden,
whether or not §12.4 names it. There are no implicit, derived, or
convenience transitions, and no transition may be reached by an unstated
intermediate hop.

`cancellation_requested → completed` is legal and required for the honest case
in which the run finished before cancellation took effect. It is never used to
report a cancelled run as successful.

### 12.3.1 Escalation to `waiting_for_operator` (normative)

`waiting_for_operator` has exactly four allowed predecessors: `running`,
`waiting_for_model`, `waiting_for_tool`, and `waiting_for_agent`. The three
waiting-state escalations exist because an in-flight wait can produce a result
that only a human may resolve; without them, the outcomes §23.6, §21.1, and
§20.3 mandate would be unreachable.

| Escalation trigger | Predecessor | Reason class recorded |
| --- | --- | --- |
| Routing returns multiple equally-ranked permitted candidates and no declared tie-breaker resolves them (§23.6) | `waiting_for_model` | `ROUTING_TIE_UNRESOLVED` |
| A tool invocation requires an operator approval that is not yet held (§21.1 stage 7) | `waiting_for_tool` | `APPROVAL_REQUIRED` |
| A handoff, sub-run, or context conflict requires operator adjudication (§17.3 rule 3, §20.3) | `waiting_for_agent` | `APPROVAL_REQUIRED` or the recorded conflict class |
| Any §30.1 trigger arising mid-step | `running` | The applicable §33 class |

Rules:

1. Every escalation appends the §12.5 evidence record, whose `reason_code`
   names the exact escalation trigger. An escalation without evidence is
   forbidden by §12.4 rule 9.
2. The runtime **never** resolves the escalated condition itself. It may not
   pick a candidate, approve an invocation, or adjudicate a conflict.
3. Release from `waiting_for_operator` requires a recorded operator decision
   that is action-, revision-, and time-bound under §30.2. An expired decision
   releases nothing; the run remains waiting until it expires by its own limit
   or is blocked.
4. Returning to `running` carries the operator decision reference. The run
   resumes at the step that escalated; it does not restart the attempt.
5. `reconciliation_required` deliberately has **no** transition to
   `waiting_for_operator`. It is already an operator-visible open obligation
   (§28 rule 5), and routing it through a waiting state would disguise an
   unresolved external outcome as an ordinary pause.

### 12.4 Forbidden transitions (normative)

1. Any transition out of a terminal state.
2. `proposed`, `validated`, or `queued` directly to `running`.
3. Any transition to `authorized` without all **eight run-admission facts** of
   Section 14.1. Facts 9, 10, and 11 are per-invocation facts and are neither
   evaluated nor satisfiable at run authorization (§14.3).
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
10. Any transition not listed in the §12.3 table, including any transition
    reached by an unstated intermediate hop.
11. Any transition to `waiting_for_operator` from a state other than the four
    predecessors named in §12.3.1, and any release from `waiting_for_operator`
    without a recorded, unexpired, action- and revision-bound operator decision.
12. Any resolution of a routing tie, tool approval, or context conflict by the
    runtime itself, by a silent fallback, by an arbitrary or random selection,
    or by a timeout that substitutes a default.

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

Registry §21.1's **eight provider facts remain exactly eight, unmodified**, and
this specification does not amend, restate, extend, or re-scope them. The
eleven facts below are Agent Runtime facts. All eleven are **conjunctive** and
**independently established, evidenced, and revoked**.

### 14.1 The eight run-admission facts

These eight are evaluated before a run may enter `authorized` (§12.2 row 3).

| # | Fact | Canonical owner | Evidence record | Subject | Action scope | Tenant scope | Environment scope | Revision binding | Expiry | Denial class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Agent defined** | Agent Registry | Agent definition record | `agent_definition_id` | The agent may be referenced at all | Tenant-scoped | All | — | Non-expiring; revocable by supersession | `AUTHORIZATION_DENIED` |
| 2 | **Package verified** | Future Agent Package Contract | Package verification evidence (integrity, provenance, signer, digest) | `package_revision_id` | This exact revision may be installed | Tenant-scoped | All | **This revision only** | Re-verification required on revision change | `PACKAGE_UNVERIFIED` |
| 3 | **Package installed** | Agent Registry | Installation record | `installed_agent_id` | This revision is installed here | Tenant-scoped | **One environment** | This revision only | Until uninstalled or superseded | `AUTHORIZATION_DENIED` |
| 4 | **Agent registered** | Agent Registry | Conforming current agent record | `agent_definition_id` + `installed_agent_id` | The definition is bound to the installed revision | Tenant-scoped | One environment | This revision only | Until deregistered or superseded | `AGENT_UNREGISTERED` |
| 5 | **Tenant runtime authorization** | **Agent Runtime** (this specification) | `tenant_agent_runtime_authorization` | `tenant_id` | This tenant may operate the Agent Runtime and cause agent runs | **One tenant** | **One environment** | — | Explicit `expires_at` or a declared non-expiring policy reference | `RUNTIME_AUTHORIZATION_DENIED` |
| 6 | **Agent capability authorization** | **Agent Runtime** (this specification) | `tenant_agent_capability_authorization` | `tenant_id` + `agent_definition_id` + one **agent capability class** | This tenant may run this agent for this declared capability | One tenant | One environment | Bound to the package revision whose `declared_capabilities` contain the class | Explicit `expires_at` or declared non-expiring policy | `CAPABILITY_AUTHORIZATION_DENIED` |
| 7 | **Runtime enabled** | Operator, recorded | Agent Runtime enablement record | `tenant_id` + `environment` | Agent runs may execute here at all | One tenant | One environment | — | Revocable at any time; revocation takes effect immediately | `RUNTIME_DISABLED` |
| 8 | **Run authorized** | Operator / policy, recorded | Run authorization record | This exact `run_id` | This exact run, under this exact envelope digest | One tenant | One environment | **`package_revision_id` + `envelope_revision_id` + `envelope_digest`** | Explicit expiry; revocable | `AUTHORIZATION_DENIED` / `RUN_AUTHORIZATION_EXPIRED` |

### 14.2 The three per-invocation facts

These three are evaluated **at the exact point of use**, never at run
authorization.

| # | Fact | Canonical owner | Evidence record | Subject | Action scope | Revision binding | Expiry | Denial class |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 9 | **Tool authorized** | Tool Gateway (§21) | Tenant/agent/tool authorization | One `tool_id` | One tool, at one pinned contract revision | Pinned tool contract revision | Per record | `TOOL_DENIED` |
| 10 | **Provider authorized** | **Provider Registry §21.1 evaluated by Integration Gateway §17** | The Registry's own eight-fact evaluation | One provider capability + scope | One provider operation proposal | Per Registry/Gateway records | Per Registry/Gateway records | `PROVIDER_DENIED` |
| 11 | **Operation approved** | Operator | Approval record (Control Plane §16.1, Gateway §18) | One exact typed target | One exact operation | `target_version` + `target_digest` + `package_revision_id` | Explicit expiry; non-replayable | `APPROVAL_REQUIRED` |

### 14.3 Rules

1. **No `ready` boolean.** No single field, computed property, aggregate,
   score, or cached view may stand for two or more facts. A schema doing so is
   non-conforming.
2. **No fact implies another.** Tenant runtime authorization does not authorize
   a capability; capability authorization does not enable the runtime; runtime
   enabled does not authorize a run; run authorized does not authorize a tool;
   tool authorized does not authorize a provider; provider authorized does not
   approve an operation.
3. **Evaluation points are fixed.** Facts 1–8 are run-admission facts and must
   all hold to enter `authorized`. Facts 9, 10, and 11 are per-invocation facts,
   evaluated at the point of tool use, provider proposal, and consequential
   operation respectively. A run authorization **never** pre-satisfies,
   pre-approves, or reserves facts 9, 10, or 11 for operations not yet proposed,
   and no run-admission fact is re-used as evidence for a per-invocation fact.
4. **Fact 10 delegates entirely** to Registry §21.1 and Gateway §17. The Agent
   Runtime never re-implements, caches past its inputs, summarizes, or
   second-guesses the eight provider facts, and never records a provider
   decision it did not receive from the Gateway.
5. **Runtime facts are not provider facts (normative separation).** Facts 5 and
   6 are Agent Runtime authorizations about operating the runtime and running an
   agent capability. They are **not** Registry facts 5 and 6, which are
   provider-scoped (`tenant_provider_authorization` and
   `tenant_capability_authorization`, both requiring a `provider_id` per
   Registry §21.3). Specifically:
   - A Registry `tenant_provider_authorization` never satisfies runtime fact 5,
     and a `tenant_agent_runtime_authorization` never satisfies Registry fact 5.
   - A Registry `tenant_capability_authorization` never satisfies runtime fact
     6, and a `tenant_agent_capability_authorization` never satisfies Registry
     fact 6.
   - Provider-side tenant authorization and provider-side capability
     authorization exist **only** inside fact 10.
   - An agent run that proposes no provider operation requires facts 1–8 only,
     never a `provider_id`, and never a Registry authorization record.
   A schema, evaluator, or record that satisfies one of these facts with the
   other's record type is non-conforming.
6. **Two capability vocabularies exist and are disjoint in use.** The **agent
   capability vocabulary** is the closed set of capability classes a package
   declares in `declared_capabilities` (§10.1); it is authorized by fact 6 and
   requested as `requested_capability` in the envelope. The **provider
   capability vocabulary** is the set of provider capability IDs owned by the
   Provider Registry; it is authorized only inside fact 10 and appears only in a
   provider operation proposal. Neither vocabulary is ever resolved, matched, or
   substituted against the other; an attempt to do so denies with
   `UNSUPPORTED_CAPABILITY`.
7. Facts 5, 6, 7, and 8 are separately revocable. Revoking any one denies
   without altering the evidence of the others, exactly as Registry §21.2 rule 3
   requires within its own set.
8. An `authorization_status` view MAY be computed at evaluation time. It is
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
| Routing | `model_routing_request_ref` (a request, never a model binding), `bound_routing_decision_ref` (nullable; present **only** when this revision was created to bind an already-issued routing decision — §15.4) |
| Context | `context_snapshot_refs[]`, `context_access_scope`, `redaction_policy_ref`, `context_staleness_policy_ref` |
| Memory | `memory_scope_refs[]`, `memory_write_scope` |
| Permissions | `tool_permission_refs[]`, `provider_permission_refs[]` |
| Limits | `max_steps`, `max_depth`, `max_wall_clock`, `max_input_tokens`, `max_output_tokens`, `max_concurrent_steps` |
| Authorization | `authorization_refs[]` (facts 1–10), `approval_refs[]` (fact 11) |
| Audit | `audit_intent_ref`, `audit_reservation_ref` |
| Cost | `cost_budget_ref`, `reserved_budget` |
| Behavior | `cancellation_policy_ref`, `retry_policy_ref`, `external_content_posture` |
| Integrity | `envelope_revision_id`, `supersedes_envelope_revision_id` (nullable), `envelope_digest` (canonical, per Section 8.3), `schema_version` |

### 15.2 Prohibited envelope contents (normative)

The envelope MUST NOT contain: credentials of any kind; raw secrets;
environment variables; provider tokens, keys, or session identifiers; OAuth
grants or codes; account identifiers; connection strings; or complete
sensitive context bodies where a reference is sufficient.

Sensitive context is carried **by reference**, resolved at the point of use
under the run's access scope, and never inlined into an envelope, a handoff, a
log, an event payload, an error message, or an audit record.

### 15.3 Immutability and the revision chain

An envelope revision is **immutable from the moment it is constructed** — not
merely from attempt start. It is never edited, patched, completed, or repaired
in place. An envelope whose `envelope_digest` does not reproduce is rejected
with `ENVELOPE_INTEGRITY_FAILED`.

A change of any kind produces a **new revision**, never a mutation:

1. The new revision receives a fresh `envelope_revision_id`, a fresh
   `envelope_digest`, and `supersedes_envelope_revision_id` pointing at its
   predecessor.
2. The superseded revision **remains stored, addressable, and auditable**. It is
   never deleted, overwritten, or tombstoned.
3. Section 14.1's eight run-admission facts are **re-evaluated in full** against
   the new revision. A prior authorization does not carry forward.
4. Any operator approval bound to the superseded revision's digest is stale by
   construction and authorizes nothing for the new revision
   (`APPROVAL_STALE`, §30.2, Scenario 32).
5. If the run has already started, a new revision additionally requires a new
   attempt with a new `attempt_id`.

There is no partial, provisional, or "to be completed" envelope field. Every
field is fixed at construction; a field whose value is not yet knowable is
absent or `null` **and stays that way for the life of that revision**.

### 15.4 Authorization sequencing (normative)

This section fixes the temporal order so that no field can be required before
it is knowable, and no decision can silently alter an authorized artifact.

| # | Step | Produces | State |
| --- | --- | --- | --- |
| 1 | Run request | Run intent, `run_id`, `run_kind: agent_run` | `proposed` |
| 2 | Initial validation | **Envelope revision 1** — structurally valid, digest-bound, `bound_routing_decision_ref: null` | `validated` |
| 3 | Pre-authorization routing request (**only** when tenant policy requires the model bound before authorization) | Routing request artifact | `validated` |
| 4 | Routing decision | Immutable, digest-bound routing decision artifact | `validated` |
| 5 | Resolved revision | **Envelope revision 2** — carries `bound_routing_decision_ref`, supersedes revision 1, new digest | `validated` |
| 6 | Renewed validation | Structural re-validation of the current revision | `validated` |
| 7 | Authorization | Facts 1–8 evaluated against the **current revision's exact digest** | `authorized` |
| 8 | Dispatch eligibility | Admission for scheduling | `queued` |

Steps 3–5 are **skipped entirely** in the ordinary case. Then the authorized
artifact is revision 1 with `bound_routing_decision_ref: null`, and routing is
performed per step during execution.

**Per-step routing during execution.** Once an attempt is running, a routing
decision is a **step-scoped artifact**, not an envelope field. It carries
`run_id`, `attempt_id`, `step_id`, its own canonical digest, and its
authorization references, and it is bound to the step and recorded in the Run
Ledger. It never enters, alters, or re-digests the envelope. This is why
`bound_routing_decision_ref` can only ever describe a decision issued **before**
authorization: a decision issued after authorization is bound to a step, never
to the envelope.

Invariants (normative):

1. **An authorized envelope revision is never mutated.** Not to add a routing
   decision, not to record a result, not for any reason.
2. **Adding or changing a bound routing decision creates a new digest-bound
   revision**, and that revision requires renewed validation and renewed
   authorization under §15.3 rules 3–5.
3. **The prior revision and the prior routing decision remain auditable**, with
   the supersession link recorded in both directions.
4. **A stale approval cannot authorize a changed decision.** An approval bound
   to revision *N*'s digest is void for revision *N+1*.
5. A per-step routing decision that would cross a §23.4 boundary — sensitivity,
   provider, quality floor, cost ceiling, or the approved-model set — is not a
   step decision at all: it requires a new routing decision, a new envelope
   revision, a new attempt, and renewed authorization, plus a fresh approval
   where policy demands one.
6. An envelope revision whose `supersedes_envelope_revision_id` chain contains a
   cycle, a gap, or an unresolvable predecessor is rejected with
   `ENVELOPE_INTEGRITY_FAILED`.

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
   refreshes; a run holding one is told, and the outcome follows §17.4
   deterministically (Scenario 25).
5. **Sensitivity does not decay.** Derived context inherits the highest
   sensitivity of its sources unless an explicit, recorded redaction
   transformation lowers it.

### 17.4 Snapshot staleness policy (normative)

Canonical context truth is owned by the Shared Context Layer. This section
governs only what the **Agent Runtime** does with a snapshot it already holds.
It adds no admission rule and changes no provenance or sensitivity semantics.

Every run carries a `context_staleness_policy_ref` (§15.1). A staleness policy
is a declared, versioned, digest-bound artifact containing:

| Field | Meaning |
| --- | --- |
| `policy_revision` | Exact version of this policy |
| `max_snapshot_age` | Maximum acceptable age, or `null` for "age is never sufficient grounds" |
| `non_material_field_set` | The **explicitly enumerated** fields whose change is non-material for this run. Absent or empty means *every* change is material |
| `refresh_permitted` | Whether the runtime may re-read on a non-material change |
| `operator_exception_permitted` | Whether an operator may authorize use of a stale snapshot |

**Materiality is determined by enumeration, never by inference.** A change is
non-material only if every changed field is named in `non_material_field_set`.
Any change to a field the run's authorization, read scope, or output contract
depends on is material regardless of enumeration.

Detection compares the held `context_snapshot_id` and its canonical digest
against the current source revision under §8.3.

| # | Condition | Detection | Resulting `run_state` | Reason class | Evidence | Operator |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Current** — digest and source revision match, and `max_snapshot_age` is unset or unexceeded | Digest equality | `running` — proceed | n/a | Context read record | No |
| 2 | **Stale, non-material, refresh permitted** — every changed field is enumerated non-material and `refresh_permitted` is true | Digest mismatch, changed-field set ⊆ `non_material_field_set` | `running` — a **new** snapshot is read, receiving a **new** `context_snapshot_id` | n/a | §19 trace record with both digests and the changed-field set | No |
| 3 | **Stale and material** — any changed field is material | Digest mismatch, changed-field set ⊄ `non_material_field_set` | `blocked` | `STALE_STATE` | Held digest, current digest, changed-field set | Yes — a new run or new envelope revision is required |
| 4 | **No declared policy** — `context_staleness_policy_ref` absent, unresolvable, or expired | Reference resolution failure | `blocked` | `STALE_STATE` | Missing or expired policy reference | Yes |
| 5 | **Source unavailable** — currency cannot be established | Source read failure or `freshness_state:unknown` | `blocked` | `STALE_STATE` with `evidence_state:unknown` | Attempted source reference and failure class | Yes |
| 6 | **Conflicting revision** — two current revisions contend for one source | Conflict detection (§17.3 rule 3) | `waiting_for_operator` | Recorded conflict class | Both revisions with provenance and precedence | **Yes — adjudication** |

Rules:

1. **A stale snapshot is never used automatically.** Only condition 1 proceeds
   on the held snapshot; only condition 2 proceeds at all, and only on a freshly
   read replacement.
2. **Refresh is replacement, never mutation.** A refreshed snapshot is a new
   immutable snapshot with a new identity. The prior snapshot and both digests
   remain recorded, and a §19 trace record is appended for the transfer.
3. **A material change invalidates the envelope's context binding.** The run's
   authorization was granted against `context_snapshot_refs[]` at a specific
   revision; a materially different context is a different run input. Proceeding
   requires a new envelope revision and renewed authorization under §15.3 — not
   a re-read.
4. **Absence fails closed.** Conditions 4 and 5 block. There is no default
   policy, no default staleness tolerance, and no substituted, cached, partial,
   or nearest-available context.
5. **An operator exception is explicit and bounded.** Where
   `operator_exception_permitted` is true, an operator may authorize the use of
   a specific stale snapshot by its exact `context_snapshot_id` and digest, for
   one named run, time-bound and recorded under §30.2. It never generalizes to
   another snapshot, run, or class, and it never converts a material change into
   a non-material one.
6. **Every outcome is auditable**, including conditions that proceed. A staleness
   evaluation that produced no change is still recorded with its policy revision
   and both digests.

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
a derived record — appends an immutable trace record of **exactly seventeen
fields**:

| # | Field | Purpose |
| --- | --- | --- |
| 1 | `source_agent_id` | Which agent released the context |
| 2 | `destination_agent_id` | Which agent is the intended recipient |
| 3 | `source_run_id` | Which run released it |
| 4 | `destination_run_id` | Which run receives it, so every transfer is attributable to both runs and cross-run flow is auditable under §29.1 run isolation |
| 5 | `source_step_id` | Which step released it |
| 6 | `context_class` | The class transferred |
| 7 | `source_reference` | The exact addressable source |
| 8 | `canonical_hash` | Digest under §8.3 |
| 9 | `transformation_id` | Which transformation, if any, was applied |
| 10 | `redaction_applied` | Whether redaction occurred |
| 11 | `sensitivity_level` | From the canonical vocabulary |
| 12 | `access_decision` | The scope evaluation result at the point of use |
| 13 | `acceptance_state` | `accepted` \| `rejected` |
| 14 | `rejection_reason` | Nullable; required when rejected |
| 15 | `observed_at` | When the transfer was observed |
| 16 | `recorded_at` | When the record was durably appended |
| 17 | `trace_id` | End-to-end causal trace |

`destination_run_id` is `null` only for a transfer into a derived record within
the same run, where it is the source run by construction.

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

**Exactly twelve** required contents: `source_identity` (agent, run, attempt,
step), `intended_recipient`, `purpose`, `allowed_action_scope`,
`context_refs[]`, `output_contract_ref`, `budget`, `deadline`,
`cancellation_behavior`, `provenance`, `authorization_evidence_refs[]`,
`handoff_digest` (Section 8.3).

A `broadcast_proposal` additionally carries `acceptance_deadline` and
`acceptance_version` (§20.4).

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

### 20.4 Concurrent acceptance (normative)

A `broadcast_proposal` is offered to several eligible recipients, so two or more
may attempt acceptance at the same instant. That race is resolved
deterministically.

**Model: single-winner with an atomic acceptance decision.** A broadcast is
never multi-accept, never quorum-based, and never arbitrated by a policy the
runtime would have to interpret.

**Acceptance transaction.** Acceptance is a two-part operation, and only the
second part is decisive:

1. The receiving agent's runtime independently evaluates §14.1 facts 1–8 for the
   receiving side (§20.3 rule 1). Failure ends the attempt here; no claim is
   made.
2. On success it submits an acceptance **claim** as an atomic compare-and-set on
   the handoff record, keyed by `handoff_id`, with `acceptance_version` as the
   expected-version precondition — the same optimistic-concurrency mechanism
   §29.2 already mandates for shared derived records.

Exactly one claim can satisfy the precondition. That recipient is the winner.
Every other claim fails the precondition and is denied.

| # | Condition | Outcome | Reason class | Recipient run | Budget |
| --- | --- | --- | --- | --- | --- |
| 1 | Two or more simultaneous claims | Exactly one wins the compare-and-set | Winner: n/a. Losers: `HANDOFF_ALREADY_ACCEPTED` | Winner's run reaches `authorized`; losers create **no run at all** | Winner draws the reservation; losers release theirs |
| 2 | Claim after a winner exists | Deny | `HANDOFF_ALREADY_ACCEPTED` | None | Nothing drawn |
| 3 | Claim after `acceptance_deadline` | Deny | `HANDOFF_EXPIRED` | None | Reservation released to the parent |
| 4 | Claim after the broadcast was cancelled or withdrawn | Deny | `HANDOFF_WITHDRAWN` | None | Reservation released |
| 5 | Claim when the parent's remaining reserve cannot cover the carved budget | Deny **before** any run is created | `BUDGET_EXCEEDED` | None | Nothing drawn |
| 6 | Claimant lacks a required §14.1 fact | Deny at part 1; no claim is submitted | The unmet fact's class | None | Nothing drawn |
| 7 | Duplicate claim from the recipient that already won | Suppressed; the recorded decision is returned | n/a — duplicate suppressed | Unchanged | Unchanged |

Rules:

1. **Racing grants nothing.** Winning the compare-and-set decides *who* proceeds,
   never *with what*. The winner's effective scope remains the intersection of
   the handoff's `allowed_action_scope` and its own authorizations (§20.3 rule
   2). No permission, context class, tool, provider, model, or budget is widened
   by having accepted first.
2. **Budget is reserved once.** A broadcast reserves the carved budget from the
   parent once, at broadcast creation. Only the winner draws it. On expiry,
   withdrawal, or no acceptance, the reservation is released to the parent in
   full and the release is recorded.
3. **Losing is recorded, not erased.** Every claim and every denial is appended
   append-only with its reason class. A losing recipient's evaluation evidence
   is retained.
4. **No partial starts.** A losing claimant never instantiates an agent, never
   reads context under the handoff, and never emits a step.
5. **Cancellation propagates to the winner only**, per the handoff's declared
   `cancellation_behavior`. Losers have nothing to cancel.
6. **Duplicate suppression is unchanged** (§20.3 rule 4): identity remains the
   canonical digest of source identity, recipient, purpose, scope, context
   references, and output contract.
7. If the atomic decision boundary cannot be established — the handoff record is
   unreachable or its version cannot be read — **no acceptance occurs**. The
   claim denies and the run is not created. There is no optimistic acceptance
   pending confirmation.

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

**Reachability (normative).** A run awaiting a routing decision is in
`waiting_for_model` (§12.2 row 7). The transition
`waiting_for_model → waiting_for_operator` is explicitly permitted by §12.3 and
governed by §12.3.1, so the outcome this section mandates is reachable by a
single, listed transition. No intermediate hop through `running` is used,
implied, or permitted.

The escalation appends the §12.5 evidence record with
`reason_code: ROUTING_TIE_UNRESOLVED`, `actor: runtime`, and evidence
references to the routing request, the complete tied candidate set, and the
applied rules and precedence.

Resolution rules:

1. The runtime **never** breaks the tie. It may not select, rank, prefer,
   sample, or default to any candidate.
2. The operator's decision selects one candidate **from the recorded tied set
   only**. A candidate outside that set is outside the authorized set and denies
   with `MODEL_UNAUTHORIZED`.
3. The decision is action-bound, revision-bound, and time-bound under §30.2. An
   expired decision releases nothing.
4. On release, the run returns to `running` carrying the operator decision
   reference and resumes at the escalating step (§12.3.1 rule 4).
5. If the operator declines, or the decision expires, the run transitions to
   `blocked` with `ROUTING_TIE_UNRESOLVED`. A tie is **never** resolved by
   timeout, by silent fallback, or by a default model.
6. Where the operator's selection crosses a §23.4 boundary, it is an override,
   not a tie-break, and additionally follows §15.4 invariant 5.

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

   `INSUFFICIENT_PRICING_DATA` is an **Agent Runtime-layer class**, owned by
   this specification and enumerated in §33. It names the runtime-layer
   condition "this run's cost cannot be established from available pricing
   evidence". It does **not** redefine cost semantics: the underlying rules that
   an estimate is never a measured charge, that zero never means unknown, and
   that a budget check over unmeasured values reports `unenforceable` rather
   than `pass` remain owned by
   `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.2–§5.3 and Control
   Plane §19, and are reused unchanged.
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

### 25.1 Record identity (normative)

The Agent Runtime's run/attempt/step model and the canonical ledger's record
identity are reconciled by
`[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5.1 and §5.9, as amended by
`[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]` §8. This
specification **consumes** that identity model and does not define one.

Every ledger record the Agent Runtime emits carries:

| Field | Value the runtime supplies |
| --- | --- |
| `ledger_record_id` | The record's own stable identity — the **deduplication identity** |
| `run_kind` | `agent_run`, always (§8.4) |
| `run_id` | The logical run |
| `attempt_id` | The attempt this record belongs to — **always present** for an agent run |
| `step_id` | The step, where the record is step-scoped |
| `sequence` | Monotonic per attempt (§26.3 rule 3) |
| `observed_at` / `recorded_at` | Separate, never merged (§12.5) |

Consequences, all owned by AI Operations §5.9 and reused here unchanged:

1. **Deduplication cannot collapse attempts.** Records sharing a `run_id` but
   differing in `attempt_id` are distinct records and are never deduplicated.
   Only identical `ledger_record_id` values deduplicate.
2. **A retry produces a new `attempt_id`**, so its records are additive. The
   original attempt's records remain intact, addressable, and independently
   readable (§13 rule 1).
3. **A replay produces a new `run_id`** with a recorded link to
   `source_run_id`, never a second attempt of the source run.
4. **Model, provider, and outcome are attempt-level attributions.** Two attempts
   of one run may legitimately record different models, providers, and outcomes,
   and both are true of their own attempt.
5. **A logical-run summary is derived, never stored as a replacement.** It never
   erases, supersedes, hides, or stands in for attempt records. Where attempts
   disagree, the summary reports the disagreement and its basis rather than
   selecting one attempt as the run's truth.
6. **Ordering evidence is explicit.** Sequence gaps surface as
   `evidence_state:partial` with the last confirmed sequence; a gap is never
   rendered as quiet.

The Agent Runtime does **not** own, operate, or define a second run ledger. Any
design in which runtime evidence lives outside the canonical Unified Run Ledger
is non-conforming.

### 25.2 Rules

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
| Concurrent broadcast acceptance | Single-winner atomic compare-and-set on the handoff record; losers denied with `HANDOFF_ALREADY_ACCEPTED`, no run created, reservations released (§20.4) |
| Runtime-instance loss | Orphaned runs are claimed only by a recorded takeover; any state in which an external effect could be in flight resolves to `reconciliation_required` (§29.3) |

### 29.3 Runtime restart and recovery (normative)

A `runtime_instance_id` identifies one coordinator instance (§8.1). An instance
can be lost — crash, host failure, or shutdown — while an attempt it owned may
still have external work in flight. This section fixes what happens next. The
*persistence mechanism* remains deferred (§41.3); the *safe-state requirement*
does not.

**Durable evidence expected before restart.** §12.5 requires every transition to
be durably appended with `recorded_at` before it is effective, and §25.1
requires every ledger record to carry `run_id`, `attempt_id`, and monotonic
`sequence`. The **last durably recorded transition** is therefore authoritative
for recovery. Evidence that was observed but not durably appended is treated as
absent, never as inferred.

**Takeover is explicit.** A new instance never adopts a run implicitly. It
performs a recovery scan of runs whose owning `runtime_instance_id` is lost and,
for each, appends a **takeover record** carrying the prior and new
`runtime_instance_id`, the last durable `run_state`, `attempt_id`, last
confirmed `sequence`, and the recovery decision below. A run without a takeover
record is not owned and is not advanced by anyone.

**External status query.** Where the framework bridge supports it, the runtime
MAY query bridge status for the attempt. A definitive answer is evidence. An
unsupported query, an error, a timeout, or an ambiguous answer is **not**
evidence of absence and yields `unknown`.

| # | Last durable `run_state` | Authoritative external status | Resulting `run_state` | Dispatch allowed | Reconciliation | Operator |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `proposed`, `validated`, `authorized` | n/a — nothing dispatched | Unchanged | Yes, after re-evaluating facts 1–8 | No | No |
| 2 | `queued` | n/a — nothing dispatched | `queued` | Yes, after re-evaluating facts 1–8 | No | No |
| 3 | `starting` | Definitive: never reached the framework | `queued` | Yes — **same** attempt | No | No |
| 4 | `starting` | `unknown` | `reconciliation_required` | **No** | **Yes** | Yes |
| 5 | `running` | Definitive: no external call in flight | `running` | Yes — **same** attempt, resuming at the last confirmed step | No | No |
| 6 | `running` | `unknown` | `reconciliation_required` | **No** | **Yes** | Yes |
| 7 | `waiting_for_model` / `waiting_for_tool` | Definitive: request never transmitted | Return to `running` | Yes — **same** attempt | No | No |
| 8 | `waiting_for_model` / `waiting_for_tool` | Definitive: completed, result retrievable | Return to `running` with the retrieved result recorded | Yes — **same** attempt | No | No |
| 9 | `waiting_for_model` / `waiting_for_tool` | `unknown` | `reconciliation_required` | **No** | **Yes** | Yes |
| 10 | `waiting_for_agent` | Sub-run's own last durable state is definitive | Follows the sub-run's recovered state | Per sub-run | Only if the sub-run requires it | Per sub-run |
| 11 | `waiting_for_agent` | Sub-run state `unknown` | `reconciliation_required` | **No** | **Yes** | Yes |
| 12 | `waiting_for_operator` | n/a — nothing external in flight | `waiting_for_operator` | No — still waiting | No | Already involved |
| 13 | `cancellation_requested` | Definitive: no effect occurred or all were reverted | `cancelled` | No | No | No |
| 14 | `cancellation_requested` | `unknown` | `reconciliation_required` | **No** | **Yes** | Yes |
| 15 | `reconciliation_required` | Any | Unchanged | **No** | **Yes** — still open | Yes |
| 16 | Any terminal state | Any | Unchanged | No | No | No |

Rules:

1. **No unknown attempt is ever blindly redispatched.** Rows 4, 6, 9, 11, and
   14 forbid dispatch outright. This is the same rule as §28's unsafe-retry
   prohibition, applied to recovery.
2. **Resumption within the same attempt is permitted only when no external
   effect could be in flight** — rows 3, 5, 7, and 8, each requiring a
   *definitive* external status. Resuming preserves `attempt_id` and continues
   the monotonic `sequence` from the last confirmed value.
3. **A new attempt is required** whenever reconciliation establishes what
   happened and the run may safely proceed. The new attempt receives a new
   `attempt_id`; the interrupted attempt's evidence remains intact and is never
   reused, rewritten, or continued.
4. **Duplicate dispatch is prevented** by attempt identity and by the §28
   idempotency-key state: a recovered attempt never re-issues a request whose
   idempotency key is already recorded as transmitted.
5. **Operator escalation** is required for every `reconciliation_required`
   outcome. The obligation is visible until resolved (§28 rule 5).
6. **Permanent block** applies when reconciliation cannot establish the external
   outcome and the operator declines to authorize a new attempt: the run
   transitions to `blocked` with `EXTERNAL_OUTCOME_UNKNOWN` recorded, and the
   unresolved obligation is retained rather than closed.
7. **Recovery never revives a terminal run** (row 16), and never rewrites,
   backfills, or re-times any prior record.
8. If the durable evidence itself is unreadable or internally inconsistent, the
   run is `blocked` with `evidence_state:unknown`; it is never reconstructed by
   inference.

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
| `AUTHORIZATION_DENIED` | A runtime authorization fact (1, 3, or 8) is unmet | No |
| `RUNTIME_AUTHORIZATION_DENIED` | Fact 5 unmet — no `tenant_agent_runtime_authorization` for this tenant and environment. Distinct from `PROVIDER_DENIED`, which covers provider-side tenant authorization inside fact 10 | No |
| `CAPABILITY_AUTHORIZATION_DENIED` | Fact 6 unmet — no `tenant_agent_capability_authorization` for this tenant, agent, and agent capability class | No |
| `RUN_KIND_MISMATCH` | A run reference was resolved across identity namespaces, or a bare `run_id` was presented without its `run_kind` (§8.4) | No |
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
| `INSUFFICIENT_PRICING_DATA` | Cost cannot be established from available pricing evidence; the value is `null`, never `0`, and any budget over it is `unenforceable` (§24 rule 2) | No |
| `STEP_LIMIT_EXCEEDED` | The step containment limit was reached | No |
| `DEPTH_LIMIT_EXCEEDED` | The delegation-depth containment limit was reached | No |
| `LOOP_DETECTED` | A repeated-state or handoff cycle was detected | No |
| `STALE_STATE` | A held context snapshot is no longer current and §17.4 does not permit proceeding, or an expected-version precondition failed. Adopted from Gateway §25.2 unchanged | No |
| `HANDOFF_ALREADY_ACCEPTED` | A broadcast acceptance claim lost the atomic decision (§20.4) | No |
| `HANDOFF_EXPIRED` | An acceptance claim arrived after `acceptance_deadline` | No |
| `HANDOFF_WITHDRAWN` | An acceptance claim arrived after the handoff was cancelled or withdrawn | No |
| `RUNTIME_INSTANCE_LOST` | The owning runtime instance was lost; recovery per §29.3 applies | No |
| `TENANT_ISOLATION_VIOLATION` | A cross-tenant reference was attempted | No |
| `ENVELOPE_INTEGRITY_FAILED` | `envelope_digest` did not reproduce | No |
| `DIGEST_COLLISION_SUSPECTED` | A canonical-identity collision was detected | No |
| `PROVENANCE_VERIFICATION_FAILED` | Provenance evidence did not verify | No |
| `APPROVAL_CONFLICT` | Two approvals contend for one exact target binding | No |
| `BRIDGE_UNSUPPORTED_BEHAVIOR` | A required behavior is unrepresentable in this bridge | No |
| `BRIDGE_FAILURE_UNCLASSIFIED` | A bridge failure could not be mapped | No |

**Row count and class count are distinct and are both stated.** The table above
has **49 rows and 49 distinct Agent Runtime-layer class names** — one row per
class, with no row carrying more than one class. Any future amendment MUST
preserve the one-row-one-class property so the two counts can never diverge
again, and MUST restate both numbers.

`STALE_STATE` is adopted unchanged from Gateway §25.2 and is listed here only
because the Agent Runtime raises it at a non-provider boundary (§17.4, §29.2).
Listing it neither redefines nor forks the Gateway class. The Gateway classes
`CONTRACT_CONFLICT`, `APPROVAL_STALE`, `AUDIT_RESERVATION_FAILED`,
`PARTIAL_APPLICATION`, `INDETERMINATE`, and `INJECTION_SUSPECTED` are likewise
adopted unchanged, are **not** restated in this table, and remain owned by
`[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §25.2.

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

**Projection rules for operator surfaces (normative).**

1. Every view that displays a run MUST display its `run_state` — the
   authoritative field — and MAY additionally display the projected
   `lifecycle_status`. A view that shows only the projection is non-conforming,
   because the projection is deliberately lossy (§12.2).
2. The six `run_state` values projecting to `lifecycle_status:running` MUST
   remain individually distinguishable in the Active-runs and Waiting-states
   views. "Running" is never rendered as a single undifferentiated bucket.
3. `waiting_for_operator` and `reconciliation_required` both project to
   `blocked` and MUST be separated in the Blocked-runs view, because one awaits
   a decision and the other carries an unresolved external obligation.
4. No operator surface may display `lifecycle_status:active` for an agent run.
   `active` remains reserved for an effective policy or configuration
   (Control Plane §8.2).
5. Filtering, sorting, and querying by the projected dimension MUST NOT be the
   only way to reach a run; `run_state` is filterable in its own right.

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
| 15 | Routing returns multiple equal candidates | No declared tie-breaker resolves; run is in `waiting_for_model` | `waiting_for_operator` **via the listed `waiting_for_model → waiting_for_operator` transition** (§12.3, §12.3.1) | Escalate; no arbitrary pick, no timeout default | `ROUTING_TIE_UNRESOLVED` | Request, complete tied candidate set, applied rules, escalation evidence | No |
| 16 | Cost estimate exceeds budget | Estimate > budget or reservation | `blocked` | Deny **before** execution | `BUDGET_EXCEEDED` | Estimate, basis, budget, reservation | No |
| 17 | Tool output contains prompt injection | Untrusted tool result, instruction-shaped | `running` | Flag; continue treating as data; no policy change | `INJECTION_SUSPECTED`; quarantine → `EXTERNAL_CONTENT_REJECTED` | Content-free security event + tool invocation ref | No |
| 18 | Agent output contains instructions for another agent | Untrusted agent-to-agent content | Recipient `running` | Treat as data; not an authorization | `INJECTION_SUSPECTED` | Context-flow trace + security event | No |
| 19 | Cancellation during a model call | Request sent; response state unknown | `reconciliation_required` | Local stop; **not** `cancelled` | `CANCELLATION_INCOMPLETE` + `EXTERNAL_OUTCOME_UNKNOWN` | Cancellation request, ack state, in-flight refs | **Yes** |
| 20 | Cancellation during an external tool call | Consequential tool in flight | `reconciliation_required` | Local stop; **not** `cancelled` | `CANCELLATION_INCOMPLETE` | Same, plus tool invocation ref | **Yes** |
| 21 | Timeout with unknown external outcome | Limit reached; effect unknown | `reconciliation_required` | **Not** `timed_out` | `EXTERNAL_OUTCOME_UNKNOWN` | Limit, elapsed, in-flight refs | **Yes** |
| 22 | Safe idempotent retry | Read-only or provably idempotent; prior effect known absent | `running` | New attempt under the same authorization | n/a | New `attempt_id`; original attempt intact | No |
| 23 | Unsafe consequential retry | Consequential; outcome unknown | `reconciliation_required` | Refuse retry | `UNSAFE_RETRY_REFUSED` | Key state, prior attempt, obligation | **Yes** |
| 24 | Duplicate handoff | Identical handoff digest already decided | Unchanged | Return recorded decision; no re-execution | n/a — duplicate suppressed | Duplicate-suppression record referencing the original | No |
| 25 | Stale context snapshot | Snapshot digest/version no longer current; outcome fixed by the §17.4 condition table | **§17.4 cond. 2** (every changed field enumerated non-material **and** `refresh_permitted`): `running` on a **new** snapshot. **All other cases** — material change, absent or expired policy, or unavailable source: `blocked`. Conflicting revisions: `waiting_for_operator` | Never silently refresh; never substitute; a material change additionally requires a new envelope revision and renewed authorization | `STALE_STATE` (cond. 3–5); recorded conflict class (cond. 6) | Policy revision, held vs. current digest, changed-field set, condition number | No |
| 26 | Conflicting context proposals | Two proposals contend | `waiting_for_operator` | Surface both; auto-apply neither | n/a — conflict recorded | Both proposals, provenance, precedence | No |
| 27 | Malicious `str` subclass at a digest boundary | Value passes shape checks; `type(v) is str` fails | `blocked` | Reject, or canonically convert **before** hashing | `INVALID_CANONICAL_TYPE` | Field path + class; **no value echo** | No |
| 28 | Two distinct inputs attempt a digest collision | Distinct canonical bytes → one digest, or two values → one encoding | `blocked` | Quarantine both; block dependents | `DIGEST_COLLISION_SUSPECTED` | Both encodings by reference, algorithm, trace | No |
| 29 | Provider authentication mode unresolved (`P2-04`) | Registry mode vs. required class unreconciled | `blocked` | Deny; do **not** infer a mode | `PROVIDER_DENIED` with `CONTRACT_CONFLICT` inward | Registry ref, required class, unresolved-finding ref | No |
| 30 | Bridge reports unsupported cancellation | `CANCELLATION_UNSUPPORTED` returned | `reconciliation_required` if anything in flight, else `cancelled` | Forced local stop; no guarantee claimed | `CANCELLATION_UNSUPPORTED` | Bridge report + in-flight inventory | **Yes**, if in flight |
| 31 | Package revision changes after authorization | Authorized revision ≠ installed revision | `blocked` | Deny; never silently upgrade | `PACKAGE_MISMATCH` | Both revision IDs and digests | No |
| 32 | Operator approval targets an older revision | Approval binding version/digest ≠ current | `blocked` | Deny; require a fresh decision | `APPROVAL_STALE` (Gateway class) | Complete approval binding vs. current target | No |

### 38.1 Additional scenarios (33–42)

Added by `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001` from the
adversarial replay set of
`[[../research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001]]` §42.
Each resolves without architectural interpretation.

| # | Scenario | Relevant facts | Expected `run_state` | Decision | Reason class | Audit record | Reconciliation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 33 | Framework emits an unknown event type | Bridge cannot map the event (§16 `stream_events`, §26.3 rule 5) | Unchanged | Emit an explicit `unmapped` event carrying the bridge's raw category as untrusted data; never drop, never guess | n/a — `unmapped` is a valid event | `unmapped` event with bridge identity and raw category | No |
| 34 | Framework writes native memory outside the bridge | §11.2 rules 1 and 6; §18 rule 2; §29.1 framework-process isolation | Unchanged | Contained as memory category 2 at most; bridge-local; never canonical, never cross-run without explicit normalized admission, never cross-tenant; discarded at attempt end | `BRIDGE_UNSUPPORTED_BEHAVIOR` where the behavior is required and unrepresentable | Bridge report; containment outcome; no memory content | No |
| 35 | Agent requests a model outside the approved provider set | Facts 1–8 ✓; candidate outside the authorized set (§23.2, §23.4) | `blocked` | Deny the step; **no model call**; never substitute a permitted neighbour | `MODEL_UNAUTHORIZED` | Routing request, requested model, authorized set, rejection reason | No |
| 36 | Agent requests a provider operation while provider registration is unresolved | Fact 10 unmet; Registry mode vs. required class unreconciled (`P2-04`, §22.5) | `blocked` | Deny; **never infer** an authentication mode; the Cloudflare constraint is not discharged | `PROVIDER_DENIED` with `CONTRACT_CONFLICT` inward | Proposal, Registry reference, required class, unresolved-finding reference | No |
| 37 | Handoff references a superseded package revision | Handoff carries revision *N*; installed revision is *N+1* (§8.2 rule 6, §10.2 rule 4) | Recipient `blocked` | Recipient re-evaluates facts 2–4 against the **current installed** revision and denies; never silently upgrade or downgrade | `PACKAGE_MISMATCH` | Both revision IDs and digests; handoff digest; explicit rejection | No |
| 38 | Approval expires while a run waits in a queue | Fact 8 or fact 11 expired during `queued` (§6 principle 3, §14.3 rule 3, §30.2) | `blocked` | Re-evaluate facts 1–8 at dispatch; expired authority authorizes nothing; deny **before** `starting` | `RUN_AUTHORIZATION_EXPIRED`, or `APPROVAL_REQUIRED` where fact 11 lapsed | Expiry timestamp, binding, dispatch-time evaluation record | No |
| 39 | Two agents propose conflicting canonical-state updates | Two proposals contend for one canonical target (§17.3 rule 3, §29.2) | `waiting_for_operator` **via `waiting_for_agent → waiting_for_operator`** or `running → waiting_for_operator` (§12.3.1) | Record both; auto-apply neither; surface with provenance and precedence; the runtime never picks a winner | n/a — conflict recorded | Both proposals, provenance, precedence, escalation evidence | No |
| 40 | Duplicate model responses arrive out of order | Two deliveries for one `model_invocation_id`; `sequence` non-monotonic (§8.1, §26.3 rules 3–4, §28) | Unchanged | Suppress the duplicate against the invocation identity; order by `sequence`; report gaps as `evidence_state:partial` with the last confirmed sequence; never merge, never reorder silently | n/a — duplicate suppressed | Both delivery records, `sequence` evidence, suppression reference | No |
| 41 | Cancellation and completion race | Cancellation requested while the run was completing (§29.2 cancellation-race row, §12.3) | `completed` when the run finished first **and** no external effect is unknown; otherwise `reconciliation_required` | Record the honest terminal state with the cancellation request retained; never report a cancelled run as successful, never report a completed run as cancelled | `CANCELLATION_INCOMPLETE` in the unknown branch | Cancellation request, acknowledgement state, completion evidence, in-flight inventory | **Yes**, in the unknown branch |
| 42 | Runtime restarts with an attempt in an unknown state | Owning `runtime_instance_id` lost; last durable transition authoritative (§29.3) | Per the §29.3 recovery matrix: rows 1–3, 5, 7, 8 resume; rows 4, 6, 9, 11, 14 → `reconciliation_required`; row 12 unchanged; row 16 terminal unchanged | Explicit recorded takeover; **no blind redispatch**; same-attempt resumption only when a definitive external status excludes in-flight effects; otherwise a new attempt after reconciliation | `RUNTIME_INSTANCE_LOST`, with `EXTERNAL_OUTCOME_UNKNOWN` on the unknown branches | Takeover record: prior and new instance, last durable state, `attempt_id`, last confirmed `sequence`, recovery decision | **Yes**, on every unknown branch |

**Scenario totals: 32 original + 10 additional = 42, all deterministic.**

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
- `[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`
- `[[../research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001]]`
- `[[../architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001]]`,
  `shared_context/loops/RUN_LEDGER_SCHEMA.json`
- `[[../research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002]]`
- `[[../research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001]]`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `VALIDATION.md`,
  `CONTEXT_GRAPH_SCHEMA.md`, `MODEL_ROUTING.md`

### 43.2 External

None. No external source was fetched, and no framework documentation, SDK, or
service was consulted, installed, or contacted during this task.
