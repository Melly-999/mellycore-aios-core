# MellyCore Agent Runtime Canonical Seam Decision 001

**Decision ID:** MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001
**Task ID:** MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001
**Version:** 1.0

## 1. Status

**ACCEPTED as a canonical seam decision only.**

This record fixes where each Agent Runtime architectural seam is resolved and
which canonical owner document, if any, is minimally amended. It **authorizes no
implementation**: no Agent Runtime, no framework bridge, no agent framework
installation or connection, no agent execution, no model-provider call, no tool
invocation, no provider access or authentication, no credential configuration,
no persistence, no queue, no frontend, and no deployment.

It does **not** reorder, reprioritize, or reinterpret the global higher-priority
pointer `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`.

Remediation claims recorded here remain **unverified** pending
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002`.

## 2. Purpose

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001` (commit
`ac762f5a9964c5c5111b83e831aee6624651e391`) returned
`FAIL_REMEDIATION_REQUIRED` with P0 = 0, P1 = 4, P2 = 5, P3 = 5. Three of the
four blocking findings are **seam conflicts**: the Agent Runtime states
semantics that a different canonical owner already owns and, as written, forbids
or cannot represent.

Such a conflict has exactly two honest resolutions:

1. **Conform the Agent Runtime** to the existing owner, or
2. **Minimally amend the owner** where its current model provably cannot
   represent the accepted required semantics.

A third option — restating or redefining another subsystem's canonical
semantics inside the Agent Runtime document — is **prohibited**, because it
hides the conflict rather than resolving it and leaves two documents asserting
incompatible truths. This record exists so that every owner amendment is
decided, justified, and bounded **before** any specification is edited.

## 3. Reviewed findings

Imported verbatim in scope from
`docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md` §45.
The review record owns these definitions; this record does not restate or
weaken them.

| ID | Severity | Finding | Owner in conflict |
| --- | --- | --- | --- |
| `P1-01` | Blocking | Six `run_state` values project to `lifecycle_status:active`, which Control Plane §8.2 forbids for a running agent; §9.5/§9.7 Run lifecycle sets exclude `active`, `queued`, `draft`, `ready` | Control Plane |
| `P1-02` | Blocking | Runtime facts 5 and 6 duplicate Registry facts 5 and 6, whose §21.3 record types are provider-scoped and require `provider_id`, while fact 10 already delegates to all eight | Provider Registry |
| `P1-03` | Blocking | Multi-attempt evidence contradicts AI Operations §5.9 deduplication by `run_id` and §5.1's single `outcome`/`model`/`provider` per run | AI Operations Intelligence |
| `P1-04` | Blocking | §23.6 mandates `run_state:waiting_for_operator` for an unresolved routing tie; §12.3 does not permit that transition from `waiting_for_model` | Agent Runtime (internal) |
| `P2-01` | Material | Stale-snapshot resolution is "`blocked` or re-read per policy" with no defined, declared, or deterministic policy | Agent Runtime / Shared Context |
| `P2-02` | Material | `model_routing_decision_ref` lives in an envelope frozen at attempt start, but routing decisions are step-scoped and therefore later | Agent Runtime (internal) |
| `P2-03` | Material | Agent-run identity not reconciled with the existing run-ledger `run_id` form; loop runs never mentioned | AI Operations / Loop Operations |
| `P2-04` | Material | Concurrent acceptance of one `broadcast_proposal` has no specified race behavior | Agent Runtime (internal) |
| `P2-05` | Material | Runtime-instance failure or restart with an attempt in an unknown state is unaddressed | Agent Runtime (internal) |
| `P3-01` | Editorial | Context-flow trace enumerates 16 fields against a 17-field claim | Agent Runtime |
| `P3-02` | Editorial | Handoff envelope contents are 12, described as 11 | Agent Runtime |
| `P3-03` | Editorial | §33 has 38 rows but 40 distinct class names | Agent Runtime |
| `P3-04` | Editorial | `INSUFFICIENT_PRICING_DATA` has no owner or taxonomy entry; nine-state ↔ eleven-fact mapping unstated | Agent Runtime |
| `P3-05` | Editorial | §8.3 rule 1 states the type discipline in implementation-language-specific terms | Agent Runtime |

