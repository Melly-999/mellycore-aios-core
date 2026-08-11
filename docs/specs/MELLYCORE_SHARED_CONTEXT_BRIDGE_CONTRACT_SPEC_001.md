# MellyCore Shared Context Bridge Contract Spec

**Task ID:** MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-001
**Contract ID:** MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_001
**Version:** 1.0 — first draft.
**Verification status:** **Unverified.** No independent review has run. This
document is **not accepted** until
`MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001` completes with a
passing gate decision, in the same sequence used for
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`,
`[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]`, and
`[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]`.
**Status:** Drafted, specification-level only, pending independent review.
**This status does not authorize:** any Shared Context runtime, storage,
database, vector store, memory service, context-mutation engine, compression
implementation, validation implementation, proposal-lifecycle implementation,
Framework Adapter, framework execution, package loading, provider or model
call, MCP connection, plugin loading, hook execution, command execution, Batch
Orchestration, frontend, backend, network operation, or deployment. It fixes
the contract a later, separately authorized implementation must satisfy.
**Scope:** Defines the **Shared Context Bridge** — the bounded, traceable,
provenance-preserving exchange boundary through which the Agent Runtime, Agent
Packages, Framework Bridges, agents, tools, model providers, and future
orchestration systems may read, project, propose, transform, and return
context **without receiving unrestricted authority over canonical Shared
Context**.

---

## 1. Purpose and scope

### 1.1 The problem this contract solves

`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §17 fixes seven context
operations and states plainly that Shared Context canonical truth is owned by
the Shared Context Layer and that **"Agents never write it."**
`[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` §18 fixes that framework
writes are proposal-only. Neither defines the **exchange boundary itself**:
what a bounded context carrier looks like, how context is selected for one
consumer and one purpose, what makes a projection eligible, and — most
importantly — what must happen to context **coming back** from an agent, a
tool, a framework, or a provider before it may even be considered as a
proposal.

Without this contract, each consumer would invent its own idea of "the
context," and returned content would drift toward canonical status by
convenience rather than by governed admission.

### 1.2 In scope

The bridge boundary: context identity correlation, the logical context
envelope, selection, projection and projection eligibility, per-consumer read
boundaries, the write/proposal/mutation separation, a proposal lifecycle,
return-path validation, provenance and lineage preservation, namespace
isolation, classification and sensitivity preservation, the secret boundary,
memory-scope separation, memory proposals, compression and transformation
boundaries, context loss, conflict handling, staleness and versioning, leases,
retention and deletion propagation, quarantine, a bridge-owned rejection
taxonomy, an ordered validation model, mutation eligibility, per-subsystem
interaction boundaries, Batch compatibility, observability, audit evidence,
security, privacy, failure behavior, non-goals, deferred dependencies,
acceptance criteria, document metrics, references, and amendment rules.

### 1.3 Explicitly out of scope

1. Any Shared Context runtime, storage, database, vector store, index, or
   memory service.
2. Any canonical mutation engine or context-mutation implementation.
3. Any context-compression implementation (contract owned elsewhere — §21).
4. Any context-validation or proposal-lifecycle implementation.
5. Agent Runtime implementation (owned by
   `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`, unchanged here).
6. Framework Adapter implementation, SDK installation, or framework execution.
7. Package loading, installation, activation, or execution.
8. Command, hook, plugin, skill, or MCP runtime.
9. Batch Orchestration.
10. Provider connection, credential configuration, model call, or network
    operation.
11. Frontend, backend, or deployment.
12. Any push, pull request, merge, or remote branch operation.
13. Any MellyTrade interaction, trading, broker, or order behavior.

### 1.4 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Shared Context Bridge | `NOT_IMPLEMENTED` — no bridge, service, or exchange code exists |
| Canonical mutation engine | `NOT_IMPLEMENTED` — no canonical mutation has ever been performed by any bridge |
| Context storage, database, vector store, index | `NOT_IMPLEMENTED` |
| Memory service, durable memory store | `NOT_IMPLEMENTED` |
| Context compression | `NOT_IMPLEMENTED`; contract owned elsewhere (§21) |
| Context validation, proposal lifecycle | `NOT_IMPLEMENTED` — vocabulary only |
| Context envelopes created | **Zero** |
| Context proposals submitted | **Zero** |
| Canonical mutations performed via this bridge | **Zero** |
| Framework Bridge | Unchanged; `NOT_IMPLEMENTED`; no adapter exists for any framework |
| Agent Runtime, Agent Package Contract | Unchanged by this task; both `NOT_IMPLEMENTED` |
| Empirical framework validation | **`NOT_PERFORMED`** — unchanged by this task |
| Evidence class for every flow below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by this documentation task. A validator that did
not run records `NOT_RUN`, never a defaulted pass.

### 1.5 Relationship to migration triggers

This specification implements nothing, so it crosses no migration trigger in
`shared_context/PROJECT_STATE.md`'s Model A contract. Triggers **#1**, **#4**,
**#5**, **#6**, and **#7** remain uncrossed.

## 2. Terminology

Normative definitions. Where a term is already canonically defined elsewhere,
this section cites the owner instead of redefining it.

| Term | Definition |
| --- | --- |
| **Shared Context** | The canonical MellyCore-owned context layer (`shared_context/**`, the Context Gate, Control Plane §9.3). Owned entirely elsewhere; this contract never redefines it. |
| **Canonical Context** | Context whose authoritative value is held by the Shared Context Layer. Only the canonical owner may change it, and only through the governed path of §11. |
| **Context Bridge** | The bounded exchange boundary defined by this contract. It carries context outward as projections and inward as proposals. It holds no authority of its own. |
| **Context Projection** | A one-directional, non-canonical representation of selected canonical context, prepared for one named consumer and one declared purpose (§8). |
| **Context Selection** | The purpose-bounded, consumer-bounded act of choosing which canonical context may be projected (§7). Selection precedes projection and is itself governed. |
| **Context Envelope** | The logical carrier for one projection or one proposal (§6). A logical contract only — never a serialization format, wire protocol, or storage record. |
| **Context Slice** | The bounded subset of canonical context carried by one envelope. A slice is always smaller than or equal to what the consumer is authorized to read. |
| **Execution-Local Context** | Context living only within one run or attempt, owned by the Agent Runtime. Never canonical. |
| **Framework-Local Context** | Context living inside a framework session, bridge-local per `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` §4.2 and Runtime §18 rule 2. Never canonical. |
| **Context Proposal** | A reviewable artifact submitted inward proposing that context be admitted or changed. Corresponds to Runtime §17.1's `propose_update`; it changes nothing by itself. |
| **Context Mutation Request** | A request entering an approval path for a governed canonical change. Corresponds to Runtime §17.1's `request_canonical_mutation`. Distinct from a proposal (Runtime §17.1). |
| **Context Return Path** | The mandatory inward path every externally produced context artifact traverses before it may become a proposal (§13). |
| **Context Provenance** | Source, origin, and derivation evidence, owned by `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` and `shared_context/CONTEXT_GRAPH_SCHEMA.md`'s `SourceRef`. This contract preserves and augments it; it defines no provenance vocabulary. |
| **Context Lineage** | The relationship chain between context items, expressed **only** through `CONTEXT_GRAPH_SCHEMA.md` §5's existing relation types (§15). |
| **Context Namespace** | The isolation boundary a context item belongs to (§16). Namespaces are never flattened, merged, or inferred. |
| **Context Policy** | The policy governing whether a given consumer may receive a given context slice, evaluated by the Integration Gateway (Gateway §17) and Shared Context owners. This contract evaluates nothing. |
| **Context Eligibility** | The state in which a selection has satisfied every §9 precondition for projection to one exact consumer. Eligibility is **not** execution authorization and **not** permission to mutate. |
| **Context Validation** | The ordered layer evaluation of §30. It establishes only what §30.14 says it establishes; it never authorizes, mutates, or confers trust. |
| **Context Quarantine** | The terminal holding state for context that failed a §28 condition. Quarantined context is neither projected nor committed. |
| **Context Rejection** | A determinate refusal carrying a stable reason class (§29). Rejection is recorded, never silent. |
| **Context Redaction** | An explicit, recorded transformation that removes content. Per Runtime §17.3 rule 5, redaction is the **only** mechanism by which derived sensitivity may be lowered. |
| **Context Compression** | Lossy reduction of context volume. Bounded here (§21); its full contract is a named deferred dependency (§46). |
| **Context Transformation** | Any permitted change of form applied to a slice (§22). Distinct from, and never a substitute for, runtime result normalization. |
| **Context Loss** | Any canonical detail not carried by a projection or proposal, classified by §23. Safety- or authority-relevant loss fails closed. |
| **Memory Projection** | The bounded representation of a memory-scoped record for a consumer, subject to §19's scope separation. |
| **Durable Memory** | Memory persisting beyond one run, corresponding to the Agent Runtime §18 categories named **canonical project context** and **operator-approved long-term memory**. Never written by a bridge. |
| **Working Memory** | Attempt-scoped scratch state, corresponding to Runtime §18's **short-term working memory** category. Discarded at attempt end. |
| **Context Lease** | A bounded, expiring authorization to continue using a projection (§26). Expiry ends eligibility. |
| **Context Snapshot** | An immutable, addressable, versioned canonical context state, owned by the Shared Context Layer and identified by Runtime §8.1's `context_snapshot_id`. |
| **Context Version** | The version identity of a context item or snapshot as assigned by its canonical owner. This contract mints no version identity. |
| **Context Conflict** | Two or more competing claims about the same subject. Per Runtime §17.3 rule 3, conflicts are **never silently resolved**. |

