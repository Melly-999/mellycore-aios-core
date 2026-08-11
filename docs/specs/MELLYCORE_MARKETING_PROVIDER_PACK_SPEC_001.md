# MellyCore Marketing Provider Pack Specification 001

## 1. Title and status

- **Contract ID:** `MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001`
- **Task ID:** `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001`
- **Status:** Accepted specification only.
- **Revision:** 001.

Acceptance records a documentation contract. No provider is connected; no
credential exists or is authorized; no adapter or runtime exists; no tracking,
audience, campaign, send, activation, deployment, API operation, MCP connection,
integration-fabric connection, or webhook registration is authorized.

## 2. Purpose

This contract defines a zero-trust, read-oriented Marketing Provider Pack for
analytics, advertising, CRM, customer-data, and engagement systems. It gives
MellyCore stable provider IDs, normalized entity and capability vocabularies,
privacy and identity constraints, and provider-specific inheritance rules.

The pack enables future design and conformance review. It is not an adapter,
identity graph, attribution engine, consent system, marketing automation system,
or runtime-enablement decision.

## 3. Authority and source contracts

Normative repository authority, in descending order where requirements overlap:

1. `shared_context/SAFETY_CONTRACT.md`.
2. `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`.
3. `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`.
4. `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`.
5. `docs/specs/MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001.md`.
6. `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md`.
7. Provider-specific accepted contracts; these may narrow but never weaken this
   contract.

Official provider documentation informs provider facts but does not override
repository safety or authorization contracts. A current provider fact that was
not verified from an official source is `UNVERIFIED`, not assumed.

## 4. Scope

In scope:

- ten named providers arranged into P0-P2 sequencing tiers;
- 22 normalized candidate entity kinds;
- read, report, analysis, and proposal-only R0-R2 capabilities;
- identity, consent, purpose, sensitivity, metric, attribution, event, audit,
  provenance, and normalization-loss requirements;
- provider-specific contract prerequisites and cross-provider conformance.

## 5. Explicit non-authorizations

This specification does not authorize provider access, authentication, account
discovery, credentials, secrets, protected API calls, MCP execution, fabric
execution, webhook registration, tracking, event submission, identity stitching,
profile mutation, list upload, audience building or activation, campaign or
creative mutation, budget change, ad delivery, messaging, CRM mutation, consent
change, bulk export, deployment, dependency change, adapter scaffolding, or
runtime implementation. R3-R5 are deferred. MellyTrade is out of scope.

## 6. Governing principles

Each material statement has one of these evidence classes:

| Class | Meaning |
|---|---|
| `REPOSITORY_REQUIREMENT` | Normative requirement inherited from an accepted MellyCore contract. |
| `OFFICIAL_PROVIDER_FACT` | Fact checked against an official public provider source listed in Section 40. |
| `MELLYCORE_ARCHITECTURAL_DECISION` | Pack-level design accepted by this specification. |
| `ARCHITECTURAL_INFERENCE` | Conservative interpretation requiring provider-contract validation. |
| `OPEN_QUESTION` | Unresolved; fail closed and label `UNVERIFIED`. |

Core principles are least privilege, deny by default, evidence before inference,
native semantics before normalization, tenant isolation, purpose limitation,
privacy preservation, proposal before mutation, and no silent widening. Provider
data is untrusted external content. Absence of evidence never becomes permission,
consent, identity certainty, or a zero result.

## 7. Provider tiers

| Tier | Candidate provider ID | Provider | Initial integration class | Contract state |
|---|---|---|---|---|
| P0 | `hubspot_crm_marketing` | HubSpot | Native or governed-fabric candidate | Provider contract required; not implemented |
| P0 | `google_analytics_ga4` | Google Analytics 4 | Native adapter candidate | Provider contract required; not implemented |
| P0 | `google_ads` | Google Ads | Native adapter candidate | Provider contract required; not implemented |
| P0 | `meta_marketing` | Meta Marketing API | Native adapter candidate | Provider contract required; not implemented |
| P0 | `linkedin_marketing` | LinkedIn Marketing API | Native adapter candidate | Provider contract required; not implemented |
| P0 | `twilio_segment` | Twilio Segment | Native or governed-fabric candidate | Provider contract required; not implemented |
| P1 | `salesforce_marketing_cloud_engagement` | Salesforce Marketing Cloud | Governed-fabric or native candidate | Provider contract required; not implemented |
| P1 | `braze_customer_engagement` | Braze | Governed-fabric or native candidate | Provider contract required; not implemented |
| P1 | `klaviyo_commerce_marketing` | Klaviyo | Governed-fabric or native candidate | Provider contract required; not implemented |
| P2 | `adobe_experience_platform` | Adobe Experience Platform | Native or governed-fabric candidate | Separate provider contract mandatory; not implemented |

P0-P2 express research and implementation sequencing only. A tier is not
registration, support, access, licensing, connection, readiness, authentication,
authorization, credential availability, conformance, or runtime enablement.