## 4. Canonical owners

Unchanged by this record, and reaffirmed:

| Concern | Canonical owner |
| --- | --- |
| Status dimensions, status vocabulary, display projection | `MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` §8 |
| Entity catalogue and common entity contract | Control Plane §7 |
| Provider records, the eight provider facts, acting identities, credential classes, authorization-record custody | `MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` |
| Provider access, credentials, provider policy-evaluation order, provider error taxonomy | `MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` |
| Unified Run Ledger record, token and cost semantics, ledger deduplication and supersession | `MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` §5, §13 |
| Loop registry, loop run identity, loop state and guard contracts | `MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md` + `shared_context/loops/**` |
| Canonical Shared Context truth, admission, provenance, sensitivity | `shared_context/**`, Context Gate specs, Context Provenance and Sensitivity spec |
| Permissions and approval semantics | Control Plane §16 + Gateway §18 |
| Agent runtime coordination, run lifecycle, envelopes, bridges, handoffs, runtime events | `MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` |
| Agent packages | Deferred — future Agent Package Contract |

## 5. Decision principles

1. **The existing owner wins** unless its accepted model provably cannot
   represent the required semantics. "Inconvenient" is not "cannot".
2. **A seam is never hidden inside the Agent Runtime.** The Agent Runtime never
   redefines, extends by restatement, or locally overrides another owner's
   vocabulary.
3. **Owner amendments are additive and minimal.** An amendment adds the smallest
   normative clause that closes the seam. It never weakens an existing
   prohibition, never broadens an unrelated section, and never removes an
   existing guarantee.
4. **Additive is not weakening.** Adding a new enum member or a new optional
   evidence field does not require an ADR weakening amendment under Gateway §33
   rule 5, provided every existing rule survives unchanged. Both amendments
   below are additive and preserve every prior prohibition verbatim.
5. **Higher-precedence contracts are absolute.** AI Operations §1.8 places the
   enforced loop contracts (`shared_context/loops/RUN_LEDGER_SCHEMA.json`,
   `LOOP_STATE_SCHEMA.json`) **above** the AI Operations specification. Any AI
   Operations amendment must therefore be satisfiable by existing loop ledgers
   **without editing them**. All new fields are optional with explicit
   absent-value semantics, so existing loop records remain conforming and
   unchanged.
6. **Runtime-specific semantics belong to the Runtime.** Where no owner defines
   a needed record, the Agent Runtime may define it — provided it is genuinely
   runtime-scoped and cannot be confused with an existing owner's record.
7. **Provider authorization stays delegated.** Nothing here permits the Agent
   Runtime to compute, cache, summarize, or second-guess provider authorization.
8. **No safety property is traded for coherence.** Canonical serialization,
   digest safety, package/runtime separation, framework-bridge restrictions,
   Shared Context protections, memory categories, handoff acceptance, provider
   gateway enforcement, cancellation honesty, retry and reconciliation
   safeguards, tenant isolation, operator approval, and inert-v1 boundaries are
   preserved unchanged.

## 6. Lifecycle projection decision (`P1-01`)

### 6.1 The conflict, restated precisely

Control Plane §8.1 fixes the lifecycle legal values as `draft`, `planned`,
`queued`, `ready`, `active`, `blocked`, `completed`, `failed`, `cancelled`,
`superseded`, `historical`. Control Plane §8.2 states that `active` "is
lifecycle-only and means an effective policy/configuration. It MUST NOT describe
connectivity, **a running agent**, selected UI state, or general availability."

The Agent Runtime is the first MellyCore subsystem to represent a **live** run.
The Control Plane's `Run` entity was specified as "normalized historical
execution evidence" for a static, evidence-only phase, and its two
Run-rendering modules (§9.5, §9.7) accordingly enumerate only `planned`,
`blocked`, `completed`, `failed`, `cancelled`, `historical`.

### 6.2 Why the owner cannot represent the semantics

The lifecycle enum contains **no member meaning "currently executing"** other
than `active`, and `active` is explicitly forbidden for exactly that meaning.
Every conforming alternative was tested and rejected:

- **Reuse `active`.** Rejected. §8.2's prohibition is a deliberate safety
  separation preventing an operator from reading "active" as "an agent is
  running" when it denotes an effective policy. Overloading it reintroduces the
  ambiguity §8.2 exists to prevent and would weaken an existing rule.
- **Project executing states to `queued` or `ready`.** Rejected. Both would
  misreport an in-flight run as not yet started, and Review 001 requires that
  waiting, running, blocked, reconciliation, and terminal meanings not collapse.
- **Omit `lifecycle_status` while executing** (permitted by §8.1's "omit the
  field when inapplicable"). Rejected. It removes an executing run from every
  lifecycle filter, sort, and module `Statuses` contract, and §8.2 requires a
  module `Statuses` row to be a complete cross-dimensional contract. Operators
  would lose the ability to see live work in the surfaces designed to show it.
- **Add a seventh status dimension.** Rejected and prohibited: it contradicts
  Control Plane §24's accepted six-dimension decision.
- **Define an Agent-Runtime-local alias.** Rejected under principle 2.

### 6.3 Decision

**Minimally amend the Control Plane** by adding exactly one additive lifecycle
member, `running`, and reaffirming the `active` prohibition unchanged.

- `lifecycle_status:running` means **a live execution is in progress for this
  entity**. It applies only to entities that can execute — currently `Run`.
- `lifecycle_status:active` keeps its existing meaning and its existing
  prohibition **verbatim**: it still MUST NOT describe connectivity, a running
  agent, selected UI state, or general availability.
- The two labels are unambiguous because Control Plane §8.1 fixes machine
  identity as the dimension-qualified pair; `lifecycle_status:running` and
  `run_state:running` are distinct machine values, exactly as §8.1 already
  permits for `Unknown`, `Expired`, and `Rejected`.
- Control Plane §9.5, §9.7, and §9.10 extend their Run lifecycle sets to the
  full live-run set so the projection is renderable.

No dimension is added. No existing value changes meaning. No existing
prohibition is relaxed.

### 6.4 Resulting projection

The Agent Runtime publishes a complete, unambiguous 17-row projection table
(spec §12.2). Waiting-on-a-human and open-obligation states project to
`blocked`; in-flight states project to `running`; admission states project to
`draft`, `planned`, `ready`, and `queued`; terminal states project to their
canonical terminal equivalents. `run_state` remains the authoritative
fine-grained field; the projection is explicitly lossy, deterministic, and
never the reverse direction.

## 7. Authorization-fact decision (`P1-02`)

### 7.1 The conflict, restated precisely

Registry §21.3 defines exactly two authorization record types —
`tenant_provider_authorization` (Registry fact 5) and
`tenant_capability_authorization` (Registry fact 6) — and **both require a
`provider_id`**. Agent Runtime fact 10 already delegates entirely to all eight
Registry facts, which include those two. Agent Runtime facts 5 and 6 named the
same concepts and, for fact 5, named Registry custody as their owner.

Consequences found by Review 001: facts 5 and 6 are either re-implementations of
provider facts nested inside fact 10 (violating the Runtime's own rule 3), or
agent-scoped facts with no defined record type (leaving the concern unowned).
Under the literal reading, a purely local agent run touching no provider could
not be authorized at all, because no `provider_id` exists to bind.

### 7.2 Decision

**Resolve entirely inside the Agent Runtime. The Provider Registry is not
amended and its eight facts remain byte-identical.**

Runtime facts 5 and 6 are renamed and redefined as unambiguously
**runtime-scoped** authorizations with their own record types and their own
vocabulary:

- Fact 5 becomes **Tenant runtime authorization**, evidenced by a
  `tenant_agent_runtime_authorization` record: subject = tenant, action scope =
  operating the Agent Runtime for agent runs in one environment. It says nothing
  about any provider.
- Fact 6 becomes **Agent capability authorization**, evidenced by a
  `tenant_agent_capability_authorization` record binding a tenant to one
  `agent_definition_id` and one capability drawn from the **agent capability
  vocabulary** (the package's `declared_capabilities`), explicitly **not** from
  the provider capability vocabulary.

Normative separations added:

1. Neither fact 5 nor fact 6 is satisfied by, substitutes for, or is satisfiable
   by a Registry `tenant_provider_authorization` or
   `tenant_capability_authorization`, and vice versa.
2. Provider-side tenant authorization and provider-side capability
   authorization exist **only** inside fact 10 and remain owned by the Registry
   and evaluated by the Gateway.
3. The two capability vocabularies are named and disjoint in use: agent
   capability classes are authorized by fact 6; provider capability IDs are
   authorized inside fact 10.
4. An agent run that proposes no provider operation requires facts 1–8 and
   never requires a `provider_id`.

### 7.3 Consequential correction

Review 001's ownership analysis exposed a dependent inconsistency that must be
closed for the fact table to be coherent: §12.2 defined `authorized` as "all
eleven facts hold", yet facts 9, 10, and 11 are per-invocation facts that cannot
hold at run-authorization time for tools, providers, and operations not yet
proposed. This record fixes the evaluation point explicitly:

- **Facts 1–8 are run-admission facts**, all of which must hold to enter
  `authorized`.
- **Facts 9, 10, and 11 are per-invocation facts**, evaluated at the exact point
  of tool use, provider proposal, and consequential operation respectively, and
  **never** pre-satisfied at run authorization.

This narrows what run authorization claims; it grants nothing new. No fact is
inferred from another and no aggregate readiness field is introduced.

## 8. Run Ledger identity decision (`P1-03`, `P2-03`)

### 8.1 The conflict, restated precisely

AI Operations §5 owns the Unified Run Ledger. §5.9 states "duplicate run events
(same `run_id`) are deduplicated to one record", and §5.1's logical record
carries exactly one `outcome`, one `model`, and one `provider` per `run_id`.
The Agent Runtime introduces multiple **attempts** under one logical `run_id`
and requires (§13 rule 1) that every attempt's ledger records remain intact and
addressable — evidence that §28 depends on for reconciling unknown external
outcomes.

Separately, §5.1 requires `run_id` to be "compatible with the existing
run-ledger `run_id` form", which `shared_context/loops/RUN_LEDGER_SCHEMA.json`
constrains to `<loop-id>--<UTC timestamp>--<12 hex>` — a **loop** run identity.

### 8.2 Why the owner cannot represent the semantics

Deduplication keyed on `run_id` alone is mathematically incapable of preserving
two attempts of one run: any second attempt is, by that key, a duplicate of the
first and is collapsed. No reading of §5.9 preserves attempt evidence. The
Agent Runtime is a declared non-owner and cannot amend §5.9 itself, and
declaring a second, competing Agent Runtime ledger is explicitly prohibited.

### 8.3 Decision

**Minimally amend AI Operations Intelligence §5**, additively, so the canonical
ledger can carry attempt-level evidence:

1. **`ledger_record_id`** — a stable unique identity for one ledger record,
   added to §5.1. It, not `run_id`, is the deduplication identity.
2. **`attempt_id`** — optional, added to §5.1. Absent or `null` means a
   single-attempt domain, which is exactly the existing loop behavior.
3. **`run_kind`** — optional, added to §5.1, with values `loop_run` and
   `agent_run` and an explicit default of `loop_run` for records conforming to
   the loop run-ledger schema. `run_id` uniqueness and form are scoped **within**
   a `run_kind` namespace; the loop form is preserved unchanged for
   `run_kind: loop_run`; an `agent_run` identity is opaque and is never
   substituted for a loop identity or vice versa.
4. **Deduplication rule** — records sharing a `run_id` but differing in
   `attempt_id` are **distinct records and MUST NOT be deduplicated**.
   Deduplication applies only to records with identical `ledger_record_id`.
5. **Derived logical-run summary** — a logical-run view MAY be derived from the
   complete attempt set. It is derived, never stored as a replacement, and
   **never erases, supersedes, or hides** attempt-level records. Where attempts
   disagree, the summary reports the disagreement rather than choosing.
6. **Attempt-level attribution** — when `attempt_id` is present, `model`,
   `provider`, and `outcome` are attributed to that attempt, not to the logical
   run.

### 8.4 Backward compatibility

Every existing loop run ledger remains conforming **without modification**:
`attempt_id` absent → single-attempt semantics; `run_kind` absent → `loop_run`;
`ledger_record_id` absent → the record's existing identity is used, and
deduplication reduces exactly to the prior `run_id` behavior. §5.2 through §5.8
and §13 are untouched. The higher-precedence loop schemas
(AI Operations §1.8 item 3) are **not edited** and are not contradicted.

**No migration is performed, required, or claimed.** No persistence exists to
migrate.

### 8.5 Runtime-side alignment

The Agent Runtime records, without redefining the owner: one logical run has one
or more attempts; one attempt has one or more steps; the runtime emits
append-only records carrying `ledger_record_id`, `run_id`, `attempt_id`,
`run_kind: agent_run`, and ordering evidence; retries create distinct attempt
identities; replays create distinct run identities with recorded linkage; and an
agent run is never represented as, projected onto, or substituted for a loop
run. A loop that triggers an agent run records an explicit typed reference
carrying both kind and identity — never identity reuse.

## 9. Routing-tie transition decision (`P1-04`)

**Resolved entirely inside the Agent Runtime. No owner is amended.**

The lifecycle graph gains the transitions the architecture already mandates:
`waiting_for_model`, `waiting_for_tool`, and `waiting_for_agent` may each
transition to `waiting_for_operator` when, and only when, a recorded escalation
condition requires a human decision. All three are added rather than only the
routing case, because tool-approval and handoff-adjudication escalations reach
the same state by the same logic, and leaving them unlisted would reproduce the
defect under a different trigger.

Guarantees attached: every such transition carries the §12.5 evidence record
naming its escalation reason class; no tie is ever resolved by silent fallback
or arbitrary selection; no unauthorized model may be selected; and the operator
decision that releases the run remains action-, revision-, and time-bound under
§30.2. `reconciliation_required` deliberately does **not** gain this
transition: it is already an operator-visible open obligation and routing it
through a waiting state would obscure that.

## 10. P2 policy decisions

| Finding | Decision | Location |
| --- | --- | --- |
| `P2-01` | A **declared, deterministic staleness policy** is mandatory. Six exact conditions (current; stale non-material; stale material; policy absent; source unavailable; conflicting revision) each have one outcome. Absent policy fails closed to `blocked`. A materially changed snapshot invalidates the envelope's context binding and requires renewed authorization. No silent substitution or automatic acceptance. | Agent Runtime §17.4 (new), Scenario 25 |
| `P2-02` | **Immutable envelope revision chain.** `model_routing_decision_ref` is removed from the envelope; routing decisions become step-scoped, digest-bound artifacts. Where a run must be bound to a routing decision before authorization, a **new envelope revision** is created, the prior revision remains auditable, and validation and authorization are renewed against the new digest. An authorized envelope is never mutated; a routing change after authorization invalidates that authorization. | Agent Runtime §15.4 (new), §23 |
| `P2-03` | **Typed identity namespaces** (`run_kind`) with forbidden substitution, as decided in §8.3 of this record. Loop Operations is neither renamed nor absorbed. | AI Operations §5.1; Agent Runtime §8.4 (new) |
| `P2-04` | **Single-winner broadcast with an atomic acceptance decision.** Acceptance is an atomic compare-and-set on the handoff record using an expected-version precondition, reusing the optimistic-concurrency mechanism §29.2 already mandates. The first successful claim wins; every later claim is denied with an explicit class and creates no run. Losing claims release their provisional budget reservation to the parent. No recipient gains scope by racing: the winner's effective scope is still the intersection of the handoff scope and its own authorizations. | Agent Runtime §20.4 (new) |
| `P2-05` | **Explicit restart and recovery model.** A new runtime instance claims orphaned runs only through a recorded takeover event. A recovery matrix maps each last-durable state, with and without an authoritative external status, to a resulting state. Any state in which an external effect could be in flight and cannot be positively excluded resolves to `reconciliation_required`. No unknown attempt is ever blindly redispatched. Resumption within the same attempt is permitted only when no external effect could be in flight. | Agent Runtime §29.3 (new) |

## 11. Owner documents requiring amendment

| Document | Sections amended | Nature | Justification |
| --- | --- | --- | --- |
| `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | §8.1 (one enum member), §8.2 (one clause), §9.5, §9.7, §9.10 (Run lifecycle sets) | **Additive** | The lifecycle enum has no member meaning "executing" and forbids the only near-fit; a live run is otherwise unrepresentable (§6.2) |
| `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | §5.1 (three optional fields), §5.9 (deduplication identity and attempt preservation) | **Additive** | Deduplication keyed on `run_id` alone cannot preserve two attempts of one run (§8.2) |

Both amendments preserve every existing prohibition, guarantee, and enum member
verbatim, add only optional or additive elements, and are backward compatible
with every existing record and fixture.

## 12. Owner documents not requiring amendment

| Document | Why unchanged |
| --- | --- |
| `MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | `P1-02` is fully resolved by making the Runtime's own facts runtime-scoped. The eight provider facts, §21.3 record types, and §21.2 rules are untouched |
| `MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | No finding implicates it; its error taxonomy, policy order, retry, and enablement gate are adopted unchanged |
| `MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` | Complementary; no seam |
| `MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md` and `shared_context/loops/**` | `P2-03` is resolved by namespacing at the ledger layer; the loop model is neither renamed nor absorbed, and the higher-precedence loop schemas are not edited |
| `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md`, Context Provenance and Sensitivity spec | `P2-01` is a runtime consumption policy over snapshots the Shared Context Layer already owns; admission and provenance semantics are unchanged |
| `shared_context/SAFETY_CONTRACT.md`, `VALIDATION.md` | Unaffected; no safety boundary is relaxed |
| `MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | Not superseded, silently or otherwise; no amendment weakens a rule it governs |
| Both prior review records and both original task reports | Historical evidence; immutable by construction |

## 13. Compatibility impact

- **Control Plane.** Purely additive. Existing entities, fixtures, modules, and
  the six-dimension model are unaffected. No consumer that never renders a live
  run observes any change. `active` behaves exactly as before.
- **Provider Registry.** Byte-identical. The eight facts remain eight.
- **Integration Gateway.** Unaffected; provider authorization remains delegated
  and the §32 enablement gate still governs, none of it passing.
- **AI Operations.** Additive; all new fields optional with defined absent
  semantics. Existing loop ledger records remain conforming unmodified.
- **Loop Operations.** Unaffected. Loop run identity, guard behavior, and
  ledger form are preserved exactly.
- **Shared Context.** Unaffected; the staleness policy constrains the runtime's
  consumption, not the Layer's canonical truth.

## 14. Migration impact

**None executed, and none claimed.** No Agent Runtime, Run Ledger persistence,
database, queue, or agent package exists. There is no stored record to migrate.
The AI Operations amendment is specified so that, if persistence is ever
separately authorized, existing loop ledgers satisfy it without rewriting: every
added field is optional with an explicit absent-value meaning that reproduces
current behavior exactly. Any future implementation task must re-derive its own
migration analysis; this record supplies none.

## 15. Implementation impact

**No implementation is authorized by this record.** It constrains a future,
separately authorized implementation as follows: the lifecycle projection table
is fixed; the eleven authorization facts have fixed names, records,
vocabularies, and evaluation points; ledger records must carry
`ledger_record_id` and, for agent runs, `attempt_id` and `run_kind`; envelopes
are revision-chained and never mutated; staleness, broadcast acceptance, and
restart recovery follow the stated deterministic policies. Agent Runtime
implementation, the Agent Package Contract, the Framework Bridge Contract, the
Shared Context Bridge, and the Agent Runtime Scaffold all remain **blocked**
pending `MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002` and separate
explicit Operator authorization.

## 16. Explicit non-authorizations

This record authorizes none of: Agent Runtime implementation; framework bridge
implementation; Agent Package Contract, Framework Bridge Contract, or Shared
Context Bridge drafting; Agent Runtime Scaffold work; agent framework SDK
installation, vendoring, or dependency declaration; execution of any agent,
sub-agent, workflow, graph, crew, or conversation; any model-provider API call;
any tool invocation; any provider connection, authentication, credential
configuration or verification, OAuth flow, or token creation; any MCP or
integration-fabric connection or webhook registration; persistence, database, or
queue implementation; backend or frontend implementation; dependency
installation, workflow YAML, release, or deployment; any push, pull request,
merge, or remote branch; or any MellyTrade interaction.

Live provider work remains blocked and unauthorized. Migration triggers #1, #4,
#5, #6, and #7 remain uncrossed.

## 17. Supersession and amendment rules

This record is amended only by an explicit, Operator-approved successor decision
record that names it and states exactly what changes. Superseded content is
retained and marked, never deleted. A weakening amendment — one that relaxes a
prohibition preserved here, or that widens either owner amendment beyond its
stated bound — additionally requires an ADR amendment under Gateway §33 rule 5.

Neither owner amendment made under this record may be widened by a later task
citing this record as precedent. Each is bounded to the exact sections listed in
§11.

## 18. References

- `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md`
- `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001.md`
- `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`
- `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001.md`
- `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md`
- `shared_context/loops/RUN_LEDGER_SCHEMA.json`, `LOOP_STATE_SCHEMA.json`
- `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`
- `shared_context/SAFETY_CONTRACT.md`, `VALIDATION.md`

### 18.1 Seam summary

| Finding | Canonical owner | Runtime responsibility | Selected resolution | Documents changed | Why alternatives were rejected |
| --- | --- | --- | --- | --- | --- |
| `P1-01` | Control Plane §8 | Publish a deterministic 17-row projection; never define status values | Add additive `running` lifecycle member; reproject all states | Control Plane, Agent Runtime | Reusing `active` weakens a safety prohibition; `queued`/`ready` misreport in-flight work; omission removes runs from lifecycle surfaces; a seventh dimension is forbidden; a local alias hides the seam |
| `P1-02` | Provider Registry §21 | Define only runtime-scoped authorization stages | Rename/redefine facts 5–6 as runtime records with an agent capability vocabulary; fix fact evaluation points | Agent Runtime only | Amending Registry would change the eight facts, which must remain exactly eight; reusing provider-scoped records makes provider-free runs unauthorizable |
| `P1-03` | AI Operations §5 | Emit append-only evidence as a producer only | Add `ledger_record_id`, optional `attempt_id`, attempt-preserving deduplication, derived summaries | AI Operations, Agent Runtime | Keying dedup on `run_id` cannot preserve attempts under any reading; a second Runtime-owned ledger is prohibited; treating an attempt as a run destroys logical-run identity |
| `P1-04` | Agent Runtime §12 | Own its own lifecycle graph | Add `waiting_for_*` → `waiting_for_operator` with mandatory evidence | Agent Runtime only | No owner is implicated; leaving the graph closed contradicts §23.6; an unstated intermediate hop is interpretation |
| `P2-01` | Shared Context (truth) / Runtime (consumption) | Declare a deterministic consumption policy | Six exact conditions, fail-closed default, material change invalidates authorization | Agent Runtime only | Shared Context already owns snapshot truth; the gap was the runtime's undefined branch selection |
| `P2-02` | Agent Runtime §15 | Keep authorized envelopes immutable | Revision chain; routing decisions become step-scoped artifacts | Agent Runtime only | Mutating the envelope breaks the digest; one attempt per model call breaks the step model |
| `P2-03` | AI Operations / Loop Operations | Never present an agent run as a loop run | `run_kind` namespacing with forbidden substitution | AI Operations, Agent Runtime | Renaming or absorbing the loop model is prohibited; sharing one identity form invites collision and confusion |
| `P2-04` | Agent Runtime §20 | Make acceptance atomic | Single-winner compare-and-set; losers denied and budget released | Agent Runtime only | Multi-accept violates the parent budget invariant; policy-selected arbitration needs an arbiter no owner defines |
| `P2-05` | Agent Runtime §29 | Never redispatch unknown work | Recorded takeover plus a recovery matrix defaulting to reconciliation | Agent Runtime only | Persistence mechanism is deferred, but the safe-state requirement cannot be |
