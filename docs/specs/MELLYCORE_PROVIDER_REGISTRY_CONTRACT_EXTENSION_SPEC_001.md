# MellyCore Provider Registry Contract Extension Spec

**Task ID:** MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001
**Contract ID:** MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_001
**Version:** 1.0
**Status:** ACCEPTED as a specification-level registry contract only. **This status does not authorize runtime implementation, registry implementation, adapter scaffolding, provider authentication, credential creation or access, any provider API call, any MCP connection, any integration-fabric connection, or deployment.** It fixes the record structure, lifecycle, and validation rules that a later, separately authorized implementation must satisfy.
**Scope:** Extends the Provider Registry concept defined in `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` (§7.2 entity catalogue, §9.1 Provider Registry and Model Gateway) from AI model providers to enterprise, cybersecurity, marketing, integration-fabric, and restricted-MCP providers, so every future provider is describable through one stable, safety-first, fail-closed contract.

---

## 1. Title and status

### 1.1 Status meaning (normative)

This document is an **accepted specification-level contract**, in the same
sense as `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`
and `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`.

Acceptance means, and means only, that the record structure, lifecycle
model, authorization separation, and validation rules below are the
canonical target a future provider registry must satisfy, and that any
future provider registration deviating from them is non-conforming.

Acceptance does **not** mean any of the following, none of which exist:
an implemented registry; a registered provider; a configured or verified
credential; an authenticated provider; an implemented adapter; an executed
provider call; a connected MCP server or integration fabric; or a
deployment.

### 1.2 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Registry implementation | `NOT_IMPLEMENTED` — no runtime registry, database, schema file, or model class exists |
| Registered providers | **Zero.** No provider record exists in any executable form |
| Adapter implementations | `NOT_IMPLEMENTED`; scaffolding `BLOCKED` (Section 29) |
| Credentials | `NOT_CONFIGURED` — none exists in this repository or its environment |
| Provider authentication | `NEVER_PERFORMED` |
| Provider API execution | `NEVER_PERFORMED` |
| MCP / integration-fabric connection | `NOT_CONNECTED` |
| Evidence class for every record shape below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by a documentation task.

## 2. Purpose

MellyCore needs one registry contract that can describe a Cloudflare WAF
mutation, a HubSpot campaign read, a Composio-brokered delegated OAuth
call, and a restricted MCP documentation session **in the same structure**,
without any of the following becoming true by side effect: that a provider
is connected, that a credential exists, that a capability may run, or that
a tenant is authorized.

The registry exists to make provider governance *addressable by policy*.
It is deliberately **not** an execution surface, **not** a credential
store, and **not** a permission grant.

## 3. Authority and source contracts

| Source | Binding effect |
| --- | --- |
| `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` | Governing architecture decision. Provider integration classes (§4), tenant isolation (§10), identity model (§11), credential model (§12), capability/risk tiers (§13), approval model (§14), audit/verification (§15), external-content posture (§16), implementation gate (§19). Reused verbatim; never relaxed. |
| `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]` | The first provider-specific contract. This registry MUST be able to represent it without weakening it (Section 26). |
| `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` | The existing Provider Registry concept this document extends: §7.1 common entity contract, §7.2 `Provider`/`Integration` entities, §8 six-dimension status taxonomy, §16 approval contract, §17 secrets boundary, §18 provenance, §19 failure states. |
| `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` | Canonical `source_type`, `verification_state`, `trust_level`, `sensitivity_level`, and `allowed_use` vocabularies. Reused, never redefined (Section 16). |
| `shared_context/SAFETY_CONTRACT.md` | No secrets, no real keys, no provider tokens, no `.env` values, no account IDs. |

**Conflict rule.** Where this document appears to conflict with the ADR or
with an accepted provider-specific contract, the conflict is a defect in
this document and must be corrected here. A silent contradiction amends
nothing. No architectural conflict was found while authoring this contract;
one **terminology reconciliation** was required and is recorded in
Section 7.4.

## 4. Scope

**In scope:** the normalized provider record; provider identity and
categories; integration classes; the registration lifecycle state machine;
the scope hierarchy; authentication modes; credential-profile *metadata*;
capability records; risk and approval metadata; data classification;
external-content posture; API/connector compatibility; health metadata;
registry audit and provenance; the separation between registration and
runtime authorization; the integration-fabric chain; MCP registration;
suspension/deprecation/retirement; provider-specific contract inheritance;
Cloudflare conformance; and validation rules.

**Out of scope:** any executable artifact. No JSON Schema, TypeScript,
Python, SQL, ORM model, migration, API, storage engine, secret-store
integration, adapter, or workflow. Illustrative field listings below are
**documentation fragments describing shape**, never runtime schemas.

## 5. Explicit non-authorizations

This contract does **not** authorize: registry implementation of any kind;
provider adapter implementation or scaffolding; provider authentication;
creation, storage, rotation, reading, or verification of any credential;
any provider API call, **including read-only calls**; any MCP or
integration-fabric connection; any change to any external system; any
dependency, lockfile, or workflow change; deployment, push, pull request,
merge, or tag; or any MellyTrade, broker, trading, or order-execution
behavior.

Registering a provider under this contract — if a registry ever exists —
authorizes nothing on its own (Section 21).

## 6. Registry design principles

1. **Descriptive, not self-authorizing.** A record describes a provider.
   It never grants reach.
2. **Fail closed on absence.** A field required for an authorization
   decision that is missing, `null`, `unknown`, or unresolved **denies**.
   No permissive default exists anywhere in this contract.
3. **Separation of facts.** Registration, implementation, credential
   existence, credential verification, tenant authorization, capability
   authorization, runtime enablement, and operation approval are eight
   independent facts (Section 21). No field may collapse them.