## 8. Normalized entities

The following 22 kinds remain separate and stable:

`marketing_provider`, `marketing_account`, `analytics_property`,
`marketing_campaign`, `marketing_ad_group`, `marketing_ad_set`, `marketing_ad`,
`marketing_creative`, `marketing_audience`, `marketing_contact`, `marketing_lead`,
`marketing_profile`, `marketing_segment`, `marketing_event`,
`marketing_conversion`, `marketing_touchpoint`, `marketing_attribution_result`,
`marketing_funnel_stage`, `marketing_metric_snapshot`, `marketing_experiment`,
`marketing_recommendation`, and `marketing_action_proposal`.

Contacts, leads, authenticated users, customer profiles, anonymous visitors,
devices, advertising IDs, organizations, and provider-native profiles must not be
collapsed. Each normalized envelope carries:

- stable normalized ID, provider ID, native object type, and native object ID;
- tenant, provider-native account/property/workspace, and exact resource scope;
- native and observed timestamps, reporting window, timezone, and currency;
- native status/objective, metric definitions, identity and audience references;
- consent, purpose, sensitivity, and external-exposure markings;
- confidence, normalization-loss declarations, extensions, raw evidence reference,
  retrieval provenance, and contract revision.

Raw payloads remain outside model context unless independently admitted by the
context-sensitivity contract.

## 9. Common capabilities

Reserved read/proposal families include:

- `marketing.inventory.*`, `marketing.accounts.read`, `marketing.analytics.read`;
- `marketing.campaigns.read`, `marketing.creatives.read`,
  `marketing.audiences.read`, `marketing.contacts.read`, `marketing.leads.read`;
- `marketing.events.read`, `marketing.conversions.read`,
  `marketing.attribution.read`, `marketing.funnels.read`,
  `marketing.cohorts.read`, and `marketing.segments.read`;
- `marketing.reports.generate`, `marketing.recommendations.propose`,
  `marketing.campaigns.propose`, `marketing.budgets.propose`,
  `marketing.audiences.propose`, `marketing.creatives.propose`, and
  `marketing.crm_tasks.propose`.

Every mapping preserves common capability ID and revision, provider-specific
capability and operation, tenant, exact native resource, acting identity,
credential profile, risk, time window, attribution context, and declared
normalization loss. No generic write capability is defined by this pack.

## 10. Risk classification

Initial pack scope is limited to R0-R2:

- **R0:** passive inventory or non-sensitive metadata with no protected-content
  expansion.
- **R1:** bounded sensitive read/reporting that requires authorization, tenant and
  resource scope, purpose, provenance, and audit.
- **R2:** draft, analysis, recommendation, or action proposal that cannot execute.

R3-R5—including campaigns, sends, budget changes, tracking, audience activation,
identity mutation, CRM changes, data export, consent changes, and destructive or
externally consequential operations—are deferred and unauthorized. Provider
marketing labels do not lower a risk tier.

## 11. Identity and tenant model

The acting-identity chain must preserve requesting principal, delegated human if
any, MellyCore service identity, gateway policy decision, adapter or fabric hop,
provider credential profile, provider-native principal, tenant, account/property/
workspace, and exact resource. Tenant scope and provider-native scope are separate
facts. Cross-tenant correlation, cache reuse, identity linking, or credential
fallback is prohibited.

For every fabric-mediated path, provenance also preserves `fabric_provider_id`,
`downstream_provider_id`, `downstream_tenant_identity`, `delegated_identity`,
`credential_custodian`, `capability_source`, `policy_enforcement_location`,
`audit_source_location`, `data_transit_regions`, `fallback_behavior`, and
`provenance_loss_risk`. A fabric may not obscure the true downstream provider,
actor, capability, resource, policy decision, or approval.

Identity classes remain distinct: anonymous visitor, device/browser ID,
advertising ID, authenticated user, CRM contact, lead, customer profile,
organization/company, household/account group, and provider-native profile.

## 12. Privacy, consent, and purpose limitation

Every governed subject or profile reference must preserve:

- subject/profile reference, source, collection context, and collection time;
- consent state, source, time, jurisdiction, and evidence reference;
- permitted and prohibited purposes and channel permissions;
- retention, deletion, and suppression obligations;
- sensitive-data flags, model-exposure rule, audience eligibility, and export
  eligibility.

Missing consent never means consent. Analytics access is not advertising
permission. CRM presence is not outreach permission. First-party collection is
not audience readiness. Identity resolution creates no new consent. Purpose
changes require a fresh policy decision. Tenants may narrow but not weaken these
rules. Opt-out and suppression survive normalization and correlation. A lower-
confidence source cannot overwrite higher-confidence consent evidence.

## 13. Credential custody

