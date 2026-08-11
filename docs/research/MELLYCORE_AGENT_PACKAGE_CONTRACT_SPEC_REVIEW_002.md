# MellyCore Agent Package Contract Spec — Independent Review 002

## 1. Review identity

**Task ID:** MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002
**Reviews:** `MELLYCORE_AGENT_PACKAGE_CONTRACT_001`, **version 1.1**, as
remediated by `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001` at
commit `ad1d1fc7f947280fa55033629dc97c72eb022670`.
**Consumes:** `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001`
(`FAIL_REMEDIATION_REQUIRED`; P0 = 0, P1 = 1, P2 = 3, P3 = 3) and
`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001`
(`REMEDIATION_COMPLETE_UNVERIFIED`).
**Status:** Independent, read-only architecture, ownership, safety, and
consistency re-review. This record is a documentation artifact only; it
implements, connects, executes, or authorizes nothing.
**Gate decision:** `PASS_WITH_NON_BLOCKING_FINDINGS` (§22). P0 = 0 and
P1 = 0; all seven Review 001 findings are independently `CLOSED`; seven new
non-blocking findings are recorded (three P2, four P3).

This review did not accept the remediation report's assertions. Every
finding disposition below was re-derived from the committed specification
text and from the canonical owner documents directly.

## 2. Repository and baseline

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-package-contract-spec-remediation-001`
- Starting HEAD: `ad1d1fc7f947280fa55033629dc97c72eb022670` (short `ad1d1fc`)
- Latest subject at start: `docs: remediate agent package contract review findings`
- Starting worktree/index: clean (`git status --short` empty)
- Upstream tracking for the starting branch: **none**
- Configured remotes: `origin`, `clean-origin` (neither contacted)
- Review branch created from that exact HEAD:
  `docs/mellycore-agent-package-contract-spec-review-002`
- **No network operation occurred at any point in this review** — no fetch,
  pull, push, or remote access. The reviewed commit was already local.

Identity-gate result: every required baseline matched. The review-002 branch
did not previously exist and was created fresh from `ad1d1fc`.

### 2.1 Remediation commit under review

`ad1d1fc7f947280fa55033629dc97c72eb022670`, parent
`f8b465bd7744343a2a3ee8e294117d1409b42437` (`docs: review agent package
contract`), the sole commit on the remediation branch. It changed exactly
eight files: the reviewed specification, the remediation task report, and
the six canonical state documents. The full specification diff was read in
its entirety before any conclusion was drawn.

## 3. Reviewed artifact and version

`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md`, version **1.1**,
1,075 lines, 29 sections (§1–§29). The document's own header correctly
records that version 1.1 is unverified, that the gate remains
`FAIL_REMEDIATION_REQUIRED` pending this review, and that the document is
**not accepted** — no re-claim of a passed gate was found anywhere.

Also read in full as context, not as authority:
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` (original task
report), `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md`
(Review 001 record, 708 lines),
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md`, and
`docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`
(285 lines).

## 4. Review methodology

1. Read-only repository identity gate before any mutation (branch, full and
   short HEAD, subject, clean worktree, remotes, upstream absence, artifact
   existence, next-task pointer).
2. Immutable baselines recorded as Git blob IDs (§6) before any edit.
3. Review branch created from the verified commit.
4. The complete remediated specification read end to end — not only the
   sections the seven findings touched.
5. The complete remediation diff (`ad1d1fc^..ad1d1fc`) read line by line, so
   that what actually changed governs, not what was reported to have changed.
6. Every Review 001 finding re-read from the review record's own §32 and
   independently re-tested against the current specification text.
7. Every load-bearing owner citation re-verified against the owner document
   directly — in particular Control Plane §7.1's typed-domain-field
   allowance, on which the entire P1 remediation depends.
8. Every occurrence of `Provider Registry`, `lifecycle_status`,
   `evidence_state`, `approval_state`, and `run_state` audited in context.
9. Every self-reported count in the specification's §1.4 recomputed directly
   from its cited section.
10. Every `[[wikilink]]` resolved against the filesystem.
11. Severity assigned strictly by the repository's existing taxonomy
    (P0/P1/P2/P3) and gate names (`PASS`,
    `PASS_WITH_NON_BLOCKING_FINDINGS`, `FAIL_REMEDIATION_REQUIRED`) as
    already used by Review 001 §34 and Agent Runtime Review 002 §36. No
    replacement taxonomy was invented.
12. Nothing found wrong was repaired. The reviewed specification was not
    edited.

## 5. Canonical owner map

Rebuilt from the owner documents directly, then compared against the
specification's claims.

| Concern | Canonical owner | Agent Package Contract claim | Review method | Result |
| --- | --- | --- | --- | --- |
| Agent Runtime architecture, agent/run identity, package/runtime separation states | `MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001` | Consumes verbatim; supplies the package-side declarations Runtime §10 reserved | Runtime §9 row 3 read directly: "Package verified … Owner: **Future Agent Package Contract**" | ✅ Self-claim matches the owner's own reservation |
| Control Plane six status dimensions and entity contract | `MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC` §7.1, §8.1 | Package lifecycle and Package Trust State are typed entity data under §7.1's allowance; **no projection defined** onto any §8.1 dimension | CP §7.1 lines 228–230 read verbatim; CP §8.1's six dimensions and closed enums read in full | ✅ Quote is verbatim, correctly scoped, and literally names "trust" |
| Provider Registry: provider authorization facts, credential classes, MCP server registration | `MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001` §21.1, §24 | Referenced only; MCP Declarations carry `mcp_server_id` + `tool_contract_revision` | All 17 `Provider Registry` occurrences audited in context; §24.3 read in full | ✅ No ownership transferred (one editorial residue — `NEW-P3-01`) |
| Integration Gateway: capability resolution, policy order, approval binding, MCP security, error-taxonomy pattern | `MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001` §12, §17, §18, §21, §25 | Consumed unchanged; package capability declarations are requests only | Gateway §12.1 "One capability, one bounded operation" located and confirmed | ✅ Referenced, never redefined |
| Shared Context admission, provenance, sensitivity | `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001` | §15's eight rules bound what may be proposed, never how it is admitted | §15 unchanged by remediation (diff confirms); Review 001 found no finding | ✅ Unweakened |
| Package validation and safety boundaries ("Package verified") | **This Agent Package Contract** | Owns the validation-layer vocabulary (§18) | Runtime §9 row 3 names this contract as owner | ✅ Correctly self-claimed |
| Command namespace ownership and activation | **Future Command Registry** (§26 item 5) | This contract fixes pre-registration rejection rules only (§14.1 rule 7) | §14.1 rule 7 read; `ROADMAP.md`'s "Planned Commands" reservation (20 names) verified to exist | ✅ Boundary held (one completeness gap — `NEW-P2-03`) |
| Dependency evaluation and `DEPENDENCY_UNRESOLVED` | **This Agent Package Contract** (§18.1 layer 4) | Exclusive owner of the determination; Runtime consumes, never re-derives | §12.2 rules 1–5 and §18.1 layers 3–4 read together for a single consistent reading | ✅ Deterministic |
| Provenance and trust vocabulary | **This Agent Package Contract** (§19), built on Runtime §10.1's `package_provenance` | No second provenance field; no signing mechanism claimed | §19.1–§19.2 read; §7.1 `publisher_or_origin` "never a trust grant by itself" | ✅ No overclaim |
| Observability information architecture | `MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC` (dimensions) + this contract (§20 package fields) | Package-typed fields labeled as package-domain data | §20.1's eleven projections enumerated; §20.2 read | ⚠ Package lifecycle state has no §20.1 field — `NEW-P2-01` |
| Batch Orchestration | Future, separate task; consuming surface Control Plane §9.8 | Package-side eligibility declarations only (§23) | §23's seven declarations read; unchanged by remediation | ✅ No authorization granted |
| Versioning and compatibility | **This Agent Package Contract** (§22) | `package_version` and `contract_version` are independent | §22 rules 1–7 read against the v1.1 header | ⚠ Self-contradictory version identity — `NEW-P2-02` |

No concern was found with two incompatible canonical owners. No ownership
conflict was introduced by the remediation.

## 6. Immutable-source baseline

Recorded as Git blob IDs at review start, before any edit.

### 6.1 Reviewed subject and review evidence (MUST NOT change)

| Blob ID | Path |
| --- | --- |
| `12b67752f041fef38d769221a2bd9a4df2891068` | `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (reviewed subject) |
| `9a392a730b345c14df4c184f65200beca0bfbea6` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md` |
| `69a8bcbe0ace5d3f7b46f2a5a46b438b5eb75f5d` | `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md` |
| `de318f4721f0552db871672746faf3ea776baa50` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md` |
| `2178bb0abc21a7556559861a6e6cec857509cbf1` | `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md` |

