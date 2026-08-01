# MellyCore Integration Gateway Security Contract Spec

**Task ID:** MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001
**Contract ID:** MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_001
**Version:** 1.0
**Status:** ACCEPTED as a specification-level security contract only. **This status does not authorize Gateway implementation, runtime execution, adapter scaffolding, provider authentication, credential configuration or access, any provider API call, any MCP connection, any integration-fabric connection, webhook registration, or deployment.** It fixes the enforcement boundary a later, separately authorized implementation must satisfy.
**Scope:** Defines the complete specification-level security boundary governing how MellyCore AIOS may later route a request from an operator or agent, through MellyCore identity, tenant, capability, policy, credential, and approval evaluation, out through a native adapter, governed integration fabric, or restricted MCP path, to an exact resource at a downstream enterprise provider — and how inbound webhooks and provider events re-enter that boundary.

---

## 1. Title and status

### 1.1 Status meaning (normative)

This is an **accepted specification-level contract**, in the same sense as
`[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`,
`[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`, and
`[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`.

Acceptance means only that the trust boundary, identity chain, evaluation
order, envelopes, error taxonomy, and containment rules below are the
canonical target a future Integration Gateway must satisfy, and that any
future implementation deviating from them is non-conforming.

Acceptance does **not** mean any of: an implemented Gateway; a routed
request; an authenticated provider; a configured or verified credential; a
connected MCP server or integration fabric; a registered webhook; or a
deployment.

### 1.2 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Integration Gateway implementation | `NOT_IMPLEMENTED` — no gateway process, router, proxy, or enforcement code exists |
| Requests routed through it | **Zero.** No request has ever been evaluated or forwarded |
| Adapter implementations | `NOT_IMPLEMENTED`; scaffolding `BLOCKED` (Section 37) |
| Credentials | `NOT_CONFIGURED` — none exists in this repository or its environment |
| Provider authentication | `NEVER_PERFORMED` |
| Provider API execution | `NEVER_PERFORMED` |
| MCP / integration-fabric connection | `NOT_CONNECTED` |
| Webhook endpoints | `NOT_REGISTERED` — no inbound endpoint exists or is authorized |
| Evidence class for every flow below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by a documentation task.

## 2. Purpose

The Provider Registry contract established *what may be described* and the
eight facts that must hold before anything runs. It deliberately did not
say **who checks them, in what order, and what happens when one fails
mid-flight**. This contract answers exactly that.

Its purpose is to make an unauthorized external operation **structurally
impossible** rather than merely discouraged: every path from a MellyCore
caller to a downstream resource passes through one enforcement boundary
that independently re-derives every authorization input, trusts no claim
supplied by the caller or the provider, and fails closed on absence.

## 3. Authority and source contracts

| Source | Binding effect |
| --- | --- |
| `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` | Governing decision. Integration classes (§4), fabric selection (§5), tenant isolation (§10), identity model (§11), credential model (§12), risk tiers (§13), approval model (§14), audit/verification (§15), external-content posture (§16), implementation gate (§19). Reused; never relaxed. |
| `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` | The eight authorization facts (§21), scope hierarchy (§11), credential profiles (§13), capability records (§14), fabric chain (§23), MCP registration (§24), inheritance (§25). This contract **enforces** them; it does not restate them as new rules. |
| `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]` | First provider-specific contract; its error taxonomy (§28) is the base this contract extends (Section 25), and it is the conformance target of Section 34. |
| `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` | §3.1–§3.3 Control/Data Plane boundary and trust rule, §8 status taxonomy, §9.6 Integration Gateway display module, §16.1 approval binding, §17 secrets boundary, §18 provenance, §19 failure states. |
| `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` | `source_type`, `verification_state`, `trust_level`, `sensitivity_level`, `allowed_use`. Reused, never redefined. |
| `shared_context/SAFETY_CONTRACT.md` | No secrets, keys, tokens, `.env` values, or account IDs. |

### 3.1 Relationship to the Control Plane spec (no conflict)

`[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §3.1 assigns
integration "OAuth, connection, network communication, read/write
operations" to the **future Data Plane**, and §3.2 permits that Data Plane
to consume approved manifests "only after its own architecture, threat
model, implementation task, and validation gates are accepted."

**This contract is that anticipated architecture and threat model for the
integration path.** It does not modify, supersede, or reinterpret the
Control Plane spec. That spec's §9.6 "Integration Gateway" module remains
the **display projection** — a metadata-only catalogue with "no Connect,
OAuth, authorize, or credential-entry flow". This contract governs the
**enforcement boundary** beneath it. Both remain simultaneously true, in
the same layering the Registry contract established for `ProviderRecord`
versus the §7.2 `Provider`/`Integration` entities.

**Conflict rule.** Where this contract appears to conflict with the ADR,
the Registry contract, or an accepted provider contract, the conflict is a
defect here and must be corrected here. No material conflict was found
among the accepted documents while authoring this contract.

## 4. Scope

**In scope:** the Gateway trust boundary; identity model and acting-identity
chain; authentication/authorization separation; Registry resolution;
capability resolution; tenant and provider-native isolation; credential
custody and selection; delegated-user and service-account execution;
deterministic policy-evaluation order; approval binding; native adapter,
integration-fabric, and MCP boundaries; webhook and event ingestion;
request/response envelopes; error taxonomy; retry, idempotency,
concurrency; external-content security; audit and provenance; delivery
semantics; failure containment; the runtime enablement gate; provider
inheritance; Cloudflare conformance; and validation requirements.

**Out of scope:** any executable artifact — no Gateway implementation,
proxy, router, adapter, SDK, HTTP client, schema file, database, queue,
secret-store integration, or workflow. Envelope field listings are
**documentation fragments describing shape**, never runtime schemas.

## 5. Explicit non-authorizations

This contract does **not** authorize: Integration Gateway implementation;
adapter implementation or scaffolding; provider authentication; creation,
storage, rotation, reading, or verification of any credential; any provider
API call, **including read-only calls**; any MCP or integration-fabric
connection; webhook endpoint creation or registration with any provider;
any change to any external system; any dependency, lockfile, or workflow
change; deployment, push, pull request, merge, or tag; or any MellyTrade,
broker, trading, or order-execution behavior.

## 6. Trust model

### 6.1 The Gateway is a policy-enforcement boundary, not a proxy

**Normative.** The Gateway does not forward requests. It **re-derives** the
authorization decision from authoritative sources on every call, constructs
a new bounded provider request from validated inputs, and executes only
that. A caller's request is a **proposal describing intent**, never a
request to relay.

A design in which the Gateway passes through a caller-supplied URL, method,
body, header set, or tool invocation is non-conforming (Section 36).

### 6.2 Untrusted inputs (exhaustive for this contract)

The Gateway MUST NOT trust, and MUST independently verify or ignore:
caller-supplied tenant IDs; caller-supplied provider IDs; caller-supplied
capability IDs; caller-supplied scope or target claims; session keys;
conversation IDs; agent names; model names; runtime-supplied identity
assertions not cryptographically bound; integration-fabric claims about
identity, scope, or success; downstream provider responses; webhook
payloads; MCP tool names, descriptions, and schemas; external
documentation; and any provider-generated text.

**Every externally supplied value is a claim requiring independent
verification against an authoritative MellyCore record.**

### 6.3 Claim-to-fact resolution

A claim is only ever used to **look up** an authoritative record — never as
the value itself. A caller claiming `tenant_id: T` causes the Gateway to
resolve the caller's *authenticated* tenant and compare; a mismatch denies
(Section 25). The caller's claim never becomes the operative tenant.

### 6.4 Fail-closed axioms

1. Every mandatory field that is missing, `null`, `unknown`, unresolved,
   stale, expired, suspended, or conflicting **denies**.
2. No later evaluation step may compensate for a failed earlier step.
3. No error may be converted into an empty success, a narrower action, a
   different credential, or a lower-visibility notification (ADR §9;
   Cloudflare contract Rule 28.1).
4. Absence of evidence is never evidence of permission.

## 7. Gateway responsibilities

The Gateway is solely responsible for, and may not delegate:

1. Authenticating the caller and establishing the acting-identity chain.
2. Resolving tenant, provider, capability, scope, and credential profile
   from authoritative records.
3. Evaluating policy in the deterministic order of Section 17.
4. Verifying approval binding for R3–R5.
5. Selecting and applying credentials without exposing them.
6. Constructing the bounded provider request.
7. Enforcing idempotency and concurrency preconditions.
8. Normalizing responses and marking external content.
9. Performing or requiring read-after-write verification.
10. Writing audit evidence before reporting success.
11. Classifying failures and applying containment.

**Policy enforcement never delegates** to an integration fabric, an MCP
server, a provider, or an adapter. Their own controls are additive, never
substitutive (Registry §23.4).

## 8. Identity model

### 8.1 The twelve identities

| # | Identity | Authenticated? | Authorization subject? | Execution actor? | Credential owner? | Audit actor? |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Human operator | **Yes** | **Yes** | Only via approval | No | **Yes** |
| 2 | Enterprise tenant | Derived, not asserted | **Yes** (primary scope) | No | Owns profiles | **Yes** |
| 3 | Delegated end user | **Yes** (provider-side grant) | **Yes** | **Yes** | Subject of grant | **Yes** |
| 4 | Service account | **Yes** | **Yes** | **Yes** | **Yes** | **Yes**, explicitly labelled |
| 5 | MellyCore agent | **Yes** | Requester only | Requester only | **No** | **Yes** |
| 6 | Runtime / worker | **Yes** | No | Carrier only | **No** | **Yes** |
| 7 | Provider credential | Proves itself to provider | **No** | Means, not actor | — | Referenced only |
| 8 | Integration fabric | **Yes** (to MellyCore) | **No** | Transport only | Sometimes custodian | **Yes** |
| 9 | Downstream provider | Verified by MellyCore | **No** | Executor of record | No | **Yes** |
| 10 | Session / context | **No** | **No** | **No** | **No** | Correlation only |
| 11 | Approval authority | **Yes** | Grants fact 8 | No | No | **Yes** |
| 12 | Webhook source | **Yes** (signature) | **No** | **No** | No | **Yes** |

### 8.2 Normative identity rules

1. **Session, conversation, context, agent, and model identifiers are
   never authorization.** They are routing and correlation selectors
   (ADR §§9, 11). They never widen scope, never substitute for an approval
   ID, and never satisfy a precondition.
2. **An agent may request; it may never approve.** Identity 5 can never
   satisfy fact 8.
3. **A credential is a means, not an actor.** Identity 7 never appears as
   the acting identity in audit; the identity that *authorized* the use
   does.
4. **The fabric is transport, never subject.** Identity 8 is never
   recorded as the acting identity for a downstream operation
   (Section 20).
5. **Service-account actions are always labelled as such** and never
   presented as human- or user-performed (ADR §11).
6. **Identities may legitimately differ** across the chain — the operator
   who approved, the agent that requested, the worker that carried, and
   the delegated user under whose grant it ran can all be different. What
   may never happen is any of them being *lost, merged, or substituted*.

## 9. Acting-identity chain

### 9.1 The chain

```text
human_operator
  → tenant
    → requesting_agent
      → runtime_worker
        → gateway
          → credential_profile
            → integration_fabric        (when present)
              → delegated_user | service_account
                → downstream_provider
                  → target_resource