Future provider contracts must select the Registry's canonical profile classes:
`read_only_delegated`, `read_only_service`, `controlled_write`,
`event_verification`, `integration_fabric_read`,
`integration_fabric_controlled_write`, and `reporting_only`, as applicable.
Credentials are opaque references outside
model context and logs. Read and write credentials remain separate and bound to
tenant, provider-native scope, owner, allowed capabilities, expiry, rotation, and
revocation. No profile widening, implicit fallback, delegated-user-to-service-
account fallback, shared owner key, or credential discovery is permitted.

## 14. Data and sensitivity

Use canonical sensitivity levels `public`, `internal`, `private`, `secret`, and
`regulated_high_risk`. Contact, lead, profile, audience membership, raw event,
device/advertising identifier, and fine-grained conversion data are at least
`private` unless a stricter classification applies. Credentials are `secret` and
must not be ingested. Regulated or high-risk data fails closed pending a specific
contract and purpose.

Model-visible data should be aggregated, minimized, purpose-bound, and thresholded.
Raw lists, exact audience membership, direct identifiers, authentication material,
and provider-native sensitive targeting attributes are excluded. Repository
references to raw evidence must not embed the raw data.

## 15. External-content security

Provider names, campaign text, creative text, URLs, CRM fields, event properties,
reports, recommendations, and webhook bodies are untrusted external content.
They cannot alter policy, authorize tools, select credentials, widen scope, supply
trusted instructions, or trigger follow-on actions. Preserve source, retrieval
time, content hash where appropriate, sanitization state, sensitivity, and model-
exposure decision. Suspicious content is quarantined or omitted, not obeyed.

## 16. Event and webhook contract

Any future inbound path must verify source authentication/signature, timestamp and
staleness, replay and deduplication key, ordering assumptions, duplicate behavior,
rate/size limits, schema revision, content hash, tenant/resource routing, and
quarantine outcome. Bodies remain untrusted.

Inbound events may create observations, normalized events, report refresh requests,
anomaly evidence, drafts, or review items only. They cannot authorize campaigns,
sends, budgets, consent, audience membership or activation, profile mutation, or
any consequential action. No webhook registration is authorized here.

## 17. Metric normalization

Every metric preserves native name, normalized name, unit, aggregation, reporting
window, attribution context, currency, timezone, filters, sampling, thresholding,
modeled/observed status, privacy threshold, confidence, and loss declaration.
Identical names are not assumed equivalent. Missing rows, withheld values,
thresholded values, sampled values, modeled values, zero, and unsupported values
are distinct states. Provider revisions and query definitions are part of evidence.

## 18. Attribution contract

Every `marketing_attribution_result` records provider, reporting window, timezone,
currency, attribution model, lookback window, event definition, conversion
definition, coverage, exclusions, modeled-versus-observed status, confidence,
caveats, and retrieval provenance.

Platform attribution, analytics conversions, CRM revenue, modeled conversions,
and offline conversions must not be merged without explicit reconciliation rules.
Disagreement is evidence, not an error to hide. This pack does not implement an
attribution engine or declare a cross-provider source of truth.

## 19. Identity-resolution contract

Deterministic and probabilistic links remain distinct. Weak, recycled, shared, or
provider-controlled identifiers cannot silently merge profiles. Email or phone
alone is not sufficient in every context. Cross-tenant links are prohibited. A
provider identity graph is not authoritative truth; ambiguity and link rationale
must be explicit. Model-suggested links are R2 proposals only. Consent, purpose,
suppression, provenance, and confidence survive every proposed link. This pack
does not implement an identity graph.

## 20. Cross-provider correlation

Correlation requires tenant isolation, native evidence references, deterministic-
versus-heuristic classification, confidence, rationale, ambiguity, and declared
loss. It cannot silently reconcile attribution, currency, timezone, reporting
windows, identities, consent, campaign status, or metric definitions. Data from
one provider cannot be copied to another, used to create consent, or activated as
an audience. Cross-provider outputs are reports or proposals, never execution.

## 21. Proposal-only outputs

Permitted R2 candidates are performance, funnel, attribution, budget, channel,
audience, segment, campaign, creative-brief, CRM-task, tracking-plan,
instrumentation, and consent/data-quality proposals. Every proposal is visibly
nonexecuting and includes evidence, provider/native resources, reporting window,
assumptions, limitations, uncertainty, sensitivity, purpose, and future approval
requirements. It must not claim that a provider accepted, scheduled, published,
sent, changed, or activated anything.

## 22. HubSpot profile

Candidate read scope: accounts, CRM object/property metadata, contacts, companies,
deals, lifecycle evidence, marketing-event metadata, engagement metadata, and
bounded campaign/funnel/lead analysis. Candidate R2 scope: CRM task and segment
proposals.

`OFFICIAL_PROVIDER_FACT`: HubSpot exposes distinct CRM object and property APIs,
contact read/write scopes, CRM search, and a marketing-events object surface.
`ARCHITECTURAL_INFERENCE`: exact marketing-campaign semantics, licensing, OAuth
scopes, association limits, rate limits, archived-record handling, sensitive-
property access, and webhook verification remain `UNVERIFIED` for a provider
contract.

