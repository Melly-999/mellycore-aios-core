# MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001

## 1. Purpose

Create the first inert, provider-neutral code scaffold for MellyCore provider
adapters. The scaffold translates accepted Provider Registry and Integration
Gateway vocabulary into reusable Python contracts without implementing a real
provider, transport, credential boundary, authorization service, or execution
path.

## 2. Starting repository state

- Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
  (resolved root `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`).
- Starting branch:
  `docs/mellycore-enterprise-provider-docs-integration-review-004`.
- Starting HEAD: `b32c81fa96b9f3f7542a93101b73a4fe038b033f`.
- Starting parent: `b90ce82ab497469ea3c8b8c0f3c8be8ce8717dbd`.
- Starting subject: `docs: verify restricted operator tool path conformance`.
- Canonical remote: `clean-origin` at
  `https://github.com/Melly-999/mellycore-aios-core.git`.
- Worktree and index: clean.
- Scaffold branch: absent locally and on `clean-origin`.
- One explicitly authorized read-only `git fetch clean-origin` completed in
  Phase 1. Fresh `clean-origin/main`:
  `947f33d27d5546775186e96bdc61e30db78c0b3d`, unchanged.
- No other network operation occurred after that fetch.
- Branch created directly from the starting HEAD:
  `feat/mellycore-provider-adapter-scaffold-001`.

## 3. Documentation-gate dependency