### 6.2 Canonical cross-check sources (MUST NOT change)

| Blob ID | Path | Matches Review 001 §7 baseline? |
| --- | --- | --- |
| `3e085f97141fc0cb505ab4d9a738592d7ca601f7` | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` | ✅ identical |
| `f35f0e157879322c9edbaf834043902579a6d98f` | `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` | ✅ identical |
| `fa90b65b4f91545550247d81fc181eb10cca942a` | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` | ✅ identical |
| `65192fa157b57a2a46768ceca4660aed1584f649` | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` | ✅ identical |
| `4ea189989665907b0b931c2a86dcc112285d69b8` | `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` | ✅ identical |
| `13b2df338ad53cff02eb236ba0d30d34cd35bf20` | `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` | ✅ identical |
| `0d2768be8d9ae19b5a14ce1c61441550081113e3` | `docs/decisions/MELLYCORE_ENTERPRISE_PROVIDER_ARCHITECTURE_ADR_001.md` | ✅ identical |
| `fb77b573c5351ddf4afab8ff6eb6580a2c39d3fc` | `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md` | ✅ identical |
| `e8f8961f5c1a12275527cc05c83c432c9312d0d6` | `shared_context/CONTEXT_GRAPH_SCHEMA.md` | ✅ identical |
| `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` | `shared_context/SAFETY_CONTRACT.md` | ✅ identical |

**Every canonical cross-check source is byte-identical to the baseline
Review 001 recorded before the remediation ran.** This is independent proof
— not a report assertion — that Remediation 001 edited no owner document to
make the specification pass.

### 6.3 State documents this review will edit

| Blob ID | Path |
| --- | --- |
| `ec25c9d9cdb1df4c510e730efbeecb289f053c19` | `shared_context/PROJECT_STATE.md` |
| `6f659841bdaf026beea1319d8e5c7ff7c4cbe926` | `shared_context/ROADMAP.md` |
| `b62a6e9718590b5b23d1e65dd42162abb950d061` | `shared_context/RUN_QUEUE.md` |
| `9a6c71badd56a7868a82a23ff90935c218e920ee` | `shared_context/AGENT_HANDOFF.md` |
| `7c3fc0c0ba257f85611ee179d259b277340c4d8f` | `shared_context/PROJECT_HISTORY.md` |
| `c7fc101c19e5eac8d0c094ca518ec2f294829d74` | `shared_context/TASK_INDEX.md` |

## 7. Review 001 finding verification matrix

| Finding ID | Claimed remediation | Independent verification | Disposition | Evidence |
| --- | --- | --- | --- | --- |
| `P1-01` (P1) | Exact-projection claim removed; lifecycle and trust state restated as typed entity data under Control Plane §7.1; any future projection requires a dedicated mapping contract or explicit CP amendment | Audited **every** occurrence of `lifecycle_status`, `evidence_state`, `approval_state`, `run_state` in the specification (lines 256, 671, 685, 692, 848, 1021). Each is either an explicit **denial** of projection or a non-collision statement. Zero surviving projection claims. The CP §7.1 allowance is quoted **verbatim** and is correctly scoped — CP literally names "trust" among the permitted typed domain fields. No Control Plane enum member was invented. CP spec byte-identical to baseline. The remediation adopted precisely shape (b) that Review 001 §36 itself named as an acceptable resolution. | **CLOSED** | Spec §4 (`Package Trust State`), §5 CP row, §16 stage 7 (renamed "Lifecycle rendering"), §17.1, §20.2; CP `MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` lines 228–230 and §8.1 |
| `P2-01` (P2) | All three cited locations rephrased as explicit non-normative analogies | Verified all three carry the disclaimer "modeled on, but not owned or governed by, Provider Registry §24.x … §24 does not itself extend to generic package …". Then audited **all 17** `Provider Registry` occurrences across 13 lines — beyond the three Review 001 named. None presents Provider Registry as owning package lifecycle, trust state, validation, dependency resolution, activation, command namespaces, runtime authorization, installation, or execution. | **CLOSED** (one adjacent editorial residue recorded as `NEW-P3-01`) | Spec §11.1 row 3, §16 stage 9, §17.3 rule 2; full occurrence audit §11 below |
| `P2-02` (P2) | Deterministic evaluation boundary: §18.1 layer 4 is the exclusive owner | Verified §12.2 rule 2 assigns exclusive ownership to layer 4, **explicitly excludes** layer 3 (reference validation resolves a target; it does not test constraint satisfiability) and **explicitly excludes** Runtime's §16 stage 5. Ordering is stated: dependency validation must reach a determination *before* Runtime §9 state 3 ("Package verified"), itself a precondition of states 4–9. Runtime **consumes**, never re-derives. Rule 3 (required → deny) and rule 4 (optional → narrows, never denies, never silently satisfied) are distinguished. Rule 1 states no installation, fetch, activation, or resolution is implied. §18.1 layers 3 and 4 agree with §12.2 and with §21's `DEPENDENCY_UNRESOLVED` trigger. | **CLOSED** | Spec §12.2 rules 1–5, §18.1 layers 3–4, §16 stage 5, §21 |
| `P2-03` (P2) | New normative §14.1 enumerated under §18.1 layer 1 | Verified §14.1 exists as normative text with seven rules covering: duplicate identifiers; duplicate aliases (and alias-vs-identifier); reserved MellyCore commands; already-authorized runtime namespaces; Unicode NFKC normalization-equivalent deception; protected safety/validation/approval/Git/provider/deployment classes; and package-local-declaration-is-not-activation. §18.1 layer 1 names the check explicitly with its error class. §14's Command row and §24's command-shadowing row both cross-reference §14.1. `ROADMAP.md`'s "Planned Commands" reservation (20 names, `/roadmap` included) verified to exist as a real target for rule 3. | **CLOSED** (rule 6's class set is undefined — recorded as `NEW-P2-03`) | Spec §14.1, §18.1 layer 1, §14 Command row, §24; `shared_context/ROADMAP.md` §"Planned Commands" |
| `P3-01` (P3) | `claude_code` row replaced with a substantive correspondence | Verified the row now states a five-way asset-type correspondence (Skill↔skill, Hook↔hook, Command↔slash command, Plugin↔plugin, MCP Declaration↔MCP server reference) framed as a "naming and shape parallel only", and explicitly states this contract's activation, permission, and validation boundaries govern **regardless of framework** and that "no Claude Code-native mechanism satisfies or bypasses any of them". This is substantive and **anti**-privileging: it is the only row that explicitly forecloses a native bypass. No seventh framework introduced; Runtime §11.1's closed set unchanged. | **CLOSED** | Spec §13.2 `claude_code` row; Runtime §11.1 |
| `P3-02` (P3) | Dedicated `COMMAND_NAMESPACE_COLLISION` error class added | Verified present in §21 with a precise trigger enumerating §14.1's seven rules, and cross-referenced from §14.1, §18.1 layer 1, and §24. Independently recounted §21: **16** table rows. §1.4 correctly updated 15 → 16. | **CLOSED** (§21's prose numeral not updated — `NEW-P3-02`) | Spec §21, §1.4, §14.1, §18.1, §24 |
| `P3-03` (P3) | `license_metadata` absence-handling moved from the §7.1 table cell into a §7.2 rule | Verified §7.1's cell now reads "License reference, where applicable (§7.2 rule 4)" and §7.2 rule 4 states the substance in the identical numbered-rule format as rules 1–3. Checked for scope creep: rule 4 adds "MUST NOT be treated as a validation, trust, or capability signal by any layer of §18 or §19" — this **bounds** existing layers rather than introducing a new requirement outside the contract's scope, and is consistent with §18/§19 as written. | **CLOSED** | Spec §7.1, §7.2 rule 4, §18.1, §19 |

**All seven Review 001 findings are independently `CLOSED`. The single P1 is
closed in full, not partially.** No finding was closed by assertion; each was
re-tested against the committed text.

## 8. New-finding inventory

### P0 — Critical

**None.** No direct credential or provider path, no cross-tenant execution
possibility, no canonical Shared Context mutation bypass, no authorization or
approval bypass, no secret exposure, no self-authorizing package permission,
and no unsafe consequential retry exists anywhere in the reviewed
specification.

### P1 — Blocking

**None.** No Review 001 P1 was falsely closed. No new ownership conflict was
introduced. No canonical owner document was edited. The specification remains
provider-agnostic and fail-closed throughout.

### P2 — Material, non-blocking

**`NEW-P2-01` — The P1 remediation redirects package-lifecycle rendering to
§20, but §20.1 defines no package-lifecycle-state field.**

- **Location:** §20.1 (the eleven package-level projections), with the
  dangling references at §16 stage 7 and §17.1.
- **Claim:** §17.1 states that "an implementer needing a cross-referenced
  view of package lifecycle alongside Control Plane's dimensions **MUST**
  treat package lifecycle state as its own independently rendered field
  (§20)". §16 stage 7 states the lifecycle state "is rendered for
  observability (§20) as its own typed field".
- **Canonical owner:** this Agent Package Contract (§5 — it owns its own
  observability information architecture in §20).
- **Why this is a defect:** §20.1's eleven projections are Package ID/version,
  framework projection, declared capabilities, allowed capabilities, denied
  capabilities, validation result, trust state, provenance, activation
  status, failure reason, and cost-attribution reference. **Package lifecycle
  state is not among them**, and §20.2 names only projections 6 (validation
  result) and 7 (trust state) as package-typed fields requiring package-domain
  labeling. Trust state was given a rendering home by the remediation;
  package lifecycle state was not. An implementer obeying §17.1's `MUST`
  therefore arrives at a section that does not define the field, and can
  comply only by inventing a twelfth projection (unauthorized here, and
  contradicting §1.4's count of 11) — or by falling back to a Control Plane
  dimension, which §17.1 prohibits absolutely.
- **Required correction:** either add package lifecycle state as an explicit
  §20.1 projection and update §1.4's "Observability projections" count from
  11 to 12; or restate §16 stage 7 and §17.1 to point at the owning follow-up
  (the "Package Lifecycle" contract, §26 item 9) rather than at §20.
- **Gate impact:** **non-blocking.** It fails closed — §17.1's prohibition on
  coercion into a Control Plane enum is absolute and does not depend on §20
  being complete — and it does not reopen `P1-01`'s ownership conflict, since
  no projection onto a canonical owner's vocabulary is reintroduced. It is a
  completeness gap inside this contract's own text.

**`NEW-P2-02` — §22 declares the contract version as "currently `1.0`" while
the document is version 1.1 and version 1.1 added mandatory rejection rules.**

- **Location:** §22 rule 2, against the document header ("**Version:** 1.1").
- **Claim:** "**`contract_version`** is the version of *this specification*
  (currently `1.0`) a package declares conformance to. A Package Validator
  MUST reject a package declaring an unrecognized `contract_version` with
  `CONTRACT_VERSION_INCOMPATIBLE`."
- **Canonical owner:** this Agent Package Contract (§22 owns its own
  versioning and compatibility contract).
- **Why this is a defect:** the remediation advanced the document from 1.0 to
  1.1 and, in doing so, added §14.1's seven mandatory structural rejections
  and a sixteenth error class — neither of which existed at 1.0. Under the
  document's **own** §22.4, "narrowing a previously permissive rule" is a
  breaking change requiring a new **major** `contract_version`; under §22.5,
  additive changes take a minor bump. The document performs neither analysis
  and leaves §22 rule 2 asserting 1.0. Consequently a package author cannot
  know which `contract_version` to declare, and §22 rule 2's own `MUST
  reject … unrecognized contract_version` rule operates over a recognized set
  the document never defines. §29 requires an amendment to recompute §1.4's
  metrics (which was done) but the contract-version consequence was not
  addressed. Review 001 §27 had verified this statement as consistent
  precisely because the header then read 1.0; the remediation invalidated
  that consistency without restating the rule.
- **Required correction:** state which `contract_version` version 1.1
  corresponds to, and classify the §14.1 addition explicitly against §22.4
  and §22.5; or state expressly that `contract_version` remains `1.0` and
  explain why newly mandatory rejection rules are not a narrowing.
- **Gate impact:** **non-blocking.** No package, validator, or registry
  exists; nothing is granted or authorized by the inconsistency; the
  specification claims no implementation. Classified P2 by direct analogy to
  Review 001's own `P2-02`, which likewise treated a contract-level ambiguity
  with implementation implications as material but non-blocking.

**`NEW-P2-03` — §14.1 rule 6 imposes an absolute, non-liftable prohibition
over a set of "protected command classes" that no document enumerates.**

- **Location:** §14.1 rule 6.
- **Claim:** "No declared command identifier or alias MUST match, alias, or
  shadow a command in the safety, validation, approval, Git, provider, or
  deployment classes, regardless of tenant or environment authorization
  state — this prohibition is absolute and MUST NOT be lifted by any
  package-level declaration, capability, or approval."
- **Canonical owner:** this Agent Package Contract for the pre-registration
  rejection rule (§14.1); the future Command Registry (§26 item 5) for full
  namespace policy.
- **Why this is a defect:** rules 3 and 4 are deterministically evaluable —
  rule 3 against `ROADMAP.md`'s explicit twenty-name "Planned Commands"
  reservation, rule 4 against the Operator-authorized namespaces for a
  tenant and environment. Rule 6 instead names **six command classes that
  are defined nowhere** — not in this contract, not in `ROADMAP.md`, and not
  in any cited owner document. `ROADMAP.md`'s reserved list contains
  plausible members (`/validate`, `/security`, `/provider`, `/review`) but
  publishes no class taxonomy and no mapping from name to class. A validator
  cannot deterministically evaluate an absolute `MUST` over an unenumerated
  set, and the resulting indeterminacy is not uniformly fail-closed: an
  implementer uncertain whether a given name belongs to "the deployment
  class" may under-reject a genuinely protected name. This partially weakens
  the strongest rule of the `P2-03` remediation.
- **Required correction:** enumerate the six protected command classes (or
  cite an owner document that does); or reduce rule 6 to a deterministic
  superset of rules 3–4 and defer the class taxonomy explicitly to the future
  Command Registry.
- **Gate impact:** **non-blocking.** Rules 1–5 already carry the
  command-shadowing threat deterministically, `COMMAND_NAMESPACE_COLLISION`
  exists as a stable rejection identity, nothing is granted, and no
  namespace ownership is conferred (rule 7 holds).

### P3 — Editorial / maintainability

**`NEW-P3-01` — §17.3 rule 1 retains a bare "mirroring Provider Registry"
analogy while its three sibling analogies carry explicit non-normative
disclaimers.** *(The special review target named by Remediation 001 §15.2.)*

- **Location:** §17.3 rule 1.
- **Claim:** "`retired` is terminal: a retired `package_revision_id` is never
  reused (mirroring Provider Registry §24.3's `provider_id` rule)."
- **Independent assessment.** Three questions were tested separately:
  1. **Is it technically accurate?** Yes. Provider Registry §24.3's own
     retirement row reads "`retired` | Not registrable; `provider_id` never
     reused; historical audit records are never deleted." The analogy is
     factually correct.
  2. **Is it an ownership overreach?** **No.** The rule itself is stated as
     this contract's own rule about `package_revision_id`; §5 unambiguously
     assigns package lifecycle to this contract; the parenthetical claims
     only a parallel, not a source of authority. Provider Registry is not
     presented as governing package retirement, and nothing is granted.
  3. **Is it a contradiction with the remediation?** **No** — but it is
     **inconsistent treatment of one citation class within one document.**
     §11.1 row 3, §16 stage 9, and §17.3 rule 2 each received an explicit
     "modeled on, but not owned or governed by" disclaimer; §17.3 rule 1,
     two lines above rule 2 and in the same rule list, did not.
- **Verdict:** a **new P3**, not a P1 or P2. It is the weaker "mirroring"
  phrasing rather than the "reused" phrasing Review 001's `P2-01` actually
  objected to, and it transfers no ownership. Remediation 001 §15.2
  deliberately left it as out of scope, which was a defensible reading of a
  remediation brief; this review flags it because Review 001's silence is not
  a reason to leave a known inconsistency unrecorded.
- **Required correction:** apply the same non-normative parenthetical used at
  §11.1 row 3, §16 stage 9, and §17.3 rule 2.
- **Gate impact:** non-blocking, editorial.

**`NEW-P3-02` — §21's prose numeral is stale: "Fifteen stable rejection
classes" against sixteen table rows.**

- **Location:** §21, opening sentence, against §21's own table and §1.4.
- **Why:** the remediation added `COMMAND_NAMESPACE_COLLISION` and correctly
  updated §1.4 from 15 to **16**, but did not update §21's lead sentence.
  Independent recount: §21's table contains **16** rows.
- **Note:** the specification's §27 acceptance criterion 14 still holds —
  it tests §1.4 against its cited sections, and §1.4's "16" matches the
  actual 16. The divergence is internal to §21.
- **Required correction:** "Sixteen stable rejection classes."
- **Gate impact:** non-blocking, editorial. Introduced by the remediation.

**`NEW-P3-03` — Five inverted normative modals in text added by version 1.1.**

- **Locations:** §14.1 rule 2 ("no alias **MUST** equal another command's
  primary identifier"), rule 3 ("No declared command identifier or alias
  **MUST** match any reserved operator command name"), rule 4 ("… **MUST**
  match a command namespace an Operator has already authorized"), rule 6 ("No
  declared command identifier or alias **MUST** match, alias, or shadow …");
  and §17.1 ("No package lifecycle state below **MUST** be silently coerced
  into … any Control Plane §8.1 enum value").
- **Why:** each intends a prohibition but is written as "No X MUST Y", which
  under RFC 2119 reads as "it is not required that X do Y" — the negation of
  the intended meaning. The correct form is "MUST NOT". §14.1 rules 1, 5, and
  7 use the correct form, so the defect is inconsistent within one
  subsection.
- **Mitigating fact:** the surrounding prose disambiguates intent ("**any**
  match denies the package at structural-validation time, before any other
  layer runs"), so the practical reading fails closed.
- **Required correction:** rewrite the five constructions as "MUST NOT".
- **Gate impact:** non-blocking, editorial. All five are in text introduced by
  the remediation.

**`NEW-P3-04` — Remediation 001's own Provider Registry audit undercounts the
occurrences it claims to have reviewed.**

- **Location:** `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`
  §13 item 7: "every Provider Registry reference in the corrected
  specification (**nine occurrences**) was reviewed".
- **Independent recount:** **17** occurrences of the string `Provider
  Registry` across **13** lines of the corrected specification.
- **Why recorded:** the audit's substantive conclusion nonetheless reproduces
  independently — this review re-audited all 17 and found no ownership
  transfer — so the discrepancy is a self-report accuracy issue, not a missed
  defect. It is recorded so that a future task does not inherit "nine" as a
  verified audit baseline.
- **Required correction:** none in the immutable remediation report; a future
  task citing this audit should use the recounted figure.
- **Gate impact:** none. This is a finding against review evidence, not
  against the specification.

## 9. P0/P1/P2/P3 counts

### 9.1 Review 001 findings, as re-verified by this review

| Severity | Count | IDs | Disposition |
| --- | --- | --- | --- |
| **P0** | 0 | — | — |
| **P1** | 1 | `P1-01` | `CLOSED` |
| **P2** | 3 | `P2-01`, `P2-02`, `P2-03` | all `CLOSED` |
| **P3** | 3 | `P3-01`, `P3-02`, `P3-03` | all `CLOSED` |
| **Total** | **7** | | **7 of 7 closed** |

### 9.2 New findings introduced by this review

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **0** | — |
| **P2** | **3** | `NEW-P2-01`, `NEW-P2-02`, `NEW-P2-03` |
| **P3** | **4** | `NEW-P3-01`, `NEW-P3-02`, `NEW-P3-03`, `NEW-P3-04` |
| **Total** | **7** | |

Six of the seven new findings are defects in text the remediation itself
introduced or should have updated; one (`NEW-P3-04`) is against the
remediation's own evidence rather than the specification.

## 10. Control Plane projection assessment

**Verdict: `P1-01` is genuinely and fully closed.**

Every reference in the specification to a Control Plane status dimension was
audited in context:

| Location | Text class | Assessment |
| --- | --- | --- |
| §4 `Package Trust State` | Explicit denial: "this contract defines **no projection** of Package Trust State onto `evidence_state`, `approval_state`, or any other Control Plane §8.1 dimension" | ✅ No claim |
| §5 Control Plane ownership row | Explicit denial for both lifecycle and trust state | ✅ No claim |
| §16 stage 7 | Renamed "Lifecycle **rendering**"; "**not** projected onto any Control Plane §8.1 dimension" | ✅ No claim (but see `NEW-P2-01`) |
| §17.1 | Explicit denial plus an absolute prohibition on silent coercion into any §8.1 enum value | ✅ No claim (but see `NEW-P2-01`) |
| §17.1, §27 criterion 6 | Non-collision statements against Runtime's seventeen `run_state` values | ✅ Legitimate, not a projection |
| §20.2 | Requires projections 6 and 7 to be labeled package-domain data, "never displayed as though they were a `lifecycle_status`, `evidence_state`, or `approval_state` value" | ✅ Strengthens the denial |

Specifically confirmed:

- The unsupported exact-projection claim is **removed**, not softened.
- Package lifecycle and Package Trust State are treated as **Agent Package
  domain concepts**, and the justifying allowance is quoted **verbatim** from
  Control Plane §7.1 — which literally enumerates "trust" among the domain
  fields that "remain typed entity data and are not additional status
  dimensions".
- **No new Control Plane enum value was invented** anywhere.
- **No package state is silently coerced** into an existing Control Plane
  value; §17.1 forbids it in terms.
- A **future explicit mapping contract or owner amendment is required**
  before any such projection may exist (§4, §17.1).
- **Control Plane ownership is unchanged** — proven by blob-ID identity
  (§6.2), not by assertion.

The remediation deliberately chose Review 001 §36's option (b) over option
(a). This review regards that as the stronger of the two available shapes,
because it resolves the finding with **zero** edits to any canonical owner.

## 11. Provider Registry scope assessment (including §17.3 rule 1)

All 17 occurrences across 13 lines were audited, not only the three Review
001 named.

| Line | Location | Character of the reference | Assessment |
| --- | --- | --- | --- |
| 203 | §3 precedence chain | Names the Provider Registry contract as a higher rung | ✅ Correct |
| 246 | §4 `Provider Adapter` | References the existing Provider Registry/Gateway track | ✅ Correct |
| 251 | §4 `MCP Declaration` | Reference to an already-registered §24 record; "never registers, re-registers, or redefines" | ✅ Correct |
| 258 | §4 `Provider Pack` | Disambiguates an unrelated concept | ✅ Correct |
| 411 | §9 manifest relationships | MCP Declarations reference registered §24 records only | ✅ Correct |
| 458 | §11.1 row 3 (shell execution) | Explicit non-normative disclaimer | ✅ `P2-01` corrected |
| 460 | §11.1 row 5 (provider access) | Cites Provider Registry's eight facts (§21.1) — genuinely PR-owned | ✅ Correct |
| 464 | §11.1 row 9 (MCP access) | Cites §24 registration — genuinely PR-owned | ✅ Correct |
| 567 | §14 MCP Declaration row | Ownership explicitly attributed to §24 and Gateway §21 | ✅ Correct |
| 673 | §16 stage 9 | Explicit non-normative disclaimer | ✅ `P2-01` corrected |
| 729 | **§17.3 rule 1** | Bare "(mirroring Provider Registry §24.3's `provider_id` rule)" | ⚠ `NEW-P3-01` |
| 733 | §17.3 rule 2 | Explicit non-normative disclaimer | ✅ `P2-01` corrected |
| 994 | §26 item 7 | Server registration remains Provider Registry §24's | ✅ Correct |

**Provider Registry is nowhere presented as owning** package lifecycle,
package trust state, package validation, dependency resolution, package
activation, command namespaces, runtime authorization, package installation,
or package execution. Every analogy is either explicitly non-normative or
technically accurate and non-transferring.

**§17.3 rule 1 — explicit determination.** It is **not** an ownership
overreach, **not** a contradiction with the remediation, and **not** a P1 or
P2. It is a **valid, technically accurate, non-normative analogy that is
inconsistently formatted relative to its three siblings**, recorded as
`NEW-P3-01`. It was assessed independently and on its merits, not dismissed
because Review 001 failed to name it.

## 12. Dependency evaluation assessment

**Verdict: `P2-02` closed; the boundary is deterministic.**

| Requirement | Location | Result |
| --- | --- | --- |
| One deterministic validation stage owns the finding | §12.2 rule 2; §18.1 layer 4 | ✅ Layer 4 is named the **exclusive** owner; layer 3 and Runtime §16 stage 5 are each explicitly excluded |
| Required and optional dependencies distinguished | §12.2 rules 3–4 | ✅ Required denies; optional narrows the feature set |
| Evaluation happens before activation eligibility | §12.2 rule 2 | ✅ Must reach a determination before Runtime §9 state 3, a precondition of states 4–9 |
| Runtime consumes rather than re-deriving | §12.2 rule 2 | ✅ "does **not** independently re-derive, re-evaluate, or override" |
| Unresolved required dependencies block eligibility | §12.2 rule 3 | ✅ Denies package verification; no deferral to a later stage |
| Optional dependencies never silently become active | §12.2 rule 4 | ✅ "MUST NOT be silently treated as present, active, or satisfied" |
| No dependency is automatically installed | §12.2 rule 1 | ✅ "defines no dependency-installation or dependency-resolution mechanism" |
| Validation does not imply execution authorization | §18.2 | ✅ Passing all nine layers establishes only Runtime §9 state 3 |
| Error taxonomy and validation layers agree | §21 `DEPENDENCY_UNRESOLVED` ↔ §18.1 layer 4 ↔ §12.2 | ✅ Consistent; `REFERENCE_UNRESOLVED` correctly maps to layer 3 instead |

No residual ambiguity between this contract's validation time and the Agent
Runtime's instantiation-eligibility time remains.

## 13. Command-shadowing assessment

**Verdict: `P2-03` and `P3-02` closed; one completeness gap recorded.**

| Required coverage | §14.1 rule | Result |
| --- | --- | --- |
| Duplicate command IDs | 1 | ✅ |
| Duplicate aliases | 2 | ✅ (also forbids alias-equals-identifier) |
| Reserved MellyCore commands | 3 | ✅ Target verified to exist: `ROADMAP.md`'s twenty-name "Planned Commands" reservation, `/roadmap` included |
| Active runtime namespace collisions | 4 | ✅ Scoped to tenant and environment, package-of-origin irrelevant |
| Unicode / normalization-equivalent deception | 5 | ✅ NFKC normalization required before comparison |
| Overriding safety or approval commands | 6 | ⚠ Absolute prohibition, but over an unenumerated class set — `NEW-P2-03` |
| Git, provider, deployment, validation, security command protection | 6 | ⚠ Same |
| Package-local declaration vs environment-wide activation | 7 | ✅ Declaration is a reference candidate only; confers no namespace ownership |
| Future Command Registry ownership boundary | 7 + §26 item 5 | ✅ Explicitly reserved to the registry |
| Stable rejection / error class | §21 `COMMAND_NAMESPACE_COLLISION` | ✅ Dedicated class, cross-referenced from §14.1, §18.1 layer 1, and §24 |

Enumeration under §18.1 layer 1 is explicit, so a future Package Validator
cannot miss the check — which was the substance of `P2-03`.

## 14. P3 assessment

| Review 001 finding | Verified remediation | Disposition |
| --- | --- | --- |
| `P3-01` — `claude_code` row was a thin restatement | The row now carries a genuine five-way asset-type correspondence **and** an explicit statement that this contract's activation, permission, and validation boundaries govern regardless of framework, with no Claude Code-native bypass. Substantive, and the opposite of a privileged special case. | `CLOSED` |
| `P3-02` — no dedicated error class for command collision | `COMMAND_NAMESPACE_COLLISION` added to §21 with a precise trigger and three cross-references. Verified from the review record's own §32 text, not inferred from the remediation report. | `CLOSED` |
| `P3-03` — `license_metadata` absence-handling in prose rather than the rule format | Moved into §7.2 rule 4 in the identical numbered-rule format as rules 1–3. Checked for scope creep: the added clause bounds §18 and §19 rather than creating a new requirement outside the contract. | `CLOSED` |

## 15. Full-contract safety assessment

Reviewed beyond the seven prior findings.

**Package boundary (§6.2).** All seven prohibitions intact and unchanged by
the remediation: embedded secrets; provider credentials; `.env` and Safety
Contract blocklist patterns; undeclared executable payloads; hidden network
dependencies; unbounded filesystem access; self-authorized runtime
permissions. Violation denies with `PACKAGE_BOUNDARY_VIOLATION` **before any
other check runs**. Path traversal is separately named (§24, "Filesystem
escape"). Activation is nowhere implied by installation — §17.1 state 8 is
`installed_reference` and §17.3 rule 3 states no lifecycle state authorizes
execution.

**Capability model (§10.1).** The five states — declared, runtime-supported,
policy-allowed, Operator-approved, active — remain independently established,
with §10.2 rule 1 requiring **all five simultaneously** for one exact
revision, tenant, environment, and run, and rule 3 requiring the
**intersection, never the union**. No stage collapses into another. The
remediation did not touch §10.

**Asset types (§14).** All five rows retain all six required columns
(declarative purpose, ownership boundary, validation expectation, activation
boundary, security implications, future registry). Prompts, runtime adapters,
and provider adapters are bounded in §4 and §8.1 as reference targets only.

**Shared Context (§15).** Unchanged by the remediation (confirmed from the
diff). Asset content bodies may never be admitted; only identity, validation
results, trust state, and provenance references may, and only through the
existing admission gate. `source_refs` back to the exact `package_revision_id`
is required. Writes remain proposal-only (rule 5); an out-of-class proposal
is denied `CONTEXT_CLASS_UNDECLARED` **before** reaching the admission gate
(rule 7); rule 8 forecloses any package-scoped shortcut. No undeclared
mutation path exists.

**Runtime (§16).** All nine stages remain distinct concepts — discovery,
validation, compatibility projection, policy evaluation, instantiation
eligibility, activation gating, lifecycle rendering, observability
projection, termination/suspension projection. Stage 6 alone gates whether a
run may begin, and it is owned entirely by the already-accepted Agent Runtime
architecture. No parallel authorization path is created.

**Trust and provenance (§19).** `validated ≠ trusted` (§18.2 establishes only
Runtime §9 state 3); `trusted ≠ executable` (§17.3 rule 3); origin categories
grant nothing (§7.1 `publisher_or_origin` is "never a trust grant by
itself"); generated and first-party packages are not implicitly authorized
(§19.1 rows 2 and 5, plus §19.2's default); and **cryptographic signing is
explicitly not claimed to exist** (§19.2) — every package is at best
`unsigned_or_unverified` in the cryptographic sense.

## 16. Provider-agnostic compatibility assessment

**Verdict: the specification remains provider-agnostic and fail-closed.**

§13.1 selects `framework_type` from Runtime §11.1's six-member closed set
(`claude_code`, `openai_agents_sdk`, `langgraph`, `crewai`, `autogen`,
`mellycore_custom`); **no seventh value is added** and no framework-specific
ownership is created. §13.2's six rows were checked for asymmetric privilege:
after the `P3-01` correction, the `claude_code` row is now the **most**
constrained of the six, because it alone explicitly forecloses a
framework-native bypass ("no Claude Code-native mechanism satisfies or
bypasses any of them"). §13.2's header still labels the table "illustrative
structure, not a verified capability test", and §13.1 preserves Runtime
§11.3's "architectural planning position" caveat unchanged rather than
upgrading it. The closing line — "No row above is implemented, verified, or
authorized to be implemented by this document" — is intact.

## 17. Shared Context and Runtime boundary assessment

Covered in §15 above. Both boundaries hold. Neither was weakened by the
remediation; §15 was not edited at all, and §16's only change (stage 7's
rename from "Lifecycle projection" to "Lifecycle rendering") **strengthens**
the boundary by removing the projection language `P1-01` objected to.

## 18. Runtime boundary assessment

The nine-stage separation of §16 remains 1:1 consistent with Runtime §9's
package/runtime separation states, with stage 9 explicitly new and explicitly
attributed to a future owner. No stage claims an authorization Runtime §14's
eleven facts do not already gate. `Package Instance` (§4) remains explicitly
distinct from Runtime's `runtime_instance_id`.

## 19. Batch compatibility assessment

**Verdict: batch compatibility grants no batch authorization.**

§23 was not modified by the remediation and re-verified in full. Its opening
sentence states that Batch Orchestration "is not specified, implemented, or
authorized by this document", and the consuming surface remains Control Plane
§9.8, unchanged. All seven package-side declarations are present: isolated
execution eligibility; **explicit** writable-file ownership (an unbounded
claim fails §18.1 layer 7); exhaustively declared side effects; bounded
resource requirements (a floor, never a ceiling); validation command
references (a pointer, never the validator); integration ownership reserved
to Batch Orchestration's own future contract; and item 7's explicit "**No
implicit PR, push, merge, or deployment permission**", cross-referenced to
§11.1 rows 6, 7, and 12.

Confirmed: package compatibility with a future `/batch` workflow grants
**none** of parallel execution, worktree creation, file mutation, push, PR
creation, merge, or deployment.

## 20. Metrics and self-report verification

Every count in §1.4 was recomputed directly from its cited section.

| Dimension | Claimed (§1.4) | Independently recounted | Result |
| --- | --- | --- | --- |
| Specification sections | 29 | 29 (§1–§29) | ✅ |
| Terminology entries | 21 | 21 | ✅ |
| Architectural ownership rows | 13 | 13 | ✅ |
| Prohibited package contents | 7 | 7 | ✅ |
| Package identity fields | 12 | 12 | ✅ |
| Reused Agent Runtime package-metadata fields | 18 | 18 | ✅ |
| Asset categories in the layout model | 9 | 9 | ✅ |
| Manifest relationship rows | 6 | 6 | ✅ |
| Capability states | 5 | 5 | ✅ |
| Permission/approval categories | 12 | 12 | ✅ |
| Framework compatibility rows | 6 | 6 | ✅ |
| Asset-type boundary rows | 5 | 5 | ✅ |
| **Command collision-detection rules** (new in v1.1) | 7 | 7 | ✅ |
| Shared Context rules | 8 | 8 | ✅ |
| Runtime-interaction stages | 9 | 9 | ✅ |
| Package lifecycle states | 11 | 11 | ✅ |
| Validation layers | 9 | 9 | ✅ |
| Trust-state categories | 7 | 7 | ✅ |
| Observability projections | 11 | 11 | ✅ (but see `NEW-P2-01` — the set is complete as counted, yet omits the field §17.1 requires) |
| **Error/rejection classes** | **16** | **16** | ✅ §1.4 correct — **but §21's own prose still says "Fifteen"** (`NEW-P3-02`) |
| Batch eligibility declarations | 7 | 7 | ✅ |
| Security threats | 12 | 12 | ✅ |
| Non-goals | 12 | 12 | ✅ |
| Follow-up contracts | 12 | 12 | ✅ |
| Acceptance criteria | 14 | 14 | ✅ |

**All 25 §1.4 rows reproduce exactly.** The remediation's claim to have
recomputed the metrics table is independently confirmed. The one numeric
defect found is outside §1.4, in §21's prose.

Other self-reports checked:

| Self-report | Source | Independent result |
| --- | --- | --- |
| "nine occurrences" of Provider Registry references audited | Remediation report §13 item 7 | **17 occurrences across 13 lines** — discrepancy recorded as `NEW-P3-04` |
| Exactly eight files changed | Remediation report §12 | ✅ Confirmed: `git diff --stat ad1d1fc^ ad1d1fc` lists exactly those eight |
| Canonical owner documents unedited | Remediation report §14 | ✅ Confirmed independently by blob-ID identity against Review 001's own recorded baselines (§6.2) |
| §27 acceptance criterion 14 (metrics match) | Specification §27 | ✅ Holds |

## 21. Overclaim review

The specification and this review's own diff were scanned for `implemented`,
`available`, `enabled`, `installed`, `operational`, `executable`,
`production-ready`, `supported`, `accepted`, `approved`, `passed`, `live`,
and `deployed`. Every hit in the specification is one of: a negated claim
(`NOT_IMPLEMENTED`, `NONE_EXIST`, "Zero"); a reused field or state name
already fixed by an owner (`supported_environments`, `installed_reference`,
`runtime-enabled`, `Operator-approved`, `policy-allowed`); or explicit prose
stating the gate remains failed and the document is **not accepted**.

Specifically confirmed in the reviewed specification:

- §1.2's implementation-state table records `NOT_IMPLEMENTED` /
  `NONE_EXIST` / "**Zero.**" for every dimension, and states that no row may
  be advanced by a documentation task.
- The header states version 1.1 "does not re-open or re-claim a passed gate".
- §1.3 confirms migration triggers #1, #4, #5, #6, and #7 remain uncrossed.
- The global higher-priority pointer
  `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is neither reordered
  nor reinterpreted (§1.1).