Deferred: contact/company/deal create/update/delete, property or lifecycle changes,
assignment, workflow/enrollment, subscription or consent changes, campaign
publication, send, and bulk export. CRM access does not imply marketing-contact,
subscription, outreach, or audience permission.

## 23. Google Analytics 4 profile

Candidate read scope: property and metadata inventory, bounded Data API reports,
realtime reports, acquisition, events, key-event/conversion reporting, funnels,
and cohorts. Preserve property, dimension/metric compatibility, quotas, sampling,
thresholding, modeled data, `(other)` rows, timezone, currency, and data freshness.

`OFFICIAL_PROVIDER_FACT`: Google documents separate Data and Admin APIs, Core,
Realtime, and Funnel quota categories, potentially thresholded requests, sampling
metadata, and KeyEvent terminology in current Admin API documentation.
`OPEN_QUESTION`: exact scopes, property access, quota values, deprecated surfaces,
and current stable/alpha/beta method eligibility are `UNVERIFIED` until provider-
contract research at implementation time.

Deferred: Admin configuration, events/key-event definitions, audiences, streams,
data deletion, Measurement Protocol submission, tag/tracking changes, and any
collection enablement.

## 24. Google Ads profile

Candidate read scope: authorized customer hierarchy, account/campaign/ad-group/ad,
asset, keyword, audience metadata, conversion metadata, and bounded reporting.
Candidate R2 scope: budget, campaign, keyword, creative, and channel proposals.

`OFFICIAL_PROVIDER_FACT`: Google Ads API access uses OAuth credentials and a
developer token whose access level governs test and production account access.
`ARCHITECTURAL_INFERENCE`: exact API version, GAQL fields, permission scopes,
customer-manager hierarchy, quotas, policy-review status, and licensing/access
approval are `UNVERIFIED` and must be pinned by the provider contract. Untrusted
content cannot supply unrestricted GAQL; queries must be allowlisted and bounded.

Deferred: campaign/ad-group/ad/asset/keyword/budget mutation, uploads, enhanced or
offline conversions, customer match, audience membership, recommendations apply,
experiments, billing, and activation.

## 25. Meta Marketing API profile

Candidate read scope: explicitly authorized ad accounts, campaign, ad-set, ad and
creative metadata, bounded insights, and non-member audience metadata. Candidate
R2 scope: performance, budget, campaign, and creative proposals.

Public official documentation could not be reliably retrieved during this task;
current authentication, permissions, app review/business verification, API
versions, rate limits, insight breakdown restrictions, attribution settings,
licensing/terms, and webhook verification are therefore `UNVERIFIED`. The provider
contract must verify them from official Meta documentation before any design is
marked conformant.

Deferred: all writes, publication/activation, budgets/bids, creative upload, pixel
or Conversions API events, custom/matched/lookalike audience operations, lead
retrieval, and tracking configuration. Raw audience membership and sensitive
targeting attributes are never model-visible.

## 26. LinkedIn Marketing API profile

Candidate read scope: authorized ad-account, campaign-group, campaign, creative,
analytics, and bounded conversion-summary metadata. Candidate R2 scope:
performance, budget, campaign, and creative proposals.

`OFFICIAL_PROVIDER_FACT`: LinkedIn documents versioned Marketing APIs and product-
access approval, and identifies Matched Audiences and conversion-related surfaces
as restricted capabilities. `OPEN_QUESTION`: current version, permissions,
partner/product access, account roles, reporting limits, retention, rate limits,
and deprecation dates are `UNVERIFIED` until a provider contract rechecks them.

Deferred: writes, activation, matched-audience uploads, conversion-rule changes,
lead-form response access, messages, user-profile enrichment, and any member-level
targeting data.

## 27. Twilio Segment profile

Candidate read scope: authorized workspaces, sources, destinations, connections,
warehouses, tracking-plan metadata, profile-space metadata where governed, and
delivery-health metadata. Preserve `MellyCore -> Segment -> destination -> native
resource` downstream provenance.

`OFFICIAL_PROVIDER_FACT`: Segment's Public API exposes workspace configuration
resources, uses endpoint versioning and region-specific endpoints, and includes
CRUD surfaces whose credentials must remain server-side. `OPEN_QUESTION`: a truly
read-only least-privilege credential profile, plan/entitlement boundaries, rate
limits, profile-space exposure, EU/US routing, and delivery metric semantics are
`UNVERIFIED`.

Deferred: source/destination creation or enablement, tracking-plan mutation, event
submission, identity merge, profile/audience operation, warehouse mutation,
deletion, and replay. Segment is not an authorization source.

## 28. Salesforce Marketing Cloud profile

P1 candidate read scope: business-unit inventory, campaign/journey/asset metadata,
data-extension schema and governed counts, subscriber aggregate counts, and
bounded performance reporting through applicable REST/SOAP surfaces.

