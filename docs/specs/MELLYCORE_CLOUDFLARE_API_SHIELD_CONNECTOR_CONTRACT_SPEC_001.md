# MellyCore Cloudflare API Shield Connector Contract Spec

**Task ID:** MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001
**Contract ID:** MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_001
**Version:** 1.0
**Status:** ACCEPTED as a specification-level connector contract only. **This status does not authorize runtime implementation, adapter scaffolding, provider authentication, Cloudflare API token creation, credential access, any Cloudflare API call (including read-only calls), any Cloudflare MCP connection, any Cloudflare configuration change, or deployment.** It fixes the capability, authorization, approval, idempotency, verification, audit, and rollout contract that a later, separately authorized implementation task must satisfy.
**Scope:** Defines the complete specification-level contract governing how MellyCore AIOS may — once separately authorized — interact with a future `Cloudflare Application & API Security Provider` across API Shield, API Discovery, Endpoint Management, Authentication Posture, endpoint labels, Schema Validation 2.0, WAF Rulesets, security events, audit events, and restricted operator-assisted Cloudflare MCP use.

---

## 1. Title and status

### 1.1 Status meaning (normative)

This document is an **accepted specification-level contract**, in exactly the
same sense as the ACCEPTED status of
`[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]`: it
fixes direction so that later, separately gated implementation tasks have a
stable target, without itself performing or authorizing that implementation.

Acceptance of this contract means, and means only, that:

1. The capability set, risk classification, approval rules, credential
   model, audit fields, verification rules, and rollout staging below are
   the canonical target a future Cloudflare adapter must satisfy.
2. Any future Cloudflare implementation task that deviates from this
   contract is non-conforming and must either be corrected or must
   explicitly amend this contract under Section 38.

Acceptance of this contract does **not** mean any of the following, none of
which exist at the time of writing: an implemented connector; a configured
provider; a created or stored Cloudflare API token; an authenticated
session; an executed Cloudflare API request; a connected Cloudflare MCP
server; a modified Cloudflare account, zone, ruleset, schema, or endpoint;
or a deployment.

### 1.2 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Connector implementation | `NOT_IMPLEMENTED` |
| Adapter scaffold | `BLOCKED` (Section 35) |
| Provider credential | `NOT_CONFIGURED` — none exists in this repository or its environment |
| Provider authentication | `NEVER_PERFORMED` |
| Cloudflare API execution | `NEVER_PERFORMED` (no authenticated call, read or write) |
| Cloudflare MCP connection | `NOT_CONNECTED` |
| Cloudflare account/zone configuration | `UNCHANGED` — no MellyCore task has mutated any |
| Evidence class for every capability below | `future_live` (per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8) |

No row above may be advanced by a documentation task. Each requires its own
separately authorized implementation or authorization task with file-backed
evidence.

## 2. Purpose

MellyCore needs a fixed, tenant-safe, credential-safe contract for a future
Cloudflare application- and API-security connector **before** any adapter
code exists, so that:

- capability scope and blast radius are decided deliberately rather than
  emerging from whatever the SDK happens to expose;
- the boundary between reading Cloudflare state, proposing a change, and
  executing a change is structural rather than conventional;
- legacy and deprecated Cloudflare API generations are excluded by contract
  rather than discovered late;
- approval, idempotency, concurrency, verification, rollback, and audit
  obligations are attached to each capability individually rather than
  applied as a uniform afterthought;
- the specific ways a Cloudflare change can break production traffic
  (a zone-wide `block`, a reordered blocking rule, a detached protective
  ruleset, a deleted endpoint) are named and gated in advance.

## 3. Authority and relationship to the enterprise-provider ADR

`[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` is the
governing architecture decision. This contract is **subordinate** to it and
does not amend, reinterpret, or narrow it. Where the ADR states a rule, this
contract restates it in Cloudflare-specific terms and adds detail; it never
relaxes it.

| ADR section (by number and title) | Binding effect on this contract |
| --- | --- |
| §4 Provider integration classes | If a Cloudflare connector is ever authorized, it must be built as a **native high-trust adapter** — not through an integration fabric and not through MCP (Section 25). Cloudflare is not integrated today (Section 1.2). |
| §6 Cybersecurity-provider tiers | Initial Cloudflare behavior must be read-only; WAF mutation, schema blocking, and remediation are R4/R5 requiring explicit human approval. |
| §8 Cloudflare decision | Binding legacy exclusions (Section 7) and the consequential-operation list (Section 17.1). |
| §10 Tenant isolation model | Section 9 of this contract. |
| §11 Identity model | Section 10 of this contract. |
| §12 Credential model | Section 11 of this contract. |
| §13 Capability and risk-tier model | Sections 12–14 of this contract; R0–R5 tiers are reused verbatim, not redefined. |
| §14 Approval model | Section 18 of this contract. |
| §15 Audit and verification model | Sections 31–33 of this contract. |
| §16 External-content and prompt-injection posture | Section 26 of this contract. |
| §19 Implementation prerequisites | Section 35 of this contract; this document is item 2 of that nine-item gate. |
| §20 Explicit non-authorizations | Section 5 of this contract. |
| §22 Supersession or amendment rules | Section 38 of this contract. |

**Conflict rule.** If a future reading of this contract appears to conflict
with the ADR, the ADR prevails and the conflict must be corrected here — a
silent contradiction in this document does not amend the ADR. No
architectural conflict with the ADR was found while authoring this contract;
one **documentation defect** in the ADR was observed and is recorded, without
edit, in Section 37.2.

## 4. Scope

### 4.1 In scope

Specification-level definition of: supported and excluded Cloudflare API
families; stable MellyCore capability IDs; read-only, proposal-only,
approval-required, and prohibited classifications; tenant/account/zone
isolation; credential separation; risk classification; approval and
execution rules; idempotency and concurrency; read-after-write verification;
rollback and containment; prompt-injection handling; audit-event
requirements; staged Schema Validation rollout; WAF Rulesets mutation
safety; and the conditions that must pass before implementation may begin.

### 4.2 Out of scope

Adapter code, HTTP client, SDK selection, retry library, secret-store
selection, UI surface, workflow definition, dependency addition, Cloudflare
account/zone selection, token issuance, and every runtime concern. These
belong to later, separately authorized tasks and are constrained — not
performed — by this document.

## 5. Explicit non-authorizations

This contract does **not** authorize:

1. Cloudflare connector or adapter implementation of any kind, including a
   scaffold, stub, interface, or type definition intended for runtime.
2. Cloudflare authentication of any kind.
3. Creation, storage, rotation, or reading of any Cloudflare API token, API
   key, or credential.
