# MellyCore Integration Fabric Comparison Specification 001

## 1. Title and status

- **Contract ID:** `MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001`
- **Version:** 1.0
- **Status:** `SPECIFICATION_ACCEPTED · EVIDENCE_NOT_YET_PRODUCED`
- **Scope:** documentation and future conformance evidence only

No fabric is selected, connected, configured, credentialed, authenticated, or
authorized by this specification. No provider API, MCP server, webhook, runtime,
deployment, account, workspace, or paid service is used or created.

## 2. Purpose

Own the comparison prerequisite named by the Enterprise Provider ADR and define
the positive evidence standard by which a fabric-mediated path can be judged
equivalent to a native adapter for a bounded MellyCore capability.

## 3. Authority

Requirements inherit, without weakening, from:

1. `shared_context/SAFETY_CONTRACT.md`;
2. `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`;
3. `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`;
4. `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`;
5. accepted provider-specific and provider-pack contracts.

## 4. Ownership decision

This document owns candidate comparison, evidence shape, positive
native-equivalence criteria, and assessment outcomes. The Registry owns provider,
credential-profile, capability, and authorization-record metadata. The Gateway
owns runtime policy evaluation. Provider contracts own native semantics. No new
ADR is required because this specification operationalizes, rather than changes,
the accepted ADR's direction and fail-closed boundary.

## 5. Candidates in scope

Composio; private self-hosted n8n; Pipedream Connect; Tray.ai Agent Gateway;
Workato; restricted Zapier MCP; and OpenClaw as an architectural reference only.
Candidate naming is inventory, not selection or authorization.

## 6. Candidate disposition

| Candidate | Architectural role | v1 disposition |
| --- | --- | --- |
| Composio | managed auth / agent-tool candidate | `PRIMARY_CANDIDATE · INSUFFICIENT_EVIDENCE` |
| private self-hosted n8n | deterministic workflow / audit candidate | `PRIMARY_CANDIDATE · INSUFFICIENT_EVIDENCE` |
| Pipedream Connect | managed embedded-integration candidate | `SECONDARY_CANDIDATE · INSUFFICIENT_EVIDENCE` |
| Tray.ai Agent Gateway | governed enterprise-orchestration candidate | `SECONDARY_CANDIDATE · INSUFFICIENT_EVIDENCE` |
| Workato | enterprise integration candidate | `SECONDARY_CANDIDATE · INSUFFICIENT_EVIDENCE` |
| restricted Zapier MCP | operator-restricted MCP candidate | `RESTRICTED · CYBERSECURITY_EXECUTION_PROHIBITED` |
| OpenClaw | architectural comparison reference | `REFERENCE_ONLY · NOT_A_RUNTIME_DEPENDENCY` |

Composio and private self-hosted n8n remain the ADR's primary candidates; this is
directional prioritization, not a winner declaration.

## 7. Unit of assessment

Equivalence is never awarded to a vendor globally. The assessment key is the
exact tuple `(fabric_provider_id, downstream_provider_id, capability_class,
tenant_model, credential_custody_mode, fabric_revision, downstream_contract_revision,
gateway_contract_revision)`. A pass for one tuple grants nothing to another.

## 8. Comparison dimensions

Identity continuity; tenant isolation; downstream scope fidelity; credential
custody; class determinism; capability bounding; approval binding; audit
completeness; provider request-ID preservation; idempotency; concurrency; retry
semantics; unknown-outcome reconciliation; read-after-write verification;
containment; data transit/retention; regional controls; webhook security;
external-content handling; tool-set stability; fallback behavior; suspension;
revocation propagation; exportability; operator visibility; and failure honesty.

## 9. Evidence classes

Accepted evidence is one of: `CONTRACT_EVIDENCE`, `CONFIGURATION_EVIDENCE`,
`CONTROL_TEST_EVIDENCE`, `FAILURE_INJECTION_EVIDENCE`, `AUDIT_TRACE_EVIDENCE`,
`PROVIDER_DOCUMENTATION_EVIDENCE`, or `OPERATOR_ATTESTATION_EVIDENCE`.
Marketing copy, tool descriptions, feature matrices without control details,
screenshots without reproducible context, and MCP/fabric output are not evidence.

## 10. Evidence record

Each evidence item requires stable ID, assessment key, evidence class, source,
collector, collection time, environment, exact versions, method, sanitized
artifact reference, result, limitations, sensitivity, expiry/review date, and
independent reviewer. Missing provenance makes the item inadmissible.

## 11. Native baseline

The comparison first records the conforming native-adapter baseline from Gateway
§19 for the same downstream provider and capability. If no accepted native
contract exists, equivalence cannot be assessed and the outcome is
`INSUFFICIENT_EVIDENCE`.

## 12. Identity equivalence

Evidence MUST show the authenticated requester, tenant, delegated user or
labelled service account, MellyCore policy actor, fabric, downstream principal,
provider, and target remain distinct and reconstructable. Substitution,
impersonation, or a missing link fails.

## 13. Tenant and scope equivalence