## 3. Architectural ownership

No concern below is owned by more than one document. Where this contract
*consumes* another owner's concept, it is named "consumes," never "owns."

| Concern | Canonical owner | This contract's role | Explicit non-responsibility |
| --- | --- | --- | --- |
| Canonical Shared Context truth and admission | Shared Context Layer (`shared_context/**`, Context Gate, Control Plane §9.3) | Consumes; delivers proposals to the existing gate | MUST NOT mutate canonical state or create a parallel admission path |
| The seven context operations | Agent Runtime §17.1 | Consumes **by name** | MUST NOT define an eighth operation or rename one |
| Required context-record metadata | Agent Runtime §17.2 | References the ten fields unchanged | MUST NOT rename, add to, or narrow them |
| Snapshot staleness policy and its six conditions | Agent Runtime §17.4 | Consumes unchanged | MUST NOT define a competing staleness rule |
| Memory categories | Agent Runtime §18 (six categories) | Maps bridge scopes onto them **by semantic name** | MUST NOT create a seventh category, renumber, or conflate two |
| Context-flow trace record | Agent Runtime §19 (seventeen fields) | References it as the transfer evidence | MUST NOT add an eighteenth field |
| Graph entities and relation types | `shared_context/CONTEXT_GRAPH_SCHEMA.md` | Consumes §5's relation types for lineage | MUST NOT invent a relation type |
| Provenance labels, `sensitivity_level`, `allowed_use` | `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` | Preserves and augments across the bridge | MUST NOT define a sensitivity scale or a parallel provenance vocabulary |
| Context ingestion and admission workflow | `[[MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001]]`, `[[MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001]]` | Consumes; proposals terminate at the gate | MUST NOT bypass, weaken, or replace admission |
| **The bridge exchange boundary** — envelope, selection, projection eligibility, return-path validation, quarantine, context loss, bridge rejection classes, per-consumer read boundaries | **This Shared Context Bridge Contract** | **Owns** | — |
| Execution-local state, run lifecycle, `run_state` | Agent Runtime | Consumes | MUST NOT define run state |
| Package context declarations | `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` | Consumes | MUST NOT define package lifecycle or grant package access |
| Framework-local state and framework projection | `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` | Consumes | MUST NOT cite capability ordinals or own result normalization |
| Six status dimensions and entity contract | `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §7.1, §8.1 | Bridge fields are typed entity data | MUST NOT add a status dimension |
| Provider authorization facts, MCP server records | `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` §21.1, §24 | References | MUST NOT authorize a provider |
| Capability resolution, policy order, approval binding | `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §12, §17, §18 | References decisions | MUST NOT grant or evaluate policy |
| Model selection and routing decisions | Model Router (Runtime §23; `shared_context/MODEL_ROUTING.md`) | References | MUST NOT select a model or provider |
| Knowledge Graph presentation | Knowledge Graph specifications | Unaffected | MUST NOT redefine graph presentation |
| Context compression contract | Future, separate task (§46) | Bounds the safety envelope only (§21) | MUST NOT specify a compression algorithm or implementation |
| Observability, audit, cost attribution | Control Plane; `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5; `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` | Supplies projections (§40) and evidence (§41) | MUST NOT define a cost schema or a new dimension |

### 3.1 Precedence

```text
shared_context/SAFETY_CONTRACT.md
  > Enterprise-Provider ADR
  > Provider Registry contract
  > Integration Gateway contract
  > Shared Context Layer contracts (Context Graph Schema, Provenance and
    Sensitivity, Context Gate, Ingestion Gate)
  > Agent Runtime architecture
  > this Shared Context Bridge Contract (stricter only)
  > Framework Bridge Contract / Agent Package Contract (stricter only, on
    their own concerns)
  > tenant policy (stricter only)
```

This contract MAY add requirements stricter than any document above it and
MUST NOT subtract from any. Conflicts fail closed and the affected exchange is
denied pending resolution.

## 4. Canonical versus projected context

### 4.1 The direction rule (normative)

The **allowed** direction is:

```text
Canonical Shared Context
        ↓ bounded context selection (§7)
        ↓ validated projection (§8, §9)
execution-local or framework-local context (§10)
        ↓ returned context proposal (§11, §13)
        ↓ validation, provenance, policy, and approval gates (§30, §31)
optional canonical mutation by the canonical owner
```

The **prohibited** direction is:

```text
Framework or agent output
        ↓
