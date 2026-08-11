# MellyCore Cybersecurity Provider Pack Specification 001

## 1. Title and status

**Contract ID:** `MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001`

**Task ID:** `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001`

**Status:** Accepted at specification level

**Research snapshot:** 2026-08-01

**Contract revision:** `001`

This is a documentation and specification artifact only. No provider is
connected, no credential is configured, no adapter or runtime exists, and no
deployment is authorized or performed by accepting this specification.

Normative words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** describe future
conformance requirements. They do not describe implemented behavior.

## 2. Purpose

This specification defines the first bounded, read-oriented cybersecurity
provider pack for MellyCore AIOS. It establishes one normalized security model,
stable provider and capability identifiers, provider-specific read mappings,
and fail-closed uncertainty rules for:

- P0: Microsoft Defender XDR / Microsoft Graph Security, GitHub Advanced
  Security, Cloudflare, and Okta;
- P1: Splunk and CrowdStrike Falcon; and
- P2: Snyk.

The initial pack is limited to R0 discovery, R1 low-risk reads, and R2 analysis
and proposal generation. It makes provider evidence comparable without
pretending that unlike provider objects are identical.

## 3. Authority and source contracts

This contract is downstream of, and MUST NOT weaken:

1. `shared_context/SAFETY_CONTRACT.md`;
2. `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`;
3. `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`;
4. `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`;
5. `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`;
6. `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`;
7. `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`;
8. `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`; and
9. `shared_context/VALIDATION.md`.

The accepted Cloudflare connector contract remains authoritative for every
Cloudflare operation. Section 21 is a pack mapping, not a replacement copy.
When any downstream provider source conflicts with a canonical MellyCore
contract, MellyCore fails closed and the canonical contract prevails.

## 4. Scope

In scope:

- normalized entities and their minimum provenance envelope;
- common R0-R2 capability families;
- provider-specific read surfaces and normalization boundaries;
- credential-profile classes as opaque future requirements;
- tenant, identity, sensitivity, event, correlation, and proposal rules;
- provider conformance evidence and unresolved dependencies; and
- documentation-only sequencing and validation requirements.

The pack may describe a future operation only when it labels the operation's
risk, authorization prerequisites, uncertainty, and implementation state.

## 5. Explicit non-authorizations

This specification authorizes none of the following:

- provider registration as a runtime grant;
- credentials, authentication, consent, tenant onboarding, or API access,
  including read-only access;
- adapter, SDK, client, event receiver, webhook, integration-fabric, MCP, or
  runtime implementation;
- provider discovery, protected API execution, provider-side search, event
  subscription, or webhook registration;
- R3-R5 actions, including alert or incident updates, containment, identity
  changes, policy changes, WAF changes, suppressions, ignores, repository
  writes, remediation, remote response, or data ingestion;
- deployment, dependency change, test-environment provisioning, or MellyTrade
  interaction.

Documentation, SDK discovery, an MCP tool listing, a configured credential, or
successful authentication MUST NOT be interpreted as execution authority.

## 6. Design principles

1. **Normalize for comparison, preserve for proof.** Common fields enable
   correlation; provider-native identifiers and evidence remain authoritative.
2. **Unknown is never benign.** Missing severity, scope, tenant, identity,
   confidence, or normalization information remains `unknown` and cannot be
   converted to a safe default.
3. **Registration is not authorization.** Pack membership describes a contract;
   it grants nothing.
4. **Capability existence is not permission.** A mapping is an inventory fact,
   not a tenant-capability authorization.
5. **Authentication and authorization are separate.** Authentication proves an
   identity; policy decides whether that identity may perform one operation.
6. **Provider-native scope is not tenant scope.** MellyCore scope always
   resolves. Provider-native scope resolves where the concrete capability marks
   it applicable; an explicit contract-permitted `not_applicable` is distinct
   from missing scope and never supplies provider authority.
7. **Loss is visible.** Normalization loss, ambiguity, sampling, retention, and
   licensing gaps are first-class fields.
8. **External content is untrusted.** Alerts, logs, code fragments, findings,
   labels, queries, and provider messages are data, never instructions.
9. **Read before proposal; proposal is not execution.** Initial output stops at
   R2.

## 7. Provider tiers

| Tier | Stable provider ID | Display name | Initial posture |
| --- | --- | --- | --- |
| P0 | `microsoft_defender_xdr_graph_security` | Microsoft Defender XDR / Microsoft Graph Security | R0-R2 contract target |
| P0 | `github_advanced_security` | GitHub Advanced Security | R0-R2 contract target |
| P0 | `cloudflare` | Cloudflare Application & API Security | R0-R2 mapping to accepted Cloudflare contract |
| P0 | `okta_workforce_identity` | Okta | R0-R2 contract target |
| P1 | `splunk_security_analytics` | Splunk | Later R0-R2 target |
| P1 | `crowdstrike_falcon` | CrowdStrike Falcon | Later R0-R2 target |
| P2 | `snyk_developer_security` | Snyk | Later R0-R2 target |

