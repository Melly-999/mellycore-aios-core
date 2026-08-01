# ADR: MellyCore Enterprise Provider, Integration-Fabric, and Cybersecurity/Marketing Provider Architecture

**Status:** ACCEPTED as architecture and sequencing direction only
(2026-08-01), recorded by `MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001`
on branch `docs/mellycore-enterprise-provider-decision-record-001`,
converting the research synchronized by
`MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001`
(`docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001.md`) into a
canonical decision. **This status explicitly does not authorize runtime
implementation, provider authentication, credential creation, API
execution, MCP connection, deployment, or production use.** It is a
decision/specification-level acceptance only, in the same sense as
`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`'s ACCEPTED status:
it fixes direction and sequencing so that later, separately gated
implementation tasks have a stable target, without itself performing or
authorizing that implementation.

## 1. Context

MellyCore AIOS is a local-first, operator-controlled AI Operations
Observatory (`shared_context/PROJECT_STATE.md`). It is separate from
MellyTrade and performs no broker, trading, or order execution. The
operator supplied architectural research spanning enterprise integration
fabrics, cybersecurity providers, marketing providers, Cloudflare, and the
OpenClaw gateway as an architectural reference. That research was
synchronized into `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, and
`RUN_QUEUE.md` by `MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001` as a
parallel track that does not reorder the live OpenAI Batch API track (whose
current next task, `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001`,
remains unchanged and is unaffected by this decision).

No provider adapter, credential, MCP connection, or runtime integration
exists in this repository today. This ADR is the first canonical
architecture decision for the enterprise-provider track; no earlier
decision record, Provider Registry contract, or Integration Gateway
contract exists in `docs/decisions/`, `docs/specs/`, or elsewhere in this
repository (verified by repository-wide search prior to writing this
record).

## 2. Problem statement

MellyCore needs a stable, tenant-safe, credential-safe architecture for
eventually integrating enterprise cybersecurity, marketing, and
general-business providers, without prematurely committing to specific
vendors, without exposing provider credentials to model context, and
without allowing a single shared gateway process to become a de facto
multi-tenant security boundary. Without this decision, future
implementation work would either stall for lack of direction or proceed
inconsistently across providers.

## 3. Decision

MellyCore adopts the architecture, provider tiers, isolation model,
identity model, credential model, capability/risk model, approval model,
audit model, and external-content posture recorded in Sections 4–20 below
as its accepted direction for enterprise-provider integration. Adapter
implementation remains blocked behind the documentation gate in Section 23
and a separate explicit operator authorization (Section 24).

## 4. Provider integration classes

MellyCore recognizes three provider integration classes:

1. **Native high-trust adapters** — preferred for cybersecurity systems,
   identity systems, security policy systems, deterministic production
   operations, operations requiring stable capability contracts, and
   operations requiring exact approval, audit, and verification semantics.
   A native adapter gives MellyCore full control over the capability
   contract, credential scoping, and read-after-write verification defined
   in Sections 17–19, which a general-purpose fabric cannot guarantee.
2. **Governed integration-fabric adapters** — usable for broad business
   integrations, marketing and CRM workflows, non-critical long-tail APIs,
   deterministic private automation, and delegated-user OAuth flows where
   the fabric provides appropriate governance (audit trail, scoped tokens,
   revocability).
3. **Restricted MCP-assisted operator tools** — usable for controlled
   investigation, documentation/API discovery, operator-assisted
   exploration, and low-risk bounded operations explicitly allowlisted by
   MellyCore. **Unrestricted MCP execution must not be exposed to
   autonomous agents.**

Class selection follows the provider's role, not convenience: a provider
capable of a critical security action (Section 12's R4/R5 tiers) is
integrated through a native adapter or, at minimum, a fabric-mediated path
with equivalent approval/audit guarantees — never through unrestricted MCP.

## 5. Integration-fabric selection

Primary initial candidates: **Composio**, for managed authentication and
agent-tool integration, and **private, self-hosted n8n**, for deterministic
workflows, transformations, webhooks, and controlled automation. Secondary
candidate: **Pipedream Connect**, for long-tail APIs and delegated-user
integrations. Later enterprise candidates: **Tray.ai Agent Gateway** and
**Workato**. Restricted broad-business candidate: **Zapier MCP** — usable
for broad marketing/business integrations, but **must not become the
primary cybersecurity execution boundary**.

These are **architecture selections and implementation candidates only**.
No fabric is configured, credentialed, or connected by this ADR. Selection
of one fabric over another for a specific integration remains subject to
`MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` and the relevant
provider-pack spec.

## 6. Cybersecurity-provider tiers

P0 candidates: Microsoft Defender XDR / Microsoft Graph Security, GitHub
Advanced Security, Cloudflare, Okta. P1/P2 candidates: Splunk, CrowdStrike
Falcon, Snyk.

Initial cybersecurity provider behavior **must be read-only**. Initial
capabilities are limited to inventory, alerts, incidents, security posture,
findings, logs, reporting, correlation, and draft recommendations. Initial
autonomous capabilities **must not include** endpoint isolation, user
blocking, credential revocation, firewall or WAF mutation, incident
resolution, remediation deployment, or any destructive security action —
these remain R4/R5 actions under Section 12 and require explicit human
approval whenever they are eventually implemented.

## 7. Marketing-provider tiers

P0 candidates: HubSpot, Google Ads, Google Analytics 4, Meta Marketing API,
LinkedIn Marketing API, Twilio Segment. Later enterprise/vertical
candidates: Salesforce Marketing Cloud, Braze, Klaviyo, Adobe Experience
Platform.

Initial marketing capabilities **must be read-only or draft-only**:
campaign analytics, CRM search, pipeline analysis, attribution reporting,
audience reporting, performance summaries, draft tasks, and draft
recommendations. The following remain consequential actions requiring
explicit approval whenever implemented: sending communications, publishing
content, activating campaigns, changing campaign status, changing budgets
or bids, modifying audiences, deleting campaigns or assets, changing
consent status, and exporting sensitive customer data.

## 8. Cloudflare decision

Cloudflare is a **P0 cybersecurity-provider candidate** under a future
`Cloudflare Application & API Security Provider` domain. Planned capability
areas: API Shield, API Discovery, Endpoint Management, endpoint labels,
Authentication Posture, Schema Validation 2.0, WAF Rulesets, security
events, audit events, and controlled operator investigation.

**Legacy exclusions (binding on any future Cloudflare connector
contract):**

- Do not implement the deprecated Firewall Rules API
  (`/zones/{zone_id}/firewall/rules`) for new functionality; use the
  Rulesets API for future WAF custom rules.
- Do not use `/api_gateway/user_schemas/hosts` for new integration; prefer
  Schema Validation 2.0 surfaces.
- Do not expose unrestricted Cloudflare MCP execution to autonomous agents.

**Source and verification note.** These exclusions were supplied by the
operator as already-established research and were recorded verbatim by
`MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001`. During this task, live
web access was available and used for a spot check: a fetch of
`https://developers.cloudflare.com/api/resources/api_gateway` (accessed
2026-08-01) did not surface a `user_schemas.hosts` subresource or "Schema
Validation 2.0" wording in its summarized content, and a fetch of
`https://developers.cloudflare.com/api/resources/firewall/subresources/rules`
(accessed 2026-08-01) found no explicit deprecation banner on that raw
resource-reference page itself. Cloudflare's auto-generated API reference
pages commonly omit deprecation banners that appear instead in narrative
migration guides, so this does not contradict the operator's research; it
means this task's own live spot check neither independently confirmed nor
refuted the deprecation wording via those two fetches. The exclusions above
remain the binding MellyCore direction regardless: preferring the actively
developed Rulesets API and Schema Validation 2.0 over older surfaces is a
defensible security posture independent of whether a given reference page
displays a deprecation banner. No Cloudflare API was authenticated, called
with credentials, or mutated by this task or the prior spot check (both
fetches were unauthenticated reads of public documentation pages).

