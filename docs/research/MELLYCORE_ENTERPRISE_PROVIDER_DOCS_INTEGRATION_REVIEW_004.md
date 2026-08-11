# MellyCore Enterprise Provider Docs Integration Review 004

## 1. Title and status

**Task ID:** `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004`

**Record ID:** `MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_004`

**Review date:** 2026-08-03

**Status:** Complete. Independent post-remediation documentation-gate review.

**Gate decision:** `PASS_WITH_NON_BLOCKING_FINDINGS`.

**Finding counts:** P0 = 0, P1 = 0, P2 = 0, P3 = 3.

**Review 003 closure results:** `P1-301` `CLOSED`; `P1-302` `CLOSED`;
`P2-301` `CLOSED`; `P3-301` `CLOSED`; `P3-302` `CLOSED`.

This record is documentation evidence only. It authorizes no implementation,
no provider authentication, no provider API call, no MCP or integration-fabric
connection, no webhook registration, no credential, and no deployment. A gate
pass is not an execution authorization.

## 2. Purpose

Independently verify whether commit `b90ce82ab497469ea3c8b8c0f3c8be8ce8717dbd`
(`docs: align restricted operator tool path`) fully closes the five Review 003
findings — `P1-301`, `P1-302`, `P2-301`, `P3-301`, `P3-302` — across ten
dimensions: canonical acting-identity representation, `mellycore_operator`
Gateway support, capability-level scope applicability, D4 provider-native
`not_applicable` semantics, exact restricted-tool scope, authentication-target
ownership, `mcp_oauth_grant` target isolation, the canonical
`required_acting_identity_type` selector, canonical acting-identity vocabulary,
and all related restricted-tool-path regressions.

The reviewer did not author the remediation. Every remediation claim was
treated as unverified until confirmed directly from canonical repository
evidence. The remediation report's own restatement of a finding was never used
as the authoritative definition of that finding; the definitions were
reconstructed from the immutable Review 003 record.

## 3. Scope

**In scope.** Repository identity and history verification; read-only
`clean-origin` fetch; complete inspection of the `b90ce82…` diff against parent
`699f1d39…`; complete reads of the four amended canonical contracts, the
governing ADR's identity and capability sections, the Review 003 record and
task report, the restricted-tool-path remediation report, and the four
shared-context files plus `SAFETY_CONTRACT.md` and `VALIDATION.md`; mechanical
counting of every structural quantity; independent verification of all five
Review 003 findings; twenty-four-scenario deterministic replay; repository-wide
regression search for residual and competing identity, scope, target, and field
vocabularies; read-only documentation validators; and creation of exactly one
local documentation commit containing this record, the Review 004 task report,
and bounded shared-context updates.

**Out of scope, and not performed.** Any modification of a reviewed ADR,
contract, provider pack, remediation report, or earlier review record; any
repair of a finding; any source-code change; any Adapter Scaffold work; any
provider authentication or API execution; any MCP or integration-fabric
connection; any webhook registration; any credential, secret, or `.env`
handling; any dependency, lockfile, or workflow change; and any push, pull
request, merge, tag, remote branch, deployment, or MellyTrade interaction.

## 4. Starting repository state

| Dimension | Observed |
| --- | --- |
| Repository path | `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios` |
| Resolved root | `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` |
| Starting branch | `docs/mellycore-enterprise-provider-restricted-tool-path-conformance-remediation-001` |
| Starting HEAD | `b90ce82ab497469ea3c8b8c0f3c8be8ce8717dbd` |
| HEAD subject | `docs: align restricted operator tool path` |
| HEAD parent | `699f1d39b011b6afe5ba82d4c2bd8f5639c5de59` |
| Worktree / index | Clean (`git status --short --branch` reported only the branch line) |
| Canonical remote | `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git` |
| `clean-origin/main` after fetch | `947f33d27d5546775186e96bdc61e30db78c0b3d` — unchanged, no drift |
| Review 004 branch before this task | Absent locally and on `clean-origin` |
| Review branch created | `docs/mellycore-enterprise-provider-docs-integration-review-004`, from `b90ce82…`, not from `clean-origin/main` |

`origin` (`https://github.com/Melly-999/mellycore-aios.git`) exists in the
remote list and was **not** contacted.

## 5. Reviewed commits

| Commit | Role | Verified |
| --- | --- | --- |
| `8a5c4ebf16485d6e7508b811c4ccdd8032dfdcb2` | Review 001 (`FAIL_REMEDIATION_REQUIRED`; P0 0, P1 4, P2 2, P3 3) | Referenced; record unchanged |
| `95b5b03defcfa9530f7e2625f12648aa8eac918c` | Review 002 (`FAIL_REMEDIATION_REQUIRED`; sole blocker `P1-201`) | Referenced; record unchanged |
| `8e1f7289345eb556d6b1972cac61c0aa9a950c89` | Credential-class conformance remediation | Referenced; report unchanged |
| `699f1d39b011b6afe5ba82d4c2bd8f5639c5de59` | Review 003 (`FAIL_REMEDIATION_REQUIRED`; P0 0, P1 2, P2 1, P3 2) | Parent of the remediation commit; confirmed |
| `b90ce82ab497469ea3c8b8c0f3c8be8ce8717dbd` | Restricted-tool-path conformance remediation under review | Confirmed: expected parent, expected subject, exactly nine changed paths |

Remediation commit changed paths (nine, as reported):

1. `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
2. `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
3. `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
4. `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
5. `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001.md`
6. `shared_context/AGENT_HANDOFF.md`
7. `shared_context/PROJECT_STATE.md`
8. `shared_context/ROADMAP.md`
9. `shared_context/RUN_QUEUE.md`

No Review 001, Review 002, or Review 003 record or task report, no prior
remediation report, no ADR, no Marketing Pack, and no Fabric Comparison spec
appears in that path set. Diffstat: 790 insertions, 163 deletions.

## 6. Reviewed documents

| # | Document | Depth |
| --- | --- | --- |
| 1 | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | Complete for §§7.5, 11, 12, 12.1, 13, 14, 21, 24, 26, 27; full diff; structural sweep elsewhere |
| 2 | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | Complete for §§8.2, 9, 13, 14, 15, 16, 17, 21, 23, 29, 32, 34; full diff; structural sweep elsewhere |
| 3 | `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md` | Complete for §§9, 10, 11, 13, 25, 31; full diff; mechanical row extraction across all capability and prohibition tables |
| 4 | `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md` | Complete for §§7, 11, 12, 21, 32; full diff; provider and ceiling extraction |
| 5 | `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | §§11–13 complete; identity-term search |
| 6 | `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` | Baseline hash and authority reference only; unchanged |
| 7 | `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md` | Complete (all 37 sections), as the authoritative finding source |
| 8 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003.md` | Complete |
| 9 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001.md` | Complete |
| 10 | `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md` | Baseline hash; identity-lineage reference |
| 11 | `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md` | Baseline hash; `P1-201` lineage reference |
| 12 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md` | Baseline hash only; unchanged |
| 13 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md` | Baseline hash only; unchanged |
| 14 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md` | Baseline hash only; unchanged |
| 15 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md` | Baseline hash only; unchanged |
| 16 | `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md` | Baseline hash only; unchanged |
| 17 | `shared_context/PROJECT_STATE.md` | Enterprise-provider region complete |
| 18 | `shared_context/ROADMAP.md` | Enterprise-provider sequence complete |
| 19 | `shared_context/RUN_QUEUE.md` | Enterprise-provider queue complete |
| 20 | `shared_context/AGENT_HANDOFF.md` | Latest and previous update blocks complete |

`shared_context/SAFETY_CONTRACT.md` and `shared_context/VALIDATION.md` were
read in full as governing authorities.

## 7. Independent method

1. Repository, branch, HEAD, parent, subject, remote, and worktree gate.
2. Read-only `clean-origin` fetch and canonical-main drift check.
3. Blob-ID baselines captured for every reviewed document and the four
   shared-context files before branch creation and before any edit.
4. Review branch created from the remediation commit, not from canonical main.
5. Review 003 finding definitions reconstructed from the immutable Review 003
   record (§29 and §11), never from the remediation report's restatement.
6. Full diff of `b90ce82…` inspected hunk by hunk against its parent, with the
   pre-remediation text of every affected region retrieved from `699f1d39…`.
7. Contract text read directly. Remediation prose and task-report claims were
   never accepted as evidence for the fact they assert.
8. Counting checks executed mechanically — canonical acting-identity rows,
   authentication-target rows, credential-profile-class rows, capability rows,
   prohibition rows, D4 rows — by regex extraction on the actual section line
   ranges, with false positives from adjacent tables eliminated by boundary
   inspection.
9. Cloudflare capability- and prohibition-row integrity proved by extracting
   all 71 rows at both commits and comparing SHA-256 digests.
10. Twenty-four deterministic scenarios replayed against contract text, each
    resolved to one outcome and exact source sections, or marked as requiring
    architectural interpretation.
11. Repository-wide searches for retired tokens (`required_identity_type`,
    `required_provider_scope`, `required_scope_dimensions`,
    `delegated_end_user`, two-value `acting_identity_type`), for stale numeric
    field cross-references after the §14.1 renumbering, for malformed tables
    introduced by the remediation, and for the global task pointer.
12. Read-only validators executed and reported truthfully.

## 8. Immutable baselines

Recorded at HEAD `b90ce82…` before branch creation and before any edit. These
are re-verified after the Review 004 commit.

| Path | Git blob ID |
| --- | --- |
| `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | `fa90b65b4f91545550247d81fc181eb10cca942a` |
| `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | `65192fa157b57a2a46768ceca4660aed1584f649` |
| `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md` | `9a318a1a25a08a6ca1ebdc53802fb286b3b4a5c9` |
| `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md` | `9901b075d53f530d98cd4daeef30f3c7a0527611` |
| `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md` | `5febae25d2fb315072a35cbe556d02c709308f59` |
| `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | `0d2768be8d9ae19b5a14ce1c61441550081113e3` |
| `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md` | `5ae4f4695746e28df73fd9da17ff9017a2102fb0` |
| `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md` | `09804c6184195c25c2754ea201c5282cb96c1ea3` |
| `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md` | `756c5ccb234e939b45f59370bec60d7cf9bc7876` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md` | `8d768fb9a89055e13193f1f2879c1917e6e7283f` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md` | `45685cacd2d64f1f8d96627ff4df28b086de6e7a` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003.md` | `9a116c83891166a41aa2836162a6be0755b41ad9` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md` | `07916d0c444ad6455e8d2f632444cc4e5decb0af` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md` | `d99129e8ebc1f004dc34dde078a8ef23e6070088` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md` | `23a1769ddae9511a52ec569f3eb648f0481a48b5` |
| `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001.md` | `e7a81bdc87312c6276cf79d52205b271fc4a1ebd` |
| `shared_context/SAFETY_CONTRACT.md` | `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` |
| `shared_context/VALIDATION.md` | `a4acf641d3cc1551ad1513bcc8ec0cc619be941b` |

