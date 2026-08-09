# MellyCore Product Track Integration Plan 001

Task ID: `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-001`

Status: `PLAN_REMEDIATED_UNVERIFIED_INTEGRATION_NOT_AUTHORIZED`

Remediation: `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-001`
resolves the P1/P2 findings recorded durably in
`docs/research/MELLYCORE_PRODUCT_TRACK_INTEGRATION_PLAN_REVIEW_001.md` without
changing the 42-commit Product Track or any of its nine unit boundaries.

## 1. Purpose and authority boundary

This repository-owned plan converts the completed read-only Product Track
integration decision into a deterministic execution contract. It maps the exact
committed Product Track history from canonical baseline
`947f33d27d5546775186e96bdc61e30db78c0b3d` through local Product Track tip
`a0b70ae6c45c640ede4889abeb1f169e5b5a6381` into nine ordered integration
units, then defines a distinct post-Unit-9 Governance Tail for the plan and its
durable governance evidence. The Governance Tail is not Unit 10 and does not
increase the Product Track above 42 commits or nine logical units.

Source decision/audit: `MELLYCORE-PRODUCT-TRACK-INTEGRATION-DECISION-001`, a
completed read-only governance exercise supplied as current-session evidence.
Because that exercise intentionally performed no repository mutation, no
repository-owned decision artifact existed at plan creation. Its proposed unit
map and method were treated as claims and independently rechecked against Git
objects before being recorded here.

This plan is documentation only. It does **not** authorize or perform branch
creation, worktree creation, fetch, merge, fast-forward, cherry-pick, rebase,
push, pull request creation, canonical merge, deployment, provider access,
runtime execution, scaffold implementation, or Roadmap Lock creation.

The exact SHA of the remediation commit that carries this amended plan cannot
be embedded in that same commit without unsafe self-reference. After Git creates
the remediation commit, the independent
`MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-REVIEW-001` must verify
and pin it as `REVIEW_PINNED_GOVERNANCE_TAIL_SHA`. Any future integration
authorization must pin the same accepted full SHA again before mutation.

The later integration run requires new, explicit Operator authorization naming
this plan, the exact baseline, the Product Track checkpoints, the exact accepted
`REVIEW_PINNED_GOVERNANCE_TAIL_SHA`, the separately bounded permitted Git
mutations, and the exact file/worktree boundary. Publication requires separate
authorization as defined in §12.

## 2. Fixed evidence and baseline lock

The following facts were mechanically reconfirmed on 2026-08-08 before this
plan was written:

- Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`.
- Canonical remote: `clean-origin` =
  `https://github.com/Melly-999/mellycore-aios-core.git`.
- Live read-only `ls-remote` result for `refs/heads/main`:
  `947f33d27d5546775186e96bdc61e30db78c0b3d`.
- Local `clean-origin/main`:
  `947f33d27d5546775186e96bdc61e30db78c0b3d`.
- Product Track branch at audit time:
  `refs/heads/docs/mellycore-cross-agent-context-pack-002`.
- Product Track tip:
  `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`.
- Merge-base with `clean-origin/main`:
  `947f33d27d5546775186e96bdc61e30db78c0b3d`.
- Ahead/behind (`clean-origin/main...Product Track`): `0 42`, meaning the
  Product Track is 42 commits ahead and 0 behind.
- The 42-commit path is linear, contains zero merge commits, and every commit's
  sole parent is the immediately preceding checkpoint recorded here.
- Accepted Unit 1-8 cutoff:
  `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5` = exactly 40 commits after the
  baseline.
- Context Pack tail: exactly two commits, ending at
  `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`.

Plan Remediation 001 reverified the live and local canonical baseline, Product
Track endpoint, 42 unique linear commits, nine-unit partition, and all nine
FF-only graph proofs on 2026-08-09 before editing this plan. No fixed Product
Track fact changed.

The baseline is immutable for this plan. Before any future mutation, the
integration agent MUST verify `clean-origin/main` by a fresh, read-only remote
query. If it is not exactly
`947f33d27d5546775186e96bdc61e30db78c0b3d`, the agent MUST stop with
`BASELINE_DRIFT_PLAN_REVIEW_REQUIRED`; it MUST NOT rebase, merge the new main,
rewrite ranges, or silently reinterpret this plan.

## 3. Eligibility, accepted cutoffs, and exclusions

### 3.1 Eligible committed history

The only history eligible under this plan is the exact 42-commit, parent-linked
sequence in §6:

- Units 1-8: 40 commits from
  `adcceae9f0720826c2cc702c3007acbcdd463d89` through
  `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5`. This is the accepted composed
  Product Track cutoff, subject to the mandatory composed review in §10.
- Unit 9: two commits from
  `bde76bfd704ad2f8ce6eaa76d7532212129baa38` through
  `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`. This tail is conditionally
  eligible only after Units 1-8 pass the composed review and the Context Pack
  freshness gate in §11.

Failed reviews, remediation commits, and superseded prose within this sequence
remain required ancestry and evidence. They are not independently selectable
targets and MUST NOT be omitted merely because a later review closed their
findings.

The Product Track eligibility boundary ends at
`a0b70ae6c45c640ede4889abeb1f169e5b5a6381`. Descendant governance commits may
be admitted only through the separate Governance Tail contract in §6A. They are
never Product Track commits, never Unit 10, and never alter the nine unit
boundaries.

### 3.2 Not eligible

The following are not eligible:

- any commit after `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`
  **as Product Track history**; the only descendant-history exception is a
  full-SHA-pinned, independently reviewed Governance Tail under §6A;
- any commit presented as Product Track history but not listed in §6; descendant
  Governance Tail history is governed exclusively by §6A;
- any worktree-only or index-only content;
- the current uncommitted delta in
  `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md`;
- any proposed scaffold implementation, Runtime implementation, concrete
  provider connection, credential, provider call, framework adapter, frontend,
  deployment, workflow, dependency, or Roadmap Lock content;
- the proposed 68-task roadmap or any unreviewed future roadmap content;
- any conflict resolution, manual edit, or regenerated state not separately
  reviewed against this plan.

The accepted committed Unit 8 history legitimately changes
`docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md`. Only those exact
committed blobs are eligible. The unrelated uncommitted delta currently layered
over the file is foreign state and is never accepted by this plan.