**Consequential Cloudflare operations** (all require explicit approval
whenever a connector is eventually implemented, per Section 12's R4
minimum): adding or deleting managed API operations; replacing label
bindings; uploading, activating, or deleting schemas; changing Schema
Validation actions; setting validation to `block`; creating, updating,
reordering, or deleting WAF rules; changing rate-limiting or
access-control policy. Managed-label replacement is additionally a bulk
mutation and must satisfy Section 18's diff-disclosure requirement.

## 9. OpenClaw findings

OpenClaw is an **architectural reference, not an approved runtime
dependency**. No OpenClaw code, service, or dependency is adopted,
vendored, or connected by this ADR or by the prior roadmap sync. Findings,
informed by the operator-supplied documentation references
(`docs.openclaw.ai/concepts/architecture#gateway-(daemon)`,
`.../gateway/openresponses-http-api`, `.../gateway/protocol#agent-delivery-fallback`,
`.../gateway/external-apps`, `.../reference/rpc`,
`.../gateway/protocol#auth`,
`.../gateway/openresponses-http-api#authentication%2C-security%2C-and-routing`,
recorded here as repository-synchronized research; live web access was not
used to re-fetch these specific pages during this task, so they are
labeled as carried forward from prior research, not independently
re-verified in this session):

- The gateway assumes a **trusted operator boundary**.
- One shared operator-level gateway **must not** be treated as hostile
  multi-tenant isolation.
