# MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001

## Status

**Complete — local documentation commit only; not pushed.**

## Objective

Define the first canonical, read-oriented Marketing Provider Pack for MellyCore
AIOS, downstream of the accepted enterprise-provider ADR, Provider Registry,
Integration Gateway, context-sensitivity, and control-plane contracts.

## Result

Created:

- `docs/specs/MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md`

The accepted 40-section specification defines:

- P0 HubSpot, Google Analytics 4, Google Ads, Meta Marketing API, LinkedIn
  Marketing API, and Twilio Segment;
- P1 Salesforce Marketing Cloud, Braze, and Klaviyo;
- P2 Adobe Experience Platform;
- 22 separate normalized marketing entity kinds and a common evidence,
  sensitivity, identity, consent, purpose, metric, attribution, and loss envelope;
- stable read, report, and proposal-only common capability families;
- an initial R0-R2 ceiling, with all R3-R5 mutation, tracking, audience,
  activation, send, identity, CRM, consent, and export surfaces deferred;
- cross-provider metric, attribution, identity-resolution, event, provenance, and
  correlation safeguards;
- provider-specific evidence, authorization/licensing uncertainty, and future
  contract prerequisites; and
- a bounded implementation sequence that grants no implementation authority.

## Contract integrity

The pack preserves the Provider Registry's eight independent facts. Pack
membership, provider tier, registration, capability existence, authentication,
MCP discovery, fabric availability, and data presence are not authorization.
The Integration Gateway remains the policy boundary. Missing consent is not
consent; provider-native identity or attribution is not universal truth; and
unknown provider details remain explicitly `UNVERIFIED`.

No inferred license, permission, tenant scope, API version, event guarantee,
identity match, metric equivalence, or consent state is presented as confirmed.

## Repository scope

Exactly six paths are changed by this task:

1. `docs/specs/MELLYCORE_MARKETING_PROVIDER_PACK_SPEC_001.md` (new)
2. `docs/tasks/MELLYCORE-MARKETING-PROVIDER-PACK-SPEC-001.md` (new)
3. `shared_context/PROJECT_STATE.md`
4. `shared_context/ROADMAP.md`
5. `shared_context/RUN_QUEUE.md`
6. `shared_context/AGENT_HANDOFF.md`

Branch:
`docs/mellycore-marketing-provider-pack-spec-001`

Starting commit:
`918aa4c437364986e80d9c52608b5a1e0141f946`

Commit subject:
`docs: define marketing provider pack`

Commit SHA: reported in the final execution report.

## Research evidence

Only public official provider documentation was reviewed. Section 40 of the
specification records the evidence register and official URLs for all ten
providers. Meta public documentation was not reliably retrievable in the
research environment, so its current authentication, permission, review,
versioning, quota, and webhook details are `UNVERIFIED` rather than inferred.

No provider authentication, protected API call, credential access, MCP/fabric
connection, webhook registration, tracking action, audience operation, campaign
operation, or provider-side search occurred.

## Validation

The validation gate requires and records in the final execution report:

- exact sequential 40-section structure;
- all ten provider profiles, conformance rows, and evidence rows;
- all 22 normalized entities and mandatory envelope fields;
- privacy, consent, purpose, identity, metric, attribution, and correlation
  fail-closed semantics;
- R0-R2-only semantics and explicit R3-R5 deferral;
- Provider Registry eight-fact independence;
- canonical negative-scope and authorization language;
- exact six-path working and staged inventories;
- `py -3.9 scripts/validate_project_state.py`;
- `git diff --check` and `git diff --cached --check`; and
- final branch, parent, commit subject, canonical-main, remote-branch, and clean-
  worktree verification.

Pytest is `NOT_RUN`: this is a documentation-only task, no dependency was
installed, and no runtime code changed.

## Safety and non-authorization

This task performs documentation and bounded repository operations only. It
authorizes and performs no provider connection, credential configuration,
adapter/runtime implementation, deployment, protected API call, MCP or
integration-fabric connection, webhook registration, tracking, event submission,
identity resolution, audience operation, campaign operation, CRM mutation,
messaging, R3-R5 action, dependency change, or MellyTrade operation.

No push, pull request, merge, release, or deployment is part of this task.

## Next task

`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001`

It remains documentation-only and requires its own exact authorization. Provider
adapter scaffolding remains blocked until that review passes, any required
remediation completes, and a separate explicit operator authorization is issued.
The global OpenAI Batch pointer is unchanged.