4. **Orthogonal dimensions.** Following
   `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.2, health,
   evidence, freshness, approval, and lifecycle never imply one another.
5. **Least privilege by construction.** Scope, credential class, and
   capability set are allowlists. Anything unlisted is unavailable.
6. **Immutable identity, mutable description.** `provider_id` and
   `capability_id` never change; labels, health, and revisions do.
7. **Append-only history.** Revisions supersede; they never overwrite, and
   historical revisions are never deleted (Section 20).
8. **Provider content is untrusted.** Every provider-authored string is
   data, never instruction (Section 17).
9. **Generic floor, specific ceiling.** Provider-specific contracts may
   only add restriction, never remove it (Section 25).

## 7. Provider identity

### 7.1 Identity fields

| Field | Rule |
| --- | --- |
| `provider_id` | **Immutable, stable, machine-safe** (`^[a-z][a-z0-9_]*$`). Opaque with respect to state — it MUST NOT encode lifecycle, tenant, environment, health, or authorization (per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §7.1: "IDs MUST NOT encode mutable state"). Never reused after retirement. |
| `canonical_name` | Stable vendor-neutral name used in contracts and audit. |
| `display_name` | Human label. **May change freely without changing identity.** |
| `provider_family` | Vendor/organization grouping (e.g. one family may own several providers). |
| `provider_category` | Section 8. |
| `provider_subcategory` | Section 8. |
| `provider_owner` | MellyCore steward accountable for the record — a role reference, never a personal account ID. |
| `documentation_refs` | Official provider documentation URLs, each with `reviewed_at`. |
| `contract_ref` | Provider-specific contract identifier + revision (Section 25). `null` until one exists. |
| `registry_schema_version` | Version of *this* contract the record conforms to. |
| `record_revision` | Monotonic integer; every change increments it (Section 20). |
| `created_at` / `last_reviewed_at` | Unknown timestamps are `null`, **never fabricated** (§7.1 of the Control Plane spec). |
| `provenance` | Full provenance block per Section 16.3. |

### 7.2 Provider categories

`ai_model`, `cybersecurity`, `marketing`, `crm`, `analytics`, `identity`,
`source_control`, `cloud_infrastructure`, `observability`, `communication`,
`integration_fabric`, `mcp_server`, `internal_tool`.

A provider MAY hold exactly one primary category and zero or more
subcategories. Category is descriptive and **never** implies risk,
authorization, or trust; a `marketing` provider holding an R5 capability is
still R5.

### 7.3 Identity anti-patterns (prohibited)

Mutable `provider_id`; ID reuse after retirement; ID encoding tenant or
environment; one record shared across tenants (Section 11.4); display name
used as a join key; a downstream provider identified only by its fabric
(Section 23).

### 7.4 Terminology reconciliation with the Control Plane spec (recorded)

`[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §7.2 already defines
two entities that overlap this contract's subject:

- `Provider` — "Provider metadata; `provider_id`", oriented to **AI model
  providers** (it "Has Models", carries `modalities`, feeds the Model
  Gateway).
- `Integration` — "External-system metadata; `integration_id`", a
  **metadata-only catalogue** of external systems (GitHub, Drive, Slack,
  Vercel, …) with `access_mode`, `allowed_actions`, `read_write_class`,
  `risk_class`.

An enterprise security provider such as Cloudflare fits neither cleanly: it
is not a model provider, and it is far more consequential than a
metadata-only catalogue entry.

**Resolution (non-weakening, no edit to that spec).** This contract defines
a governance-layer record, `ProviderRecord`, which is the **authoritative
governance object**. The Control Plane's `Provider` and `Integration`
entities are **display projections** of it:

| Governance object | Control Plane projection | Projection carries |
| --- | --- | --- |
| `ProviderRecord` (category `ai_model`) | §7.2 `Provider` | Display metadata only |
| `ProviderRecord` (any other category) | §7.2 `Integration` | Display metadata only |
| `CapabilityRecord` | §7.2 `Tool` (where surfaced) | Display metadata only |

A projection **never** carries authorization, credentials, or execution
capability, consistent with §9.1's "no connect or credential action" and
§9.6's "no Connect, OAuth, authorize, or credential-entry flow". This
contract does not modify, supersede, or reinterpret the Control Plane spec;
it adds a governance layer beneath its display layer. Both remain true
simultaneously.

## 8. Provider categories and subcategories

Subcategory examples, illustrative and extensible: for `cybersecurity` —
`application_security`, `api_security`, `endpoint_security`, `siem`,
`vulnerability_management`, `identity_security`; for `marketing` —
`advertising`, `marketing_automation`, `web_analytics`, `cdp`,
`email_messaging`; for `integration_fabric` — `managed_auth_broker`,
`self_hosted_workflow`, `long_tail_connector`, `enterprise_ipaas`.

Naming a candidate here **does not** select, authorize, or schedule it.
Candidate lists live in `shared_context/ROADMAP.md` and the ADR; this
contract defines only how any of them would be *described*.

## 9. Integration classes

Extending ADR §4's three classes with the transport shapes this registry
must represent:

| Class | Meaning | Constraint |
| --- | --- | --- |
| `native_adapter` | MellyCore-owned direct adapter | **Required** for any provider holding an R4/R5 capability (ADR §4) |
| `integration_fabric` | Governed third-party fabric | Permitted for broad business/marketing/long-tail work; **never** the primary cybersecurity execution boundary (ADR §5) |
| `mcp_assisted_tool` | Restricted, operator-assisted MCP | Section 24; never unrestricted, never autonomous generic execution |
| `webhook_source` | Inbound provider-initiated events | Payloads are untrusted (Section 17); inbound events never auto-trigger a mutation |
| `event_stream` | Continuous inbound telemetry | As above, plus volume/retention limits |
| `rest_connector` / `sdk_connector` / `hybrid_connector` | Transport shape of a `native_adapter` | Declared for compatibility tracking (Section 18) |

A provider MAY be reachable through more than one class. **Each
(provider, integration class) pair is registered separately**, because
their credential, audit, and policy-enforcement properties differ — the
same downstream provider reached natively and through a fabric is not
interchangeable (Section 23).

## 10. Lifecycle state machine

### 10.1 Three orthogonal axes (material reconciliation — see 10.5)

The registry separates what a naive model would merge:

**Axis A — `registration_status`** (governance progression of the *record*):

`candidate` → `research_recorded` → `architecture_accepted` →
`contract_defined` → `conformance_verified`
with hold/terminal states `suspended`, `deprecated`, `retired`.

**Axis B — `adapter_state`** (implementation progression of the *adapter*):

`not_started` → `blocked` → `planned` → `scaffolded` → `implemented` →
`test_verified`, plus `withdrawn`.

**Axis C — the eight authorization facts** (Section 21). **Not a lifecycle
state.**

### 10.2 `registration_status` definitions

| State | Meaning | Evidence required to enter |
| --- | --- | --- |
| `candidate` | Named as a possibility | A roadmap or research reference |
| `research_recorded` | Research synchronized into canonical docs | A committed research/sync record |
| `architecture_accepted` | Covered by an accepted ADR | ADR reference + accepted status |
| `contract_defined` | A provider-specific contract exists and is accepted | `contract_ref` resolves to an accepted contract revision |
| `conformance_verified` | The contract satisfies Section 27's checklist, verified and recorded | A dated conformance record citing each check |
| `suspended` | Temporarily denied (Section 24 triggers) | Documented trigger + authority |
| `deprecated` | Superseded; historical use retained | Successor reference or explicit none |
| `retired` | No longer registrable | Retirement record; **history preserved** |

### 10.3 Transition rules

1. **No skipping.** Forward transitions occur one step at a time along
   Axis A. A provider cannot reach `contract_defined` without
   `architecture_accepted`.
2. **Evidence-gated.** Every transition cites the evidence in the table
   above. A transition without resolvable evidence is invalid.
3. **Authority.** Forward transitions to `architecture_accepted` and
   beyond require a MellyCore operator decision recorded in a canonical
   document. An agent may propose; it may never self-advance a record.
4. **Suspension is immediate and always available** from any state, by any
   operator, and does not require step-wise progression.
5. **Reverse transitions** (`conformance_verified` → `contract_defined`,
   etc.) are permitted when evidence lapses, and are **not** failures —
   they are the correct fail-closed response to contract drift
   (Section 18.3).
6. **Axis A and Axis B advance independently.** `contract_defined` +
   `adapter_state: blocked` is the current, correct state for Cloudflare
   (Section 26).
7. **No lifecycle state authorizes anything.** Not `conformance_verified`,
   not `implemented`, not `test_verified`. Authorization is exclusively
   Section 21.

### 10.4 Prohibited lifecycle designs

A state named `enabled`, `active`, `live`, `connected`, or `production`;
any state whose entry implies a credential exists; any state that grants
capability execution; a single field merging Axis A and Axis B; use of the
Control Plane's `lifecycle_status:active` to mean connectivity (its §8.2
forbids exactly this).