- Session keys and session identifiers are **routing/context selectors,
  not authorization** (see Section 15).
- Operator-level OpenResponses endpoints **must not** be exposed directly
  to an untrusted frontend.
- Agent-delivery fallback must not silently hide failure of consequential
  security notifications — a failed critical alert must surface as a
  failure, not degrade silently to a lower-visibility channel.
- External applications must pass through MellyCore's own identity,
  tenant, capability, policy, and audit controls (Sections 14–19); OpenClaw
  connectivity, if ever adopted, does not substitute for them.
- OpenClaw terminology may inform MellyCore's own gateway and delivery
  architecture vocabulary without OpenClaw becoming MellyCore's security
  contract.

## 10. Tenant isolation model

Each enterprise tenant requires an **isolated logical authorization
boundary**, consisting at minimum of: tenant-specific provider
registration; tenant-specific credentials; tenant-specific scopes;
tenant-specific policy evaluation; tenant-specific audit attribution;
tenant-specific data retention and classification; and prevention of
cross-tenant session, cache, context, or credential access. Cross-tenant
access attempts must fail closed, not fail open.

For high-impact providers, deployment **may additionally require**: a
separate gateway process; a separate worker or container; a separate
queue; a separate secret namespace; and a separate network policy. **One
shared application process alone is not accepted as sufficient hostile
multi-tenant isolation** — this restates and formalizes the OpenClaw
finding in Section 9 as a MellyCore requirement, not merely an observation
about a third-party reference system.

## 11. Identity model

Seven identity types are distinguished and must not be conflated:

1. MellyCore operator identity
2. Enterprise tenant identity
3. Delegated end-user identity
4. Service-account identity
5. Provider credential identity
6. Agent or runtime identity
7. Session or context identity

Rules: session IDs do not grant authorization (Section 9); delegated-user
credentials must not silently fall back to administrator credentials;
service-account actions must be labeled as service-account actions in
audit records (Section 19), never presented as if a specific human or
delegated user performed them.

## 12. Credential model

Read and write credentials must be separate wherever the provider's
capability model permits it. Write credentials must never enter model
context — an agent may request a write action, but the credential material
itself is resolved and applied outside the context the model can read.
Provider credentials must be accessed through a secrets boundary outside
agent-visible context (a secrets manager or equivalent, not inline
configuration readable by the model). Global or account-owner keys are
prohibited when scoped tokens are available. Credential scope must be
minimized along every applicable axis: tenant, provider, account, zone,
workspace, project, and capability.

## 13. Capability and risk-tier model

Every provider capability, once implemented, must declare: a stable
capability ID; provider ID; operation class; read/write classification;
risk tier; required identity type; required provider scope; tenant scope;
data classification; approval policy; idempotency policy; audit policy;
verification policy; and rollback or containment behavior.

**Risk tiers:**

| Tier | Meaning | Required behavior |
| --- | --- | --- |
| R0 | Passive metadata | May be policy-allowed read-only |
| R1 | Sensitive read | May be policy-allowed read-only |
| R2 | Draft or proposal | Generates a draft/proposed diff, never executes |
| R3 | Reversible mutation | Requires policy evaluation; approval per tenant policy |
| R4 | Consequential mutation | Requires explicit human approval |
| R5 | Critical or potentially destructive security action | Requires explicit human approval, strict preconditions, exact resource enumeration, and enhanced audit |

## 14. Approval model

