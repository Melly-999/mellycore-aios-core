# MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001

## 1. Purpose

Resolve exactly Review 003 findings `P1-301`, `P1-302`, `P2-301`,
`P3-301`, and `P3-302` by making the restricted operator-investigation path
deterministically representable across the Provider Registry, Integration
Gateway, Cloudflare contract, Cybersecurity Provider Pack, and shared context.
This is documentation conformance only and authorizes no implementation or
external access.

## 2. Starting repository state

- Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`.
- Resolved root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`.
- Starting branch:
  `docs/mellycore-enterprise-provider-docs-integration-review-003`.
- Starting HEAD: `699f1d39b011b6afe5ba82d4c2bd8f5639c5de59`.
- Starting subject: `docs: verify enterprise provider credential class conformance`.
- Starting parent: `8e1f7289345eb556d6b1972cac61c0aa9a950c89`.
- Canonical remote: `clean-origin` at
  `https://github.com/Melly-999/mellycore-aios-core.git`.
- Fetched `clean-origin/main`:
  `947f33d27d5546775186e96bdc61e30db78c0b3d` — unchanged.
- Worktree and index were clean; no local or canonical-remote remediation
  branch existed.
- New local branch:
  `docs/mellycore-enterprise-provider-restricted-tool-path-conformance-remediation-001`,
  created directly from `699f1d39…`, not from `clean-origin/main`.

## 3. Review 003 dependency

The immutable Review 003 record is
`docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md`.
It records `FAIL_REMEDIATION_REQUIRED`, P0 = 0, P1 = 2, P2 = 1, P3 = 2,
and `P1-201: PARTIALLY_CLOSED`. Both P1 findings fail in the deny direction.
This remediation does not amend that evidence and is not a documentation-gate
PASS.

## 4. Finding register

| Finding | Review 003 evidence | Canonical owner | Correction | Closure status |
| --- | --- | --- | --- | --- |
| `P1-301` | Gateway §9.2, Rule 16.7, §17 step 13, and §23 admitted only delegated/service identities | Registry §7.5 vocabulary; Gateway runtime enforcement | Add constrained `mellycore_operator` representation through chain, evaluation, envelope, credential matching, and audit | `REMEDIATED_CLAIM_UNVERIFIED_PENDING_REVIEW_004` |
| `P1-302` | Registry provider-wide account/zone requirement contradicted D4 empty binding | Registry §11 applicability; Cloudflare §§9/11/13/25 constraints | Capability-level `required`/`optional`/`not_applicable`; D4 provider-native N/A and exact tool scope required | `REMEDIATED_CLAIM_UNVERIFIED_PENDING_REVIEW_004` |
| `P2-301` | `mcp_oauth_grant` target was ambiguous | Registry §12.1 target vocabulary; Gateway enforcement | Separate auth mode from target; D4 OAuth targets only exact registered restricted tool | `REMEDIATED_CLAIM_UNVERIFIED_PENDING_REVIEW_004` |
| `P3-301` | `CF_READ` selector had no named field | Registry capability record | Name `required_acting_identity_type`; bind before runtime | `REMEDIATED_CLAIM_UNVERIFIED_PENDING_REVIEW_004` |
| `P3-302` | No canonical identity-token vocabulary | Registry §7.5 | One closed three-token vocabulary consumed by Gateway and provider contracts | `REMEDIATED_CLAIM_UNVERIFIED_PENDING_REVIEW_004` |

## 5. Ownership decisions

- Provider Registry owns canonical acting-identity types, authentication
  targets, capability record fields, generic scope applicability, and
  restricted-tool registration shape.
- Integration Gateway owns runtime resolution and fail-closed evaluation.
- Cloudflare owns which provider-native dimensions are applicable to each
  Cloudflare capability and the `CF_*` projection.
- Cybersecurity Pack references these owners and does not duplicate D4.
- No broad ADR was required.

## 6. Acting-identity vocabulary

Registry §7.5 owns exactly `delegated_user`, `service_account`, and
`mellycore_operator`. Each defines human/non-human status, delegation,
provider-account and API eligibility, restricted-tool eligibility, compatible
credential classes, substitution prohibition, and audit representation.

## 7. Runtime acting-identity field

`required_acting_identity_type` is the single canonical selector. It is stored
on every concrete capability registration, carried in the Gateway request
envelope, bound before credential resolution, frozen for one evaluation, and
matched against class, target, mode, and exact actor. Missing, unknown,
conflicting, or incompatible values deny.