No overclaim was found in the specification. This review's own record and
state-synchronization text were written to the same standard: acceptance is
recorded as **documentation acceptance under recorded non-blocking
constraints**, and every non-existent capability is stated as non-existent.

## 22. Gate decision

### `PASS_WITH_NON_BLOCKING_FINDINGS`

Derived from the findings, using the repository's existing gate taxonomy and
the rule Review 001 §34 stated and Agent Runtime Review 002 §36 applied:
**any P0 or P1 blocks; `PASS` requires zero new findings; new non-blocking
findings yield `PASS_WITH_NON_BLOCKING_FINDINGS`.**

Each condition was tested independently and each is met:

1. **P0 = 0** — no critical safety or integrity failure exists.
2. **P1 = 0** — no blocking architectural, ownership, or contract failure
   exists.
3. **No Review 001 finding is falsely closed.** All seven are `CLOSED`
   against the committed text, with `P1-01` closed **in full** by removing
   the claim rather than partially by softening it.
4. **No new ownership conflict was introduced.** The canonical owner map
   (§5) resolves to exactly one owner per concern, and every canonical
   cross-check source is byte-identical to Review 001's recorded baseline
   (§6.2) — the remediation changed no owner document to make this
   specification pass.
5. **The specification remains provider-agnostic and fail-closed** (§16, §15).
6. **The safety distinctions hold** — `specified ≠ implemented`,
   `declared ≠ authorized`, `validated ≠ trusted`, `validated ≠ executable`,
   `compatible ≠ enabled`, `available ≠ permitted`, `installed ≠ activated`,
   `package-local state ≠ Control Plane state`, `package lifecycle ≠ live
   agent run state`, `dependency declaration ≠ dependency installation`,
   `command declaration ≠ command activation`, `command declaration ≠
   namespace ownership`, `batch compatibility ≠ batch authorization`,
   `review pass ≠ runtime implementation`.