## 4. Dependency and order contract

The integration order is fixed:

`UNIT-01 → UNIT-02 → UNIT-03 → UNIT-04 → UNIT-05 → UNIT-06 → UNIT-07 → UNIT-08 → composed review → UNIT-09`

That line is the complete Product Track order. After Unit 9, a separate
governance-layer transition is required:

`a0b70ae6 → REVIEW_PINNED_GOVERNANCE_TAIL_SHA → durable completion evidence → canonical state reconciliation`

The transition is not Product Track Unit 10. No governance commit may be
inserted between Units 1-9.

No unit may be skipped, reordered, split, or partially selected. A later unit
depends on the complete checkpoint immediately before it. A failure at any
checkpoint freezes the dedicated integration branch at the last passing
checkpoint; no later unit may enter.

| Unit | Name | Required predecessor | First SHA | Last SHA | Count | Acceptance state |
| --- | --- | --- | --- | --- | ---: | --- |
| UNIT-01 | Enterprise Provider Documentation Foundation | `947f33d27d5546775186e96bdc61e30db78c0b3d` | `adcceae9f0720826c2cc702c3007acbcdd463d89` | `b32c81fa96b9f3f7542a93101b73a4fe038b033f` | 15 | Documentation gate passed with non-blocking findings |
| UNIT-02 | Provider Adapter Scaffold | `b32c81fa96b9f3f7542a93101b73a4fe038b033f` | `311ee3f371c61ca87bef2b0e5718d0f85b728902` | `5c9616350536e614096b24a5559aa86ed59ab40f` | 2 | Inert scaffold accepted with non-blocking findings |
| UNIT-03 | Cloudflare API Shield Read-Only Adapter | `5c9616350536e614096b24a5559aa86ed59ab40f` | `3de6a4961a6ba4d20b7bc133298292ff1f0fc71c` | `95a31316b0c4871343637a6b414f4aaa79dee76d` | 4 | Offline checkpoint accepted with non-blocking findings |
| UNIT-04 | Agent Runtime Architecture | `95a31316b0c4871343637a6b414f4aaa79dee76d` | `17da8603fbe8b75082cfea44223745b3c63f14de` | `bb2e216a9c3510a4dd6f37ab18eb62f8df1c374b` | 4 | Documentation gate passed with non-blocking findings |
| UNIT-05 | Agent Package Contract | `bb2e216a9c3510a4dd6f37ab18eb62f8df1c374b` | `9575bce8ae4aff2517838143f767a3a3979c77f8` | `7fa3d8ad2d319312cc7785c4b4ef9f89a5a04776` | 5 | Documentation gate passed with non-blocking findings |
| UNIT-06 | Framework Bridge Contract | `7fa3d8ad2d319312cc7785c4b4ef9f89a5a04776` | `278eae0c47af31c67c69417d447ee4f9bdb7e049` | `b26b330ccee7d9efba304ee66e6c3ccc4e1ae5e1` | 2 | Documentation gate passed with non-blocking findings |
| UNIT-07 | Shared Context Bridge Contract | `b26b330ccee7d9efba304ee66e6c3ccc4e1ae5e1` | `d3f8b737e67dd3e0afed76f15b1e50be41f2db61` | `3019a2303d794d89288edcf2f2ea201fef357f09` | 2 | Documentation gate passed with non-blocking findings |
| UNIT-08 | Runtime Scaffold Specification | `3019a2303d794d89288edcf2f2ea201fef357f09` | `f11e4c1a5fbe27c1275116d5f38565eb29afb738` | `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5` | 6 | Documentation accepted; implementation `NOT_READY` |
| UNIT-09 | Cross-Agent Context Pack | `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5` | `bde76bfd704ad2f8ce6eaa76d7532212129baa38` | `a0b70ae6c45c640ede4889abeb1f169e5b5a6381` | 2 | Content accepted; durable post-remediation review present; freshness-gated; integration unauthorized |

## 5. Common integration-unit contract

Every unit contract in §6 inherits these rules:

1. The pre-unit `HEAD` MUST equal the unit's required predecessor.
2. The incoming commits MUST equal the listed full-SHA sequence exactly and in
   order. Commit subjects and parent links MUST match `git show -s` and
   `git rev-list --parents`; abbreviation matching is insufficient.
3. The unit path manifest is the committed-object result of
   `git diff --name-only <required-predecessor>..<last-SHA>`. The future agent
   MUST capture it before mutation and compare it byte-for-byte to the same
   range after the checkpoint. Worktree paths are not evidence.
4. The integration MUST preserve original commit identities. The permitted
   method is the per-unit `--ff-only` checkpoint advancement in §8; it is not a
   branch-wide fast-forward of the current tip.
5. The post-unit `HEAD` MUST equal the unit's last SHA. The newly included range
   MUST contain exactly the listed count, and the first SHA of the next unit
   MUST not yet be an ancestor of `HEAD`.
6. `git status --porcelain` in the dedicated integration worktree MUST be empty
   before and after each advancement. Any conflict or modification is a STOP;
   no conflict resolution is authorized by this plan.
7. Run the common checkpoint validations in §9 plus the unit-specific checks in
   §6. A failed required check is a STOP at the current checkpoint.
8. A checkpoint is a rollback/stop boundary, not permission for destructive
   rollback. Leave the branch at the last passing SHA. Recreating a new branch
   from a verified checkpoint requires explicit authorization; reset, rebase,
   force, and history rewrite remain prohibited.

## 6. Exact logical units

### UNIT-01 — Enterprise Provider Documentation Foundation