### 10.5 Reconciliation of the candidate state list (documented)

The state names proposed for this task were reviewed rather than adopted
verbatim, per the task's own instruction. Material changes:

| Proposed | Disposition | Reason |
| --- | --- | --- |
| `candidate`, `research_recorded`, `architecture_accepted`, `contract_defined` | **Adopted** on Axis A | Match the existing enterprise-provider documentation chain exactly |
| `implementation_blocked`, `adapter_planned`, `adapter_scaffolded`, `test_only` | **Moved to Axis B** as `blocked`, `planned`, `scaffolded`, `test_verified` | These describe the *adapter*, not the provider record; merging them onto one axis would make "provider progress" ambiguous |
| `authorized_read_only`, `authorized_limited_write` | **Rejected as lifecycle states** | These are authorization facts. Making them lifecycle states would collapse Axis C into Axis A — precisely the "registration as authorization" design this contract rejects (Section 28). Authorization is per-tenant, per-capability, and revocable independently of the provider's registration progress; a lifecycle state cannot express that |
| `suspended`, `deprecated`, `retired` | **Adopted** on Axis A | Standard terminal/hold semantics; map to Control Plane `superseded`/`historical` for evidence retention |
| — | **Added** `conformance_verified` | Section 27 needs a state meaning "validated", distinct from "a contract exists" |

## 11. Scope hierarchy

### 11.1 Dimensions

`tenant` (always required), then as applicable: `organization`, `account`,
`subscription`, `workspace`, `project`, `repository`, `site`, `zone`,
`property`, `campaign_account`, `dataset`, `environment`, `region`,
`resource`.

### 11.2 Rules

1. **`tenant` is mandatory on every record and every capability
   invocation.** A record without a resolved tenant is unusable.
2. Each provider declares its `required_scope_dimensions` and
   `optional_scope_dimensions`. A capability invocation missing a required
   dimension **fails closed** — it is never widened to a default.
3. **Scope values are explicit allowlists.** A zone, account, or workspace
   absent from the allowlist is out of scope even when the credential
   technically reaches it.
4. **Wildcards are prohibited** for R3–R5 capabilities and require an
   explicit, recorded operator decision at R0–R2. `*` never appears as an
   implicit default (Section 28).
5. **Inheritance is downward and narrowing only.** A child scope may
   restrict a parent's allowlist; it may never broaden it.
6. **Cross-scope access fails closed**, visibly and audited — never as a
   silent empty result.

### 11.3 Provider scope is not the MellyCore tenant boundary

**Normative.** A provider's own account/organization boundary MUST NOT be
assumed to equal a MellyCore tenant boundary. MellyCore enforces tenant and
scope in its own authorization layer on every invocation, independently of
what the provider's credential permits.

This generalizes a verified, concrete hazard: Cloudflare's API Gateway
Read/Edit permission groups are **account-scoped** and reach "all domains
in an account" (`[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`
§9.2). The same shape recurs across providers — organization-wide GitHub
tokens, tenant-wide Microsoft Graph grants, account-level ad-platform
access. Where a tenant's isolation requirement exceeds what the provider's
scoping can express, the resolution is a **separate provider account per
isolation boundary**, not a broader credential with MellyCore-side
filtering alone.

### 11.4 One record per tenant boundary

Provider records are **not** shared across tenants. Cross-tenant record,
credential, cache, session, context, or capability reuse is prohibited and
fails closed (ADR §10).

## 12. Authentication modes

Declared per provider as `supported_auth_modes`:

`delegated_oauth`, `service_account_oauth`, `api_token`,
`scoped_personal_token`, `workload_identity`, `signed_request`, `mtls`,
`webhook_secret`, `fabric_delegated_identity`, `mcp_oauth_grant`,
`no_auth_public_documentation`.