The outcome is `PASS_WITH_NON_BLOCKING_FINDINGS` rather than `PASS` **solely**
because this review introduced seven new findings (three P2, four P3). The
distinction is recorded honestly rather than resolved in the remediation's
favour. Neither `PASS` nor `FAIL_REMEDIATION_REQUIRED` is available on this
evidence: no P0 or P1 exists to force a fail, and new findings exist that
forbid an unqualified pass.

The decision was **not** reached by accepting Remediation 001's claim that
all findings are resolved, and **not** by treating validator success as proof
of architectural correctness. `py -3.9 scripts/validate_project_state.py`
passing proves only that repository scaffolding is well-formed; it proves
nothing about ownership, projection, or contract consistency, and no
architectural conclusion in this record rests on it.

## 23. Specification acceptance and required follow-up

### 23.1 Acceptance

`MELLYCORE_AGENT_PACKAGE_CONTRACT_001`, version **1.1**, is **accepted as a
documentation contract** for the Agent Package track, under the seven
non-blocking constraints recorded in §8.

Acceptance is of a **documentation contract only**. It establishes what a
future Agent Package must satisfy. It does **not** establish that any of the
following exists, and none does: an Agent Package Store, a Package Registry,
an Agent Registry, a Package Validator, a package loader, any Agent Package,
any package installation, any package execution, any command, hook, plugin,
or MCP execution, any batch execution, any runtime, any provider connection,
any credential, or any deployment.