`OFFICIAL_PROVIDER_FACT`: Salesforce Marketing Cloud documents REST resources for
campaigns, contacts and journeys, and data extensions whose ownership and scope
interact with business units. `OPEN_QUESTION`: product edition, Installed Package
OAuth scopes, tenant subdomain, business-unit inheritance, SOAP/REST parity,
retention, rate limits, event-notification verification, and governed row access
are `UNVERIFIED`.

Deferred: sends, journey activation/change, subscriber or subscription mutation,
data-extension row access absent an explicit governed purpose, data-extension
mutation, content change, and contact deletion.

## 29. Braze profile

P1 candidate read scope: campaign, Canvas, segment metadata, aggregate analytics,
event-name metadata, delivery/performance summaries, and bounded export metadata.

`OFFICIAL_PROVIDER_FACT`: Braze documents instance-specific REST endpoints and API
keys with endpoint permissions, including separate read/export and messaging/user
mutation surfaces. `OPEN_QUESTION`: workspace entitlement, exact key permissions,
current endpoint versions, export privacy limits, regional routing, rate limits,
retention, and webhook/security model are `UNVERIFIED`.

Deferred: sends, campaign/Canvas activation or mutation, user/profile/subscription
mutation, segment mutation, personalization, content-card, push, and raw user
export.

## 30. Klaviyo profile

P1 candidate read scope: profile/list/segment metadata and aggregate counts,
campaign, flow, metric, event-schema, template, and performance metadata. Direct
profile or event records require a separate sensitivity and purpose decision.

`OFFICIAL_PROVIDER_FACT`: Klaviyo documents OAuth for applications, private-key
authentication, revision headers, endpoint-specific scopes, per-account/app rate
limits, and `429` handling. `OPEN_QUESTION`: current revision, plan entitlements,
least-privilege scopes, retention, privacy deletion, webhook verification, and
bulk access boundaries are `UNVERIFIED` and must be repinned.

Deferred: profile/list/subscription/suppression mutation, sends, flow activation or
change, template mutation, event submission, audience synchronization, and raw
profile export.

## 31. Adobe Experience Platform profile

P2 candidate read scope is metadata-only by default: sandboxes, schemas, datasets,
identity namespaces, merge-policy metadata, audience definitions without member
lists, destination configuration metadata, governance labels, lineage, and
authorized query metadata.

`OFFICIAL_PROVIDER_FACT`: Adobe Experience Platform documents sandbox-isolated
APIs with organization and sandbox headers across Schema, Catalog/Datasets,
Identity, Profile, Segmentation/Audiences, Destinations, Query, and governance
surfaces. Those surfaces include consequential CRUD, ingestion, stitching,
activation, and deletion operations.

Deferred: ingestion, raw profile access, identity stitching, audience evaluation or
activation, destination export, schema/dataset/governance mutation, data hygiene,
and query execution over sensitive data. Exact authentication, roles, sandbox,
licensing, regional boundaries, API stability, and quotas are `UNVERIFIED`. A
separate provider contract is mandatory before any adapter design.

## 32. Cross-provider conformance matrix