**Normative separation.** `supported_auth_modes` states what the provider
*offers*. It is **not** evidence that any credential is configured, valid,
or authorized. Per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]`
§17, authentication mode is permitted metadata; the value never is.

**Prohibited modes** unless a provider-specific contract explicitly governs
them with stricter rules: global/account-owner keys where scoped tokens
exist (ADR §12, §17); any mode placing credential material in
model-visible context; any mode without a revocation path.

**Delegated identity never falls back.** A `delegated_oauth` request that
lacks reach **fails**. It is never retried under
`service_account_oauth` or an administrator identity (ADR §11).

## 13. Credential profiles

### 13.1 Profile metadata (no secret material, ever)

| Field | Rule |
| --- | --- |
| `credential_profile_id` | Stable, machine-safe, opaque |
| `identity_type` | One of the seven ADR §11 identity types |
| `tenant_owner` / `provider_owner` | Both required |
| `environment` | e.g. `local`, `staging`, `production` — declared, never inferred |
| `credential_profile_class` | One canonical reusable class from Section 13.2; provider-local requirement labels and pack-local aliases are prohibited as stored/runtime values |
| `credential_class` | Coarse descriptive metadata derived from `credential_profile_class`: `read`, `controlled_write`, `containment`, or `investigation`; never a runtime-selection identifier |
| `authentication_mode` | Exactly one mode from Section 12, pinned by the concrete profile; never selected at runtime from a list |
| `permitted_capability_classes` | Allowlist of `read` / `proposal` / `mutation` classes this profile may serve |
| `provider_scope` | The explicit `(dimension → allowlist)` map of Section 11 |
| `secret_manager_ref` | **An opaque reference only** — a pointer resolvable outside model-visible context. Never a value, path to a value, or anything from which a value is derivable |
| `creation_authority` | Who authorized issuance |
| `expiry_metadata` / `rotation_metadata` | Expiry instant, rotation interval, rotation-due date |
| `revocation_state` | `active`, `revoked`, `expired`, `unknown` — `unknown` denies |
| `last_verification_time` | When the credential was last *proven* usable; `null` if never |
| `write_separation_ref` | The paired read profile, asserting separation holds |
| `emergency_containment` | Boolean; marks the narrowly scoped containment profile |

### 13.2 Canonical reusable credential-profile classes

Provider packs and provider-specific contracts MUST reference one of these
class identifiers. The class fixes the coarse Registry fields; the concrete
profile record pins the one permitted authentication mode and exact scope.

| `credential_profile_class` | `identity_type` | `credential_class` | Permitted authentication mode | Capability / use constraint |
| --- | --- | --- | --- | --- |
| `read_only_delegated` | `delegated_end_user` | `read` | `delegated_oauth` | `read`, `proposal`; never mutation |
| `read_only_service` | `service_account` | `read` | exactly one of `service_account_oauth`, `api_token`, `scoped_personal_token`, `workload_identity` | `read`, `proposal`; service identity labelled |
| `controlled_write` | exactly one of `delegated_end_user`, `service_account` | `controlled_write` | exactly one provider-contract-approved mode compatible with that identity | `mutation`; separate read profile required |
| `event_verification` | `provider_credential` | `read` | exactly one of `signed_request`, `mtls`, `webhook_secret` | inbound verification only; no outbound capability |
| `integration_fabric_read` | exactly one of `delegated_end_user`, `service_account` | `read` | `fabric_delegated_identity` | fabric-mediated `read`/`proposal`; full downstream provenance required |
| `integration_fabric_controlled_write` | exactly one of `delegated_end_user`, `service_account` | `controlled_write` | `fabric_delegated_identity` | fabric-mediated mutation; native-equivalence evidence required |
| `emergency_containment` | `service_account` | `containment` | exactly one provider-contract-approved service mode | containment allowlist only; `emergency_containment: true` |
| `reporting_only` | `service_account` | `read` | exactly one of `service_account_oauth`, `api_token`, `workload_identity` | aggregate reporting only; no raw export or mutation |
| `restricted_operator_investigation` | `mellycore_operator` | `investigation` | exactly one of `no_auth_public_documentation`, `mcp_oauth_grant`, pinned by the separately registered restricted tool | documentation/investigation only; R0-R2 maximum; no provider account access, provider API, proposal evidence, or mutation |

`read_delegated_user` and `read_service_account` are retired pack-local
aliases for `read_only_delegated` and `read_only_service`. A generic
`integration_fabric` class is prohibited because it fails to distinguish read
from controlled write. A provider-specific contract may narrow a canonical
class, but may not invent another class or widen its capability/use constraint.

**Concrete binding rule (normative).** Every concrete capability registration
MUST declare exactly one `required_credential_profile_class` from this closed
catalogue before Gateway resolution. A provider-specific requirement label may
permit more than one canonical class at specification level only when the
concrete registration selects exactly one based on its declared acting-identity
mode. The authorization records bind to that selected class. The Gateway never
chooses between classes, identity modes, or authentication modes. Zero or
multiple compatible profiles deny; there is no "best available credential",
delegated-user-to-service-account fallback, or read-to-write widening.

`restricted_operator_investigation` is not a provider credential or an
exception to provider credential resolution. It is valid only for a separately
registered, operator-only restricted tool whose account/resource binding is
empty and whose provider API and mutation authority are both prohibited. It
cannot be used by a provider API capability or substituted for any read, write,
event, fabric, containment, or reporting class.

### 13.3 Prohibitions (normative)

Raw secrets, token values, private keys, `Authorization` headers, cookies,
account IDs, or anything secret-*shaped* in any registry record, audit
entry, export, log, error, fixture, or repository file. Credential material
in model-visible context. Hidden cross-profile fallback. Automatic
privilege widening. A single profile serving both `read` and
`controlled_write` (ADR §12; Section 28).

### 13.4 Profile presence is not credential existence

**Normative.** A `credential_profile` record describes a credential that
*would* be used. Its presence is **not** evidence that a credential exists,
is valid, is unexpired, or is authorized. Those are separate facts —
Section 21 items 3 and 4 — each requiring its own evidence.

## 14. Capability records

### 14.1 Required fields

Every capability declares all of:

(1) `capability_id` — stable, immutable, **provider-bound** (prefixed by
`provider_id`); (2) `provider_id`; (3) `contract_ref` + revision;
(4) `name`; (5) `connector_domain`; (6) `operation_class`;
(7) `resource_type`; (8) `api_family`; (9) `transport_class`;
(10) `risk_tier` (Section 15); (11) `classification` —
`read` | `proposal` | `mutation` | `prohibited`; (12)
`required_identity_type`; (13) `required_credential_profile_class`;
(14) `required_provider_scope`; (15) `tenant_scope`;
(16) `data_classification` (Section 16); (17) `approval_policy`
(Section 15); (18) `idempotency_policy`; (19) `audit_policy`;
(20) `verification_policy`; (21) `retry_policy`; (22) `pagination_policy`;
(23) `concurrency_policy`; (24) `rollback_or_containment`;
(25) `external_content_exposure` (Section 17); (26)
`implementation_status` (Axis B); (27) `authorization_status`
(Section 21 — a *computed view*, never a stored grant).

### 14.2 Rules

1. **Capability IDs are immutable and provider-bound.** Two providers never
   share a capability ID. An ID is never repurposed.
2. **Absence is denial.** A capability not registered is not a MellyCore
   capability. The registry is an allowlist (mirroring
   `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]`
   Rule 15.1).
3. **A missing `risk_tier` denies.** It never defaults to R0.
4. **A missing `required_provider_scope` denies.** It never defaults to
   wildcard.
5. **A missing `approval_policy` denies.** It never defaults to allow.
6. **Capability presence is not permission.** A registered capability is a
   *policy input*. Execution requires all eight Section 21 facts.
7. **`prohibited` capabilities are registered deliberately**, so a request
   naming one is recognized and denied as an audited security event, rather
   than merely unsupported.
8. **One concrete capability, one canonical class.** Field (13) contains
   exactly one Section 13.2 identifier selected before runtime. Missing,
   provider-local, unresolved, or multiply applicable values deny.

### 14.3 The registry does not restate provider capability tables

Provider-specific contracts own their capability detail. The registry
stores the **record shape**, the **reference**, and the **conformance
requirement** — not a duplicate of the table. Duplication would create two
sources of truth that could drift (Section 26).

## 15. Risk and approval metadata

### 15.1 Risk tiers (reused verbatim from ADR §13)

| Tier | Meaning | Required behavior |
| --- | --- | --- |
| R0 | Passive metadata | May be policy-allowed read-only |
| R1 | Sensitive read | May be policy-allowed read-only |
| R2 | Draft or proposal | Produces a diff and stops; never executes |
| R3 | Reversible mutation | Policy evaluation; approval per tenant policy |
| R4 | Consequential mutation | Explicit human approval always |
| R5 | Critical or potentially destructive | Explicit human approval, strict preconditions, exact resource enumeration, enhanced audit |

Tiers are **not** redefined here. A provider-specific contract may assign a
**higher** tier than a generic reading would suggest; never a lower one
(Section 25).

### 15.2 Approval metadata (the registry references; it never approves)

Per capability: `approval_required`; `approval_class`;
`approval_authority`; `approval_expiry_policy`;
`target_binding_requirements`; `exact_enumeration_required`;
`before_after_diff_required`; `reapproval_triggers`;
`emergency_containment_path`.

**Normative.** The registry **stores approval policy**; it does not
evaluate, grant, hold, or replay approvals. Approval records are separate
objects governed by
`[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §16.1, whose
immutable four-field target binding (`target_type`, `target_id`,
`target_version`, `target_digest`) this contract adopts unchanged. A
registry record is never an approval target substitute.

**Re-approval triggers** minimally include: target state change; digest
mismatch; capability revision change; contract revision change; scope
change; credential-profile change; risk-tier change; and approval expiry.

## 16. Data classification

### 16.1 Reuse of the canonical vocabulary (no new conflicting scale)

`sensitivity_level` uses the existing five-value scale from
`[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` §5 —
`public`, `internal`, `private`, `secret`, `regulated_high_risk` — with its
`allowed_use` matrix (§5.2) and its hard rules (§5.1) unchanged: `secret`
is refused at admission always; `regulated_high_risk` defaults to rejected
pending a separate approval process that does not yet exist.

This contract does **not** invent a parallel classification scale.

### 16.2 Provider data categories (orthogonal, descriptive)

Because a five-value sensitivity scale does not by itself say *what kind*
of data a capability returns, each capability additionally declares one or
more `data_categories`, which **map into** `sensitivity_level`:

| `data_category` | Minimum `sensitivity_level` |
| --- | --- |
| `public_metadata` | `public` |
| `configuration_metadata` | `internal` |
| `business_data` | `internal` |
| `security_telemetry` | `internal` (often `private`) |
| `customer_content` | `private` |
| `personal_data` | `private`, escalating to `regulated_high_risk` where compliance obligations attach |
| `authentication_data` | `secret` |
| `credential_material` | `secret` — **never** model-visible, never registrable as a returnable category |
| `regulated_data` | `regulated_high_risk` |

A category may raise the minimum sensitivity; it may never lower it. Where
a capability returns mixed categories, the **highest** sensitivity governs
the whole response.

### 16.3 Additional data metadata

`data_origin`; `data_residency_regions`; `retention_policy`;
`permitted_storage`; `permitted_model_exposure` (derived from
`allowed_use`, never set independently); `redaction_requirements`;
`export_restrictions`; `deletion_requirements`.

**Provenance block** (per Control Plane §7.1/§18 and the sensitivity spec
§4): `source`, `source_type`, `verification_state`, `trust_level`,
`captured_at`, `validated_at`, `freshness`, `confidence`,
`immutability`, `estimation_basis`, `supersedes`, `conflict_state`.

## 17. External-content posture

### 17.1 Declared exposure

Each capability declares whether its response may contain provider- or
user-authored text: `user_generated_text`, `alert_descriptions`,
`incident_notes`, `crm_notes`, `campaign_names`, `api_schemas`,
`endpoint_labels`, `issue_bodies`, `logs`, `webhook_payloads`, `html`,
`documents`, `executable_looking_content`.

`external_content_exposure` is graded `none` | `low` | `medium` | `high`.
**Unknown exposure is treated as `high`** — the fail-closed reading.

### 17.2 Required controls (ADR §16, non-negotiable)

1. **Data, never instruction.** Provider content is never interpreted as
   an instruction, however phrased, and whatever authority it claims.
2. **Structural separation** from instruction context.
3. **Provenance preserved** on every field.
4. **Schema validation**; unexpected fields preserved untyped, never
   promoted.
5. **Normalization and sanitization** — control characters, homoglyphs,
   bidirectional overrides, nested delimiters neutralized.
6. **Size limits**; truncation explicit and labelled, never silent.
7. **No policy elevation.** Provider content may never create, modify,
   relax, or satisfy a policy, approval, capability grant, allowlist entry,
   scope, or safety rule.
8. **No tool-call generation from untrusted text** without separate policy
   review. A mutation target never originates from provider free text.
9. **Injection attempts are audited security events** (Section 20.2), with
   offending content quoted as inert data.

## 18. API and connector compatibility

### 18.1 Declared fields

`api_generation`; `api_version`; `sdk_version`; `connector_version`;
`schema_version`; `supported_date_range`; `deprecated_surfaces`;
`prohibited_legacy_surfaces`; `transitional_surfaces`;
`unverified_surfaces`; `capability_verification_date`;
`documentation_review_date`.

### 18.2 Fail-closed compatibility rules

| Condition | Behavior |
| --- | --- |
| Unsupported version | **Deny.** No execution |
| Unknown version | **Deny.** Unknown is never treated as supported |
| Only a deprecated surface available | **Deny.** No silent legacy fallback (Section 28) |
| Incompatible adapter/contract version | **Deny** until the conflict is resolved by an explicit revision |
| Capability disappeared from the provider | **Deny**; mark the capability `unavailable`; open a contract-drift review |
| Contract drift detected | **Deny** affected capabilities; reverse `conformance_verified` (Section 10.3 rule 5) |
| `capability_verification_date` absent or stale beyond policy | **Deny** R3–R5; R0–R2 per tenant policy |

### 18.3 No inference from surface naming

A surface is neither current nor deprecated because of its URL shape, its
prefix, or the absence of a deprecation banner. This generalizes the
verified Cloudflare finding
(`[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]` §8.4):
raw API-reference pages routinely omit deprecation notices that appear only
in narrative guides. Currency is established per capability, by dated
verification, and recorded.

## 19. Health and availability

### 19.1 Health values

Using the Control Plane `availability_status` dimension
(`available`, `degraded`, `unavailable`, `disconnected`, `unknown`) plus
registry-specific descriptive reasons: `reachable`, `unreachable`,
`degraded`, `rate_limited`, `authentication_unavailable`,
`permission_insufficient`, `contract_mismatch`, `api_version_unsupported`,
`suspended_by_policy`, `disabled_by_operator`.

### 19.2 Health is not authorization

**Normative, and the most commonly confused point.** Health is
**independent** of credential validity, tenant authorization, capability
authorization, and implementation status. Specifically:

- `available` does **not** mean a credential exists, is valid, or is
  authorized.
- `available` does **not** mean any tenant may invoke anything.
- `unavailable` does **not** mean unauthorized — an authorized capability
  can be temporarily unreachable.
- `unknown` means health could not be established; it is **never** read as
  available (Control Plane §8.1, §19).

Health is descriptive evidence about reachability. It is never an input
that *grants* anything, only one that can *withhold*.

## 20. Audit and provenance

### 20.1 Registry audit events (all mandatory)

Record creation; record update; lifecycle transition (either axis);
credential-profile reference update; capability addition, modification, or
retirement; scope change; risk-tier change; approval-policy change;
contract-reference change; suspension; deprecation; retirement.

Each event preserves: `actor` (and whether human, service account, or
agent — never conflated); `tenant`; `provider_id`; `previous_revision`;
`new_revision`; **exact diff**; `rationale`; `authority`; `timestamp`;
`correlation_id`; and `source_commit_or_decision_ref`.

### 20.2 Security observations

Recorded as audited security events: an attempt to invoke a `prohibited`
capability; an attempt to reach a prohibited legacy surface; a cross-tenant
or out-of-allowlist attempt; a credential-widening attempt; a suspected
injection attempt (Section 17.2 rule 9); an approval-binding mismatch; and
a registry write attempted by a non-authoritative actor.

### 20.3 Append-only history

Revisions **supersede**; they never overwrite. Historical revisions are
never deleted, including on retirement (Section 24.3). Prohibited in audit
records: raw credentials, tokens, `Authorization` headers, secret-shaped
values, and unnecessarily sensitive payload bodies. Provider account and
resource identifiers are stored as **references** resolvable within the
tenant boundary.

### 20.4 Audit availability is a precondition

If the registry's audit sink is unavailable, registry **mutations do not
proceed**, and capabilities at R3–R5 do not execute. Audit failure is
blocking, not a warning.

## 21. Registry state versus runtime authorization

### 21.1 The eight independent facts

This is the core of the contract. Execution requires **all eight** to hold
simultaneously. Each is established, evidenced, and revoked independently.

| # | Fact | Established by | Absence means |
| --- | --- | --- | --- |
| 1 | **Provider registered** | A conforming record at `registration_status: conformance_verified` | Unknown provider — deny |
| 2 | **Adapter implemented** | `adapter_state: implemented` or `test_verified`, with evidence | No execution path — deny |
| 3 | **Credential configured** | A resolvable `secret_manager_ref` for the required class | No credential — deny |
| 4 | **Credential verified** | A successful, dated verification; `revocation_state: active`; unexpired | Unverified — deny |
| 5 | **Tenant authorized** | An explicit tenant-provider authorization record | Not authorized — deny |
| 6 | **Capability authorized** | An explicit tenant-capability authorization within scope | Not authorized — deny |
| 7 | **Runtime enabled** | An explicit runtime enablement for the environment | Not enabled — deny |
| 8 | **Operation approved** | For R3–R5: a valid, unexpired, digest-bound approval for *this* operation | Not approved — deny |

### 21.2 Rules

1. **Conjunctive and fail-closed.** All eight must hold. Any one missing,
   `unknown`, expired, or unresolved **denies**. There is no override.
2. **No collapsing field.** No `enabled`, `ready`, `ok`, `connected`, or
   `status: active` field may stand for two or more facts. A schema doing
   so is non-conforming (Section 28).
3. **Independent revocation.** Revoking fact 5 does not alter facts 1–4.
   Suspending fact 1 denies everything downstream without erasing it.
4. **Facts 1–7 are standing state; fact 8 is per-operation.** Facts 1–7
   never authorize a specific mutation; only fact 8 does, and only for the
   exact bound target.
5. **`authorization_status` is a computed view**, derived at evaluation
   time from the eight facts. It is never a stored grant, never cached
   past its inputs, and never writable.
6. **Registration is not authorization.** Reaching
   `conformance_verified` satisfies fact 1 only.

### 21.3 Authorization-record custody and metadata

The Provider Registry is the authoritative custodian of authorization-record
metadata and lifecycle history. The Integration Gateway evaluates those records;
it does not issue, own, or silently synthesize them. Two record types exist and
remain separate: `tenant_provider_authorization` (fact 5) and
`tenant_capability_authorization` (fact 6).

Each record requires: stable `authorization_record_id`; `record_type`; `tenant_id`;
`provider_id`; `capability_id` (required only for fact 6); exact provider-native
scope; `environment`; `authorization_state`; `issued_by`; `issued_at`;
`effective_at`; `expires_at` or an explicit non-expiring policy reference;
`revoked_at`; `revoked_by`; `revocation_reason`; `supersedes_record_id`;
`policy_revision`; `evidence_refs`; `record_revision`; and append-only audit
metadata from Section 20. Raw credential or approval material is prohibited.

### 21.4 Lifecycle and transition authority

The lifecycle is `proposed` → `approved` → `active`, with terminal or restrictive
transitions to `suspended`, `expired`, `revoked`, or `superseded`. `approved`
does not satisfy facts 5 or 6 until its `effective_at` is reached and the record
is `active`. Only an authenticated human operator or a separately accepted
authorization-governance service may approve, suspend, revoke, or supersede a
record. An agent, provider, fabric, MCP server, webhook, adapter, or Gateway may
never do so. Reinstatement creates a new revision or successor record; it never
removes the restrictive history.

### 21.5 Issuance, revocation, propagation, and retention

Issuance requires an explicit request, exact tenant/provider/capability/scope,
authoritative approver, policy revision, and evidence. Revocation becomes
effective immediately in the Registry. The Gateway MUST re-resolve the current
revision at evaluation time and immediately before any external attempt; a stale,
missing, conflicting, suspended, expired, revoked, or superseded record denies.
Cached authorization may never outlive the earlier of record expiry, policy
freshness, or a revocation notification, and cache uncertainty denies.

Authorization records are append-only governance evidence: no hard deletion
while referenced by an audit, proposal, approval, or execution record. Retention
follows the stricter applicable legal/audit policy; expiry or revocation changes
state and never erases history. Operation approval remains separate fact 8 and
cannot be embedded in either standing authorization record.

## 22. Provider-specific contract inheritance

See Section 25 — inheritance rules are stated there to keep the
generic/specific boundary in one place.

## 23. Integration-fabric chain

### 23.1 The chain must be preserved end to end

```text
MellyCore → integration fabric → downstream provider → resource
```

Each hop is separately identified and separately registered. The fabric is
registered as a provider (`provider_category: integration_fabric`); the
downstream provider retains its **own** `provider_id`; the
`(fabric, downstream)` pair is registered as its own integration-class
record (Section 9).

### 23.2 Required chain fields

`fabric_provider_id`; `downstream_provider_id`; `downstream_tenant_identity`;
`delegated_identity`; `credential_custodian` (who holds the downstream
credential — the fabric or MellyCore); `capability_source` (whose contract
defines the capability); `policy_enforcement_location`;
`audit_source_location`; `data_transit_regions`; `fallback_behavior`;
`provenance_loss_risk`.

### 23.3 A fabric must never obscure

The real downstream provider; the acting identity; the requested
capability; the target resource; the policy decision; or the approval
record. If the fabric cannot surface all six with fidelity,
`provenance_loss_risk` is `high`, and the pair is **ineligible for R3–R5
capabilities**.

### 23.4 Fabric-specific limits

Per ADR §4–§6: a fabric MUST NOT be the primary execution boundary for
cybersecurity capabilities, and a provider holding R4/R5 capabilities MUST
be integrated natively or through a fabric-mediated path with *equivalent*
approval and audit guarantees — equivalence being demonstrated, not
assumed. Zapier MCP specifically must not become the cybersecurity
execution boundary (ADR §5).

**Policy enforcement never delegates.** MellyCore evaluates tenant, scope,
risk, and approval itself. A fabric's own governance is additive, never
substitutive.

## 24. MCP registration, suspension, deprecation, and retirement

### 24.1 MCP servers register separately

MCP servers are registered as a distinct record type, never as ordinary
providers, with: `mcp_server_id`; `server_owner`; `transport`;
`authentication_mode`; `tool_discovery_mode` (`static` | `dynamic`);
`tool_set_stability`; `generic_execution_capability` (boolean);
`allowed_tools` (allowlist); `denied_tools`; `tenant_binding`;
`credential_binding`; `output_trust_level`; `operator_only` (boolean);
`autonomous_agent_eligible` (boolean); `audit_mode`;
`max_response_size`; `execution_timeout`; `mutation_prohibited` (boolean).

### 24.2 Defaults (fail-closed)

- **No unrestricted search-and-execute**, in any form.
- **No autonomous generic execution.** `generic_execution_capability: true`
  requires `autonomous_agent_eligible: false` and `operator_only: true`.
- **Read-only or documentation-only** unless a provider-specific contract
  authorizes more.
- `dynamic` tool discovery is `high` risk by default: a tool set that can
  change between sessions cannot be pre-approved, so dynamic discovery is
  **ineligible for autonomous use**.
- `output_trust_level` is always `untrusted` (Section 17).
- Provider-specific contracts may only **narrow** these (Section 25).

This generalizes the verified rationale in
`[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]` §25.1:
a single OAuth grant spanning an entire provider API (Cloudflare's Code
Mode server covers 2,500+ endpoints) is unrestricted execute by
construction, regardless of intent.

### 24.3 Suspension, deprecation, retirement

**Suspension triggers (all fail closed, denying immediately):** provider
documentation becomes inconsistent; an API generation is deprecated; a
credential leak is suspected; tenant access is revoked; the provider
violates its contract; registered capabilities disappear; audit becomes
unavailable; read-after-write verification fails; a contract-version
conflict is unresolved.

| State | Behavior |
| --- | --- |
| `suspended` | All capabilities deny. Standing authorizations are **not deleted** — they are inert while suspended, so lifting suspension does not silently re-grant anything without re-verification of facts 3–8 |
| `deprecated` | No new registrations or authorizations; existing ones wind down under a recorded plan; **historical provenance fully preserved** |
| `retired` | Not registrable; `provider_id` never reused; **historical audit records are never deleted** |

Suspension is immediate, available from any state, and requires no
step-wise progression (Section 10.3 rule 4).

## 25. Provider-specific contract inheritance

### 25.1 Inheritance rules (normative)

1. **Generic requirements in this contract are mandatory floors.**
2. **Provider-specific contracts may add stricter requirements** — higher
   risk tiers, narrower scopes, more approvals, more verification.
3. **Provider-specific contracts may not weaken any generic requirement.**
   A weaker rule is void, not an override.
4. **Conflicts fail closed** — the stricter interpretation governs while
   the conflict is unresolved, and affected capabilities are denied.
5. **Weakening a generic rule requires an explicit, operator-approved ADR
   amendment**, never a provider contract alone.
6. **References are revisioned.** `contract_ref` carries an immutable or
   revisioned identifier, so drift is detectable.
7. **Unresolved contract-version conflicts deny execution** (Section 18.2).

### 25.2 Precedence

```text
SAFETY_CONTRACT.md  >  Enterprise-Provider ADR  >  this Registry contract
                    >  provider-specific contract (stricter only)
                    >  tenant policy (stricter only)
```

Every level may restrict. No level may relax a level above it.

## 26. Cloudflare conformance example

Demonstrating representability **without duplicating** the Cloudflare
contract's tables (Section 14.3).

### 26.1 Provider record projection

| Field | Value |
| --- | --- |
| `provider_id` | `cloudflare` |
| `canonical_name` | Cloudflare Application & API Security Provider |
| `provider_category` / `subcategory` | `cybersecurity` / `api_security`, `application_security` |
| `integration_class` | `native_adapter` — **required**, since the provider holds R4/R5 capabilities (Section 9) |
| `contract_ref` | `MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_001` @ v1.0 |
| `registration_status` (Axis A) | `contract_defined` |
| `adapter_state` (Axis B) | `blocked` |
| `required_scope_dimensions` | `tenant`, `account`, `zone` |
| `supported_auth_modes` | Provider API: `api_token` (scoped), global API key **prohibited**. Separately registered D4 restricted tools pin exactly one of `no_auth_public_documentation` or `mcp_oauth_grant` and carry no Cloudflare account binding |
| Control Plane projection | §7.2 `Integration` (display only, no authorization) |

`registration_status: contract_defined` — **not** `conformance_verified`,
because Section 27's checklist includes open verification items that the
Cloudflare contract itself records as `UNVERIFIED` in its §8.8.

### 26.2 Capability representability

The Cloudflare contract's **58 capabilities** (16 read-only, 16
proposal-only, 23 approval-required mutations, 3 operator-investigation)
and **13 prohibited** capabilities map onto Section 14.1 as follows. Its 25
per-capability attributes are a **subset** of this registry's 27 fields:

| Cloudflare attribute (its §13.0) | Registry field (Section 14.1) |
| --- | --- |
| capability ID, name, domain | 1, 4, 5 |
| Cloudflare API family, HTTP method class, resource type | 8, 9, 7 |
| account/zone scope | 14, 15 (via `required_scope_dimensions`) |
| classification, risk tier | 11, 10 |
| required MellyCore identity, provider-specific credential requirement label, minimum permission | 12; label projects normatively to 13 before registration; profile `permitted_capability_classes` narrows use |
| data classification, prompt-injection exposure | 16, 25 |
| approval requirement | 17 |
| idempotency, preconditions, concurrency | 18, 17/23, 23 |
| response normalization, pagination, rate-limit/retry | (adapter concern) 22, 21 |
| audit fields, read-after-write, rollback/containment | 19, 20, 24 |
| failure outcome | 24 + Section 18.2 |

The two registry fields with no Cloudflare counterpart —
`implementation_status` (26) and `authorization_status` (27) — are exactly
the registry's own contribution: they keep *description* separate from
*readiness* and *authorization*, which a provider contract alone cannot
express.

The Cloudflare labels project as follows: `CF_READ` selects exactly one of
`read_only_delegated` or `read_only_service` according to the concrete
registration's acting-identity mode; `CF_WRITE_CONTROLLED` selects
`controlled_write`; `CF_CONTAIN` selects `emergency_containment`; and
`CF_MCP_OPERATOR` selects `restricted_operator_investigation`. The projection
is performed by the provider contract and stored on the concrete capability
record before runtime. The Gateway never receives or interprets a `CF_*` label.