R0/R1 capabilities may be policy-allowed without per-call human approval.
R2 capabilities produce a draft or proposed diff and stop — they never
execute. R3 capabilities require policy evaluation and may require
approval depending on tenant policy. R4 and R5 capabilities always require
explicit human approval; R5 additionally requires strict preconditions,
exact resource enumeration (no wildcard or implicit scope), and enhanced
audit. This mirrors the per-merge, non-blanket approval pattern already
established for deployment in `shared_context/PROJECT_STATE.md`'s
"Production Deployment Authorization — Model A Contract": one approval
authorizes only the specific action it names, never a standing or future
authorization.

## 15. Audit and verification model

Every mutation, once implemented, must use: (1) a fresh provider-state
read; (2) explicit preconditions; (3) an exact proposed diff; (4) policy
evaluation; (5) human approval when required by Section 14; (6) idempotency
protection; (7) exact execution attribution; (8) read-after-write
verification; (9) an audit ledger entry; and (10) failure containment or
rollback guidance. Bulk replacement operations (e.g. Cloudflare
managed-label replacement, Section 8) must show resources added, resources
removed, and resources unchanged as an explicit diff — never a silent
wholesale replace. **Silent write fallbacks are prohibited**: if a write
cannot be verified or its preconditions are not met, it must fail visibly,
not substitute a different action or credential silently.

## 16. External-content and prompt-injection posture