## 8. Scope-applicability model

Registry §11 owns exactly `required`, `optional`, and `not_applicable`.
MellyCore tenant, capability, acting identity, environment, and runtime state
remain required. Provider-native and restricted-tool dimensions are declared
per concrete capability. Missing declarations deny; omitted scope never means
N/A; supplying a value for an N/A dimension denies.

## 9. Provider versus capability scope

Provider metadata defines possible provider-native dimensions and strict API
defaults. Each capability declares applicability within that allowed model.
The Gateway validates the concrete declaration. A capability can narrow only
itself; it cannot weaken another capability. Cloudflare D1–D3 retain applicable
account, zone, and resource requirements.

## 10. Authentication-target model

Registry §12.1 owns exactly `provider_account`, `restricted_tool`, and
`integration_fabric`. Authentication mode and target are separate fields.
Every profile and capability pins one compatible target before runtime.

## 11. `mcp_oauth_grant` result

Retained only for `restricted_operator_investigation` when the target is the
exact registered `restricted_tool`. The OAuth authority is the tool/server,
not Cloudflare or another provider; it grants no provider account or API reach,
is tenant/tool/capability bound, and cannot become a provider credential.

## 12. Restricted-tool registration model

The Registry record requires exact tool/server ID, tool-contract revision,
tenant, environment, allowed capabilities, operator eligibility,
authentication target, credential class, data sensitivity, allowed resource
classes, external-content posture, audit source/mode, retention, and session
metadata. Discovery is untrusted inventory. Exact record, revision, identity,
scope, runtime enablement, and authorization must match; zero or multiple
matches deny.

## 13. Gateway alignment

Gateway §9.2, Rule 16.7, §17 step 13, §23, and §34 now consume the Registry
vocabulary. `mellycore_operator` is accepted only for an explicitly compatible
operator-bound restricted-tool capability and class. No universal or
operator-to-service fallback exists.

## 14. Registry alignment

Registry §7.5, §11, §12.1, §13, §14, §24, and §26 define the vocabulary,
scope, authentication target, record fields, exact tool registration, and
Cloudflare projection. The canonical credential-class count remains nine.

## 15. Cloudflare D4 alignment

D4 remains documentation/investigation-only, operator-bound, R0 in v1.0 and
R2 maximum, non-provider-account, non-provider-API, non-mutating,
non-containment, and non-evidentiary. It binds
`required_acting_identity_type: mellycore_operator`, class
`restricted_operator_investigation`, target `restricted_tool`, provider-native
account/zone/resource `not_applicable`, and exact restricted-tool scope.

## 16. Cybersecurity Pack alignment

The Pack references Registry-owned identity and scope vocabularies, states its
class table is non-exhaustive, keeps the R0–R2 ceiling and Cloudflare authority,
and authorizes neither restricted MCP execution nor provider API access.

## 17. P1 closures

`P1-301` and `P1-302` are remediated claims only. They remain unverified until
independent Review 004. The documentation gate remains failed.

## 18. P2 closure

`P2-301` is remediated by the closed authentication-target vocabulary and the
tool-only semantics of `mcp_oauth_grant`, pending Review 004 verification.

## 19. P3 closures

`P3-301` is remediated by `required_acting_identity_type`. `P3-302` is
remediated by Registry §7.5's single reusable vocabulary. Both await Review
004 verification.

## 20. Safety-invariant preservation

Registration, implementation, credential configuration, credential
verification, tenant authorization, capability authorization, runtime
enablement, and operation approval remain eight independent facts. Provider
registration is not authorization. Restricted-tool authentication is not
provider authentication. Tool authorization is not Cloudflare authorization.
No identity fallback, scope widening, provider API authority, mutation,
containment, or proposal evidence was introduced. Read-after-write,
reconciliation, audit, external-content distrust, tenant isolation, and all
R0–R5 meanings remain intact.

## 21. Files changed

1. `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
2. `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
3. `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
4. `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
5. `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001.md`
6. `shared_context/PROJECT_STATE.md`
7. `shared_context/ROADMAP.md`
8. `shared_context/RUN_QUEUE.md`
9. `shared_context/AGENT_HANDOFF.md`

Review 001/002/003 records and reports and every prior remediation report remain
immutable.

## 22. Validation evidence