### 26.3 Preserved without weakening

| Cloudflare rule | Registry mechanism preserving it |
| --- | --- |
| Firewall Rules API, Filters API, Classic Schema Validation, `user_schemas/hosts` excluded | `prohibited_legacy_surfaces` (Section 18.1) + no-legacy-fallback (Section 18.2, Section 28) |
| Zone-wide `block` always R5 | Risk tier stored per capability; provider contract may raise, never lower (Section 15.1) |
| Read/write credential separation | Two profiles, `credential_class` `read` and `controlled_write` (Section 13) |
| Account-scoped Cloudflare permissions ≠ MellyCore tenant | Section 11.3, stated generically |
| MCP documentation-only, no account grant | `restricted_operator_investigation` capability binding plus MCP record with `mutation_prohibited: true`, `operator_only: true`, `autonomous_agent_eligible: false`, empty account binding (Section 24) |
| Read-after-write mandatory for mutations | `verification_policy` (field 20), non-optional for `classification: mutation` (Section 27) |
| Read-only Cloudflare API access still unauthorized | Section 21 facts 5–7 unsatisfied; `adapter_state: blocked` |

**Result: representable with no weakening detected.** No Cloudflare
requirement failed to fit, and no generic rule had to be relaxed to
accommodate it.

## 27. Validation and conformance rules