```

### 9.2 Field requirements

| Link | Requirement | Absence behavior |
| --- | --- | --- |
| `human_operator` | Required for R3–R5; optional for R0–R2 agent-initiated reads | Missing at R3–R5 → deny |
| `tenant` | **Always required** | Deny |
| `requesting_agent` | Required when the request did not originate directly from an operator | Deny |
| `runtime_worker` | Required whenever execution is not in-process with the requester | Deny |
| `gateway` | Always recorded (instance/version) | Deny |
| `credential_profile` | Always required for any provider call | Deny |
| `integration_fabric` | Required **when present**; `null` only for native paths | Ambiguity → deny |
| `delegated_user` \| `service_account` | Exactly one required; never both, never neither | Deny |
| `downstream_provider` | Always required; distinct from fabric | Deny |
| `target_resource` | Required; exact enumeration at R3–R5 | Deny |

### 9.3 Chain-validation rules

1. **Continuity.** Every link resolves to an authenticated or
   authoritative record. A break in continuity **denies**; it is never
   bridged by inference, defaulting, or "best guess".
2. **No substitution.** No link may be replaced by another. Most
   importantly, **an integration fabric must not replace downstream
   identity with its own** (Section 20.3).
3. **No collapsing.** The chain is recorded in full. Recording only the
   endpoints is non-conforming.
4. **Impersonation prevention.** A link is only assertable by the
   component that authenticated it. An agent cannot assert an operator; a
   runtime cannot assert a tenant; a fabric cannot assert a delegated user.
5. **Immutability in flight.** Once evaluation begins, the chain is
   frozen. A change requires a new request with a new decision.
6. **Audit representation.** The complete chain is recorded on every
   decision and every attempt, success or failure (Section 29).

## 10. Authentication and authorization separation

**Authentication** proves an identity or credential is what it claims.
**Authorization** determines whether that identity may perform a specific
capability against an exact target, now, under policy.

### 10.1 Explicitly rejected equivalences (each independently)

| Rejected claim | Why it is false |
| --- | --- |
| Valid credential ⇒ authorized operation | A credential proves possession, not permission. Facts 5–8 are separate |
| Successful OAuth ⇒ tenant authorization | OAuth proves a provider-side grant. MellyCore tenant authorization (fact 5) is a MellyCore record |
| Connected provider ⇒ runtime enabled | Reachability is health (Registry §19.2), not fact 7 |
| Session ownership ⇒ provider permission | Sessions are correlation only (Section 8.2 rule 1) |
| Provider account ownership ⇒ MellyCore tenant boundary | Registry §11.3; verified account-scoped-permission hazard |
| Adapter implemented ⇒ capability authorized | Fact 2 ≠ fact 6 |
| Approval exists ⇒ authorization | An approval without exact target binding authorizes nothing (Section 18; Control Plane §16.1) |
| Provider returned 200 ⇒ operation succeeded and verified | Section 30 separates six statuses |

### 10.2 Ordering

Authentication is a **precondition** of authorization, never a substitute.
The Gateway authenticates first (Section 17 steps 1–3) and authorizes
afterwards (steps 4–18). A component that authorizes on the strength of
authentication alone is non-conforming.

## 11. Provider Registry resolution

Before any external execution, the Gateway resolves all sixteen, from
authoritative records, never from the request:

1. `provider_id` — resolved from the authenticated context, compared
   against the caller's claim.
2. Provider `registration_status` — must be `conformance_verified`
   (fact 1).
3. `adapter_state` — must be `implemented` or `test_verified` (fact 2).
4. Provider-specific contract reference **and revision**.
5. Requested `capability_id` — must exist in that contract revision.
6. Capability `implementation_status`.
7. Capability `authorization_status` — the computed view (fact 6).
8. MellyCore tenant scope (fact 5).
9. Provider-native resource scope (Section 13).
10. Required `credential_profile` class.
11. External-content classification (Section 28).
12. Risk tier.
13. Approval policy.
14. Idempotency policy.
15. Verification policy.
16. Runtime enablement state for this environment (fact 7).

**Rule 11.1 — any unresolved, missing, stale, deprecated, suspended,
conflicting, or unverified mandatory record denies.** No partial
resolution proceeds. No default is substituted.

**Rule 11.2 — revision pinning.** The registry-record revision and the
provider-contract revision resolved at step 4 are pinned into the request
envelope (Section 23) and re-checked immediately before execution. A
revision change mid-flight **denies** (`CONTRACT_CONFLICT`).

## 12. Capability resolution

### 12.1 One capability, one bounded operation

A `capability_id` MUST resolve to **exactly one bounded provider
operation** with a fixed method class, a fixed resource type, and a
validated parameter shape.

A capability MUST NOT resolve to: arbitrary HTTP execution; arbitrary MCP
tool execution; arbitrary provider method calls; unrestricted
search-and-execute; dynamic mutation discovery; hidden fallback
operations; or undocumented provider actions.

### 12.2 Rules

| Concern | Rule |
| --- | --- |
| Aliases | An alias resolves to exactly one canonical capability. **An alias may never widen permissions, risk tier, or scope** — it inherits them unchanged, or it is invalid |
| Versions | Capabilities are versioned with their contract revision. A request names a capability; the Gateway pins the revision |
| Deprecated IDs | Resolve to a **denial** with `CAPABILITY_UNKNOWN`, not to a successor. Silent redirection is prohibited |
| Contract revisions | A capability from a superseded revision is not executable until re-resolved and re-authorized |
| Parameter validation | Validated against the contract's declared shape *before* credential selection. Unknown parameters are rejected, never forwarded |
| Target binding | The target resource set is resolved to exact IDs from authoritative reads; never from caller free text |
| Risk-tier inheritance | The **higher** of the generic and provider-specific tier governs (Section 33) |
| Provider restrictions | Provider-specific narrowing always applies |
| Ambiguity | Any ambiguity — two matches, no match, unclear revision — **denies**. The Gateway never guesses |

### 12.3 No capability selection from untrusted text

A capability is never selected, suggested-into, or inferred from provider
content, MCP tool descriptions, webhook payloads, or model output that has
ingested them (Section 28).

## 13. Tenant and resource isolation

### 13.1 Two independent boundaries

Both must hold:

1. **MellyCore tenant boundary** — the authoritative authorization scope.
2. **Provider-native resource boundary** — organization, account,
   subscription, workspace, project, repository, site, zone, property,
   campaign account, dataset, environment, region, resource ID.

### 13.2 Rules

1. **Caller scope claims are not trusted** — they are compared against
   resolved allowlists, never adopted.
2. **Targets resolve through Registry allowlists.** A resource absent from
   the allowlist is out of scope even if the credential reaches it.
3. **Wildcards fail closed** unless explicitly authorized and recorded;
   never at R3–R5 (Registry §11.2 rule 4).
4. **R3–R5 require exact target enumeration** — no pattern, index, name
   match, or implicit "all".
5. **Cross-tenant reuse is prohibited** for cache, context, session,
   queue, credential, idempotency key, and response.
6. **Provider account scope is not a tenant boundary** (Registry §11.3).
7. **Fabric-level tenancy does not replace downstream tenancy** — a
   fabric's own workspace/project model is additional, never substitutive.

### 13.3 Denial is uniform outward, precise inward

An out-of-scope target returns a **coarse** outward error
(`AUTHZ_DENIED_MELLYCORE`) while the audit record carries the precise
`denial_reason`. This prevents the Gateway becoming an existence oracle
for resources the caller may not know about, without losing audit
fidelity (Section 25.3).

## 14. Credential custody

### 14.1 Exposure prohibitions

Raw credential material MUST NEVER be exposed to: models; agents; frontend
clients; logs; audit payloads; error messages; tool arguments visible to
models; response envelopes; or integration-fabric metadata beyond the
minimum the fabric requires to act as custodian.

Credentials are handled exclusively through **opaque references**
(`secret_manager_ref`, Registry §13.1), resolved outside model-visible
context at the moment of use and never returned upward.

### 14.2 Selection inputs (all required)

Tenant; provider; capability class; acting identity type; environment;
provider-native scope; read/write class; and approval state where
applicable. Selection is **deterministic** — the same inputs select the
same profile, or deny.

### 14.3 Prohibited selection behaviors

| Prohibited | Consequence if attempted |
| --- | --- |
| Automatic credential widening | Deny; audited security event |
| Cross-tenant fallback | Deny; audited security event |
| Delegated-user → service-account fallback | Deny; audited security event |
| Read credential → write credential escalation | Deny; audited security event |
| Global API Key fallback | Deny (ADR §12, §17) |
| "Best available credential" selection | Deny — non-deterministic selection is prohibited by construction |
| Credential selection influenced by untrusted provider content | Deny; `INJECTION_SUSPECTED` |

**Rule 14.4.** A permission failure from the provider
(`AUTHZ_DENIED_PROVIDER`) is **terminal**. It is never retried with a
broader credential, a different profile, or a different identity.

## 15. Delegated-user execution

1. **Preserves the end-user identity** through the full chain and into
   audit.
2. **Uses only that user's granted scopes** — never the union of user and
   service-account scopes.
3. **Fails if the user's authorization is absent, expired, or revoked**
   (`DELEGATED_AUTHORIZATION_EXPIRED`).
4. **Never silently switches to a service account** — the single most
   important rule in this section (ADR §11).
5. **Records the delegated subject** as an identity reference, never as
   personal data beyond what the tenant's classification permits.
6. Eligible when the tenant policy permits delegated execution *and* the
   capability's `required_identity_type` includes delegated users.

## 16. Service-account execution

1. **Explicitly labelled** in every audit record and every operator-facing
   presentation. Never rendered as if a human or a specific end user acted.
2. **Requires tenant policy explicitly permitting service-account use** for
   that capability class.
3. **Uses a separately registered credential profile** — never a delegated
   user's.
4. **Records the service-account identity** distinctly.
5. **May carry stricter capability limits** than delegated execution, at
   tenant discretion; never looser.
6. Eligible only when the capability's `required_identity_type` includes
   service accounts.

**Rule 16.7 — exclusivity.** Exactly one of delegated-user or
service-account identity is present per request (Section 9.2). Both, or
neither, denies.

## 17. Policy-evaluation order (deterministic, ordered, fail-closed)

| # | Step | On failure |
| --- | --- | --- |
| 1 | Authenticate caller | `IDENTITY_UNRESOLVED` |
| 2 | Resolve tenant (authoritative, not claimed) | `AUTHZ_DENIED_MELLYCORE` |
| 3 | Validate requesting agent / runtime identity | `IDENTITY_UNRESOLVED` |
| 4 | Resolve provider record | `PROVIDER_UNREGISTERED` |
| 5 | Resolve provider-specific contract + revision | `CONTRACT_CONFLICT` |
| 6 | Resolve capability | `CAPABILITY_UNKNOWN` |
| 7 | Validate provider and adapter lifecycle states (facts 1–2) | `PROVIDER_SUSPENDED` / `ADAPTER_UNAVAILABLE` |
| 8 | Validate runtime enablement (fact 7) | `RUNTIME_NOT_ENABLED` |
| 9 | Validate tenant authorization (fact 5) | `AUTHZ_DENIED_MELLYCORE` |
| 10 | Validate capability authorization (fact 6) | `AUTHZ_DENIED_MELLYCORE` |
| 11 | Resolve target scope against allowlists | `AUTHZ_DENIED_MELLYCORE` |
| 12 | Validate data classification and `allowed_use` | `AUTHZ_DENIED_MELLYCORE` |
| 13 | Resolve acting identity type (delegated vs service) | `IDENTITY_UNRESOLVED` |
| 14 | Resolve credential profile (facts 3–4) | `CREDENTIAL_UNAVAILABLE` |
| 15 | Evaluate risk tier | `PRECONDITION_UNMET` |
| 16 | Resolve approval policy | `PRECONDITION_UNMET` |
| 17 | Validate approval where required (fact 8) | `APPROVAL_MISSING` / `APPROVAL_EXPIRED` |
| 18 | Bind approval to the exact request | `APPROVAL_STALE` |
| 19 | Validate idempotency, expected state, and concurrency | `IDEMPOTENCY_CONFLICT` / `STALE_STATE` |
| 20 | Construct bounded provider request | `PRECONDITION_UNMET` |
| 21 | Reserve durable, append-only execution intent for R3–R5 | `AUDIT_RESERVATION_FAILED` — no external mutation |
| 22 | Execute through the selected adapter class | Section 25 |
| 23 | Normalize response, mark external content | `SCHEMA_UNEXPECTED` |
| 24 | Read-after-write verification where required | `VERIFICATION_FAILED` |
| 25 | Append audit completion evidence | `AUDIT_COMPLETION_FAILED` — no success; reconcile and contain |
| 26 | Deliver result or failure per delivery policy | `DELIVERY_FAILED` (Section 30) |

**Rule 17.1 — no compensation.** No later step may compensate for, retry,
soften, or bypass a failed earlier step.

**Rule 17.2 — no reordering.** Credential resolution (14) occurs *after*
authorization (9–12), so an unauthorized request never causes a credential
to be resolved. Approval binding (18) occurs *after* approval validation
(17), and concurrency (19) *after* binding, so an approval can never be
bound to state it did not describe.

**Rule 17.3 — two-stage durable audit.** For R3–R5, step 21 durably
records and acknowledges the exact execution intent **before** step 22 may
issue an external mutation. Step 25 appends the observed execution and
verification outcome before step 26 delivery. A missing reservation
prevents execution; a failed completion append prevents success reporting
and enters reconciliation and containment. The audit store and provider
are not a distributed transaction, and this contract does not pretend
that atomic cross-system commit exists (Section 29).

## 18. Approval binding

### 18.1 Bound elements (all twelve)

Tenant; provider; capability (and contract revision); acting identity;
exact target resource set; before-state or state version; exact proposed
diff; risk tier; credential class; expiry; request fingerprint; policy
decision reference.

This extends the Control Plane §16.1 four-field binding (`target_type`,
`target_id`, `target_version`, `target_digest`) rather than replacing it;
those four remain the immutable core.

### 18.2 Rules

1. **Re-approval on any change.** Any bound element changing invalidates
   the approval. The Gateway does not adapt an approval to new facts.
2. **Recompute before execute.** The request fingerprint and state digest
   are recomputed immediately before step 21; mismatch → `APPROVAL_STALE`
   / `STALE_STATE`, abort.
3. **Single use, single target.** An approval authorizes one operation
   against one enumerated target set. No replay, no reuse across entities,
   IDs, or versions.
4. **No self-approval, no blanket, no inferred consent** (Control Plane
   §16.2).

### 18.3 Insufficient approval forms (each explicitly non-authorizing)

"Allow Cloudflare changes"; "allow this agent"; "allow marketing writes";
"approve this session"; "approve until revoked"; "approve this provider";
"approve this capability class"; a digest match without matching target
type, ID, and version (confused-deputy prevention, Control Plane §17).

### 18.4 R0–R2

For R0–R2 the approval policy resolves to `approval_state: not_required`.
That is a **resolved decision**, not an absent one; fact 8 is satisfied by
the resolution, and it is recorded. An *unresolvable* approval policy
denies (Section 17 step 16).

## 19. Native adapter contract

Native adapters are required for any provider holding R4/R5 capabilities
(ADR §4; Registry §9). Each MUST expose:

bounded capability methods (one per registered capability); typed request
envelopes; typed normalized response envelopes; provider request IDs;
exact scope metadata; declared idempotency behavior; declared concurrency
behavior; rate-limit metadata; retry classifications; read-after-write
methods for every mutation; and health and compatibility status.

**Rule 19.1 — no generic escape hatch.** A native adapter MUST NOT expose
an arbitrary-request, raw-passthrough, `execute_any`, or free-form-method
interface to autonomous agents. Where a low-level interface exists for
operator-run diagnostics, it is operator-only, non-autonomous, mutation-
prohibited, and separately audited.

**Rule 19.2 — the adapter does not decide.** Adapters execute what the
Gateway authorized. An adapter that performs its own capability
resolution, credential selection, or approval interpretation is
non-conforming.

## 20. Integration-fabric contract

### 20.1 Preserved chain

```text
MellyCore → fabric → downstream provider → downstream identity → target resource
```

Candidates named at architecture level (ADR §5): Composio, private
self-hosted n8n, Pipedream Connect, Tray.ai, Workato, restricted Zapier
MCP. **Naming a candidate authorizes nothing** — none is selected,
configured, credentialed, or connected.

### 20.2 Required declarations

Credential custodian; delegated identity; downstream provider identity;
downstream capability identity; policy-enforcement location;
approval-enforcement location; audit-source locations; data transit
regions; data retention; retry behavior; fallback behavior; provider
request ID preservation; loss-of-provenance handling.

### 20.3 The fabric must never obscure

The real downstream provider; the acting identity; the requested
capability; the target resource; the policy decision; the approval record;
or the provider's own request ID.

**Rule 20.4 — lost provenance prohibits R3–R5.** If downstream identity,
capability, scope, approval, or audit provenance cannot be preserved with
fidelity, `provenance_loss_risk` is `high` and the pair is **ineligible
for R3–R5 execution** (Registry §23.3).

**Rule 20.5 — fabric fallback is a new decision.** A fabric MUST NOT
switch provider, credential identity, tenant, capability, region, or
execution mode without a **fresh policy decision** and, where applicable,
**fresh approval**. A silent fabric-side failover is a contract violation,
not a resilience feature.

**Rule 20.6 — policy enforcement stays in MellyCore.** A fabric's own
governance is additive. MellyCore evaluates tenant, scope, risk, and
approval itself, and a fabric's assertion that it already did so carries no
weight (Section 6.2).

**Rule 20.7 — never the cybersecurity execution boundary.** Per ADR §5,
a fabric — Zapier MCP specifically named — must not become the primary
cybersecurity execution boundary.

## 21. MCP security contract

### 21.1 Separate registration

MCP servers register as a distinct record type (Registry §24.1), never as
ordinary providers, declaring: server identity; tool-set provenance;
static vs dynamic tools; tool-discovery trust level; credential binding;
tenant binding; allowed tools; denied tools; output trust level;
operator-only status; autonomous-agent eligibility; response-size limit;
timeout; audit mode.

### 21.2 Default rules (fail-closed)

1. **Unrestricted search-and-execute prohibited**, in any form.
2. **Generic arbitrary execution prohibited.**
3. **Dynamic tool discovery cannot authorize mutation** — a tool set that
   can change between sessions cannot be pre-approved.
4. **Tool descriptions are untrusted metadata** (Section 28) — never
   instructions, never capability selectors.
5. **MCP tools MUST map to registered MellyCore capability IDs.**
6. **Unregistered tools are not executable.**
7. **Discovered tools never become authorized automatically** — discovery
   is inventory, not permission.
8. **Provider-specific contracts may only narrow** these defaults.
9. **Cloudflare MCP remains documentation-only** under its current
   contract (`[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`
   §25.1).

### 21.3 Four phases

| Phase | Meaning | Advance requires |
| --- | --- | --- |
| 1 | Documentation-only | — (narrowest default) |
| 2 | Read-only investigation | Provider-contract amendment + explicit operator authorization |
| 3 | Proposal generation | As above, plus proposals derived from authorized reads, never from MCP output alone |
| 4 | Approval-gated execution | As above, plus every Section 17 step and full Section 18 binding |

**Rule 21.4.** No MCP server may advance a phase without a
provider-specific contract amendment **and** explicit operator
authorization. Phase advancement is never implicit, never inferred from
usage, and never granted by the MCP server itself.

**Rule 21.5 — MCP output is never evidence.** MCP results never satisfy a
precondition, back a proposal, or serve as verification. Evidence derives
only from authorized adapter reads (Cloudflare contract §25.3).

## 22. Webhook and event-ingestion contract

### 22.1 Inbound boundary

Covers webhooks, provider event streams, security alerts, marketing
events, CRM events, and integration-fabric callbacks.

### 22.2 Required controls (all mandatory)

Source authentication; signature or equivalent cryptographic verification
where the provider supports it (and explicit risk acceptance recorded
where it does not); replay protection; timestamp validation within a
bounded skew; event-ID deduplication; tenant resolution; provider
resolution; schema validation; size limits; content-type validation;
provenance preservation; quarantine for malformed or suspicious payloads;
untrusted-content treatment (Section 28); and **no direct execution from
inbound text**.

### 22.3 What inbound events may and may not do

**May create:** observations; alerts; draft proposals; queued review items.

**May NOT:** authorize a consequential provider action; select a
capability; select a credential; satisfy an approval; alter policy, scope,
or allowlists; or trigger a mutation directly or transitively.

**Rule 22.4 — the inbound/outbound asymmetry.** An inbound event can only
ever *raise work for a human or a policy-gated proposal path*. Every
outbound consequential action re-enters Section 17 from step 1 with its
own identity chain, approval, and audit. There is no path by which a
provider can cause MellyCore to act on that provider by sending it an
event.

**Rule 22.5 — unverifiable source quarantines.** An event failing source
authentication, signature, timestamp, or schema validation is quarantined
with provenance intact, audited, and never processed into the normal
pipeline.

## 23. Request envelope

Normalized fields (documentation shape, not a runtime schema):

`request_id`; `correlation_id`; `tenant_ref`; `operator_ref`; `agent_ref`;
`runtime_ref`; `gateway_ref`; `provider_id`; `downstream_provider_id`
(when a fabric is present); `integration_fabric_id` (or `null`);
`capability_id`; `capability_version`; `target_resource_set` (exact,
enumerated at R3–R5); `acting_identity_type` (`delegated_user` |
`service_account`); `acting_identity_ref`; `credential_profile_ref`
(**opaque**); `risk_tier`; `approval_ref`; `policy_decision_ref`;
`idempotency_key`; `expected_state_version` / `state_digest`;
`sanitized_parameters`; `timeout`; `delivery_policy`;
`provider_contract_revision`; `registry_record_revision`.

**Rule 23.1 — no raw credentials.** The envelope carries an opaque
profile reference only. No token, key, header, or derivable value appears.

**Rule 23.2 — sanitized parameters only.** Parameters are validated
against the capability's declared shape (Section 12.2) before entering the
envelope. Unknown fields are rejected, never carried.

## 24. Response envelope

`request_id`; `provider_request_id`; `fabric_request_id` (when present);
`execution_status`; `provider_status`; `normalized_result`;
`external_content_markers`; `pagination_cursor`; `completeness`;
`rate_limit_state`; `retry_classification`; `read_after_write_status`;
`delivery_status`; `sanitized_error`; `audit_ref`; `started_at`;
`completed_at`; `provenance_chain`.

**Rule 24.1 — transport success is not operation success.** A 2xx
provider response means the transport succeeded. It does **not** mean the
operation applied, applied completely, or was verified. `execution_status`,
`provider_status`, `read_after_write_status`, and `delivery_status` are
independent fields and are never collapsed (Section 30).

**Rule 24.2 — external content is marked, always.** Every field carrying
provider-authored text is marked untrusted with its provenance, so no
downstream consumer can lose that classification.

**Rule 24.3 — errors are sanitized outward, precise inward.** The
`sanitized_error` is the coarse class; the audit record carries the
precise reason (Section 25.3).

## 25. Error taxonomy

### 25.1 Reconciliation with existing terminology

The task-proposed error names were reviewed rather than adopted verbatim.
The accepted Cloudflare contract §28 already defines a canonical class set;
**those names are adopted unchanged as the base**, and Gateway-layer
classes are added only where the Cloudflare set has no equivalent.
Fragmenting an existing class into new near-synonyms was rejected.

| Proposed | Disposition |
| --- | --- |
| `tenant mismatch`, `capability unauthorized`, `target scope denied` | **Merged** into the existing `AUTHZ_DENIED_MELLYCORE`, refined by an internal `denial_reason` (Section 25.3). Separate outward classes would make the Gateway an existence oracle |
| `credential insufficient` | **Merged** into the existing `AUTHZ_DENIED_PROVIDER` |
| `approval missing`, `approval stale` | Mapped to existing `APPROVAL_MISSING` / `APPROVAL_EXPIRED`, plus `APPROVAL_STALE` for binding drift |
| `state changed after approval` | Existing `STALE_STATE` |
| `provider rate limited`, `provider unavailable`, `provider response invalid`, `verification failed` | Existing `RATE_LIMITED`, `PROVIDER_UNAVAILABLE`, `SCHEMA_UNEXPECTED`, `VERIFICATION_FAILED` |
| `API version unsupported` | Existing `CONTRACT_CONFLICT` domain; retained as a distinct class because compatibility failure is operationally distinct |
| `external content quarantined` | New `CONTENT_QUARANTINED`, complementing existing `INJECTION_SUSPECTED` |

### 25.2 Class table

| Class | Meaning | Retry? | Outcome |
| --- | --- | --- | --- |
| `IDENTITY_UNRESOLVED` | Caller, agent, runtime, or acting identity not established | No | Deny; audited |
| `AUTHZ_DENIED_MELLYCORE` | MellyCore tenant, scope, capability, classification, or allowlist denial | No | Deny; audited with precise `denial_reason` |
| `AUTHZ_DENIED_PROVIDER` | Provider rejected the credential's permission | No | **Never** retried with a broader credential |
| `PROVIDER_UNREGISTERED` | No conforming registry record (fact 1) | No | Deny |
| `PROVIDER_SUSPENDED` | Registration suspended or deprecated | No | Deny |
| `ADAPTER_UNAVAILABLE` | Fact 2 unmet or adapter unhealthy | No | Deny |
| `RUNTIME_NOT_ENABLED` | Fact 7 unmet for this environment | No | Deny |
| `CONTRACT_CONFLICT` | Contract/registry revision mismatch, drift, or unsupported API generation | No | Deny; contract-drift review |
| `CAPABILITY_UNKNOWN` | Unknown, deprecated, ambiguous, or unregistered capability | No | Deny; never redirected |
| `CREDENTIAL_UNAVAILABLE` | Facts 3–4 unmet | No | Deny; **never** widened |
| `DELEGATED_AUTHORIZATION_EXPIRED` | Delegated grant absent/expired/revoked | No | Deny; **never** falls back to service account |
| `APPROVAL_MISSING` / `APPROVAL_EXPIRED` / `APPROVAL_STALE` | Fact 8 unmet or binding drifted | No | Abort before any provider request |
| `STALE_STATE` | State digest or version precondition failed | No | Abort; new proposal + approval |
| `PRECONDITION_UNMET` | A required precondition absent | No | Abort |
| `IDEMPOTENCY_CONFLICT` | Key in flight or conflicting | No | Surface in-flight state |
| `RATE_LIMITED` | Provider throttling | Yes, bounded | Backoff, honor `Retry-After` |
| `PROVIDER_UNAVAILABLE` | Provider 5xx / transport failure | Reads yes; **mutations → `INDETERMINATE`** | Section 26 |
| `INDETERMINATE` | Mutation outcome unknown | **No blind retry** | Reconciliation (Section 26.3) |
| `PARTIAL_APPLICATION` | Some enumerated targets changed, others not | No | Report exact partial state; never claim success |
| `VERIFICATION_FAILED` | Read-after-write mismatch | No | Failure + containment assessment |
| `SCHEMA_UNEXPECTED` | Response shape not as contracted | No | Fail closed; never guess |
| `INJECTION_SUSPECTED` | Instruction-shaped untrusted content detected | n/a | Record, surface, continue treating as data |
| `CONTENT_QUARANTINED` | Inbound payload failed validation/authentication | n/a | Quarantine with provenance; never processed |
| `LEGACY_SURFACE_REFUSED` | An excluded legacy API family was requested | No | Refuse; audited security event |
| `AUDIT_RESERVATION_FAILED` | Durable execution intent could not be created or acknowledged before an R3–R5 attempt | No | **No external mutation executes** |
| `AUDIT_COMPLETION_FAILED` | The post-attempt completion append could not be durably recorded | **Never retry the provider mutation** | No success; reconcile, contain, and retry only the audit append through the durable outbox |
| `AUDIT_UNAVAILABLE_FOR_READ` | Required audit evidence for a read operation cannot be durably recorded | No | Classify according to risk and policy; never silently report a successful read |
| `AUDIT_RECORD_INDETERMINATE` | Audit durability or record state cannot be established | **Never retry the provider mutation** | Operator review and audit/provider-state reconciliation are required |
| `DELIVERY_FAILED` | Result could not be delivered | No | Remains visible and auditable (Section 30) |

### 25.3 Outward coarse, inward precise

Outward classes are deliberately coarse to avoid leaking existence,
scope, or configuration to an unauthorized caller. The audit record
carries the precise `denial_reason`, the exact failing evaluation step,
and the resolved facts. **This asymmetry is required, not optional.**

### 25.4 No silent degradation

No class may be converted into an empty success, a narrower action, a
different credential, a different provider, or a lower-visibility
notification (ADR §9; Cloudflare Rule 28.1).

## 26. Retry and idempotency behavior

### 26.1 Reads

Retry only on `RATE_LIMITED` and `PROVIDER_UNAVAILABLE`, with exponential
backoff, jitter, a bounded attempt count, a retry budget per
`(tenant, credential_profile)`, and `Retry-After` honored. Never retry
authorization or approval failures.

### 26.2 Mutations

1. **Never blindly retried.**
2. A `RATE_LIMITED` response received **before** the request was
   transmitted may be retried under the same idempotency key with
   unchanged preconditions.
3. Any timeout or ambiguous response yields `INDETERMINATE`.
4. Provider-native idempotency is used where offered; where it is not,
   Gateway-side keys plus concurrency preconditions (Section 27) are the
   authoritative mechanism.

### 26.3 Indeterminate reconciliation (mandatory)

On `INDETERMINATE`: perform a **fresh authoritative read** → compare
against the approved after-state → if applied, record success **with
verification evidence**; if not applied, a **new proposal and new
approval** are required; if partially applied, report
`PARTIAL_APPLICATION` with the exact partial state. **Blind retry is
prohibited** — it risks a duplicate write with a different outcome.

### 26.4 Idempotency keys

Derived from tenant, provider, capability, enumerated targets, approval
reference, and before-state digest. Stable across retries of the same
intended action; different for any different intended action. A replayed
key with a recorded terminal outcome returns that outcome without
re-execution. A key whose attempt is in flight blocks and surfaces
`IDEMPOTENCY_CONFLICT`. Keys are never shared across tenants.

## 27. Concurrency and stale-state behavior

Before every R3–R5 operation: a fresh authoritative read within the
capability's freshness window; an expected version or equivalent
precondition; a target fingerprint; an approval-state fingerprint; and
stale-state rejection.

**Rule 27.1 — state change after approval.** If state changed after
approval: **do not execute**; invalidate the approval; generate a new
diff; require re-approval. The Gateway never reconciles silently or
force-applies.

**Rule 27.2 — serialization.** Concurrent MellyCore mutations against the
same target resource are serialized per resource. A lost race is not
worked around by forcing.

**Rule 27.3 — control-plane confirmation only.** Verification confirms
provider control-plane state. It does not prove downstream/edge
enforcement, and must never be reported as such.

## 28. External-content security

All downstream and inbound content is untrusted: logs; alerts; incident
descriptions; CRM notes; campaign names; API schemas; endpoint labels;
issue bodies; HTML; files; webhook payloads; **MCP tool descriptions**;
and provider error messages.

Required controls: content/data separation; provenance tags; sanitization
(control characters, homoglyphs, bidirectional overrides, nested
delimiters); normalization; schema validation; size limits; explicit
truncation indicators; **no policy elevation**; **no instruction
execution**; **no capability selection from untrusted text**; **no
credential selection from untrusted text**; and quarantine for suspicious
payloads.

**Rule 28.1 — the confused-deputy rule.** Untrusted content may never
cause the Gateway to act with authority the content's author does not
have. Text claiming operator authority, prior approval, or system origin
is data.

**Rule 28.2 — no transitive laundering.** Content that passes through a
model, a summarizer, a fabric, or an MCP server does not become trusted.
Trust is a property of origin and verification, never of transformation.

## 29. Audit and provenance

### 29.1 Two-stage durable audit model

Every decision and attempt uses append-only evidence. R3–R5 mutation
flows require two distinct stages: a **Stage A execution-intent
reservation** before external execution, then a **Stage B completion
append** after the attempt and required verification. The Stage A record
is preserved even when execution, verification, completion recording, or
delivery fails. There is deliberately **no distributed transaction**
across the audit store and an external provider or fabric; the two-stage
protocol makes that non-atomic boundary observable and recoverable rather
than claiming impossible cross-system atomicity. The Gateway cannot
atomically transact across its audit store and an arbitrary external
provider. Durable intent prevents unaudited mutation initiation;
post-execution failures require reconciliation rather than pretending the
mutation never occurred.

### 29.2 Stage A — durable execution-intent reservation

Before an R3–R5 external mutation, the Gateway confirms audit-subsystem
availability, creates an append-only intent, and obtains a durable
acknowledgement. The intent contains: audit event ID; request ID; tenant;
provider; capability; complete acting-identity chain; opaque credential-
profile reference; exact enumerated targets; risk tier; policy decision;
approval ID; request fingerprint; before-state fingerprint; proposed-diff
fingerprint; idempotency key; registry revision; provider-contract revision;
selected execution path (native or named fabric); and reservation
timestamp. Raw secrets remain prohibited. Failure returns
`AUDIT_RESERVATION_FAILED`; **no provider or fabric mutation request is
issued**.

### 29.3 Stage B — durable completion append

After the attempt and read-after-write verification, the Gateway appends:
execution start and finish times; provider and fabric request IDs when
applicable; response classification; normalized outcome, including
`INDETERMINATE` where appropriate; verification result; rollback or
containment state; delivery state; completion or failure classification;
and completion timestamp. The append references the immutable Stage A
audit event ID and never replaces or deletes the intent.

### 29.4 Denials and request-ID absence semantics

A denied request produces a durable audit record. Denials are the highest-
value security signal and are never dropped as "no-ops". The denial reason
and exact failed evaluation stage are recorded. For denials
before any provider or fabric attempt, provider/fabric request IDs are
absent or `not_applicable`. For an external attempt, the returned IDs are
recorded. If no ID can be obtained, the record uses exactly one truthful
status: `not_returned`, `not_supported`, or `unknown_after_timeout`.
Implementations never invent, synthesize, or backfill a provider/fabric
request ID as though it had been returned.

### 29.5 Prohibited in audit

Raw credentials, tokens, `Authorization` headers, secret-shaped values,
and unnecessarily sensitive payload bodies. Provider account and resource
identifiers are stored as references resolvable within the tenant
boundary.

### 29.6 Audit failure and recovery semantics

If Stage A cannot be durably acknowledged, **R3–R5 operations do not
execute** (`AUDIT_RESERVATION_FAILED`). If Stage B cannot be durably
appended, the mutation may already have happened: the Gateway returns no
success, never blindly re-executes the provider mutation, marks the state
`AUDIT_COMPLETION_FAILED` or `AUDIT_RECORD_INDETERMINATE` as applicable,
starts provider-state reconciliation and containment, and places the
completion append in a durable outbox for bounded audit-store retry. An
read operation whose required audit evidence cannot be durably recorded is
classified `AUDIT_UNAVAILABLE_FOR_READ` according to its risk and policy
and is never silently reported as a successful read. An
`AUDIT_RECORD_INDETERMINATE` requires operator review and reconciliation.
Audit availability and durability are preconditions, not best-effort side
effects.

## 30. Delivery semantics

Six independent statuses, never collapsed into one `success`:

| # | Status | Meaning |
| --- | --- | --- |
| 1 | Operation executed | The Gateway issued the bounded request |
| 2 | Provider acknowledged | The provider returned a terminal response |
| 3 | Result verified | Read-after-write confirmed the expected state |
| 4 | Audit lifecycle recorded | Stage A intent reserved where required and Stage B completion durably appended; otherwise this status is false and the explicit audit-failure/outbox state is surfaced separately |
| 5 | External notification delivered | Any required outbound notification reached its channel |
| 6 | Operator received result | The human-facing surface confirmed receipt |

**Rule 30.1 — no collapsing.** A response asserting `success` without
distinguishing these six is non-conforming.

**Rule 30.2 — critical alerts never degrade silently.** A failed critical
security notification must surface as a failure. It must not fall back to
an internal-only success state or a lower-visibility channel (ADR §9).

**Rule 30.3 — delivery failure stays visible.** `DELIVERY_FAILED` remains
visible and auditable, and does not retroactively invalidate statuses 1–4,
which are recorded truthfully as they occurred. A completion-audit failure
is never hidden by successful external delivery and never permits a
provider mutation retry.

## 31. Failure containment

| Trigger | Containment (specification level) |
| --- | --- |
| Suspected credential compromise | Suspend credential profile; invalidate bound approvals; deny; preserve evidence |
| Tenant-boundary violation | Deny; audited security event; operator review |
| Provider-contract drift | `CONTRACT_CONFLICT`; deny affected capabilities; reverse `conformance_verified` |
| MCP tool-set drift | Deny affected tools; re-verification required before reuse |
| Lost provenance through a fabric | Prohibit R3–R5 for that pair (Rule 20.4) |
| Audit reservation outage | Block R3–R5 before external execution |
| Audit completion outage after an attempt | No success; no provider retry; reconcile and contain; retry only the completion append through the durable outbox |
| Read-after-write failure | Failure + containment assessment; no retry into a pass |
| Repeated ambiguous mutations | Enter read-only mode for the capability; require operator review |
| Provider documentation inconsistency | Require dated re-verification before further use |
| Unsupported API generation | Deny; **no legacy fallback** |

Available containment actions: suspend provider record; suspend credential
profile; disable adapter runtime; deny capability; quarantine inbound
events; require operator review; enter read-only mode; stop all mutations;
preserve evidence.

**Rule 31.1 — containment is itself governed.** A containment action that
mutates provider state is itself a mutation requiring approval (expedited
where tenant policy defines it), idempotency, verification, and audit.

**Rule 31.2 — no runtime authorization here.** No containment action is
authorized for runtime by this contract.

**Rule 31.3 — containment leaves a tracked follow-up.** Reducing
enforcement is a posture regression; every containment opens a tracked
item to restore intended protection through a new proposal and approval.

## 32. Runtime enablement gate

Before any provider execution may be enabled, **all seventeen** must be
evidenced:

1. Provider contract exists. 2. Registry record exists. 3. Adapter
implementation exists. 4. Adapter version is compatible. 5. Credential
profile is configured. 6. Credential is verified. 7. Tenant is authorized.
8. Capability is authorized. 9. Runtime is explicitly enabled.
10. Required policy exists. 11. Approval system is available where
required. 12. Audit system is available. 13. Verification method exists
for mutations. 14. External-content controls exist. 15. Provider-specific
validators pass. 16. Security review passes. 17. Explicit operator
authorization is recorded.

**Rule 32.1 — this contract asserts none of these currently pass**, for
any provider, including Cloudflare. Consistent with
`[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` §1.5, a validator that
did not run records `NOT_RUN`, never a defaulted pass.

## 33. Provider-specific inheritance

1. This contract is a **mandatory floor**.
2. Provider-specific contracts may add **stricter** requirements.
3. They may **not weaken** any requirement here. A weaker rule is void.
4. Conflicts **fail closed**; the stricter interpretation governs while
   unresolved, and affected capabilities are denied.
5. Weakening requires an explicit operator-approved ADR amendment.
6. Where generic and provider-specific risk tiers differ, the **higher**
   governs.

Precedence:

```text
SAFETY_CONTRACT.md > Enterprise-Provider ADR > Provider Registry contract
                   > this Gateway contract > provider-specific contract (stricter only)
                   > tenant policy (stricter only)
```

## 34. Cloudflare conformance example

Six representative flows. The Cloudflare contract's full capability tables
are **not** duplicated (Registry §14.3). Common to every flow: tenant
always required; provider-native scope `account` + `zone`; caller claims
untrusted; R3–R5 audit intent durably reserved before execution and
completion appended after verification; and read-only Cloudflare API
access **still unauthorized** because facts 5–7 are unsatisfied and
`adapter_state` is `blocked`.

### 34.1 Read-only API operations inventory (`cloudflare.endpoint_management.operations.list`, R1)

| Aspect | Enforcement |
| --- | --- |
| Identity chain | operator *or* agent → tenant → agent → worker → gateway → `CF_READ` → service account → cloudflare → zone |
| Registry facts | 1–7 required; fact 8 resolves `not_required` (Section 18.4) |
| Credential class | `CF_READ` — a write profile is **prohibited** here (Rule 17.2 ordering; Section 14.3) |
| Target scope | Zone must be on the tenant allowlist; account scope not inferred |
| Risk tier | R1 |
| Approval | Not required, but **resolved and recorded** |
| Execution path | Native adapter, bounded `GET` |
| Audit | Full Section 29.1 record including the denial-free decision |
| Verification | N/A (no write) |
| Fail-closed | Truncated pagination marks `completeness: truncated`; a truncated read may not back a deletion or replacement proposal |

### 34.2 Proposal-only WAF rule change (`cloudflare.waf.rules.update.propose`, R2)

| Aspect | Enforcement |
| --- | --- |
| Identity chain | As above; **`CF_READ` only** |
| Registry facts | 1–7; fact 8 `not_required` for producing a proposal |
| Credential class | `CF_READ`. A D2 capability issued a write credential is non-conforming |
| Target scope | Exact ruleset and rule IDs from a fresh read |
| Risk tier | R2 — **generates a diff and stops** |
| Approval | The proposal **confers none**; it names the R4/R5 mutation it would target |
| Execution path | No write request is ever issued |
| Audit | Proposal ID bound to before-state digest |
| Verification | N/A |
| Fail-closed | Incomplete inputs → `INCOMPLETE` proposal naming what is missing; never inferred |

### 34.3 Approval-gated endpoint-specific Schema Validation `block` (`cloudflare.schema_validation.operation.set_block`, R4→R5)

| Aspect | Enforcement |
| --- | --- |
| Identity chain | **operator required** → tenant → agent → worker → gateway → `CF_WRITE_CONTROLLED` → service account → cloudflare → exact operation |
| Registry facts | All eight; fact 8 digest-bound |
| Credential class | `CF_WRITE_CONTROLLED`; read/write separation enforced |
| Target scope | Exact `operation_id`; no pattern matching |
| Risk tier | R4, **escalating to R5** when the endpoint is tenant-critical or observation evidence is absent |
| Approval | Twelve-element binding (Section 18.1); approval view shows the full rollout evidence |
| Execution path | Native adapter only; **the 17-stage rollout must already have reached stage 12**, and the emergency `none` containment path must be proven reachable *before* this executes |
| Audit | Full record + R5 enhancements where escalated |
| Verification | **Mandatory** read-after-write; mismatch → `VERIFICATION_FAILED` + containment |
| Fail-closed | Missing observation evidence → prohibited (`block_without_observation`); state drift → `STALE_STATE`, approval invalidated |

### 34.4 Zone-wide `block` (`cloudflare.schema_validation.zone_default.set_block`, R5 always)

| Aspect | Enforcement |
| --- | --- |
| Identity chain | Operator required; agent may never self-approve |
| Registry facts | All eight |
| Credential class | `CF_WRITE_CONTROLLED` |
| Target scope | Exact zone, enumerated; **wildcard prohibited** |
| Risk tier | **R5, always — never downgraded** |
| Approval | R5 binding: strict preconditions, exact resource enumeration, enhanced audit |
| Execution path | Native adapter; unreachable without the full staged rollout |
| Audit | R5 enhancements: enumerated targets shown to approver, approver identity, preconditions evaluated, stored rollback representation, verified containment path |
| Verification | Mandatory; control-plane only — **never** reported as edge enforcement |
| Fail-closed | `zone_wide_block.unapproved` is a prohibited capability → `LEGACY_SURFACE_REFUSED`-class refusal, audited as a security event |

### 34.5 Endpoint deletion with dependency analysis (`cloudflare.endpoint_management.operations.delete`, R5)

| Aspect | Enforcement |
| --- | --- |
| Identity chain | Operator required |
| Registry facts | All eight |
| Credential class | `CF_WRITE_CONTROLLED` |
| Target scope | Exact `operation_id` plus confirmed method/hostname/path triple |
| Risk tier | **R5 — irreversible**; historical metrics cannot be restored |
| Approval | Approval view must show the dependency lookup, the affected-feature list, and the irreversibility |
| Execution path | Native adapter; **absent traffic evidence blocks deletion** — unknown is never read as zero |
| Audit | Enumerated targets; stored rollback representation noting what cannot be restored |
| Verification | Mandatory: exactly the enumerated operations removed, and no others |
| Fail-closed | Bulk/unenumerated deletion is a prohibited capability; any dependency unresolved → deny |

### 34.6 Documentation-only Cloudflare MCP (`cloudflare.mcp.documentation_session`, R0)

| Aspect | Enforcement |
| --- | --- |
| Identity chain | **Operator-initiated only**; no agent initiation, no background use |
| Registry facts | MCP record; **no Cloudflare account grant in v1.0** |
| Credential class | `CF_MCP_OPERATOR` — carries no account reach |
| Target scope | Documentation only; no account, zone, or resource |
| Risk tier | R0 |
| Approval | Operator initiation is the authorization; the session confers no capability |
| Execution path | Phase 1 only (Section 21.3). `cloudflare.mcp.code_mode_execute` is **prohibited** — 2,500+ endpoints behind one grant is unrestricted execute by construction |
| Audit | Full session transcript metadata (Section 29) |
| Verification | N/A |
| Fail-closed | MCP output is **never evidence** (Rule 21.5); any mutation attempt refused and audited |

### 34.7 Result

**The Cloudflare contract is enforceable through this Gateway contract
with no weakening detected.** No Cloudflare requirement needed relaxation,
and every Cloudflare-specific restriction is either enforced by a generic
Gateway rule or preserved by Section 33's stricter-only inheritance.

## 35. Testing and validation requirements

A future implementation must demonstrate, **without any live provider
call**, that:

1. Each Section 17 step denies independently when its input is absent.
2. Step order is enforced — no credential resolves before authorization
   passes.
3. Caller-supplied tenant, provider, capability, and scope claims cannot
   override resolved values.
4. Session, conversation, and agent IDs cannot authorize anything.
5. Delegated-user failure never falls back to a service account.
6. Read credentials cannot execute mutations, and vice versa.
7. Approval binding rejects every element-drift case in Section 18.1.
8. Approval replay, cross-entity reuse, and digest-only matches are
   refused.
9. Stale state aborts and invalidates the approval.
10. `INDETERMINATE` never blind-retries and always reconciles.
11. Read-after-write cannot be disabled.
12. Audit reservation failure blocks R3–R5 before execution; completion
    failure after an attempt blocks success, never retries the mutation,
    and drives reconciliation, containment, and durable-outbox recovery.
13. A fabric cannot substitute downstream identity, and lost provenance
    blocks R3–R5.
14. MCP discovery does not authorize; unregistered tools are not
    executable; dynamic discovery cannot mutate.
15. Webhook payloads cannot trigger a consequential action by any path.
16. Instruction-shaped untrusted content is treated as data and flagged.
17. Prohibited capabilities are refused and audited as security events.
18. Outward errors are coarse while audit reasons are precise.
19. No fixture, log, or report asserts that the Gateway or any provider is
    connected, authenticated, enabled, or deployed.

All tests use local fixtures. **No test may authenticate to a provider,
call a provider API, connect an MCP server or fabric, or register a
webhook.** A test that did not run records `NOT_RUN`, never a defaulted
pass.

## 36. Rejected designs

| Rejected | Why |
| --- | --- |
| Gateway as a passive proxy / request forwarder | Section 6.1 — the Gateway re-derives and reconstructs; it never relays |
| Caller-supplied URL, method, body, or header passthrough | Same; an escape hatch defeats every other control |
| Trusting caller-asserted tenant, provider, capability, or scope | Section 6.2–6.3 |
| Authentication as authorization | Section 10.1 |
| Session/conversation/agent ID as authorization | Section 8.2 rule 1 |
| One `success` status | Section 30 — six independent statuses |
| Provider 2xx as proof of operation and verification | Rule 24.1 |
| Credential resolution before authorization | Rule 17.2 — would resolve secrets for unauthorized requests |
| "Best available credential" selection | Section 14.3 — non-deterministic selection is prohibited |
| Any credential widening, cross-tenant, or read→write escalation fallback | Section 14.3 |
| Delegated-user → service-account fallback | Section 15 rule 4; ADR §11 |
| Fabric asserting identity, scope, or prior policy evaluation | Rules 20.3, 20.6 |
| Silent fabric failover across provider/credential/tenant/region | Rule 20.5 |
| Fabric as the cybersecurity execution boundary | Rule 20.7; ADR §5 |
| MCP discovery granting execution | Section 21.2 rules 6–7 |
| Unregistered MCP tools being executable | Section 21.2 rule 5 |
| Dynamic MCP discovery authorizing mutation | Section 21.2 rule 3 |
| MCP output as evidence or proposal basis | Rule 21.5 |
| Inbound webhooks triggering consequential actions | Rule 22.4 |
| Blind mutation retry after timeout | Section 26.2–26.3 |
| Reconciling drifted state silently instead of re-approving | Rule 27.1 |
| Optional or post-hoc-only audit, or optional read-after-write | Sections 29.1–29.6 and 35 item 11–12; the Registry and Cloudflare contracts both forbid it |
| Fine-grained outward error classes | Section 25.3 — would create an existence oracle |
| Trust conferred by transformation (model/fabric/MCP passthrough) | Rule 28.2 |
| Provider-specific contracts relaxing this contract | Section 33 rule 3 |

## 37. Implementation prerequisites

Gateway implementation may not begin until **all** hold:

1. This contract is accepted and — like the ADR, Cloudflare, and Registry
   contracts — reviewed, published, and merged through normal gates.
2. `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` passes.
3. `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` passes.
4. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001` passes.
5. `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` receives its own **separate,
   explicit operator authorization**, independent of Model A/B deployment
   authorization and of the OpenAI Batch Stage C gate. It remains
   **blocked** until then.
6. A secrets boundary exists that resolves opaque references outside
   model-visible context.
7. An approval broker exists enforcing the Section 18.1 twelve-element
   binding atop the Control Plane §16.1 four-field core.
8. An audit subsystem exists that satisfies Section 29, including durable
   Stage A reservation, append-only Stage B completion, readable evidence,
   and a durable completion outbox; it blocks or contains on each named
   failure mode.
9. A tenant-provider and tenant-capability authorization store exists
   (facts 5–6) — the item the Registry contract deferred here
   (Section 38.1).

Until item 5 is satisfied, **read-only provider API access also remains
unauthorized**, consistent with `shared_context/RUN_QUEUE.md`.

## 38. Open questions

### 38.1 Items inherited from the Provider Registry contract

- **Where tenant-provider and tenant-capability authorization records
  live** (facts 5–6). This contract fixes that they must be **explicit,
  separate, independently revocable records** resolved at Section 17 steps
  9–10, and that their absence denies. Their storage, issuance workflow,
  and revocation propagation remain unspecified and are carried forward to
  the provider-pack specs and the adapter-scaffold authorization.
- **How a fabric demonstrates approval/audit equivalence to a native
  adapter** (Rule 20.4). This contract fixes the *consequence* of failure
  (R3–R5 prohibited) but not the positive evidence standard. Unresolved.

### 38.2 New to this contract

- **Cryptographic binding of the acting-identity chain.** Section 9.3
  requires continuity and forbids impersonation, but the mechanism
  (signed assertions, mTLS, token exchange) is deliberately unspecified.
- **Credential verification without a broad probe** (fact 4) — how to
  prove a credential usable without exercising a consequential capability.
- **Bounded skew and replay-window values** for webhook timestamp
  validation — shape fixed, numbers tenant-policy.
- **Whether operator-only low-level adapter diagnostics (Rule 19.1) should
  exist at all** in v1.0, or be deferred entirely.
- **Multi-target partial-application semantics** — Section 25 defines
  `PARTIAL_APPLICATION`, but whether multi-target R5 operations should be
  permitted at all, versus decomposed into single-target operations, is
  unresolved.

## 39. Amendment and supersession

This contract may be amended or superseded only by a later, explicitly
identified document that references this file **by path** and states which
section(s) it changes — the pattern established by
`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`. A later document
that silently contradicts this contract does **not** supersede it; such a
contradiction must be corrected, not treated as an implicit amendment.

Specifically requiring an amendment: weakening any fail-closed default;
reordering Section 17; reducing the Section 18.1 binding; permitting
generic/arbitrary execution on any path; permitting MCP phase advancement
without operator authorization; permitting inbound events to authorize
actions; making audit or verification optional; permitting any fallback
prohibited in Section 14.3; or allowing a provider-specific contract to
relax a rule here.

Amending this contract never amends the ADR or the Registry contract;
where they diverge, the higher precedence in Section 33 prevails.

## 40. References

### 40.1 Repository (canonical)

- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]`
- `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` — §3.1–§3.3
  Control/Data Plane boundary and trust rule, §8 status taxonomy, §9.6
  Integration Gateway display module, §16.1 approval binding, §16.2 hard
  prohibitions, §17 secrets boundary, §18 provenance, §19 failure states,
  §25 integration seams.
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` — §1.5 truthfulness.
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`.
- `docs/tasks/MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001.md`.

### 40.2 External

None. This contract governs MellyCore's own enforcement boundary; every
provider-specific technical claim it relies on is carried by reference
from the already-verified Cloudflare contract rather than re-asserted
here. No external documentation was fetched, and no provider was
contacted, during its authoring.