- **Commits, exact order:**
  1. `adcceae9f0720826c2cc702c3007acbcdd463d89` — `docs: sync enterprise provider research and roadmap`
  2. `e4b8db4a657d7316ab6168f806fefb2f3e9ac636` — `docs: record enterprise provider architecture decision`
  3. `40afc86258af4f7e46e061a8c4a0eca19827a511` — `docs: define Cloudflare API Shield connector contract`
  4. `0695292a987ed31d0a70cf86d28753c3170ca715` — `docs: repair enterprise provider document integrity`
  5. `7c3b971e93790e1ad10b1c6cf452ac1c5c60f7c6` — `docs: extend provider registry contract`
  6. `12188b8f62127f05fc26277fe6c7a21c2a1e897c` — `docs: define integration gateway security contract`
  7. `918aa4c437364986e80d9c52608b5a1e0141f946` — `docs: define cybersecurity provider pack`
  8. `f66e37a8cc506c9d5580342e146ab46cd2a39f89` — `docs: define marketing provider pack`
  9. `8a5c4ebf16485d6e7508b811c4ccdd8032dfdcb2` — `docs: review enterprise provider documentation integration`
  10. `086773cc20d5742cd28b7e10b11ba83f96e2b1ab` — `docs: remediate enterprise provider documentation integration`
  11. `95b5b03defcfa9530f7e2625f12648aa8eac918c` — `docs: verify enterprise provider documentation remediation`
  12. `8e1f7289345eb556d6b1972cac61c0aa9a950c89` — `docs: align enterprise provider credential classes`
  13. `699f1d39b011b6afe5ba82d4c2bd8f5639c5de59` — `docs: verify enterprise provider credential class conformance`
  14. `b90ce82ab497469ea3c8b8c0f3c8be8ce8717dbd` — `docs: align restricted operator tool path`
  15. `b32c81fa96b9f3f7542a93101b73a4fe038b033f` — `docs: verify restricted operator tool path conformance`
- **Purpose/canonical effect:** establish the enterprise-provider ADR,
  Cloudflare connector contract, Provider Registry extension, Integration
  Gateway security contract, provider packs, failed-review evidence,
  remediations, and final deterministic documentation gate.
- **Dependencies:** canonical baseline only.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_ENTERPRISE_PROVIDER_DOCS_INTEGRATION_REVIEW_004.md`
  and
  `docs/tasks/MELLYCORE-ENTERPRISE-PROVIDER-DOCS-INTEGRATION-REVIEW-004.md`;
  outcome `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 0 / P3 3.
  Reviews 001-003 and their failed outcomes remain required evidence.
- **Unresolved non-blocking findings:** `P3-401`, `P3-402`, `P3-403`.
- **Implementation blockers:** documentation acceptance authorizes no provider
  credentials, provider runtime, restricted tool, MCP connection, Cloudflare
  call, or concrete provider adapter. Each requires its own contract gates and
  explicit Operator authorization.
- **Excluded content:** credentials, provider calls, runtime enablement, and all
  noncommitted state.
- **Post-unit validation:** common §9 checks; documentation validator; confirm
  final Review 004 result and that Provider Registry/Gateway/Cloudflare
  ownership and credential-class mappings are deterministic.
- **Rollback/STOP boundary:** stop at baseline on any mismatch; after success,
  `b32c81fa96b9f3f7542a93101b73a4fe038b033f` is the first checkpoint.

### UNIT-02 — Provider Adapter Scaffold

- **Commits, exact order:**
  1. `311ee3f371c61ca87bef2b0e5718d0f85b728902` — `feat: scaffold provider adapter contracts`
  2. `5c9616350536e614096b24a5559aa86ed59ab40f` — `docs: review provider adapter scaffold`
- **Purpose/canonical effect:** add the provider-neutral, standard-library,
  fixture-only inert contracts and their independent review; execution remains
  `EXECUTION_DISABLED` and implementation remains `FIXTURE_ONLY`.
- **Dependencies:** complete UNIT-01.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md` and
  `docs/tasks/MELLYCORE-PROVIDER-ADAPTER-SCAFFOLD-REVIEW-001.md`; outcome
  `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 6 / P3 5.
- **Unresolved non-blocking findings:** `P2-01` through `P2-06` and `P3-01`
  through `P3-05`, as recorded by Review 001; they include sealing,
  validation-coverage, authentication-mode, event-verification, public-surface,
  range, and provider-ID-bound concerns.
- **Implementation blockers:** this unit authorizes no concrete adapter,
  credential, network transport, SDK, OAuth, MCP/fabric path, provider access,
  or execution-success path. Findings relevant to a concrete implementation
  must be resolved by that implementation's gate.
- **Excluded content:** any adapter other than the exact inert committed
  scaffold and all live/provider behavior.
- **Post-unit validation:** common §9 checks plus
  `py -3.9 -m unittest tests.test_provider_adapters` and the full standard-
  library test discovery used by repository convention.
- **Rollback/STOP boundary:** checkpoint
  `5c9616350536e614096b24a5559aa86ed59ab40f`; any non-disabled outcome,
  network/environment/subprocess/SDK behavior, or mutable foreign state is a
  STOP.

### UNIT-03 — Cloudflare API Shield Read-Only Adapter

- **Commits, exact order:**
  1. `3de6a4961a6ba4d20b7bc133298292ff1f0fc71c` — `feat: add Cloudflare API Shield read-only adapter`
  2. `81fbe401ac6b901d7e0bc5c47903be084133de7b` — `docs: review Cloudflare API Shield read-only adapter`
  3. `1a9acd2f1ad7b4597bce795d5d626424f34466e2` — `fix: bind Cloudflare read authentication modes`
  4. `95a31316b0c4871343637a6b414f4aaa79dee76d` — `docs: verify Cloudflare adapter remediation`
- **Purpose/canonical effect:** add and review the transportless,
  credentialless, execution-disabled Cloudflare descriptor, manifests, plans,
  synthetic fixtures, and normalization boundary. Review 001's failure and the
  remediation remain required ancestry.