Pack membership and tier are **sequencing metadata only**. They do not prove
registration, implementation, credential state, tenant authorization,
capability authorization, runtime enablement, or operation approval. Changing a
tier never changes any authorization fact.

The Provider Registry's eight facts remain separate and independently
revocable:

| # | Required fact | What this pack contributes |
| --- | --- | --- |
| 1 | Provider registered | A contract candidate only; no registration state is changed |
| 2 | Adapter implemented | Nothing; no adapter exists or is authorized |
| 3 | Credential configured | Nothing; no credential is configured |
| 4 | Credential verified | Nothing; no authentication or verification occurs |
| 5 | Tenant authorized | Nothing; no tenant-provider grant is issued |
| 6 | Capability authorized | Nothing; capability mappings are not grants |
| 7 | Runtime enabled | Nothing; no runtime is enabled |
| 8 | Operation approved | Nothing; no operation is approved by this specification |

No aggregate `enabled`, `ready`, `connected`, or tier field may replace these
facts.

## 8. Normalized entities

The stable entity kinds are:

| Entity kind | Meaning |
| --- | --- |
| `security_provider` | One provider contract identity and revision |
| `security_alert` | Provider signal requiring triage |
| `security_incident` | Provider-correlated investigation container |
| `security_finding` | Discrete control, code, configuration, or exposure finding |
| `security_vulnerability` | Vulnerability observation with affected subject |
| `security_asset` | Host, endpoint, application, API, repository, image, or other protected asset |
| `security_identity` | User, group, service principal, application, or workload identity |
| `security_event` | Immutable or append-oriented provider event observation |
| `security_evidence` | Bounded evidence reference supporting another entity |
| `security_control` | Provider-native control, policy, or posture rule description |
| `security_posture_snapshot` | Time-bound aggregate posture observation |
| `security_recommendation` | Non-executing analysis with rationale |
| `security_remediation_proposal` | Non-executing, reviewable future-action proposal |

Every instance MUST carry this common required envelope:

| Field | Requirement |
| --- | --- |
| `normalized_id` | Stable, collision-resistant normalized ID; never derived from mutable display text alone |
| `entity_kind` | Exactly one kind from this section |
| `provider_id` | Stable provider ID from Section 7 |
| `provider_object_type` / `provider_object_id` | Native type and stable native ID; unknown explicitly represented |
| `tenant_id` | Authoritative MellyCore tenant; absence quarantines the object |
| `provider_resource_scope` | Native account/org/repository/zone/index/resource boundary |
| `source_created_at` / `source_updated_at` | Native timestamps when supplied; missing values remain unknown |
| `severity` / `status` / `confidence` | Native value plus normalized value; unknown is never low, closed, or trusted |
| `affected_resource_refs` / `affected_identity_refs` | Explicit references; empty and unknown are distinct |
| `evidence_refs` | Bounded references, never a raw secret |
| `sensitivity_level` / `allowed_use` | Canonical Section 13 classification |
| `external_exposure` | Whether content may have been influenced by an external actor |
| `normalization_confidence` / `normalization_loss` | Confidence plus enumerated omissions, coercions, sampling, and ambiguity |
| `raw_reference_policy` | `not_retained`, `opaque_reference`, `sanitized_excerpt`, or separately governed encrypted retention |
| `retrieved_at` | Gateway retrieval time, distinct from source time |
| `provider_contract_revision` | Exact provider-specific contract revision used |

An entity MUST NOT be merged across tenants. Native objects remain
independently addressable after correlation.

## 9. Common capability families

The common stable capability families are:

```text
security.inventory.*
security.alerts.*
security.incidents.*
security.findings.*
security.vulnerabilities.*
security.assets.*
security.identities.*
security.events.*
security.audit.*
security.posture.*
security.evidence.*
security.recommendations.propose
security.remediation.propose
```

Initial concrete capabilities MUST end in `.discover`, `.list`, `.get`,
`.read`, `.analyze`, or `.propose` and MUST be classified R0, R1, or R2.
Names suggesting update, dismiss, resolve, ignore, contain, isolate, execute,
delete, create, send, publish, block, revoke, or remediate are outside this
initial pack.

Every provider mapping preserves: the common capability ID; stable provider ID;
provider-specific capability ID and revision; tenant; provider resource scope;
acting identity; risk tier; and normalization-loss metadata. Provider-specific
IDs MUST NOT be silently repurposed when an upstream API changes.

## 10. Risk model

The canonical R0-R5 model is preserved:

| Risk | Pack meaning |
| --- | --- |
| R0 | Static capability and schema discovery with no protected-provider call |
| R1 | Bounded, tenant-scoped read of existing provider state |
| R2 | Analysis, correlation, recommendation, or proposal with no external change |
| R3 | Reversible consequential mutation — deferred |
| R4 | High-impact or broad mutation — deferred |
| R5 | Critical, destructive, containment, identity, or remote-response action — deferred |

Only R0-R2 are admitted by this revision. A provider-specific label such as
`read`, `investigate`, or `response` cannot lower risk. Any capability with an
uncertain side effect is excluded until a later contract proves otherwise.