4. Any Cloudflare API call, **including read-only calls** — no connector
   contract existing previously, read-only Cloudflare API access was and
   remains unauthorized (`shared_context/RUN_QUEUE.md`, "Parallel Decision
   Track — Enterprise Provider Integration"). Acceptance of this contract
   alone does not lift that block; Section 35 does.
5. Any Cloudflare MCP server connection or MCP-mediated execution.
6. Any change to a Cloudflare account, zone, ruleset, rule, schema,
   endpoint, label, or setting.
7. Any HTTP client, SDK dependency, lockfile change, or workflow definition.
8. Deployment, release, push, pull request, merge, or tag.
9. Any MellyTrade, broker, trading, or order-execution behavior. MellyCore
   AIOS performs none and this contract introduces none.

## 6. Supported Cloudflare domains

The connector is divided into four logical domains. The domain boundary is
an **authorization boundary**, not merely an organizational one: a
capability may not be promoted from one domain to another without amending
this contract (Section 38).

| Domain | Name | Nature | Executes a write? |
| --- | --- | --- | --- |
| D1 | Cloudflare Security Inventory | Deterministic read-only access | No |
| D2 | Cloudflare API Shield Posture | Read + proposal generation | No — produces diffs, never applies them |
| D3 | Cloudflare Protection Changes | Approval-required mutation | Yes, only after Section 18 approval |
| D4 | Cloudflare Operator Investigation | Restricted operator-assisted access | No |

Supported Cloudflare product areas: API Shield, API Discovery, Endpoint
Management, Authentication Posture, managed endpoint labels, user-defined
endpoint labels, Schema Validation 2.0, WAF Rulesets (via the Rulesets API),
security-event observation, audit-event observation, and — under Section 25
only — documentation-scoped operator-assisted MCP use.

## 7. Excluded legacy API families (binding)

The following are **excluded from any new MellyCore integration**. Exclusion
is by contract, not by convenience: a future implementation task may not
select one of these because it appeared simpler, better documented, or
lacked a deprecation banner.

| Excluded family | Basis | Replacement |
| --- | --- | --- |
| Cloudflare Firewall Rules API (`/zones/{zone_id}/firewall/rules`) | Product deprecated; API unsupported since 2025-06-15 (Section 8.1) | Rulesets API, phase `http_request_firewall_custom` |
| Cloudflare Filters API | Unsupported since 2025-06-15 alongside Firewall Rules (Section 8.1) | Rulesets API |
| Classic Schema Validation | Deprecated; new schemas cannot be added (Section 8.2) | Schema Validation 2.0 |
| `GET /zones/{zone_id}/api_gateway/user_schemas/hosts` | Legacy user-schema surface; explicitly excluded by ADR §8 | Schema Validation 2.0 schema inventory |
| `POST` / `DELETE` `/zones/{zone_id}/api_gateway/user_schemas[/{schema_id}]` as a **primary** schema-lifecycle surface | Belongs to the Classic generation | `POST` / `GET` / `DELETE` `/zones/{zone_id}/schema_validation/schemas[/{schema_id}]` |

**Rule 7.1 — no legacy fallback.** If a supported replacement surface is
unavailable, degraded, or returns an unexpected shape, the connector fails
closed. It must not silently fall back to an excluded family. A silent
generation downgrade is a contract violation, not a resilience feature.

**Rule 7.2 — legacy IDs are not portable.** Rule IDs differ between legacy
firewall rules and WAF custom rules (Section 8.1). No MellyCore record,
proposal, approval, or audit entry may carry a legacy rule ID forward as if
it identified a Rulesets-API rule.

## 8. API-generation and compatibility policy

### 8.1 Verified: Firewall Rules → Rulesets API

Verified 2026-08-01 against
`https://developers.cloudflare.com/waf/reference/migration-guides/firewall-rules-to-custom-rules/`
("Firewall rules upgrade"), by unauthenticated read of public documentation:

- "Cloudflare Firewall Rules is now deprecated."
- "The Firewall Rules API and Filters API ... are no longer supported since
  2025-06-15."
- "You must manually update any automation based on the Firewall Rules API
  or Cloudflare Filters API to the Rulesets API."
- "Rule IDs are different between firewall rules and custom rules, which may
  affect automated processes dealing with specific rule IDs."
- The custom-rules phase is `http_request_firewall_custom`.

This **independently confirms** the operator-supplied research recorded by
`MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001`, which the prior ADR task's
narrower spot check could neither confirm nor refute (ADR §8, source note).

### 8.2 Verified: Schema Validation 2.0 is current; Classic is deprecated

Verified 2026-08-01 against
`https://developers.cloudflare.com/api-shield/security/schema-validation/`
("Schema validation") and
`https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/`
("Classic Schema validation (deprecated)"):

- "Schema validation 2.0 is the current version."
- "You can make changes to your Classic Schema validation settings but you
  cannot add any new schemas."
- "Classic Schema validation has been deprecated." — the page title itself
  carries the `(deprecated)` marker.
- "Upload all new schemas to Schema validation 2.0."
- "Endpoints must be added to Endpoint Management for Schema validation to
  protect them."
- Supported mitigation actions: `none`, `log`, `block`, settable as a zone
  default and per endpoint.

### 8.3 Verified: current Schema Validation API surfaces

Verified 2026-08-01 against
`https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/`
("Schema Validation › Settings"):

```text
GET    /zones/{zone_id}/schema_validation/settings
PUT    /zones/{zone_id}/schema_validation/settings
PATCH  /zones/{zone_id}/schema_validation/settings
GET    /zones/{zone_id}/schema_validation/settings/operations
GET    /zones/{zone_id}/schema_validation/settings/operations/{operation_id}
PUT    /zones/{zone_id}/schema_validation/settings/operations/{operation_id}
PATCH  /zones/{zone_id}/schema_validation/settings/operations
DELETE /zones/{zone_id}/schema_validation/settings/operations/{operation_id}
```

and, from
`https://developers.cloudflare.com/api-shield/security/schema-validation/api/`
("Configure Schema validation via the API"):

```text
POST   /zones/{zone_id}/schema_validation/schemas
GET    /zones/{zone_id}/schema_validation/schemas
DELETE /zones/{zone_id}/schema_validation/schemas/{schema_id}
```

Mitigation-action values are `log`, `block`, `none`. A zone-level
`validation_override_mitigation_action` exists and, when set, "overrides both
zone level and operation level mitigation actions" — Cloudflare describes it
as "a quick way to disable schema validation for the whole zone." This
contract adopts that field as the **emergency containment lever** required by
Section 21.

### 8.4 Recorded honestly: transitional documentation inconsistency

The current Schema Validation 2.0 configuration guide
(`.../schema-validation/api/`, accessed 2026-08-01) still references
`/api_gateway/...` paths for several steps, alongside the
`/schema_validation/...` family above:

```text
PATCH /zones/{zone_id}/api_gateway/user_schemas/{schema_id}                 (activate a schema)
GET   /zones/{zone_id}/api_gateway/user_schemas/{schema_id}/operations      (retrieve new operations)
POST  /zones/{zone_id}/api_gateway/operations                               (add operations to Endpoint Management)
GET   /zones/{zone_id}/api_gateway/settings/schema_validation               (default mitigation action)
PUT   /zones/{zone_id}/api_gateway/settings/schema_validation
PATCH /zones/{zone_id}/api_gateway/settings/schema_validation
GET   /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation
PUT   /zones/{zone_id}/api_gateway/operations/{operation_id}/schema_validation
```

So the same logical settings exist under **two path families**
(`/api_gateway/settings/schema_validation` and
`/schema_validation/settings`), and the 2.0 guide still routes schema
*activation* and *operation discovery* through `/api_gateway/user_schemas/`
— a family this contract otherwise treats as the Classic generation.

Additionally, the raw API-reference pages for
`/zones/{zone_id}/api_gateway/user_schemas` and
`/zones/{zone_id}/api_gateway/user_schemas/hosts` carry **no deprecation
banner** (both accessed 2026-08-01), while the narrative
`Classic Schema validation (deprecated)` page states the generation is
deprecated. Cloudflare's auto-generated reference pages commonly omit
deprecation notices that appear only in narrative guides.

**Rules derived from this inconsistency (normative):**

1. **No URL-family inference.** A path is neither current nor deprecated
   because of its prefix. `/api_gateway/...` is not automatically legacy and
   `/schema_validation/...` is not automatically current.
2. **No banner inference.** Absence of a deprecation banner on a raw
   reference page is **not** evidence a surface is current. Presence of a
   `(deprecated)` marker on a narrative page **is** evidence it is not.
3. **Implementation-time capability verification is mandatory.** Before the
   first request of any capability in Section 13, the implementation task
   must re-verify, against official Cloudflare documentation on that date,
   which concrete path currently serves that capability, and record the
   result. This contract binds the *capability*, not the *URL*.
4. **Prefer the replacement where one exists.** Where a supported
   replacement exists for a step (schema create/list/delete), the
   `/schema_validation/...` family is mandatory. Where the current 2.0 guide
   documents **only** an `/api_gateway/...` path for a step (schema
   activation, new-operation discovery, adding operations to Endpoint
   Management), that path is permitted as a **transitional surface**, must be
   labeled `transitional` in the capability record and in every audit entry,
   and must be re-verified per rule 3 at each implementation milestone.
5. **Excluded regardless.** `/api_gateway/user_schemas/hosts` is excluded
   outright (Section 7) and is not eligible for transitional use, because no
   MellyCore capability requires it.

### 8.5 Verified: Rulesets API concepts

Verified 2026-08-01 against
`https://developers.cloudflare.com/ruleset-engine/about/rulesets/`
("Rulesets") and `.../rulesets-api/` ("Rulesets API"):

- Ruleset categories: **entry point rulesets**, **managed rulesets**
  (Cloudflare-provided), **custom rulesets** (user-created).
- `kind` values for phase entry points: `root` (account level), `zone`
  (zone level).
- "Each phase has at most one entry point ruleset at the account level and
  at the zone level."
- "Rulesets belong to a phase and can only execute in the same phase."
- "Each ruleset modification creates a new version of the ruleset." Multiple
  versions coexist; deployment selects the most recent version by default.
- Cloudflare advises: "You should avoid making concurrent updates to the
  same ruleset," and to update "the entire ruleset in a single operation."
- Endpoint shapes include `PUT /zones/{zone_id}/rulesets/{ruleset_id}` and
  `PUT /zones/{zone_id}/rulesets/phases/{phase_name}/entrypoint`, with
  account-level equivalents under `/accounts/{account_id}/rulesets`.

### 8.6 Verified: Endpoint Management and Authentication Posture

Verified 2026-08-01 against
`https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/`
("Endpoint Management"):

- An operation is identified by "its HTTP method, hostname pattern, and path
  pattern."
- Operations enter Endpoint Management from API Discovery, from an uploaded
  schema, or manually.
- Operations must be in the `full` state for persisted API profiles, risk
  findings, and profile learning / performance-analysis data collection.
- On deletion of a full operation: "Cloudflare stops tracking its associated
  performance and analytics data. Its previous historical metrics cannot be
  restored."

Verified against `.../api-shield/security/authentication-posture/`
("Authentication Posture"): it is read-only reporting that emits
`cf-missing-auth` and `cf-mixed-auth` labels and does not block traffic;
blocking requires a separate custom rule.

Verified against
`.../api-shield/management-and-monitoring/endpoint-labels/`
("Endpoint labeling service"): managed labels (e.g. `cf-log-in`,
`cf-purchase`, `cf-risk-missing-auth`) are Cloudflare-applied; user-defined
labels are operator-created.

### 8.7 Verified: token permissions, audit logs, MCP

- `https://developers.cloudflare.com/fundamentals/api/reference/permissions/`
  ("API token permissions"): **API Gateway Read** / **API Gateway Edit** are
  account-scoped permission groups covering API Gateway "(including API
  Shield) for all domains in an account". **Account WAF Read** / **Account
  WAF Edit**, **Account Settings Read/Edit**, and **Logs Read/Edit** are
  likewise account-scoped. The page contains no discussion of Global API Key
  versus API tokens.
- `https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/`
  ("Review audit logs - v1"): audit logs are retained 18 months; Audit Logs
  version 2 exists with separate documentation; v1 carries no explicit
  deprecation notice on that page.
- Cloudflare operates a catalog of managed remote MCP servers reachable over
  OAuth, including a **Code Mode server covering the entire Cloudflare API
  (over 2,500 endpoints)** at `https://mcp.cloudflare.com/mcp`, plus
  domain-specific servers for documentation, observability, and DNS
  analytics.

### 8.8 Claims requiring later external verification

The following were **not** independently verified in this session and are
carried as open verification items, not as established fact. None may be
treated as settled by an implementation task without its own dated check.

| Item | Status |
| --- | --- |
| Exact REST paths for endpoint-label creation and label→operation binding | `UNVERIFIED` — narrative docs list no REST paths; API reference not fetched |
| Exact zone-scoped token permission names for API Gateway and WAF (only account-scoped names were surfaced) | `UNVERIFIED` |
| Exact path/shape of the Audit Logs v2 endpoint, and whether v1 is formally deprecated | `UNVERIFIED` |
| Exact security-event search surface (Firewall Events vs GraphQL Analytics) and its filter grammar | `UNVERIFIED` |
| Whether label→operation binding is additive or wholesale-replacing at the API level | `UNVERIFIED` — Section 24 assumes replacement semantics as the fail-safe reading |
| Whether managed labels are editable by API | `UNVERIFIED` — Section 24 treats them as read-only |
| Cloudflare plan-dependence of API Shield / Schema Validation features | `PLAN_DEPENDENT`, not enumerated here |

## 9. Tenant, account, and zone isolation

### 9.1 Isolation requirements

Per ADR §10, each enterprise tenant requires an isolated logical
authorization boundary. Applied to Cloudflare:

1. **Tenant-specific provider registration.** A tenant that has not
   registered the Cloudflare provider has no Cloudflare capability, and a
   registration for tenant A never satisfies a request for tenant B.
2. **Explicit account scoping.** Every capability carries an explicit
   Cloudflare account reference. No capability may operate against "the
   default account," "the only account," or an account inferred from a
   token's implicit reach.
3. **Explicit zone scoping.** Every zone-scoped capability carries an
   explicit zone reference. Enumerating zones (`cloudflare.zones.list`) does
   not authorize acting on them.
4. **Allowlist, not denylist.** The set of `(tenant, account, zone)` triples
   a credential may touch is an explicit allowlist. A zone absent from the
   allowlist is out of scope even if the credential technically reaches it.
5. **No cross-tenant reuse.** No Cloudflare credential, cache entry, session,
   context packet, proposal, approval, or idempotency key may be shared
   across tenants.
6. **Fail closed.** A cross-tenant, cross-account, or out-of-allowlist access
   attempt fails visibly with an audited denial. It never degrades to a
   narrower success, and never silently returns empty.

### 9.2 The account-scope hazard (Cloudflare-specific)

Cloudflare's **API Gateway Read/Edit** permission groups are **account
scoped** and grant access "for all domains in an account" (Section 8.7).
A token that MellyCore intends for one zone therefore reaches every zone in
that account.

**Rule 9.2.** Cloudflare's own permission model must never be treated as
MellyCore's tenant boundary. MellyCore enforces zone scope in its own
authorization layer, on every request, independently of what the token
permits. Where a tenant's isolation requirements exceed what Cloudflare
account-scoped tokens can express, the correct resolution is a **separate
Cloudflare account per isolation boundary** — not a broader token with
MellyCore-side filtering alone.

**Rule 9.3.** Under ADR §10, one shared application process is not accepted
as sufficient hostile multi-tenant isolation. For Cloudflare — a provider
holding R4/R5 capabilities — a deployment serving mutually untrusting
tenants additionally requires separated execution: separate process or
container, separate queue, separate secret namespace, and separate network
policy.

## 10. Identity model

The seven identity types of ADR §11 are not conflated. Cloudflare-specific
consequences:

| Identity | Cloudflare-specific rule |
| --- | --- |
| MellyCore operator | The only identity that may initiate a D4 investigation session or grant an R4/R5 approval. |
| Enterprise tenant | Selects the provider registration, credential profile, and account/zone allowlist. Never inferred. |
| Delegated end user | If ever used, must not silently fall back to a service account or an administrator identity. A delegated request that lacks reach **fails**; it is not retried with broader credentials. |
| Service account | Every service-account action is labeled as such in audit records and never presented as a human action. |
| Provider credential | A Cloudflare token identity distinct from every MellyCore identity; possession is not authorization. |
| Agent / runtime | May request; may never self-approve an R4/R5 action. |
| Session / context | **Routing and context selectors only, never authorization** (ADR §§9, 11). A session ID never widens scope, never substitutes for an approval ID, and never satisfies a precondition. |

**Rule 10.1 — capability IDs are not grants.** A capability ID is an
authorization *input*: it names what is being requested so that policy can
evaluate it. Presenting, possessing, or resolving a capability ID confers no
permission. Authorization requires, jointly: tenant registration, an
allowlisted `(account, zone)` scope for provider API capabilities, a policy
decision, the canonical `required_credential_profile_class` bound by the
concrete capability, and — for R4/R5 — a valid approval bound to that exact
proposal.

## 11. Credential model and credential profiles

### 11.1 Profiles

At least four credential profiles are defined. They are **specifications for
credentials that do not exist**; this contract creates none.