| Provider | Candidate ID | Tier | Integration class | Initial read entities | Initial capabilities | Explicit exclusions | Sensitive-data boundary | Event/webhook posture | Credential profile | Licensing/access unknowns | Contract status |
|---|---|---:|---|---|---|---|---|---|---|---|---|
| HubSpot | `hubspot_crm_marketing` | P0 | Native/fabric candidate | account, contact, lead, campaign, event, funnel, metric | inventory, contacts/leads/events/funnels read; reports/proposals | CRM writes, enrollment, subscriptions, sends, bulk export | direct CRM fields private; no outreach inference | inbound observation only; registration deferred | delegated/service read TBD | hubs, scopes, sensitive properties | Required; not implemented |
| GA4 | `google_analytics_ga4` | P0 | Native candidate | account, property, event, conversion, funnel, metric, attribution | metadata, analytics, events, conversions, funnels, cohorts | Admin changes, Measurement Protocol, tracking, deletion | aggregated/thresholded reports preferred | collection/admin changes deferred | delegated/service read TBD | property roles, quotas, alpha/beta features | Required; not implemented |
| Google Ads | `google_ads` | P0 | Native candidate | account, campaign, ad group, ad, creative, audience, conversion, metric | inventory, campaigns/creatives/audiences/conversions read; proposals | every mutation, upload, match, apply, billing | no member lists or sensitive targeting | conversion upload/webhooks deferred | OAuth read + developer-token ref TBD | access level, policy approval, versions | Required; not implemented |
| Meta | `meta_marketing` | P0 | Native candidate | account, campaign, ad set, ad, creative, audience, metric | bounded metadata/insights; proposals | writes, activation, pixel/CAPI, custom audience, lead data | no raw membership or sensitive targeting | inbound observation only; verification TBD | read profile TBD | permissions, app review, verification, version | Required; not implemented |
| LinkedIn | `linkedin_marketing` | P0 | Native candidate | account, campaign, creative, conversion, metric | bounded campaign/creative/analytics read; proposals | writes, matched audience, lead forms, messages, member enrichment | no member-level targeting/export | event use deferred | read profile TBD | product/partner approval, roles, versions | Required; not implemented |
| Segment | `twilio_segment` | P0 | Native/fabric candidate | account, event metadata, profile-space metadata, metric | inventory, metadata, delivery health | config CRUD, tracking, submit, merge, audience, replay | no raw event/profile/member data by default | downstream provenance; inbound observation only | reporting/read profile TBD | plan, regions, read-only credential availability | Required; not implemented |
| Salesforce MC | `salesforce_marketing_cloud_engagement` | P1 | Native/fabric candidate | account, campaign, segment schema, metric | inventory, bounded aggregate reports | sends, journeys, subscriber/DE mutation or raw rows | business-unit scoped; raw subscriber rows excluded | notifications observation only | installed-package read TBD | edition, BU, REST/SOAP, scopes | Required; not implemented |
| Braze | `braze_customer_engagement` | P1 | Native/fabric candidate | account, campaign, segment metadata, event metadata, metric | inventory, aggregate analytics | sends, Canvas/user/subscription/segment mutation, raw export | no raw user/profile export | observation only; verification TBD | endpoint-permission read key TBD | package, instance, permissions | Required; not implemented |
| Klaviyo | `klaviyo_commerce_marketing` | P1 | Native/fabric candidate | account, campaign, segment/list metadata, event/metric | metadata and aggregate reporting | profile/list/subscription/send/flow/template/event writes | direct profiles/events separate gate | observation only; verification TBD | OAuth/private read profile TBD | plan, revisions, scopes | Required; not implemented |
| Adobe AEP | `adobe_experience_platform` | P2 | Native/fabric candidate | sandbox/schema/dataset/namespace/audience/destination/lineage metadata | inventory and governance metadata only | ingest, profile, stitch, activate, mutate, sensitive query | metadata default; no member/profile/dataset rows | observation only; registration deferred | sandbox-bound service/delegated read TBD | licenses, roles, sandboxes, quotas | Separate contract mandatory; not implemented |

## 33. Provider-specific contract requirements

Before any provider becomes registry-eligible, its accepted contract must pin:

1. official product/API family, exact version and deprecation policy;
2. authentication family, acting identity, tenancy, native account hierarchy, and
   least-privilege credential profiles;
3. explicit allowlisted read operations, schemas, pagination, query bounds,
   quotas, rate behavior, freshness, retention, and licensing/access gates;
4. entity and capability mappings with loss, sensitivity, purpose, consent,
   metric, attribution, and error semantics;
5. event/webhook signature, replay, ordering, dedupe, quarantine, and provenance;
6. audit and delivery semantics, unknown-outcome handling, and failure containment;
7. R3-R5 exclusions and any future separately reviewed mutation contract;
8. conformance tests and supersession rules.

A provider contract may narrow these requirements but cannot weaken them.
Any future MCP representation is separately registered, tenant- and credential-
bound, tool-allowlisted, mutation-prohibited for this pack, and non-autonomous.
MCP discovery does not authorize execution, and unrestricted search-and-execute is
prohibited. A fabric's or MCP server's governance is additive and cannot replace
MellyCore Gateway policy, approval, audit, or provenance.

## 34. Implementation sequencing

Candidate sequence:

1. GA4 bounded reporting and metric-loss validation.
2. HubSpot read-only CRM/funnel metadata.
3. Google Ads bounded reporting.
4. Segment topology and downstream-provenance metadata.
5. Meta bounded insights.
6. LinkedIn bounded analytics.
7. cross-provider metric-normalization conformance.
8. attribution and funnel reconciliation as non-authoritative reports.
9. Klaviyo metadata/reporting.
10. Braze metadata/reporting.
11. Salesforce Marketing Cloud metadata/reporting.
12. Adobe Experience Platform metadata-only exploration.

This ordering favors aggregate analytics and evidence-model validation before
identity-rich engagement platforms. It is a planning decision only, not approval,
readiness, access, or an adapter-scaffolding authorization.

## 35. Testing and validation requirements

Future provider contracts and implementations must test:

- Provider Registry independence and fail-closed authorization facts;
- tenant/native-resource and acting-identity isolation;
- read/write credential separation and absence of fallback;
- consent, purpose, suppression, sensitivity, and model-exposure enforcement;
- normalized IDs, native evidence, loss, time, currency, metric and attribution
  semantics;
- bounded pagination/query limits, rate limits, partial results, thresholding,
  sampling, privacy suppression, schema/version drift, and staleness;
- untrusted content, malicious field names/text, webhook replay, duplicates,
  ordering, signature failure, and quarantine;
- audit failure, provider timeout, revoked credentials, unknown results, and
  cross-provider disagreement;