Consumed the independent Review 004 outcome:
`PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0, P1 0, P2 0, P3 3). All five Review
003 findings were independently closed, all 24 replay scenarios were
deterministic, and the review made this scaffold eligible for this separately
authorized task.

Canonical evidence:

- `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_004.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004.md`

## 4. Review 004 constraints imported

Exactly four constraints from Review 004 Section 36 were carried into code and
tests:

1. `P3-401`: use the raw Registry Section 7.5 values rather than depending on
   the malformed Markdown table rendering. The three tokens are explicit enum
   values; production code reads no Markdown or contract file.
2. `P3-402`: resolve fields by canonical names, not mutable Section 14.1
   ordinals. The scaffold has named `scope_applicability` fields and no retired
   runtime field.
3. `P3-403`: do not assume a restricted-tool OAuth grant is available for
   Cloudflare D4. Authentication mode is deliberately absent from the scaffold
   envelope and no such route is selectable, configured, defaulted, or enabled.
4. Gateway Rule 32.1: no runtime-enable gate currently passes. The only
   execution state is `disabled`, and every adapter execution attempt returns
   `EXECUTION_DISABLED` even when fixture fact inputs are optimistic.

## 5. Runtime discovery

The accepted runtime source architecture is standard-library Python 3.9:

- canonical source root: `scripts/`;
- canonical test root: `tests/`;
- package convention: `scripts/<package>/` with `__init__.py`;
- test convention: standard-library `unittest`;
- public structural interface convention: `typing.Protocol`;
- immutable-model convention: `@dataclass(frozen=True)` and tuple-backed
  collections;
- error convention: typed exceptions with stable machine-readable codes;
- validation convention: strict, fail-fast, no silent rewriting;
- import convention: absolute `scripts.*` imports in tests and relative imports
  inside a package.

No provider-neutral adapter package existed. The provider boundary under
`scripts/mellycore_batch/` is specific to the separate Batch track and was not
modified or reused as a generic registry.

## 6. Existing architecture reused

The scaffold reuses repository-native patterns from `scripts/context_gate`,
`scripts/loop_ops`, and `scripts/mellycore_batch`: future annotations, frozen
dataclasses, explicit tuples, protocols, stable error codes, sanitized failure
messages, standard-library-only validation, socket-denial tests, and no package
installation.

No new language, framework, package manager, dependency, persistence layer,
runtime registry, logging framework, or architectural gateway was introduced.

## 7. Source paths

- `scripts/provider_adapters/__init__.py` — public API exports.
- `scripts/provider_adapters/contracts.py` — closed vocabulary, immutable
  descriptors, envelope, facts, normalized result, and error contracts.
- `scripts/provider_adapters/validation.py` — static manifest and resolved
  envelope validation plus safe reference redaction.
- `scripts/provider_adapters/adapters.py` — provider-neutral protocol and
  deterministic disabled adapter.
- `tests/provider_adapter_fixtures.py` — fixture-only in-memory descriptor,
  capability, envelope, facts, and normalizer.
- `tests/test_provider_adapters.py` — focused contract and negative-path tests.

## 8. Public adapter API

`scripts.provider_adapters` exports:

- `ProviderId` and `CapabilityId`;
- canonical enum types for credential classes, acting identities,
  authentication targets, scope applicability/family, risk, approval,
  implementation, network, credential, execution, outcome, and error state;
- `ProviderDescriptor`, `CapabilityDescriptor`,
  `ContractScopeDimension`, `ScopeApplicabilityEntry`, `ScopeReference`,
  `AuthorizationFacts`, `ResolvedExecutionEnvelope`,
  `NormalizedAdapterError`, and `NormalizedOperationResult`;
- `AdapterValidationError` and stable `AdapterErrorCode` values;
- `ProviderAdapter` and `DisabledProviderAdapter`;
- `parse_canonical_value`, `validate_manifest`, and `validate_envelope`.

The protocol surface is limited to returning static descriptor/manifest data,
reporting execution state, validating an already resolved envelope, and an
`execute` method that is disabled by construction. It contains no arbitrary
request, URL, method, transport, discovery, credential, or authorization API.

## 9. Canonical vocabularies

- Provider ID grammar: `^[a-z][a-z0-9_]*$`; exact, case-sensitive, with no
  dotted IDs, aliases, or fuzzy matching.
- Credential-profile classes: exactly nine — `read_only_delegated`,
  `read_only_service`, `controlled_write`, `event_verification`,
  `integration_fabric_read`, `integration_fabric_controlled_write`,
  `emergency_containment`, `reporting_only`, and
  `restricted_operator_investigation`.
- Acting identities: exactly three — `delegated_user`, `service_account`, and
  `mellycore_operator`.
- Authentication targets: exactly three — `provider_account`,
  `restricted_tool`, and `integration_fabric`.
- Scope applicability: exactly three — `required`, `optional`, and
  `not_applicable`.
- Risk tiers: exactly six — R0 through R5.

All serialize to their exact string value. Unknown values fail without case
folding, aliasing, fuzzy matching, or default selection.

## 10. Provider descriptor

`ProviderDescriptor` is frozen and requires every field explicitly: canonical
provider ID, display name, family, contract reference/revision, adapter kind,
supported environments, manifest revision, adapter revision, implementation
state, network behavior, credential support, and execution state.

Static validation accepts only scaffold-only implementation, disabled network,
unsupported credentials, and disabled execution. A descriptor is metadata; it
is not a provider registration and has no default provider selection.

## 11. Capability descriptor

`CapabilityDescriptor` is frozen and provider-bound. It includes stable
capability ID/version, provider contract and native provenance references,
risk, exact credential class, exact acting identity, exact authentication
target, provider-contract scope dimensions, complete scope applicability,
sensitivity reference, external-content exposure, classification, verification
requirement, approval policy, and audit requirement.

Static validation enforces unique provider-prefixed capability IDs, one exact
class/identity/target binding, required contract revision, R4/R5 approval
metadata, mutation verification, mandatory audit, and provider-contract-owned
scope permissions. Provider-specific labels are never runtime identifiers.

## 12. Scope-applicability model

Each provider-contract dimension declares its family and whether `optional` or
`not_applicable` is permitted. Each capability must then declare exactly one
applicability value for every dimension. Missing, duplicate, unknown, or
provider-contract-incompatible declarations deny.

Envelope validation requires one opaque value for every `required` dimension,
allows an absent `optional` value only where the contract explicitly permits
it, and rejects every value supplied for `not_applicable`. Omission never means
`not_applicable`.

The restricted-tool fixture declares provider-native account/zone/resource
explicitly `not_applicable` and all seven exact restricted-tool dimensions
`required`. Supplying provider-native scope or omitting any exact tool scope
denies.

## 13. Execution-envelope model

`ResolvedExecutionEnvelope` is frozen and carries only typed values and opaque
references: request/correlation/fingerprint, tenant, provider,
capability/version, environment, acting identity, credential class/profile
reference and exact match count, authentication target, normalized scope
applicability/references, risk, contract/adapter revision, authorization-record
references, runtime-enable/approval/audit references, external-content marker,
and all eight facts.

It stores no raw credential, authorization evidence body, approval evidence
body, provider payload, endpoint, method, header, or account ID. Sensitive-
shaped or structurally invalid references deny with a generic message that does
not echo the rejected value.

## 14. Eight-fact representation

`AuthorizationFacts` contains exactly eight independent fields:

1. provider registered;
2. adapter implemented;
3. credential configured;
4. credential verified;
5. tenant authorized;
6. capability authorized;
7. runtime enabled;
8. operation approved.

No aggregate `ready`, `connected`, or `enabled` boolean replaces them. Facts
1-7 cannot be `not_required`. Operation approval may be `not_required` only for
R0-R2 validation input; R3-R5 require a separately satisfied approval and
opaque reference. Changing one field infers none of the others.

## 15. Disabled adapter behavior

`DisabledProviderAdapter` validates only static metadata and resolved envelope
shape. Every call to `execute` immediately returns a normalized
`EXECUTION_DISABLED` result without first resolving credentials, reading the
environment, opening a socket, contacting a provider, interpreting facts, or
performing I/O. No success outcome exists in `OperationOutcome`.

The result carries no provider request ID and cannot claim authentication or
mutation. Unsafe request references are replaced by a deterministic hash-based
redacted reference.

## 16. Fixture-only behavior

`tests.provider_adapter_fixtures.FixtureProviderAdapter` is test-only and
in-memory. It accepts only an immutable tuple of three allowlisted scalar fields,
rejects sensitive-shaped fixture text, loads no file, reads no environment,
runs no command, and performs no I/O. Normalized fixture output is always
`FIXTURE_ONLY`, with no provider request ID, authentication, mutation,
deployment, or enablement claim. Its inherited `execute` remains disabled.

## 17. Manifest validation

Validation covers canonical ID grammar, provider binding, unique capabilities,
closed vocabularies, exact class/identity/target compatibility, complete scope
applicability, provider-contract permission for optional/N/A states, contract
revision, risk, approval, verification, audit, scaffold-only implementation,
disabled network/execution, and unsupported credential behavior.

Validation reads no canonical document or rendered table and makes no provider
call. It constructs no registry and selects no default provider, profile,
identity, target, scope, or risk tier.

## 18. Error model

Stable error codes cover invalid provider/capability identity, unknown or
duplicate capability, incompatible credential class/acting identity/target,
missing or unexpected scope, zero or ambiguous credential matches, missing
contract revision, unsupported or disabled execution, external-content
failure, fixture-only operation, sensitive reference rejection, and invalid
approval status.

`ErrorPhase` distinguishes manifest validation, envelope validation, and
execution. Every normalized error states that no provider request occurred.
Errors contain field names and coarse fixed messages, never complete envelopes
or rejected values.

## 19. Security posture

- Inert and fail-closed by construction.
- No real provider ID is registered in production code.
- No real provider adapter or provider-specific implementation.
- No URL, endpoint, HTTP client, SDK, socket, environment, credential resolver,
  secret manager, token exchange, OAuth flow, MCP client/server, integration
  fabric, webhook, database, dynamic import, arbitrary command, or tool
  discovery.
- No execution-success state and no provider-success claim.
- External content remains explicitly untrusted and must match the manifest.
- Zero and multiple credential-profile matches deny; no best-available or
  identity/class widening.
- No default provider, credential class, acting identity, authentication target,
  N/A scope, or risk tier.
- No sensitive value is serialized in errors or fixture results.

## 20. Test coverage

The focused module contains 62 tests covering the original brief's canonical
vocabulary, identity, capability, scope, credential/identity/target binding,
eight-fact, disabled execution, fixture, redaction, source-absence, and Review
004 requirements.

Network and environment denial are exercised with standard-library mocks.
Static source assertions verify no document parsing, field ordinal, retired
scope field, selectable restricted-tool OAuth mode, network/environment/SDK
import, or endpoint URL exists in production scaffold code.

## 21. Files changed

Exactly eleven allowlisted paths:

1. `scripts/provider_adapters/__init__.py`
2. `scripts/provider_adapters/contracts.py`
3. `scripts/provider_adapters/validation.py`
4. `scripts/provider_adapters/adapters.py`
5. `tests/provider_adapter_fixtures.py`
6. `tests/test_provider_adapters.py`
7. `docs/tasks/MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001.md`
8. `shared_context/PROJECT_STATE.md`
9. `shared_context/ROADMAP.md`
10. `shared_context/RUN_QUEUE.md`
11. `shared_context/AGENT_HANDOFF.md`

## 22. Validation commands

| Command | Exit | Exact result |
| --- | ---: | --- |
| `py -3.9 -m black --version` | 1 | `No module named black`; unavailable, no installation |
| `py -3.9 -m flake8 --version` | 1 | `No module named flake8`; unavailable, no installation |
| `py -3.9 -m mypy --version` | 1 | `No module named mypy`; unavailable, no installation |
| `py -3.9 -B -m unittest tests.test_provider_adapters` (first run) | 1 | 59 tests; one static assertion failed because a source comment legitimately referenced `docs/specs`; assertion narrowed to test file-reading behavior |
| `py -3.9 -B -m unittest tests.test_provider_adapters` | 0 | 59 tests, `OK` |
| `py -3.9 -B -m unittest discover` | 0 | 633 tests, `OK` |
| `py -3.9 scripts/validate_project_state.py` (first run) | 1 | Safety validator found one synthetic secret-shaped literal in the redaction test; no real secret; literal removed and constructed only at runtime |
| `py -3.9 -B -m unittest tests.test_provider_adapters` (after safety correction) | 0 | 59 tests, `OK` |
| `py -3.9 scripts/validate_project_state.py` (after correction) | 0 | `PASS MellyCore project scaffold validation passed` |
| `py -3.9 -B -m unittest tests.test_provider_adapters` (final expanded suite) | 0 | 62 tests, `OK` |
| `py -3.9 -B -m unittest discover` (final expanded suite) | 0 | 636 tests, `OK` |
| `py -3.9 scripts/validate_project_state.py` (final staged tree) | 0 | `PASS MellyCore project scaffold validation passed` |
| `py -3.9 -B -c "import scripts.provider_adapters as p; print(p.DisabledProviderAdapter.__name__)"` | 0 | Import/build smoke passed; `DisabledProviderAdapter` |
| `git diff --check` | 0 | No whitespace errors |
| `git diff --cached --check` | 0 | No staged whitespace errors |

Final Git whitespace, allowlist, immutable-document, static-search, full-suite,
and post-commit checks are recorded in the final execution report. No failed
validation is represented as passing.

## 23. Validators not run

- `black`: `NOT_RUN`; module unavailable, and dependency installation was
  prohibited.
- `flake8`: `NOT_RUN`; module unavailable, and dependency installation was
  prohibited.
- `mypy`: `NOT_RUN`; module unavailable, and dependency installation was
  prohibited.
- Separate package build: `NOT_APPLICABLE`; this is a standard-library package
  with no build system or package manifest. Python 3.9 imported and executed all
  scaffold modules through both focused and full tests.

## 24. Known limitations

- This is not a registry, Gateway implementation, policy engine, credential
  resolver, approval broker, audit backend, or transport.
- It validates only static descriptors and already resolved fixture envelopes.
- It intentionally has no authentication-mode field, so no restricted-tool
  OAuth authority can be configured or selected.
- It does not claim the complete Gateway Section 17 runtime gate is implemented.
- It does not encode the seventeen provider IDs as an execution registry.
- It implements no concrete provider-specific constraints beyond generic
  binding rules and a non-executable restricted-tool fixture shape.

## 25. Exact next task

`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-REVIEW-001`

Independent review must verify this scaffold against the accepted Registry,
Gateway, provider contracts/packs, Review 004 Section 36, source absence scans,
and negative-path tests. Every concrete provider adapter remains blocked until
that review passes and a separate explicit Operator authorization is issued.

## 26. Explicit non-authorizations

This task authorizes and performs no real provider adapter, provider
registration, provider authentication, provider API access, credential access,
secret access, environment credential read, OAuth flow, MCP execution,
integration-fabric connection, webhook, database, runtime enablement, operation
approval implementation, frontend change, workflow change, dependency, lockfile
change, deployment, push, pull request, merge, remote branch, or MellyTrade
interaction.

No provider is registered, connected, authenticated, credentialed, enabled,
live, deployed, or implemented. No restricted tool is connected. No provider
access occurred.

## 27. Commit and no-push state

One local commit is authorized with subject:
`feat: scaffold provider adapter contracts`.

Commit SHA: reported in the final execution report.

No amend, reset, restore, stash, clean, rebase, squash, cherry-pick, force
operation, push, pull request, merge, deployment, remote branch, upstream, or
provider action is authorized or performed.