### 27.1 Checklist required before `conformance_verified`

1. A canonical provider-specific contract exists and is accepted.
2. `provider_id` unique and never previously retired.
3. All `capability_id`s unique and provider-bound.
4. Every capability has an explicit `risk_tier`.
5. Every capability has explicit `required_provider_scope`; no wildcards at
   R3–R5.
6. Read and write credential profiles are separate and declared.
7. `external_content_exposure` declared for every capability.
8. Audit requirements complete for every capability.
9. **Read-after-write verification defined and non-optional for every
   `classification: mutation` capability.**
10. Approval policy defined for every capability; none defaults to allow.
11. Prohibited legacy/deprecated surfaces enumerated and excluded.
12. Implementation validators exist and are runnable.
13. Security review complete and recorded.
14. Every `UNVERIFIED` item in the provider contract resolved and dated.

### 27.2 Truthfulness rule

**No provider may be described as conformance-verified, connected,
authenticated, credentialed, enabled, or authorized without canonical,
file-backed evidence.** Consistent with
`[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` §1.5: a validator that
did not run records `NOT_RUN`, never a defaulted pass. **This contract
asserts these validations pass for no provider**, including Cloudflare
(Section 26.1).

## 28. Rejected designs

| Rejected | Why |
| --- | --- |
| One `enabled` boolean as provider state | Collapses eight independent facts (Section 21) into one; makes revocation and partial authorization inexpressible |
| Provider registration as runtime authorization | Registration is description; authorization is Section 21 |
| Capability existence as permission | A capability record is a policy input, not a grant (Section 14.2) |
| Provider account as MellyCore tenant boundary | Section 11.3; verified account-scoped-permission hazard |
| Raw credentials in registry records | Section 13.3; `SAFETY_CONTRACT.md` |
| One credential for read and write | ADR §12, §17 |
| Silent delegated-user → service-account fallback | ADR §11; Section 12 |
| Fabric-only downstream identity | Section 23.3; destroys attribution and approval fidelity |
| Unrestricted MCP tool discovery and execution | ADR §4, §17; Section 24.2 |
| Missing risk tier defaulting to low risk | Section 14.2 rule 3 |
| Missing scope defaulting to wildcard | Section 14.2 rule 4 |
| Missing approval policy defaulting to allow | Section 14.2 rule 5 |
| Deprecated APIs as silent fallback | Section 18.2; a failed replacement fails closed |
| Provider health as proof of authorization | Section 19.2 |
| Cross-tenant provider records | Section 11.4 |
| Deletion of historical registry revisions | Section 20.3; Section 24.3 |
| Mutable provider IDs | Section 7.1, 7.3 |
| Provider-specific contracts overriding generic safety with weaker rules | Section 25.1 rule 3 |
| Lifecycle states that mean "authorized" | Section 10.5 — would re-merge Axis C into Axis A |
| A registry that stores or resolves secrets | Section 5; the registry holds references only |