- proof that R2 outputs cannot execute and every R3-R5 path is absent or blocked.

No live provider test is authorized by this document.

## 36. Rejected designs

Rejected:

- treating a tier, registration, capability existence, or connection as runtime
  authorization;
- one broad marketing super-credential or delegated-to-service fallback;
- a generic write capability or proposal that can execute;
- provider data, webhooks, MCP discovery, or fabric metadata as authority;
- silent contact/profile/device/advertising-ID merging;
- consent inferred from data presence, account access, first-party collection, or
  identity resolution;
- raw audience, profile, lead, subscriber, or sensitive targeting data in model
  context;
- silent metric, attribution, timezone, currency, or identity reconciliation;
- mutation retries without idempotency, reconciliation, and read-after-write;
- provider-specific weakening of generic contracts.

## 37. Implementation prerequisites

The Provider Registry preserves eight independent facts for every provider and
capability:

| # | Fact | Required state before future runtime use |
|---:|---|---|
| 1 | Provider registered | A conforming record at `registration_status: conformance_verified`; implies no other fact |
| 2 | Adapter implemented | `adapter_state: implemented` or `test_verified`, with evidence |
| 3 | Credential configured | Resolvable secret-manager reference for the exact required credential class |
| 4 | Credential verified | Dated successful verification, active revocation state, and unexpired credential |
| 5 | Tenant authorized | Explicit tenant-provider authorization record |
| 6 | Capability authorized | Explicit tenant-capability authorization within exact resource scope |
| 7 | Runtime enabled | Explicit enablement for the exact runtime environment |
| 8 | Operation approved | For R3-R5 only, valid unexpired digest-bound approval for the exact operation and target |

Registration is not runtime authorization. Capability existence is not
permission. Authentication is separate from authorization. Tenant scope is
separate from provider-native scope. Stable provider and capability IDs remain
mandatory. All eight facts are conjunctive and independently evidenced and
revoked; one missing, unknown, expired, or unresolved fact denies. Facts 1-7 are
standing state, while fact 8 is per-operation. No aggregate `enabled`, `ready`,
`connected`, or `active` field may collapse them.

Before scaffolding,
`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002` must pass after
this remediation. Any future R3-R5 work additionally
requires exact target-bound approval, fresh state, separate write credentials,
mandatory audit (whose failure blocks consequential action), idempotency,
read-after-write verification, and reconciliation of unknown outcomes. Stale state
invalidates approval; blind mutation retry is prohibited.

## 38. Open questions

The provider-specific `UNVERIFIED` items in Sections 22-31 and 40 are blocking
inputs to provider contracts. Cross-pack questions also remain:

- Which aggregate/privacy thresholds qualify a metric for model visibility?
- Which consent authority and jurisdiction rules are canonical per tenant?
- Which identity-link evidence grades are permitted for R2 proposals?
- Which currency/timezone and attribution reconciliation methods are acceptable?
- Which providers support genuinely read-only credential profiles?
- Which integration class best preserves each provider's native semantics and
  downstream provenance?

Open questions do not grant permission. They fail closed.

## 39. Amendment and supersession

Changes require a new reviewed revision or an explicit superseding contract.
Provider documentation drift does not silently amend this specification. A
provider-specific contract supersedes only its explicitly identified narrower
details and cannot weaken the enterprise ADR, Provider Registry, Integration
Gateway, safety, sensitivity, audit, or provenance requirements. Historical
revisions remain evidence. Runtime and credentials require separate authorization.

## 40. References and official-source evidence register

Repository references are listed in Section 3. The following public official
sources were consulted on 2026-08-01; access does not authorize provider use.