The Review 001 and Review 002 record and report blob IDs, and the three prior
remediation-report blob IDs, are **identical to the values Review 003 recorded
at commit `8e1f728…`**. This independently confirms that neither the
credential-class remediation nor the restricted-tool-path remediation touched
any historical evidence.

Shared-context blob IDs before this review's edits (these four are expected to
change, and only these four):

| Path | Git blob ID at `b90ce82…` |
| --- | --- |
| `shared_context/PROJECT_STATE.md` | `ca34cbe4c7541147093ec2a2902429e36727998b` |
| `shared_context/ROADMAP.md` | `3136a20f6d89d8038f0b959fbd2ea84e33848625` |
| `shared_context/RUN_QUEUE.md` | `22bb565aaa3d2289eb10a1eeb14f876962da814f` |
| `shared_context/AGENT_HANDOFF.md` | `70ed0952d8a29bc6edb8a86ae6104c1358d281a8` |

Structural baselines, measured mechanically at `b90ce82…`:

| Quantity | Value | Method |
| --- | --- | --- |
| Canonical acting-identity types (Registry §7.5) | 3 | Row extraction, lines 204–224, header excluded |
| Canonical authentication targets (Registry §12.1) | 3 | Row extraction, lines 438–462, header excluded |
| Canonical credential-profile classes (Registry §13.2) | 9 | Row extraction, lines 488–540, header excluded |
| Scope-applicability values (Registry §11.2) | 3 (`required`, `optional`, `not_applicable`) | Enumerated in rule 2 |
| Cloudflare capability rows | 58 (D1 16, D2 16, D3 23, D4 3) | Regex row count |
| Cloudflare prohibition rows | 13 (`P-01`…`P-13`) | Regex row count |
| D4 capabilities | 3 (`D4-01`, `D4-02`, `D4-03`), all R0 | §13.4.1 row count |
| Cloudflare 71-row content digest | `759d4250007946ee4456537ae74cbce54051186592617bcd75b16ebc9a592a41` at **both** `699f1d39…` and `b90ce82…` | SHA-256 over the extracted, ordered row set |

## 9. Review 003 finding baseline

Reconstructed from the immutable Review 003 record, §29 and §11, without
reference to the remediation report:

- **`P1-301`** (P1). Locations: Gateway §9.2, Rule 16.7, §17 step 13, §23
  envelope, §14.2, §34.6, §34.7; Registry §13.2 row 9. Contradiction: Registry
  §13.2 defines `restricted_operator_investigation` with `identity_type:
  mellycore_operator`, while the Gateway's acting identity is a closed
  two-value set (`delegated_user` | `service_account`) everywhere it is
  defined, so a D4 request has no resolvable acting identity. An implementer
  had to choose between "every D4 request denies" and "add a third value",
  which is architectural interpretation.
- **`P1-302`** (P1). Locations: Registry §26.1 `required_scope_dimensions`;
  Registry §11.2 rule 2; Cloudflare §11.2 rule 2; Cloudflare §11.1.1 row 4;
  Gateway §14.2. Contradiction: the Cloudflare provider record declared
  `required_scope_dimensions: tenant, account, zone` and a missing required
  dimension fails closed, while D4 was required to have an empty account, zone,
  and resource binding. A D4 invocation therefore had to both have and not have
  an account and zone.
- **`P2-301`** (P2). Locations: Registry §13.2 row 9; Registry §12; Cloudflare
  §11.1.1 row 4; Cloudflare §25.1. Contradiction: `mcp_oauth_grant` was a
  permitted mode for a class that must have no provider-account binding, and no
  document explained how a tool OAuth grant differs from a provider-account
  grant or how the emptiness would be verified.
- **`P3-301`** (P3). The `CF_READ` projection depended on "the declared
  acting-identity mode", but no document named the record field carrying it.
- **`P3-302`** (P3). Registry §13.1 required `identity_type` to be "one of the
  seven ADR §11 identity types" while no canonical token list existed;
  `mellycore_operator` appeared exactly once in the repository, and Gateway
  §8.1 independently defined a twelve-identity table with different labels.

## 10. Remediation assessment

The remediation is architecturally coherent and, on the evidence below,
sufficient. Verified directly from the contract text rather than from its
report:

- Registry gains **§7.5**, declared sole normative owner of the reusable
  `acting_identity_type` vocabulary, with exactly three rows and nine
  per-row dimensions including provider-account eligibility, provider-API
  eligibility, restricted-tool eligibility, compatible credential-profile
  classes, substitution prohibition, and audit actor representation.
- Registry gains **§12.1**, declared sole normative owner of the
  authentication-target vocabulary, separating `authentication_mode` (how) from
  `authentication_target` (what authority), with three closed values and an
  explicit rule that "a mode name containing `oauth` or `mcp` never implies a
  provider-account target".
- Registry **§11.1/§11.2** replace the provider-wide
  `required_scope_dimensions` model with three scope domains (MellyCore always
  required; provider-native as applicable; restricted-tool when the target is a
  restricted tool) and a capability-level `required` / `optional` /
  `not_applicable` applicability model governed by four new rules (7–10).
- Registry **§13.1** replaces the single `identity_type` field with
  `credential_subject_type` plus `compatible_acting_identity_types`, and adds
  `authentication_target`. **§13.2** renames identity tokens to the canonical
  set and adds a closed target-compatibility paragraph.
- Registry **§14.1** renumbers to 28 fields, introducing (12)
  `required_acting_identity_type`, (14) `required_authentication_target`, and
  (15) `scope_applicability`; **§14.2** adds rules 9 and 10.
- Registry **§24.1** expands the restricted-tool/MCP record to require a stable
  `restricted_tool_id`, `tool_contract_revision`, environment, authentication
  target, credential class, exact `allowed_capability_ids`,
  `eligible_acting_identity_types`, data sensitivity, allowed resource classes,
  external-content posture, audit source, retention, and session-metadata
  policy, with an explicit non-executability rule for discovered tools.
- Registry **§26.1** replaces `required_scope_dimensions` with
  `possible_provider_native_scope_dimensions`, `provider_api_scope_defaults`,
  and an explicit D4 scope rule.
- Gateway **§8.2** subordinates its twelve-identity provenance table to
  Registry §7.5 and forbids a second acting-identity enum; **§9.1/§9.2**
  replace the two-value chain element with `required_acting_identity_type`,
  `acting_identity_ref`, and `required_authentication_target`; **§9.3** adds
  rule 7; **Rule 16.7** becomes three-value exclusivity; **§17 step 13**
  resolves and freezes the selector; **§23** carries the canonical fields and
  gains **Rule 23.3** immutability; **§13.1/§13.2** adopt the applicability
  model with rules 8–10; **§21.1/§21.2** adopt the expanded registration and
  add rules 10–11; **§29.1** adds the canonical audit-actor requirement;
  **§34.6** is rewritten with four new binding rows.
- Cloudflare **Rule 9.4** permits `not_applicable` for `account`, `zone`, and
  `resource` **only on D4**; **Rule 10.2** bars operator identity from D1–D3;
  **§11.1/§11.1.1/§11.2** bind targets and applicability; **§13.0** makes the
  four canonical fields the sole Gateway resolution inputs; **§13.1.0–§13.4.0**
  declare targets and applicability per domain; **§25.2** expands from eleven to
  sixteen conditions; **§31.3/§31.4** expand the audit records.
- The Cybersecurity Pack **§7 rule 6**, **§11**, **§12**, **§21**, and **§32**
  reference the Registry-owned vocabularies, declare the pack class table
  non-exhaustive, and replace the Review 003 prerequisite with a required
  future Review 004 `PASS`.

Three residual editorial defects were found. All are P3, none affects
implementation behavior, and none blocks the gate. They are recorded in
Section 33.

## 11. Review 003 closure matrix