- **Dependencies:** complete UNIT-02 and UNIT-01's accepted provider contracts.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_002.md`
  and
  `docs/tasks/MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002.md`;
  outcome `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 2 / P3 1.
- **Unresolved non-blocking findings:** `P2-03` (`str` subclass normalization /
  digest concern), `P2-04` (provider record does not enumerate
  `delegated_oauth` as an offered provider-API mode), and `P3-01`.
- **Implementation blockers:** close `P2-03` before downstream consumption of
  normalized strings or `state_digest`; resolve `P2-04` before creating a
  Cloudflare provider record or credential profile. No live Cloudflare work is
  authorized.
- **Excluded content:** endpoint, credential, authentication execution, SDK,
  OAuth flow, MCP, webhook, mutation, containment, runtime, or deploy behavior.
- **Post-unit validation:** common §9 checks plus
  `py -3.9 -m unittest tests.test_cloudflare_provider_adapter tests.test_provider_adapters`
  and full standard-library test discovery.
- **Rollback/STOP boundary:** checkpoint
  `95a31316b0c4871343637a6b414f4aaa79dee76d`; any provider request, socket,
  credential access, non-synthetic endpoint, mutation, or enabled execution is
  a STOP.

### UNIT-04 — Agent Runtime Architecture

- **Commits, exact order:**
  1. `17da8603fbe8b75082cfea44223745b3c63f14de` — `docs: define agent runtime architecture`
  2. `ac762f5a9964c5c5111b83e831aee6624651e391` — `docs: review agent runtime architecture`
  3. `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` — `docs: remediate agent runtime architecture`
  4. `bb2e216a9c3510a4dd6f37ab18eb62f8df1c374b` — `docs: verify agent runtime architecture remediation`
- **Purpose/canonical effect:** establish the Runtime architecture and canonical
  seams, retain the failed Review 001 evidence, apply the bounded owner-document
  amendments, and record the passing Review 002.
- **Dependencies:** complete UNIT-03; Provider Registry, Gateway, adapter, and
  Cloudflare constraints remain upstream owners.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_002.md` and
  `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002.md`;
  outcome `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 0 / P3 1.
- **Unresolved non-blocking findings:** `NEW-P3-01`, the §12.2 projection-note
  overstatement concerning Control Plane §9.10 renderability.
- **Implementation blockers:** documentation acceptance authorizes no Runtime,
  framework, agent, model, tool, provider, credential, context backend, memory
  backend, queue, or frontend implementation.
- **Excluded content:** every implementation or execution surface.
- **Post-unit validation:** common §9 checks; documentation validator; confirm
  the Provider Registry remains the sole provider-authorization owner and the
  Runtime/Control Plane/Run Ledger seams remain consistent.
- **Rollback/STOP boundary:** checkpoint
  `bb2e216a9c3510a4dd6f37ab18eb62f8df1c374b`; ownership duplication, status
  invention, or runtime enablement is a STOP.

### UNIT-05 — Agent Package Contract

- **Commits, exact order:**
  1. `9575bce8ae4aff2517838143f767a3a3979c77f8` — `docs: record Developer Platform and Agent Package Ecosystem direction`
  2. `708e2658f57d4dccd675e16fe858ca84b143dd2b` — `docs: define agent package contract`
  3. `f8b465bd7744343a2a3ee8e294117d1409b42437` — `docs: review agent package contract`
  4. `ad1d1fc7f947280fa55033629dc97c72eb022670` — `docs: remediate agent package contract review findings`
  5. `7fa3d8ad2d319312cc7785c4b4ef9f89a5a04776` — `docs: review remediated agent package contract`
- **Purpose/canonical effect:** record the Developer Platform direction and the
  Agent Package contract, retain Review 001's failed gate, remediate it, and
  record documentation acceptance.
- **Dependencies:** complete UNIT-04.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002.md` and
  `docs/tasks/MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-REVIEW-002.md`; outcome
  `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 3 / P3 4.
- **Unresolved non-blocking findings:** `NEW-P2-01` through `NEW-P2-03` and
  `NEW-P3-01` through `NEW-P3-04`, including the lifecycle-field, package-
  contract-version, protected-command-class, metrics, modal, and report-count
  constraints in Review 002.
- **Implementation blockers:** each P2 must be resolved before the dependent
  follow-up contract identified by Review 002. No Package Store, Package
  Registry, Agent Registry, Package Validator, loader, package, installation,
  command, hook, plugin, or MCP execution is authorized.
- **Excluded content:** package/runtime implementation and the proposed 68-task
  roadmap.
- **Post-unit validation:** common §9 checks; documentation validator; verify
  Package/Runtime/Control Plane ownership and that no disputed version or
  lifecycle projection was silently resolved.
- **Rollback/STOP boundary:** checkpoint
  `7fa3d8ad2d319312cc7785c4b4ef9f89a5a04776`; invented owner fields,
  implementation claims, or omitted failed-review ancestry is a STOP.

### UNIT-06 — Framework Bridge Contract

- **Commits, exact order:**
  1. `278eae0c47af31c67c69417d447ee4f9bdb7e049` — `docs: define agent framework bridge contract`
  2. `b26b330ccee7d9efba304ee66e6c3ccc4e1ae5e1` — `docs: review framework bridge contract`
- **Purpose/canonical effect:** specify the six-framework bridge boundary and
  record its independent documentation acceptance without installing or
  connecting a framework.
- **Dependencies:** complete UNIT-05 and UNIT-04.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001.md` and
  `docs/tasks/MELLYCORE-FRAMEWORK-BRIDGE-CONTRACT-SPEC-REVIEW-001.md`; outcome
  `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 4 / P3 4.
- **Unresolved non-blocking findings:** `NEW-P2-01` through `NEW-P2-04` and
  `NEW-P3-01` through `NEW-P3-04`, including incomplete Runtime-operation
  coverage, rejection-class overlap, capability numbering divergence,
  validation wiring, metrics, lifecycle-event, and outcome-record issues.
- **Implementation blockers:** close the relevant P2 findings before the first
  per-framework adapter specification or any component that emits the disputed
  bridge classes. No framework SDK installation/import/execution is authorized.
- **Excluded content:** framework adapters, SDKs, framework processes, model
  calls, and execution.
- **Post-unit validation:** common §9 checks; documentation validator; verify
  all framework vocabulary remains subordinate to Runtime and Agent Package
  owners and no framework dependency was added.
- **Rollback/STOP boundary:** checkpoint
  `b26b330ccee7d9efba304ee66e6c3ccc4e1ae5e1`; any framework install/import,
  result-success path, or owner collision is a STOP.

### UNIT-07 — Shared Context Bridge Contract

- **Commits, exact order:**
  1. `d3f8b737e67dd3e0afed76f15b1e50be41f2db61` — `docs: define shared context bridge contract`
  2. `3019a2303d794d89288edcf2f2ea201fef357f09` — `docs: review shared context bridge contract`
- **Purpose/canonical effect:** specify the read-only Shared Context bridge and
  record its independent documentation acceptance without implementing a
  context mutation path.
- **Dependencies:** complete UNIT-06, UNIT-05, and UNIT-04.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_REVIEW_001.md`
  and
  `docs/tasks/MELLYCORE-SHARED-CONTEXT-BRIDGE-CONTRACT-SPEC-REVIEW-001.md`;
  outcome `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 / P2 8 / P3 2.
- **Unresolved non-blocking findings:** `NEW-P2-01` through `NEW-P2-08` and
  `NEW-P3-01` through `NEW-P3-02`, covering taxonomy ownership, admission,
  quarantine precedence, memory mapping, ContextPacket overlap, replay,
  permission-amplification validation, numbering, and version-definition gaps.
  Upstream Agent Package and Framework Bridge P2 findings remain open and
  contained; none is silently resolved here.
- **Implementation blockers:** close the review-designated P2 findings before a
  Shared Context Bridge component or a dependent implementation emits or
  consumes the unresolved classes, mappings, or admission behavior. No context
  write is authorized.
- **Excluded content:** bridge code, context mutation, memory backend, runtime,
  framework, provider, and frontend implementation.
- **Post-unit validation:** common §9 checks; documentation validator; verify
  Runtime/Package/Framework/Shared Context ownership is non-overlapping and all
  upstream findings remain visible.
- **Rollback/STOP boundary:** checkpoint
  `3019a2303d794d89288edcf2f2ea201fef357f09`; any context mutation path,
  ownership reassignment, or silent finding closure is a STOP.

### UNIT-08 — Runtime Scaffold Specification

- **Commits, exact order:**
  1. `f11e4c1a5fbe27c1275116d5f38565eb29afb738` — `docs: define inert agent runtime scaffold`
  2. `0969a316a23e2dee0ef04e92746638b059832ffc` — `docs: review inert agent runtime scaffold`
  3. `038453f806321073ee17ca5a7a3bfb19c80dc8f7` — `docs: remediate inert agent runtime scaffold spec`
  4. `c220ec0c5713ff8f20895d75eb76610eacac6667` — `docs: review remediated inert agent runtime scaffold`
  5. `ee897e4092664af4282b1cf1841ad0d6b51830f6` — `docs: remediate inert scaffold review 002 findings`
  6. `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5` — `docs: review inert scaffold specification v1.2`
- **Purpose/canonical effect:** integrate the specification/remediation/review
  chain through version 1.2, including all historical failed or provisional
  evidence, and stop at the accepted 40-commit cutoff.
- **Dependencies:** complete UNIT-07 and all earlier owner contracts.
- **Accepted review evidence:**
  `docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_003.md` and
  `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003.md`;
  documentation outcome `PASS_WITH_NON_BLOCKING_FINDINGS`, P0 0 / P1 0 /
  P2 2 / P3 3; implementation outcome
  `NOT_READY_IMPLEMENTATION_AFFECTING_FINDINGS`.
- **Unresolved non-blocking findings:**
  - `NEW-P2-01`: seven live positional citations contradict the document's
    no-positional-dependency criterion. Non-blocking for documentation
    integration; blocking for a future amendment.
  - `NEW-P2-02`: the §27.1 evidence-completeness test is indeterminate for an
    approved inert fixture occupying a §12 port. Non-blocking for documentation
    integration; **blocking for implementation**.
  - `NEW-P3-01`: version-restatement amendment mechanism can recreate the prior
    version inconsistency; blocking for a future amendment.
  - `NEW-P3-02`: §44.1 cites nonexistent §34.1 instead of §31.1.1.
  - `NEW-P3-03`: `EVIDENCE_INCOMPLETE` representation is unconstrained.
- **Implementation blockers:** scaffold implementation remains `NOT_READY`.
  `NEW-P2-02` MUST remain visible and MUST be resolved before implementation;
  acceptance of this unit MUST NOT be cited as implementation authorization.
  `NEW-P2-01` and `NEW-P3-01` remain future-amendment blockers and MUST NOT be
  reclassified.
- **Excluded content:** every uncommitted modification to the scaffold spec and
  all scaffold code, Runtime, adapters, loaders, tests, dependencies, provider
  behavior, or execution not present in the exact six commits.
- **Post-unit validation:** common §9 checks; documentation validator; verify
  owner-document consistency, all 15 upstream P2 findings remain open and
  contained, no execution-success path is claimed, and implementation state is
  exactly `NOT_READY`.
- **Rollback/STOP boundary:** checkpoint and accepted cutoff
  `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5`. STOP before UNIT-09 until the
  composed review in §10 passes.

### UNIT-09 — Cross-Agent Context Pack

- **Commits, exact order:**
  1. `bde76bfd704ad2f8ce6eaa76d7532212129baa38` — `docs: finalize cross-agent context pack`
  2. `a0b70ae6c45c640ede4889abeb1f169e5b5a6381` — `docs: remediate cross-agent context status semantics`
- **Purpose/canonical effect:** establish the canonical cross-agent bootstrap /
  navigation packet and correct its task-status semantics after review.
- **Dependencies:** complete and accepted UNIT-01 through UNIT-08, a passing
  composed review, and exact Context Pack freshness under §11.
- **Accepted review evidence:** the original candidate review outcome
  `ACCEPT_MELLYCORE_CROSS_AGENT_CONTEXT_PACK_002` is recorded in
  `docs/tasks/MELLYCORE-CROSS-AGENT-CONTEXT-PACK-REMEDIATION-001.md`. The final
  remediation outcome
  `ACCEPT_MELLYCORE_CROSS_AGENT_CONTEXT_PACK_REMEDIATION_001` with P0 0 / P1 0 /
  P2 0 / P3 1 is now recorded durably in
  `docs/research/MELLYCORE_CROSS_AGENT_CONTEXT_PACK_REMEDIATION_REVIEW_001.md`.
  That record explicitly states that the independent result was Operator-
  supplied and subsequently recorded by the Plan Remediation task; it does not
  falsely claim contemporaneous repository origin.
- **Unresolved non-blocking findings:** R1/P3 records the ancestry-count
  qualification: source Context Pack commit `bde76bfd...` was 41 ahead / 0
  behind, while final remediation commit `a0b70ae6...` was 42 ahead / 0 behind.
  F1 is `CLOSED`; F2 remains `OPEN_GOVERNANCE_ITEM`.
- **Implementation blockers:** none created by Context Pack documentation
  acceptance; every implementation block from Units 1-8 remains in force.
- **Excluded content:** any refreshed, generated, or worktree-only Context Pack
  content and any unreviewed factual rewrite.
- **Post-unit validation:** common §9 checks plus exact fact-by-fact comparison
  of `shared_context/CROSS_AGENT_CONTEXT.md` against the integrated canonical
  tree, status vocabulary owners, current safety contract, and implementation
  truth.
- **Rollback/STOP boundary:** checkpoint
  `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`. Any stale fact requires a
  separately authorized refresh and independent review; do not integrate stale
  Context Pack content.

## 6A. Post-Unit-9 Governance Tail checkpoint

The Product Track ends exactly at Unit 9 commit
`a0b70ae6c45c640ede4889abeb1f169e5b5a6381`: 42 commits, nine logical units,
zero merges, and no governance commit inserted between unit boundaries.

The **Governance Tail** is a separate descendant layer after that endpoint. It
is **not Unit 10**, is not counted in the Product Track inventory, and does not
change any Unit 1-9 first SHA, last SHA, predecessor, count, or FF-only proof.

Conceptually:

- Product Track: `clean-origin/main → Units 1-9 → a0b70ae6`
- Governance Tail: `a0b70ae6 → reviewed Governance Tail candidate → durable completion evidence → reconciled canonical state`

### 6A.1 `GOVERNANCE_TAIL_CANDIDATE`

The current `GOVERNANCE_TAIL_CANDIDATE` must be a linear descendant of
`a0b70ae6c45c640ede4889abeb1f169e5b5a6381` and contain, at minimum:

1. plan commit `14eb6c90ff3ffa7125b3f7b3ef077b17ce93d0c6`;
2. this remediated integration plan;
3. durable Context Pack remediation review evidence;
4. durable Integration Plan Review 001 evidence;
5. the Plan Remediation 001 task record;
6. the latest task-owned handoff update.

The remediation commit cannot reliably declare its own SHA because its hash
depends on this content. Therefore this document intentionally contains no
claimed final remediation SHA. After the commit exists, the independent
`MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-REVIEW-001` MUST:

- verify the candidate is a linear descendant of Unit 9;
- verify its exact changed-path scope and provenance;
- verify the two source findings are closed without changing Units 1-9;
- publish its full SHA as `REVIEW_PINNED_GOVERNANCE_TAIL_SHA`.

Any future integration authorization MUST name that same accepted full SHA.
The executor MUST reject a branch name, tag, inferred `HEAD`, abbreviated SHA,
or candidate SHA supplied only by this remediation task.

### 6A.2 Governance Tail completion evidence

The review-pinned candidate preserves the plan and remediation evidence, but
the governance workflow is not complete until the tail also durably preserves:

- the accepted Plan Remediation Review outcome and exact candidate pin;
- the Unit 8 composed-review result;
- the integration execution/checkpoint report;
- the latest handoff and canonical governance/state reconciliation.

The Unit 8 composed review may occur read-only before Unit 9. Its result is
recorded afterward in the Governance Tail; no evidence commit is inserted
between Units 8 and 9. Any commit that records these later outcomes requires its
own explicit scope and authority. Before publication or Roadmap Lock, the exact
final reconciled Governance Tail head must itself be verified and pinned.

### 6A.3 Governance Tail admission gate

Before any advance beyond Unit 9, all of the following are mandatory:

1. Unit 9 freshness and integration gates passed at the exact Product Track
   endpoint;
2. `REVIEW_PINNED_GOVERNANCE_TAIL_SHA` exists in an accepted independent
   remediation-review record;
3. explicit Operator authorization names that exact SHA and permits only the
   bounded Governance Tail advance;
4. the candidate range is linear, conflict-free, and contains no Product Track
   rewrite, foreign worktree content, implementation, provider, or deployment
   change;
5. the dedicated integration worktree is clean.

Failure of any condition is `GOVERNANCE_TAIL_NOT_ADMISSIBLE_STOP`.

## 7. Foreign dirty-state isolation contract

At plan creation, the source worktree contains one known foreign modification:
`docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md`, unstaged. Its
uncommitted content was not used as authority and is outside the accepted
committed stack.

The future integration run MUST:

1. Never use the current dirty Product Track worktree as the integration
   worktree or as a file-copy source.
2. Create a separate clean worktree and dedicated branch from the exact
   baseline, after explicit authorization.
3. Integrate only commit objects by full SHA; never copy files from the source
   worktree.
4. Require an empty index and worktree in the dedicated integration worktree at
   every checkpoint.
5. Never run `git add .` or `git add -A`; stage explicit authorized paths only
   in separately authorized documentation/remediation tasks.
6. Never edit, stage, restore, stash, reset, clean, or otherwise manipulate the
   foreign delta as part of integration.
7. Treat any appearance of that uncommitted delta in an integration diff or
   index as `FOREIGN_WORKTREE_CONTAMINATION` and stop.

Resolution of the foreign work is not required for this plan to exist. Before
Roadmap Lock canonicalization it must either be independently resolved under
its owning task or remain demonstrably isolated in a different worktree.

## 8. Authorized future integration method

Only after explicit Operator authorization, the future integration agent may
use this architecture:

1. Reverify repository identity, `clean-origin` URL, live remote main SHA,
   local remote-tracking SHA, merge-base, 42-commit inventory, signatures if a
   later authorization requires them, and all nine unit boundaries.
2. Create a new clean worktree and dedicated local branch from exact commit
   `947f33d27d5546775186e96bdc61e30db78c0b3d`. The branch name must be named in
   that authorization (recommended:
   `integrate/mellycore-product-track-integration-001`).
3. Advance the dedicated branch one unit at a time with `git merge --ff-only
   <unit-last-SHA>`, beginning with UNIT-01. The pre-unit HEAD and incoming
   sequence checks in §§5-6 must pass before each command.
4. Validate and record every checkpoint before advancing.
5. Stop after UNIT-08 for the mandatory independent composed review.
6. If the composed review passes, recheck Context Pack freshness against the
   exact composed Units 1-8 tree and advance to UNIT-09 only if §§10-11 pass.
7. Verify the Unit 9 endpoint is exactly
   `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`; no governance commit may have
   entered the Product Track range.
8. Resolve `REVIEW_PINNED_GOVERNANCE_TAIL_SHA` only from the accepted Plan
   Remediation Review and exact Operator authorization. Reproduce §6A's
   descendant, path-scope, and safety gates before any advance to it.
9. Advance to that exact review-pinned candidate only under the separately
   authorized Governance Tail scope, then durably record the composed-review,
   integration-execution, remediation-review, handoff, and canonical state-
   reconciliation evidence required by §6A.2.
10. Treat integration as incomplete until the reconciled Governance Tail head
    is verified and pinned. Roadmap Lock remains blocked throughout.

This method preserves every original commit and reviewed checkpoint. It is not
permission to run the commands now.

Explicitly rejected:

- using `refs/heads/docs/mellycore-cross-agent-context-pack-002` or any current dirty
  working branch directly as the integration branch;
- copying or staging worktree files;
- arbitrary individual cherry-picks or cherry-picked subsets;
- one branch-wide merge of the current Product Track branch;
- one full current-tip fast-forward from baseline to
  `a0b70ae6c45c640ede4889abeb1f169e5b5a6381` without
  unit checkpoints;
- treating the Governance Tail as Unit 10 or counting its commits in the
  42-commit Product Track;
- inserting a governance-evidence commit between Product Track units;
- advancing beyond Unit 9 using an unreviewed SHA, branch name, tag, inferred
  `HEAD`, or self-declared remediation SHA;
- rebase, squash, commit rewriting, conflict resolution, or force operations;
- integrating any unreviewed future commit.

## 9. Checkpoint validation policy

After every unit, record all of the following before proceeding:

- repository top-level and canonical remote URL;
- expected pre-unit SHA and exact post-unit `HEAD`;
- exact newly included commits, subjects, parents, and count;
- cumulative count from baseline;
- proof that the next unit's first commit did not enter early;
- exact changed-path manifest for the unit range and confirmation that each path
  comes from committed objects;
- clean dedicated index/worktree;
- no foreign dirty content;
- `git diff --check` for the cumulative baseline-to-checkpoint range;
- `py -3.9 scripts/validate_project_state.py` where the clean integration
  worktree makes it suitable;
- focused and full standard-library tests after UNIT-02 and UNIT-03;
- canonical state consistency across `PROJECT_STATE.md`, `AGENT_HANDOFF.md`,
  `RUN_QUEUE.md`, `ROADMAP.md`, `TASK_INDEX.md`, and task/review artifacts as
  applicable to the checkpoint;
- safety consistency: no secret, credential, provider request, live connection,
  execution success, runtime enablement, context mutation, or deploy
  authorization introduced;
- confirmation that inert code remains inert and documentation remains distinct
  from implementation readiness;
- secret/config and prohibited-scope scans over the exact newly included range.

After Unit 9, §6A adds separate Governance Tail checks: exact review-pinned
candidate SHA, linear ancestry from `a0b70ae6...`, no Unit 1-9 boundary change,
candidate path allowlist, durable evidence presence, clean integration worktree,
and no foreign content. Governance Tail commits are never included in a Product
Track checkpoint count.

Any validator that writes, formats, generates, or otherwise changes the tree is
unsuitable unless separately authorized. A validator failure may be diagnosed
read-only, but no repair is authorized by the integration permission itself.

## 10. Mandatory composed integration review after UNIT-08

After UNIT-08, the dedicated branch MUST stop at
`fb63f2f3c82fdb2c94ea12f9501c0109089f17f5`. An independent read-only composed
review is mandatory. Prior per-unit reviews are evidence, not a substitute.

The review MUST compare the entire composed tree against baseline
`947f33d27d5546775186e96bdc61e30db78c0b3d` and verify:

1. exact inclusion of Units 1-8: 40 commits, once each, in plan order;
2. owner-document consistency and no duplicated authority;
3. task/status consistency and truthful historical failed-review records;
4. exact reviewed-SHA references and no supersession drift;
5. Provider → Adapter → Cloudflare → Runtime dependency consistency;
6. Agent Package / Framework Bridge / Shared Context Bridge consistency;
7. no accidental provider, framework, model, tool, context-write, runtime, or
   execution enablement;
8. inert provider code still has no live/network/credential/success path;
9. Runtime Scaffold implementation remains exactly `NOT_READY`;
10. `NEW-P2-02` remains visible and implementation-blocking;
11. `NEW-P2-01` and `NEW-P3-01` remain future-amendment blockers;
12. all other open P2/P3 findings remain visible and correctly scoped;
13. repository validator and relevant unit tests pass in the clean composed
    worktree;
14. no foreign worktree content or later-unit commit is present.

Any P0/P1, ownership contradiction, task/status contradiction, stale reviewed
SHA, unexpected path, validation failure, implementation enablement, or hidden /
reclassified blocker yields `COMPOSED_REVIEW_FAILED_STOP`. UNIT-09 must not
begin.

The composed review may remain read-only at this checkpoint so that the proven
Unit 8 → Unit 9 ancestry is not altered. Before the overall integration workflow
is complete, its exact outcome, reviewed Unit 8 SHA, evidence, and disposition
MUST be committed durably in the Governance Tail under separate authorization.
An ephemeral-only composed-review result cannot satisfy §6A.2 or the Roadmap
Lock gate.

## 11. Context Pack freshness and integration gate

UNIT-09 may advance only when all are true:

- Units 1-8 are integrated at the exact accepted cutoff;
- the composed review in §10 passes;
- the canonical state at that checkpoint matches every fact summarized by the
  Context Pack;
- the original acceptance, remediation task record, and durable post-
  remediation review record are present;
- the post-remediation acceptance outcome
  `ACCEPT_MELLYCORE_CROSS_AGENT_CONTEXT_PACK_REMEDIATION_001` is recorded in
  `docs/research/MELLYCORE_CROSS_AGENT_CONTEXT_PACK_REMEDIATION_REVIEW_001.md`
  as Operator-supplied, subsequently committed evidence with P0 0 / P1 0 / P2 0
  / P3 1;
- the Context Pack still distinguishes formal `TASK_INDEX.md` statuses from
  broader architecture/project terms;
- F2's integration-risk warning remains truthful.

The durable review record establishes **content acceptance only**. Integration
is still unauthorized, and freshness MUST be rechecked immediately before Unit
9 against the exact composed Units 1-8 tree. The record does not make Unit 9
automatically eligible.

If integration, conflict handling, canonical drift, a later review, or any
other event changes a fact summarized by the Context Pack, UNIT-09 becomes
stale and MUST NOT be advanced. The required action is a separately authorized
Context Pack refresh from the accepted UNIT-08 composed tree, followed by an
independent review. The refreshed commit(s) are not automatically eligible
under this plan; this plan must be amended or superseded with new exact SHA
boundaries.

## 12. Publication boundary and required Operator authorizations

Integration and publication are separate authority domains.

The first future authorization must explicitly name:

- `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-001` after independent review;
- repository and `clean-origin`;
- baseline `947f33d27d5546775186e96bdc61e30db78c0b3d`;
- eligible endpoints `fb63f2f3c82fdb2c94ea12f9501c0109089f17f5` and,
  conditionally, `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`;
- the exact accepted `REVIEW_PINNED_GOVERNANCE_TAIL_SHA` from
  `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-REVIEW-001`, with an
  explicit statement that it is a separate post-Unit-9 governance layer and not
  Product Track Unit 10;
- the dedicated branch/worktree name and location;
- permission to create that local branch/worktree and perform only the nine
  per-unit `--ff-only` advancements plus the separately bounded, exact-SHA
  Governance Tail advance;
- required validation and stop boundaries;
- an explicit statement that no push, PR, canonical merge, deployment, rebase,
  squash, force, or destructive operation is authorized.

After local integration and independent final review, each later publication
phase requires its own explicit Operator authorization:

1. one normal push of the exact reviewed dedicated-branch head;
2. creation of one non-draft PR with exact base/head and complete evidence;
3. independent PR review of the exact head;
4. merge of the exact reviewed PR head.

No authorization is inferred across phases. Under the current Model A contract,
merging into canonical `main` immediately triggers public Vercel Production
publication. Any merge-authorization request MUST state that consequence and
must name the exact PR, head, base, merge method, and post-merge verification.
This plan grants none of those permissions.

## 13. Roadmap Lock gate

`MELLYCORE-ROADMAP-LOCK-001` is not minted, drafted, executed, or authorized by
this task. It may not be canonically minted or executed until all of the
following are true:

1. this integration plan passes
   `MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-REVIEW-001`, which pins
   the exact `REVIEW_PINNED_GOVERNANCE_TAIL_SHA`;
2. Product Track Units 1-8 are integrated on the explicitly authorized
   dedicated branch with their exact boundaries;
3. the Unit 8 independent composed review passes;
4. Unit 9 freshness is checked against the accepted composed Units 1-8 tree;
5. Unit 9 is integrated at exact endpoint
   `a0b70ae6c45c640ede4889abeb1f169e5b5a6381`;
6. the exact reviewed Governance Tail candidate is integrated under separate
   Operator authorization;
7. the composed-review result and integration execution/checkpoint evidence are
   recorded durably in the Governance Tail;
8. the latest canonical governance, handoff, and state documents are reconciled
   against the integrated tree and the exact reconciled tail head is verified;
9. the foreign scaffold work is either resolved under its own task or remains
   demonstrably isolated outside canonical and integration worktrees;
10. Scaffold `NEW-P2-02` remains visible as an implementation blocker, all
    future-amendment blockers remain preserved, and no unreviewed 68-task
    roadmap has been introduced;
11. a separate, explicit Operator authorization names the Roadmap Lock task,
    scope, evidence, and permitted files.

Drafting is not authorized by this plan. Canonicalization is blocked until all
eleven conditions are independently verified.

## 14. Global STOP conditions

Stop without mutation beyond the last explicitly authorized checkpoint if any
of the following occurs:

- repository identity or `clean-origin` is wrong;
- live `clean-origin/main` differs from the fixed baseline;
- any commit, parent, subject, path manifest, order, or count differs;
- any of the 42 commits is unclassified, duplicated, or absent;
- any Governance Tail commit is counted as Product Track Unit 10 or inserted
  between Units 1-9;
- the dedicated worktree is dirty or the current dirty Product Track worktree
  would need to be used;
- a conflict or manual edit would be required;
- a canonical owner document materially contradicts the accepted audit;
- the durable post-remediation Context Pack review record is absent, its
  subsequent-recording provenance is obscured, or Unit 9 freshness fails;
- `REVIEW_PINNED_GOVERNANCE_TAIL_SHA` is absent, abbreviated, inferred from a
  floating ref, not reproduced from the accepted remediation review, or differs
  from the exact SHA in Operator authorization;
- the remediation plan attempts to self-declare its own commit SHA;
- composed-review, execution, remediation-review, or reconciliation evidence
  would remain ephemeral after Governance Tail completion;
- a required validator fails or changes the tree;
- provider/live/runtime/context-write enablement appears;
- `NEW-P2-02` is hidden, downgraded, or treated as resolved;
- execution requires a file, command, remote mutation, publication, or
  authorization outside the current explicit allowlist;
- integration would need to be performed merely to discover the plan.

## 15. Deterministic execution decision

The repository now has a complete unit map for all 42 commits. The preferred
future method is a dedicated clean integration branch from the fixed canonical
baseline, advanced by exact per-unit fast-forward checkpoints, with mandatory
validation after every unit, an independent composed review after UNIT-08, and
a freshness gate before UNIT-09. After Unit 9, the integration must advance only
to the exact independently reviewed `REVIEW_PINNED_GOVERNANCE_TAIL_SHA`, then
durably record the composed-review, integration-execution, review, handoff, and
state-reconciliation evidence before the workflow is complete. The Governance
Tail is not Unit 10 and changes none of the 42 Product Track commits. The current
dirty Product Track branch is an evidence source for commit objects only and is
never a direct integration source.

No integration or publication action is authorized. The exact next canonical
action after the remediation commit exists is an independent, read-only review:

`MELLYCORE-PRODUCT-TRACK-INTEGRATION-PLAN-REMEDIATION-REVIEW-001`