| Provider | Official source | API family | Authentication family | Candidate read surfaces | Event/webhook model | Versioning/deprecation | Licensing/access dependency | Open questions |
|---|---|---|---|---|---|---|---|---|
| HubSpot | [CRM contacts](https://developers.hubspot.com/docs/api-reference/latest/crm/objects/contacts/guide), [CRM properties](https://developers.hubspot.com/docs/api-reference/latest/crm/properties/guide), [CRM search](https://developers.hubspot.com/docs/api-reference/latest/crm/search-the-crm), [marketing events](https://developers.hubspot.com/docs/api-reference/latest/marketing/marketing-events/guide), [webhooks](https://developers.hubspot.com/docs/api-reference/latest/webhooks/guide) | CRM objects/properties/search; marketing events | OAuth or private-app token family; exact profile `UNVERIFIED` | CRM and marketing-event metadata | App webhook subscriptions; registration deferred | Latest/versioned pages; exact pinned version `UNVERIFIED` | Product/scopes/sensitive properties `UNVERIFIED` | Exact scopes, limits, campaign semantics, verification |
| GA4 | [Data quotas](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas), [data expectations](https://developers.google.com/analytics/devguides/reporting/data/v1/reporting-data-expectations), [metadata](https://developers.google.com/analytics/devguides/reporting/data/v1/rest/v1alpha/properties/getMetadata), [Admin API](https://developers.google.com/analytics/devguides/config/admin/v1), [Admin REST](https://developers.google.com/analytics/devguides/config/admin/v1/rest), [changelog](https://developers.google.com/analytics/devguides/config/admin/v1/changelog) | Data API; Admin API metadata only | User or service auth family; exact scopes `UNVERIFIED` | properties, metadata, bounded reports | Collection/configuration excluded | v1 plus alpha/beta surfaces; reverify | Property role/quota eligibility `UNVERIFIED` | Stable methods, scopes, thresholds, freshness |
| Google Ads | [developer tokens](https://developers.google.com/google-ads/api/docs/api-policy/developer-token), [OAuth credential management](https://developers.google.com/google-ads/api/docs/oauth/credential-management), [access levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels) | Google Ads API/GAQL | OAuth plus developer token | customer hierarchy and bounded reports | Upload/mutation paths excluded | Exact current API version `UNVERIFIED` | Token access level and policy approval | GAQL allowlist, scopes, hierarchy, quotas |
| Meta | [Marketing API insights](https://developers.facebook.com/docs/marketing-api/insights/), [authorization overview](https://developers.facebook.com/docs/marketing-api/overview/authorization/) | Marketing API | `UNVERIFIED` | account/object metadata and bounded insights candidate | `UNVERIFIED`; registration deferred | `UNVERIFIED` | App review/business verification/permissions `UNVERIFIED` | All current auth, versions, limits, terms |
| LinkedIn | [Marketing APIs](https://learn.microsoft.com/en-us/linkedin/marketing/), [access approval](https://learn.microsoft.com/en-us/linkedin/marketing/increasing-access) | LinkedIn Marketing APIs | OAuth/product permissions; exact profile `UNVERIFIED` | ad entities and bounded analytics | `UNVERIFIED`; consequential surfaces deferred | Explicit versions/sunsets; current pin `UNVERIFIED` | Product and partner approval | roles, scopes, reporting/retention limits |
| Segment | [Public API](https://www.twilio.com/docs/segment/api/public-api), [Config API](https://www.twilio.com/docs/segment/api/config-api) | Public/Config API | Public API token family; read-only profile `UNVERIFIED` | workspace/source/destination/tracking metadata | Delivery metadata candidate; tracking submission excluded | Endpoint versioning; current pins required | Plan/region/features `UNVERIFIED` | least privilege, region, quotas, profile access |
| Salesforce Marketing Cloud | [REST overview](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/rest-api-overview.html), [data extensions](https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/dataextension.htm) | REST/SOAP product surfaces | Installed Package OAuth family `UNVERIFIED` | business-unit, journey/campaign/schema metadata | Event model `UNVERIFIED`; registration deferred | Product-specific; exact versions `UNVERIFIED` | Edition/BU/scopes `UNVERIFIED` | auth, tenancy, parity, retention, limits |
| Braze | [API basics](https://www.braze.com/docs/api/basics), [campaign export](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns/) | REST API | Endpoint-permission API key | campaign/Canvas/segment and aggregate metadata | `UNVERIFIED`; registration deferred | Endpoint docs; exact revisions `UNVERIFIED` | Package/instance/permissions | export privacy, region, rate/retention |
| Klaviyo | [API overview](https://developers.klaviyo.com/en/v2024-07-15/reference/api_overview), [rate limits](https://developers.klaviyo.com/en/docs/rate_limits_and_error_handling), [list read](https://developers.klaviyo.com/en/reference/get_list) | Klaviyo API | OAuth or private key; exact read profile required | list/segment/campaign/flow/metric metadata | `UNVERIFIED`; event submission excluded | Revision header required; repin current revision | Plan/scopes `UNVERIFIED` | least privilege, retention, webhook verification |
| Adobe Experience Platform | [Platform overview](https://experienceleague.adobe.com/en/docs/experience-platform), [API guide](https://experienceleague.adobe.com/en/docs/experience-platform/landing/platform-apis/api-guide), [sandboxes](https://experienceleague.adobe.com/en/docs/experience-platform/sandbox/api/getting-started), [audiences](https://experienceleague.adobe.com/en/docs/experience-platform/segmentation/api/audiences), [datasets](https://experienceleague.adobe.com/en/docs/experience-platform/catalog/datasets/overview), [destinations](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/home) | Schema/Catalog/Identity/Profile/Segmentation/Destinations/Query/governance | Adobe auth plus org/sandbox headers; exact profile `UNVERIFIED` | metadata only by default | Ingest/activation excluded; event model `UNVERIFIED` | Service-specific; exact pins required | Product licenses, roles, sandboxes | auth, region, quotas, permitted metadata |

If an official page changes, becomes inaccessible, or conflicts with this evidence
register, the related fact becomes `UNVERIFIED` until a provider-contract review
re-establishes it. No third-party article is normative.