Any future R3-R5 revision MUST preserve exact target-bound approval; invalidate
approval on stale target, policy, tenant, identity, credential, or capability
state; durably acknowledge Gateway audit Stage A before the provider attempt;
append Stage B outcome evidence afterward; and block execution when Stage A is
unavailable. Unknown mutation outcome requires reconciliation, never blind
provider retry, and every claimed mutation requires authoritative read-after-
write verification (`read-after-write verification`). These inherited
requirements are recorded here to prevent a
provider-specific contract from weakening them; they do not admit R3-R5.

## 11. Identity and tenant isolation

Every request MUST preserve the Gateway's complete acting-identity chain.
Provider Registry §7.5 is the sole owner of the canonical acting-identity
vocabulary: `delegated_user`, `service_account`, and `mellycore_operator`.
The last is valid only for an explicitly operator-bound restricted-tool
capability and is never a fallback. The chain includes tenant, requesting
actor, exact canonical acting identity, authentication target, adapter/fabric
when present, applicable downstream provider, and exact provider or tool
target. It MUST NOT be merged, substituted, or inferred from session state.

A fabric-mediated path MUST preserve the full downstream chain
`MellyCore -> integration fabric -> downstream provider -> target resource`,
including both fabric and provider request identities, capability revisions,
credential-profile references, and provider-native scope. Lost provenance
cannot be repaired by the fabric's own authentication and makes the path
ineligible.

Tenant authorization and applicable provider-native account scope are
independent checks.
Enterprise, organization, repository, account, subscription, zone, index,
customer, and region identifiers remain provider resource scopes; none is a
MellyCore tenant ID. Cross-tenant caches, correlation, credentials, results,
event deduplication, and raw references are prohibited.

## 12. Credential contract

Future provider-specific contracts MUST select an explicit credential-profile
class. This table is a non-exhaustive pack projection of the Registry §13.2
catalogue and creates no second enum:

| Class | Purpose | Initial pack status |
| --- | --- | --- |
| `read_only_delegated` | Registry class: bounded delegated human read | Described, not configured |
| `read_only_service` | Registry class: explicitly labelled workload read | Described, not configured |
| `controlled_write` | Future provider mutation | Deferred and unauthorized |
| `event_verification` | Verify an inbound event source/signature or token | Described, not configured |
| `integration_fabric_read` | Bound fabric-mediated downstream read identity | Described only where relevant |
| `integration_fabric_controlled_write` | Bound fabric-mediated downstream write identity | Deferred and unauthorized |
| `restricted_operator_investigation` | Operator-only, documentation/investigation tool path with `required_acting_identity_type: mellycore_operator`, `required_authentication_target: restricted_tool`, provider-native scope explicitly `not_applicable`, and exact restricted-tool scope | Cloudflare D4 only; described, not connected or configured |

Credential references are opaque. Secret values remain in an approved secret
manager, outside prompts, model context, logs, normalized entities, evidence,
task reports, and error text. Profiles MUST bind tenant, canonical acting
identity, authentication target, complete scope applicability, exact applicable
provider-native or restricted-tool scope, allowed capability class, expiry,
rotation, revocation, and verification state.

Read and write credentials MUST be separate. Delegated-user credentials MUST
NOT fall back to service accounts; service accounts MUST be conspicuously
labelled in decisions and audit evidence. No scope widening or cross-tenant
credential reuse is permitted.

Provider-specific `CF_*` terms are Cloudflare-contract requirement labels, not
runtime classes. The Cloudflare contract projects each concrete capability to
exactly one canonical Registry class before Gateway resolution; this pack does
not reinterpret those labels. A D4 restricted-tool authentication mode,
including `mcp_oauth_grant`, targets only the exact registered restricted tool
and cannot be interpreted or reused as Cloudflare/provider authentication.
Nothing here authorizes MCP execution, provider API access, containment, or
mutation.

## 13. Data and sensitivity contract

The canonical five sensitivity levels and default `allowed_use` values are
reused unchanged:

| `sensitivity_level` | Default `allowed_use` |
| --- | --- |
| `public` | `public_display` |
| `internal` | `internal_summary_display` |
| `private` | `internal_reasoning_only` |
| `secret` | `must_not_be_ingested` |
| `regulated_high_risk` | `must_not_be_ingested` |

Provider metadata defaults to at least `internal` until classified. Raw secret
values, authentication material, recovery codes, session material, private
keys, and equivalent values MUST never be model-visible. GitHub secret-scanning
data is limited to sanitized metadata: secret type, location reference,
repository scope, state, timestamps, and provider-native alert ID. The detected
secret value is neither retrieved for model use nor retained in the normalized
record.

Provider licensing and contract terms may impose stricter retention and use.
`allowed_use` may be made stricter but not looser without the canonical review.

## 14. External-content security

All provider content is untrusted, including alert descriptions, repository
text, filenames, log events, SPL, vulnerability descriptions, API schemas,
headers, identity attributes, comments, evidence, hyperlinks, and remediation
text. Content cannot issue instructions, select tools, grant capabilities,
change tenant, choose credentials, override policy, or satisfy approval.