For this contract, each `CF_*` name is a **provider-specific credential
requirement label**: Cloudflare-owned shorthand for provider-specific intent.
It is not a Registry class, a Gateway runtime-selection identifier, an
authorization fact, an approval, runtime enablement, or operation approval. The
Provider Registry owns canonical credential-profile classes; the Integration
Gateway resolves one concrete profile only after the provider contract has
projected its label to exactly one canonical class on the capability record.

| Provider-specific requirement label | Purpose | Cloudflare permission class (minimum) | Capabilities served |
| --- | --- | --- | --- |
| `CF_READ` | Deterministic inventory and posture reads | API Gateway Read; WAF/Rulesets read; Logs Read for event lookup; account/zone read | All of D1; the read half of D2 |
| `CF_WRITE_CONTROLLED` | Approved, scoped mutations | API Gateway Edit and/or WAF Edit, narrowed to the exact capability set approved for the tenant | D3 only, and only after Section 18 approval |
| `CF_CONTAIN` | Emergency containment (Section 33.3) | The narrowest permission that permits setting mitigation action to `none` and disabling a schema | The containment subset of D3 only |
| `CF_MCP_OPERATOR` | Operator-assisted documentation session | Documentation-scoped only; **no account grant** in v1.0 (Section 25) | D4 only |

### 11.1.1 Normative projection to Registry classes