| Finding | Original severity | Original affected documents / sections | Original contradiction | Remediation sections | Dependent references checked | Independent scenario evidence | Result | Review 004 severity | Gate impact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `P1-301` | P1 | Gateway §9.2, Rule 16.7, §17 step 13, §23, §14.2, §34.6, §34.7; Registry §13.2 row 9 | Registry declared `identity_type: mellycore_operator` for the ninth class while the Gateway's acting identity was a closed two-value set, so no D4 request had a resolvable acting identity; an implementer had to choose between two unadjudicated readings | Registry §7.5 (new); Gateway §8.2, §9.1, §9.2, §9.3 rule 7, §14.2, §15.6, §16.6, Rule 16.7, §17 step 13, §23 + Rule 23.3, §29.1, §34.6, §34.7; Cloudflare §10 preamble, Rule 10.2, §13.4.0; Pack §11 | Repository sweep confirms no surviving two-value acting-identity enum: the retired `required_identity_type`, `delegated_end_user`, and two-value `acting_identity_type` tokens appear **only** in immutable Review 002/003 records. The single surviving "delegated-user or service-account" phrase (Cloudflare §11.1.1 row 2) correctly scopes `controlled_write`. ADR §11 item 1 is already "MellyCore operator identity", so §7.5 canonicalizes an existing ADR type rather than inventing one | Scenarios 3, 4, 5, 6, 7, 19 (Section 30). Scenario 7 — the Review 003 `INDETERMINATE` case — now resolves deterministically to contract-resolvable, then `RUNTIME_NOT_ENABLED` / `ADAPTER_UNAVAILABLE`. Scenario 19 denies on Registry §7.5 provider-API ineligibility plus Cloudflare Rule 10.2 | **`CLOSED`** | — | Blocker removed |
| `P1-302` | P1 | Registry §26.1, §11.2 rule 2; Cloudflare §11.2 rule 2, §11.1.1 row 4; Gateway §14.2 | Provider-wide `required_scope_dimensions: tenant, account, zone` combined with fail-closed-on-missing-dimension contradicted D4's mandatory empty account/zone/resource binding | Registry §11.1, §11.2 rules 2 and 7–10, §14.1 field (15), §14.2 rules 4 and 10, §26.1; Gateway §13.1, §13.2 rules 8–10, §14.2; Cloudflare §9.1 rules 2–3, Rule 9.4, §11.2 rule 2, §13.1.0–§13.4.0 | `required_scope_dimensions` now appears **only** in immutable review records and shared-context history, never in a live contract rule. `tenant` moved from the provider-native list into the always-required MellyCore set (§11.1, §11.2 rule 1), so tenant scope is strengthened, not relaxed. `environment` likewise moved to always-required | Scenarios 11, 12, 13 (Section 30). Missing applicability denies; explicit `not_applicable` resolves; a supplied provider-native value denies and audits | **`CLOSED`** | — | Blocker removed |
| `P2-301` | P2 | Registry §13.2 row 9, §12; Cloudflare §11.1.1 row 4, §25.1 | `mcp_oauth_grant` was permitted for a class requiring no provider-account binding, with no stated distinction between a tool OAuth grant and a provider-account grant | Registry §12.1 (new, including the dedicated `mcp_oauth_grant` paragraph), §13.1 `authentication_target` field, §13.2 target-compatibility paragraph; Gateway §9.2, §14.2, §21.2 rule 10, §23; Cloudflare §11.1 target paragraph, §13.4.0, §25.2 item 6; Pack §12 | Mode and target are now independent fields with independent closed vocabularies. Target compatibility is closed per class: `restricted_operator_investigation` **requires** `restricted_tool`. No document treats mode and target as the same concept | Scenarios 17, 18 (Section 30). A tool-targeted grant resolves at contract level; a provider-account-targeted grant denies before credential material is resolved | **`CLOSED`** | — | None |
| `P3-301` | P3 | Registry §13.2, §14.1 field (12); Cloudflare §11.1.1 row 1 | The `CF_READ` identity selector was never bound to a named record field | Registry §14.1 field (12) `required_acting_identity_type`, §13.2 concrete binding rule, §14.2 rule 9, §26.2; Gateway §9.2, §14.2, §15.6, §16.6, §17 step 13, §23, Rule 23.3, §34 preamble, §34.1, §34.2; Cloudflare §11.1.1 row 1, §13.0, §13.1.0, §13.2.0 | The field is named identically in all four contracts. Cloudflare §11.1.1 row 1 now states the mapping explicitly: `delegated_user` selects `read_only_delegated`; `service_account` selects `read_only_service` | Scenarios 1, 2, 3, 4 (Section 30) | **`CLOSED`** | — | None |
| `P3-302` | P3 | Registry §13.1, §13.2; Gateway §8.1; ADR §11 | No canonical identity-token vocabulary existed; `mellycore_operator` appeared exactly once in the repository | Registry §7.5; Gateway §8.2 preamble; Cloudflare §10 preamble; Pack §11 | Registry §13.1's "one of the seven ADR §11 identity types" phrasing is gone. Gateway §8.2 explicitly states its twelve identities "do not create a second acting-identity enum". Cloudflare §10 and Pack §11 defer to §7.5. §7.5 maps the ADR's human-readable concepts to the canonical tokens | Scenario coverage throughout Section 30; every scenario cites one canonical token | **`CLOSED`** | — | None |

No finding is partially closed. No finding was reopened. No regression was
introduced into a previously closed Review 001, Review 002, or `P1-201`
sub-defect.

## 12. Canonical ownership review

**Result: PASS.** Ownership is single-sourced and non-competing.

| Concern | Sole normative owner | Enforcer | Verified statement |
| --- | --- | --- | --- |
| Acting-identity vocabulary | Registry §7.5 | Gateway §8.2, Rule 16.7, §9.3 rule 7 | "This Registry contract is the sole normative owner of the reusable `acting_identity_type` vocabulary" |
| Authentication targets | Registry §12.1 | Gateway §9.2, §14.2, §21.2 rule 10 | Three closed values; "A mode name containing `oauth` or `mcp` never implies a provider-account target" |
| Scope applicability | Registry §11 | Gateway §13.2 rules 8–10 | "Registry §11 owns the generic `required` / `optional` / `not_applicable` model" (Cloudflare Rule 9.4) |
| Credential-profile class catalogue | Registry §13.2 | Gateway §14.2 | Nine identifiers; a provider contract "may not invent another class" |
| Which provider-native dimensions apply per Cloudflare capability | Cloudflare §9.1, Rule 9.4, §13.1.0–§13.4.0 | Gateway §13.2 | "Cloudflare permits `not_applicable` … only on D4" |
| Restricted-tool registration shape | Registry §24.1 | Gateway §21.1, §21.2 rules 6, 7, 11 | "A discovered tool is never executable until this exact record … match" |
| Runtime resolution and fail-closed evaluation | Gateway §14.2, §17 | Gateway | "Zero or multiple matches deny" |
| Pack references | Pack §11, §12 | — | "creates no second enum"; "non-exhaustive pack projection" |

No second catalogue, no competing enum, and no provider-local token acting as
an independent authorization identity was found. References in the Gateway,
Cloudflare contract, and Pack constrain the vocabulary but do not redefine it
incompatibly. Precedence remains identical in Registry §25.2 and Gateway §33.

## 13. Acting-identity vocabulary review

**Result: PASS.** Registry §7.5 defines exactly three canonical identifiers,
each carrying all eight required dimensions.

| Identifier | Human? | Delegation | Provider-account eligible | Provider API eligible | Restricted-tool eligible | Compatible classes | Substitution rule | Audit representation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `delegated_user` | Yes | Provider-side grant held by the exact end user | Yes, only within the exact grant | Yes, only for an explicitly compatible capability | No | `read_only_delegated`; identity-compatible `controlled_write`; identity-compatible fabric classes | Never substitute a service account or operator | Exact delegated-subject reference, labelled `delegated_user` |
| `service_account` | No | None implied; acts only under explicit tenant policy | Yes, within its explicit allowlist | Yes, only for an explicitly compatible capability | No | `read_only_service`; identity-compatible `controlled_write`; identity-compatible fabric classes; `emergency_containment`; `reporting_only` | Never present as a human, delegated user, or operator | Exact service-account reference, conspicuously labelled |
| `mellycore_operator` | Yes | Authenticated MellyCore human operator; no provider-side delegation, provider-user identity, or provider-account identity implied | **No** | **No** | Yes, only for an explicitly operator-bound capability and registered restricted tool | `restricted_operator_investigation` **only** | Never substitute a service account, delegated user, agent, session, or credential | Exact MellyCore operator reference, labelled `mellycore_operator`; provider-native actor is `not_applicable` |

- Exactly three rows; identifiers unique; no near-synonym; no fourth value
  anywhere in the chain.
- The closing paragraph forbids downstream contracts from creating a competing
  token, silently translating one acting identity into another, or treating
  `mellycore_operator` as a universal third fallback.
- The ADR mapping is explicit and consistent with ADR §11, whose item 1 is
  already "MellyCore operator identity". `mellycore_operator` is therefore the
  canonical token for an existing ADR type, not a new identity.
- The `event_verification` class, which has no execution actor, is handled by
  an explicit `not_applicable` on the profile's
  `compatible_acting_identity_types` field rather than by a fourth identity
  token. Because Gateway §9.2 requires exactly one §7.5 value on every request
  and the class carries "no outbound capability", this cannot become an
  identity bypass.

One editorial defect affects this section's table rendering only; see
`P3-401` in Section 33.

## 14. `mellycore_operator` review

**Result: PASS.**

| Required property | Evidence | Verified |
| --- | --- | --- |
| MellyCore-authenticated human operator | Registry §7.5 ("Human? Yes"; "Authenticated MellyCore human operator") | Yes |
| Tenant-bound | Registry §11.2 rule 1, rule 10; §24.1 `tenant_binding`; Gateway §13.2; Cloudflare §25.2 items 2, 5 | Yes |
| Operator-bound | Registry §7.5 audit column; §11.2 rule 10 ("Missing exact … operator … denies"); Cloudflare §13.4.0, §25.2 item 4 | Yes |
| Non-provider-account | Registry §7.5 ("Provider-account eligible: **No**"); §13.2; Cloudflare §11.1.1 row 4; Gateway §14.2 | Yes |
| Non-provider-API | Registry §7.5 ("Provider API eligible: **No**"); Cloudflare §11.1.1 row 4 "Provider API authority: **None**"; Rule 10.2 | Yes |
| Non-delegated-provider-user | Registry §7.5 ("no provider-side delegation, provider-user identity, or provider-account identity is implied") | Yes |
| Non-service-account | Registry §7.5 substitution rule; Cloudflare §11.1.1 row 4 "no service-account fallback"; Gateway Rule 16.7 | Yes |
| Non-fallback | Gateway Rule 16.7 ("never selected as fallback"); §9.3 rule 7 ("It is never a fallback"); Registry §7.5 ("never … a universal third fallback"); Pack §11 | Yes |
| Eligible only for explicitly compatible capabilities | Gateway §9.3 rule 7; Rule 16.7; Cloudflare Rule 10.2 ("valid only for D4"); Registry §7.5 | Yes |
| Eligible only for explicitly compatible credential classes | Registry §7.5 ("`restricted_operator_investigation` only"); §13.2 target-compatibility paragraph | Yes |
| Auditable as the exact human actor | Gateway §29.1 ("the audit actor is the authenticated MellyCore human operator; no service account, agent, credential, session, or tool may replace it"); Cloudflare §31.3, §31.4 | Yes |