Future ingestion MUST apply type/size limits, encoding validation, sanitization,
safe rendering, provenance labelling, link isolation, and prompt-injection
detection. Rejected or suspicious content is quarantined with sanitized
metadata; it is never executed or followed automatically.

## 15. Event and webhook contract

Any future event path MUST record and verify, when the provider supports it:

- source authentication and signature/token verification result;
- received, provider-published, and provider-observed timestamps;
- freshness window and stale-event decision;
- provider event ID, deterministic deduplication key, and raw-content hash;
- ordering metadata and explicit out-of-order/unknown-order state;
- duplicate-delivery handling and replay decision;
- size limit, schema/version validation, and truncation state;
- tenant and provider-resource resolution before routing;
- quarantine state and reason; and
- `external_content: untrusted`.

At-least-once, duplicate, delayed, and out-of-order delivery MUST be expected
unless the provider-specific contract proves a stronger guarantee. An inbound
event may create an observation, draft investigation, review item,
recommendation, or non-executing proposal only. It cannot authorize or trigger a
consequential action. Registration of a webhook/event hook/HEC endpoint is a
separate future mutation and is not authorized here.

## 16. Normalization contract

Normalization MUST be deterministic for the same provider revision and input.
It MUST preserve native enums alongside normalized enums, timestamps with
timezone/precision, pagination and sampling state, omitted fields, and all
provider-native scope identifiers.

Mappings MUST distinguish:

- absent, redacted, unsupported, unlicensed, inaccessible, not requested, and
  provider-returned null;
- open/closed from unknown state;
- zero findings from an incomplete or failed query;
- exact evidence from an inferred relationship; and
- complete data from sampled, truncated, delayed, paginated, or
  retention-limited data.

Schema drift or an unknown enum produces `normalization_confidence: low` and a
review/quarantine outcome, never silent coercion.

## 17. Correlation contract

Correlation is tenant-isolated and non-destructive. Every relationship MUST
record confidence, rationale, algorithm/revision, evidence references, and
whether it is deterministic or heuristic.

Deterministic joins require strong provider identifiers or an approved stable
mapping. Weak attributes such as display name, email text, IP address, hostname,
repository name, or free-form label MUST NOT merge entities by themselves.
Ambiguity remains explicit as competing candidates. Correlation never changes a
provider object, closes an incident, or converts inference into provider fact.

## 18. Proposal-only output contract

R2 recommendations and remediation proposals MUST include:

- tenant, provider, exact affected resources/identities, and capability;
- evidence references and source freshness;
- reasoning, confidence, uncertainty, alternatives, and normalization loss;
- proposed outcome and explicit `execution_state: not_executed`;
- likely future risk tier and approval class, clearly labelled preliminary;
- provider-specific contract and implementation prerequisites; and
- a statement that the proposal neither proves feasibility nor grants
  authorization.

No R2 output may claim that a provider state changed, a risk was remediated, or
an action succeeded. A proposal cannot be converted directly into an adapter
request.

## 19. Microsoft Defender XDR / Microsoft Graph Security

**Provider ID:** `microsoft_defender_xdr_graph_security`

**Tier:** P0

**Initial integration class:** future native adapter

**Initial risk ceiling:** R2

### 19.1 Included read mappings

| Common capability | Provider-specific mapping | Risk | Normalized output |
| --- | --- | --- | --- |
| `security.incidents.list/get` | Microsoft Graph Security `GET /security/incidents` and incident retrieval | R1 | `security_incident`, related alerts/evidence |
| `security.alerts.list/get` | Microsoft Graph Security `GET /security/alerts_v2` and alert retrieval | R1 | `security_alert`, affected assets/identities, evidence refs |
| `security.evidence.read` | Evidence and affected-resource fields returned with authorized alerts/incidents | R1 | `security_evidence`, `security_asset`, `security_identity` |
| `security.posture.analyze` | Bounded analysis of normalized alert/incident state | R2 | `security_posture_snapshot`, `security_recommendation` |
| `security.remediation.propose` | Non-executing response proposal | R2 | `security_remediation_proposal` |

The legacy Microsoft Graph Security Alerts API at `/security/alerts` is
deprecated and excluded from new integration. Microsoft documents retirement
beginning 2026-08-31; the future provider contract MUST re-verify the then-
current endpoint and migration state before implementation.

### 19.2 Authorization and uncertainty

Future access MUST use the minimum applicable Microsoft Graph security read
permissions and resolve both Entra identity/role requirements and product-
specific licensing. Exact delegated/application permission sets, Defender
product entitlements, evidence availability, retention, regional behavior, and
tenant consent are `UNVERIFIED` until a provider-specific contract tests the
exact tenant and endpoint. Read-write permissions are excluded.

All alert/incident updates, comments, assignments, status changes, hunting or
containment mutations, machine isolation, indicator changes, identity actions,
and automated response are deferred to R3-R5 contracts.