| Label/value | Remains? | Canonical projection | Concrete-registration rule | Identity constraints | Maximum risk | Provider API authority | MCP authority | Mutation authority | Fail-closed behavior | Migration / retirement rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CF_READ` | Yes, as provider shorthand only | Exactly one of `read_only_delegated`, `read_only_service` | Select one before runtime from the declared acting-identity mode; store it as `required_credential_profile_class` | Delegated user or conspicuously labelled service account; no switching | R2 | Bounded read only, and only after separate authorization | None | None | Zero/multiple compatible profiles, identity mismatch, or unresolved label deny; no delegated→service fallback | Existing registrations migrate to one identity-specific canonical class; no Gateway interpretation of `CF_READ` |
| `CF_WRITE_CONTROLLED` | Yes, as provider shorthand only | `controlled_write` | Every D3 non-containment registration binds this one class | Exactly one declared delegated-user or service-account mode; separate read profile required | R5 | Exact approved write surface only | None | R4/R5 only with all approval, audit, idempotency, verification, and reconciliation controls | Missing/multiple profiles, permission failure, or approval mismatch deny; no broader-profile retry or read→write widening | Replace any runtime use of the label with `controlled_write`; label remains descriptive in this contract |
| `CF_CONTAIN` | Yes, as provider shorthand only | `emergency_containment` | Containment registrations bind this one class and the containment allowlist | Labelled service account only | R5 | Narrow containment API surface only | None | Approved containment only; class membership alone never authorizes it | Missing/multiple profiles or any absent approval/audit/verification fact denies; no fallback | Replace any runtime use of the label with `emergency_containment`; existing R5 decisions remain unchanged |
| `CF_MCP_OPERATOR` | Yes, as provider shorthand only | `restricted_operator_investigation` | D4 registrations bind this class and a separately registered restricted tool/MCP record | MellyCore operator only; no agent initiation; no service-account fallback; empty account/resource binding | R2 (D4 v1.0 remains R0) | **None** | Documentation/investigation only under Section 25 | **None** | Missing/multiple profiles, tool-registration mismatch, account binding, provider API attempt, or mutation attempt denies and audits | Migrate runtime-looking uses to `restricted_operator_investigation`; the label never authorizes Cloudflare account access |
| `credential_class: investigation` | Yes only as Registry-derived coarse descriptive metadata; not a Cloudflare requirement label | Produced only by `restricted_operator_investigation` | No runtime component interprets it; concrete D4 registration uses `required_credential_profile_class: restricted_operator_investigation` | MellyCore operator only under the restricted-tool record | R2 | **None** | Documentation/investigation only | **None** | Any use as a runtime selector or alias denies | Retire all standalone/runtime uses; retain only as derived non-authorizing metadata |

The projection is complete before Gateway resolution. No concrete capability
registration may retain two candidate canonical classes. Authorization records
bind to the selected canonical class, zero compatible profiles deny, multiple
compatible profiles deny, and no "best available credential" behavior exists.

### 11.2 Requirements (normative)

1. **Tenant-specific.** One profile instance per tenant. Never shared.
2. **Account/zone-scoped for provider API labels.** `CF_READ`,
   `CF_WRITE_CONTROLLED`, and `CF_CONTAIN` bind to the tenant's explicit
   allowlist. `CF_MCP_OPERATOR` instead requires an empty Cloudflare account,
   zone, and resource binding and cannot be reused for a provider API.
3. **Least privilege.** The minimum permission group that satisfies the
   capability, not the most convenient one.
4. **Read/write separation.** `CF_READ` must never carry an Edit permission.
   A read capability must never execute under a write credential — not for
   convenience, not to reduce token count, not during an approved mutation's
   own fresh-state read.
5. **Never in model context.** Credential material is resolved and applied
   outside any context the model can read. An agent may request an action; it
   may never see, receive, echo, or reconstruct the credential.
6. **Never in logs.** No raw token, key, `Authorization` header, or
   secret-shaped value in any audit entry, error, trace, proposal, approval
   record, or repository file. Audit records carry a **credential reference
   ID** only (Section 31).
7. **No widening.** A failure due to insufficient permission is a terminal,
   audited failure. Automatic escalation to a broader credential is
   prohibited.
8. **No Global API Key.** Cloudflare Global API Keys are prohibited wherever
   scoped API tokens are available (ADR §12, §17). No capability in this
   contract is permitted to use one.
9. **No cross-tenant fallback.** Prohibited outright (Section 15).
10. **Secrets boundary only.** Credentials are referenced through a secrets
    provider, never through repository files, `.env`, inline configuration,
    fixtures, or agent-visible config.
11. **Lifecycle metadata required.** Each profile declares owner, issuing
    identity, creation time, expiry, rotation interval, rotation due date,
    and revocation procedure. An expired or overdue profile is unusable for
    R3–R5 and downgrades to unavailable rather than being auto-renewed.
12. **Revocation is immediate and fail-closed.** On revocation, in-flight
    mutations abort at the next boundary, pending approvals bound to that
    profile are invalidated, and subsequent requests fail closed.

**No credential value, token example, account ID, zone ID, email address, or
secret-shaped placeholder appears anywhere in this contract**, per
`shared_context/SAFETY_CONTRACT.md`.

## 12. Capability naming rules

### 12.1 Grammar

```text
cloudflare.<area>[.<sub-area>].<resource>.<action>[.<qualifier>]
```

Lowercase, dot-separated, `snake_case` segments. Stable for the life of the
contract version. Rules:

1. **Stability over brevity.** An ID never changes to track a Cloudflare URL
   change; it names the capability, not the endpoint (Section 8.4 rule 3).
2. **Generation-explicit where generations differ.** Where Cloudflare has two
   generations of the same concept, the ID names the generation.
3. **One ID, one blast radius.** Two operations with materially different
   blast radius get different IDs even where Cloudflare exposes one endpoint.
4. **Proposal suffix.** `.propose` or `.diff`, or a `.report` terminal, marks
   a D2 capability that never executes.
5. **No wildcards.** `cloudflare.waf.rules.*` is not a capability. Wildcards
   appear only in Section 15's prohibition list, where they exclude a family.

### 12.2 Normalizations applied to the candidate names (documented)

The candidate names supplied by the task prompt were reviewed against
Cloudflare semantics, the repository's conventions, and duplicate/overlap
risk. Material changes:

| Candidate | Adopted ID | Reason |
| --- | --- | --- |
| `cloudflare.api_operations.*` | `cloudflare.endpoint_management.operations.*` | "API operations" is ambiguous with "API calls"; the resource belongs to Endpoint Management, whose lifecycle rules (Section 23) govern it. |
| `cloudflare.schemas.*` | `cloudflare.schema_validation.schemas.*` | Cloudflare has two schema generations; a bare `cloudflare.schemas.upload` would not say which. Directly implements Section 8.4 rule 1. |
| `cloudflare.schema_validation.global.set_*` | `cloudflare.schema_validation.zone_default.set_*` | Cloudflare's "global" default is **zone**-scoped. "Global" would misstate blast radius as account-wide. |
| `cloudflare.waf.rule.*.propose` (singular) | `cloudflare.waf.rules.*.propose` (plural) | The candidate list mixed singular `rule` in D2 with plural `rules` in D3 for the same resource. Normalized to plural. |
| `cloudflare.waf.rulesets.deploy` | `cloudflare.waf.entrypoint.execute_rule.add` | Cloudflare has no "deploy" verb. A custom ruleset becomes effective via an **execute rule in a phase entry-point ruleset** (Section 8.5). "Deploy" hid which object is mutated. `deploy` is retained as a documented alias. |
| `cloudflare.waf.rulesets.detach` | `cloudflare.waf.entrypoint.execute_rule.remove` | Same reason; `detach` retained as a documented alias. |
| — (new) | `cloudflare.schema_validation.zone_override.set_none` | Required by Section 21's mandatory emergency containment path; backed by the verified `validation_override_mitigation_action` field (Section 8.3). Absent from the candidate list. |
| — (new) | `cloudflare.shadow_endpoints.report` | Named in the D2 architectural boundary but omitted from the candidate list. |
| — (new) | `cloudflare.rate_limiting.propose` | Named in the D2 architectural boundary but omitted. Proposal-only; **no** corresponding mutation capability exists in v1.0. |
| — (new prohibitions) | `cloudflare.mcp.code_mode_execute`, `cloudflare.firewall.rules.*`, `cloudflare.filters.*`, `cloudflare.api_gateway.user_schemas.hosts.list` | Section 15. Code Mode covers 2,500+ endpoints behind one grant (Section 8.7) — the exact unrestricted-execute risk ADR §4 rejects. |

No candidate ID was silently dropped. `cloudflare.zones.get`,
`cloudflare.accounts.list`, `cloudflare.authentication_posture.findings.list`,
`cloudflare.security_events.search`, `cloudflare.audit_events.search`,
`cloudflare.endpoint_labels.bindings.diff`,
`cloudflare.endpoint_labels.bindings.replace`, and the `*.report` family are
adopted unchanged.

## 13. Capability matrix

### 13.0 Column key

Each capability declares the 25 required attributes. To keep the matrix
readable, common attributes are factored into per-domain **defaults**
(Sections 13.1.0, 13.2.0, 13.3.0, 13.4.0); per-capability rows state only
identity, scope, tier, and any deviation from those defaults. A defaulted
attribute is as binding as an inline one.

Attributes: (1) capability ID; (2) name; (3) domain; (4) Cloudflare API
family; (5) HTTP method class; (6) resource type; (7) account/zone scope;
(8) classification; (9) risk tier; (10) required MellyCore identity;
(11) provider-specific credential requirement label; (12) minimum Cloudflare permission; (13) data
classification; (14) prompt-injection exposure; (15) approval requirement;
(16) idempotency; (17) preconditions; (18) response normalization;
(19) audit fields; (20) read-after-write; (21) rollback/containment;
(22) rate-limit and retry; (23) pagination; (24) concurrency;
(25) failure outcome.

In addition to these 25 provider attributes, every concrete registration binds
exactly one Registry `required_credential_profile_class` under Section 11.1.1.
That canonical field, not attribute (11), is the sole Gateway resolution input.

### 13.1 Domain 1 — Cloudflare Security Inventory (read-only)

#### 13.1.0 D1 defaults

- **Classification:** read. **Method class:** `GET` only.
- **Identity:** tenant + (operator or agent). **Provider requirement label:**
  `CF_READ`. Each concrete registration selects `read_only_delegated` or
  `read_only_service` before runtime from its declared acting-identity mode.
- **Approval:** none required (policy-allowed per ADR §14 for R0/R1).
- **Idempotency:** naturally idempotent; no idempotency key required.
- **Preconditions:** tenant registered; `(account, zone)` on the allowlist;
  credential unexpired.
- **Response normalization:** provider payload mapped to a MellyCore
  envelope (Section 27); unknown fields preserved under a namespaced
  `provider_extra` and never promoted to typed fields.
- **Read-after-write:** not applicable.
- **Rollback:** not applicable — no state changes.
- **Rate limit / retry:** retry only on `429` and `5xx`, with exponential
  backoff plus jitter, a bounded attempt count, and respect for
  `Retry-After`. Never retry `4xx` other than `429`.
- **Pagination:** cursor/page parameters carried explicitly; every response
  declares whether it is complete or truncated; a truncated result is never
  presented as a complete inventory (Section 30).
- **Concurrency:** none required.
- **Failure outcome:** fail closed — return an explicit typed error. Never
  substitute an empty list for an error, and never treat a partial page as
  the full set.
- **Prompt-injection exposure:** every capability returning provider-authored
  text (host names, paths, labels, schema text, rule descriptions, event
  fields) is untrusted input under Section 26.

#### 13.1.1 D1 capabilities

| # | Capability ID | Cloudflare family | Scope | Resource | Tier | Data class | Injection exposure |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D1-01 | `cloudflare.accounts.list` | Accounts | account | Account | R0 | config metadata | low |
| D1-02 | `cloudflare.zones.list` | Zones | account | Zone | R0 | config metadata | low |
| D1-03 | `cloudflare.zones.get` | Zones | zone | Zone | R0 | config metadata | low |
| D1-04 | `cloudflare.endpoint_management.operations.list` | API Shield / Endpoint Management | zone | Operation | R1 | API surface topology | **high** — host/path strings |
| D1-05 | `cloudflare.endpoint_management.operations.get` | API Shield / Endpoint Management | zone | Operation | R1 | API surface topology | **high** |
| D1-06 | `cloudflare.endpoint_labels.list` | Endpoint labeling service | zone | Label | R0 | config metadata | medium — user-defined label text |
| D1-07 | `cloudflare.endpoint_labels.get` | Endpoint labeling service | zone | Label + bindings | R0 | config metadata | medium |
| D1-08 | `cloudflare.schema_validation.schemas.list` | Schema Validation 2.0 | zone | Schema | R1 | API surface topology | **high** |
| D1-09 | `cloudflare.schema_validation.schemas.get` | Schema Validation 2.0 | zone | Schema | R1 | API surface topology + schema body | **high** — full OpenAPI text |
| D1-10 | `cloudflare.schema_validation.settings.get` | Schema Validation 2.0 | zone | Settings | R1 | security posture | low |
| D1-11 | `cloudflare.schema_validation.operation_settings.list` | Schema Validation 2.0 | zone | Operation setting | R1 | security posture | low |
| D1-12 | `cloudflare.authentication_posture.findings.list` | API Shield / Authentication Posture | zone | Finding | R1 | security finding | medium |
| D1-13 | `cloudflare.waf.rulesets.list` | Rulesets API | account or zone | Ruleset | R1 | security control config | medium — descriptions |
| D1-14 | `cloudflare.waf.rulesets.get` | Rulesets API | account or zone | Ruleset + rules | R1 | security control config | **high** — expressions, descriptions |
| D1-15 | `cloudflare.security_events.search` | Security/Firewall Events | zone | Event | R1 | **security-sensitive; may contain request data** | **high** |
| D1-16 | `cloudflare.audit_events.search` | Audit Logs | account | Audit entry | R1 | **security-sensitive; actor identities** | **high** |

**D1-13/D1-14 note.** Account-scoped ruleset reads require an explicit
account-scope declaration and are the read counterpart of the elevated
account-level mutation risk in Section 22.

**D1-15/D1-16 note.** Both may surface personal or request-borne data.
Retention, redaction, and export of their results follow the tenant's data
classification policy; neither result set may be exported outside the
tenant's boundary by a D1 capability.

### 13.2 Domain 2 — Cloudflare API Shield Posture (proposal-only)

#### 13.2.0 D2 defaults

- **Classification:** proposal. **Risk tier: R2 for every D2 capability.**
- **Method class:** `GET` reads only. **A D2 capability never issues a
  write request of any kind** (ADR §14: R2 "produces a draft or proposed diff
  and stops — they never execute").
- **Identity:** tenant + (operator or agent). **Provider requirement label:**
  `CF_READ` only; the concrete registration selects one identity-specific read
  class before runtime. A D2 capability may not be issued a write credential.
- **Approval:** producing a proposal requires no approval; the proposal
  itself confers none.
- **Idempotency:** proposal generation is side-effect-free; regenerating
  produces a new proposal ID bound to a new state digest.
- **Preconditions:** a successful fresh D1 read of every resource the
  proposal touches, within the freshness window of Section 20.3.
- **Output contract:** every proposal carries proposal ID; tenant; account;
  zone; capability ID of the **intended** mutation; the exact target resource
  IDs; the exact before-state digest; the complete before/after diff; the
  risk tier the mutation would carry; the approval that would be required;
  an explicit blast-radius estimate; and the provenance of every input.
- **Rollback / read-after-write:** not applicable; nothing is written.
- **Failure outcome:** fail closed; an incomplete proposal is emitted as
  `INCOMPLETE` with the missing inputs named. A proposal is never completed
  by guessing a value.

#### 13.2.1 D2 capabilities

| # | Capability ID | Proposes | Target mutation capability | Tier |
| --- | --- | --- | --- | --- |
| D2-01 | `cloudflare.endpoint_management.operations.add.propose` | Adding operations to Endpoint Management | D3-01 | R2 |
| D2-02 | `cloudflare.endpoint_management.operations.delete.propose` | Deleting operations | D3-02 | R2 |
| D2-03 | `cloudflare.endpoint_labels.bindings.diff` | Label→operation binding change | D3-03 | R2 |
| D2-04 | `cloudflare.schema_validation.schemas.upload.propose` | Schema upload (non-enforcing) | D3-04 | R2 |
| D2-05 | `cloudflare.schema_validation.rollout.propose` | A staged rollout plan (Section 21) | D3-06…D3-13 | R2 |
| D2-06 | `cloudflare.schema_validation.operation_change.propose` | Per-operation mitigation change | D3-11…D3-13 | R2 |
| D2-07 | `cloudflare.waf.rules.create.propose` | New WAF custom rule | D3-19 | R2 |
| D2-08 | `cloudflare.waf.rules.update.propose` | WAF rule update | D3-20 | R2 |
| D2-09 | `cloudflare.waf.rules.reorder.propose` | WAF rule reordering | D3-21 | R2 |
| D2-10 | `cloudflare.waf.rules.delete.propose` | WAF rule deletion | D3-23 | R2 |
| D2-11 | `cloudflare.api_posture.report` | Authentication-posture report | — (report only) | R2 |
| D2-12 | `cloudflare.schema_coverage.report` | Schema-coverage report | — | R2 |
| D2-13 | `cloudflare.schema_drift.report` | Schema-drift report | — | R2 |
| D2-14 | `cloudflare.unprotected_endpoints.report` | Unprotected-endpoint report | — | R2 |
| D2-15 | `cloudflare.shadow_endpoints.report` | Shadow-endpoint report (discovered but unmanaged) | — | R2 |
| D2-16 | `cloudflare.rate_limiting.propose` | Rate-limiting recommendation | **none in v1.0** | R2 |

**D2-16 note.** No rate-limiting mutation capability exists in v1.0. The
proposal is advisory output for a human to apply outside MellyCore. Adding a
mutation counterpart requires a Section 38 amendment.

**D2-11 note.** Authentication Posture is read-only reporting on
Cloudflare's side (Section 8.6); this report never implies enforcement.
Acting on a `cf-missing-auth` finding requires a separate custom rule, which
is a D3 mutation.

### 13.3 Domain 3 — Cloudflare Protection Changes (approval-required)

#### 13.3.0 D3 defaults

- **Classification:** mutation. **Every D3 capability requires explicit
  human approval** (ADR §8 sets an R4 minimum for the Cloudflare operations
  listed there; no D3 capability in this contract falls below R4).
- **Identity:** tenant + MellyCore operator as approver; an agent may request
  but never approve. **Provider requirement label:** `CF_WRITE_CONTROLLED`
  projecting to `controlled_write` (or `CF_CONTAIN` projecting to
  `emergency_containment` for the containment subset, Section 33.3).
- **Minimum Cloudflare permission:** the narrowest Edit group that covers the
  capability — API Gateway Edit for Endpoint Management, labels, and Schema
  Validation; WAF/Rulesets Edit for Rulesets capabilities (Section 8.7).
- **Preconditions (all mandatory, in order):** (a) a fresh D1 read within
  the Section 20.3 freshness window; (b) a D2 proposal with a complete
  before/after diff; (c) a policy decision; (d) an approval bound to that
  exact proposal ID and before-state digest; (e) a concurrency precondition
  (Section 20); (f) an idempotency key (Section 19).
- **Idempotency:** required; see Section 19.
- **Concurrency:** required; see Section 20.
- **Read-after-write:** **mandatory and non-optional** for every D3
  capability; see Section 32.
- **Audit:** the full Section 31 record, plus the R5 enhancements of
  Section 31.3 where applicable.
- **Rate limit / retry:** a failed mutation is **never** blindly retried.
  See Section 29.2.
- **Failure outcome:** fail closed and fail visibly. A failed, unverifiable,
  or partially applied mutation is reported as a failure with its exact
  partial state; it is never reported as success, never silently
  compensated, and never substituted with a different action or credential.

#### 13.3.1 D3 capabilities

| # | Capability ID | Cloudflare family | Scope | Method class | Tier | Escalation |
| --- | --- | --- | --- | --- | --- | --- |
| D3-01 | `cloudflare.endpoint_management.operations.add` | Endpoint Management | zone | `POST` | R4 | — |
| D3-02 | `cloudflare.endpoint_management.operations.delete` | Endpoint Management | zone | `DELETE` | **R5** | irreversible metric loss (Section 23) |
| D3-03 | `cloudflare.endpoint_labels.bindings.replace` | Endpoint labeling | zone | `PUT`/`PATCH` | R4 | → R5 if net removals ≥ tenant threshold (Section 24) |
| D3-04 | `cloudflare.schema_validation.schemas.upload` | Schema Validation 2.0 | zone | `POST` | R4 | — (uploaded non-enforcing, Section 21) |
| D3-05 | `cloudflare.schema_validation.schemas.delete` | Schema Validation 2.0 | zone | `DELETE` | **R5** | destructive; Section 33.2 |
| D3-06 | `cloudflare.schema_validation.schemas.enable` | Schema Validation 2.0 | zone | `PATCH` | R4 | → R5 if zone default is `block` |
| D3-07 | `cloudflare.schema_validation.schemas.disable` | Schema Validation 2.0 | zone | `PATCH` | R4 | protection-removing; Section 33.4 |
| D3-08 | `cloudflare.schema_validation.zone_default.set_none` | Schema Validation 2.0 | zone | `PUT`/`PATCH` | R4 | protection-removing |
| D3-09 | `cloudflare.schema_validation.zone_default.set_log` | Schema Validation 2.0 | zone | `PUT`/`PATCH` | R4 | — |
| D3-10 | `cloudflare.schema_validation.zone_default.set_block` | Schema Validation 2.0 | zone | `PUT`/`PATCH` | **R5** | zone-wide block — always R5 (Section 21.4) |
| D3-11 | `cloudflare.schema_validation.operation.set_none` | Schema Validation 2.0 | zone/operation | `PUT` | R4 | protection-removing |
| D3-12 | `cloudflare.schema_validation.operation.set_log` | Schema Validation 2.0 | zone/operation | `PUT` | R4 | — |
| D3-13 | `cloudflare.schema_validation.operation.set_block` | Schema Validation 2.0 | zone/operation | `PUT` | R4 | **→ R5** when the endpoint is tenant-critical, or observation evidence (Section 21.3) is absent or below threshold |
| D3-14 | `cloudflare.schema_validation.zone_override.set_none` | Schema Validation 2.0 | zone | `PATCH` | R4 | emergency containment lever (Section 33.3) |
| D3-15 | `cloudflare.waf.rulesets.create` | Rulesets API | account or zone | `POST` | R4 | → R5 if account-scoped |
| D3-16 | `cloudflare.waf.rulesets.update` | Rulesets API | account or zone | `PUT` | R4 | → R5 per Section 22.3 |
| D3-17 | `cloudflare.waf.entrypoint.execute_rule.add` (alias: `deploy`) | Rulesets API — phase entry point | account or zone | `PUT` | **R5** | makes a ruleset live on traffic |
| D3-18 | `cloudflare.waf.entrypoint.execute_rule.remove` (alias: `detach`) | Rulesets API — phase entry point | account or zone | `PUT` | **R5** | removes protection |
| D3-19 | `cloudflare.waf.rules.create` | Rulesets API | account or zone | `POST` | R4 | → R5 if action is `block` or scope is account |
| D3-20 | `cloudflare.waf.rules.update` | Rulesets API | account or zone | `PATCH` | R4 | → R5 per Section 22.3 |
| D3-21 | `cloudflare.waf.rules.reorder` | Rulesets API | account or zone | `PUT` | R4 | → R5 if a blocking rule moves earlier or crosses an allow/skip rule |
| D3-22 | `cloudflare.waf.rules.disable` | Rulesets API | account or zone | `PATCH` | R4 | → R5 if the rule is protective |
| D3-23 | `cloudflare.waf.rules.delete` | Rulesets API | account or zone | `DELETE` | **R5** | destructive; requires a stored rollback representation |

**Rule 13.3.2 — escalation is one-way.** An escalation condition raises the
tier; nothing lowers it. A capability that escalates to R5 acquires R5's
strict preconditions, exact resource enumeration (no wildcard or implicit
scope), and enhanced audit for that specific execution.

**Rule 13.3.3 — no R3 in v1.0.** No Cloudflare mutation in scope is
classified R3. ADR §8 places every operation in this domain at an R4
minimum, and none of them is reliably reversible without a separately
approved compensating mutation. Classifying any of them R3 — thereby making
approval merely policy-dependent — would contradict the ADR.

### 13.4 Domain 4 — Cloudflare Operator Investigation

#### 13.4.0 D4 defaults

- **Classification:** read (documentation scope only in v1.0).
- **Identity:** MellyCore **operator only**. No autonomous agent may initiate a
  D4 session. **Provider requirement label:** `CF_MCP_OPERATOR`, projecting to
  `restricted_operator_investigation`; it carries no Cloudflare account grant
  in v1.0 and authorizes no provider API.
- **Approval:** operator initiation is the authorization; the session
  confers no capability outside its allowlist.
- **Output:** untrusted (Section 26), size-bounded, provenance-stamped, and
  never elevated into policy, proposal input, or approval evidence without a
  D1/D2 re-derivation from the authorized read path.
- **Audit:** full session transcript metadata retained per Section 31.4.

#### 13.4.1 D4 capabilities

| # | Capability ID | Purpose | Tier | Account access |
| --- | --- | --- | --- | --- |
| D4-01 | `cloudflare.docs.search` | Official Cloudflare documentation search | R0 | none |
| D4-02 | `cloudflare.api_surface.discover` | Documentation-derived capability/path verification per Section 8.4 rule 3 | R0 | none |
| D4-03 | `cloudflare.mcp.documentation_session` | Bounded, operator-visible, documentation-scoped MCP session | R0 | **none in v1.0** |

### 13.5 Counts

| Classification | Count | Tier distribution |
| --- | --- | --- |
| Read-only (D1) | 16 | R0 × 5, R1 × 11 |
| Proposal-only (D2) | 16 | R2 × 16 |
| Approval-required mutation (D3) | 23 | R4 × 17, R5 × 6 (before escalation) |
| Operator investigation (D4) | 3 | R0 × 3 |
| **Total defined** | **58** | R0 × 8, R1 × 11, R2 × 16, R3 × 0, R4 × 17, R5 × 6 |
| Explicitly prohibited | 13 | n/a — never executable |

## 14. Risk tiers

The R0–R5 tiers of ADR §13 are reused verbatim and are not redefined here.

| Tier | Meaning | Required behavior | Cloudflare examples |
| --- | --- | --- | --- |
| R0 | Passive metadata | May be policy-allowed read-only | zone list, label list, docs search |
| R1 | Sensitive read | May be policy-allowed read-only | ruleset detail, security events, audit events |
| R2 | Draft or proposal | Generates a diff, never executes | every D2 capability |
| R3 | Reversible mutation | Policy evaluation; approval per tenant policy | **none in v1.0** (Section 13.3.3) |
| R4 | Consequential mutation | Explicit human approval | schema upload, per-operation `log`, rule create |
| R5 | Critical or potentially destructive | Explicit human approval, strict preconditions, exact resource enumeration, enhanced audit | zone-wide `block`, entry-point changes, rule/operation/schema deletion |

## 15. Explicitly prohibited capabilities

The following are **never executable** by any identity, at any tier, under
any approval. They are enumerated so that a request naming one is recognized
and denied rather than silently unsupported. An attempt is an audited
security event (Section 31.5).

| # | Prohibited ID | Why |
| --- | --- | --- |
| P-01 | `cloudflare.mcp.unrestricted_execute` | ADR §4, §17 — unrestricted MCP execution is rejected. |
| P-02 | `cloudflare.mcp.code_mode_execute` | Cloudflare's Code Mode server spans 2,500+ endpoints behind one OAuth grant (Section 8.7) — unbounded search-and-execute by construction. |
| P-03 | `cloudflare.global_api_key.use` | ADR §12, §17 — Global API Keys prohibited where scoped tokens exist. |
| P-04 | `cloudflare.cross_tenant_credential_fallback` | Section 9.1; ADR §10 — cross-tenant access fails closed. |
| P-05 | `cloudflare.zone_wide_block.unapproved` | Section 21.4 — zone-wide `block` is R5 and always requires explicit approval. |
| P-06 | `cloudflare.bulk_delete.unenumerated` | R5 requires exact resource enumeration; no wildcard or implicit-scope deletion. |
| P-07 | `cloudflare.waf.ruleset.replace_without_diff` | Section 22.2 — wholesale replace without a complete diff. |
| P-08 | `cloudflare.schema_validation.block_without_observation` | Section 21.3 — `block` without an observation period and its evidence. |
| P-09 | `cloudflare.audit_suppression` | Section 31 — no execution path may omit, disable, downgrade, or defer its audit record. |
| P-10 | `cloudflare.read_after_write.skip` | Section 32 — read-after-write is mandatory for every mutation. |
| P-11 | `cloudflare.firewall.rules.*` (entire family) | Section 7 — legacy Firewall Rules API. |
| P-12 | `cloudflare.filters.*` (entire family) | Section 7 — legacy Filters API. |
| P-13 | `cloudflare.api_gateway.user_schemas.hosts.list` | Section 7; ADR §8 — excluded legacy surface. |

**Rule 15.1.** This list is not exhaustive of everything forbidden. Anything
not defined in Section 13 is **not** a MellyCore Cloudflare capability and
is unavailable by default. The connector is an allowlist, not a denylist.

## 16. Read-only contract

1. A read capability never issues a write request, never uses a write
   credential, and never has a side effect on Cloudflare state.
2. A read result is **evidence with a timestamp**, not current truth. Every
   normalized read carries an observation time and a state digest.
3. A read that is truncated, partially paginated, rate-limited, or degraded
   is labeled as such and must not be presented as a complete inventory.
   "No results" and "could not determine" are distinct outcomes and must
   never be merged.
4. Read results never elevate into policy, approval evidence, or trusted
   instruction (Section 26).
5. A stale read may not satisfy a mutation precondition; freshness is
   enforced by Section 20.3.

## 17. Proposal-only contract

1. A proposal **is not an authorization**. It records what a mutation would
   do; it never performs it and never pre-authorizes it.
2. A proposal is bound to an exact before-state digest of every resource it
   touches. If that state changes, the proposal is invalid (Section 20.2).
3. A proposal must name the mutation capability ID it targets, that
   capability's risk tier, and the approval it would require — so an approver
   sees blast radius before consenting, not after.
4. A proposal must present **complete** diffs. For any replacement operation
   it must show added, removed, and unchanged resources (Sections 22.2, 24).
5. A proposal must state its own completeness. Missing inputs are named;
   they are never inferred, defaulted, or filled from provider text.
6. Proposals expire. An expired proposal cannot be approved or executed.

### 17.1 Consequential operations (from ADR §8, binding)

All of the following are consequential and carry an R4 minimum: adding or
deleting managed API operations; replacing label bindings; uploading,
activating, or deleting schemas; changing Schema Validation actions; setting
validation to `block`; creating, updating, reordering, or deleting WAF
rules; changing rate-limiting or access-control policy. Section 13.3
classifies each at or above that minimum.

## 18. Approval rules

1. **R0/R1** — may be policy-allowed without per-call human approval.
2. **R2** — no approval to generate; the output is a draft and executes
   nothing.
3. **R3** — no R3 Cloudflare capability exists in v1.0.
4. **R4** — always requires explicit human approval.
5. **R5** — always requires explicit human approval **plus** strict
   preconditions, exact resource enumeration (no wildcard, no implicit
   scope), and enhanced audit.

**Rule 18.1 — approvals are singular and non-standing.** An approval
authorizes exactly the action it names: one capability ID, one tenant, one
account, one zone, one enumerated resource set, one proposal ID, one
before-state digest. It is never blanket, standing, batch, or future
authorization. This mirrors the per-merge, non-blanket pattern already
canonical in this repository (`shared_context/PROJECT_STATE.md`, "Production
Deployment Authorization — Model A Contract").

**Rule 18.2 — approval binding.** An approval that does not carry a matching
proposal ID and before-state digest is invalid. Execution recomputes the
digest immediately before the write; a mismatch aborts (Section 20.2).

**Rule 18.3 — no self-approval.** An agent or runtime identity may request
but never approve. The approver is a MellyCore operator identity.

**Rule 18.4 — approval lifecycle.** Approvals use the repository's existing
approval dimension (`[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]`
§8): `not_required`, `awaiting_approval`, `approved`, `rejected`, `expired`,
`revoked`. Approvals expire; an expired or revoked approval never executes.

**Rule 18.5 — approval view is complete.** An approver must see: tenant;
account; zone; capability ID; risk tier; exact resource IDs; before state;
after state; the complete diff including unchanged items for replacements;
blast-radius estimate; the rollback representation that will be stored; and
the provenance of the proposal. An approval collected on a partial view is
invalid.

**Rule 18.6 — emergency containment.** Containment actions (Section 33.3)
still require approval; they may use an expedited path with a reduced
approver set defined by tenant policy, but never a bypass. The absence of an
available approver blocks the action; it does not auto-approve it.

## 19. Idempotency rules

1. Every D3 execution carries an **idempotency key** derived from: tenant,
   account, zone, capability ID, enumerated resource IDs, proposal ID, and
   before-state digest. The key is stable across retries of the same intended
   action and different for any different intended action.
2. A replayed key with an already-recorded terminal outcome returns that
   recorded outcome. It does not re-execute.
3. A key whose recorded attempt is **in flight** blocks re-execution and
   surfaces the in-flight state. It never races a duplicate write.
4. A key whose recorded attempt ended **indeterminate** (timeout, transport
   failure, ambiguous response) does **not** permit blind retry. It requires
   a fresh read to establish actual provider state, then a new proposal and
   approval if state moved (Section 29.2).
5. Cloudflare provides no universal idempotency-key header across these API
   families; MellyCore-side keys are therefore the authoritative mechanism,
   supplemented by the concurrency preconditions of Section 20.
6. Read and proposal capabilities require no idempotency key.

## 20. Concurrency and stale-state rules

### 20.1 Version preconditions

Every ruleset modification creates a new ruleset version (Section 8.5). A
D3 Rulesets mutation must therefore carry the expected ruleset version or
equivalent concurrency token observed in the fresh read that produced the
proposal. If the provider's current version differs at execution time, the
mutation **aborts**; it is not force-applied.

### 20.2 State-digest precondition

For every D3 capability — including those whose Cloudflare family exposes no
version field — the connector computes a **before-state digest** over the
exact resources in scope, at proposal time. Immediately before the write it
recomputes the digest from a fresh read. A mismatch aborts with an audited
`STALE_STATE` failure, invalidates the proposal and its approval, and
requires a new proposal, a new diff, and a new approval.

### 20.3 Freshness window

Each capability declares a maximum permitted age for the fresh read backing
its proposal. A proposal whose backing read exceeds that window is stale and
non-executable. Defaults: R4 — 15 minutes; R5 — 5 minutes. Tenant policy may
shorten but never lengthen these.

### 20.4 Serialization

Concurrent MellyCore mutations against the same ruleset, zone Schema
Validation settings object, or label are serialized per resource. Cloudflare
explicitly advises against concurrent updates to the same ruleset
(Section 8.5); the connector must not generate them, and must not work
around a lost race by retrying with force.

### 20.5 Propagation delay

Cloudflare configuration changes propagate asynchronously. Read-after-write
(Section 32) confirms the **control-plane** state. It does not prove
edge-wide enforcement. Traffic-effect claims require the observation period
of Section 21.3, not a successful write response. A successful write must
never be reported as "protection is now active at the edge."

## 21. Schema Validation rollout contract (mandatory staging)

No `block` action may be reached by any shorter path. The seventeen stages
below are ordered and each must complete before the next begins.

### 21.1 Stages

| # | Stage | Capability | Gate |
| --- | --- | --- | --- |
| 1 | Inventory current schemas and operations | D1-08, D1-11, D1-04 | Complete, non-truncated inventory |
| 2 | Identify Endpoint Management coverage | D1-04, D1-05 | Every schema operation mapped to an Endpoint Management operation or explicitly listed as uncovered |
| 3 | Produce exact coverage and conflict report | D2-12, D2-13, D2-15 | Report is complete; conflicts enumerated, not summarized |
| 4 | Upload schema **inactive / non-enforcing** | D3-04 | Approval; upload must not enable validation |
| 5 | Validate parse diagnostics | D1-09 | Zero parse errors; warnings enumerated |
| 6 | Add or verify required operations | D3-01 (if needed) | Approval per operation set; Section 23 preconditions |
| 7 | Start at mitigation action `none` | D3-08 / D3-11 | Confirmed `none` before any enabling step |
| 8 | Move selected operations, or the zone default, to `log` | D3-12 / D3-09 | Approval; `log` only, never straight to `block` |
| 9 | Send or observe representative traffic | — (tenant-side) | Traffic volume meets Section 21.3 minimum |
| 10 | Review Security Events and HTTP response impact | D1-15 | Evidence collected and retained |
| 11 | Propose endpoint-specific `block` | D2-06 | Complete proposal with observation evidence attached |
| 12 | Obtain explicit human approval | — | Section 18; R4 or R5 per Section 13.3.1 |
| 13 | Apply **endpoint-specific** `block` | D3-13 | Never zone-wide at this stage |
| 14 | Verify read-after-write state | D1-11 | Section 32 |
| 15 | Observe production impact | D1-15 | Section 21.3 metrics within thresholds |
| 16 | Expand only through a separate approved change | new proposal | No implicit expansion of scope |
| 17 | Preserve an emergency `none` containment path | D3-14 / D3-11 | Verified reachable **before** stage 13 |

**Rule 21.1.1.** Stage 17 is a precondition of stage 13, not a follow-up:
the containment path must be proven reachable before the first `block` is
applied. If containment cannot be demonstrated, `block` is not authorized.

**Rule 21.1.2.** Schema Validation protects only operations present in
Endpoint Management (Section 8.2). A rollout that reaches `block` while
material operations are uncovered is misleading about its own coverage; the
coverage gap must be stated in the approval view (Rule 18.5).

### 21.2 Observation period — required evidence

Stages 9–10 and 15 each require, before the next stage may proceed:

- a minimum observation duration and a minimum request volume per affected
  operation, both set by tenant policy and both recorded;
- counts of schema-validation `log` events per operation;
- the false-positive rate: `log` events on requests the tenant confirms are
  legitimate;
- the affected-endpoint HTTP status distribution before and after;
- the error-rate delta attributable to the change;
- the exact evidence identifiers (event query, time window, zone) so the
  evidence is re-derivable.

Absent evidence is **not** passing evidence. An observation stage whose
minimum volume was not met records `INSUFFICIENT_OBSERVATION` and blocks
progression; it never defaults to a pass. This mirrors the repository's
existing rule that a validator which did not run records `NOT_RUN`, never a
defaulted pass.

### 21.3 Acceptable thresholds and rollback trigger

Tenant policy sets numeric thresholds; this contract fixes their **shape**
and their fail-closed default:

- a maximum tolerated false-positive rate;
- a maximum tolerated increase in 4xx responses on affected endpoints;
- a maximum tolerated error-rate delta;
- a minimum observation duration and request volume.

**Rollback trigger.** Any threshold breach, or any inability to measure a
threshold, triggers containment: revert the affected operations to `none`
(D3-11) or, if scope is unclear or the breach is zone-wide, apply the
zone-wide override to `none` (D3-14). Containment is triggered on
*inability to measure*, not only on measured harm.

### 21.4 Tiering of `block`

- **Zone-wide `block` (D3-10) is R5, always**, without exception or
  downgrade.
- **Endpoint-specific `block` (D3-13) is R4 minimum**, escalating to R5 when
  the endpoint is tenant-critical or when Section 21.2 evidence is absent or
  below threshold.
- No `block` capability may execute without the observation evidence of
  Section 21.2 — enforced as prohibition P-08.

### 21.5 Emergency override semantics

`cloudflare.schema_validation.zone_override.set_none` (D3-14) sets the
verified zone-level `validation_override_mitigation_action` to `none`,
which overrides both zone-level and per-operation actions (Section 8.3).

- It is **containment only**: it may reduce enforcement, never increase it.
  A capability that *sets* the override to `log` or `block` is deliberately
  not defined in v1.0.
- It still requires approval (Rule 18.6), on an expedited path if tenant
  policy defines one.
- It is loud: applying it raises an audited containment event and must be
  surfaced, because it silently neutralizes per-operation settings that
  remain configured. Leaving it set is a standing posture regression and
  must be tracked to explicit removal.
- Removing the override restores the underlying per-operation actions and is
  therefore an enforcement-increasing change requiring its own proposal and
  approval.

### 21.6 Propagation-delay handling

Between stages 13 and 15 the connector must not claim enforcement is
complete. Read-after-write confirms configuration; only Section 21.2
evidence over the observation window supports a claim about traffic.

## 22. WAF Rulesets safety model

### 22.1 Required understanding before any mutation

A Rulesets mutation proposal must resolve and display: account vs zone
scope; ruleset ID; ruleset `kind` (`root` / `zone` / custom / managed);
phase; whether the target is a phase **entry-point** ruleset; the current
ruleset version; rule IDs; rule order; each rule's expression, action, and
enabled state; and each rule's description and MellyCore provenance marker.

### 22.2 Required preconditions

Before any D3 Rulesets execution:

1. a fresh read of the exact ruleset (D1-14);
2. exact ruleset and rule IDs — never a name, index, or pattern match;
3. the expected ruleset version or equivalent concurrency token
   (Section 20.1);
4. a **complete** before/after diff — never a desired end state alone;
5. a **rule-order diff** showing every position change, not only moved rules;
6. an **expression diff** with an explicit narrower/equivalent/broader
   judgment;
7. an **action diff**;
8. a **scope diff** (account vs zone; phase; entry point vs custom);
9. an estimated traffic impact with its basis stated;
10. explicit approval (Section 18);
11. read-after-write verification (Section 32).

Cloudflare advises updating an entire ruleset in a single operation
(Section 8.5); where the connector does so, the diff obligation applies to
the **whole submitted ruleset**, not merely to the rules the operator
intended to change. Rules unintentionally carried, dropped, or reordered by
a whole-ruleset write must appear in the diff. Prohibition P-07 forbids a
wholesale replace without this.

### 22.3 High-risk changes (escalate to R5)

- changing a rule's action to `block`;
- broadening a rule expression;
- moving a blocking rule earlier in the order;
- changing an allow/skip relationship, or moving a rule across one;
- deploying a previously inactive ruleset — i.e. adding an execute rule to a
  phase entry point (D3-17);
- detaching a protective ruleset — removing that execute rule (D3-18);
- any change to an **account-level** ruleset, whose blast radius spans every
  zone in the account;
- bulk replacement of a ruleset's rule list;
- deleting a rule without a stored rollback representation — which is
  prohibited outright by Rule 33.2.

### 22.4 Provenance

Every MellyCore-created or MellyCore-modified rule carries a provenance
marker in its description identifying MellyCore, the tenant, the capability
ID, and the approval ID — so an operator inspecting Cloudflare directly can
attribute the change without consulting MellyCore. The marker contains no
credential, token, personal data, or internal URL.

## 23. Endpoint Management safety model

Adding or deleting an operation is **not** harmless metadata maintenance.
Verified downstream effects (Section 8.6): persisted API profiles, risk
findings, and profile learning / performance-analysis data collection all
depend on an operation being present in the `full` state, and on deletion
"its previous historical metrics cannot be restored."

Additionally affected, per the ADR and this contract: Schema Validation
enforcement scope; authentication-posture findings and labels; endpoint
analytics; API Discovery state; label bindings; rate-limiting
recommendations; and every downstream posture report in D2.

### 23.1 Preconditions for deletion (D3-02, R5)

1. **Dependency lookup** — every Schema Validation setting, label binding,
   schema operation reference, and posture finding referencing the
   operation, enumerated exactly.
2. **Affected-feature list** — the concrete features that stop functioning,
   including irreversible loss of historical metrics, presented in the
   approval view.
3. **Exact operation ID** — never a method/host/path pattern match at
   execution time.
4. **Method, hostname pattern, and path pattern confirmation** — the triple
   that identifies the operation (Section 8.6), displayed and confirmed.
5. **Traffic evidence** — recent request volume for the operation, so a
   live endpoint is not deleted as if dormant. Absent traffic data is
   recorded as unknown and **blocks** deletion; it is not read as zero.
6. **Explicit approval** at R5, with exact resource enumeration.
7. **Read-after-write verification** that exactly the enumerated operations,
   and no others, were removed.

### 23.2 Preconditions for addition (D3-01, R4)

An added operation immediately falls under the zone's default mitigation
action. If that default is `log` or `block`, adding an operation changes
live traffic handling. The approval view must state the current zone default
and the resulting enforcement, and the capability escalates accordingly. An
operation must never be added "just to inventory it" while the zone default
is `block`.

## 24. Label-replacement safety model

Replacement operations must **never** display only the desired final set.
The approval view for `cloudflare.endpoint_labels.bindings.replace` (D3-03)
must show:

1. resources **added**;
2. resources **removed**;
3. resources **unchanged**;
4. **missing or invalid operation IDs** in the requested set, named
   individually;
5. the **current** binding count;
6. the **resulting** binding count;
7. tenant, Cloudflare account, and zone;
8. label identity, and whether the label is **managed** or **user-defined**;
9. the source of the proposal — which D2 capability produced it, from which
   read, at what time.

**Rule 24.1 — fail on drift.** Execution fails if the current binding set
differs from the set the approval was computed against (Section 20.2). It is
never reconciled silently.

**Rule 24.2 — managed labels are read-only.** Cloudflare-applied managed
labels (e.g. `cf-log-in`, `cf-purchase`, `cf-risk-missing-auth`) are treated
as read-only in v1.0. Only user-defined label bindings are eligible for
D3-03. Whether managed labels are API-editable is an open verification item
(Section 8.8); the fail-safe reading is adopted until verified.

**Rule 24.3 — replacement is assumed wholesale.** Until verified
(Section 8.8), label binding is assumed to be replacement semantics — the
riskier reading — so the full add/remove/unchanged diff is mandatory. If it
is later verified to be additive, that does not relax Rule 24.1.

**Rule 24.4 — net-removal escalation.** A replacement whose net removals
meet or exceed the tenant's bulk threshold escalates to R5 (Section 13.3.1),
because removing risk or ownership labels degrades posture reporting
silently.

## 25. MCP restrictions

### 25.1 Decision (v1.0): documentation-only

Cloudflare MCP use is permitted in v1.0 **only** as a documentation-scoped,
operator-initiated, read-only session (D4-03). This is the narrowest
defensible option and is consistent with ADR §4, which *permits* restricted
MCP-assisted investigation without requiring it.

| MCP use | v1.0 status |
| --- | --- |
| Documentation search / API-surface discovery | **Permitted** under Section 25.2 |
| Read-only investigation against a Cloudflare account | **Specified but not authorized** — requires a Section 38 amendment |
| Proposal generation from MCP output | **Not permitted** — proposals derive only from D1 reads |
| Approval-gated mutation via MCP | **Permanently prohibited** under this contract |

Rationale: Cloudflare's Code Mode MCP server spans the entire Cloudflare API
(2,500+ endpoints) behind a single OAuth grant (Section 8.7). That is the
unrestricted search-and-execute shape ADR §4 and §17 reject. Narrowing to
documentation scope means the MCP path holds no account grant at all, so
there is no credential to over-scope and no mutation reachable by
misconfiguration rather than by decision.

### 25.2 Conditions (all must hold simultaneously)

1. operator-initiated session — never agent-initiated, never background;
2. tenant explicitly selected;
3. provider requirement label `CF_MCP_OPERATOR` projected before runtime to
   `required_credential_profile_class: restricted_operator_investigation`;
4. capability allowlist applied — the session may reach only D4 capabilities;
5. read-only by default, with no write method reachable;
6. bounded execution envelope — call count, duration, and concurrency capped;
7. bounded response size, with truncation labeled, never silently dropped;
8. output treated as untrusted (Section 26);
9. complete audit trail preserved (Section 31.4);
10. dangerous generic methods blocked — no arbitrary request execution, no
    raw path passthrough, no code execution, no credential-bearing call;
11. **no autonomous unrestricted search-and-execute**, in any form.

### 25.3 Non-substitution

MCP output never substitutes for an authorized read. A proposal, approval,
audit record, or verification step must derive from D1 capabilities on the
authorized read path. MCP may inform an operator; it may not supply
evidence.

## 26. External-content and prompt-injection handling

Per ADR §16, all Cloudflare-sourced content is **untrusted external input**.
Cloudflare-specific carriers, all attacker-influenceable in whole or part:

- hostnames and path patterns in Endpoint Management and API Discovery;
- OpenAPI/JSON schema text, including `description`, `title`, `example`,
  `summary`, and extension fields;
- user-defined label names and descriptions;
- WAF rule descriptions and expressions;
- security-event fields, including request-derived values, user agents,
  headers, and URIs;
- audit-log actor and resource fields;
- error messages and provider documentation returned through tools;
- any MCP or webhook payload.

### 26.1 Rules

1. **Data, never instruction.** Provider content is never interpreted as an
   instruction, however phrased and whoever it claims to be from. Text
   inside a schema description claiming operator authority, prior approval,
   or system origin is data.
2. **Structural separation.** Provider content is carried in clearly
   delimited data fields, never concatenated into instruction context.
3. **Provenance preserved.** Every field retains source, capability ID,
   observation time, and zone.
4. **Sanitize and normalize.** Control characters, homoglyph and
   bidirectional-override sequences, embedded markup, and nested
   delimiters are neutralized before rendering or storage.
5. **Size bounds.** Output is capped; truncation is explicit and labeled.
6. **Schema validation.** Responses are validated against expected shapes;
   unexpected fields are preserved under `provider_extra` and never promoted
   to typed fields (Section 27).
7. **No policy elevation.** No provider content may create, modify, relax,
   or satisfy a MellyCore policy, approval, capability grant, allowlist
   entry, or safety rule.
8. **No provider-sourced targeting.** A mutation target never originates
   from provider free text. Targets are exact IDs from an authorized read,
   confirmed in the approval view.
9. **Injection attempts are events.** Content that attempts instruction
   injection is recorded as a security observation (Section 31.5) with the
   offending content quoted as inert data, and surfaced to the operator.

## 27. Normalized response envelopes

Every capability returns a MellyCore envelope. Provider payloads are never
passed through raw.

| Field | Meaning |
| --- | --- |
| `capability_id` | The capability that produced this result |
| `tenant_ref` | Tenant identifier reference |
| `account_ref` / `zone_ref` | Cloudflare scope references (references, never raw IDs in logs) |
| `observed_at` | Observation timestamp |
| `state_digest` | Digest over the normalized resource set |
| `completeness` | `complete` \| `truncated` \| `partial` \| `unknown` |
| `pagination` | Cursor state and whether more pages exist |
| `items` | Normalized, typed resources |
| `provider_extra` | Unrecognized provider fields, namespaced and untyped |
| `provenance` | Source capability, credential reference ID, request correlation ID, provider request ID |
| `trust` | Always `untrusted_provider_content` for provider-authored text |
| `evidence_class` | `future_live` until an implementation exists |
| `warnings` | Non-fatal anomalies, explicitly enumerated |

**Rule 27.1.** An absent value is `null` with a reason. Zero never stands in
for unknown or unmeasured — the repository's existing truthfulness rule
(`[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` §1.5) applied to provider
data.

**Rule 27.2.** `completeness` is mandatory. A caller that ignores it is
non-conforming; a `truncated` result may not back a proposal that claims
full coverage.

## 28. Error taxonomy

| Class | Meaning | Retry? | Outcome |
| --- | --- | --- | --- |
| `AUTHZ_DENIED_MELLYCORE` | MellyCore policy, tenant, or allowlist denial | No | Fail closed; audited |
| `AUTHZ_DENIED_PROVIDER` | Cloudflare rejected the credential's permission | No | Fail closed; **never** retried with a broader credential |
| `APPROVAL_MISSING` / `APPROVAL_INVALID` / `APPROVAL_EXPIRED` | Section 18 violation | No | Abort before any request |
| `STALE_STATE` | Digest or version precondition failed | No | Abort; new proposal + approval required |
| `PRECONDITION_UNMET` | A Section 13.3.0 precondition absent | No | Abort |
| `LEGACY_SURFACE_REFUSED` | An excluded family was requested | No | Refuse; audited security event |
| `RATE_LIMITED` | Cloudflare `429` | Yes, bounded | Backoff with `Retry-After` |
| `PROVIDER_UNAVAILABLE` | Cloudflare `5xx` / transport failure | Reads yes; **mutations see `INDETERMINATE`** | Section 29.2 |
| `INDETERMINATE` | Mutation outcome unknown (timeout, ambiguous response) | **No blind retry** | Fresh read to establish truth; Section 29.2 |
| `VERIFICATION_FAILED` | Read-after-write did not match | No | Report failure; containment assessment (Section 33) |
| `PARTIAL_APPLICATION` | Some enumerated resources changed, others not | No | Report exact partial state; never claim success |
| `SCHEMA_UNEXPECTED` | Response shape not as contracted | No | Fail closed; do not guess |
| `INJECTION_SUSPECTED` | Section 26.1 rule 9 | n/a | Record, surface, continue treating as data |

**Rule 28.1 — no silent degradation.** No error class may be converted into
an empty success, a narrower action, a different credential, or a
lower-visibility notification. Per ADR §9, a failed critical alert must
surface as a failure and must not degrade to a lower-visibility channel.

## 29. Rate limiting and retries

### 29.1 Reads

Retry only `429` and `5xx`, with exponential backoff, jitter, a bounded
attempt count, and `Retry-After` respected. Rate-limit budget is tracked per
`(tenant, credential profile)` so one tenant cannot exhaust another's
headroom.

### 29.2 Mutations

1. A mutation is **never** blindly retried. An identical retry risks a
   duplicate write with a different outcome.
2. A `429` before the request is transmitted may be retried under the same
   idempotency key and unchanged preconditions.
3. A timeout or ambiguous response yields `INDETERMINATE`. Recovery is:
   fresh read → compare against the expected after-state → if the change
   applied, record success with verification evidence; if it did not, a new
   proposal and a new approval are required; if it applied partially, report
   `PARTIAL_APPLICATION` with the exact partial state.
4. Cloudflare's guidance to avoid concurrent updates to the same ruleset
   (Section 8.5) is enforced by Section 20.4 serialization, not by retry.

## 30. Pagination

1. Every list capability declares its pagination model and carries cursor or
   page state explicitly.
2. Aggregation across pages is complete or is labeled `truncated`. An
   inventory, coverage, or drift report built on a truncated read must
   declare that and may not be used as the basis of a deletion or
   replacement proposal.
3. Page-boundary drift (items added or removed mid-traversal) is detected
   and reported rather than silently accepted.
4. Unbounded pagination is prohibited; a page-count or item-count cap exists
   and hitting it produces `truncated`, never a silent stop.

## 31. Audit requirements

### 31.1 Required fields

Every Cloudflare execution record includes, where applicable:

tenant ID; MellyCore operator ID; delegated-user or service-account
identity (explicitly labeled as to which); provider ID; Cloudflare account
ID reference; Cloudflare zone ID reference; capability ID; risk tier;
approval ID; policy decision ID; credential reference ID; request
correlation ID; provider request ID; exact target resources (enumerated,
never summarized); sanitized before state; sanitized proposed diff;
sanitized after state; idempotency key; start and completion time; provider
response status; read-after-write result; rollback or containment result;
external-delivery result; failure classification.

### 31.2 Prohibited in audit records

Raw credentials, API tokens, `Authorization` headers, secret-shaped values,
and unnecessarily sensitive payload bodies. Account and zone identifiers are
stored as **references** resolvable within the tenant boundary, not as raw
values in general-purpose logs. Request bodies captured from security events
are minimized and redacted per tenant data classification.

### 31.3 R5 enhancements

An R5 execution additionally records: the exact enumerated resource list
presented to the approver; the approver identity and approval timestamp; the
strict preconditions evaluated and their results; the stored rollback
representation and where it is held; the containment path verified available
before execution; and the post-execution observation evidence identifiers.

### 31.4 D4 session audit

An MCP or investigation session records: operator identity; tenant; profile;
start and end time; every capability invoked; every query issued; response
sizes and truncation; and any content flagged under Section 26.1 rule 9.
Session records are retained under the tenant's retention policy.

### 31.5 Security observations

Recorded as audited security events: an attempt to invoke a Section 15
prohibited capability; an attempt to reach an excluded legacy family; a
cross-tenant or out-of-allowlist access attempt; a credential-widening
attempt; a suspected injection attempt; and any approval-binding mismatch.

### 31.6 Audit is non-optional

Prohibition P-09: no execution path may omit, disable, downgrade, or defer
its audit record. If the audit sink is unavailable, an R3–R5 mutation does
not proceed. Audit failure is a blocking condition, not a warning.

## 32. Read-after-write verification

1. **Mandatory for every mutation.** Not configurable, not skippable, not
   sampled. Prohibition P-10 forbids skipping it.
2. Verification is a **fresh read** through the authorized D1 path — never
   an echo of the write response, never a cached value, never the request
   body assumed applied.
3. Verification compares the observed after-state to the approved
   after-state over the exact enumerated resources, including resources that
   were expected to remain **unchanged**.
4. A mismatch produces `VERIFICATION_FAILED`, is audited, and triggers the
   containment assessment of Section 33. It is never retried into a pass.
5. Verification confirms **control-plane** state only. It does not
   demonstrate edge enforcement (Section 20.5) and must never be reported as
   such.
6. Verification failure for an R5 action escalates to the operator
   immediately; a failed escalation delivery is itself a failure and must not
   degrade to a lower-visibility channel (ADR §9).

## 33. Rollback and containment

### 33.1 Rollback representation

Before any R4/R5 execution, the connector stores a **rollback
representation** — the exact prior state of every enumerated resource,
sufficient to reconstruct it. Where Cloudflare's model makes exact
restoration impossible, the proposal and the approval view must say so
explicitly and name what cannot be restored.

### 33.2 Irreversible actions

Some actions cannot be fully rolled back and must be presented as
irreversible in the approval view:

- **Endpoint deletion (D3-02)** — historical performance and analytics
  metrics "cannot be restored" (Section 8.6). The operation can be re-added;
  its history cannot.
- **Schema deletion (D3-05)** — recoverable only from a MellyCore-retained
  copy of the schema text; without one, the action is prohibited.
- **Rule deletion (D3-23)** — permitted only when a complete rollback
  representation of the rule is stored first; deletion without one is a
  high-risk change forbidden by Section 22.3.

### 33.3 Containment paths (must exist and be verified reachable)

| Situation | Containment |
| --- | --- |
| Schema Validation blocking legitimate traffic, scoped | D3-11 → `none` for the affected operations |
| Schema Validation impact unclear or zone-wide | D3-14 → zone override `none` |
| A MellyCore-created WAF rule causing harm | D3-22 disable the rule (preferred over delete — reversible) |
| A newly effective ruleset causing harm | D3-18 remove the execute rule that made it effective |
| Credential compromise suspected | Revoke the profile (Rule 11.2.12); all bound approvals invalidate |

Rollback is itself a mutation: it requires approval (expedited per
Rule 18.6), idempotency, read-after-write verification, and audit. Rollback
is **not** exempt from this contract.

### 33.4 Protection-removing changes

Containment reduces enforcement, which is also a posture regression. Every
containment action opens a tracked follow-up to restore intended protection
through a new proposal and approval. A zone left in a contained state
without a tracked follow-up is a contract violation.

## 34. Testing requirements

Before implementation may be considered complete, a future implementation
task must demonstrate, without any live Cloudflare call:

1. **Capability registry conformance** — every ID in Section 13 present,
   with all 25 attributes populated; no undeclared capability reachable.
2. **Allowlist enforcement** — a capability outside Section 13 is rejected.
3. **Prohibition enforcement** — each Section 15 entry is refused and audited.
4. **Legacy refusal** — an excluded family (Section 7) is refused, including
   as a fallback after a replacement surface fails (Rule 7.1).
5. **Credential separation** — a read capability cannot execute with a write
   credential and vice versa; no code path places credential material in
   model-visible context.
6. **Tenant/zone isolation** — cross-tenant and out-of-allowlist attempts
   fail closed and are audited.
7. **Approval binding** — execution without a matching proposal ID and
   before-state digest is refused; expired and revoked approvals refuse.
8. **Stale-state abort** — a digest or version mismatch aborts.
9. **Idempotency** — replay returns the recorded outcome; in-flight blocks;
   indeterminate does not blind-retry.
10. **Read-after-write** — cannot be disabled; a mismatch fails the mutation.
11. **Rollout staging** — `block` is unreachable without the full Section 21
    sequence and its observation evidence.
12. **Diff completeness** — replacement operations without add/remove/
    unchanged sets are refused.
13. **Injection handling** — schema descriptions, labels, rule descriptions,
    and event fields carrying instruction-shaped text are treated as data and
    flagged.
14. **Audit completeness** — every Section 31.1 field populated; audit-sink
    failure blocks R3–R5.
15. **Failure taxonomy** — each Section 28 class produces its contracted
    outcome, with no silent degradation.
16. **Truthfulness** — no test fixture, log line, or report asserts that
    Cloudflare is integrated, connected, authenticated, or deployed.

All tests use local fixtures. **No test may authenticate to Cloudflare or
call a Cloudflare API.** A test that did not run records `NOT_RUN`, never a
defaulted pass.

## 35. Implementation prerequisites

Implementation of this connector may not begin until **all** of the
following hold:

1. This contract is accepted and — like the ADR it serves — reviewed,
   published, and merged through the repository's normal gates.
2. `MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001` passes.
3. `MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` passes.
4. `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` passes.
5. `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` passes.
6. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003` passes.
7. `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` receives its own **separate,
   explicit operator authorization**, independent of Model A/B deployment
   authorization and independent of the OpenAI Batch Stage C gate. It
   remains **blocked** until then.
8. A secrets boundary exists that can hold `CF_READ` and
   `CF_WRITE_CONTROLLED` separately, outside model-visible context.
9. An approval broker exists that can enforce Section 18, including
   proposal-ID and state-digest binding.
10. An audit sink exists that can record Section 31.1 in full and block
    R3–R5 when unavailable (Rule 31.6).
11. The Section 8.8 open verification items are re-verified against official
    Cloudflare documentation, dated, and recorded.
12. Per-capability path verification (Section 8.4 rule 3) is performed and
    recorded for every capability before its first request.

Until item 7 is satisfied, **read-only Cloudflare API access also remains
unauthorized**, consistent with `shared_context/RUN_QUEUE.md`.

## 36. Rejected alternatives

| Rejected | Why |
| --- | --- |
| Using the Firewall Rules / Filters APIs because their reference pages lack a deprecation banner | Section 8.1 confirms unsupported since 2025-06-15; banner absence is not currency (Section 8.4 rule 2). |
| Treating every `/api_gateway/...` path as legacy | Section 8.4 — the current 2.0 guide still routes some steps there. Blanket exclusion would break schema activation and operation discovery. |
| Treating every `/schema_validation/...` path as automatically safe | Same rule, inverted. Currency is verified per capability, not inferred from prefix. |
| A single Cloudflare token for reads and writes | ADR §12, §17; Rule 11.2.4. |
| Relying on Cloudflare's account-scoped permissions as MellyCore's tenant boundary | Rule 9.2 — API Gateway permissions span all domains in an account. |
| Cloudflare Code Mode / full-API MCP for autonomous use | Section 25.1 — 2,500+ endpoints behind one grant is unrestricted execute. |
| MCP as a proposal or evidence source | Section 25.3 — evidence derives only from authorized D1 reads. |
| Classifying endpoint deletion as reversible metadata cleanup | Section 8.6 — historical metrics cannot be restored; it is R5. |
| Classifying any Cloudflare mutation R3 to make approval policy-dependent | Section 13.3.3 — contradicts ADR §8's R4 minimum. |
| Zone-wide `block` as a faster path to protection | Section 21.4 — always R5, never reachable without staged rollout. |
| Showing an approver the desired final label set only | Section 24 — replacement requires add/remove/unchanged. |
| Blind retry of a timed-out mutation | Section 29.2 — duplicate-write risk; `INDETERMINATE` requires a fresh read. |
| Read-after-write as a configurable option | Section 32; prohibition P-10. |
| Treating a successful write response as proof of edge enforcement | Section 20.5 — propagation is asynchronous. |
| Silent fallback from a failed critical alert to an internal-only success | ADR §9; Rule 28.1. |
| Defining a rate-limiting mutation capability in v1.0 | Section 13.2.1 D2-16 — proposal-only until a separate amendment. |

## 37. Open questions

### 37.1 Requiring external verification

The Section 8.8 items — label API paths and binding semantics, managed-label
editability, zone-scoped token permission names, Audit Logs v2 path and v1
deprecation status, the security-event search surface and filter grammar,
and plan-dependent feature availability — remain open and must be resolved
by Section 35 item 11 before implementation.

### 37.2 ADR documentation defect — corrected, history preserved

`docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
formerly contained stale internal cross-references. They were corrected by
`MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001` in a
separate append-only documentation commit. That remediation changed no
Cloudflare capability, risk tier, credential rule, authorization, or runtime
state, and this accepted connector contract remains authoritative.

The historical defect and remediation record are deliberately retained here;
they are not a current open correction. Implementation-time verification items
in Section 37.1 remain open and blocking. Nothing in the correction, the later
integration review, or this remediation authorizes Cloudflare authentication,
API access, MCP use, credentials, adapter work, deployment, or runtime execution.

### 37.3 Deferred design questions

- Whether read-only MCP investigation against a live account should be
  authorized in a future version, and under what bounded envelope
  (Section 25.1).
- Whether a rate-limiting mutation capability is warranted (D2-16).
- Whether per-tenant separate Cloudflare accounts should be **required**
  rather than recommended for hostile multi-tenancy (Rule 9.2).
- Numeric threshold defaults for Section 21.3, which are currently
  tenant-policy shaped rather than fixed.

## 38. Amendment and supersession rules

This contract may be amended or superseded only by a later, explicitly
identified document that references this file **by path** and states which
section(s) it changes — the same pattern the ADR requires of itself and that
`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md` established. A
later document that silently contradicts this contract does **not** supersede
it; such a contradiction must be corrected, not treated as an implicit
amendment.

Specifically requiring an amendment: adding a capability; promoting a
capability between domains; lowering any risk tier; relaxing any approval
requirement; authorizing MCP beyond documentation scope; defining a
rate-limiting mutation; or permitting any excluded legacy family.

This contract's ACCEPTED status is specification-level only (Section 1.1)
and remains so until a future task explicitly changes it. Amendment of this
contract never amends the ADR; where the two diverge, the ADR prevails
(Section 3).

## 39. References

### 39.1 Repository (canonical)

- `[[../decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001]]` —
  governing architecture decision.
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001.md`,
  `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001.md`.
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` — status
  dimensions (§8), Provider Registry (§9.1), Integration Gateway (§9.6),
  Security and Secrets Boundary (§9.9).
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]` — truthfulness rules
  (§1.5) and contract-spec format precedent.
- `shared_context/SAFETY_CONTRACT.md`, `shared_context/PROJECT_STATE.md`,
  `shared_context/ROADMAP.md`, `shared_context/RUN_QUEUE.md`,
  `shared_context/AGENT_HANDOFF.md`.

### 39.2 Official Cloudflare documentation (verified 2026-08-01)

All accessed as **unauthenticated, read-only fetches of public
documentation pages**. No Cloudflare API was authenticated, called with a
credential, or mutated; no Cloudflare MCP server was used.

| Title | URL |
| --- | --- |
| Firewall rules upgrade | `https://developers.cloudflare.com/waf/reference/migration-guides/firewall-rules-to-custom-rules/` |
| Schema validation | `https://developers.cloudflare.com/api-shield/security/schema-validation/` |
| Configure Schema validation via the API | `https://developers.cloudflare.com/api-shield/security/schema-validation/api/` |
| Classic Schema validation (deprecated) | `https://developers.cloudflare.com/api-shield/reference/classic-schema-validation/` |
| Schema Validation › Settings (API reference) | `https://developers.cloudflare.com/api/resources/schema_validation/subresources/settings/` |
| API Gateway › User Schemas (API reference) | `https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/` |
| API Gateway › User Schemas › Hosts (API reference) | `https://developers.cloudflare.com/api/resources/api_gateway/subresources/user_schemas/subresources/hosts/` |
| Rulesets | `https://developers.cloudflare.com/ruleset-engine/about/rulesets/` |
| Rulesets API | `https://developers.cloudflare.com/ruleset-engine/rulesets-api/` |
| Endpoints (Rulesets API) | `https://developers.cloudflare.com/ruleset-engine/rulesets-api/endpoints/` |
| Endpoint Management | `https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/` |
| Endpoint labeling service | `https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-labels/` |
| Authentication Posture | `https://developers.cloudflare.com/api-shield/security/authentication-posture/` |
| API token permissions | `https://developers.cloudflare.com/fundamentals/api/reference/permissions/` |
| Review audit logs - v1 | `https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/` |
| Cloudflare's own MCP servers | `https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/` |

**Verification date:** 2026-08-01. Unresolved contradictions are recorded in
Section 8.4; unverified claims in Section 8.8; plan-dependent capability in
Section 8.8.