Provider content is untrusted external input, including but not limited
to: alert titles, incident descriptions, CRM notes, campaign names, logs,
API schemas, endpoint labels, issue text, user-generated content, provider
documentation returned through tools, and webhook payloads. Any future
implementation must apply prompt-injection treatment to such content;
separate data from instructions; preserve provenance; sanitize and
normalize; enforce output-size limits; validate against expected schemas;
and never elevate provider content into trusted policy. This mirrors the
existing repository posture (`shared_context/PROJECT_STATE.md`'s Safety
Boundaries and the Context Gate's admission model) applied specifically to
provider-sourced content.

## 17. Rejected alternatives

- **One unrestricted shared operator gateway for multiple hostile
  tenants** — rejected; see Section 10. A single process boundary does not
  provide adequate isolation against a hostile or compromised tenant.
- **Session keys as authorization** — rejected; see Sections 9 and 11.
  Session keys are routing/context selectors only.
- **Unrestricted MCP execution** — rejected; see Section 4. MCP is
  restricted to controlled investigation and explicitly allowlisted
  low-risk operations.
- **Global API Key use when scoped tokens are available** — rejected; see
  Section 12. Scoped, minimally privileged tokens are required whenever a
  provider supports them.
- **One credential for read and consequential write operations** —
  rejected; see Section 12. Read and write credentials are separated
  wherever the provider permits.
- **Integration fabric as the only cybersecurity execution boundary** —
  rejected; see Sections 4–6. Native adapters are preferred for
  deterministic, high-trust cybersecurity operations; Zapier MCP
  specifically must not become the primary cybersecurity execution
  boundary.
- **Direct frontend access to provider-owner credentials** — rejected;
  provider credentials are resolved behind a secrets boundary outside
  agent- and frontend-visible context (Section 12).
- **Autonomous execution of critical security actions** — rejected; see
  Sections 6 and 13–14. R4/R5 actions always require explicit human
  approval.
- **Immediate implementation of every researched provider** — rejected.
  This ADR fixes architecture and tiering only; implementation proceeds
  provider-by-provider, gated by the sequence in Section 23, not in bulk.
- **Use of the deprecated Cloudflare Firewall Rules API for new
  integration** — rejected; see Section 8. The Rulesets API is the
  accepted future WAF direction.

## 18. Consequences and tradeoffs

**Positive:** future provider work has a stable, pre-agreed architecture,
reducing inconsistent per-provider decisions; tenant and credential
isolation requirements are fixed before any provider code exists, rather
than retrofitted; the R0–R5 risk-tier model gives a uniform vocabulary for
approval requirements across unrelated provider domains (a Cloudflare WAF
mutation and a marketing-campaign activation are both R4 despite being
otherwise unrelated).

**Tradeoffs:** committing to Composio/private-n8n as primary
integration-fabric candidates ahead of a full fabric-comparison spec (item
2 of Section 23) narrows early implementation choices in exchange for
directional clarity; it remains subject to revision at
`MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001` amendment (Section 25)
if the fabric-comparison work surfaces a materially better option. The
seven-item documentation gate (Section 23) intentionally delays any
provider adapter work; this is an accepted cost of the fail-closed posture
this repository already applies to deployment authorization and Batch API
activation.

## 19. Implementation prerequisites

Before any provider adapter scaffolding begins, the following
enterprise-provider documentation tasks must pass, in order:

1. `MELLYCORE-ENTERPRISE-PROVIDER-DECISION-RECORD-001` — this ADR. **Complete
   as a local, unpushed documentation commit.**
2. `MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001` — not started.
3. `MELLYCORE-PROVIDER-REGISTRY-CONTRACT-EXTENSION-001` — not started.
4. `MELLYCORE-INTEGRATION-GATEWAY-SECURITY-CONTRACT-001` — not started.
5. `MELLYCORE-CYBERSECURITY-PROVIDER-PACK-SPEC-001` — not started.
6. `MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001` — not started.
7. `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001` — not
   started.

`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` remains **blocked**, not started,
and not authorized until item 7 passes and a separate, explicit operator
authorization is given — independent of Model A/B deployment authorization
and independent of the OpenAI Batch Stage C gate.

## 20. Explicit non-authorizations

This ADR does **not** authorize: provider implementation of any kind;
provider authentication or credential creation of any kind; any provider
API call, including read-only Cloudflare, cybersecurity, or marketing
calls; any MCP server connection to any provider; any integration-fabric
account, workspace, or credential; deployment of any kind; any marketing
campaign action; any cybersecurity remediation action; or provider adapter
scaffolding. It authorizes architecture and sequencing only.

## 21. Follow-up tasks

See Section 19 for the ordered documentation gate. In addition,
`shared_context/RUN_QUEUE.md`'s "Parallel Decision Track — Enterprise
Provider Integration" is updated by this task to point to this ADR as the
canonical source and to record `MELLYCORE-CLOUDFLARE-API-SHIELD-CONNECTOR-CONTRACT-001`
as the next task on this track.

## 22. Supersession or amendment rules

This ADR may be amended or superseded only by a later, explicitly
identified decision record that references this document by path and
states which section(s) it changes, following the same pattern used by
`docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`'s exact
supersession map (its Section 7). A later document that silently
contradicts this ADR without referencing it does not supersede it; any
such contradiction found during a future review must be corrected, not
treated as an implicit amendment. This ADR's ACCEPTED status is
decision/specification-level only, per this document's Status line and
Section 20, and remains so until a future task explicitly changes it.

## 23. References

- Repository: `shared_context/PROJECT_STATE.md` ("Enterprise Provider
  Integration — Architectural Research Recorded"), `shared_context/ROADMAP.md`
  ("Enterprise Provider Integration — Research Direction"),
  `shared_context/RUN_QUEUE.md` ("Parallel Decision Track — Enterprise
  Provider Integration"), `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-ROADMAP-SYNC-001.md`.
- Repository ADR-format precedent: `docs/decisions/MELLYCORE_3D_RENDERER_HYBRID_ADR_001.md`.
- Repository deployment-authorization precedent for the per-approval,
  non-blanket pattern applied in Section 14:
  `shared_context/PROJECT_STATE.md`'s "Production Deployment Authorization
  — Model A Contract (Temporary, Static-Phase Only)".
- OpenClaw (architectural reference, operator-supplied, not independently
  re-fetched in this session): `docs.openclaw.ai/concepts/architecture#gateway-(daemon)`,
  `docs.openclaw.ai/gateway/openresponses-http-api`,
  `docs.openclaw.ai/gateway/protocol#agent-delivery-fallback`,
  `docs.openclaw.ai/gateway/external-apps`, `docs.openclaw.ai/reference/rpc`,
  `docs.openclaw.ai/gateway/protocol#auth`,
  `docs.openclaw.ai/gateway/openresponses-http-api#authentication%2C-security%2C-and-routing`.
- Cloudflare (spot-checked live, accessed 2026-08-01; see Section 8's
  source note for exact scope and limits of that check):
  `https://developers.cloudflare.com/api/resources/api_gateway`,
  `https://developers.cloudflare.com/api/resources/firewall/subresources/rules`.
  Not independently re-fetched in this session:
  `https://developers.cloudflare.com/api/resources/api_gateway#(resource)%20api_gateway.labels.managed.resources`,
  `https://developers.cloudflare.com/api/resources/api_gateway#(resource)%20api_gateway.user_schemas.hosts`.