The Gateway does **not** admit `mellycore_operator` for normal provider API
reads or writes. Registry §7.5 sets provider-API eligibility to **No**
unconditionally — stricter than the gate criterion, which would have allowed a
future provider-specific carve-out. Cloudflare Rule 10.2 states it "can never
be substituted into D1–D3". For current Cloudflare D4, provider API access
remains prohibited by Cloudflare §11.1.1 row 4, §13.4.0, and prohibitions
`P-01`/`P-02`.

## 15. Acting-identity selector review

**Result: PASS.** The canonical selector discovered in the repository is
`required_acting_identity_type`, matching the field name the task anticipated.

| Requirement | Evidence | Verified |
| --- | --- | --- |
| Appears in concrete capability registration | Registry §14.1 field (12) | Yes |
| Binds before credential resolution | Gateway §17 step 13 precedes step 14; Rule 23.3 ("bind before credential resolution"); Registry §13.2 concrete binding rule | Yes |
| Appears in the Gateway request/evaluation envelope | Gateway §9.2 chain field; §23 envelope field | Yes |
| Immutable for one evaluation | Gateway §9.2 ("immutable for one evaluation"); Rule 23.3; §17 step 13 ("resolve and freeze") | Yes |
| Matches the credential class | Registry §14.2 rule 9; §7.5 compatible-class column; Gateway §14.2 | Yes |
| Matches standing authorization where applicable | Registry §13.2 ("The authorization records bind to that selected class"); §21.3–21.5 | Yes |
| Denies when missing | Gateway §9.2; §17 step 13 `IDENTITY_UNRESOLVED`; Registry §14.2 rule 9; Cloudflare §11.1.1 row 1 | Yes |
| Denies when unknown | Gateway §9.2, Rule 16.7, Rule 23.3 | Yes |
| Denies when conflicting | Gateway Rule 16.7 ("Zero, multiple, unknown, or conflicting types deny") | Yes |
| Included in audit evidence | Gateway §29.1; §23; Cloudflare §31.3, §31.4 | Yes |

`CF_READ` resolution is now fully deterministic and never dynamic: Cloudflare
§11.1.1 row 1 states `delegated_user` selects `read_only_delegated` and
`service_account` selects `read_only_service`, stored as
`required_credential_profile_class` before runtime. Gateway §14.2 retains "the
Gateway never interprets a pack-local alias or chooses among authentication
modes", and Registry §13.2 retains "The Gateway never chooses between classes,
identity modes, or authentication modes".

## 16. Authentication-target review

**Result: PASS.** Registry §12.1 owns exactly three targets.

| Target | Valid credential classes | Valid identity types | Valid scope families | Provider-access implication | Mismatch behavior |
| --- | --- | --- | --- | --- | --- |
| `provider_account` | `read_only_delegated`, `read_only_service`, `controlled_write`, `event_verification`, `emergency_containment`, `reporting_only` | `delegated_user`, `service_account` (and `not_applicable` for inbound-only `event_verification`) | MellyCore + applicable provider-native | Provider-native account/API authority governed by the provider contract | Deny before credential material is resolved (§12.1; Gateway §9.2) |
| `restricted_tool` | `restricted_operator_investigation` only | `mellycore_operator` only | MellyCore + restricted-tool; provider-native explicitly `not_applicable` | "grants no provider-account or provider-API authority" | Deny and audit (§12.1; Cloudflare §11.1.1 row 4; Gateway §21.2 rule 10) |
| `integration_fabric` | `integration_fabric_read`, `integration_fabric_controlled_write` | `delegated_user`, `service_account` | MellyCore + provider-native, with full downstream provenance | Must preserve the full downstream identity and provider chain | Deny (§12.1; Gateway §14.2) |

Registry §13.2's target-compatibility paragraph closes the mapping in both
directions: fabric classes require `integration_fabric`;
`restricted_operator_investigation` requires `restricted_tool`; every other
class requires `provider_account`.

No document treats authentication **mode** and authentication **target** as the
same concept. Registry §12.1 opens by distinguishing them explicitly, Registry
§13.1 carries both as separate fields, Gateway §9.2 and §23 carry both, and
Cloudflare §11.1 states "Authentication mode and authentication target are
independent."

## 17. `mcp_oauth_grant` review

**Result: PASS.**

| Requirement | Evidence | Verified |
| --- | --- | --- |
| Authentication target is explicitly `restricted_tool` | Registry §12.1 dedicated paragraph; §13.2 row 9 ("target MUST be `restricted_tool`"); Cloudflare §11.1, §13.4.0 | Yes |
| OAuth authority is the exact registered restricted tool or MCP server | Registry §12.1 ("the OAuth authority belongs only to the exact registered restricted tool or MCP server"); Gateway §21.2 rule 10 | Yes |
| Not Cloudflare OAuth | Cloudflare §11.1 ("it is not a Cloudflare grant"); §13.4.0 ("never Cloudflare/provider OAuth"); Pack §12 | Yes |
| Grants no Cloudflare account access | Registry §12.1; Cloudflare §11.1.1 row 4; §13.4.1 "Account access: none" | Yes |
| Grants no Cloudflare API access | Registry §7.5, §12.1; Cloudflare §11.1.1 row 4 "Provider API authority: **None**" | Yes |
| Cannot be stored or reused as a provider credential | Registry §12.1 ("cannot be reused, projected, or resolved as a provider credential"); Gateway §21.2 rule 10; Pack §12 | Yes |
| Exact tool ID and revision required | Registry §24.1; Gateway §21.2 rule 11; Cloudflare §25.2 item 5 | Yes |
| Exact tenant and operator required | Registry §11.2 rule 10, §24.1; Cloudflare §25.2 items 2, 4 | Yes |
| Exact allowed tool capability required | Registry §24.1 `allowed_capability_ids`; Gateway §21.2 rules 5, 11; Cloudflare §25.2 items 5, 8 | Yes |
| Zero or multiple matching profiles deny | Gateway §14.2; Registry §13.2, §24.1 | Yes |
| Provider-account target with this class denies | Registry §12.1, §13.2 target compatibility; Gateway §9.2, §21.2 rule 10; Cloudflare §11.1 | Yes |

**No document permits a provider-account interpretation.** Registry §12.1's
rule that "a mode name containing `oauth` or `mcp` never implies a
provider-account target" removes the inference that generated `P2-301`. The
finding is closed.

One residual observation — the contracts identify no concrete restricted-tool
OAuth authority that is not itself provider-operated — is recorded as
`P3-403`. It does not create ambiguity: the contract result is an explicit
deny for any provider-targeted grant.

## 18. Scope-applicability review

**Result: PASS.** Registry §11 owns exactly three values.

| Requirement | Evidence | Verified |
| --- | --- | --- |
| Applicability declared at capability-registration level | Registry §11.2 rule 2 ("Every concrete capability MUST declare `scope_applicability` for every dimension allowed by its provider contract"); §14.1 field (15) | Yes |
| Applicability must be permitted by the provider contract | Registry §11.2 rule 7 ("valid only when the provider contract explicitly permits it for that concrete capability"); §14.2 rule 10; Cloudflare Rule 9.4 | Yes |
| Gateway validates before execution | Gateway §13.1 ("The Gateway validates the declaration before resolving targets or credentials"); §13.2 rule 8; §14.2; §17 step 13 | Yes |
| Omitted applicability denies | Registry §11.2 rules 2 and 8; §14.2 rule 4; Gateway §13.2 rule 8 | Yes |
| Unknown applicability denies | Registry §11.2 rule 8 ("selecting `not_applicable` outside the provider contract's permitted model denies and is audited"); Gateway §13.2 rule 8 | Yes |
| `not_applicable` is not equivalent to missing | Registry §11.2 rule 8 ("`not_applicable` is not an empty wildcard"); §14.2 rule 4 ("absent scope never implies `not_applicable`"); Gateway §13.2 rule 8 ("Omission never means `not_applicable`") | Yes |
| `not_applicable` cannot be used merely because a value is unavailable | Registry §11.2 rule 8 ("It asserts that the capability has no authority in that scope domain") | Yes |
| `optional` never widens authority | Registry §11.2 rule 7 | Yes |

## 19. Provider-versus-capability scope review

**Result: PASS.**

- Provider metadata defines the complete possible scope family:
  `possible_provider_native_scope_dimensions` plus
  `provider_api_scope_defaults` (Registry §11.2 rule 2; §26.1).