### 23.2 Required follow-up

The three P2 findings require correction before, or as part of, the first
follow-up contract that depends on the affected section. None blocks this
gate, and none is authorized to begin by this review.

| Finding | Must be corrected before | Reason |
| --- | --- | --- |
| `NEW-P2-01` (no §20.1 lifecycle field) | any observability or Package Lifecycle follow-up contract (§26 item 9) | §17.1's `MUST` currently resolves to a section that does not define the field |
| `NEW-P2-02` (contract-version contradiction) | any Package Validation follow-up contract (§26 item 8) | a validator cannot implement §22 rule 2's reject-unrecognized rule over an undefined recognized set |
| `NEW-P2-03` (undefined protected command classes) | the Command Registry contract (§26 item 5) | an absolute `MUST` over an unenumerated set is not deterministically evaluable |

The four P3 findings (`NEW-P3-01` through `NEW-P3-04`) are editorial and may
be closed in any future amendment to the specification, which under §29 must
be additive and must recompute §1.4's metrics. They are **not** discarded:
each is recorded here with a location and a required correction.

## 24. Acceptance limitations

1. This review is a **documentation review**. It verifies internal
   consistency, ownership attribution, fail-closed discipline, and
   cross-reference integrity. It does not and cannot verify runtime
   behavior, because no runtime, package, registry, validator, or loader
   exists.