## 20. GitHub Advanced Security

**Provider ID:** `github_advanced_security`

**Tier:** P0

**Initial integration class:** future native adapter

**Initial risk ceiling:** R2

### 20.1 Included read mappings

| Common capability | Provider-specific mapping | Risk | Required provenance |
| --- | --- | --- | --- |
| `security.findings.secret_scanning.list/get` | Secret-scanning alerts and locations | R1 | enterprise/org/repo, alert, location, branch/commit/file where supplied; never secret value |
| `security.findings.code_scanning.list/get` | Code-scanning alerts/instances/analyses metadata | R1 | enterprise/org/repo, tool/rule, branch/ref, commit, path, location |
| `security.vulnerabilities.dependabot.list/get` | Dependabot alerts | R1 | enterprise/org/repo, advisory/dependency/package, manifest/path, branch where supplied |
| `security.posture.repositories.read` | Bounded repository/org security posture metadata supported by the entitled API | R1 | enterprise/org/repo and feature/license state |
| `security.recommendations.propose` | Cross-alert analysis and non-executing recommendation | R2 | exact repositories/findings/evidence |

Secret-scanning values are prohibited from normalized content and model
context even if an upstream response exposes them. Location references are
sanitized and sensitivity-classified.

### 20.2 Authorization and deferred surfaces

Future access MUST use fine-grained read permissions for the exact alert family
and repository/organization scope. GitHub App, fine-grained token, enterprise,
organization, and repository eligibility differ; the provider-specific contract
MUST resolve them without widening scope.

Alert state changes, dismissals, reopenings, resolutions, push-protection bypass
decisions, policy changes, repository settings, code-scanning database uploads,
autofix creation/commit, repository writes, and pull-request creation are
deferred and unauthorized.

## 21. Cloudflare

**Provider ID:** `cloudflare`

**Tier:** P0

**Authority:**
`MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001`

**Initial risk ceiling:** R2

This section maps the accepted Cloudflare contract into the common pack; that
contract controls whenever wording differs.

The mapping is a projection only: all 58 accepted Cloudflare capabilities and
all 13 explicit prohibitions remain authoritative under provider ID
`cloudflare`. This pack neither duplicates nor narrows those tables.
The Cloudflare contract's normative credential projection also remains
authoritative: `CF_*` labels are not Gateway inputs, and every concrete
registration binds one canonical Registry class, acting-identity type,
authentication target, and complete scope-applicability declaration before
runtime. D4 uses `mellycore_operator`, target `restricted_tool`, provider-native
account/zone/resource `not_applicable`, and exact registered-tool scope; this
does not authorize a tool connection or Cloudflare API access.

| Common capability | Accepted Cloudflare mapping | Risk |
| --- | --- | --- |
| `security.inventory.endpoints.read` | Endpoint inventory and API discovery observations | R1 |
| `security.posture.api_schema.read` | API Shield schema coverage and validation posture | R1 |
| `security.findings.api_drift.read` | Endpoint/schema drift and unprotected-endpoint reports | R1 |
| `security.posture.authentication.read` | Authentication posture observations | R1 |
| `security.controls.waf_inventory.read` | WAF/Rulesets inventory only | R1 |
| `security.events.read` / `security.audit.read` | Bounded security-event and audit-log reads | R1 |
| `security.recommendations.propose` | WAF/schema recommendation | R2 |
| `security.remediation.propose` | Non-executing WAF/schema proposal | R2 |

All Cloudflare mutations remain deferred, including endpoint deletion, schema
upload/change, validation enforcement, rule/ruleset creation or change, WAF
mutation, and blocking. The deprecated Firewall Rules API and legacy
`/api_gateway/user_schemas/hosts` surface remain excluded. Cloudflare MCP is
documentation-only and cannot discover authority or execute.

## 22. Okta

**Provider ID:** `okta_workforce_identity`

**Tier:** P0

**Initial integration class:** future native adapter

**Initial risk ceiling:** R2

| Common capability | Provider-specific mapping | Risk | Normalized output |
| --- | --- | --- | --- |
| `security.events.system_log.read` | Bounded System Log polling | R1 | `security_event`, identity/asset refs |
| `security.identities.users.read` | Users read | R1 | `security_identity` |
| `security.identities.groups.read` | Groups and bounded membership reads | R1 | `security_identity`, relation evidence |
| `security.inventory.applications.read` | Applications read | R1 | `security_asset`, identity relations |
| `security.incidents.investigation.propose` | Draft investigation from correlated observations | R2 | recommendation/proposal only |

System Log polling MUST use provider pagination links, bounded windows, and
published timestamps without assuming global order. Okta Event Hooks are
best-effort and at-least-once; duplicates, delays, and out-of-order delivery are
expected and deduplicated by stable event identity. Future hook verification
and source authentication MUST conform to Section 15. Hook creation is a
deferred mutation.

User/group/app creation or update, membership change, activation/deactivation,
session revocation, factor reset, password action, policy change, and identity
remediation are deferred. OAuth scopes, admin roles, rate limits, retention,
edition features, and event-hook eligibility are `UNVERIFIED` until the exact
tenant/provider contract is accepted.