| Check | Result |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` | **PASS** — `PASS MellyCore project scaffold validation passed`, exit 0 |
| `git diff --check` | **PASS** — no output, exit 0 |
| `git status --short`; `git diff --name-only`; `git diff --stat` | **PASS** — exact nine-file documentation allowlist; no source/runtime path |
| Finding register | **PASS** — exactly five Review 003 finding rows |
| Scenario replay | **PASS** — exactly 16 deterministic rows; no architectural interpretation required |
| Canonical acting-identity types | **PASS** — exactly 3 |
| Canonical credential-profile classes | **PASS** — exactly 9 |
| Authentication targets | **PASS** — exactly 3 |
| Cloudflare capability rows | **PASS** — 58 (D1 16, D2 16, D3 23, D4 3) |
| Cloudflare prohibition rows | **PASS** — 13 |
| Cloudflare row integrity | **PASS** — all 71 capability/prohibition rows retain starting SHA-256 `759d4250007946ee4456537ae74cbce54051186592617bcd75b16ebc9a592a41` |
| Zone-wide Schema Validation block | **PASS** — D3-10 remains R5 |
| Cloudflare MCP posture | **PASS** — documentation-only |
| Cybersecurity Pack ceiling | **PASS** — R0–R2 |
| Review/prior-remediation immutability | **PASS** — no diff; starting Git blob IDs retained |
| Global OpenAI Batch pointer | **PASS** — 12 occurrences in the four edited shared-context files, content SHA-256 unchanged at `42772651115782069b3ce149f6c78aa32d1b797729eadc66e97b5fb686077e62` |
| Introduced secret patterns | **PASS** — 0 |
| `pytest` | `NOT_RUN` — documentation-only task; no dependency installed |

No unavailable or unrun validator is represented as passing.

## 23. Remaining open questions

No contract interpretation is left for the sixteen scenarios below. Provider
credentials, account identifiers, tool connections, implementation, and live
evidence remain absent and unauthorized. Independent Review 004 must determine
whether the remediation claims close the findings.

## 24. Exact next task

`MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004`

Not started. It is an independent documentation review, not provider access.

## 25. Adapter Scaffold block

`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` remains blocked, ineligible, not
started, and unauthorized. This remediation cannot make it eligible.

## 26. No-push status

One local documentation commit is authorized. No push, PR, merge, tag, remote
branch, deployment, provider authentication, provider API call, MCP/fabric
connection, webhook registration, credential, secret, `.env`, runtime,
adapter, scaffold, dependency, workflow, source-code, or MellyTrade action is
authorized or performed.

Commit SHA: reported in the final execution report.

## 27. Sixteen-scenario deterministic replay

All scenarios assume exact MellyCore tenant and environment unless the row says
otherwise. Facts are the Registry's independent facts 1–8.

| # | Acting identity / canonical type | Credential class; auth mode; target | Tenant; provider-native applicability; restricted-tool scope | Capability / tier | Required facts; expected contract decision | Exact fail-closed reason | Source sections |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Exact delegated subject / `delegated_user` | `read_only_delegated`; `delegated_oauth`; `provider_account` | Exact tenant; account/zone/resource `required` as row applies; tool N/A | Cloudflare bounded read / R1 | Facts 1–7, fact 8 `not_required`; resolves, then current state denies | `ADAPTER_UNAVAILABLE` / `RUNTIME_NOT_ENABLED` because facts 2 and 7 are absent | Registry §§7.5, 11, 13.2; Gateway §§14, 17; Cloudflare §§11, 13.1 |
| 2 | Exact service identity / `service_account` | `read_only_service`; one pinned service mode; `provider_account` | Exact tenant; applicable provider-native scope `required`; tool N/A | Cloudflare bounded read / R1 | Facts 1–7; resolves, then current state denies | `ADAPTER_UNAVAILABLE` / `RUNTIME_NOT_ENABLED` | Same, plus Gateway §16 |
| 3 | Missing / missing | `CF_READ` cannot project; mode/target unresolved | Tenant exact; provider scope present; tool N/A | Cloudflare read / R1 | No credential resolution; deny | Missing `required_acting_identity_type` → `IDENTITY_UNRESOLVED` | Registry §14.2; Gateway §§17 step 13, 23.3; Cloudflare §11.1.1 |
| 4 | Delegated and service both / conflicting | Two candidate read classes/modes; `provider_account` | Tenant exact; provider scope present; tool N/A | Cloudflare read / R1 | Deny before credential material | Multiple/conflicting identity selectors; no dynamic switch | Registry §§7.5, 13.2; Gateway Rule 16.7 |
| 5 | Exact operator / `mellycore_operator` | `restricted_operator_investigation`; `no_auth_public_documentation`; `restricted_tool` | Exact tenant; account/zone/resource N/A; exact tool ID/revision/capability/operator/environment/resource class | D4 documentation lookup / R0 | Facts 1–7, fact 8 `not_required`; contract-resolvable, current state denies | `RUNTIME_NOT_ENABLED` / `ADAPTER_UNAVAILABLE`; no tool is connected | Registry §§11, 12.1, 24; Gateway §§21, 34.6; Cloudflare §§13.4, 25 |
| 6 | Exact operator / `mellycore_operator` | Same class/mode/target | Tenant exact; provider N/A; no registered tool | D4 / R0 | Deny | Missing exact restricted-tool registration | Registry §24; Gateway §21.2 rules 6, 11 |
| 7 | Exact operator / `mellycore_operator` | Same class/mode/target | Tenant exact; empty provider scope but applicability omitted; tool otherwise exact | D4 / R0 | Deny | Omission never means `not_applicable`; incomplete `scope_applicability` | Registry §11.2; Gateway §13.2 rule 8 |
| 8 | Exact operator / `mellycore_operator` | Same class/mode/target | Tenant exact; D4 account or zone supplied despite N/A; exact tool | D4 / R0 | Deny and audit | Value supplied for `not_applicable` provider-native dimension | Registry §11.2; Cloudflare Rules 9.4, 11.2 |
| 9 | Exact operator / `mellycore_operator` | Restricted class; any allowed tool mode; `restricted_tool` | Tenant exact; provider N/A; exact tool | Cloudflare REST API attempt / R1+ | Deny | Class has provider API authority `None`; target/class/capability mismatch | Registry §13.2; Gateway §14.2; Cloudflare §11.1.1 |
| 10 | Exact operator / `mellycore_operator` | Restricted class; tool mode; `restricted_tool` | Tenant exact; provider N/A; exact tool | D4 mutation attempt / R3+ | Deny and audit | `mutation_prohibited: true`; mutation authority `None` | Gateway §21.2; Cloudflare §§11.1.1, 25 |
| 11 | Exact operator / `mellycore_operator` | Normal `read_only_service`; service mode; `provider_account` | Tenant exact; D4 provider N/A; tool exact | D4 / R0 | Deny | Identity/class/target mismatch; no cross-class substitution | Registry §§7.5, 13.2; Gateway §14.2 |
| 12 | Exact operator / `mellycore_operator` | Restricted class; `mcp_oauth_grant`; `restricted_tool` | Tenant exact; provider N/A; exact registered tool scope | D4 MCP documentation session / R0 | Contract-resolvable, current state denies | `RUNTIME_NOT_ENABLED`; grant is tool-only and creates no provider authority | Registry §12.1; Gateway §21.2 rule 10; Cloudflare §25.2 |
| 13 | Exact operator / `mellycore_operator` | Restricted class; `mcp_oauth_grant`; **`provider_account`** | Tenant exact; provider scope supplied; tool scope absent | D4 / R0 | Deny before credential resolution | Authentication target incompatible with class and D4; provider-targeted OAuth prohibited | Registry §§12.1, 13.2; Gateway §14.2; Cloudflare §11.1.1 |
| 14 | Exact operator / `mellycore_operator` | Any normal Cloudflare read class; provider mode; `provider_account` | Tenant exact; provider scope required; tool N/A | Normal Cloudflare provider API read / R1 | Deny | `mellycore_operator` is not provider-API eligible and class is incompatible | Registry §7.5; Gateway Rule 16.7; Cloudflare Rule 10.2 |
| 15 | Exact operator / `mellycore_operator` | Restricted class; valid tool mode/target | Tenant exact; provider N/A; exact tool but requested tool capability not allowed | D4 / R0 | Deny | Missing exact restricted-tool capability authorization | Registry §24; Gateway §21.2 rules 5, 11; Cloudflare §25.2 |
| 16 | Exact operator / `mellycore_operator` | Two matching restricted profiles; same valid mode/target | Tenant exact; provider N/A; exact tool | D4 / R0 | Deny before material resolution | Multiple compatible credential profiles; no best-available choice | Registry §13.2; Gateway §14.2 |