2. **Validator success proves nothing architectural.** The project-state
   validator checks repository scaffolding only.
3. Acceptance is **bounded by the seven non-blocking findings** of §8, which
   remain open and are not waived by this gate.
4. This review **does not authorize any downstream implementation task**. The
   next task named in §25 is identified from the canonical queue only; it is
   neither started nor authorized here, and it requires its own separate
   explicit Operator authorization.
5. The Agent Runtime architecture gate (Review 002,
   `PASS_WITH_NON_BLOCKING_FINDINGS`) is **not reopened**. Review 001's
   `FAIL_REMEDIATION_REQUIRED` remains historically recorded as failed;
   this gate supersedes it prospectively, not retroactively.
6. The global higher-priority pointer
   `MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
   reordered, and not reinterpreted by this review.
7. Migration trigger #6 ("first execution-capable agent") remains uncrossed,
   as do triggers #1, #4, #5, and #7. Any task that would make an agent
   execution-capable additionally requires Model B reconsideration.
8. `pytest`, Black, flake8, and mypy were **`NOT_RUN`** — no source or test
   file was changed by this review. They are not claimed passing.

## 25. Exact next task

From the canonical `shared_context/RUN_QUEUE.md`, the next item in the Agent
Package track's recommended order after
`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002` is the **Framework Bridge
Contract**, followed by Shared Context Bridge, Agent Runtime Scaffold (inert),
Scaffold Review, first Agent Package, Cross-Agent Smoke (inert modes only),
Integration Review, and then the twelve named follow-up contracts of
specification §26.

Each remains **blocked**, requiring its own specification, independent
review, and separate explicit Operator authorization. **No queued task is
invented, activated, started, or authorized by this review.**

## 26. Implementation status (unchanged by this review)

| Dimension | State |
| --- | --- |
| Agent Package Store, Package Registry, Agent Registry, Package Validator, package loader | `NOT_IMPLEMENTED` |
| Agent Packages | `NONE_EXIST` |
| Package installations | `NONE_EXIST` |
| Packages executed | **Zero** |
| Skill, Hook, Command, Plugin, MCP registries | `NOT_IMPLEMENTED` |
| Command, hook, plugin, MCP execution | **None** |
| Batch execution | **None**; Batch Orchestration remains unspecified and unauthorized |
| Cryptographic package signing | `NOT_SPECIFIED`, `NOT_IMPLEMENTED` |
| Agent Runtime | Unchanged; still `NOT_IMPLEMENTED`; its Review 002 gate is not reopened |
| Control Plane, Provider Registry, Integration Gateway, Shared Context contracts | Unchanged, byte-identical (§6.2) |
| Evidence class for every flow in the reviewed specification | `future_live` |

This review performed exactly one class of repository mutation: creating this
research record, its task report, and the bounded state-synchronization edits
named in the task report. No specification, source file, test, configuration,
workflow, registry, validator, loader, or execution mechanism was created,
modified, or executed.

## 27. Explicit non-authorizations

This review authorizes none of: any edit to the reviewed specification, its
task report, Review 001's artifacts, or the Remediation 001 report; any
Control Plane, Provider Registry, Agent Runtime, Integration Gateway, or
Shared Context amendment; any Agent Package Store, Package Registry, Agent
Registry, Package Validator, or loader implementation; any package, agent,
skill, command, hook, plugin, or MCP execution; any Batch Orchestration
implementation; any provider connection, credential configuration, or
model-provider call; any network operation; any push, pull request, merge,
remote branch, or deployment; any MellyTrade interaction.

## 28. Amendment and supersession

This review record is superseded only by a later, independently authored
review of a later version of the specification. It does not amend the
reviewed specification, any canonical owner document, or any prior review or
remediation record.

## 29. References

### 29.1 Reviewed

- `docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md` (version 1.1)
- `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REMEDIATION-001.md`

### 29.2 Prior gate evidence consumed

- `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_001.md`
- `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-001.md`
- `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001.md`

### 29.3 Canonical cross-check sources

Listed with blob IDs in §6.2.

### 29.4 External

None.