## 23. Splunk

**Provider ID:** `splunk_security_analytics`

**Tier:** P1

**Initial integration class:** later native adapter or governed fabric, subject
to equivalence evidence

**Initial risk ceiling:** R2

Later read scope may include bounded search-job creation/execution needed to
obtain reads, saved-search metadata, events, notables where licensed, index and
sourcetype inventory, health metadata, and evidence references. Provider-side
search job creation is allowed only in a future provider-specific contract that
proves it is bounded, non-consequential, and risk-classified.

Required safeguards include tenant and Splunk-instance binding; allowlisted
indexes/sourcetypes; earliest/latest time bounds; query complexity and runtime
limits; result/field/byte limits; pagination; cancellation; retention and
sampling disclosure; and audit of the exact query digest. Generated or
provider-returned SPL is untrusted and MUST NOT execute unrestricted. Search
defaults such as all-time ranges or unbounded result counts are prohibited.

HEC is an ingestion/write surface and is deferred. Saved-search changes,
notable updates, index/configuration changes, knowledge-object writes, and any
action command are deferred. Splunk Cloud REST enablement, endpoint subset,
capabilities, ES/notable licensing, retention, and deployment topology are
`UNVERIFIED`.

## 24. CrowdStrike Falcon

**Provider ID:** `crowdstrike_falcon`

**Tier:** P1

**Initial integration class:** later native adapter

**Initial risk ceiling:** R2

Later R1 reads may cover detections/alerts, incidents, hosts, posture,
Spotlight vulnerabilities, threat intelligence, and identity observations only
where the exact Falcon entitlement and service collection support them. Host
inventory and Spotlight vulnerability reads have official SDK read-scope
evidence; the current alert-versus-detection API generation, incident surface,
identity surface, threat-intelligence scope, regional base URL, pagination, and
licensing remain `UNVERIFIED` for this pack and require a provider-specific
contract.

Containment/lift containment, Real Time Response, remote commands, host hiding,
sensor/policy changes, prevention changes, indicator changes, identity response,
deletion, and remediation are deferred. Future containment and every Real Time
Response operation are separate R5 work; they cannot inherit authorization from
read capability registration or from this provider's P1 sequence tier.

## 25. Snyk

**Provider ID:** `snyk_developer_security`

**Tier:** P2

**Initial integration class:** later native adapter

**Initial risk ceiling:** R2

Later R1 scope may include REST API versions, organizations, projects, targets,
and issues/findings for entitled Snyk products. Every object MUST preserve Snyk
group/org/project/target plus repository, branch/ref, package, container image,
and IaC provenance where supplied. Snyk Open Source, Code, Container, and IaC
findings MUST retain product distinction; they are not interchangeable issue
types.

REST requests require an explicit supported date version, regional base URL,
cursor pagination, and deprecation/Sunset handling. A group-level read-only
service-account path is documented, while organization-level service-account
roles may be broader; the exact least-privilege identity design, product
entitlements, issues endpoint coverage, retention, and rate limits remain
`UNVERIFIED`.

Ignore/suppress/state changes, policy edits, integration changes, project or
target mutation, remediation execution, repository writes, autofix, and pull-
request creation are deferred and unauthorized.

## 26. Cross-provider conformance matrix

| Provider | Stable scope preserved | R0-R2 only | Raw secret excluded | Events fail closed | Mutation deferred | Key uncertainty |
| --- | --- | --- | --- | --- | --- | --- |
| Microsoft | tenant + native resource | Yes | Yes | n/a in initial mapping | Yes | permissions/licensing/evidence by product |
| GitHub | enterprise/org/repo/ref/object | Yes | Yes, mandatory | future events only | Yes | entitlement/token family by endpoint |
| Cloudflare | account/zone/hostname/endpoint | Yes | Yes | per accepted contract | Yes | plan/retention/sampling |
| Okta | tenant/org/user/group/app/event | Yes | Yes | duplicates/out-of-order expected | Yes | scopes/roles/edition |
| Splunk | tenant/instance/index/sourcetype/search | Yes | Yes | HEC deferred | Yes | Cloud enablement/ES license |
| CrowdStrike | tenant/CID/host/detection/object | Yes | Yes | future events only | Yes | current API families/entitlements |
| Snyk | group/org/project/target/repo/ref/product | Yes | Yes | future events only | Yes | least privilege/product coverage |

Conformance requires every `Yes` property plus the common envelope, Registry,
Gateway, audit, and sensitivity contracts. A row is not implementation evidence.

## 27. Provider-specific contract requirements

Before any adapter or protected-provider call, a separate provider-specific
contract MUST:

1. pin current official API families, versions, base URLs/regions, schemas,
   pagination, rate limits, retention, and deprecations;
2. enumerate each capability ID, HTTP method/tool, side effects, and R tier;
3. prove least-privilege delegated and/or service-account permissions;
4. bind tenant and every provider-native scope;
5. define credential lifecycle without exposing secret material;
6. specify error, retry, freshness, idempotency, concurrency, and unknown-outcome
   behavior;