Evidence MUST demonstrate tenant-isolated credentials, queues, caches, context,
idempotency keys, audit, and responses; exact provider-native allowlists; and
denial of cross-tenant, wildcard, and out-of-scope requests. Fabric tenancy alone
is insufficient.

## 14. Credential equivalence

Evidence MUST show one exact Registry §13.2 class resolves deterministically,
secret material stays outside model-visible context, read/write separation holds,
revocation fails closed, and no broader-profile, delegated-to-service, or
cross-tenant fallback exists.

## 15. Capability equivalence

Every fabric operation MUST map one-to-one to a registered bounded MellyCore
capability. Arbitrary HTTP, generic execute, dynamic mutation discovery, raw
method/path passthrough, and undocumented actions fail.

## 16. Approval equivalence

For R3–R5, evidence MUST show the Gateway's exact request binding is preserved
through execution: tenant, provider, capability/revision, actor, target set,
before state, diff, risk, credential class, expiry, request fingerprint, and
policy decision. Fabric approval cannot substitute for MellyCore approval.

## 17. Audit equivalence

Evidence MUST reproduce the Gateway's durable Stage A intent reservation before
an external mutation and append-only Stage B attempt/response/verification/
delivery evidence afterward. Missing audit, invented request IDs, or a single
collapsed success flag fails.

## 18. Failure-semantics equivalence

Evidence MUST demonstrate no blind mutation retry; unknown outcomes reconcile by
fresh authoritative read; stale state invalidates approval; concurrency conflicts
deny; fallback triggers a fresh policy decision and approval; and partial
application remains explicit.

## 19. Verification and containment equivalence

Every mutation requires authoritative read-after-write verification against the
approved target set. Containment is itself governed, separately approved when it
mutates provider state, and audited. Transport acknowledgement is never reported
as verified provider state.

## 20. Positive native-equivalence standard

`PASS_EQUIVALENT` requires all Sections 11–19 controls to have current,
reproducible, independently reviewed evidence; zero unresolved P0/P1 findings;
no weakening of the native baseline; complete negative-path tests; exact revision
binding; and a signed assessment record. Compensating strengths cannot offset a
failed control. Equality means equivalent safety guarantees, not identical
implementation.

## 21. Assessment outcomes

| Outcome | Meaning | Runtime consequence |
| --- | --- | --- |
| `PASS_EQUIVALENT` | Every positive criterion passes for the exact assessment key | May satisfy this prerequisite only; grants no authorization |
| `PASS_READ_ONLY_ONLY` | R0–R2 controls pass; mutation equivalence not proven | R3–R5 prohibited |
| `FAIL_NOT_EQUIVALENT` | One or more required controls fail | Assessed path prohibited |
| `INSUFFICIENT_EVIDENCE` | Evidence missing, stale, ambiguous, or native baseline absent | Deny; never infer a pass |
| `EXPIRED_REASSESSMENT_REQUIRED` | A prior assessment exceeded freshness or a revision changed | Deny until reassessed |

## 22. Current outcome

No candidate has file-backed configuration, control-test, failure-injection, or
audit-trace evidence in this repository. Therefore every candidate is currently
`INSUFFICIENT_EVIDENCE`; no `PASS_EQUIVALENT` or `PASS_READ_ONLY_ONLY` claim is
made. All fabric-mediated provider access remains unauthorized.

## 23. Candidate selection rule

A future selection compares only tuples with admissible evidence. Safety is a
hard gate, not a weighted score. Among passing tuples, an operator may consider
operability, cost, latency, connector coverage, data residency, portability, and
maintenance, but the choice requires a separate ADR amendment or explicit
selection decision and separate implementation authorization.

## 24. Cybersecurity boundary

A fabric is never the primary cybersecurity execution boundary. Restricted
Zapier MCP is prohibited for cybersecurity execution. A future fabric-mediated
cybersecurity read or proposal path still requires provider-contract permission,
`PASS_READ_ONLY_ONLY` or stronger evidence, and separate runtime authorization.

## 25. Reassessment triggers

Reassess on fabric, connector, Gateway, Registry, provider-contract, tenant,
credential-custody, tool-set, region, retry, audit, or policy revision; material
incident; provider deprecation; control-evidence expiry; or provenance loss.
Until reassessed, the prior outcome is `EXPIRED_REASSESSMENT_REQUIRED`.

## 26. Explicit non-authorizations

This specification authorizes no account creation, trial, purchase, login,
credential, OAuth grant, token, API call, MCP connection, webhook, fabric
connection, provider connection, adapter, source code, dependency, workflow,
deployment, production access, marketing action, or cybersecurity action.

## 27. Implementation prerequisite

`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002` must pass before
adapter scaffolding may even be considered. A passing review still does not
authorize scaffolding; `MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` requires a
separate explicit Operator authorization.

## 28. Amendment and references

Changes require a reviewed revision that identifies affected assessment keys,
criteria, outcomes, and migration impact. Historical assessments remain
append-only. Canonical references are the five documents in Section 3 plus
`docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md`.