automatic canonical Shared Context write
```

**No framework, agent, package, provider, tool, plugin, hook, command, MCP
server, adapter, or batch worker may independently mutate canonical Shared
Context.**

### 4.2 Rules

1. Projection is one-directional. A canonical value MAY be projected. A
   projected or returned value MUST NOT be read back as canonical.
2. **Projected context MUST NOT become canonical merely because** it is used
   by a framework; returned by an agent; stored by a framework session;
   present in a package; emitted by a tool; generated by a model; or passes
   structural validation. None of these is an admission decision.
3. Structural validity is not truth. Passing §30's layers establishes only
   what §30.14 states.
4. Round-trip is not identity. A projected value returning byte-identical is
   still returned content and still traverses §13.
5. Canonical mutation is performed only by the canonical owner, only after
   §31's intersection holds, and only through Runtime §17.1's
   `request_canonical_mutation` path with its required approval.

### 4.3 Canonical-versus-projected register

| Context form | Canonical? | Owner | May be projected? | Authoritative when returned? |
| --- | --- | --- | --- | --- |
| Canonical Shared Context | **Yes** | Shared Context Layer | Yes, as a bounded slice | n/a |
| Context snapshot | **Yes** (immutable) | Shared Context Layer | By reference and bounded slice | n/a |
| Context projection / envelope | No | This contract | n/a | **No** |
| Execution-local context | No | Agent Runtime | n/a | **No** |
| Framework-local context / session state | No | Framework Bridge | n/a | **No** |
| Working memory | No | Agent Runtime (short-term working memory) | n/a | **No** |
| Agent-local memory | No | Agent Runtime (agent-local memory) | Within agent + tenant only | **No** |
| Shared derived memory | No | Agent Runtime (shared derived memory) | Within authorized scope | **No** — proposal only |
| Tool output | No | Tool, via Gateway | n/a | **No** — untrusted (§36) |
| Provider or model output | No | Provider, via Model Router | n/a | **No** — untrusted (§35) |
| Context proposal | No | This contract | n/a | **No** — reviewable artifact only |
| Compressed or summarized context | No | Compression contract (§21, §46) | Yes, when declared | **No** |
| Quarantined context | No | This contract | **No** | **No** |

## 5. Context identity

### 5.1 Identity and correlation fields

Where a field is owned elsewhere, this contract **references it unchanged and
mints no replacement**.

| # | Field | Owner | Role at the bridge |
| --- | --- | --- | --- |
| 1 | `context_item_id` | Shared Context Layer / `CONTEXT_GRAPH_SCHEMA.md` `ContextNode.id` | Identifies one addressable canonical item |
| 2 | `context_envelope_id` | **This contract** | Identifies one envelope (§6) |
| 3 | `source_refs` | `CONTEXT_GRAPH_SCHEMA.md` §2.1 (non-empty required) | Traces every item to at least one source |
| 4 | `context_namespace` | **This contract** (§16) | The isolation boundary |
| 5 | `context_version` | Shared Context Layer | The canonical version identity; never minted here |
| 6 | `context_snapshot_id` | Agent Runtime §8.1 | The immutable snapshot reference |
| 7 | `projection_id` | **This contract** | Identifies one projection act |
| 8 | `proposal_id` | **This contract** | Identifies one inward proposal |
| 9 | `run_id` | Agent Runtime §8.1 | The consuming run |
| 10 | `agent_package_id` / `package_revision_id` | Agent Runtime §8.1 | The consuming package revision |
| 11 | `agent_definition_id` | Agent Runtime §8.1 | The consuming agent |
| 12 | `framework_session_reference` | Framework Bridge Contract | The framework-local session, non-canonical |
| 13 | `provenance_reference` | Context Provenance and Sensitivity spec (`ContextSource`) | The provenance record |
| 14 | `policy_decision_reference` | Integration Gateway §18 | A reference to the authorizing decision, never copied authority |

### 5.2 Rules

1. Identity fields are opaque and carry no mutable state, permission,
   sensitivity, or authorization outcome.
2. This contract mints exactly three identities — `context_envelope_id`,
   `projection_id`, `proposal_id` — and **no replacement for any
   owner-defined field**.
3. An identity MUST NOT encode a namespace, tenant, sensitivity, or policy
   outcome.
4. A `projection_id` binds to exactly one consumer, one purpose, and one
   selection. It is never reused across consumers.
5. A `proposal_id` never becomes a `context_item_id`. Admission, if it ever
   occurs, mints canonical identity through the canonical owner.

## 6. Context envelope

### 6.1 Required envelope fields

The envelope is a **logical contract only** — not a serialization format, wire
protocol, storage record, or schema migration.

| # | Field | Meaning |
| --- | --- | --- |
| 1 | `context_envelope_id` | Identity (§5.1) |
| 2 | `source` | The canonical source reference(s); `source_refs` MUST be non-empty |
| 3 | `context_namespace` | The namespace this slice belongs to (§16) |
| 4 | `provenance` | The provenance reference(s), preserved per §14 |
| 5 | `classification` | `context_class` per Runtime §17.2, unchanged |
| 6 | `retention_hint` | The canonical `retention_policy` reference (§27); a hint never loosens the policy |
| 7 | `sensitivity_marker` | `sensitivity_level` from the canonical vocabulary (§17); never a parallel scale |
| 8 | `policy_requirements` | The policy conditions the consumer must satisfy; a requirement statement, never a grant |
| 9 | `transformation_history` | The ordered, recorded transformations applied (§22) |
| 10 | `projection_scope` | The exact bounded scope this envelope covers |
| 11 | `permitted_consumer` | The exact consumer identity permitted to receive it |
| 12 | `lease` | Expiration or lease information (§26) |
| 13 | `integrity_metadata` | Digest or equivalent integrity evidence, computed under Runtime §8.3 |
| 14 | `validation_state` | The §30 outcome; absent or `unknown` denies |

### 6.2 Rules

1. An envelope missing any required field is invalid and MUST NOT be projected.
2. An envelope MUST NOT carry authority: no field grants read, write, mutation,
   execution, or approval.
3. An envelope MUST NOT carry secret values (§18).
4. An envelope is bound to exactly one `permitted_consumer`. Re-addressing an
   envelope to another consumer requires a new selection, a new eligibility
   evaluation, and a new envelope.
5. `validation_state` MUST NOT be self-asserted by a consumer.
6. This contract specifies no serialization, encoding, transport, storage
   location, or persistence mechanism for envelopes.

## 7. Context selection

Selection chooses what MAY be projected. It precedes projection and is itself
governed.

Selection MUST be:

1. **Purpose-bounded** — a declared purpose, evaluated against policy; a
   selection without a declared purpose is invalid.
2. **Consumer-bounded** — bound to one named consumer identity.
3. **Policy-aware** — evaluated against Gateway §17 policy and Shared Context
   access scope; availability is never authorization (Runtime §17.3 rule 1).
4. **Namespace-aware** — confined to namespaces the consumer is authorized for
   (§16).
5. **Provenance-preserving** — every selected item retains its `source_refs`.
6. **Minimal** — the smallest slice satisfying the declared purpose (§43).
7. **Observable** — every selection is recorded per §40 and §41.
8. **Reproducible where required** — where a run declares reproducibility, the
   selection MUST be reconstructible from its recorded inputs and the
   referenced snapshot.

Rules:

1. **A framework MUST NOT request unrestricted project context.** A request for
   "all context", an unbounded namespace, or an unscoped wildcard is rejected.
2. A selection MUST NOT expand as a side effect of transformation, compression,
   or retry.
3. Selection returns a candidate slice only; it confers no eligibility (§9).

## 8. Context projection

Projection renders a selected slice into an execution-local or framework-local
representation.

Projection MUST NOT:

1. add authority of any kind;
2. broaden permissions;
3. remove or relax restrictions carried by the slice;
4. erase, truncate, or replace provenance;
5. silently change classification;
6. silently promote a memory scope (§19);
7. grant write access to canonical context;
8. expose secret values (§18);
9. bypass policy evaluation.

Rules:

1. Projection is **subtractive or equal** with respect to authority: the
   projected form expresses a subset of what the canonical slice permits.
2. A restriction the target representation cannot express is a safety-relevant
   loss and MUST fail closed (§23).
3. Every projection carries its `projection_id`, its envelope, and the
   context-flow trace evidence required by Runtime §19.
4. A projection is not a copy of authority; the consumer's permission is
   re-evaluated at the point of use (Runtime §17.3 rule 1).

## 9. Projection eligibility

A projection MUST NOT occur unless **all** of the following hold for the exact
slice, consumer, purpose, and namespace:

| # | Precondition | Absence means |
| --- | --- | --- |
| 1 | Identity valid | Deny — `CONTEXT_IDENTITY_INVALID` |
| 2 | Provenance available and non-empty | Deny — `CONTEXT_PROVENANCE_MISSING` |
| 3 | Consumer known and named | Deny |
| 4 | Purpose declared | Deny |
| 5 | Policy evaluated (Gateway §17) | Deny — never a default allow |
| 6 | Permission allowed for this consumer | Deny |
| 7 | Classification compatible with the consumer | Deny |
| 8 | Namespace compatible (§16) | Deny — `CONTEXT_NAMESPACE_VIOLATION` |
| 9 | Retention compatible (§27) | Deny |
| 10 | Sensitivity compatible (§17) | Deny — `CONTEXT_SENSITIVITY_MISMATCH` |
| 11 | Requested transformation permitted (§22) | Deny — `CONTEXT_TRANSFORMATION_UNPERMITTED` |
| 12 | Lease valid and unexpired (§26) | Deny — `CONTEXT_LEASE_EXPIRED` |

Rules:

1. **Eligibility MUST NOT imply execution authorization.** It permits one
   bounded projection and nothing else.
2. Eligibility is evaluated per projection, never cached across consumers,
   purposes, or namespaces.
3. **An unvalidated framework profile MUST NOT become context-projection
   eligible through this specification.** Framework empirical validation
   remains `NOT_PERFORMED` and is owned by
   `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` §27.2 and its open
   finding `NEW-P2-04` (§46). This contract neither performs nor substitutes
   for that validation.
4. Missing, expired, `unknown`, or malformed evidence for any precondition
   **denies**. There is no default-allow state.

## 10. Read boundary

Each consumer receives only what it is explicitly authorized to read. **No
consumer receives broader access than explicitly authorized**, and no consumer
receives canonical write access.

| Consumer | Read boundary |
| --- | --- |
| Agent Runtime | Reads snapshots within declared scope via Runtime §17.1 `read_snapshot`; holds execution-local context; never writes canonical state |
| Agent Packages | Bounded by the package's declared `required_context_classes`; an unlisted class is unreadable (§33) |
| Framework Bridges | Receive only projections bound to one framework session; framework-local state is never canonical (§34) |
| Tools | Purpose-specific slices only; nothing beyond the declared tool purpose (§36) |
| Model providers | Minimized model-input projections only; no credential, no unrelated namespace (§35) |
| Plugins | Bounded by their bundling package's authorized scope; bundling grants nothing (§38) |
| Hooks | Bounded to the lifecycle event's declared context; inert until authorized (§38) |
| Commands | Bounded, declaration-only consumers; no namespace ownership conferred (§38) |
| MCP servers | Bounded resource/tool/prompt exposure by reference only; untrusted output (§37) |
| Batch Orchestration | Isolated per-agent snapshots and namespaces only (§39) |

Rules:

1. Existence is not permission (Runtime §18 rule 1); a readable reference
   grants nothing.
2. **The tenant boundary is absolute** (Runtime §17.3 rule 2). Cross-tenant
   resolution denies, and the denial does not reveal existence.
3. A consumer MUST NOT infer the existence of context it may not read.

## 11. Write and mutation boundary

Five distinct concepts. **No concept implies the next.**

| # | Concept | Who may perform it | Effect on canonical state |
| --- | --- | --- | --- |
| 1 | **Execution-local write** | Agent Runtime, within a run or attempt | **None** |
| 2 | **Framework-local write** | A framework, within its session | **None** |
| 3 | **Context proposal** | Any authorized producer, inward | **None** — a reviewable artifact (Runtime §17.1 `propose_update`) |
| 4 | **Context mutation request** | An authorized requester, entering an approval path | **None on its own** (Runtime §17.1 `request_canonical_mutation`) |
| 5 | **Canonical mutation** | **The canonical Shared Context owner only**, after every gate | The only concept that changes canonical state |

Rules:

1. **Agents and frameworks MUST produce proposals, never direct canonical
   writes.** This restates Runtime §17's "Agents never write it" without
   weakening it.
2. A proposal and a mutation request are **distinct** (Runtime §17.1); neither
   mutates canonical state on its own.
3. **Only the canonical Shared Context owner may perform a canonical
   mutation**, and only after §31's intersection holds and the required
   Operator approval exists.
4. No bridge, adapter, package, tool, provider, plugin, hook, command, MCP
   server, or batch worker holds mutation authority under any condition.
5. A failed, rejected, or quarantined proposal MUST NOT be retried as a
   mutation request; escalation of kind is prohibited.

## 12. Context proposal lifecycle

These phases are **owned by this contract** and are **typed entity data** under
Control Plane §7.1's allowance for domain fields. They are distinct from the
Agent Package lifecycle, the Agent Runtime `run_state`, the Framework Bridge
lifecycles, and Control Plane's six status dimensions.

**This contract defines no projection of these phases onto any Control Plane
§8.1 dimension.** Any future rendering alongside Control Plane's dimensions
requires its own mapping contract or an explicit, separately reviewed owner
amendment — neither of which this document performs.

| # | Phase | Meaning |
| --- | --- | --- |
| 1 | `proposal_draft` | Assembled locally; not yet submitted |
| 2 | `proposal_submitted` | Received at the bridge boundary |
| 3 | `proposal_validating` | Traversing §30's layers |
| 4 | `proposal_rejected` | Failed a layer; carries a §29 reason class |
| 5 | `proposal_quarantined` | Met a §28 condition; terminal until Operator action |
| 6 | `proposal_validated` | Passed §30; **not** trusted, **not** eligible |
| 7 | `proposal_mutation_eligible` | §31's intersection holds; **not** mutated |
| 8 | `proposal_awaiting_operator_approval` | In the approval path |
| 9 | `proposal_withdrawn` | Retracted by its producer before a decision |
| 10 | `proposal_superseded` | Replaced by a later proposal on the same subject |

Rules:

1. No phase authorizes a canonical mutation. Phase 7 establishes eligibility
   only (§31).
2. A phase MUST NOT be inferred from the absence of another.
3. `proposal_quarantined` is terminal absent explicit Operator action (§28).
4. This contract defines states and their non-collision only; the full
   transition-rule, evidence, and event contract is a deferred dependency
   (§46).

## 13. Return-path validation

**Returned context MUST be treated as untrusted input**, regardless of origin,
regardless of whether MellyCore produced the original slice, and regardless of
byte-identity with what was projected.

Applies to context returned from: agents; tools; frameworks; model providers;
plugins; hooks; MCP servers; and batch workers.

At minimum, the following MUST be validated before a proposal may form:

| # | Check | Failure disposition |
| --- | --- | --- |
| 1 | Source identity | Reject |
| 2 | Provenance present and traceable | Reject — `CONTEXT_PROVENANCE_MISSING` |
| 3 | Namespace authorized for the producer | Reject — `CONTEXT_NAMESPACE_VIOLATION` |
| 4 | Policy satisfied | Reject |
| 5 | Schema conformance | Reject |
| 6 | Content safety | Reject or quarantine |
| 7 | Sensitivity consistent and not downgraded | Reject — `CONTEXT_SENSITIVITY_MISMATCH` |
| 8 | Permission held by the producer | Reject |
| 9 | Integrity evidence | Reject — `CONTEXT_INTEGRITY_FAILED` |
| 10 | Transformation record complete (§22) | Reject — `CONTEXT_TRANSFORMATION_UNPERMITTED` |
| 11 | Context-conflict risk assessed (§24) | Surface the conflict; never auto-resolve |
| 12 | Prompt-injection risk assessed | Quarantine on suspicion (§28) |
| 13 | Memory-contamination risk assessed | Quarantine on suspicion (§28) |

Rules:

1. A returned artifact that skips any check MUST NOT become a proposal.
2. **Byte-identity does not bypass validation** (§4.2 rule 4).
3. Returned content MUST NOT be treated as instructions to the Runtime, the
   bridge, or any validator (Runtime §31, §32).
4. A validation failure never itself mutates, fetches, installs, or resolves
   anything.

## 14. Provenance

Provenance is owned by
`[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` and
`CONTEXT_GRAPH_SCHEMA.md`'s `SourceRef`. This contract preserves and augments
it and defines no provenance vocabulary.

Provenance MUST be preserved and augmented across every stage: selection;
projection; transformation; compression; framework execution; tool execution;
return; proposal; and accepted mutation.

Rules:

1. **Provenance MUST NOT be replaced with only the most recent producer.**
   Augmentation appends; it never overwrites the origin chain.
2. `source_refs` MUST remain non-empty at every stage
   (`CONTEXT_GRAPH_SCHEMA.md` §2.1).
3. A returned artifact whose provenance cannot be traced to an admitted source
   is rejected (§13 check 2).
4. Provenance loss is safety-relevant and fails closed (§23).
5. Provenance preserved does **not** mean content trusted.

## 15. Lineage

Lineage relationships MUST be expressed **only** through the relation types
`CONTEXT_GRAPH_SCHEMA.md` §5 already defines. This contract **invents no graph
semantics**.

| Bridge relationship | Existing owner relation | Note |
| --- | --- | --- |
| Derived-from / transformed-from / compressed-from | `references`, plus the recorded `transformation_history` (§6.1 field 9) | The transformation record carries the derivation detail; no new relation is minted |
| Supersedes | `supersedes` | Used unchanged |
| Conflicts with | `contradicts` | Used unchanged; conflicts are surfaced, never resolved (§24) |
| Produced by | `produced_by` | Used unchanged |
| Validated by | `validated_by` | Used unchanged |
| Structural membership | `belongs_to` | Used unchanged |

Rules:

1. A lineage claim requiring a relation type not in `CONTEXT_GRAPH_SCHEMA.md`
   §5 MUST be expressed in `transformation_history` instead, or the
   relationship is not asserted.
2. This contract MUST NOT propose an amendment to the graph schema; that is
   its owner's concern.

## 16. Namespace isolation

| # | Namespace | Bound to |
| --- | --- | --- |
| 1 | Project context | The project, within one tenant |
| 2 | Agent context | One `agent_definition_id`, within one tenant |
| 3 | Package context | One `package_revision_id` |
| 4 | Run context | One `run_id` |
| 5 | Framework session | One framework session reference; never canonical |
| 6 | User context | One user identity, within one tenant |
| 7 | Tool context | One tool invocation purpose |
| 8 | Provider context | One provider interaction |
| 9 | Temporary context | One attempt; discarded at attempt end |
| 10 | Quarantined context | Isolated entirely; never projected (§28) |

Rules:

1. **A context bridge MUST NOT flatten namespaces.** Merging, defaulting,
   inferring, or collapsing two namespaces into one is prohibited.
2. Cross-namespace movement requires an explicit, recorded, policy-evaluated
   act; it never occurs as a side effect of projection, transformation, or
   compression.
3. The tenant boundary is absolute and supersedes every namespace rule
   (Runtime §17.3 rule 2).
4. **Namespace escape is a safety failure** and fails closed (§42).

## 17. Context classification and sensitivity

`sensitivity_level` and `allowed_use` are owned by
`[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`. This contract
defines **no** sensitivity scale and no parallel classification vocabulary.

Rules:

1. Classification and sensitivity markers MUST survive projection unchanged
   unless an explicit, recorded redaction transformation lowers sensitivity —
   the only permitted mechanism (Runtime §17.3 rule 5).
2. **Sensitivity does not decay.** Derived or compressed context inherits the
   **highest** sensitivity of its sources.
3. **A lower-trust consumer MUST NOT receive context requiring higher
   authorization.** Compatibility is evaluated per §9 precondition 10.
4. A stricter `allowed_use` may always be applied; a looser one requires the
   owner contract's own rules and is never applied by the bridge.
5. Sensitivity downgrade without a recorded redaction is a safety failure
   (§42).

## 18. Secret boundary

Explicitly prohibited:

1. Secret values in any context payload, envelope, projection, or proposal,
   unless a separate owner contract explicitly authorizes it — none does today.
2. Provider keys, tokens, or credential material in projected context.
3. `.env` content projection in any form.
4. Copying credential material into framework, session, or agent memory.
5. Logging, tracing, or observability rendering of secret values.
6. Persistence of secret values in Shared Context proposals.

Rules:

1. **A secret reference and a secret value are distinct.** A bounded, non-
   resolving reference MAY appear where policy permits; the value MUST NOT.
2. A bridge never holds, reads, requests, derives, or forwards a credential
   (Runtime §11.2 rule 2; Framework Bridge §10.1 category 6).
3. Detected secret material fails closed and quarantines (§28), and the
   detection record itself MUST NOT contain the value.

## 19. Memory scopes

Memory categories are owned by **Agent Runtime §18**, which fixes **six**
categories. This contract creates **no** new category and **renumbers
nothing**. The scopes below are referenced **by semantic name** and mapped onto
the owner's categories by name.

| Bridge scope | Agent Runtime §18 category (by name) | Canonical? |
| --- | --- | --- |
| Working memory | Short-term working memory | No |
| Execution-local memory | Immutable run context / short-term working memory, per record | No |
| Framework-session memory | Short-term working memory **at most** (Runtime §18 rule 2) | No |
| Package-declared memory | Declares requirements only; no category of its own | No |
| Agent memory | Agent-local memory | No |
| Shared Context | Canonical project context | **Yes** |
| Durable MellyCore memory | Canonical project context; operator-approved long-term memory | **Yes** |
| Archival evidence | Append-only evidence surfaces (Runtime §17.1 `append_evidence`) | Immutable, never mutated |

Rules:

1. **No local or framework memory may silently become durable canonical
   memory.** Every promotion is an explicit, separately authorized step with
   its own evidence (Runtime §18 rule 4).
2. Categories are never conflated (Runtime §18 rule 3).
3. A framework's automatic memory, history, or checkpoint feature is
   short-term working memory at most, regardless of its own labelling.
4. **Working memory ≠ durable memory**, and existence is never permission
   (Runtime §18 rule 1).
5. This contract declares no new memory category and no memory retention rule
   of its own.

## 20. Memory proposal boundary

A system MAY **propose** durable memory. It MUST NOT write it.

A memory proposal MUST preserve:

| # | Element |
| --- | --- |
| 1 | Source |
| 2 | Reason for proposing durability |
| 3 | Intended scope (namespace, tenant, consumer) |
| 4 | Sensitivity marker (§17) |
| 5 | Retention requirement (§27) |
| 6 | Confidence or evidence, where canonically supported (Runtime §17.2 `confidence`) |
| 7 | Validation state (§30) |
| 8 | Approval requirement |

Rules:

1. A memory proposal follows §12's lifecycle and §30's validation exactly as
   any other proposal.
2. Absence of any element above denies the proposal.
3. A memory proposal MUST NOT self-assert approval, confidence, or validation
   state.

## 21. Context compression

Context Compression remains owned by its own canonical contract, named as a
deferred dependency (§46). This section bounds only the **safety envelope**
compressed context must satisfy at the bridge; it specifies no algorithm,
ratio, model, or implementation.

Compression MUST NOT:

1. fabricate facts;
2. erase or truncate provenance;
3. hide, drop, or weaken policy restrictions;
4. change permission scope;
5. convert uncertainty into certainty;
6. remove rejection, refusal, or quarantine evidence;
7. silently merge conflicting statements (§24).

Rules:

1. Compressed context is a **transformation** (§22) and MUST carry its
   `transformation_history` entry and a compression reference.
2. Compressed context inherits the highest sensitivity of its sources (§17).
3. **Compression ≠ truth** and **summarization ≠ evidence.** A compressed
   artifact never becomes evidence for a claim its sources did not support.
4. Compression that loses safety- or authority-relevant detail fails closed
   (§23).

## 22. Transformation

Permitted transformation classes:

| # | Class | Constraint |
| --- | --- | --- |
| 1 | Formatting | No semantic change |
| 2 | Filtering | Subtractive only; never adds |
| 3 | Redaction | The only mechanism that may lower sensitivity, and only when recorded (§17) |
| 4 | Normalization | Structure only; never meaning |
| 5 | Summarization | Lossy; never evidence (§21 rule 3) |
| 6 | Compression | Bounded by §21 |
| 7 | Framework adaptation | Shape only; never authority (§8) |
| 8 | Schema projection | Field selection only; never field invention |

Rules:

1. Every transformation MUST be recorded in `transformation_history` with its
   class and ordering.
2. An unrecorded transformation invalidates the envelope.
3. A transformation MUST NOT add content, authority, certainty, or
   classification.
4. **Context transformation and runtime result normalization are separate
   concerns.** This contract **does not define, own, resolve, or substitute
   for** the Agent Runtime `normalize_result` operation or the Framework Bridge
   open finding `NEW-P2-01` concerning it (§46). Nothing here may be cited as
   satisfying that obligation.

## 23. Context loss

| # | Loss class | Disposition |
| --- | --- | --- |
| 1 | Representational loss (form only, meaning intact) | MAY proceed; MUST be recorded |
| 2 | Semantic loss (meaning changed or reduced) | MUST be declared; proceeds only when non-safety-relevant |
| 3 | **Provenance loss** | **MUST fail closed** |
| 4 | **Classification loss** | **MUST fail closed** |
| 5 | **Policy loss** | **MUST fail closed** |
| 6 | **Namespace loss** | **MUST fail closed** |

Rules:

1. **Safety-relevant or authority-relevant loss MUST fail closed** —
   `CONTEXT_LOSS_UNACCEPTABLE` (§29).
2. Ambiguity resolves to loss: where it cannot be determined whether a detail
   survived, it MUST be treated as lost.
3. Declared non-safety loss MUST NOT accumulate unnoticed into safety-relevant
   loss; each exchange is evaluated on its total loss.
4. Loss MUST be observable (§40) and never concealed.

## 24. Conflict handling

Per Runtime §17.3 rule 3, conflicts are **never silently resolved**.

Rules:

1. **The bridge MUST NOT silently choose one competing claim as canonical.**
2. Conflicting claims MUST be surfaced together with their provenance and
   precedence, expressed through `CONTEXT_GRAPH_SCHEMA.md`'s `contradicts`
   relation (§15).
3. Conflict resolution remains subject to canonical policy and evidence
   owners; the bridge records and surfaces, never adjudicates.
4. **Context-conflict concealment is a security concern** (§42).
5. A proposal that would silently overwrite a conflicting claim is rejected —
   `CONTEXT_CONFLICT_UNRESOLVED` (§29).

## 25. Staleness and versioning

The snapshot staleness policy — including its six conditions, materiality
rules, and operator-exception discipline — is owned by **Agent Runtime §17.4**
and is consumed here unchanged. This contract defines **no competing staleness
rule**.

| Concept | Owner | Bridge treatment |
| --- | --- | --- |
| Snapshot version | Shared Context Layer | Referenced |
| Context version | Shared Context Layer | Referenced; never minted here |
| Stale projection | This contract | A projection whose snapshot is no longer current under Runtime §17.4 |
| Expired lease | This contract (§26) | Ends eligibility |
| Superseded context | `CONTEXT_GRAPH_SCHEMA.md` `supersedes` | Referenced |
| Concurrent proposal | This contract | Surfaced as a conflict (§24), never merged |

Rules:

1. **A stale projection MUST NOT be used automatically.** Refresh is
   replacement with a new identity, never mutation (Runtime §17.4 rule 2).
2. Absence of a staleness determination fails closed (Runtime §17.4 rule 4).
3. This contract implements **no locking, persistence, transaction, or
   concurrency-control mechanism**.

## 26. Context leases

1. A projection MAY carry a bounded lease specifying how long it remains usable.
2. **Lease expiry MUST terminate eligibility for further use** unless
   eligibility is re-evaluated in full under §9.
3. An expired lease MUST NOT be extended implicitly, by retry, or by
   transformation.
4. A lease is not an authorization: it bounds an already-granted eligibility
   and never creates one.
5. Lease state MUST be observable (§40).

## 27. Retention and deletion

1. Retention requirements propagate with every projection; a projection MUST
   NOT outlive the canonical retention policy.
2. **A bridge MUST NOT retain context longer than the canonical policy
   permits.**
3. A retention hint in an envelope (§6.1 field 6) never loosens the canonical
   policy; it may only carry or tighten it.
4. **Deletion from canonical context and deletion from external framework
   memory MUST remain separately observable.** Canonical deletion does not
   assert that a framework, provider, or session copy was deleted, and no
   projection may claim otherwise.
5. Where external deletion cannot be established, the state is `unknown` and is
   recorded as such — never as deleted.

## 28. Quarantine

Quarantine conditions:

| # | Condition |
| --- | --- |
| 1 | Unknown or untraceable provenance |
| 2 | Schema validation failure |
| 3 | Suspected prompt injection |
| 4 | Policy conflict |
| 5 | Unauthorized namespace |
| 6 | Sensitivity mismatch |
| 7 | Transformation ambiguity |
| 8 | Suspected context poisoning |
| 9 | Integrity failure |

Rules:

1. **Quarantined context MUST NOT be projected and MUST NOT be canonically
   committed.**
2. Quarantine is isolated in its own namespace (§16 row 10) and never
   contributes to a selection.
3. Quarantine is terminal absent explicit, recorded Operator action.
4. Quarantine evidence MUST NOT be deleted (§41), and MUST NOT contain secret
   values (§18).

## 29. Rejection taxonomy

Before adding any class, the Agent Runtime §33 taxonomy, the Framework Bridge
§23 taxonomy, the Shared Context owner documents, the Integration Gateway
§25 taxonomy, the Context Graph Schema, and the Operations contracts were
audited. Classes already owned elsewhere are **consumed, not redefined**.

### 29.1 Consumed classes — owned elsewhere

| Class | Owner | Used for |
| --- | --- | --- |
| `CONTEXT_ACCESS_DENIED` | Agent Runtime §33 | Read scope denied at point of use |
| `CONTEXT_CLASS_UNDECLARED` | Agent Package Contract §21 | A proposal outside a package's `produced_context_classes` |
| `TENANT_ISOLATION_VIOLATION` | Agent Runtime §33 | Cross-tenant resolution |
| `STALE_STATE` | Agent Runtime §33 / §17.4 | Snapshot staleness outcomes |
| `SENSITIVE_VALUE_REJECTED` | Agent Runtime §33 | Secret material detected |
| `INJECTION_SUSPECTED` | Agent Runtime §33 | Prompt-injection suspicion |
| `EXTERNAL_CONTENT_REJECTED` | Agent Runtime §33 | Untrusted external content refused |
| `INVALID_REFERENCE_SHAPE` | Agent Runtime §33 | Malformed reference |
| `AUTHORIZATION_DENIED` | Agent Runtime §33 | Policy or permission denial |

### 29.2 Bridge-owned classes — genuinely absent from every audited taxonomy

| Class | Triggered by | Discriminator |
| --- | --- | --- |
| `CONTEXT_ENVELOPE_INVALID` | A required §6.1 envelope field is absent or malformed | Envelope structure only; distinct from `INVALID_REFERENCE_SHAPE`, which concerns a single reference |
| `CONTEXT_IDENTITY_INVALID` | §9 precondition 1 fails | Bridge identity correlation only |
| `CONTEXT_PROVENANCE_MISSING` | `source_refs` empty or untraceable (§9 precondition 2, §13 check 2) | Absence of provenance, not denial of access |
| `CONTEXT_NAMESPACE_VIOLATION` | §16 boundary crossed without an explicit act | Namespace only; tenant crossing remains `TENANT_ISOLATION_VIOLATION` |
| `CONTEXT_SENSITIVITY_MISMATCH` | §17 compatibility fails, or an unrecorded downgrade is detected | Classification compatibility, not secret detection |
| `CONTEXT_TRANSFORMATION_UNPERMITTED` | A transformation is unpermitted or unrecorded (§22) | Transformation record only |
| `CONTEXT_LOSS_UNACCEPTABLE` | Safety- or authority-relevant loss (§23) | Loss classification only |
| `CONTEXT_CONFLICT_UNRESOLVED` | A proposal would silently resolve a conflict (§24) | Conflict handling only |
| `CONTEXT_LEASE_EXPIRED` | §26 lease expiry | Lease only; distinct from `STALE_STATE`, which concerns snapshot currency |
| `CONTEXT_QUARANTINED` | Any §28 condition | Quarantine only |
| `CONTEXT_INTEGRITY_FAILED` | Integrity evidence absent or mismatched (§13 check 9) | Integrity only |

Rules:

1. No class above duplicates an owner-defined class; each carries a stated
   deterministic discriminator.
2. **This contract does not resolve, arbitrate, or select between the Framework
   Bridge's `PROJECTION_UNSUPPORTED` and the Agent Runtime's
   `BRIDGE_UNSUPPORTED_BEHAVIOR`.** That overlap is the Framework Bridge's open
   finding `NEW-P2-02` (§46), and no rule here depends on its resolution. This
   contract emits neither class.
3. No class is claimed implemented; this table defines stable names only.
4. A rejection MUST preserve the original failing detail; suppression is
   prohibited (§41).

## 30. Validation model

Ordered layers. Each states its owner, input, and output. Later layers MUST NOT
run before earlier layers reach a determination.

| # | Layer | Owner | Input | Output |
| --- | --- | --- | --- | --- |
| 1 | Envelope validation | This contract | Envelope (§6) | Structurally valid or `CONTEXT_ENVELOPE_INVALID` |
| 2 | Identity validation | This contract | §5 identity fields | Valid or `CONTEXT_IDENTITY_INVALID` |
| 3 | Provenance validation | Provenance and Sensitivity spec; checked here | `source_refs`, provenance reference | Present and traceable, or `CONTEXT_PROVENANCE_MISSING` |
| 4 | Namespace validation | This contract | Namespace, consumer, tenant | Compatible or `CONTEXT_NAMESPACE_VIOLATION` |
| 5 | Policy validation | Integration Gateway §17 | Policy requirements, consumer | Evaluable and satisfied, or denied |
| 6 | Permission validation | Gateway §18; Shared Context access scope | Consumer permission evidence | Allowed or `AUTHORIZATION_DENIED` |
| 7 | Sensitivity validation | Provenance and Sensitivity spec; checked here | `sensitivity_level`, `allowed_use` | Compatible or `CONTEXT_SENSITIVITY_MISMATCH` |
| 8 | Schema validation | Context Graph Schema / declaring owner | Structure | Conformant or rejected |
| 9 | Transformation validation | This contract | `transformation_history` | Permitted and recorded, or `CONTEXT_TRANSFORMATION_UNPERMITTED` |
| 10 | Return-path validation | This contract | §13's thirteen checks | Passed, rejected, or quarantined |
| 11 | Conflict validation | This contract; adjudication elsewhere | Competing claims | Surfaced, or `CONTEXT_CONFLICT_UNRESOLVED` |
| 12 | Retention validation | Shared Context retention policy; checked here | Retention requirement | Compatible or denied |
| 13 | Observability validation | This contract | §40 projections | Producible, or ineligible |

### 30.14 What validation does not do

Validation MUST NOT:

1. authorize execution;
2. authorize provider or model access;
3. perform a canonical mutation;
4. resolve an unrelated bridge error, including any Framework Bridge finding;
5. imply trust.

Correspondingly: **`context validation ≠ trust`** and **`context validation ≠
mutation authorization`**. A validated proposal is still not eligible until
§31, and still not mutated until the canonical owner acts.

## 31. Shared Context mutation eligibility

A proposal becomes **mutation-eligible** only when **all** of the following
hold simultaneously for the exact proposal, namespace, tenant, and consumer:

| # | Condition |
| --- | --- |
| 1 | All §30 layers reached a passing determination |
| 2 | Return-path validation passed (§13) |
| 3 | Provenance complete and traceable (§14) |
| 4 | Namespace authorized and unflattened (§16) |
| 5 | Sensitivity and `allowed_use` compatible (§17) |
| 6 | No unresolved conflict (§24) |
| 7 | Snapshot currency established under Runtime §17.4 |
| 8 | Retention compatible (§27) |
| 9 | Not quarantined (§28) |
| 10 | Policy decision reference present (Gateway §18) |
| 11 | Required Operator approval exists for the mutation path (Runtime §17.1, Control Plane §16) |

Rules:

1. **Eligibility is not mutation.** `mutation eligible ≠ mutation performed`.
2. Eligibility is not Operator approval; condition 11 is a separate, explicit
   act.
3. Only the canonical Shared Context owner may perform the mutation (§11).
4. Any condition absent, expired, `unknown`, or malformed denies.

## 32. Agent Runtime interaction

Ten distinct stages. None is executed, connected, or implemented by this
document.

| # | Stage | Owner |
| --- | --- | --- |
| 1 | Run creation | Agent Runtime |
| 2 | Context request | Agent Runtime |
| 3 | Context selection | This contract (§7) |
| 4 | Context projection | This contract (§8, §9) |
| 5 | Execution-local use | Agent Runtime |
| 6 | Returned proposal | This contract (§11, §13) |
| 7 | Validation | This contract (§30) |
| 8 | Mutation eligibility | This contract (§31) |
| 9 | Observation | Agent Runtime / Control Plane (§40) |
| 10 | Run termination | Agent Runtime |

Rules:

1. Stages remain distinct; none implies the next.
2. This contract consumes Runtime §17.1's seven operations by name and defines
   no eighth.
3. Canonical mutation is not a stage of this table; it belongs to the canonical
   owner alone.

## 33. Agent Package interaction

A package MAY declare: required context capabilities (by **semantic name**);
allowed namespaces; required context schemas; memory requests; context-write
proposals; and retention requirements.

Rules:

1. **Package declarations MUST NOT grant access or mutation rights.** A
   declaration is a request statement (Agent Package Contract §10.2 rule 2,
   §12.2 rule 1).
2. An unlisted context class is unreadable and unproposable (Agent Package
   Contract §15 rule 4).
3. **Context capabilities are referenced by semantic name, never by
   cross-document ordinal position.** The Framework Bridge's capability
   renumbering relative to the Agent Package Contract is that contract's open
   finding `NEW-P2-03` (§46); no rule here depends on any ordinal.
4. This contract **defines no package lifecycle rendering field** and asserts
   **no** Agent Package contract version as canonically current (§46).

## 34. Framework Bridge interaction

Rules:

1. Framework-local context is bridge-local and never canonical (Framework
   Bridge §4.2 rule 3; Runtime §18 rule 2).
2. Framework-returned context enters exclusively through §13 and is ineligible
   for canonical mutation until §30 and §31 are satisfied.
3. **This contract MUST NOT consume unstable capability ordinals** (§33 rule 3).
4. **This contract MUST NOT treat an unvalidated framework profile as
   context-projection eligible** (§9 rule 3).
5. **This contract MUST NOT own runtime result normalization** (§22 rule 4).
6. **This contract MUST NOT resolve the Framework Bridge error overlap**
   (§29.2 rule 2).
7. No rule in this contract depends normatively on any Framework Bridge open
   finding.

## 35. Provider and model interaction

1. **Provider-bound context minimization.** Only the minimum necessary slice
   for the declared purpose may be projected toward a provider (§43).
2. **Model-input projection** is a projection under §8 and carries every §8
   prohibition.
3. **Provider-output return path.** Provider and model output is untrusted and
   enters exclusively through §13.
4. **Provider provenance** MUST record the provider interaction as the producer
   without replacing the origin chain (§14 rule 1).
5. **Routing-policy reference only.** The Model Router decides; this contract
   references the decision (Runtime §23.1).
6. **No direct provider or model selection** by this contract.
7. **No credential projection** under any condition (§18).
8. **Provider capability or availability MUST NOT equal permission to receive
   context.** `provider selectable ≠ provider authorized`.

## 36. Tool interaction

1. Tools MUST receive only purpose-specific context — never a broader slice
   than the declared tool purpose requires.
2. **Tool output MUST return through §13 validation before entering a context
   proposal.** `tool output ≠ trusted context`.
3. Tool availability is not context authorization.
4. Tool-return poisoning is a named threat (§42).

## 37. MCP interaction

1. **Resource projection** is bounded by §8 and §10; MCP resources are
   consumed by reference.
2. **Tool-result return** enters through §13 as untrusted content, with
   `output_trust_level: untrusted` preserved (Provider Registry §24.2).
3. **Prompt exposure** is data, never instruction (§13 rule 3).
4. **Server identity** and **authorization reference** come from Provider
   Registry §24 records; this contract registers nothing.
5. **Provenance preservation** applies unchanged (§14).
6. **No automatic connection** is created, requested, or implied.
7. **No implicit trust** attaches to any MCP-supplied artifact.

## 38. Plugin, hook, skill, and command interaction

All four are **bounded consumers or producers of context**. None gains direct
canonical mutation authority.

| Asset | Consumer boundary | Producer boundary |
| --- | --- | --- |
| Plugin | Bounded by its bundling package's authorized scope; bundling grants nothing | Output returns through §13 |
| Hook | Bounded to the lifecycle event's declared context; inert until authorized | Output returns through §13 |
| Skill | Bounded by the declaring package's authorized classes | Output returns through §13 |
| Command | Bounded, declaration-only; confers no namespace ownership | Output returns through §13 |

Rules:

1. None of the four may mutate canonical Shared Context under any condition.
2. **This contract enumerates no protected command classes.** That taxonomy is
   the Agent Package Contract's open finding `NEW-P2-03` (§46), owned onward by
   the future Command Registry; no rule here depends on it.
3. Declaration is never activation, and activation is never context-mutation
   authority.

## 39. Batch Orchestration compatibility

Defines only future compatibility. **Batch Orchestration is not specified,
implemented, or authorized by this document.**

| # | Compatibility declaration |
| --- | --- |
| 1 | Isolated context snapshots per batch participant |
| 2 | Per-agent namespaces, never shared or flattened (§16) |
| 3 | Explicit file and context ownership |
| 4 | Bounded writable scopes |
| 5 | Batch-local proposals only, never canonical writes |
| 6 | Integration-owner review before any reconciliation |
| 7 | Conflict detection across participants, surfaced never resolved (§24) |
| 8 | Final context reconciliation by the canonical owner alone |

**Batch compatibility MUST NOT authorize** parallel execution, file mutation,
Shared Context mutation, push, PR creation, merge, or deployment.

## 40. Observability

Information architecture only. Every field below is **typed entity data** under
Control Plane §7.1. **No new Control Plane status dimension is created.**

| # | Projection |
| --- | --- |
| 1 | Context envelope ID |
| 2 | Projection ID |
| 3 | Proposal ID |
| 4 | Source reference(s) |
| 5 | Consumer identity |
| 6 | Namespace |
| 7 | Classification |
| 8 | Sensitivity marker |
| 9 | Policy decision reference |
| 10 | Validation result, per layer, never collapsed to one boolean |
| 11 | Rejection or quarantine reason (§28, §29) |
| 12 | Transformation history |
| 13 | Compression reference, where applicable |
| 14 | Context version |
| 15 | Lease state |
| 16 | Mutation-eligibility state (§31) |
| 17 | Canonical mutation reference, where one eventually exists |
| 18 | Run reference |
| 19 | Framework session reference |

Rules:

1. Bridge fields MUST be labeled bridge-domain data and MUST NOT be rendered as
   a `lifecycle_status`, `evidence_state`, or `approval_state` value.
2. No projection may synthesize a universal "healthy" or green state.
3. `NOT_RUN` / `NOT_IMPLEMENTED` never renders as pass.
4. Rejections, quarantines, and losses MUST be rendered, never collapsed away.
5. Observability output MUST NOT contain secret values (§18).

## 41. Audit evidence

The minimum evidence required to reconstruct an exchange:

| # | Question the evidence must answer |
| --- | --- |
| 1 | What context was requested, with what declared purpose |
| 2 | What was selected |
| 3 | What was removed, filtered, or withheld, and why |
| 4 | What was transformed, by which class, in what order |
| 5 | What was projected, to which consumer, under which envelope |
| 6 | Who consumed it, and under which policy decision |
| 7 | What was returned, from which producer |
| 8 | Why it was accepted, rejected, or quarantined |
| 9 | Whether a canonical mutation occurred, and under whose authority |

Rules:

1. Evidence is append-only; **evidence deletion is a named threat** (§42).
2. A transfer without a Runtime §19 trace record is not a transfer; the
   receiving side treats untraced context as absent.
3. Evidence MUST NOT contain secret values (§18).
4. Absence of evidence is recorded as `unknown`, never as success.

## 42. Security considerations

| Threat | Mitigation posture |
| --- | --- |
| Prompt injection | Returned and projected content is untrusted data, never instruction (§13 rule 3; Runtime §31–§32); suspicion quarantines (§28) |
| Context poisoning | Return-path validation is mandatory (§13); writes are proposal-only (§11); suspicion quarantines (§28) |
| Provenance spoofing | Provenance must be present, traceable, and never replaced by the latest producer (§14); untraceable provenance rejects |
| Namespace escape | Namespaces are never flattened; cross-namespace movement requires an explicit recorded act (§16); fails closed |
| Sensitivity downgrade | Only a recorded redaction may lower sensitivity (§17 rule 1); sensitivity does not decay (§17 rule 2) |
| Permission amplification | Projection is subtractive or equal (§8 rule 1); eligibility never implies authorization (§9 rule 1) |
| Secret exfiltration | Secret values prohibited in payloads, memory, logs, and proposals (§18); reference ≠ value |
| Memory contamination | Six owner categories never conflated; no silent promotion (§19); framework memory is short-term working memory at most |
| Malicious compression | Compression may not fabricate, erase provenance, hide restrictions, or merge conflicts (§21) |
| Transformation ambiguity | Unrecorded transformation invalidates the envelope (§22 rule 2); ambiguity quarantines (§28 condition 7) |
| Stale-context use | Stale projections are never used automatically (§25 rule 1; Runtime §17.4) |
| Cross-run leakage | Run namespace isolation (§16 row 4); Runtime §19 trace attributes every transfer to both runs |
| Cross-agent leakage | Agent namespace isolation (§16 row 2); agent-local memory never shared (Runtime §18) |
| Tool-return poisoning | Tool output returns through §13 (§36 rule 2) |
| MCP-return poisoning | MCP output untrusted, returns through §13 (§37 rule 2) |
| Plugin or hook injection | Bounded consumers; output returns through §13 (§38) |
| Framework-memory persistence | Framework memory never becomes durable canonical memory silently (§19 rule 1) |
| Policy stripping | Policy loss fails closed (§23 row 5); compression may not hide restrictions (§21 rule 3) |
| Evidence deletion | Evidence is append-only (§41 rule 1); compression may not remove rejection evidence (§21 rule 6) |
| Proposal replay | A proposal binds to one exact namespace, tenant, consumer, and snapshot currency (§31); expiry ends eligibility (§26) |
| Context-conflict concealment | Conflicts are surfaced with provenance and precedence, never resolved by the bridge (§24) |

## 43. Privacy and minimization

1. **Purpose limitation.** Context may be selected only for a declared purpose
   and used only for it.
2. **Minimum necessary context.** The smallest slice satisfying the purpose
   (§7 rule 6).
3. **Retention limitation.** No projection outlives the canonical retention
   policy (§27).
4. **Consumer-specific projection.** Each envelope binds to one consumer (§6.2
   rule 4); a shared or broadcast projection is prohibited.
5. Personal or user-namespace context receives the same treatment with no
   relaxation.

## 44. Failure behavior

**All of the following MUST fail closed:**

1. Ambiguous authority;
2. Missing or untraceable provenance;
3. Unknown, unauthorized, or inferred namespace;
4. Unresolved or unevaluable policy;
5. Safety-relevant or authority-relevant context loss (§23);
6. Missing, expired, `unknown`, or malformed validation evidence;
7. Undetermined snapshot currency (Runtime §17.4 rule 4);
8. Unresolved conflict (§24).

There is no default-allow state, no substituted context, no cached fallback,
and no nearest-available context.

## 45. Non-goals

1. Shared Context runtime implementation.
2. Storage implementation.
3. Database schema or migration.
4. Vector database integration.
5. Memory service implementation.
6. Canonical mutation engine.
7. Context compression implementation.
8. Framework Adapter implementation.
9. Framework execution or SDK installation.
10. Package loading or execution.
11. Provider integration.
12. Model calls.
13. MCP connection.
14. Plugin loading.
15. Hook execution.
16. Command execution.
17. Batch Orchestration.
18. Frontend.
19. Backend.
20. Deployment.

## 46. Deferred dependencies

None is started or authorized by this document. Each remains owned by the
document named.

| # | Deferred dependency | Owner | This contract's containment |
| --- | --- | --- | --- |
| 1 | Framework Bridge `NEW-P2-01` — Runtime §16 coverage, incl. missing `normalize_result` counterpart | Framework Bridge Contract | §22 rule 4: result normalization is a separate concern; this contract owns none of it |
| 2 | Framework Bridge `NEW-P2-02` — `PROJECTION_UNSUPPORTED` / `BRIDGE_UNSUPPORTED_BEHAVIOR` overlap | Framework Bridge Contract | §29.2 rule 2: this contract emits neither class and resolves nothing |
| 3 | Framework Bridge `NEW-P2-03` — capability numbering divergence | Framework Bridge Contract / Agent Package Contract | §33 rule 3: capabilities referenced by semantic name only, never by ordinal |
| 4 | Framework Bridge `NEW-P2-04` — validation obligation not wired to eligibility | Framework Bridge Contract | §9 rule 3: an unvalidated framework profile cannot become context-projection eligible here |
| 5 | Agent Package `NEW-P2-01` — missing package-lifecycle rendering field | Agent Package Contract | §33 rule 4: this contract defines no such field |
| 6 | Agent Package `NEW-P2-02` — contract-version discrepancy | Agent Package Contract | §33 rule 4: no Agent Package version is declared canonically current |
| 7 | Agent Package `NEW-P2-03` — protected command classes not enumerable | Agent Package Contract / future Command Registry | §38 rule 2: this contract enumerates none |
| 8 | Context Compression contract | Future, separate task | §21 bounds the safety envelope only |
| 9 | Durable-memory contract | Future, separate task | §19, §20 bound proposals only |
| 10 | Context-validation implementation | Future, separate task | §30 is vocabulary only |
| 11 | Context-proposal lifecycle implementation | Future, separate task | §12 rule 4: states only, no transition contract |
| 12 | Per-framework empirical validation | Future per-framework adapter specifications | §9 rule 3; remains `NOT_PERFORMED` |
| 13 | Future Batch Orchestration contract | Future, separate task | §39 declares compatibility only |

## 47. Acceptance criteria

This specification task is complete when all of the following hold:

1. All 50 sections (§1–§50) are present and each required topic is addressed.
2. Terminology (§2) defines at least the thirty terms the task brief named.
3. No concern is owned by more than one document (§3); every consumed concept
   cites its canonical owner.
4. The direction rule (§4.1) is stated, and no rule anywhere permits a
   framework, agent, package, provider, tool, plugin, hook, command, MCP
   server, adapter, or batch worker to mutate canonical Shared Context.
5. Only three identities are minted (§5.2 rule 2); no owner-defined field is
   replaced.
6. Every envelope field (§6.1) is stated, and the envelope carries no authority.
7. Selection is purpose- and consumer-bounded, and unrestricted project-context
   requests are rejected (§7).
8. Projection is subtractive or equal with respect to authority (§8).
9. Projection eligibility does not imply execution authorization (§9 rule 1),
   and an unvalidated framework profile cannot become eligible (§9 rule 3).
10. The five write/mutation concepts are separated and only the canonical owner
    may mutate (§11).
11. Returned context is treated as untrusted in every case (§13).
12. Provenance is preserved, never replaced by the latest producer (§14).
13. Lineage uses only existing `CONTEXT_GRAPH_SCHEMA.md` relation types (§15).
14. Namespaces are never flattened (§16).
15. Sensitivity does not decay and may be lowered only by recorded redaction
    (§17).
16. Secret values are prohibited in payloads, memory, logs, and proposals (§18).
17. Memory scopes map onto Agent Runtime §18's six categories **by semantic
    name**, with no new category and no renumbering (§19).
18. Compression may not fabricate, erase provenance, hide restrictions, or
    merge conflicts (§21).
19. Safety- or authority-relevant context loss fails closed (§23).
20. Conflicts are surfaced, never silently resolved (§24).
21. Every bridge-owned rejection class carries a deterministic discriminator
    and duplicates no owner-defined class (§29).
22. Validation does not authorize execution, provider access, or mutation, and
    does not imply trust (§30.14).
23. Mutation eligibility is distinct from mutation and from Operator approval
    (§31).
24. All consumer and producer boundaries (§32–§39) keep canonical mutation with
    the canonical owner alone.
25. No new Control Plane status dimension is created (§40).
26. All twenty-one security threats (§42) are addressed with a section-citing
    mitigation.
27. **Open-finding containment holds:** all seven upstream P2 findings are
    recorded as deferred, none is resolved, and no normative rule depends on
    any of them (§46).
28. No implementation, execution, storage, memory service, compression,
    mutation engine, framework integration, provider connection, credential, or
    deployment is claimed anywhere (§1.4).

## 48. Document metrics (normative)

Every count below was computed directly from this document's own sections. A
future amendment that changes a table MUST recompute and restate the
corresponding row; a divergence between this table and its section is a defect
in this document, following the discipline of
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §1.4 and
`[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` §1.4.

| Dimension | Count | Authoritative section |
| --- | --- | --- |
| Specification sections | 50 | §1–§50 |
| Terminology entries | 31 | §2 |
| Architectural ownership rows | 20 | §3 |
| Canonical-versus-projected register rows | 13 | §4.3 |
| Context identity fields | 14 | §5.1 |
| Context envelope fields | 14 | §6.1 |
| Selection requirements | 8 | §7 |
| Projection prohibitions | 9 | §8 |
| Projection eligibility preconditions | 12 | §9 |
| Read-boundary consumers | 10 | §10 |
| Write/mutation concepts | 5 | §11 |
| Proposal lifecycle phases | 10 | §12 |
| Return-path checks | 13 | §13 |
| Namespace categories | 10 | §16 |
| Secret prohibitions | 6 | §18 |
| Memory scopes | 8 | §19 |
| Memory proposal elements | 8 | §20 |
| Compression prohibitions | 7 | §21 |
| Transformation classes | 8 | §22 |
| Context-loss classes | 6 | §23 |
| Quarantine conditions | 9 | §28 |
| Consumed rejection classes | 9 | §29.1 |
| Bridge-owned rejection classes | 11 | §29.2 |
| Validation layers | 13 | §30 |
| Mutation-eligibility conditions | 11 | §31 |
| Agent Runtime interaction stages | 10 | §32 |
| Batch compatibility declarations | 8 | §39 |
| Observability projections | 19 | §40 |
| Audit evidence questions | 9 | §41 |
| Security threats | 21 | §42 |
| Failure-closed conditions | 8 | §44 |
| Non-goals | 20 | §45 |
| Deferred dependencies | 13 | §46 |
| Acceptance criteria | 28 | §47 |

## 49. References

### 49.1 Repository (canonical)

- `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`
- `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]`
- `[[../research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001]]` (research)
- `[[../research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002]]` (research)
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]`
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`
- `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]`
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001]]`
- `[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`
- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`
- `shared_context/CONTEXT_GRAPH_SCHEMA.md`,
  `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md`,
  `shared_context/context_provenance/**`
- `shared_context/MODEL_ROUTING.md`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md`

### 49.2 External

**None.** No external standard, SDK, API, database, vector store, or online
documentation was consulted or is claimed.

## 50. Amendment and supersession

1. This document may be amended only additively unless a major
   `context_bridge_contract_version` bump is explicitly declared.
2. An amendment MUST recompute and restate §48's document metrics.
3. An amendment MUST NOT weaken any rule in §3.1's precedence chain.
4. An amendment MUST NOT resolve, restate, or work around any deferred
   dependency of §46 that belongs to another owner. Silent modification of an
   owner contract's meaning through this document is prohibited.
5. A change that would add a memory category, a context operation, a
   sensitivity level, a graph relation type, or a Control Plane dimension is
   **not** an amendment to this document — it belongs to that concept's owner
   and requires that owner's own separately reviewed amendment.
6. This document does not supersede, rename, or absorb any canonical owner
   document cited in §3 or §49.1; every citation remains that document's
   unmodified, unweakened text unless a separate, explicitly authorized
   amendment task states otherwise.