7. map every native object into Section 8 with tested normalization loss;
8. define event verification/deduplication/order/quarantine if applicable;
9. prove audit and acting-identity provenance through every downstream hop;
10. enumerate licensing, consent, regional, and contractual dependencies;
11. test external-content and oversized/malformed payload handling; and
12. demonstrate that provider-specific rules cannot weaken generic contracts.

Unresolved evidence is `UNVERIFIED` and blocks that capability. Registration,
discovery, or successful conformance testing still does not satisfy the
Registry's remaining authorization facts.

## 28. Implementation sequence

If separately authorized after the full documentation-integration review, the
selected sequence is:

1. Microsoft Defender XDR / Graph Security and GitHub Advanced Security;
2. Cloudflare mapping conformance and Okta;
3. Splunk and CrowdStrike Falcon after licensing/API-family verification; and
4. Snyk after least-privilege and product-coverage verification.

Rationale: Microsoft and GitHub provide the broadest initial alert, incident,
code, secret, and dependency evidence; Cloudflare already has an accepted
provider contract; Okta contributes identity audit context. Splunk and
CrowdStrike carry deployment/licensing/API-generation uncertainty, while Snyk
benefits from the repository and identity correlations established earlier.

This is planning metadata only. It grants no implementation, procurement,
credential, provider access, adapter scaffolding, or runtime authority.

## 29. Testing and validation requirements

Future provider contracts and implementations MUST test:

- stable IDs, exact tenant/scope binding, and cross-tenant denial;
- all eight independent Registry facts, including each absent/unknown state;
- authentication/authorization separation and no credential fallback;
- read/write credential separation and service-account labelling;
- R0-R2 ceiling and refusal of every known R3-R5 surface;
- normalization for null, unknown, new enums, partial pages, truncation,
  sampling, retention gaps, schema drift, and product/license gaps;
- secret redaction and sensitivity/allowed-use enforcement;
- prompt injection, hostile text, malformed payload, and unsafe-link handling;
- event authentication, replay, duplicate, stale, delayed, out-of-order,
  oversized, and wrong-tenant cases;
- deterministic and heuristic correlation with ambiguity preserved;
- R2 proposal `not_executed` truthfulness;
- audit/provenance completeness and fail-closed audit behavior; and
- provider-specific contract inheritance with no weakening.

Documentation validation includes exact section count, provider/evidence
coverage, canonical cross-reference checks, forbidden authorization scans,
`git diff --check`, and `scripts/validate_project_state.py`.

## 30. Rejected designs

| Rejected design | Reason |
| --- | --- |
| One generic `security_provider.enabled` switch | Collapses eight independent Registry facts |
| Tier or pack membership as authorization | Sequencing metadata cannot grant access |
| One provider account as tenant identity | Confuses native scope with MellyCore tenant |
| Shared read/write credential | Prevents least privilege and independent revocation |
| Delegated-to-service fallback | Breaks acting identity and accountability |
| Raw secret-scanning value in model context | Exposes the very secret being protected |
| Normalize unknown severity to low | Converts missing evidence into false safety |
| Merge identities/assets by display text | Weak identifiers create cross-entity and cross-tenant risk |
| Execute provider-generated SPL or remediation | External content is untrusted |
| Webhook as an approval signal | Inbound content cannot authorize action |
| MCP discovery as tool authorization | Discovery proves neither permission nor safety |
| Copy the Cloudflare contract into this pack | Creates divergent authority and stale duplication |
| Auto-advance an R2 proposal to mutation | Proposal is not approval or execution authority |
| Blind retry of an uncertain mutation | Could duplicate consequential effects; future R3-R5 must reconcile |

## 31. Implementation prerequisites

All of the following are prerequisites, not authorizations:

1. acceptance of this pack and the marketing pack;
2. a future independent `PASS` from
   `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004` — currently not
   run; the documentation gate remains failed;
3. separate operator authorization for adapter scaffolding;
4. accepted provider-specific contracts for each attempted provider;
5. implemented and tested Registry, Gateway, audit, secret-manager, tenant,
   provenance, and quarantine controls;
6. approved credential provisioning and revocation procedures;
7. exact environment/runtime enablement and bounded capability grants; and
8. a separate deployment and provider-access authorization.

Until every applicable gate passes, adapter scaffolding and all protected API
calls remain blocked.

## 32. Open questions

1. What retention policy applies to provider-native raw references by
   sensitivity and provider contract?
2. Which canonical severity/status vocabulary should be versioned for security
   entities without erasing native semantics?
3. Which Microsoft permissions/licenses expose the required evidence in the
   target tenant?
4. Which GitHub credential class gives the exact cross-org read coverage?
5. Which Okta scopes/roles and editions cover System Log and identity reads?
6. Which Splunk Cloud/Enterprise and Enterprise Security surfaces are enabled?
7. Which CrowdStrike alert/detection generation and product entitlements are
   authoritative for the target environment?