## 29. Implementation prerequisites

Registry implementation may not begin until **all** hold:

1. This contract is accepted and — like the ADR and Cloudflare contract it
   serves — reviewed, published, and merged through normal gates.
2. `MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` passes.
3. `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` passes.
4. `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` passes.
5. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003` passes.
6. `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` receives its own **separate,
   explicit operator authorization**, independent of Model A/B deployment
   authorization and of the OpenAI Batch Stage C gate. It remains
   **blocked** until then.
7. A secrets boundary exists that can hold separated read/write profiles
   outside model-visible context and resolve `secret_manager_ref` without
   exposing values.
8. An approval broker exists that can enforce the Control Plane §16.1
   four-field binding.
9. An audit sink exists that can record Section 20.1 in full and block
   registry mutations and R3–R5 execution when unavailable.

Until item 6 is satisfied, **read-only provider API access also remains
unauthorized**, consistent with `shared_context/RUN_QUEUE.md`.

## 30. Open questions

1. **Credential verification mechanics** (fact 4) — how a credential is
   proven usable without a broad probe, and how often, is unresolved.
2. **Numeric freshness thresholds** for `capability_verification_date` and
   `documentation_review_date` — currently tenant-policy shaped, not fixed.
3. **Whether `regulated_high_risk` provider data can ever be admitted** —
   the sensitivity spec §5.1 defers this to a separate approval process
   that still does not exist; until it does, such capabilities are
   unregistrable as returnable.
4. **Registry record storage format** — deliberately unspecified, since
   naming one would edge toward implementation.

## 31. Amendment and supersession rules

This contract may be amended or superseded only by a later, explicitly
identified document that references this file **by path** and states which
section(s) it changes — the pattern established by
`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` and required by
the enterprise-provider ADR of itself. A later document that silently
contradicts this contract does **not** supersede it; such a contradiction
must be corrected, not treated as an implicit amendment.

Specifically requiring an amendment: weakening any fail-closed default;
merging any two of the eight authorization facts; adding a lifecycle state
that implies authorization; permitting wildcard scope at R3–R5; permitting
a shared read/write credential profile; permitting autonomous unrestricted
MCP; or allowing a provider-specific contract to relax a generic rule.

Amending this contract never amends the ADR; where the two diverge, the
ADR prevails (Section 3).

## 32. References

### 32.1 Repository (canonical)

- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` —
  governing architecture decision.
- `[[MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001]]` —
  first provider-specific contract; conformance target (Section 26).
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` — §7.1/§7.2
  entity contract and catalogue, §8 status taxonomy, §9.1 Provider Registry
  module, §9.6 Integration Gateway, §16 approval contract, §17 secrets
  boundary, §18 provenance, §19 failure states, §25 integration seams.
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]` — §4
  provenance labels, §5 sensitivity labels and `allowed_use` matrix.
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` — §1.5 truthfulness
  rules; contract-spec format precedent.
- `shared_context/SAFETY_CONTRACT.md`, `shared_context/PROJECT_STATE.md`,
  `shared_context/ROADMAP.md`, `shared_context/RUN_QUEUE.md`,
  `shared_context/AGENT_HANDOFF.md`.
- `docs/tasks/MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001.md` —
  this contract's task report.

### 32.2 External

None. This contract required no external documentation fetch: it governs
MellyCore's own record structure, and every provider-specific technical
claim it relies on is carried by reference from the already-verified
Cloudflare contract rather than re-asserted here.
