# MellyCore Enterprise Provider Docs Integration Review 003

## 1. Title and status

**Task ID:** `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003`

**Record ID:** `MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003`

**Review date:** 2026-08-03

**Status:** Complete. Independent post-remediation documentation-gate review.

**Gate decision:** `FAIL_REMEDIATION_REQUIRED`.

**Finding counts:** P0 = 0, P1 = 2, P2 = 1, P3 = 2.

**`P1-201` closure result:** `PARTIALLY_CLOSED`.

This record is documentation evidence only. It authorizes no implementation,
no provider authentication, no provider API call, no MCP or integration-fabric
connection, no webhook registration, no credential, and no deployment.

## 2. Purpose

Independently verify whether commit `8e1f7289345eb556d6b1972cac61c0aa9a950c89`
(`docs: align enterprise provider credential classes`) fully closes Review 002
finding `P1-201` — Cloudflare provider-specific credential labels versus
canonical Provider Registry credential-profile classes and Integration Gateway
runtime resolution — without introducing competing credential-class ownership,
runtime alias interpretation, credential fallback, identity-mode fallback,
read-to-write widening, operator-investigation privilege escalation, Cloudflare
API authority for documentation-only tools, risk-tier regression, capability or
prohibition regression, Gateway/Registry inconsistency, or unsafe scaffold
assumptions.

The reviewer did not author the remediation. Every remediation claim was
treated as unverified until confirmed directly from canonical repository
evidence.

## 3. Scope

**In scope.** Repository identity and history verification; read-only
`clean-origin` fetch; complete reads of the four amended canonical contracts,
the governing ADR, the Fabric Comparison spec, the Review 001 and Review 002
records and task reports, the credential-class remediation report, and the four
shared-context files plus `SAFETY_CONTRACT.md` and `VALIDATION.md`; full
inspection of the `8e1f728…` diff against parent
`95b5b03defcfa9530f7e2625f12648aa8eac918c`; independent verification of
`P1-201`; bounded deterministic scenario replay; regression search across
credential, identity, risk, and authority dimensions; read-only documentation
validators; and creation of exactly one local documentation commit containing
this record, the Review 003 task report, and bounded shared-context updates.

**Out of scope, and not performed.** Any modification of a reviewed ADR,
contract, provider pack, remediation report, Review 001 record, or Review 002
record; any repair of a finding; any source-code change; any Adapter Scaffold
work; any provider authentication or API execution; any MCP or
integration-fabric connection; any webhook registration; any credential,
secret, or `.env` handling; any dependency, lockfile, or workflow change; and
any push, pull request, merge, tag, remote branch, deployment, or MellyTrade
interaction.

## 4. Starting repository state

| Dimension | Observed |
| --- | --- |
| Repository path | `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios` |
| Resolved root | `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` |
| Starting branch | `docs/mellycore-enterprise-provider-credential-class-conformance-remediation-001` |
| Starting HEAD | `8e1f7289345eb556d6b1972cac61c0aa9a950c89` |
| HEAD subject | `docs: align enterprise provider credential classes` |
| HEAD parent | `95b5b03defcfa9530f7e2625f12648aa8eac918c` |
| Worktree / index | Clean (`git status --short --branch` reported only the branch line) |
| Canonical remote | `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git` |
| `clean-origin/main` after fetch | `947f33d27d5546775186e96bdc61e30db78c0b3d` — unchanged, no drift |
| Review 003 branch before this task | Absent locally and on `clean-origin` |
| Review branch created | `docs/mellycore-enterprise-provider-docs-integration-review-003`, from `8e1f728…`, not from `clean-origin/main` |

`origin` (`https://github.com/Melly-999/mellycore-aios.git`) exists in the
remote list and was **not** contacted.

## 5. Reviewed commits

| Commit | Role | Verified |
| --- | --- | --- |
| `8a5c4ebf16485d6e7508b811c4ccdd8032dfdcb2` | Review 001 (`FAIL_REMEDIATION_REQUIRED`; P0 0, P1 4, P2 2, P3 3) | Referenced; record unchanged |
| `95b5b03defcfa9530f7e2625f12648aa8eac918c` | Review 002 (`FAIL_REMEDIATION_REQUIRED`; sole blocker `P1-201`) | Parent of the remediation commit; confirmed |
| `8e1f7289345eb556d6b1972cac61c0aa9a950c89` | Credential-class conformance remediation under review | Confirmed: expected parent, expected subject, exactly nine changed paths |

Remediation commit changed paths (nine, as reported):

1. `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
2. `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
3. `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
4. `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
5. `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md`
6. `shared_context/AGENT_HANDOFF.md`
7. `shared_context/PROJECT_STATE.md`
8. `shared_context/ROADMAP.md`
9. `shared_context/RUN_QUEUE.md`

No Review 001 record, Review 002 record, prior remediation report, ADR,
Marketing Pack, or Fabric Comparison spec appears in that path set.

## 6. Reviewed documents

Seventeen documents were read for this review:

| # | Document | Depth |
| --- | --- | --- |
| 1 | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | Complete |
| 2 | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | Complete |
| 3 | `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md` | Complete for §§7–15, §25, §31, §33, §35; structural sweep elsewhere |
| 4 | `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md` | §§1–13, §21, §32 complete; structural sweep elsewhere |
| 5 | `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` | §§1–7 (authority and ownership) |
| 6 | `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | §§11–19 complete; full-text search for identity/operator terms |
| 7 | `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md` | §§11–16 complete, including the `P1-201` statement |
| 8 | `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md` | `P1-003` evidence (§12, §22, §29) |
| 9 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md` | Baseline hash only; content unchanged |
| 10 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md` | Baseline hash only; content unchanged |
| 11 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md` | `P1-003` treatment row |
| 12 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md` | Baseline hash only; content unchanged |
| 13 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md` | Complete |
| 14 | `shared_context/PROJECT_STATE.md` | Enterprise-provider region complete |
| 15 | `shared_context/ROADMAP.md` | Enterprise-provider sequence complete |
| 16 | `shared_context/RUN_QUEUE.md` | Enterprise-provider queue complete |
| 17 | `shared_context/AGENT_HANDOFF.md` | Latest and previous update blocks complete |

`shared_context/SAFETY_CONTRACT.md` and `shared_context/VALIDATION.md` were
read in full as governing authorities.

## 7. Independent method

1. Repository, branch, HEAD, parent, subject, remote, and worktree gate.
2. Read-only `clean-origin` fetch and canonical-main drift check.
3. Blob-ID baselines captured for every reviewed document and the four
   shared-context files before any edit.
4. Review branch created from the remediation commit.
5. Full diff of `8e1f728…` inspected hunk by hunk against its parent, with the
   pre-remediation text of every affected region retrieved from `95b5b03…` for
   comparison.
6. Contract text read directly. Remediation prose and task-report claims were
   never accepted as evidence for the fact they assert.
7. Counting checks executed mechanically (canonical classes, projection rows,
   capability rows, prohibition rows) rather than read from summary tables.