- Provider API capabilities retain strict applicable account, zone, and
  resource scope: Registry §11.2 rule 9; Cloudflare Rule 9.4 ("Every D1–D3
  provider API capability … retains `required` account, zone, and resource
  scope wherever its row or domain requires them"); Cloudflare §13.1.0,
  §13.2.0, §13.3.0 each declare `provider_account` target with applicable
  provider-native scope `required`.
- A concrete capability may mark a dimension `not_applicable` only when
  explicitly allowed: Registry §11.2 rule 7; Cloudflare Rule 9.4 restricts it
  to D4 alone.
- Capability declarations cannot weaken unrelated capabilities: Registry §11.2
  rule 9 ("it may never weaken scope for another capability"); Gateway §13.2
  rule 9; Cloudflare Rule 9.4 ("this exception cannot weaken any D1–D3
  capability").
- The Gateway evaluates the concrete applicability map: Gateway §11 item 9,
  §13.1, §14.2.
- Provider-native scope omission still fails closed for normal provider API
  capabilities: Registry §11.2 rules 7 and 8; Gateway §13.2 rules 8 and 10.

`not_applicable` therefore cannot weaken normal provider API scope. The
provider-wide relaxation that `P1-302` would have required is not what the
remediation did: it moved applicability down to the capability and fenced the
exception to D4 by name.

## 20. D4 scope review

**Result: PASS.** D4 requires all eleven dimensions and marks all four
provider-native dimensions explicitly `not_applicable`.

| Required by D4 | Evidence |
| --- | --- |
| MellyCore tenant | Registry §11.2 rules 1, 10; Cloudflare §25.2 item 2 |
| Exact operator | Cloudflare §13.4.0 ("exact operator reference required"), §25.2 item 4; Registry §11.2 rule 10 |
| Exact environment | Registry §11.1, §11.2 rule 10, §24.1; Cloudflare §13.4.0, §25.2 item 5 |
| Exact registered restricted-tool ID | Registry §11.1, §24.1; Cloudflare §13.4.0, §25.2 item 5 |
| Exact tool revision | Registry §11.1 `tool_contract_revision`, §24.1; Gateway §21.2 rule 11; Cloudflare §25.2 item 5 |
| Exact tool capability | Registry §11.1 `tool_capability`, §24.1 `allowed_capability_ids`; Cloudflare §25.2 items 5, 8 |
| Exact allowed resource class | Registry §11.1, §11.2 rule 10, §24.1; Cloudflare §13.4.0, §25.2 item 7 |
| Capability authorization | Registry §21.1 fact 6; Gateway §17 step 10 |
| Runtime enablement | Registry §21.1 fact 7; Gateway §17 step 8, §32, Rule 32.1 |
| Restricted-tool credential class | Registry §13.2 row 9; Cloudflare §11.1.1 row 4 |
| Restricted-tool authentication target | Registry §12.1, §13.2; Cloudflare §13.4.0; Gateway §9.2 |

| Marked `not_applicable` | Evidence |
| --- | --- |
| Provider account | Registry §26.1 D4 scope rule; Cloudflare Rule 9.4, §11.2 rule 2, §13.4.0 |
| Provider zone | Same |
| Provider resource | Same |
| Provider-native acting identity | Registry §7.5 audit column ("provider-native actor is `not_applicable`"); Gateway §29.1; Cloudflare §31.3 |

Every one of these is an **explicit declaration**, never inferred from absence:
Registry §11.2 rule 8 and Gateway §13.2 rule 8 both state that omission never
means `not_applicable`. Supplying unexpected provider account or zone scope
**denies rather than being ignored**: Cloudflare §13.4.0 ("a supplied value
denies"), Rule 9.4 ("provider-native value supplied to D4 denies"), §11.1.1
row 4 (denies **and audits**), Registry §11.2 rule 8, Gateway §13.2 rule 8, and
Gateway §9.2's `downstream_provider` row ("unexpectedly supplied inapplicable
value → deny").

## 21. Restricted-tool registration review

**Result: PASS.** Registry §24.1 requires every element the gate criteria
enumerate.

| Required element | Present in §24.1 |
| --- | --- |
| Stable tool/server ID | `restricted_tool_id` (plus `mcp_server_id` for MCP records) |
| Tool-contract revision | `tool_contract_revision` |
| Tenant | `tenant_binding` |
| Environment | `environment` |
| Allowed tool capabilities | `allowed_tools` + exact `allowed_capability_ids` |
| Operator eligibility | `eligible_acting_identity_types`; `operator_only` |
| Credential-profile class | one `required_credential_profile_class` |
| Authentication target | `authentication_target` |
| Sensitivity metadata | `data_sensitivity`; `allowed_resource_classes` |
| External-content posture | `external_content_posture`; `output_trust_level` |
| Audit source | `audit_source`; `audit_mode`; `retention_policy`; `session_metadata_policy` |
| Runtime-enable state | Registry §21.1 fact 7; Gateway §17 step 8, §32 |

Separation of the layered facts is explicit:

- Discovery does not register — Registry §24.1 ("A discovered tool is never
  executable until this exact record … match"); Gateway §21.2 rule 7.
- Registration does not authorize — Registry §21.2 rule 6; §14.2 rule 6.
- Authorization does not imply runtime enablement — Registry §21.1 fact 7;
  Gateway Rule 32.1.
- Runtime enablement does not imply operation approval — Registry §21.5;
  Gateway §18.
- Revision mismatch denies — Gateway §21.2 rule 11; Registry §24.1.
- Tenant mismatch denies — Registry §24.1; Gateway §13.2, §14.3.
- Capability mismatch denies — Gateway §21.2 rules 5, 11; Registry §24.1.

## 22. Gateway identity-chain review

**Result: PASS.** Every location Review 003 identified as inconsistent now
consumes the Registry vocabulary.

| Location | Pre-remediation | Post-remediation | Verified |
| --- | --- | --- | --- |
| §8.2 | No statement of ownership; §8.1's twelve identities stood beside the Registry's | Explicit preamble: §7.5 is sole owner; the twelve identities "do not create a second acting-identity enum"; "MUST NOT invent aliases or fallback translations" | Yes |
| §9.1 chain | `→ delegated_user \| service_account → downstream_provider → target_resource` | `→ delegated_user \| service_account \| mellycore_operator → required_authentication_target → downstream_provider (provider/fabric path only) → target_resource \| restricted_tool_resource` | Yes |
| §9.2 | Row `delegated_user \| service_account` — "Exactly one required; never both, never neither → Deny" | Rows `required_acting_identity_type` (one §7.5 value, immutable), `acting_identity_ref`, `required_authentication_target`, conditional `downstream_provider`, `target_resource \| restricted_tool_resource` | Yes |
| §9.3 | Six rules, none covering the operator path | New rule 7 constrains `mellycore_operator` to an exact class, target, `not_applicable` provider scope, and a resolving tool record; "never a fallback" | Yes |
| Rule 16.7 | "Exactly one of delegated-user or service-account identity is present per request" | Three-value exclusivity with zero/multiple/unknown/conflicting denial and the operator constraint | Yes |
| §17 step 13 | "Resolve acting identity type (delegated vs service)" | "Resolve and freeze exact `required_acting_identity_type`; validate identity/class/target/applicability compatibility" | Yes |
| §14.2 | Matched "class, identity, pinned `authentication_mode`, tenant, provider, environment, scope, and capability" | Adds authentication target and applicability to both the input list and the match set | Yes |
| §34.6 | "Target scope: Documentation only; no account, zone, or resource" | Four explicit rows: acting-identity selector, authentication, provider-native scope, restricted-tool scope | Yes |
| §34.7 | Claimed enforceability without weakening while §9.2 denied D4 | "D4 is now representable through the canonical operator identity, restricted-tool authentication target, explicit provider-native `not_applicable` declaration, and exact restricted-tool scope" | Yes |

Incompatible identity/class/target combinations deny at four independent
points: Registry §14.2 rule 9, Gateway §9.2, Gateway Rule 16.7, and Gateway
§14.2. Provider-native acting identity is explicitly N/A for D4 rather than
absent (Registry §7.5; Gateway §29.1).

The §14.3 prohibited-selection table retains "Delegated-user →
service-account fallback" and does not add an operator row, but every operator
fallback path is closed explicitly by Rule 16.7, §9.3 rule 7, Registry §7.5's
substitution column, and the standing "best available credential" and
"automatic credential widening" denials. No fallback is reachable.

## 23. Gateway execution-envelope review

**Result: PASS.** Gateway §23 carries `required_acting_identity_type` (one
Registry §7.5 value), `acting_identity_ref`, `required_authentication_target`
(one Registry §12.1 value), `scope_applicability`, `provider_native_scope`
(exact values or explicit `not_applicable`), `restricted_tool_id`,
`tool_contract_revision`, `restricted_tool_capability`, and
`allowed_resource_class`, with the restricted-tool fields "required exactly
when applicable".

New **Rule 23.3** makes the identity type, authentication target, and scope
applicability bind before credential resolution and remain immutable for one
request evaluation, with missing, unknown, conflicting, or class-incompatible
values denying, and states that "The Gateway never changes identity mode or
scope applicability to obtain a credential match." Rule 23.1 (no secret
material) and Rule 23.2 (unknown fields rejected) are unchanged.

`provider_id` remains an envelope field distinct from the conditional
`downstream_provider_id` chain element, so a D4 capability registered under
provider `cloudflare` carries its provider ID for profile matching while
declaring `downstream_provider: not_applicable`. This is deterministic and
introduces no contradiction.

## 24. Gateway audit-actor review

**Result: PASS.** Gateway §29.1 now requires every audit record to carry the
canonical `required_acting_identity_type` and the exact `acting_identity_ref`.
For `mellycore_operator`, "the audit actor is the authenticated MellyCore human
operator; no service account, agent, credential, session, or tool may replace
it." On a restricted-tool path the provider-native actor and provider-native
scope are recorded explicitly as `not_applicable`, and the exact tool identity,
revision, capability, authentication target, tenant, environment, and allowed
resource class are recorded.

Cloudflare §31.3 and §31.4 mirror this: the execution record carries the
canonical type, the exact labelled acting-identity reference, the
authentication target, applicable account/zone references **or explicit
`not_applicable`**, and applicable restricted-tool ID and revision; the D4
session record adds the canonical `mellycore_operator` type, environment,
mode and `restricted_tool` target, tool ID and revision, allowed resource
class, explicit provider-native `not_applicable`, audit source, and retention.

## 25. Registry Cloudflare scope review

**Result: PASS.** `P1-302`'s source is corrected at the provider record itself.

Registry §26.1 no longer contains `required_scope_dimensions`. It now declares:

- `possible_provider_native_scope_dimensions`: `account`, `zone`, `resource`.
- `provider_api_scope_defaults`: account required where the API family is
  account-scoped, zone required where zone-scoped, resource required where the
  capability targets a concrete resource, with every provider API capability
  declaring all three states explicitly.
- A **D4 scope rule**: `account: not_applicable`, `zone: not_applicable`,
  `resource: not_applicable`; exact restricted-tool ID, tool capability,
  tenant, operator, environment, revision, and allowed
  documentation/investigation resource class `required`.

`tenant`, previously listed among the Cloudflare provider record's required
dimensions, moved into the always-required MellyCore set (Registry §11.1;
§11.2 rule 1). This is a strengthening: tenant is now mandatory for every
provider rather than declared per provider.

No generic empty-scope execution exists. Registry §11.2 rule 10 permits empty
provider-native scope only under four simultaneous conditions — all
provider-native dimensions explicitly `not_applicable`, a credential class
prohibiting provider-account binding, `authentication_target: restricted_tool`,
and complete restricted-tool scope — and Gateway §13.2 rule 10 states
"Otherwise empty provider scope denies." A D4 applicability declaration cannot
be used for a provider API capability (Registry §11.2 rule 9; Cloudflare
Rule 9.4).

## 26. Cloudflare D4 review

**Result: PASS.** D4 is unchanged in substance and now fully expressible.

| Property | Evidence | Verified |
| --- | --- | --- |
| Exactly three capabilities | §13.4.1: `D4-01`, `D4-02`, `D4-03`; §13.5 "Operator investigation (D4) 3, R0 × 3" | Yes |
| Documentation or investigation only | §13.4.0 ("documentation scope only in v1.0"); §25.1 | Yes |
| R0–R2 per existing classification | §13.4.1 all R0; §11.1.1 row 4 "R2 (D4 v1.0 remains R0)" | Yes |
| Operator-bound | §13.4.0 "MellyCore **operator only**. No autonomous agent may initiate a D4 session"; Rule 10.2 | Yes |
| Non-provider-account | §13.4.1 "Account access: none"; §13.4.0; Rule 9.4 | Yes |
| Non-provider-API | §11.1.1 row 4 "Provider API authority: **None**"; §13.4.0 | Yes |
| Non-mutating | §11.1.1 row 4 "Mutation authority: **None**"; Gateway §14.2 `mutation_prohibited: true` | Yes |
| Non-containment | D4 rows carry no containment capability; §33.3 confines containment to the D3 subset under `CF_CONTAIN` | Yes |
| Restricted-tool-only | §13.4.0 target `restricted_tool`; §25.2 items 5–7 | Yes |
| Fully audited | §31.4 expanded D4 session audit; Gateway §29.1 | Yes |
| External-content-safe | §13.4.0 output rule (untrusted, size-bounded, provenance-stamped, never elevated into policy/proposal/approval evidence without D1/D2 re-derivation); §26 | Yes |

No remediation text authorizes MCP execution globally. Gateway §21.2 rules 1–2
(unrestricted search-and-execute and generic arbitrary execution prohibited)
and rule 9 (Cloudflare MCP documentation-only) are unchanged; the new rules 10
and 11 add constraints only. Cloudflare `P-01` and `P-02` are byte-identical
to the parent commit. Cloudflare §25.2 grew from eleven to sixteen conditions,
all restrictive, retaining "**no autonomous unrestricted search-and-execute**,
in any form" as the final item. An actual restricted tool remains unconnected
and unauthorized.

## 27. Cloudflare integrity review

**Result: PASS.**

| Check | Result | Method |
| --- | --- | --- |
| 58 capability rows present | D1 16, D2 16, D3 23, D4 3 = 58 | Regex row count at `699f1d39…` and `b90ce82…` |
| 13 prohibition rows present | `P-01`…`P-13` | Regex row count at both commits |
| All 71 substantive rows match the starting baseline | **Byte-identical**: SHA-256 `759d4250007946ee4456537ae74cbce54051186592617bcd75b16ebc9a592a41` at both commits | Digest over the ordered extracted row set |
| Zone-wide Schema Validation `block` remains R5 | `D3-10` unchanged within the identical row set; §13.5 tier distribution unchanged (R5 × 6) | Unchanged rows |
| Endpoint-deletion safety | `D3-02` R5 irreversible; `P-06` unchanged | Unchanged |
| Label-replacement semantics | `D3-03` R4→R5 escalation; `P-07` unchanged | Unchanged |
| Read-after-write required | §13.3.0; §32; `P-10` | Unchanged |
| Indeterminate outcomes require reconciliation | §29.2; Gateway §26.3 `INDETERMINATE` | Unchanged |
| Blind retries prohibited | §29.2; Gateway §26.2 rule 1 | Unchanged |
| MCP documentation-only | §25.1; Gateway §21.2 rule 9; `P-01`, `P-02` | Unchanged |

The remediation's edits to this contract are confined to §9.1 rules 2–3, new
Rule 9.4, §10 preamble, new Rule 10.2, §11.1, §11.1.1 rows 1 and 4, the new
target paragraph, §11.2 rule 2, §13.0, the four domain default blocks, §25.2,
§31.3, and §31.4. None touches a capability row, a prohibition row, or a risk
classification.

## 28. Cybersecurity Pack regression review

**Result: PASS.**

| Check | Result |
| --- | --- |
| Seven providers remain | `microsoft_defender_xdr_graph_security`, `github_advanced_security`, `cloudflare`, `okta_workforce_identity`, `splunk_security_analytics`, `crowdstrike_falcon`, `snyk_developer_security` — all present |
| R0–R2 ceiling remains | Seven "**Initial risk ceiling:** R2" statements, one per provider; §4, §7, §10 unchanged |
| Cloudflare authority delegated to its provider contract | §21 ("This pack neither duplicates nor narrows those tables"); §12 ("this pack does not reinterpret those labels") |
| No provider API access implied for D4 | §12 and §21 both state the D4 model does "not authorize a tool connection or Cloudflare API access" |
| No MCP execution authorized | §12 ("Nothing here authorizes MCP execution, provider API access, containment, or mutation") |
| Identity and scope terminology maps to canonical owners | §7 rule 6 (applicability); §11 (Registry §7.5 sole owner); §12 (targets and applicability) |
| Pack does not duplicate a competing identity or scope model | §11 "The chain includes … exact canonical acting identity"; §12 now declares its class table "a non-exhaustive pack projection of the Registry §13.2 catalogue and creates no second enum" |
| Prerequisites remain non-authorizations | §32 item 2 now requires "a future independent `PASS` from `MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004` — currently not run; the documentation gate remains failed" |

The Review 003 editorial observation about the §12 class table lacking a
non-exhaustive caveat is resolved by the remediation's added sentence.

Note for the shared-context update: Pack §32 item 2 states the gate "remains
failed" as of the remediation commit. That statement was true when written and
remains an accurate description of the state at `b90ce82…`. This review does
not amend it; the Pack is a reviewed, immutable document here, and the current
gate result is recorded in this record and in shared context.

## 29. Eight-fact separation review

**Result: PASS.** No new identity, target, or scope field collapses any fact.

| Fact | Preserved by | Interaction with the new fields |
| --- | --- | --- |
| 1 Provider registered | Registry §21.1; §21.2 rule 6 | An acting-identity type is not a registration |
| 2 Adapter implemented | Registry §21.1; Gateway §17 step 7 | A restricted tool is not an adapter; `adapter_state: blocked` unchanged |
| 3 Credential configured | Registry §13.4 | Registry §13.2's target paragraph states target classification "does not imply that a credential exists or that any authorization fact holds" |
| 4 Credential verified | Registry §21.1; §13.1 `last_verification_time` | Unchanged |
| 5 Tenant authorized | Registry §21.3–21.5; Gateway §17 step 9 | Tenant scope is now always-required MellyCore scope, additional to fact 5, never substitutive |
| 6 Capability authorized | Registry §21.3–21.5; Gateway §17 step 10 | Registry §14.2 rule 6 unchanged: a capability record is a policy input |
| 7 Runtime enabled | Registry §21.1; Gateway §17 step 8, §32 | Gateway Rule 32.1 still asserts none currently passes |
| 8 Operation approved | Control Plane §16.1 + Gateway §18 | Registry §21.5 forbids embedding fact 8 in a standing record |

A valid operator, tool record, credential class, authentication target, or
scope map implies none of the other facts. Registry §24.1's chain — discovery →
record → revision → identity → target → class → capability → runtime
enablement → authorization — keeps the restricted-tool path aligned with the
same separation.

## 30. Deterministic scenario results

Twenty-four scenarios replayed against contract text. **All twenty-four resolve
deterministically. None requires architectural interpretation.**

Common to every row: exact MellyCore tenant and environment are required
(Registry §11.1, §11.2 rule 1); caller claims are untrusted; and no provider is
implemented, credentialed, enabled, or connected today.

| # | Scenario | Acting identity / canonical type | Credential class | Auth mode | Auth target | Tenant | Provider-native applicability | Restricted-tool scope | Capability / tier | Facts | Runtime-enable required | Audit | Decision | Exact fail-closed reason | Sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Delegated Cloudflare read, correct identity and profile | Exact delegated subject / `delegated_user` | `read_only_delegated` | `delegated_oauth` | `provider_account` | Exact | applicable dims `required` | `not_applicable` | D1 read / R1 | 1–7; 8 `not_required` | Yes | Full decision record | **Resolves**, then denies today | `ADAPTER_UNAVAILABLE` / `RUNTIME_NOT_ENABLED` (facts 2, 7 absent) | Registry §7.5, §13.2, §14.2 r9; Gateway §14.2, §15, §17, §18.4; Cloudflare §11.1.1 r1, §13.1.0 |
| 2 | Service Cloudflare read, correct identity and profile | Exact service identity / `service_account` | `read_only_service` | one pinned service mode | `provider_account` | Exact | applicable dims `required` | `not_applicable` | D1 read / R1 | 1–7; 8 `not_required` | Yes | Service identity labelled | **Resolves**, same standing denial | as above | Registry §7.5, §13.2; Gateway §16, §34.1; Cloudflare §11.1.1 r1 |
| 3 | `CF_READ` with no acting-identity selector | Missing | Cannot project | Unresolved | Unresolved | Exact | present | n/a | D1 read / R1 | — | — | Denial audited | **Deny** before credential resolution | Missing `required_acting_identity_type` → `IDENTITY_UNRESOLVED` | Gateway §9.2, §17 step 13, Rule 23.3; Registry §14.2 r9; Cloudflare §11.1.1 r1 |
| 4 | `CF_READ` with both identity modes declared | Conflicting | Two candidate classes | Two candidates | `provider_account` | Exact | present | n/a | D1 read / R1 | — | — | Denial audited | **Deny** — multiple/conflicting types; no dynamic switch | Gateway Rule 16.7; Registry §7.5, §13.2, §14.2 r9 | Gateway Rule 16.7; Registry §13.2 |
| 5 | Delegated request with a service credential | `delegated_user` | Profile is `read_only_service` | service mode | `provider_account` | Exact | applicable `required` | n/a | D1 read / R1 | — | — | Audited security event | **Deny**; never widened | Identity/class mismatch; delegated→service fallback prohibited | Gateway §14.2, §14.3, §15.4; Registry §7.5 |
| 6 | Service request with a delegated credential | `service_account` | Profile is `read_only_delegated` | `delegated_oauth` | `provider_account` | Exact | applicable `required` | n/a | D1 read / R1 | — | — | Audited security event | **Deny** | Identity/class mismatch; a service account may never use a delegated user's profile | Gateway §14.2, §16.3; Registry §7.5 substitution column |
| 7 | D4 with exact operator, tool registration, revision, capability, and scope | Exact operator / `mellycore_operator` | `restricted_operator_investigation` | `no_auth_public_documentation` | `restricted_tool` | Exact | `account`/`zone`/`resource` explicitly `not_applicable` | Exact ID, revision, capability, operator, environment, resource class | D4-01 / R0 | 1–7; 8 `not_required` | Yes | Session transcript metadata | **Contract-resolvable**, denies today | `RUNTIME_NOT_ENABLED` / `ADAPTER_UNAVAILABLE`; no tool is connected | Registry §7.5, §11.2 r10, §24.1; Gateway §9.3 r7, Rule 16.7, §21, §34.6; Cloudflare §13.4.0, §25.2 |
| 8 | D4 with missing tool registration | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | `not_applicable` | **Absent** | D4 / R0 | — | — | Denial audited | **Deny** | No exact restricted-tool record; unregistered tools are not executable | Registry §24.1; Gateway §21.2 rules 6, 7, 11 |
| 9 | D4 with revision mismatch | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | `not_applicable` | ID matches, **revision differs** | D4 / R0 | — | — | Denial audited | **Deny** | `tool_contract_revision` mismatch | Registry §24.1; Gateway §21.2 rule 11; Cloudflare §25.2 item 5 |
| 10 | D4 with missing tool capability authorization | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | `not_applicable` | Tool exact; requested capability **not in allowlist** | D4 / R0 | — | — | Denial audited | **Deny** | Requested capability absent from `allowed_capability_ids` | Registry §24.1; Gateway §21.2 rules 5, 11; Cloudflare §25.2 items 5, 8 |
| 11 | D4 with provider-native scope absent but applicability missing | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | **Declaration omitted** | Otherwise exact | D4 / R0 | — | — | Denial audited | **Deny** | Omission never means `not_applicable`; incomplete `scope_applicability` | Registry §11.2 rules 2, 8; §14.2 r4; Gateway §13.2 r8 |
| 12 | D4 with provider-native scope explicitly `not_applicable` | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | All three explicitly `not_applicable` | Complete and exact | D4 / R0 | 1–7; 8 `not_required` | Yes | Session transcript metadata | **Contract-resolvable**, denies today | `RUNTIME_NOT_ENABLED` | Registry §11.2 r10, §26.1; Cloudflare Rule 9.4, §13.4.0; Gateway §13.2 r10 |
| 13 | D4 with an unexpected account or zone supplied | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | N/A declared but **a value is supplied** | Exact | D4 / R0 | — | — | Denial audited as a security event | **Deny**, never ignored | Value supplied for a `not_applicable` dimension | Registry §11.2 r8; Cloudflare Rule 9.4, §11.1.1 r4, §13.4.0; Gateway §13.2 r8, §9.2 |
| 14 | D4 requesting Cloudflare REST API access | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | `not_applicable` | Exact | Provider API attempt / R1+ | — | — | Audited security event | **Deny** | Provider API eligibility **No**; provider API authority **None**; class cannot serve a provider API capability | Registry §7.5, §13.2; Cloudflare §11.1.1 r4, Rule 10.2; Gateway §14.2 |
| 15 | D4 requesting a mutation | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | `not_applicable` | Exact | Mutation attempt / R3+ | — | — | Audited security event | **Deny** | `mutation_prohibited: true`; mutation authority **None** | Gateway §14.2, §21.2; Cloudflare §11.1.1 r4, §25 |
| 16 | D4 using a normal Cloudflare read credential | `mellycore_operator` | Profile is `read_only_service` | service mode | `provider_account` | Exact | `not_applicable` for D4 | Exact | D4 / R0 | — | — | Denial audited | **Deny** | Identity/class/target mismatch; zero compatible profiles; no cross-class substitution | Registry §7.5 (compatible classes = `restricted_operator_investigation` only), §13.2 closing; Gateway §14.2 |
| 17 | D4 using restricted-tool OAuth targeted at the exact tool | `mellycore_operator` | `restricted_operator_investigation` | `mcp_oauth_grant` | `restricted_tool` | Exact | `not_applicable` | Exact registered tool | D4-03 / R0 | 1–7; 8 `not_required` | Yes | Session transcript metadata | **Contract-resolvable**, denies today | `RUNTIME_NOT_ENABLED`; the grant is tool-only and creates no provider authority | Registry §12.1; Gateway §21.2 r10; Cloudflare §11.1, §25.2 item 6 |
| 18 | D4 using OAuth targeted at a provider account | `mellycore_operator` | `restricted_operator_investigation` | `mcp_oauth_grant` | **`provider_account`** | Exact | provider scope supplied | Absent | D4 / R0 | — | — | Denial audited | **Deny** before credential resolution | Target incompatible with class; a mode containing `oauth`/`mcp` never implies a provider-account target | Registry §12.1, §13.2 target compatibility; Gateway §9.2, §21.2 r10; Cloudflare §11.1 |
| 19 | `mellycore_operator` used for a normal Cloudflare API read | `mellycore_operator` | any normal read class | provider mode | `provider_account` | Exact | `required` | n/a | D1 read / R1 | — | — | Denial audited | **Deny** | Operator is not provider-account or provider-API eligible; never substituted into D1–D3 | Registry §7.5; Cloudflare Rule 10.2; Gateway Rule 16.7, §9.3 r7 |
| 20 | Two compatible restricted-tool credential profiles match | `mellycore_operator` | `restricted_operator_investigation` | valid mode | `restricted_tool` | Exact | `not_applicable` | Exact | D4 / R0 | — | — | Denial audited | **Deny** before material resolution | Multiple compatible profiles; no "best available credential" | Gateway §14.2, §14.3; Registry §13.2, §24.1 |
| 21 | Tool discovered but not registered | `mellycore_operator` | `restricted_operator_investigation` | n/a | `restricted_tool` | Exact | `not_applicable` | **Discovery only** | D4 / R0 | — | — | Denial audited | **Deny** | Discovery is untrusted inventory, not permission | Gateway §21.2 rules 6, 7, 11; Registry §24.1 |
| 22 | Tool registered and authorized but runtime disabled | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | Exact | `not_applicable` | Exact | D4 / R0 | 1–6 hold; **7 absent** | Yes | Denial audited | **Deny** | `RUNTIME_NOT_ENABLED` — fact 7 is independent | Registry §21.1 fact 7; Gateway §17 step 8, §32, Rule 32.1 |
| 23 | Registered tool belonging to another tenant | `mellycore_operator` | `restricted_operator_investigation` | tool mode | `restricted_tool` | **Mismatched** | `not_applicable` | Tool exact but bound to tenant B | D4 / R0 | — | — | Audited security event | **Deny** | `tenant_binding` mismatch; no cross-tenant reuse or fallback | Registry §24.1, §11.2 r1; Gateway §13.2, §14.3; Cloudflare §9.1 rule 5 |
| 24 | Webhook or tool response containing prompt-injection instructions | any | any | any | any | Exact | as declared | as declared | any | — | — | `INJECTION_SUSPECTED` recorded and surfaced | **Content treated as data**; any credential selection influenced by it **denies** | Untrusted external content is never an instruction or capability selector | Gateway §14.3, §21.2 rule 4, §28, §26 outcome table; Cloudflare §26, §13.4.0 output rule |

**Scenario determinism: 24 of 24 deterministic; 0 require architectural
interpretation.** Review 003's scenario 9 — the sole indeterminate case — is
row 7 here and now resolves to one outcome with exact sources.

## 31. Cross-reference review

**Result: PASS, with one editorial observation.**

- Registry §26.2's projection statement, Gateway §34's preamble, and Cloudflare
  §11.1.1 state the same four projections and the same selector field with no
  divergence.
- Registry §7.5, Gateway §8.2, Cloudflare §10, and Pack §11 all name Registry
  §7.5 as the sole acting-identity owner, consistently.
- Registry §12.1, Gateway §9.2/§21.2 rule 10, Cloudflare §11.1, and Pack §12
  state the same target semantics for `mcp_oauth_grant`.
- Registry §11.2, Gateway §13.2, and Cloudflare Rule 9.4 state the same
  applicability semantics with no divergence in value names or fail-closed
  direction.
- Every path referenced in the amended sections resolves to an existing file.
- No document silently contradicts an accepted document in a way that would
  constitute an implicit amendment (Registry §31; Gateway §39; Cloudflare §38).

Two stale intra-Registry cross-references survive the §14.1 renumbering and are
recorded as `P3-402`. One editorial observation carries no finding: Cloudflare's
new **Rule 9.4** is numbered after Rules 9.2 and 9.3 but placed inside §9.1,
ahead of the §9.2 and §9.3 headings. The rule ID is unique and unambiguous, so
no reference is broken.

## 32. Shared-context review

**Result: PASS.** Every claim the remediation wrote into the four
shared-context files was checked against the repository.

| Claim | Verified |
| --- | --- |
| Registry owns exactly three canonical acting-identity types | True — mechanically counted |
| `required_acting_identity_type` is the canonical selector | True — present in all four contracts |
| Gateway can represent `mellycore_operator` only for an explicitly compatible operator-bound restricted-tool capability and class | True — Gateway §9.3 rule 7, Rule 16.7 |
| Identity selector, target, and applicability bind before credential resolution and are immutable | True — Gateway Rule 23.3, §17 step 13 |
| D4 remains documentation/investigation-only, R0 in v1.0, R2 maximum, with no account, API, mutation, containment, or proposal-evidence authority | True — Cloudflare §13.4.0, §13.4.1, §11.1.1 row 4 |
| `mcp_oauth_grant` targets only that tool/server and is never Cloudflare/provider OAuth | True — Registry §12.1; Cloudflare §11.1, §13.4.0 |
| "This remediation is **not** a documentation-gate PASS"; closure unverified until Review 004 | True at the time written; this review is that verification |
| Adapter Scaffold remains blocked, ineligible, not started, unauthorized | True at `b90ce82…` |
| No restricted tool connected, no MCP execution authorized, no provider runtime/API authorized, no credential exists | True — no such artifact exists in the repository |
| Global OpenAI Batch pointer unchanged | True — 13 occurrences across the five shared-context files at both `699f1d39…` and `b90ce82…`, identical |

No shared-context file overstates the remediation, claims connectivity, claims
credentials, or claims runtime implementation. This review's own
shared-context updates are bounded to the enterprise-provider track and are
listed in the Review 004 task report.

## 33. New findings

### `P3-401` — the canonical acting-identity table is not a well-formed Markdown table

**Severity:** P3 (editorial; implementation behavior unaffected).

**Location:** Registry §7.5, line 211.

**Statement.** The new acting-identity vocabulary table has a nine-cell header
row and nine-cell data rows, but its delimiter row contains **ten** `---`
cells. Under GitHub-Flavored Markdown, the delimiter row must match the header
row's cell count or the block is not recognized as a table, so the repository's
single normative acting-identity vocabulary may render as an unformatted
paragraph. A scan of all four remediated specs found this to be the only
malformed table introduced.

**Why this is not blocking.** The content is complete, unambiguous, and
machine-readable as pipe-delimited text; every consuming contract restates the
constraints it depends on (Gateway §9.2, Rule 16.7, §9.3 rule 7; Cloudflare
Rule 10.2; Pack §11). No behavior, denial, or scenario outcome changes.

### `P3-402` — two intra-Registry references were not updated for the §14.1 renumbering

**Severity:** P3 (editorial; implementation behavior unaffected).

**Locations:** Registry §26.3 (line 1116); Registry §27.1 item 5 (line 1131).

**Statement.** The remediation renumbered §14.1 from 27 to 28 fields and
renamed `required_provider_scope` to `scope_applicability` (field 15). The
§26.2 mapping table was correctly renumbered throughout, but:

1. §26.3 still cites "`verification_policy` (field 20)". Under the new
   numbering `verification_policy` is field **21**; field 20 is `audit_policy`.
2. §27.1 item 5 still requires "explicit `required_provider_scope`", a field
   name this remediation retired.

**Why this is not blocking.** Both references name the policy in prose as well
as by number, and the normative requirements are carried by §14.1, §14.2 rule 4
("A missing or incomplete `scope_applicability` denies"), and §11.2 rules 2 and
7–10. §27.1 is a pre-`conformance_verified` checklist, and §27.2 records that
this contract asserts these validations pass for no provider. No runtime
decision depends on either citation.

### `P3-403` — no non-provider-operated restricted-tool OAuth authority is identified

**Severity:** P3 (maintenance; implementation behavior unaffected).

**Locations:** Registry §12.1; Cloudflare §11.1, §13.4.0, §25.1, §25.2 item 6.

**Statement.** The contracts now require that an `mcp_oauth_grant` under
`restricted_operator_investigation` target the exact registered restricted tool
and never a provider account, and that a provider-targeted grant denies. They
do not, however, identify any concrete restricted-tool or MCP-server OAuth
authority that is not itself operated by the provider. If the only candidate
D4 tool is a provider-operated MCP server whose OAuth is issued against a
provider account, `mcp_oauth_grant` would be unselectable in practice and
`no_auth_public_documentation` would be the only usable mode.

**Why this is not blocking.** The contract outcome is deterministic and
fail-closed in every case: a tool-targeted grant resolves (scenario 17) and a
provider-targeted grant denies (scenario 18). The consequence is an
availability question for a tool that is neither connected nor authorized, not
an ambiguity an implementer must adjudicate. It should be settled before any
MCP phase advance under Gateway §21.3.

## 34. Finding counts

| Severity | Count | IDs |
| --- | --- | --- |
| P0 | **0** | — |
| P1 | **0** | — |
| P2 | **0** | — |
| P3 | **3** | `P3-401`, `P3-402`, `P3-403` |

Review 003 closure results: `P1-301` `CLOSED`; `P1-302` `CLOSED`; `P2-301`
`CLOSED`; `P3-301` `CLOSED`; `P3-302` `CLOSED`. Five of five closed; none
partially closed.

No previously closed Review 001, Review 002, or `P1-201` sub-defect was found
reopened. No capability, prohibition, risk-tier, approval, audit, verification,
containment, tenant-isolation, or external-content regression was found.

## 35. Gate decision

**`PASS_WITH_NON_BLOCKING_FINDINGS`.**

The decision follows mechanically from the criteria:

- P0 findings: 0. ✔
- P1 findings: 0. ✔
- All five Review 003 findings independently verified `CLOSED`. ✔
- `mellycore_operator` has exactly one deterministic runtime representation
  (Registry §7.5 → `required_acting_identity_type` → Gateway §9.2/§23/§17
  step 13 → audit §29.1). ✔
- No identity fallback is possible. ✔
- D4 can execute only through exact restricted-tool scope. ✔
- Provider-native scope is `not_applicable` only where a provider contract
  explicitly permits it — for Cloudflare, D4 alone. ✔
- Restricted-tool OAuth cannot become provider OAuth. ✔
- Every tested scenario has one deterministic result (24 of 24). ✔
- Adapter Scaffold can be designed without architectural interpretation. ✔
- Only P2 or P3 observations remain: three P3 observations, none of which makes
  scaffold design unsafe or ambiguous.

`PASS` is reserved here for a result with no residual observations. Three P3
observations remain, so the correct outcome under the stated criteria is
`PASS_WITH_NON_BLOCKING_FINDINGS`.

## 36. Adapter-scaffold eligibility

`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001` becomes **eligible for separate
Operator authorization, under the constraints below**. It is **not started, not
authorized, and not approved for execution.** Eligibility is not authorization,
and this review authorizes no scaffold work.

Documented constraints carried into any future scaffold authorization:

1. `P3-401` — treat Registry §7.5's raw text, not its rendering, as the
   canonical acting-identity vocabulary until the delimiter row is corrected.
2. `P3-402` — resolve capability fields by name, not by the §14.1 ordinal, and
   read §27.1 item 5 as referring to `scope_applicability` (field 15).
3. `P3-403` — do not assume an `mcp_oauth_grant` path is available for
   Cloudflare D4; `no_auth_public_documentation` is the only mode currently
   demonstrable, and any provider-targeted grant must deny.
4. The scaffold remains bound by Gateway Rule 32.1: no runtime-enablement gate
   currently passes, and the scaffold may not assert otherwise.

## 37. Exact next task

`MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-001`

Status: **eligible for separate authorization**, under the four constraints in
Section 36. It is not started, not authorized, not approved for execution, not
active, not implemented, and not enabled. Separate explicit Operator
authorization is required before any scaffold work begins.

The three P3 observations may be routed by that task or by a separate editorial
task at the Operator's discretion; none blocks scaffold design.

## 38. Explicit non-authorizations

This review authorizes none of the following, and none occurred: Adapter
Scaffold implementation or scaffolding; Registry, Gateway, or adapter
implementation; provider registration as a runtime grant; provider
authentication; credential creation, storage, rotation, reading, or
verification; any provider API call, including read-only calls; any MCP,
restricted-tool, or integration-fabric connection; any MCP execution; webhook
endpoint creation or registration; any change to any external system; any
dependency, lockfile, or workflow change; deployment, push, pull request,
merge, tag, or remote branch; or any MellyTrade, broker, trading, or
order-execution behavior.

No provider is connected, authenticated, credentialed, enabled, live, deployed,
or implemented. No restricted tool is connected. No credential exists in this
repository or its environment.

## 39. Validation evidence

| Command | Result |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` | `PASS MellyCore project scaffold validation passed`, exit code `0` |
| `git diff --check` | No output, exit code `0` |
| `git status --short` | Reported in the Review 004 task report |
| `git diff --name-only` | Reported in the Review 004 task report |
| `git diff --stat` | Reported in the Review 004 task report |
| `pytest` | `NOT_RUN` — not required for a documentation-only review; no dependency was installed |

| Metric | Value |
| --- | --- |
| Review 004 record sections | 41 |
| Reviewed documents | 20 (plus `SAFETY_CONTRACT.md` and `VALIDATION.md`) |
| Review 003 findings closed | 5 of 5 |
| Canonical acting-identity types | 3 |
| Canonical credential-profile classes | 9 |
| Authentication targets | 3 |
| Scope-applicability values | 3 |
| Cloudflare capability rows | 58 |
| Cloudflare prohibition rows | 13 |
| D4 capabilities | 3 |
| Deterministic scenarios replayed | 24 (24 deterministic, 0 indeterminate) |
| Findings: P0 / P1 / P2 / P3 | 0 / 0 / 0 / 3 |
| Introduced secret patterns | 0 |
| Changed files in this commit | 6 |

No unavailable or unrun validator is represented as passing.

## 40. Amendment and supersession

This record is append-only evidence of one independent review at one commit. It
may be superseded only by a later, explicitly identified review record that
references this file **by path** and states which sections it changes. A later
document that silently contradicts this record does not supersede it; such a
contradiction must be corrected.

This record amends no ADR, contract, provider pack, remediation report, or
earlier review record. Review 001, Review 002, and Review 003 remain immutable
historical evidence, and their blob IDs were re-verified unchanged.

## 41. References

### 41.1 Repository (canonical)

- `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md`
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_FABRIC_COMPARISON_SPEC_001.md`
- `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_001.md`
- `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_002.md`
- `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_003.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-002.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-003.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCUMENT-INTEGRITY-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-CREDENTIAL-CLASS-CONFORMANCE-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-RESTRICTED-TOOL-PATH-CONFORMANCE-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004.md`
- `shared_context/SAFETY_CONTRACT.md`, `shared_context/VALIDATION.md`,
  `shared_context/PROJECT_STATE.md`, `shared_context/ROADMAP.md`,
  `shared_context/RUN_QUEUE.md`, `shared_context/AGENT_HANDOFF.md`

### 41.2 External

None. No external documentation was fetched, no provider was contacted, and no
network call other than a read-only `git fetch clean-origin` was made during
this review.