8. Which Snyk service-account topology achieves true least-privilege read-only
    access across required organizations/products?

Each remains `UNVERIFIED`; none may be filled by assumption.

Authorization-record custody is resolved by Registry §§21.3–21.5 and Gateway
Rule 17.4. Native-equivalence evidence is resolved by
`docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`; neither is an
open provider fact or an execution authorization.

## 33. Amendment and supersession

Changes require a new reviewed revision or an explicitly superseding contract.
An amendment MUST identify changed provider evidence, capability IDs, risk,
authorization, normalization, migration, and compatibility impact. Historical
revisions remain auditable.

An upstream provider deprecation, SDK change, new permission, or new product
name does not silently amend this contract. A provider-specific contract may be
stricter but cannot weaken this pack or its authorities. R3-R5 admission
requires a separately authorized contract revision; it cannot be introduced as
an editorial update.

## 34. References

### 34.1 Canonical repository references

- `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
- `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`
- `shared_context/SAFETY_CONTRACT.md`
- `shared_context/VALIDATION.md`

### 34.2 Official provider evidence snapshot

All links were reviewed as public documentation on 2026-08-01. They support
contract research only; no protected provider API was called.

| Provider | Official source | API/auth/event/deprecation evidence | Licensing or unresolved dependency |
| --- | --- | --- | --- |
| Microsoft | [Security API overview](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0), [security authorization](https://learn.microsoft.com/en-us/graph/security-authorization), [list incidents](https://learn.microsoft.com/en-us/graph/api/security-list-incidents?view=graph-rest-1.0) | Graph Security alert v2 and incident families; Entra permission/role separation; legacy alerts deprecation | Exact product permissions, roles, evidence fields, licenses, retention, and consent are `UNVERIFIED` |
| GitHub | [Secret scanning REST](https://docs.github.com/en/rest/secret-scanning/secret-scanning), [code scanning REST](https://docs.github.com/en/rest/code-scanning/code-scanning?apiVersion=2022-11-28), [Dependabot alerts REST](https://docs.github.com/en/rest/dependabot/alerts) | Read endpoints and fine-grained permissions; distinct mutation surfaces; secret payload sensitivity | GHAS entitlement and exact app/token/org/repo coverage are `UNVERIFIED` |
| Cloudflare | [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/), [Endpoint Management](https://developers.cloudflare.com/api-shield/management-and-monitoring/endpoint-management/), [Security Events](https://developers.cloudflare.com/waf/analytics/security-events/), [Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/) | API Shield posture/inventory, security event/audit families, plan-dependent behavior | Accepted internal Cloudflare contract controls; plan, retention, sampling, and permissions require re-verification |
| Okta | [System Log query](https://developer.okta.com/docs/reference/system-log-query/), [Event Hooks](https://developer.okta.com/docs/concepts/event-hooks/), [Core Okta API](https://developer.okta.com/docs/reference/core-okta-api/), [rate limits](https://developer.okta.com/docs/reference/rate-limits/) | Read-only System Log polling; OAuth/token auth; best-effort at-least-once hooks with duplicates/order caveats | Exact scopes, admin roles, retention, limits, and edition features are `UNVERIFIED` |
| Splunk | [Creating searches with REST](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-tutorials/10.2/rest-api-tutorials/creating-searches-using-the-rest-api), [REST API reference usage](https://help.splunk.com/en/splunk-enterprise/rest-api-reference/9.4/introduction/using-the-rest-api-reference), [HEC](https://help.splunk.com/en/splunk-enterprise/get-data-in/get-started-with-getting-data-in/9.4/get-data-with-http-event-collector/http-event-collector-overview) | Async search jobs/results and capabilities; HEC is an ingestion surface | Cloud API enablement, endpoint subset, ES/notables, licenses, topology, indexes, and retention are `UNVERIFIED` |
| CrowdStrike | [FalconPy](https://github.com/CrowdStrike/falconpy), [Spotlight Vulnerabilities service collection](https://docs.falconpy.io/Service-Collections/Spotlight-Vulnerabilities.html), [Hosts service collection](https://falconpy.io/Service-Collections/Hosts.html), [Falcon Integration Gateway](https://github.com/CrowdStrike/falcon-integration-gateway) | Official SDK read collections; host mutation and event-forwarding surfaces are distinct | Alert/detection generation, incidents, identity, intel, regions, scopes, and licenses are `UNVERIFIED` |
| Snyk | [REST API overview](https://docs.snyk.io/snyk-api/rest-api/about-the-rest-api), [API authentication](https://docs.snyk.io/snyk-api/authentication-for-api), [user-controlled token permissions](https://docs.snyk.io/snyk-api/authentication-for-api/snyk-api-token-permissions-users-can-control), [Projects API](https://docs.snyk.io/snyk-api/reference/projects), [API changelog](https://docs.snyk.io/snyk-api/changelog) | Versioned regional JSON:API, cursor pagination, org/project reads, service-account role differences | Exact least privilege, issue/product coverage, licenses, retention, and rate limits are `UNVERIFIED` |