8. Sixteen deterministic scenarios replayed against the contract text, each
   resolved to an outcome and an exact source section, or marked as requiring
   architectural interpretation.
9. Repository-wide searches for residual runtime uses of `investigation`, for
   the newly coined identity token, and for the global task pointer.
10. Read-only validators executed and reported truthfully.

## 8. Immutable baselines

Recorded at HEAD `8e1f728…` before branch creation and before any edit. These
are re-verified after the Review 003 commit.

| Path | Git blob ID |
| --- | --- |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | `8ae0ae0afb972a44b1f859ce2c919e04ca84aaff` |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | `b6fcbebdeaf4bb24af91635cd69c3851741864d1` |
| `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md` | `40f227dd1c5fd0e90f941acdb6999c79f2d285be` |
| `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md` | `ff23e9238317d0df9acd58f6080e0163083e1d7e` |
| `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` | `5febae25d2fb315072a35cbe556d02c709308f59` |
| `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md` | `5ae4f4695746e28df73fd9da17ff9017a2102fb0` |
| `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md` | `09804c6184195c25c2754ea201c5282cb96c1ea3` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md` | `8d768fb9a89055e13193f1f2879c1917e6e7283f` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md` | `45685cacd2d64f1f8d96627ff4df28b086de6e7a` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md` | `07916d0c444ad6455e8d2f632444cc4e5decb0af` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md` | `d99129e8ebc1f004dc34dde078a8ef23e6070088` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md` | `23a1769ddae9511a52ec569f3eb648f0481a48b5` |
| `shared_context/SAFETY_CONTRACT.md` | `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` |
| `shared_context/VALIDATION.md` | `a4acf641d3cc1551ad1513bcc8ec0cc619be941b` |

Shared-context blob IDs before this review's edits (these four are expected to
change, and only these four):

| Path | Git blob ID at `8e1f728…` |
| --- | --- |
| `shared_context/PROJECT_STATE.md` | `eca1be0fb594f705cae6acce325932cbb910613a` |
| `shared_context/ROADMAP.md` | `12072b416f35763f956daeceb0c0743e4d867a7a` |
| `shared_context/RUN_QUEUE.md` | `c0f0288336c946312c23fdc1ddbc6c263175743e` |
| `shared_context/AGENT_HANDOFF.md` | `a8221c3c0e0a667c4bf66da5e8240904727e1bab` |

Structural baselines, measured mechanically at `8e1f728…`:

| Quantity | Value | Method |
| --- | --- | --- |
| Canonical credential-profile classes (Registry §13.2) | 9 | Row extraction from §13.2, header excluded |
| Cloudflare normative projection rows (Cloudflare §11.1.1) | 5 | Row count |
| Cloudflare capability rows | 58 (D1 16, D2 16, D3 23, D4 3) | Regex row count |
| Cloudflare prohibition rows | 13 (`P-01`…`P-13`) | Regex row count |

## 9. `P1-201` baseline

Review 002 §14 recorded `FAIL — P1-201 (root cause: incomplete closure of
Review 001 P1-003)` with four consequences:

1. **`CF_MCP_OPERATOR` unrepresentable.** Cloudflare §13.4.0 pins D4 to
   MellyCore-operator identity with a documentation-scoped profile carrying no
   account grant. None of the then-eight canonical classes admitted the
   MellyCore operator identity type, and neither `mcp_oauth_grant` nor
   `no_auth_public_documentation` was a permitted mode for any of them.
2. **Registry self-contradiction.** `credential_class: investigation` was
   retained in §13.1 while no §13.2 class produced it.
3. **Gateway self-contradiction.** Gateway §§34.1–34.6 labelled `CF_*` values
   "Credential class" although §14.2 denied anything that is not one exact
   Registry §13.2 identifier.
4. **Unstated tractable mappings.** `CF_WRITE_CONTROLLED` and `CF_CONTAIN` were
   inferable; `CF_READ` was genuinely ambiguous between `read_only_delegated`
   and `read_only_service`.

Review 002 recorded the direction of failure as safe (deny, not permit), hence
P1 rather than P0. That lineage traces to Review 001 `P1-003`, whose required
repair was "an explicit projection to `credential_class`, `identity_type`,
`supported_auth_modes`, integration class and allowed capabilities".

## 10. Remediation assessment

The remediation is substantial and largely correct. Verified directly from the
contract text rather than from its report:

- Registry §13.1 now describes `credential_class` as "Coarse descriptive
  metadata derived from `credential_profile_class` … never a runtime-selection
  identifier", and `credential_profile_class` now prohibits "provider-local
  requirement labels and pack-local aliases … as stored/runtime values".
- Registry §13.2 gains a ninth row, `restricted_operator_investigation`, and a
  normative **Concrete binding rule** requiring exactly one
  `required_credential_profile_class` per concrete registration before Gateway
  resolution, with zero or multiple compatible profiles denying and no
  best-available selection, delegated-to-service fallback, or read-to-write
  widening.
- Registry §14.2 gains rule 8, "One concrete capability, one canonical class",
  denying missing, provider-local, unresolved, or multiply applicable values.
- Registry §26.2 states the four Cloudflare label projections explicitly and
  records that "The Gateway never receives or interprets a `CF_*` label".
- Cloudflare §11.1 reclassifies each `CF_*` name as a provider-specific
  credential **requirement label**, and §11.1.1 adds the five-row normative
  projection table with the eleven reviewed columns.
- Cloudflare §13.0 adds the statement that the canonical field, "not attribute
  (11), is the sole Gateway resolution input".
- Gateway §14.2 adds the ninth class and the pre-runtime projection
  requirement; §§34.1–34.6 replace every "Credential class: `CF_*`" row with a
  separated "Provider requirement label" plus "Canonical class" pair.
- The Cybersecurity Pack §12 adds the ninth class and defers `CF_*` semantics
  to the Cloudflare contract.

Two residual defects prevent full closure, both concerning the newly created
restricted-tool path. They are recorded as `P1-301` and `P1-302` in Section 29
and are the reason this gate fails.

The remediation also removed a duplicate `shared_context/SAFETY_CONTRACT.md`
entry from the Cybersecurity Pack §3 authority list. This was independently
checked against `95b5b03…`: the pre-remediation list contained the path at both
position 1 and position 9. The Safety Contract remains item 1 and its authority
is unchanged. This is a correct deduplication, not a safety regression.

## 11. `P1-201` closure matrix

| # | `P1-201` sub-defect | Required outcome | Post-remediation evidence | Verified? | Residual |
| --- | --- | --- | --- | --- | --- |
| 1a | `CF_MCP_OPERATOR` has no canonical class | A canonical class admits the operator identity and the two documentation auth modes | Registry §13.2 row `restricted_operator_investigation`, `identity_type: mellycore_operator`, modes `no_auth_public_documentation` \| `mcp_oauth_grant` | **Yes** | None |
| 1b | D4 capabilities cannot declare a conforming class | Every D4 registration binds exactly one canonical class | Cloudflare §13.4.0 and §11.1.1 row 4; Registry §14.2 rule 8 | **Yes** | None |
| 1c | The operator identity has a runtime expression | The Gateway can resolve a request whose acting identity is the MellyCore operator | **Not present.** Gateway §9.2, Rule 16.7, §17 step 13, and the §23 envelope admit only `delegated_user` \| `service_account` | **No** | **`P1-301`** |
| 1d | The restricted-tool path fits the provider record's scope model | A D4 invocation with empty account/zone binding resolves | **Not present.** Registry §26.1 still declares `required_scope_dimensions: tenant, account, zone` for provider `cloudflare`, and §11.2 rule 2 fails closed on a missing required dimension | **No** | **`P1-302`** |
| 2 | Orphaned `credential_class: investigation` | Derived, descriptive, non-normative, never a selector | Registry §13.1; Cloudflare §11.1.1 row 5; repository sweep finds no runtime use | **Yes** | None |
| 3 | Gateway §34 contradicted Gateway §14.2 | §34 uses canonical identifiers only | Gateway §34 preamble and §§34.1–34.6 label/class separation | **Yes** | None |
| 4 | `CF_READ` ambiguous between two read classes | A normative selector reduces it to exactly one before runtime | Registry §13.2 concrete binding rule; Cloudflare §11.1.1 row 1; Cloudflare §§13.1.0/13.2.0; Gateway §34 preamble | **Yes** | `P3-301` (selector field never named) |

**Result: `P1-201` is `PARTIALLY_CLOSED`.** Four of six sub-defects are
independently verified closed. The two open sub-defects are the same one Review
002 named first — the MellyCore operator identity — closed on the Registry side
and left open on the Gateway and provider-record sides.

## 12. Canonical ownership review

**Result: PASS.** Ownership is single-sourced and non-competing.

| Concern | Sole normative owner | Enforcer | Verified statement |
| --- | --- | --- | --- |
| Canonical credential-profile class catalogue | Registry §13.2 | Gateway §14.2 | "A provider-specific contract may narrow a canonical class, but may not invent another class or widen its capability/use constraint." |
| Concrete profile pinning (auth mode, scope) | Registry §13.1 | Gateway §14.2 | "`authentication_mode` … never selected at runtime from a list" |
| Provider-specific requirement labels and their projection | Cloudflare §11, §11.1.1 | Cloudflare contract, before runtime | "The Gateway never receives or interprets a `CF_*` label" (Registry §26.2) |
| Runtime profile resolution | Gateway §14.2, §17 step 14 | Gateway | "Zero or multiple matches deny" |
| Pack references | Cybersecurity Pack §12 | — | "this pack does not reinterpret those labels" |

No second catalogue, no second projection owner, and no provider-local label
acting as an independent authorization identity was found. Precedence remains
identical in Registry §25.2 and Gateway §33.

## 13. Nine-class catalogue review

**Result: PASS, with one P3.**

Mechanically extracted from Registry §13.2 (header excluded), in order:

| # | Class | `identity_type` | `credential_class` | Permitted mode(s) | Use constraint |
| --- | --- | --- | --- | --- | --- |
| 1 | `read_only_delegated` | `delegated_end_user` | `read` | `delegated_oauth` | read, proposal; never mutation |
| 2 | `read_only_service` | `service_account` | `read` | one of four service modes | read, proposal; service identity labelled |
| 3 | `controlled_write` | delegated **or** service | `controlled_write` | one contract-approved mode | mutation; separate read profile required |
| 4 | `event_verification` | `provider_credential` | `read` | `signed_request` \| `mtls` \| `webhook_secret` | inbound verification only |
| 5 | `integration_fabric_read` | delegated **or** service | `read` | `fabric_delegated_identity` | fabric read/proposal; downstream provenance |
| 6 | `integration_fabric_controlled_write` | delegated **or** service | `controlled_write` | `fabric_delegated_identity` | fabric mutation; equivalence evidence |
| 7 | `emergency_containment` | `service_account` | `containment` | one contract-approved service mode | containment allowlist only |
| 8 | `reporting_only` | `service_account` | `read` | one of three service modes | aggregate reporting only |
| 9 | `restricted_operator_investigation` | `mellycore_operator` | `investigation` | `no_auth_public_documentation` \| `mcp_oauth_grant` | documentation/investigation only; R0–R2 max |

- Exactly nine rows; identifiers unique; no duplicate or near-synonym.
- Each row declares an identity model, a coarse credential class, a closed
  authentication-mode set, and a capability/use constraint.
- Maximum-risk posture is explicit for rows 3, 6, 7 (R5-capable through their
  mutation/containment constraint) and row 9 (`R0-R2 maximum`); rows 1, 2, 4,
  5, 8 are constrained to read/proposal/inbound-verification use, which bounds
  them at R2 by ADR §13's tier definitions. This is derivable but not stated as
  a per-row numeric ceiling for rows 1–8.
- No class is stated as authorization or approval; Registry §21.2 rule 6 and
  §13.4 keep class distinct from the eight facts.
- Provider-specific contracts cannot invent a tenth class (§13.2 closing
  paragraph; §14.2 rule 8).

`P3-302` records that `mellycore_operator` is a newly coined token appearing
exactly once in the repository, while the Registry requires `identity_type` to
be "One of the seven ADR §11 identity types" and no canonical token list for
those seven exists anywhere in the chain.

## 14. `restricted_operator_investigation` review

**Result: FAIL — the class definition is correct; its runtime expression is
absent.**

Verified present in the class definition and its provider projection:

| Required property | Evidence | Verified |
| --- | --- | --- |
| Operator-bound | Registry §13.2 `identity_type: mellycore_operator`; Cloudflare §11.1.1 "MellyCore operator only" | Yes |
| Human-directed, no agent initiation | Cloudflare §13.4.0; Gateway §34.6; Cloudflare §25.2 item 1 | Yes |
| Documentation/investigation tools only | Registry §13.2; Gateway §14.2; Cloudflare §11.1.1 | Yes |
| R0–R2 maximum | Registry §13.2 (`R0-R2 maximum`); Cloudflare §11.1.1 (`R2`, D4 v1.0 remains R0) | Yes |
| Non-provider-account | Registry §13.2 ("no provider account access"); Cloudflare §11.2 rule 2 (empty account/zone/resource binding); Gateway §14.2 ("empty provider-account binding") | Yes |
| Non-provider-API | Registry §13.2; Cloudflare §11.1.1 "Provider API authority: **None**"; Gateway §14.2 | Yes |
| Non-mutating | Gateway §14.2 (`mutation_prohibited: true`); Cloudflare §11.1.1 "Mutation authority: **None**" | Yes |
| No proposal evidence | Registry §13.2; Gateway Rule 21.5; Cloudflare §13.4.0 output rule | Yes |
| No service-account fallback | Registry §13.2 closing paragraph; Cloudflare §11.1.1; Gateway §14.3 | Yes |
| Cannot use a general read credential | Registry §13.2 ("cannot … be substituted for any read, write, event, fabric, containment, or reporting class") | Yes |
| Valid only for a registered restricted tool surface | Registry §13.2; Gateway §14.2; Cloudflare §11.1.1 | Yes |
| Separately subject to tenant, capability, runtime, operator authorization | Registry §21.1 facts 5–7; Cloudflare §25.2 | Yes |
| Fully audited | Cloudflare §31.4; Gateway §29 | Yes |
| **Resolvable by the Gateway** | **Absent** — see `P1-301` | **No** |
| **Expressible under the Cloudflare provider record's scope model** | **Absent** — see `P1-302` | **No** |

Ineligibility checks — the class cannot be selected for Cloudflare REST or
GraphQL API calls, WAF reads, zone reads, account reads, writes, containment,
provider-native investigation APIs, or unrestricted MCP tools. Each is denied
by an explicit statement, not by inference: Registry §13.2 ("cannot be used by
a provider API capability"), Cloudflare §11.1.1 row 4 (Provider API authority
**None**, Mutation authority **None**), Cloudflare P-01 and P-02 (unrestricted
and Code Mode execution prohibited), and Gateway §21.2 rules 1–2. **No wording
was found that permits any such interpretation.** This is why the two open
defects are P1 (deny-direction conformance failures) and not P0.

## 15. Cloudflare projection review

**Result: PASS on determinism of the table itself.** Cloudflare §11.1.1
contains exactly five rows, each carrying all eleven reviewed dimensions.

| Row | Label status | Canonical projection | Concrete binding rule | Identity constraint | Provider API | MCP | Mutation | Max risk | Fail-closed | Migration/retirement |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `CF_READ` | Provider shorthand only | one of `read_only_delegated`, `read_only_service` | Selected pre-runtime from the declared acting-identity mode | Delegated user or labelled service account; no switching | Bounded read, after separate authorization | None | None | R2 | Zero/multiple/identity mismatch/unresolved deny | Migrate to one identity-specific class |
| `CF_WRITE_CONTROLLED` | Provider shorthand only | `controlled_write` | Every D3 non-containment registration | One declared delegated or service mode; separate read profile | Exact approved write surface | None | R4/R5 with full controls | R5 | Missing/multiple/permission/approval mismatch deny | Replace runtime use with `controlled_write` |
| `CF_CONTAIN` | Provider shorthand only | `emergency_containment` | Containment registrations plus containment allowlist | Labelled service account only | Narrow containment surface | None | Approved containment only | R5 | Missing/multiple/absent approval-audit-verification deny | Replace runtime use with `emergency_containment` |
| `CF_MCP_OPERATOR` | Provider shorthand only | `restricted_operator_investigation` | D4 registrations plus separately registered restricted tool/MCP record | MellyCore operator only; empty account/resource binding | **None** | Documentation/investigation only | **None** | R2 (D4 v1.0 R0) | Missing/multiple/tool mismatch/account binding/API or mutation attempt deny and audit | Migrate runtime-looking uses |
| `credential_class: investigation` | Derived metadata only, not a label | Produced only by `restricted_operator_investigation` | No runtime component interprets it | Operator only under the restricted-tool record | **None** | Documentation/investigation only | **None** | R2 | Any selector or alias use denies | Retire standalone/runtime uses |

No row relies on unstated interpretation **for the projection step**. The
interpretation gap is downstream of the projection, in Gateway resolution and
in the Cloudflare provider record's scope declaration.

## 16. `CF_READ` review

**Result: PASS, with `P3-301`.**

- It is a provider-specific requirement label only (Cloudflare §11.1; Gateway
  §34 preamble; Registry §26.2).
- It permits exactly `read_only_delegated` or `read_only_service` and nothing
  else (Cloudflare §11.1.1 row 1; Registry §26.2).
- Every concrete registration selects exactly one (Registry §13.2 concrete
  binding rule; Registry §14.2 rule 8; Cloudflare §13.1.0 and §13.2.0).
- The identity mode is declared before runtime; the Gateway does not choose
  (Gateway §14.2: "the Gateway never interprets a pack-local alias or chooses
  among authentication modes"; Registry §13.2: "The Gateway never chooses
  between classes, identity modes, or authentication modes").
- Authorization records bind to the selected class (Registry §13.2).
- Zero matches deny and multiple matches deny (Gateway §14.2).
- Delegated operations cannot silently become service operations, and the
  reverse impersonation is barred (Gateway §15 rule 4, §14.3, §16 rule 1;
  Registry §12; ADR §11).

`P3-301`: no document names the field that carries the "declared
acting-identity mode". Registry §14.1 field (12) `required_identity_type` is
the only candidate, and a missing value denies under §14.2 rule 8, so behavior
is unaffected; naming the field would remove a traceability gap.

## 17. `CF_WRITE_CONTROLLED` review

**Result: PASS.**

- Deterministic single projection to `controlled_write` (Cloudflare §11.1.1
  row 2; Registry §26.2; Gateway §§34.3–34.5).
- No projection to any read-only class, and read-profile reuse is prohibited
  (Cloudflare §11.2 rule 4; Gateway §14.3 "Read credential → write credential
  escalation → Deny; audited security event").
- Separate write credentials remain required (Registry §13.2 row 3 "separate
  read profile required"; ADR §12).
- R3–R5 approval unchanged: Cloudflare §13.3.0 keeps every D3 capability at an
  R4 minimum with explicit human approval, and Rule 13.3.3 ("no R3 in v1.0")
  is intact.
- Durable audit intent remains required (Gateway §17 step 21, §29.2).
- Verification and reconciliation remain mandatory (Cloudflare §32; Gateway
  §17 step 24, §26.3; prohibition `P-10`).

## 18. `CF_CONTAIN` review

**Result: PASS.**

- Deterministic single projection to `emergency_containment`.
- Class selection does not authorize containment: Gateway Rule 31.1 states a
  containment action that mutates provider state "is itself a mutation
  requiring approval … idempotency, verification, and audit", and Cloudflare
  §11.1.1 row 3 states "class membership alone never authorizes it".
- Existing R5 classification is intact — the D3 row set is byte-identical to
  the parent commit, including `D3-10` zone-wide `set_block` at R5.
- Exact target approval remains mandatory (Gateway §18.1 twelve-element
  binding; ADR §14 R5 exact enumeration).
- Runtime enablement remains a separate fact (Registry §21.1 fact 7; Gateway
  §17 step 8).
- Audit and verification remain mandatory; no emergency or fallback bypass
  exists (Gateway Rule 31.2 "No containment action is authorized for runtime
  by this contract"; §14.3 deny list).

## 19. `CF_MCP_OPERATOR` review

**Result: FAIL — `P1-301` and `P1-302`.**

Verified correct:

- Deterministic single projection to `restricted_operator_investigation`.
- No Cloudflare account grant; no Cloudflare API credential is resolved; no
  provider API call is permitted (Cloudflare §11.1.1 row 4; §11.2 rule 2;
  §13.4.1 "Account access: none").
- No mutation or proposal execution (Gateway §14.2; Rule 21.5).
- Only a separately registered restricted documentation/investigation tool may
  be used (Registry §13.2; Gateway §14.2; Gateway §34.6 "Restricted-tool
  capability record plus separate MCP record").
- Tool discovery does not authorize execution (Gateway §21.2 rules 6–7).
- Unrestricted MCP is prohibited (`P-01`, `P-02`; ADR §17; Gateway §21.2
  rule 1).
- Operator identity, tenant, capability, runtime state, and tool registration
  are all required (Cloudflare §25.2; Registry §21.1 facts 1–7).

Verified defective:

- The Gateway cannot express the operator acting identity (`P1-301`).
- The Cloudflare provider record's `required_scope_dimensions` contradicts the
  mandatory empty account/zone binding (`P1-302`).

## 20. Residual `investigation` review

**Result: PASS.**

A repository-wide sweep of `docs/**` and `shared_context/**` for `investigation`
outside the `restricted_operator_investigation` identifier returns only:

- Registry §13.1 — declared as derived coarse metadata, "never a
  runtime-selection identifier".
- Cloudflare §11.1.1 row 5 — declared derived, non-normative, never
  interpreted at runtime.
- Descriptive prose: domain naming ("Operator investigation (D4)"), ADR §4
  narrative, Gateway §21.3 phase 2 name, Cybersecurity Pack
  `security.incidents.investigation.propose` (an R2 capability ID in a
  different namespace, unrelated to credential classes), and shared-context
  narrative.

No bare `credential_class: investigation` is used as a runtime class, a Gateway
selector, an authorization-record value, or a credential-profile class
anywhere. No example implies it is a Registry class identifier.

## 21. Gateway §14.2 review

**Result: PASS as written; its scope is where `P1-301` originates.**

Verified in §14.2:

- Only exact Registry §13.2 identifiers are accepted ("The requested class MUST
  be one exact Registry §13.2 identifier").
- Unresolved provider labels deny ("An unresolved label, a label supplied as
  the runtime class, or a registration retaining multiple candidate classes
  denies before credential material is resolved").
- A missing canonical class denies (Registry §14.2 rule 8 upstream; §17 step 14
  `CREDENTIAL_UNAVAILABLE` downstream).
- Zero matching profiles deny; multiple matching profiles deny.
- No provider alias interpretation ("the Gateway never interprets a pack-local
  alias").
- No dynamic identity-mode switching ("never … chooses among authentication
  modes"; §14.3 delegated→service fallback denied and audited).
- Exact tenant, provider, environment, native scope, identity mode, capability,
  and credential class are all matched simultaneously.

The defect is not in §14.2's rules but in the identity vocabulary they depend
on: §14.2 requires the resolved profile's **identity** to match the acting
identity type, and the acting identity type is a closed two-value enumeration
elsewhere in the same contract.

## 22. Gateway §34 review

**Result: PASS for §§34.1–34.5; FAIL for §34.6 in combination with §9.2,
Rule 16.7, §17 step 13, and §23.**

- Every example now uses canonical identifiers in a "Canonical class" row, with
  `CF_*` confined to a separate "Provider requirement label" row.
- The §34 preamble states `CF_*` values "are provider-contract requirement
  labels, not Registry classes and not Gateway inputs", that projection occurs
  before runtime resolution, and that the read examples "deliberately pin a
  service-account mode".
- §34.6 (D4) matches the Registry and the Cloudflare contract on class, target
  scope, risk tier, execution path, audit, and fail-closed posture.
- No example introduces an exception to canonical resolution, and §34.7's
  closing paragraph now restates the determinism rules.

The failure is a contradiction between §34.6's premise and the Gateway's own
identity requirements, detailed as `P1-301`. §34.7's claim that "The Cloudflare
contract is enforceable through this Gateway contract with no weakening
detected" cannot hold for D4 while §9.2 denies every request lacking a
delegated-user or service-account acting identity.

## 23. Cloudflare integrity review

**Result: PASS.**

| Check | Result | Method |
| --- | --- | --- |
| 58 capability rows present | D1 16, D2 16, D3 23, D4 3 = 58 | Regex row count at HEAD and at `95b5b03…` |
| 13 prohibition rows present | `P-01`…`P-13` | Regex row count at HEAD and at `95b5b03…` |
| Substantive content unchanged | **All 71 capability and prohibition rows are byte-identical** to the parent commit | Line-level diff of the extracted row sets |
| Zone-wide Schema Validation `block` remains R5 | `D3-10` R5; §21.4; §14 tier table | Unchanged rows |
| Endpoint-deletion safety | `D3-02` R5 irreversible; §23.1 preconditions; `P-06` bulk/unenumerated deletion prohibited | Unchanged |
| Label-replacement semantics | `D3-03` R4→R5 escalation; §24; `P-07` replace-without-diff prohibited | Unchanged |
| Read-after-write mandatory | §13.3.0; §32; `P-10` | Unchanged |
| Unknown outcomes require reconciliation | §29.2; Gateway §26.3 `INDETERMINATE` | Unchanged |
| Blind mutation retries prohibited | §29.2; Gateway §26.2 rule 1 | Unchanged |
| MCP documentation-only | §25.1; Gateway §21.2 rule 9; `P-01`, `P-02` | Unchanged |
| `CF_MCP_OPERATOR` gains no API authority | §11.1.1 row 4 "Provider API authority: **None**" | New text, verified restrictive |

The remediation's edits to this contract are confined to §3 (gate item count),
§10.1, §11.1, §11.1.1 (new), §11.2 rule 2, §13.0, the four domain default
blocks, §25.2 item 3, and §35 item 6. None touches a capability row, a
prohibition row, or a risk classification.

## 24. Cybersecurity Pack regression review

**Result: PASS, with `P3-303` folded into `P3-302` as a shared vocabulary
observation.**

| Check | Result |
| --- | --- |
| Seven providers remain | `microsoft_defender_xdr_graph_security`, `github_advanced_security`, `cloudflare`, `okta_workforce_identity`, `splunk_security_analytics`, `crowdstrike_falcon`, `snyk_developer_security` — unchanged |
| R0–R2 initial ceiling remains | §4, §7, §11 and every per-provider "Initial risk ceiling: R2" — unchanged |
| Ninth class referenced correctly | §12 adds `restricted_operator_investigation`, scoped "Cloudflare D4 only; described, not connected or configured" |
| Cloudflare projection delegated to the provider contract | New §12 paragraph: "this pack does not reinterpret those labels" |
| Provider-local labels are not runtime classes | Stated explicitly in the same paragraph and in §21 |
| Authority references remain valid | §3 items 1–9; `SAFETY_CONTRACT.md` remains item 1; the removed entry was a verified duplicate |
| No new authorization | §5 non-authorizations, §7 eight-fact table, and §32 prerequisites unchanged apart from the Review 003 sequence pointer |

The §12 table lists seven of the nine canonical classes without declaring
itself a non-exhaustive projection of Registry §13.2. This shape pre-dates the
remediation, Registry §13.2 is declared sole owner, and Gateway §14.2 accepts
only Registry identifiers, so no competing catalogue is created. Recorded as an
editorial observation only.

## 25. Eight-fact separation review

**Result: PASS.** No new credential-class language collapses any of the eight
facts, and the existence of `restricted_operator_investigation` implies none of
them.

| Fact | Preserved by | Ninth-class interaction |
| --- | --- | --- |
| 1 Provider registered | Registry §21.1; §21.2 rule 6 | Class membership is not registration |
| 2 Adapter implemented | Registry §21.1; Gateway §17 step 7 | Restricted tool is not an adapter; scaffolding remains blocked |
| 3 Credential configured | Registry §13.4 | "A `credential_profile` record describes a credential that *would* be used" |
| 4 Credential verified | Registry §21.1; §13.1 `last_verification_time` | Unchanged |
| 5 Tenant authorized | Registry §21.3–21.5; Gateway §17 step 9 | Cloudflare §25.2 item 2 requires explicit tenant selection separately |
| 6 Capability authorized | Registry §21.3–21.5; Gateway §17 step 10 | Cloudflare Rule 10.1: a capability ID is an input, not a grant |
| 7 Runtime enabled | Registry §21.1; Gateway §17 step 8, §32 | Gateway Rule 32.1 asserts none currently passes |
| 8 Operation approved | Control Plane §16.1 + Gateway §18 | Registry §21.5 forbids embedding fact 8 in a standing record |

Registry §13.2's closing paragraph and the new concrete binding rule keep class
distinct from configuration, verification, authorization, enablement, and
approval, in the exact wording the invariant requires.

## 26. Deterministic scenario results

Sixteen scenarios replayed against contract text. Fifteen resolve
deterministically; scenario 9 requires architectural interpretation.

| # | Request | Label | Canonical class | Identity mode | Tenant | Native scope | Provider API | Tool authority | Tier | Facts required | Approval | Audit | Expected outcome | Exact fail-closed reason | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cloudflare read, delegated identity | `CF_READ` | `read_only_delegated` | delegated | required | zone allowlist | bounded read | n/a | R1 | 1–7; 8 `not_required` | resolved `not_required` | full decision record | **Resolves**, then denies today on facts 5–7 and `adapter_state: blocked` | `RUNTIME_NOT_ENABLED` / `ADAPTER_UNAVAILABLE` | Gateway §34 preamble, §17, §18.4; Registry §21.1 |
| 2 | Cloudflare read, service identity | `CF_READ` | `read_only_service` | service | required | zone allowlist | bounded read | n/a | R1 | as above | as above | service identity labelled | **Resolves**, same standing denial today | as above | Gateway §34.1, §16 |
| 3 | Cloudflare read, two compatible profiles match | `CF_READ` | one pinned class | as declared | required | allowlist | none | n/a | R1 | — | — | denial audited | **Deny** | Multiple matches deny | Gateway §14.2; Registry §13.2 |
| 4 | Cloudflare read, no profile matches | `CF_READ` | one pinned class | as declared | required | allowlist | none | n/a | R1 | — | — | denial audited | **Deny** `CREDENTIAL_UNAVAILABLE` | Gateway §14.2, §25.2 |
| 5 | Controlled WAF write using a read-only profile | `CF_WRITE_CONTROLLED` | `controlled_write` required | — | required | exact enumeration | none | n/a | R4/R5 | — | — | audited security event | **Deny**, never widened | Read→write escalation prohibited | Gateway §14.3; Cloudflare §11.2 rule 4 |
| 6 | Controlled WAF write using `controlled_write` | `CF_WRITE_CONTROLLED` | `controlled_write` | one declared mode | required | exact enumeration | approved write surface | n/a | R4/R5 | all eight | twelve-element binding | Stage A + Stage B | **Resolves**, denies today on facts 2/5/6/7 | `ADAPTER_UNAVAILABLE` | Gateway §17, §18.1, §29 |
| 7 | R5 containment, `emergency_containment`, no approval | `CF_CONTAIN` | `emergency_containment` | labelled service | required | containment allowlist | narrow surface | n/a | R5 | 1–7 hold, 8 absent | **missing** | denial audited | **Deny** | `APPROVAL_MISSING`; class membership never authorizes containment | Gateway §17 step 17, Rule 31.1; Cloudflare §11.1.1 |
| 8 | R5 containment, approval present, stale state | `CF_CONTAIN` | `emergency_containment` | labelled service | required | containment allowlist | narrow surface | n/a | R5 | 1–8 | present but drifted | Stage A preserved | **Deny/abort before execution** | `STALE_STATE` / `APPROVAL_STALE`; new diff and re-approval required | Gateway §18.2, §27, Rule 27.1 |
| 9 | D4 documentation lookup, restricted tool registered | `CF_MCP_OPERATOR` | `restricted_operator_investigation` | **`mellycore_operator`** | required | **empty account/zone/resource** | none | documentation only | R0 | 1–7; 8 `not_required` | operator initiation | session transcript metadata | **INDETERMINATE — requires architectural interpretation.** Cloudflare §13.4/§25.2 and Gateway §34.6 present a reachable session; Gateway §9.2, Rule 16.7, §17 step 13, §23 deny for a missing delegated/service acting identity; Registry §26.1 + §11.2 rule 2 deny for missing `account`/`zone` | Not determinable from the contract set | `P1-301`, `P1-302` |
| 10 | D4 lookup, no tool registration | `CF_MCP_OPERATOR` | `restricted_operator_investigation` | operator | required | empty | none | none | R0 | — | — | denial audited | **Deny** | Tool-registration mismatch; unregistered tools are not executable | Cloudflare §11.1.1; Gateway §21.2 rules 5–6 |
| 11 | D4 request attempting a Cloudflare REST API call | `CF_MCP_OPERATOR` | `restricted_operator_investigation` | operator | required | empty | **prohibited** | none | — | — | — | audited security event | **Deny** | Provider API authority **None**; class cannot serve a provider API capability | Cloudflare §11.1.1 row 4, §11.2 rule 2; Registry §13.2 |
| 12 | D4 request attempting a mutation | `CF_MCP_OPERATOR` | `restricted_operator_investigation` | operator | required | empty | prohibited | none | — | — | — | audited security event | **Deny** | `mutation_prohibited: true`; mutation authority **None** | Gateway §14.2, §21.2; Cloudflare §11.1.1 |
| 13 | D4 request with only a normal Cloudflare read credential | `CF_MCP_OPERATOR` | `restricted_operator_investigation` required | operator | required | empty | none | none | R0 | — | — | denial audited | **Deny** | Class mismatch; zero compatible profiles; no substitution across classes | Registry §13.2 closing paragraph; Gateway §14.2 |
| 14 | Provider-local `CF_READ` submitted directly to the Gateway | `CF_READ` supplied as the runtime class | none | — | required | — | none | n/a | — | — | — | denial audited | **Deny** | "a label supplied as the runtime class … denies before credential material is resolved" | Gateway §14.2; Registry §26.2 |
| 15 | Runtime record containing `credential_class: investigation` | — | invalid as a selector | — | required | — | none | n/a | — | — | — | denial audited | **Deny** | Derived metadata only; "Any use as a runtime selector or alias denies" | Registry §13.1; Cloudflare §11.1.1 row 5 |
| 16 | Two `restricted_operator_investigation` profiles match one request | `CF_MCP_OPERATOR` | `restricted_operator_investigation` | operator | required | empty | none | documentation | R0 | — | — | denial audited | **Deny** | Multiple compatible profiles deny | Gateway §14.2; Registry §13.2 |

**Scenario determinism: 15 of 16 deterministic; 1 requires architectural
interpretation.** Under the gate criteria, any scenario requiring architectural
interpretation is P1.

## 27. Cross-reference review

**Result: PASS.**

- Registry §29 item 5, Gateway §37 item 4, Cloudflare §35 item 6, and
  Cybersecurity Pack §32 item 2 all now name
  `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003`, consistently and
  without contradiction.
- Cloudflare §3 now describes the ADR §19 gate as a nine-item gate, matching
  the ADR's expanded item list from the Review 001 remediation.
- Registry §26.2, Gateway §34 preamble, and Cloudflare §11.1.1 state the same
  four projections with no divergence in class names or direction.
- Every path referenced in the amended sections resolves to an existing file.
- No document silently contradicts an accepted document in a way that would
  constitute an implicit amendment (Registry §31; Gateway §39; Cloudflare §38).

## 28. Shared-context review

**Result: PASS.** Every claim written by the remediation into the four
shared-context files was checked against the repository.

| Claim | Verified |
| --- | --- |
| "The documentation gate has **not** passed" | True |
| "`P1-201` closure is not yet independently verified" | True at the time written |
| Registry §13.2 owns a closed nine-value catalogue | True |
| `CF_*` are requirement labels, not runtime classes | True |
| `credential_class: investigation` is descriptive only | True |
| Gateway §§34.1–34.6 use canonical identifiers | True |
| Cybersecurity pack has the ninth class and no duplicate Safety Contract entry | True |
| Exact next task is Review 003 | True |
| Scaffold remains blocked, ineligible, not started, not authorized | True |
| No provider connected, authenticated, credentialed, enabled, live, deployed, implemented | True — no such artifact exists |
| Global OpenAI Batch pointer unchanged | True — thirteen pointer occurrences across five files, none added or removed by the remediation diff |

No shared-context file overstates the remediation, claims connectivity, claims
credentials, or claims runtime implementation.

## 29. New findings

### `P1-301` — the Gateway cannot express the acting identity that the ninth class requires

**Severity:** P1 (blocking conformance defect; deny-direction, no privilege
escalation).

**Locations:** Gateway §9.2 (acting-identity chain field requirements);
Gateway Rule 16.7; Gateway §17 step 13; Gateway §23 (request envelope);
Gateway §14.2; Gateway §34.6 and §34.7; Registry §13.2 row 9.

**Statement.** Registry §13.2 defines `restricted_operator_investigation` with
`identity_type: mellycore_operator`. Gateway §14.2 requires the Gateway to
resolve "a single concrete profile whose class, **identity**, pinned
`authentication_mode`, tenant, provider, environment, scope, and capability
constraints all match". But the Gateway's acting identity is a closed two-value
set everywhere it is defined:

- §9.2: "`delegated_user` | `service_account` — Exactly one required; never
  both, never neither → Deny."
- Rule 16.7: "Exactly one of delegated-user or service-account identity is
  present per request. Both, or neither, denies."
- §17 step 13: "Resolve acting identity type (delegated vs service)" →
  `IDENTITY_UNRESOLVED` on failure.
- §23: `acting_identity_type` (`delegated_user` | `service_account`).

No exemption for restricted-tool, operator-only, or documentation-only paths
exists anywhere in the Gateway contract; §21 (MCP security contract) adds
restrictions but no identity path, and §21.2 rule 5 routes MCP tools through
registered MellyCore capability IDs. Gateway §9.3 rule 1 makes a break in chain
continuity a denial that "is never bridged by inference, defaulting, or 'best
guess'".

**Consequence for the scaffold.** An implementer must choose between two
readings that the documents do not adjudicate: (a) every D4 request denies at
§17 step 13, which makes Cloudflare Domain 4 unreachable and falsifies Gateway
§34.7's "enforceable … with no weakening detected" and Cloudflare §25.2's
nine-condition operational path; or (b) `acting_identity_type` gains a third
value, which is an architectural change that Gateway §39 reserves for an
explicit amendment. That is architectural interpretation, which the gate
criteria forbid.

**Direction of failure:** safe. Under reading (a) the request denies; under
reading (b) the class still carries no provider API, account, or mutation
authority. Hence P1, not P0.

**Evidence that this is the residue of `P1-201`, not a new subject.** Review
002 §14.2 consequence 1 stated the defect as "None of the eight classes admits
the MellyCore operator identity type". The remediation added the identity type
to the Registry catalogue and did not extend the Gateway's identity model to
match, so the same identity gap now sits one layer down.

### `P1-302` — the Cloudflare provider record's required scope dimensions contradict the mandatory empty D4 binding

**Severity:** P1 (blocking conformance defect; deny-direction).

**Locations:** Registry §26.1 (`required_scope_dimensions`); Registry §11.2
rule 2; Cloudflare §11.2 rule 2; Cloudflare §11.1.1 row 4; Gateway §14.2.

**Statement.** Registry §11.2 rule 2 states: "Each provider declares its
`required_scope_dimensions` … A capability invocation missing a required
dimension **fails closed** — it is never widened to a default." Registry §26.1
declares provider `cloudflare` with `required_scope_dimensions`: `tenant`,
`account`, `zone`. D4 capabilities (`cloudflare.docs.search`,
`cloudflare.api_surface.discover`, `cloudflare.mcp.documentation_session`) are
registered under provider `cloudflare` and are counted among its 58
capabilities, yet Cloudflare §11.2 rule 2 requires `CF_MCP_OPERATOR` to have
"an empty Cloudflare account, zone, and resource binding", and §11.1.1 row 4
makes an account binding a denial trigger.

A D4 invocation therefore simultaneously must have no account or zone (or it
denies) and must have an account and zone (or it denies under §11.2 rule 2).

**Corroborating evidence that this is an omission, not an intended reading.**
The same remediation commit edited the adjacent `supported_auth_modes` row of
§26.1 specifically to carve out D4 restricted tools — "Separately registered D4
restricted tools pin exactly one of `no_auth_public_documentation` or
`mcp_oauth_grant` and carry no Cloudflare account binding" — while leaving
`required_scope_dimensions` untouched. The need for a D4 carve-out at the
provider-record level was recognized for one row and missed for the other.

**Direction of failure:** safe (deny). Hence P1, not P0.

### `P2-301` — `mcp_oauth_grant` is permitted for a class that must have no provider-account binding

**Severity:** P2 (material non-blocking observation; fail-closed behavior
remains deterministic).

**Locations:** Registry §13.2 row 9; Registry §12; Cloudflare §11.1.1 row 4;
Cloudflare §25.1.

**Statement.** `restricted_operator_investigation` permits
`mcp_oauth_grant` as one of its two authentication modes, while the same row
and its Cloudflare projection require "no provider account access" and an
"empty account/resource binding". An OAuth grant to a provider-operated MCP
server is, by construction, a grant against a provider account. The documents
do not explain how an `mcp_oauth_grant` can exist with an empty
provider-account binding, nor how that emptiness would be verified.

**Why this is not blocking.** Every consequence is denied independently of the
mode: provider API authority is **None**, mutation authority is **None**, any
account binding denies and audits, and Cloudflare v1.0 selects the
documentation-only path with "no account grant". Fail-closed behavior therefore
remains deterministic. The observation should be resolved before any MCP phase
advance under Gateway §21.3.

### `P3-301` — the `CF_READ` identity selector is never bound to a named field

**Severity:** P3 (editorial; implementation behavior unaffected).

Registry §13.2 and Cloudflare §11.1.1 row 1 both make the `CF_READ` projection
depend on "the declared acting-identity mode", but no document names the record
field that carries it. Registry §14.1 field (12) `required_identity_type` is
the only candidate, and any missing or ambiguous value denies under §14.2
rule 8, so behavior is unaffected.

### `P3-302` — identity-type token vocabulary is not canonically enumerated

**Severity:** P3 (editorial; implementation behavior unaffected).

Registry §13.1 requires `identity_type` to be "One of the seven ADR §11
identity types", but no document enumerates canonical tokens for those seven.
The catalogue uses `delegated_end_user`, `service_account`,
`provider_credential`, and now `mellycore_operator`, which appears exactly once
in the entire repository. Gateway §8.1 independently defines a twelve-identity
table with different labels. The mapping is derivable, and no behavior depends
on the token spelling today, but the absence of one canonical list is what
allowed `P1-301` to pass unnoticed through the remediation.

The Cybersecurity Pack §12 class table listing seven of nine canonical classes
without a "non-exhaustive projection" caveat is recorded here as a related
editorial observation rather than as a separate finding, since Registry §13.2
is the declared sole owner and Gateway §14.2 accepts only Registry identifiers.

## 30. Finding counts

| Severity | Count | IDs |
| --- | --- | --- |
| P0 | **0** | — |
| P1 | **2** | `P1-301`, `P1-302` |
| P2 | **1** | `P2-301` |
| P3 | **2** | `P3-301`, `P3-302` |

`P1-201` result: **`PARTIALLY_CLOSED`** (4 of 6 sub-defects verified closed).

No previously closed Review 001 or Review 002 finding was found reopened. No
capability, prohibition, risk-tier, approval, audit, verification, containment,
or external-content regression was found.

## 31. Gate decision

**`FAIL_REMEDIATION_REQUIRED`.**

The decision follows mechanically from the criteria:

- `PASS` requires P1 = 0 and `P1-201` independently verified `CLOSED`. Neither
  holds.
- `PASS_WITH_NON_BLOCKING_FINDINGS` requires P1 = 0 and `P1-201` fully closed.
  Neither holds.
- `FAIL_REMEDIATION_REQUIRED` applies when any P1 exists, when `P1-201` is only
  partially closed, or when runtime implementation would still require
  architectural interpretation. All three conditions are met.

The failure is a conformance and expressibility failure, not a safety failure.
Both P1 findings deny rather than permit. No documentation-only class can reach
a provider account, no class can authorize a provider API call or a mutation
without the full eight facts, no cross-tenant reuse is possible, no
consequential operation can bypass approval, audit, or authorization, and no
provider-local label acts as an independent authorization identity.

## 32. Adapter-scaffold eligibility

`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` **remains blocked and ineligible.**
It is not started, not authorized, and not eligible for authorization. This
review does not change its state in any direction.

## 33. Exact next task

`MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001`

Derived from the actual defect: make the operator-bound restricted
documentation/investigation path expressible end to end, by reconciling the
Integration Gateway's acting-identity model (§9.2, Rule 16.7, §17 step 13, §23)
and the Provider Registry's provider-record scope model (§26.1 against §11.2
rule 2) with the ninth canonical class, without weakening any fail-closed
default and without granting the class any provider account, provider API, or
mutation authority. `P2-301`, `P3-301`, and `P3-302` should be routed by the
same task.

A further independent review must follow that remediation before scaffold
eligibility is reconsidered.

## 34. Explicit non-authorizations

This review authorizes none of the following, and none occurred: Adapter
Scaffold implementation or scaffolding; Registry, Gateway, or adapter
implementation; provider registration as a runtime grant; provider
authentication; credential creation, storage, rotation, reading, or
verification; any provider API call, including read-only calls; any MCP or
integration-fabric connection; webhook endpoint creation or registration; any
change to any external system; any dependency, lockfile, or workflow change;
deployment, push, pull request, merge, tag, or remote branch; or any
MellyTrade, broker, trading, or order-execution behavior.

No provider is connected, authenticated, credentialed, enabled, live, deployed,
or implemented. No credential exists in this repository or its environment.

## 35. Validation evidence

| Command | Result |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` | `PASS MellyCore project scaffold validation passed`, exit code `0` |
| `git diff --check` | No output, exit code `0` |
| `git status --short` | Reported in the Review 003 task report |
| `git diff --name-only` | Reported in the Review 003 task report |
| `git diff --stat` | Reported in the Review 003 task report |
| `pytest` | `NOT_RUN` — not required for a documentation-only review; no dependency was installed |

| Metric | Value |
| --- | --- |
| Review 003 record sections | 37 |
| Reviewed documents | 17 (plus `SAFETY_CONTRACT.md` and `VALIDATION.md`) |
| Canonical credential-profile classes | 9 |
| Cloudflare projection rows | 5 |
| Deterministic scenarios replayed | 16 |
| Findings: P0 / P1 / P2 / P3 | 0 / 2 / 1 / 2 |
| Introduced secret patterns | 0 |
| Changed files in this commit | 6 |

No unavailable or unrun validator is represented as passing.

## 36. Amendment and supersession

This record is append-only evidence of one independent review at one commit. It
may be superseded only by a later, explicitly identified review record that
references this file **by path** and states which sections it changes. A later
document that silently contradicts this record does not supersede it; such a
contradiction must be corrected.

This record amends no ADR, contract, provider pack, remediation report, or
earlier review record. Review 001 and Review 002 remain immutable historical
evidence.

## 37. References

### 37.1 Repository (canonical)

- `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`
- `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md`
- `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003.md`
- `shared_context/SAFETY_CONTRACT.md`, `shared_context/VALIDATION.md`,
  `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`

### 37.2 External

None. No external documentation was fetched, no provider was contacted, and no
network call other than a read-only `git fetch clean-origin` was made during
this review.
