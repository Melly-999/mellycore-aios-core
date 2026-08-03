# MellyCore Agent Runtime Architecture Spec Review 002

## 1. Title and status

**Task ID:** MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-002
**Reviewed commit:** `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` — `docs: remediate agent runtime architecture`
**Review type:** Independent, read-only post-remediation architecture, canonical-owner, and implementability review.
**Reviewer relationship to the artifact:** The reviewer did not author
`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001`. Every remediation
claim was treated as unverified until independently reproduced from Review 001,
the seam-decision record, the complete nine-file diff, the amended owner
documents, and deterministic replay.
**Gate decision:** `PASS_WITH_NON_BLOCKING_FINDINGS`
**Finding counts:** P0 = 0 · **P1 = 0** · P2 = 0 · **P3 = 1 (new)**
**Review 001 closure:** all **fourteen** findings independently `CLOSED`.
**Status:** Complete as one local documentation commit; **not pushed**.

This review authorizes no implementation, no framework installation or
connection, no agent execution, no model-provider call, no tool invocation, no
provider authentication, no credential configuration, no persistence, no
frontend, and no deployment. It repaired no finding.

## 2. Purpose

Determine independently whether the remediation commit fully closes the four
P1, five P2, and five P3 findings of Architecture Review 001; whether the two
canonical owner amendments are minimal, additive, and semantically compatible;
whether every unchanged canonical owner remains compatible; and whether
`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` can now be written without
reopening Agent Runtime architecture.

The review optimizes for detecting unnecessary owner-semantics changes, new
status incompatibilities, weakened prohibitions, Run Ledger identity ambiguity,
silently changed loop-run behavior, duplicated authorization facts, unreachable
lifecycle transitions, contradictory envelope sequencing, under-specified
restart or broadcast races, prose-only count corrections, and seams closed in
one place while opened in another. It does not optimize for producing a PASS.

## 3. Scope

In scope: repository and commit identity verification; one authorized read-only
`git fetch clean-origin`; inspection of the complete nine-file remediation
commit; complete or complete-by-section reading of the canonical documents;
independent reconstruction of the fourteen-finding closure matrix, the 17-state
lifecycle projection, the 11 authorization facts, ledger and run identity, the
eight-step envelope sequence, staleness behavior, broadcast concurrency, restart
recovery, counts, and error taxonomy; replay of all 42 deterministic scenarios;
implementability assessment; documentation validators; one review record; one
review task report; bounded updates to four shared-context files; and one local
documentation commit.

Out of scope and not performed: any modification of the seam-decision record,
the Agent Runtime Architecture specification, the Control Plane specification,
the AI Operations Intelligence specification, the remediation task report,
Architecture Review 001, the Provider Registry, the Integration Gateway, Loop
Operations documents, or Shared Context contracts; any remediation; any source
or test change; any Agent Package Contract drafting; any framework installation
or execution; any agent execution; any model-provider call; any provider or tool
access; any credential handling; any MCP or fabric connection; any push, pull
request, merge, remote branch, or deployment; and any MellyTrade interaction.

## 4. Starting repository state

| Item | Verified value |
| --- | --- |
| Working tree root | `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` |
| Starting branch | `docs/mellycore-agent-runtime-architecture-spec-remediation-001` |
| Starting HEAD | `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` |
| Parent | `ac762f5a9964c5c5111b83e831aee6624651e391` |
| Subject | `docs: remediate agent runtime architecture` |
| Worktree / index at start | Clean (`git status --short --branch` returned only the branch line) |
| Canonical remote | `clean-origin` → `https://github.com/Melly-999/mellycore-aios-core.git` |
| Freshly verified `clean-origin/main` | `947f33d27d5546775186e96bdc61e30db78c0b3d` — matched the expected value; **no drift** |
| Review 002 branch before creation | Absent locally; absent on `clean-origin` and `origin` |
| Review branch created | `docs/mellycore-agent-runtime-architecture-spec-review-002`, from `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` |

Exactly one network operation occurred during this task: `git fetch
clean-origin` (exit code `0`), executed during the canonical remote gate. No
other network access of any kind occurred: no `origin` access, no pull, no push,
no GitHub API call, no provider endpoint, no model-provider endpoint, no package
download, no MCP or fabric connection, no telemetry, and no deployment.

## 5. Reviewed commits

| Commit | Subject | Role |
| --- | --- | --- |
| `17da8603fbe8b75082cfea44223745b3c63f14de` | `docs: define agent runtime architecture` | Original specification |
| `ac762f5a9964c5c5111b83e831aee6624651e391` | Architecture Review 001 | Finding source; parent of the remediation |
| `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` | `docs: remediate agent runtime architecture` | **Subject of this review** |

## 6. Remediation commit scope

**Exactly nine paths**, independently confirmed by `git show --name-only`:

1. `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` (new, 477 lines)
2. `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` (+852 lines changed)
3. `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (15 lines changed)
4. `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` (21 lines changed)
5. `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001.md` (new, 532 lines)
6. `shared_context/AGENT_HANDOFF.md`
7. `shared_context/PROJECT_STATE.md`
8. `shared_context/ROADMAP.md`
9. `shared_context/RUN_QUEUE.md`

Total: 2,115 insertions, 134 deletions. No source file, test file, schema, Provider
Registry document, Integration Gateway document, Loop Operations document, Shared
Context contract, or prior review record appears in the commit.

## 7. Canonical documents

Read completely or by complete normative section: the Agent Runtime Architecture
specification (2,193 lines); the seam-decision record (477 lines); Architecture
Review 001 (1,436 lines); the Control Plane specification (§8.1, §8.2, §9.4–§9.10);
the AI Operations Intelligence specification (§5.1, §5.9, edge-behavior table);
the Provider Registry Contract Extension (§21.1–§21.5); the Integration Gateway
Security Contract; the Operations Data Contract; the Loop Operations
Architecture; `shared_context/loops/RUN_LEDGER_SCHEMA.json`,
`LOOP_STATE_SCHEMA.json`, `LOOP_REGISTRY_SCHEMA.json`;
`shared_context/CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md`,
`SAFETY_CONTRACT.md`, `VALIDATION.md`, `MODEL_ROUTING.md`; the context-provenance
documents; and the four current shared-context state files.

Repository-wide read-only searches were performed for every closed lifecycle
vocabulary, every `lifecycle_status` occurrence in schemas and code, every
residual `run_id`-keyed deduplication clause, and every enum containing
`"active"`.

## 8. Independent method

1. Repository identity gate before any read of the artifact.
2. Canonical remote gate: one authorized `git fetch clean-origin`; fresh
   verification of `clean-origin/main`; re-verification that branch, HEAD,
   worktree, and index were unchanged; confirmation of the nine-path scope; and
   confirmation that no conflicting local or remote Review 002 branch existed.
3. Immutable baselines recorded as Git blob IDs before any edit (Section 9).
4. Review branch created from the remediation commit, never from `clean-origin/main`.
5. The fourteen findings reconstructed **from Review 001 itself**, never from the
   remediation report's restatement of them.
6. Every count recalculated mechanically from the document's own tables.
7. The lifecycle projection, transition graph, authorization facts, ledger
   identity, envelope sequence, staleness table, broadcast table, and recovery
   matrix rebuilt independently and compared against the canonical owners.
8. All 42 scenarios replayed against the reconstructed matrices.
9. Both owner amendments diffed line by line and tested for unnecessary
   semantic change, weakened prohibitions, and newly-opened seams.
10. Post-edit re-verification that every reviewed document remained
    byte-identical to its recorded baseline.

## 9. Immutable baselines

Git blob IDs recorded at `ca221df3f7ee6267c06f2050268b6a8e32bf9ea3` before any
edit. Every one was re-verified unchanged after the review commit (Section 43).

| Blob ID | Path |
| --- | --- |
| `13b2df338ad53cff02eb236ba0d30d34cd35bf20` | `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md` |
| `3e085f97141fc0cb505ab4d9a738592d7ca601f7` | `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md` |
| `4ea189989665907b0b931c2a86dcc112285d69b8` | `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` |
| `f35f0e157879322c9edbaf834043902579a6d98f` | `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` |
| `751e705457340157e6914148d72fc380f0e7cbe6` | `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md` |
| `fa90b65b4f91545550247d81fc181eb10cca942a` | `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md` |
| `65192fa157b57a2a46768ceca4660aed1584f649` | `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md` |
| `13fa511f6228d4f8f13295dbd857c7586a163333` | `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md` |
| `38c847d684e6d6f08f8b76ff482237b4c7685e37` | `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md` |
| `72cceccdae0336125f7acc34d6ef592109c4e9d1` | `shared_context/loops/RUN_LEDGER_SCHEMA.json` |
| `ec29d4894c5f942ce3e4be2d03ef33ceb0678fca` | `shared_context/loops/LOOP_STATE_SCHEMA.json` |
| `87de4d600f77e28455ac3b821013f0403abb6a29` | `shared_context/loops/LOOP_REGISTRY_SCHEMA.json` |
| `f5f70cef51eeb92c9a30edf80d31e57cac8b6c14` | `shared_context/loops/LOOP_REGISTRY.json` |
| `a70500a9909ee5bbe2bf60cdfe9e779fc47877a0` | `shared_context/SAFETY_CONTRACT.md` |
| `a4acf641d3cc1551ad1513bcc8ec0cc619be941b` | `shared_context/VALIDATION.md` |
| `b4441133b4529c1260de205b147d2c42b5063a5d` | `shared_context/MODEL_ROUTING.md` |
| `e8f8961f5c1a12275527cc05c83c432c9312d0d6` | `shared_context/CONTEXT_GRAPH_SCHEMA.md` |
| `373a9313dbec3d30f9673931ab74c742738e2adb` | `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md` |

Shared-context baselines (within the approved editable set, changed by this review):
`b00493e6496ed2dad50a9ba53b1861ed13671281` `shared_context/PROJECT_STATE.md`;
`c32de99d148f780709c138ac27a6e4d49c527052` `shared_context/ROADMAP.md`;
`9b4c6dff0336357cd6b82fe437c7678f34ba6a83` `shared_context/RUN_QUEUE.md`;
`0018870caa19fc614aa9035b3e74bc5b698e184f` `shared_context/AGENT_HANDOFF.md`.

### 9.1 Independently recounted dimensions

Every figure below was recounted mechanically from the document's own tables.

| Dimension | Claimed (§1.4) | Independently counted | Result |
| --- | --- | --- | --- |
| Run lifecycle states | 17 | 17 (§12.2 rows 1–17) | ✅ |
| Lifecycle projection rows | 17 | 17 | ✅ |
| Projection rows using `active` | 0 | **0** | ✅ |
| Distinct projected lifecycle values | — | 9 (`draft`, `planned`, `ready`, `queued`, `running`, `blocked`, `completed`, `failed`, `cancelled`) | ✅ |
| Lifecycle transition rows | 13 | 13 (§12.3) | ✅ |
| `waiting_for_operator` predecessors | 4 | 4 (§12.3.1) | ✅ |
| Forbidden-transition rules | 12 | 12 (§12.4) | ✅ |
| Authorization facts | 11 | 11 (8 + 3) | ✅ |
| Authorization sequencing steps | 8 | 8 (§15.4) | ✅ |
| Staleness conditions | 6 | 6 (§17.4) | ✅ |
| Context-flow trace fields | **17** | **17** (§19, numbered 1–17) | ✅ **P3-01 closed** |
| Handoff envelope contents | **12** | **12** (§20.2, enumerated) | ✅ **P3-02 closed** |
| Broadcast acceptance conditions | 7 | 7 (§20.4) | ✅ |
| Recovery matrix rows | 16 | 16 (§29.3) | ✅ |
| Error taxonomy rows | **49** | **49** (§33) | ✅ |
| Error taxonomy distinct class names | **49** | **49**, zero duplicates | ✅ **P3-03 closed** |
| Deterministic scenarios | **42** | **42**, IDs 1–42, no gaps, no duplicates | ✅ |
| Seam-decision sections | 18 | 18 (§1–§18) | ✅ |

## 10. Original finding register

Reconstructed from Architecture Review 001 §45–§46 directly, not from the
remediation report.

| ID | Severity | Defect as originally recorded |
| --- | --- | --- |
| `P1-01` | P1 | Six `run_state` values project to `lifecycle_status:active`, which Control Plane §8.2 forbids for a running agent; §9.5/§9.7 Run sets exclude `active`, `queued`, `draft`, `ready` |
| `P1-02` | P1 | Facts 5 and 6 duplicate Registry facts 5 and 6 (both provider-scoped, requiring `provider_id`) and are nested inside fact 10; scope, evidence, expiry, and capability vocabulary unstated; a purely local run could not be authorized |
| `P1-03` | P1 | Attempt evidence contradicts AI Ops §5.9 (dedup by `run_id`) and §5.1 (one `outcome`/`model`/`provider` per `run_id`); the runtime, a declared non-owner, could not amend it |
| `P1-04` | P1 | §23.6 mandates `waiting_for_operator` for an unresolved routing tie, but §12.3 does not permit `waiting_for_model → waiting_for_operator`; Scenario 15 unreachable |
| `P2-01` | P2 | Stale-snapshot resolution selected by an undefined policy |
| `P2-02` | P2 | `model_routing_decision_ref` cannot be populated inside a digest-frozen envelope |
| `P2-03` | P2 | Agent-run identity not reconciled with the run-ledger `run_id` form or with loop runs |
| `P2-04` | P2 | Concurrent acceptance of a broadcast handoff unspecified |
| `P2-05` | P2 | Runtime restart with an attempt in an unknown state unaddressed |
| `P3-01` | P3 | §19 enumerates 16 trace fields; described elsewhere as 17 |
| `P3-02` | P3 | Task report says 11 handoff envelope contents; §20.2 enumerates 12 |
| `P3-03` | P3 | §33 has 38 rows but 40 distinct class names |
| `P3-04` | P3 | `INSUFFICIENT_PRICING_DATA` undefined and unowned; nine-state ↔ eleven-fact mapping unstated |
| `P3-05` | P3 | §8.3 rule 1 expressed in Python-specific terms inside a language-neutral architecture |

## 11. Fourteen-finding closure matrix

| Finding | Original review evidence | Remediation decision | Changed document | Canonical evidence | Independent replay | Result | Gate impact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `P1-01` | Review 001 §11, §45; CP §8.2 prohibition; §9.5/§9.7 sets | Minimally amend the owner: add one additive lifecycle member `running`; reaffirm the `active` prohibition verbatim; extend the three Run-bearing module sets | Control Plane §8.1, §8.2, §9.5, §9.7, §9.10; Runtime §12.1, §12.2 | CP §8.1 enum now contains `running`; §8.2 clause defines it as lifecycle-only, execution-scoped, never interchangeable with `active`; `active` prohibition preserved **verbatim** | Recounted all 17 projection rows: **zero** use `active`; the 9 distinct projected values are exactly the values added to §9.5/§9.7 plus pre-existing `historical`; no schema or validator enforces a closed `lifecycle_status` enum anywhere in the repository | **`CLOSED`** | Cleared |
| `P1-02` | Review 001 §18, §45; Registry §21.3 both records provider-scoped | Resolve entirely inside the Runtime: rename and re-own facts 5 and 6 as runtime-scoped record types; declare two disjoint capability vocabularies | Agent Runtime §14.1, §14.3 only | Registry blob `fa90b65b…` **byte-identical**; eight provider facts remain eight; §14.3 rule 5 forbids either record type from satisfying the other's fact in both directions; provider-side authorization exists **only** inside fact 10 | A run proposing no provider operation requires facts 1–8 only, never a `provider_id`, never a Registry record — the original "purely local run cannot be authorized" defect is eliminated; rule 6 fixes the capability vocabulary that fact 6 evaluates | **`CLOSED`** | Cleared |
| `P1-03` | Review 001 §30, §45; AI Ops §5.9 dedup by `run_id`, §5.1 one outcome/model/provider | Minimally amend the owner: `ledger_record_id` as deduplication identity; optional `attempt_id`; §5.9 rule that differing attempts are distinct records | AI Operations §5.1, §5.9; Runtime §25.1 consumes, does not define | §5.9 now reads "Records that share a `run_id` but differ in `attempt_id` are **distinct records and MUST NOT be deduplicated**"; `model`/`provider`/`outcome` attributed to the attempt when `attempt_id` is present | Searched the whole owner document for residual `run_id`-keyed dedup or one-outcome-per-run clauses: **none remain**; the only other dedup mention (edge-behavior table, "Duplicate event") is generic and consistent with the new identity; logical-run summary is derived and may never stand in for attempt evidence | **`CLOSED`** | Cleared |
| `P1-04` | Review 001 §16, §41 Scenario 15, §45 | Add the transition to the table for all three in-flight waiting states; declare the table closed; add §12.3.1 governing escalation | Agent Runtime §12.3, §12.3.1, §12.4, §23.6 | §12.3 lists `waiting_for_model → waiting_for_operator` explicitly; §12.3.1 fixes exactly four predecessors; §12.4 rules 11–12 agree with it; §23.6 adds a normative reachability paragraph | Replayed Scenario 15: resolves by a single listed transition with no intermediate hop; runtime may not select, rank, prefer, sample, or default; operator selection bounded to the recorded tied set; refusal or expiry → `blocked`, never a timeout default | **`CLOSED`** | Cleared |
| `P2-01` | Review 001 §22, §34, Scenario 25 | Mandatory declared, versioned, digest-bound staleness policy with six exact conditions | Agent Runtime §17.4 (new) | Materiality determined by **enumeration, never inference**; absent/unresolvable/expired policy → `blocked`; source unavailable → `blocked`; conflicting revision → `waiting_for_operator` | Replayed all eight staleness cases including `max_snapshot_age: null`, bounded operator exception, and expired exception: every one resolves deterministically; a material change requires a new envelope revision and renewed authorization, not a re-read | **`CLOSED`** | Cleared |
| `P2-02` | Review 001 §19, §45 | Remove the field from the envelope; make routing decisions step-scoped; add an explicit eight-step authorization sequence | Agent Runtime §15.3, §15.4 (new) | Envelope immutable **from construction**, not merely from attempt start; per-step routing decisions never enter, alter, or re-digest the envelope; no partial or "to be completed" field exists | Replayed the eight steps: original never mutated; revisions form an auditable chain with cycle/gap rejection; a changed decision, policy, or approval target invalidates the prior authorization; a stale approval is void for revision *N+1* | **`CLOSED`** | Cleared |
| `P2-03` | Review 001 §12, §30, §45 | Typed identity namespaces at the ledger boundary | AI Operations §5.1 (`run_kind`); Agent Runtime §8.4 (new) | Identity is the pair `(run_kind, run_id)`; a bare `run_id` is not a complete reference; agent form MUST NOT be constructed in or validated against the loop form; cross-kind lookup denies `RUN_KIND_MISMATCH` without fallback | `run_kind` absent means `loop_run`, preserving every existing record; linkage is a typed `triggering_run_ref`, never identity reuse; Loop Operations is neither renamed nor absorbed | **`CLOSED`** | Cleared |
| `P2-04` | Review 001 §25, §34, §45 | Single-winner atomic compare-and-set on the handoff record | Agent Runtime §20.4 (new) | Keyed by `handoff_id` with `acceptance_version` as expected-version precondition — the mechanism §29.2 already mandates; exactly one claim satisfies it | Replayed all seven race conditions plus package-revision supersession (row 6 via facts 1–8, Scenario 37): winner deterministic; losers create **no run at all**; budget reserved once and released deterministically; every claim and denial audited; an unreadable decision boundary denies rather than optimistically accepting | **`CLOSED`** | Cleared |
| `P2-05` | Review 001 §34, Scenario 42, §45 | Explicit takeover record plus a 16-row recovery matrix | Agent Runtime §29.3 (new) | Last durably recorded transition is authoritative; observed-but-not-appended evidence is absent, never inferred; a run without a takeover record is owned by no one | Replayed all twelve required recovery situations: rows 4, 6, 9, 11, 14 forbid dispatch outright; same-attempt resumption only on a *definitive* external status; a new attempt gets a new `attempt_id` and the interrupted attempt's evidence is never reused or rewritten; unreadable or inconsistent evidence → `blocked` with `evidence_state:unknown` | **`CLOSED`** | Cleared |
| `P3-01` | Review 001 §24 | Add a genuinely required 17th field rather than lowering the prose count | Agent Runtime §19 | `destination_run_id` added with a stated purpose (both-run attributability under §29.1) and an explicit `null` rule | Counted 17 numbered rows. **Fixed structurally, not editorially** | **`CLOSED`** | Cleared |
| `P3-02` | Review 001 §25 | State "exactly twelve" and correct the report | Agent Runtime §20.2; remediation report | Twelve contents enumerated inline; broadcast additionally carries `acceptance_deadline` and `acceptance_version` | Counted 12 | **`CLOSED`** | Cleared |
| `P3-03` | Review 001 §38 | Split the multi-class row; impose a one-class-per-row invariant | Agent Runtime §33, §1.4 | Rows and distinct class names stated separately and equal by construction | Counted 49 rows, 49 class tokens, **49 distinct, zero duplicates**. **Fixed structurally** | **`CLOSED`** | Cleared |
| `P3-04` | Review 001 §29, §14 | Define and own the class; state the mapping | Agent Runtime §33, §9.1 (new) | `INSUFFICIENT_PRICING_DATA` present in §33; §9.1 gives the exact nine-state ↔ eleven-fact correspondence | Verified the class is in the taxonomy and that states 2, 7, 9 have **deliberately** no fact, with the reason stated: an existence signal must never read as a grant | **`CLOSED`** | Cleared |
| `P3-05` | Review 001 §13 | Restate the rule language-neutrally; demote Python to illustration | Agent Runtime §8.3 rule 1 | Rule now requires an "exact-type identity check … language-neutral; each implementation language binds it to its own exact-type test", with Python marked *(Non-normative illustration)* | The normative requirement is unchanged in strength; only its expression is now implementation-neutral | **`CLOSED`** | Cleared |

**Result: 14 of 14 `CLOSED`. Zero `PARTIALLY_CLOSED`, zero `NOT_CLOSED`, zero
`REGRESSION_INTRODUCED`.**

## 12. Seam-decision review

All **18** required sections are present (§1–§18, with §18.1 a subsection). Each
P1 and each P2 has an explicit decision; every decision names the canonical
owner, bounds the Runtime's responsibility, states the selected resolution, and
names the changed documents.

The record was tested for the failure mode of a decision written to justify an
already-preferred edit. It does not exhibit it. §6.2 enumerates **five**
conforming alternatives and rejects each with a checkable reason — including
"omit `lifecycle_status` while executing", which §8.1 expressly permits and
which would have avoided amending the owner at all. That option is rejected on
the ground that it removes an executing run from every lifecycle filter, sort,
and module `Statuses` contract, which §8.2 requires to be a complete
cross-dimensional contract. Reusing `active` is rejected as reintroducing
precisely the ambiguity §8.2 exists to prevent; a seventh dimension is rejected
as contradicting Control Plane §24; a Runtime-local alias is rejected under the
record's own principle 2.

§11 and §12 partition the canonical owners into "requiring amendment" (two, with
justification) and "not requiring amendment" (eight groups, with the reason each
is untouched). §16 authorizes no implementation. §17 makes supersession explicit,
requires an ADR amendment under Gateway §33 rule 5 for any weakening change, and
— materially — forbids either owner amendment from being **widened by a later
task citing this record as precedent**. No ADR is silently superseded; the
Enterprise Provider ADR is explicitly listed as not superseded.

**No finding.**

## 13. Control Plane amendment review

Every changed line was reviewed. The amendment touches exactly four locations:
§8.1 (one enum member), §8.2 (one added clause), and the `Statuses` rows of
§9.5, §9.7, and §9.10.

| Requirement | Verified |
| --- | --- |
| Exactly one additive lifecycle member added | ✅ `running`, and only `running`, added to the §8.1 enum |
| Its semantics are explicit | ✅ "a live execution is in progress for this entity"; applies only to entities that can execute — currently `Run` |
| It does not replace or alias `active` | ✅ "`active` and `running` are therefore never interchangeable" |
| The `active` prohibition remains intact | ✅ The §8.2 `active` bullet is **unchanged**; the new clause restates the prohibition and adds "an executing agent run is `lifecycle_status:running`, never `lifecycle_status:active`" |
| No existing member's meaning changed | ✅ No other enum line is touched; the diff removes nothing |
| No seventh dimension created | ✅ Stated explicitly; Control Plane §24's six-dimension decision is untouched |
| Relevant Run module status sets contain the required values | ✅ §9.5 and §9.7 — the two modules whose `Key entities` include `Run` — carry all nine projected values plus `historical` |
| Unrelated module status sets were not broadened | ✅ See below |
| Prior statuses retain their meanings | ✅ No member removed from any module row; all three changes are strictly additive |
| Missing or unknown status remains fail-closed | ✅ §8.1's "no lifecycle `unknown` member; omit the field when inapplicable and expose missing lifecycle evidence separately" is unchanged |
| UI projection semantics remain truthful | ✅ Projection declared one-directional and lossy, with the finer-grained typed field authoritative |

**Bounding independently confirmed.** §9.8 *Batch Run and Artifact Queues* was
**not** given `running`, and this is correct rather than an oversight: its `Key
entities/fields` row is `QueueItem, Task, Artifact` and contains no `Run`, so it
falls outside the amendment's own scoping rule ("applies only to entities that
can execute — currently `Run`"). The module's name contains the word "Run", which
makes the omission a deliberate, entity-driven decision rather than a
name-driven one.

**The three added values beyond `running` are required, not scope creep.** §9.5
and §9.7 additionally gained `draft`, `queued`, and `ready`. The 17-row
projection targets exactly nine distinct lifecycle values, and `draft`,
`queued`, and `ready` are the projections of rows 1, 4, and 3 respectively.
Without them the projection would be unrenderable in the two Run-bearing
modules. The extension is therefore exactly minimal.

**Closed-vocabulary sweep.** A repository-wide search was performed for closed
lifecycle vocabularies, assumptions about status count, and validators or
schemas expecting the old set. Results: `lifecycle_status` appears in **no**
JSON schema and **no** Python module; **no** JSON file anywhere contains an
`"active"` enum value. The `lifecycle` matches in `scripts/loop_ops/**` and the
loop schemas concern loop-run lifecycle, not the Control Plane dimension. No
validator, schema, fixture, or table is invalidated by the amendment, and no
unaddressed closed vocabulary exists.

**No finding.**

## 14. Lifecycle vocabulary review

`run_state` remains a typed entity field, not a seventh status dimension, and
`lifecycle_status` remains owned by the Control Plane. Label reuse between
`lifecycle_status:running` and `run_state:running` is legitimate under Control
Plane §8.1's dimension-qualified machine identity, exactly as the owner already
permits for `Unknown`, `Expired`, and `Rejected`. The Agent Runtime defines no
status value of its own, adds no dimension, and introduces no local alias
(§12.1). **No finding.**

## 15. Lifecycle projection review

All seventeen states were reconstructed independently with predecessor,
successor, terminal/waiting/pending role, projected dimension and value,
evidence requirement, and reconciliation effect.

| # | `run_state` | Role | Projected `lifecycle_status` |
| --- | --- | --- | --- |
| 1 | `proposed` | entry | `draft` |
| 2 | `validated` | non-terminal | `planned` |
| 3 | `authorized` | non-terminal | `ready` |
| 4 | `queued` | non-terminal | `queued` |
| 5 | `starting` | non-terminal | `running` |
| 6 | `running` | non-terminal | `running` |
| 7 | `waiting_for_model` | waiting | `running` |
| 8 | `waiting_for_tool` | waiting | `running` |
| 9 | `waiting_for_agent` | waiting | `running` |
| 10 | `waiting_for_operator` | waiting | `blocked` |
| 11 | `cancellation_requested` | pending | `running` |
| 12 | `reconciliation_required` | pending | `blocked` |
| 13 | `completed` | **terminal** | `completed` |
| 14 | `failed` | **terminal** | `failed` |
| 15 | `cancelled` | **terminal** | `cancelled` |
| 16 | `timed_out` | **terminal** | `failed` |
| 17 | `blocked` | **terminal** | `blocked` |

Verified: exactly 17 states and exactly 17 projection rows; **zero** rows use
`active`; executing states use the canonical `running` member; `blocked` and
`reconciliation_required` remain distinguishable in `run_state` and §34 requires
both to be displayed by `run_state`, never only by projection; `timed_out`
projects to `failed` because the owner has no timeout member, while §12.4 rule 5
still forbids `timed_out` when any external outcome is unknown; terminal states
have zero successors; and every non-terminal state has at least one safe exit.
Waiting states remain distinguishable in the Runtime even though the UI
projection is coarser — which is the correct direction of loss.

## 16. Lifecycle transition review

The §12.3 table has 13 rows and is **declared closed**: "A transition that does
not appear in it is forbidden, whether or not §12.4 names it. There are no
implicit, derived, or convenience transitions, and no transition may be reached
by an unstated intermediate hop." This closure statement is itself a remediation
of the ambiguity Review 001 identified in `P1-04`, where neither reading of the
table's closedness was settled.

Every state is reachable from `proposed`; every non-terminal state has a safe
exit; terminal states are closed; `reconciliation_required` cannot become
terminal without a recorded reconciliation outcome; `cancellation_requested` is
never treated as `cancelled`; and `cancellation_requested → completed` remains
permitted and correctly fenced. §12.4's twelve forbidden rules contradict no
row of §12.3 — rule 10 restates the closure, and rule 11 restates §12.3.1's
predecessor set rather than contradicting it.

## 17. Routing-tie review

| Requirement | Verified |
| --- | --- |
| `waiting_for_model` may transition to `waiting_for_operator` | ✅ Listed explicitly in §12.3 |
| Every other intended waiting predecessor is listed | ✅ `waiting_for_tool` and `waiting_for_agent` also listed; §12.3.1 names exactly four predecessors including `running` |
| The transition table and the forbidden table agree | ✅ §12.4 rule 11 forbids any *other* predecessor and any release without a recorded, unexpired, action- and revision-bound decision |
| Tie detection emits evidence | ✅ §12.5 record with `reason_code: ROUTING_TIE_UNRESOLVED`, `actor: runtime`, the complete tied candidate set, and applied rules and precedence |
| No model is selected before resolution | ✅ §23.6 rule 1 — the runtime may not select, rank, prefer, sample, or default; §12.4 rule 12 forbids resolution by silent fallback, arbitrary or random selection, or a timeout default |
| Operator decision is scoped and revision-bound | ✅ §23.6 rules 2–3: selection confined to the recorded tied set (outside it → `MODEL_UNAUTHORIZED`), action-, revision-, and time-bound under §30.2 |
| Timeout or refusal has a deterministic result | ✅ §23.6 rule 5 → `blocked` with `ROUTING_TIE_UNRESOLVED` |
| Scenario 15 resolves fully | ✅ By a single listed transition, "No intermediate hop through `running` is used, implied, or permitted" |

A repository-wide search found **no** surviving statement forbidding the
transition. **No finding.**

## 18. Authorization-fact review

All eleven facts were reconstructed with owner, subject, action scope, tenant
scope, environment scope, capability vocabulary, evidence record, revision
binding, expiry, and denial class. The §14.1 / §14.2 split into **eight
run-admission** and **three per-invocation** facts is new and is structurally
enforced by §12.4 rule 3, which forbids entry to `authorized` without all eight
and states that facts 9–11 are neither evaluated nor satisfiable there.

| Requirement | Verified |
| --- | --- |
| Registry's original eight remain exactly eight | ✅ Stated in §14 preamble; Registry document byte-identical |
| Registry remains byte-identical | ✅ Blob `fa90b65b4f91545550247d81fc181eb10cca942a`, unchanged from Review 001's own baseline |
| Runtime facts 5 and 6 do not reuse provider-scoped record semantics | ✅ New record types `tenant_agent_runtime_authorization` and `tenant_agent_capability_authorization` |
| Agent-runtime tenant authorization is distinct from provider tenant authorization | ✅ §14.3 rule 5, stated in **both** directions |
| Agent capability authorization is distinct from provider capability authorization | ✅ §14.3 rule 6 — two vocabularies, "never resolved, matched, or substituted against the other"; violation denies `UNSUPPORTED_CAPABILITY` |
| Provider authorization remains delegated through the one Registry/Gateway fact | ✅ §14.3 rule 4; rule 5 confines provider-side tenant and capability authorization to fact 10 **only** |
| No aggregate readiness boolean exists | ✅ §14.3 rule 1 |
| Facts 1–8 and 9–11 have explicit evaluation points | ✅ §14.1, §14.2, §14.3 rule 3 |
| No fact is inferred | ✅ §14.3 rule 2 enumerates six non-implications |

The original defect's sharpest consequence is explicitly eliminated: "An agent
run that proposes no provider operation requires facts 1–8 only, never a
`provider_id`, and never a Registry authorization record." Facts 5, 6, 7, and 8
are separately revocable, mirroring Registry §21.2 rule 3 within the Runtime's
own set. **No finding.**

## 19. Registry compatibility

The Provider Registry Contract Extension is **byte-identical** to its Review 001
baseline. It is absent from the nine-path commit. Its eight facts, its §21.3
record types, its §21.2 rules, and its custody, lifecycle, issuance, and
revocation sections are untouched. Provider authorization ownership is not
duplicated anywhere in the remediated architecture. **No finding.**

## 20. AI Operations amendment review

Every changed line was reviewed. The amendment adds three fields to §5.1 and
rewrites §5.9.

| Requirement | Verified |
| --- | --- |
| `ledger_record_id` is the record identity | ✅ "It, not `run_id`, is the deduplication identity" |
| Optional `attempt_id` defined | ✅ `string \| null`; `null`/absent means a single-attempt domain — the existing loop behavior |
| Optional `run_kind` defined | ✅ `loop_run` \| `agent_run`; **absent means `loop_run`** |
| Deduplication behavior defined | ✅ Two deliveries sharing `ledger_record_id` are one record |
| Records with differing `attempt_id` are never collapsed | ✅ "**distinct records and MUST NOT be deduplicated**" |
| Repeated ingestion of the same record remains deduplicable | ✅ By `ledger_record_id` |
| Attempt evidence remains append-only | ✅ "never collapsed, overwritten, or discarded … intact, addressable, and independently readable" |
| A logical run can derive a summary without overwriting evidence | ✅ Derived, never stored as a replacement; may not erase, supersede, hide, or stand in for attempt evidence; where attempts disagree it reports the disagreement rather than selecting a truth |
| Model/provider attribution can be attempt-specific | ✅ When `attempt_id` is present, `model`, `provider`, and `outcome` are attributed to **that attempt** |
| Outcome can be attempt-specific | ✅ Same clause |
| Replay creates a distinct run | ✅ §5.9 — new `run_id` with a recorded link to source |
| Retry creates a distinct attempt | ✅ §5.9 — new `attempt_id` |
| Ordering evidence is preserved | ✅ Runtime §25.1 monotonic `sequence` per attempt; gaps surface as `evidence_state:partial` |

**Residual-contradiction sweep.** The complete owner document was searched for
surviving clauses implying one outcome per `run_id`, one model or provider per
`run_id`, deduplication only by `run_id`, or the absence of an attempt
dimension. **None remain.** The only other deduplication statement is the
edge-behavior row "Duplicate event — Deduplicated; state not advanced twice",
which names no key and is consistent with the new identity. The §5.1 `model`,
`provider`, and `outcome` fields are now explicitly attempt-attributed when an
attempt is present, which is precisely the clause Review 001 found missing.

**No finding.**

## 21. Run Ledger identity review

Agent Runtime §25.1 **consumes** the owner's identity model and explicitly does
not define one — "The Agent Runtime does not own, operate, or define a second
run ledger. Any design in which runtime evidence lives outside the canonical
Unified Run Ledger is non-conforming." Every emitted record carries
`ledger_record_id`, `run_kind: agent_run`, `run_id`, `attempt_id` (always
present for an agent run), `step_id` where step-scoped, monotonic `sequence`,
and separate `observed_at`/`recorded_at`. The producer-only posture Review 001
credited is preserved while the identity conflict is resolved at the owner.
**No finding.**

## 22. Attempt and deduplication review

Deduplication cannot collapse distinct attempts. The identity is
`ledger_record_id`; records sharing a `run_id` and differing in `attempt_id` are
normatively distinct on the owner's side (§5.9) and on the producer's side
(§25.1 consequence 1). A retry is additive and leaves the original attempt
intact and addressable; a replay is a new run, never a second attempt of the
source. Two attempts of one run may legitimately record different models,
providers, and outcomes, and both are true of their own attempt. The
audit-integrity defect Review 001 identified — loss of exactly the attempt
evidence §28 requires for reconciling unknown external outcomes — is eliminated.
**No finding.**

## 23. Loop compatibility

| Check | Result |
| --- | --- |
| Absent `attempt_id` behavior | `null` or absent means a single-attempt domain — existing loop behavior exactly |
| Absent `run_kind` behavior | Absent means `loop_run`, "preserving every existing record unchanged" |
| Loop ledger schemas | `shared_context/loops/RUN_LEDGER_SCHEMA.json` sets `"additionalProperties": true`; the three added fields are accepted without a schema change and none is added to `required` |
| Loop registry identity | Untouched; `LOOP_REGISTRY.json`, `LOOP_REGISTRY_SCHEMA.json`, `LOOP_STATE_SCHEMA.json` all byte-identical |
| Existing deduplication expectations | Preserved: "Where a record predates `ledger_record_id` and carries no `attempt_id` — including every existing loop run ledger — its identity is its `run_id` and this section's behavior is exactly as before" |
| Existing validators | `py -3.9 scripts/validate_project_state.py` → `PASS`, exit code `0` |
| Projection into AI Operations | Additive; no loop record requires modification |
| Loop runs never silently relabelled as agent runs | ✅ Absence defaults to `loop_run`; relabelling would require an explicit write |
| Agent runs cannot use loop-run identifiers without typed linkage | ✅ §8.4 — agent `run_id` MUST NOT be constructed in, parsed as, or validated against the loop form |
| Linkage is not identity reuse | ✅ `triggering_run_ref = (run_kind, run_id)`; "Identity is **referenced**, never **reused**" |
| `RUN_KIND_MISMATCH` deterministic | ✅ Cross-kind lookup denies; "it does not fall back or return empty"; present in the §33 taxonomy |
| No loop schema change was silently required | ✅ Confirmed by `additionalProperties: true` and by all four loop artifacts remaining byte-identical |

Loop Operations semantics are unaltered. **No finding.**

## 24. Execution-envelope sequencing

The eight-step §15.4 sequence was replayed against the required order.

| # | Step | Produces | State |
| --- | --- | --- | --- |
| 1 | Run request | `run_id`, `run_kind: agent_run` | `proposed` |
| 2 | Initial validation | Envelope revision 1, digest-bound, `bound_routing_decision_ref: null` | `validated` |
| 3 | Pre-authorization routing request (only when policy requires pre-binding) | Routing request artifact | `validated` |
| 4 | Routing decision | Immutable, digest-bound artifact | `validated` |
| 5 | Resolved revision | Envelope revision 2, supersedes revision 1, new digest | `validated` |
| 6 | Renewed validation | Structural re-validation of the current revision | `validated` |
| 7 | Authorization | Facts 1–8 against the current revision's exact digest | `authorized` |
| 8 | Dispatch eligibility | Admission for scheduling | `queued` |

Verified: the original envelope is never mutated (invariant 1, and §15.3's
"immutable from the moment it is constructed"); the routing decision is
digest-bound; revisions form an auditable chain via
`supersedes_envelope_revision_id`, with a cycle, gap, or unresolvable
predecessor rejected as `ENVELOPE_INTEGRITY_FAILED`; a changed model decision
produces a new digest; a policy-boundary crossing under §23.4 forces a new
revision, a new attempt, and renewed authorization; a changed approval target
voids the approval (`APPROVAL_STALE`); stale authorization cannot dispatch a new
revision, because §15.3 rule 3 re-evaluates all eight facts in full; superseded
revisions remain stored, addressable, and auditable; and optional fields cannot
bypass the sequence, because no partial, provisional, or "to be completed" field
exists — a field not yet knowable is absent or `null` **and stays that way for
the life of that revision**.

The `P2-02` contradiction is resolved by relocation rather than by weakening: a
post-authorization routing decision is a step-scoped artifact that "never
enters, alters, or re-digests the envelope." **No finding.**

## 25. Shared Context staleness

The six §17.4 conditions were replayed across the eight required cases.

| Replay | Resolution |
| --- | --- |
| Fresh snapshot | Condition 1 → proceed on the held snapshot |
| Stale but refreshable | Condition 2 → proceed only on a **freshly read replacement** with a new `context_snapshot_id` |
| Materially stale | Condition 3 → `blocked`, `STALE_STATE` |
| Source unavailable | Condition 5 → `blocked`, `evidence_state:unknown` |
| Conflicting revision | Condition 6 → `waiting_for_operator`, operator adjudication |
| Policy without time threshold | `max_snapshot_age: null` = "age is never sufficient grounds"; outcome falls to the deterministic materiality test |
| Approved bounded exception | Rule 5 — one exact `context_snapshot_id` and digest, one named run, time-bound, recorded |
| Expired exception / expired policy | Condition 4 → `blocked` |

Verified: a stale snapshot is never used automatically; materiality is
determined by **enumeration, never inference**, and any change to a field the
authorization, read scope, or output contract depends on is material regardless
of enumeration; absence fails closed with no default policy and no substituted,
cached, partial, or nearest-available context; refresh is replacement producing
new evidence and a §19 trace record; the operator exception never generalizes to
another snapshot, run, or class and never converts a material change into a
non-material one; and a material change requires a new envelope revision and
renewed authorization rather than a re-read. Scenario 25 resolves fully.
**No finding.**

## 26. Agent-run and loop-run identity

Identity is the pair `(run_kind, run_id)`; a bare `run_id` is not a complete run
reference at any trust boundary. Every agent identifier the runtime emits — in
envelopes, handoffs, events, ledger records, audit records, and operator
projections — carries `run_kind: agent_run`. Substitution in either direction is
forbidden and denies `RUN_KIND_MISMATCH`. Because uniqueness is per-namespace, a
value resolving in both namespaces is a `DIGEST_COLLISION_SUSPECTED`-class
integrity event, not a match. Sub-runs are agent runs distinguished by
`sub_run_id` and explicit parentage, never by a different kind. **No finding.**

## 27. Broadcast concurrency

The §20.4 model is single-winner with an atomic compare-and-set on the handoff
record, keyed by `handoff_id` with `acceptance_version` as the expected-version
precondition — reusing the optimistic-concurrency mechanism §29.2 already
mandates rather than inventing a new one. Acceptance is two-part and only the
second part is decisive; §14.1 facts 1–8 are evaluated by the receiving runtime
first, so a claim is never submitted on an unauthorized basis.

All seven conditions replayed, plus package-revision supersession (resolved by
row 6 together with Scenario 37 → `PACKAGE_MISMATCH`). Verified: exactly one
claim satisfies the precondition; losers create **no run at all** and never
instantiate an agent, read context, or emit a step; budget is reserved once at
broadcast creation and only the winner draws it, with release to the parent
recorded on expiry, withdrawal, or no acceptance; every claim and denial is
appended append-only with its reason class and losing evaluation evidence is
retained; cancellation propagates to the winner only; and racing grants nothing —
the winner's effective scope remains the intersection of the handoff scope and
its own authorizations, so no permission, context class, tool, provider, model,
or budget is widened by accepting first.

Rule 7 handles the unknown atomic boundary in the strongest available way: if
the handoff record is unreachable or its version unreadable, **no acceptance
occurs**, the claim denies, and no run is created — "There is no optimistic
acceptance pending confirmation." Because no run is created, no external effect
exists to reconcile. **No finding.**

## 28. Restart and recovery

All sixteen §29.3 rows were reviewed against the twelve required situations.

| Required situation | Resolution |
| --- | --- |
| No dispatch evidence | Rows 1–2 → unchanged/`queued`, dispatch only after re-evaluating facts 1–8 |
| Dispatch evidence, known framework status | Rows 3, 5, 7, 8, 10, 13 → resume or settle |
| Dispatch evidence, unknown status | Rows 4, 6, 9, 11, 14 → `reconciliation_required`, dispatch **forbidden** |
| Framework lacks a status query | "An unsupported query, an error, a timeout, or an ambiguous answer is **not** evidence of absence and yields `unknown`" |
| External tool may still be running | Row 9 |
| Provider proposal may have been dispatched | Rows 6 / 9 |
| Completion evidence exists but was not summarized | Row 8 → return to `running` with the retrieved result recorded |
| Conflicting completion events | Rule 8 → `blocked` with `evidence_state:unknown`; never reconstructed by inference |
| Cancellation requested before restart | Rows 13–14 |
| Approval expired during outage | Re-evaluation of facts 1–8 (fact 8 carries explicit expiry) |
| Package revision changed during outage | Re-evaluation of facts 2–4 → `PACKAGE_MISMATCH` |
| Policy revision changed during outage | Re-evaluation of facts 1–8 plus §17.4 staleness |

Verified: no blind redispatch (rule 1); unknown state enters reconciliation;
resume requires *definitive* evidence and preserves `attempt_id` and the
monotonic `sequence` (rule 2); a new attempt receives a new `attempt_id` and the
interrupted attempt's evidence is never reused, rewritten, or continued (rule
3); the old attempt remains visible; operator involvement is bounded, with a
deterministic permanent-block path when reconciliation cannot establish the
outcome and the operator declines (rule 6); recovery never revives a terminal
run or back-fills any record (rule 7); and takeover is explicit — "A run without
a takeover record is not owned and is not advanced by anyone." Scenario 42
resolves fully. **No finding.**

## 29. Count and terminology review

Every count in §1.4 was recalculated mechanically from the document's own tables
(Section 9.1). All match. Three points are material to the "prose-only
correction" risk this review was directed to test:

1. **`P3-01` was fixed structurally.** The trace record did not have its prose
   count lowered to 16; a seventeenth field, `destination_run_id`, was added
   with a stated purpose and an explicit `null` rule.
2. **`P3-03` was fixed structurally.** The multi-class row was split so that
   rows and distinct class names are equal by construction, and §33 makes the
   one-class-per-row property normative. Independent counting confirms 49 rows,
   49 class tokens, 49 distinct names, and zero duplicates.
3. **§1.4 is itself normative and self-enforcing:** "a future amendment that
   changes a table MUST recompute and restate the corresponding row here, and
   any divergence between this table and the referenced section is a defect."

Normative wording is implementation-neutral; the Python construction in §8.3
rule 1 is now explicitly a *non-normative illustration*. **No finding.**

## 30. Error taxonomy review

49 rows, 49 distinct class names, no duplicates. Ownership is stated at section
level: Gateway §25.2 classes are adopted unchanged for the provider boundary and
are "not restated or fragmented here"; the classes listed are Agent Runtime-layer
classes added only where the Gateway set has no equivalent. Every class cited by
a remediated section exists in the table — verified individually for
`RUNTIME_AUTHORIZATION_DENIED`, `CAPABILITY_AUTHORIZATION_DENIED`,
`UNSUPPORTED_CAPABILITY`, `RUN_KIND_MISMATCH`, `HANDOFF_ALREADY_ACCEPTED`,
`HANDOFF_EXPIRED`, `HANDOFF_WITHDRAWN`, `INSUFFICIENT_PRICING_DATA`,
`ROUTING_TIE_UNRESOLVED`, `EXTERNAL_OUTCOME_UNKNOWN`, `STALE_STATE`, and
`ENVELOPE_INTEGRITY_FAILED`. Cloudflare `P3-01`'s separation of
`INVALID_REFERENCE_SHAPE`, `INVALID_CANONICAL_TYPE`, and
`SENSITIVE_VALUE_REJECTED` is preserved. **No finding.**

## 31. Original scenario replay

All 32 original scenarios were replayed against the reconstructed matrices. The
two that Review 001 found unresolved are now resolved:

- **Scenario 15** — resolves via the listed `waiting_for_model →
  waiting_for_operator` transition, governed by §12.3.1, with no intermediate
  hop and no runtime tie-breaking.
- **Scenario 25** — resolves by the §17.4 condition table; the outcome is fixed
  by condition number rather than by an undefined policy branch.

The remaining 30 continue to resolve as Review 001 recorded, with no regression
introduced by the remediation. Scenarios 19–21, 23, and 30 retain their
reconciliation obligations. **32 of 32 resolve.**

## 32. Additional scenario replay

Scenarios 33–42 are now carried in the specification itself as §38.1 — an
improvement, since Review 001's ten adversarial scenarios previously existed only
in the review record. **Scenario 42**, the one Review 001 found undefined,
resolves via the §29.3 recovery matrix with an explicit `RUNTIME_INSTANCE_LOST`
class, a recorded takeover, no blind redispatch, and reconciliation on every
unknown branch. **10 of 10 resolve.**

**Total: 42 of 42 deterministic scenarios resolve without architectural
interpretation.** IDs 1–42 are present with no gaps and no duplicates.

## 33. Agent Package implementability

Can `MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` be written without reopening
Agent Runtime architecture?

| Package concern | Fixed by the architecture? |
| --- | --- |
| Package identity | ✅ `agent_package_id`, `package_revision_id` (§8.1) |
| Manifest | ✅ §10.1 minimum metadata |
| Package provenance | ✅ `package_provenance` with source, build, signer, digest, verification evidence |
| Framework type | ✅ Closed six-member vocabulary (§11.1) |
| Entrypoint reference | ✅ Opaque, bridge-interpreted |
| Declared capabilities | ✅ **Now resolved** — §14.3 rule 6 fixes the agent capability vocabulary that fact 6 authorizes and makes it disjoint from the provider vocabulary |
| Tool requirements | ✅ `declared_tools` with exact identifiers and revisions |
| Context requirements | ✅ `required_context_classes` / `produced_context_classes`, plus the §17.4 staleness policy reference |
| Output contracts | ✅ `output_contract_ref` (§15.1), `normalize_result` (§16) |
| Permissions | ✅ **Now resolved** — `permission_requirements` intersect downward against a runtime-scoped tenant authorization whose record type and scope are defined (§14.1 facts 5–6) |
| Model requirements | ✅ Capability class, context window, modality, quality floor; never a model-name binding |
| Provider requirements | ✅ Delegated through fact 10 only |
| Budgets | ✅ `resource_limits`, stricter-of-package-and-policy; broadcast carving fixed by §20.4 |
| Cancellation posture | ✅ `cancellation_support`, bridge-corroborated, defaulting to `constrained` |
| Replay posture | ✅ §13 rules 4–5 plus §25.1 consequence 3 (replay is a new `run_id`) |
| Sensitivity | ✅ `sensitivity_posture` from the canonical vocabulary |
| External-content posture | ✅ `external_content_posture` (§32) |
| Installation and verification states | ✅ §9's nine states with §9.1's explicit fact correspondence |

**All eighteen concerns are specifiable without architectural invention.** The
two that Review 001 blocked on (`declared_capabilities` and
`permission_requirements`) are resolved by `P1-02`'s closure; the projection and
ledger questions a Package Contract author needed answered are resolved by
`P1-01` and `P1-03`; and the Framework Bridge author's open questions are
resolved by `P2-02` (§15.4) and `P1-04` (§12.3.1). **Zero concerns require
reopening architecture.**

## 34. New findings

### P0 — Critical

**None.** No cross-tenant ambiguity, no authorization bypass, no
canonical-context mutation bypass, no path by which attempt evidence can be
erased, no blind redispatch of consequential work, and no credential or provider
access was introduced.

### P1 — Blocking

**None.** No original P1 remains open or partially closed; no owner amendment
changed unrelated semantics; lifecycle projection is compatible and
deterministic; authorization ownership is not duplicated; attempts cannot be
deduplicated away; loop and agent identities are not substitutable; every
required transition is reachable; no scenario requires interpretation; and the
Agent Package Contract requires no architecture invention.

### P2 — Material, non-blocking

**None.**

### P3 — Editorial / maintainability

**`NEW-P3-01` — §12.2 projection note 5 overstates renderability in Control
Plane §9.10.**
Note 5 states: "Every projected value is renderable by Control Plane §9.5, §9.7,
and §9.10, whose Run lifecycle sets were extended for exactly this purpose."
This holds for §9.5 and §9.7, whose extended sets contain all nine distinct
projected values. It does **not** hold for §9.10 (Operator Console), whose
lifecycle set is `planned`, `queued`, `ready`, `active`, `running`, `blocked`,
`completed`, `failed`, `historical` — omitting `draft` (the projection of row 1,
`proposed`) and `cancelled` (row 15).

*Assessment.* This is an inaccurate completeness claim, not a semantic
incompatibility. §9.10 is explicitly an "explicitly cross-dimensional summary"
rather than a Run-rendering module, and it did **not** enumerate `cancelled`
before the amendment either, although Runs could already be `cancelled` — so its
set was never an exhaustive Run vocabulary and the amendment did not make it
less complete. The two Run-bearing modules render every projected value, and §34
independently requires operator surfaces to display `run_state` rather than only
the projection. No lifecycle state becomes unrenderable, no prohibition is
weakened, no scenario is affected, and the Agent Package Contract is unaffected.

*Classification:* P3 — editorial accuracy in a non-normative note. Behavior and
downstream implementability are unaffected. It is recorded, not repaired; this
review repairs nothing.

## 35. Finding counts

| Severity | Count | IDs |
| --- | --- | --- |
| **P0** | **0** | — |
| **P1** | **0** | — |
| **P2** | **0** | — |
| **P3** | **1** | `NEW-P3-01` |

Review 001 closure: **14 of 14 `CLOSED`.**

## 36. Gate decision

### `PASS_WITH_NON_BLOCKING_FINDINGS`

P0 = 0 and P1 = 0. All fourteen Review 001 findings are independently `CLOSED`,
with every original P1 closed in full rather than partially. No canonical owner
conflict remains. One new non-blocking P3 constraint remains (`NEW-P3-01`), and
the Agent Package Contract can proceed safely under it — the finding is an
inaccurate completeness claim in a non-normative note and constrains nothing
about package definition.

Each PASS condition was tested independently and each is met: the seam-decision
record is complete (18 sections) and internally consistent; the Control Plane
amendment is minimal, additive, and semantically compatible, adding exactly one
lifecycle member and extending only the Run-bearing module sets by exactly the
values the projection requires; the AI Operations amendment is minimal,
additive, and does not collapse attempt evidence; the Provider Registry remains
byte-identical and the sole owner of provider authorization; the lifecycle
projection is deterministic and uses `active` nowhere; every required transition
is reachable through a listed transition with no unstated hop; and all 42
scenarios resolve without interpretation.

The outcome is `PASS_WITH_NON_BLOCKING_FINDINGS` rather than `PASS` solely
because this review introduced one new P3 finding. The distinction is recorded
honestly rather than resolved in the remediation's favour; the downstream effect
is identical.

## 37. Architecture acceptance

`MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_001` is **accepted as the canonical
architectural foundation** for the Agent Runtime track, under the single
non-blocking constraint recorded as `NEW-P3-01`. Both owner amendments are
accepted as minimal, additive, and bounded to the sections listed in
seam-decision §11.

## 38. Agent Package eligibility

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001` is **eligible for separate Operator
authorization**, under the constraint in `NEW-P3-01`. Eligibility is not
authorization: the Package Contract remains a documentation-only task and
requires its own explicit Operator authorization before it starts.

This review authorizes no Agent Package implementation, no Agent Runtime
Scaffold, no framework bridges, no agent execution, no model calls, no
providers, no tools, no credentials, and no deployment.

## 39. Implementation status

Nothing is implemented and nothing was implemented, connected, or executed by
this review. No Agent Runtime, agent registry, agent package, framework bridge,
or scaffold exists. No agent framework is installed, imported, connected, or
executed. Zero agents have been executed. No model provider is connected and no
model-provider call has occurred. No tool is connected or invoked. No provider is
connected, registered, authenticated, or enabled. No credential is configured. No
context or memory backend, queue, or frontend is implemented. No deployment
occurred. Agent Runtime implementation remains blocked.

## 40. Live provider status

Live provider work remains **blocked and unauthorized**. Gateway §32's
seventeen-item runtime-enablement gate still governs and none of it passes.
Cloudflare Review 002 `P2-04` remains carried forward and explicitly unresolved
(§22.5); this review does not adjudicate it. Migration triggers #1, #4, #5, #6,
and #7 remain uncrossed.

## 41. Exact next task

`MELLYCORE-AGENT-PACKAGE-CONTRACT-SPEC-001`

A documentation-only Agent Package Contract specification, eligible for separate
Operator authorization under the constraint in `NEW-P3-01`. It is not started,
not authorized by this review, and not an implementation task.

The global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` is unchanged, not
reordered, and not reinterpreted. The Agent Runtime review is a separate
product-development track.

## 42. Explicit non-authorizations

This review authorizes none of: Agent Runtime implementation; framework bridge
implementation; Agent Package Contract, Framework Bridge Contract, or Shared
Context Bridge drafting; Agent Runtime Scaffold work; agent framework SDK
installation, vendoring, or dependency declaration; execution of any agent,
sub-agent, workflow, graph, crew, or conversation; any model-provider API call;
any tool invocation; any provider connection, authentication, credential
configuration or verification, OAuth flow, or token creation; any MCP or
integration-fabric connection or webhook registration; persistence, database, or
queue implementation; backend or frontend implementation; dependency
installation, workflow YAML, release, or deployment; any push, pull request,
merge, or remote branch; or any MellyTrade interaction.

## 43. Validation evidence

| Check | Result |
| --- | --- |
| `py -3.9 scripts/validate_project_state.py` | `PASS MellyCore project scaffold validation passed`, exit code `0` |
| `git diff --check` | Recorded in the final execution report |
| `git status --short`, `git diff --name-only`, `git diff --stat` | Recorded in the final execution report |
| Files changed | Exactly six, all within the approved allowlist |
| All nine remediation files byte-identical | ✅ Verified against the Section 9 baselines |
| Architecture Review 001 byte-identical | ✅ Blob `751e705457340157e6914148d72fc380f0e7cbe6` unchanged |
| Unchanged canonical owners byte-identical | ✅ All nine verified, including Provider Registry `fa90b65b…`, Integration Gateway, Operations Data Contract, Loop Operations Architecture, and all Shared Context contracts |
| Source or test files changed | **None** |
| Review record sections | 45 |
| Reviewed documents | 5 reviewed (spec, seam decision, two owner amendments, remediation report) + 18 canonical cross-check sources |
| Closure rows | 14 |
| Lifecycle states / projections | 17 / 17 |
| Authorization facts | 11 (8 run-admission + 3 per-invocation) |
| Recovery matrix rows | 16 |
| Original / additional / total scenarios | 32 / 10 / **42** |
| Error rows / unique classes | 49 / 49 |
| Finding counts | P0 = 0, P1 = 0, P2 = 0, P3 = 1 |
| Introduced secret-pattern count | 0 |
| `pytest` | `NOT_RUN` |
| Reason tests were not applicable | This review changes no source or test file and introduces no executable behavior. The existing suite is unaffected by a documentation-only change and would produce no evidence about it. Reported as `NOT_RUN`, never as passing |
| Unavailable validators | Black, flake8, and mypy were not run and are not claimed passing. No dependency was installed |

Every P0/P1 blocks the gate; PASS is impossible with a P0 or P1 outstanding; the
gate decision matches the finding counts; the shared-context next task matches
the gate; the Agent Package eligibility wording matches the gate; implementation
remains blocked; live provider work remains blocked; and the global pointer is
unchanged.

## 44. Amendment and supersession

This review record is amended only by an explicit, Operator-approved successor
review that names it and states exactly what changes. Superseded content is
retained and marked, never deleted. A future task does not amend this record; it
produces its own record. `NEW-P3-01` is recorded, not repaired: any correction
belongs to a separately authorized task under the Agent Runtime specification's
own §42 amendment rules, and correcting it does not require reopening the
architecture gate.

## 45. References

### 45.1 Reviewed

- `docs/specs/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001.md`
- `docs/decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001.md`
- `docs/specs/MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC.md` (amendment)
- `docs/specs/MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001.md` (amendment)
- `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REMEDIATION-001.md`

### 45.2 Finding sources

- `docs/research/MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_REVIEW_001.md`
- `docs/tasks/MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-REVIEW-001.md`

### 45.3 Canonical cross-check sources

- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001.md`
- `docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md`
- `shared_context/loops/RUN_LEDGER_SCHEMA.json`, `LOOP_STATE_SCHEMA.json`,
  `LOOP_REGISTRY_SCHEMA.json`, `LOOP_REGISTRY.json`
- `shared_context/CONTEXT_GRAPH_SCHEMA.md`, `CONTEXT_PACK_GENERATOR_SPEC.md`
- `shared_context/context_provenance/**`
- `shared_context/SAFETY_CONTRACT.md`, `VALIDATION.md`, `MODEL_ROUTING.md`
- `shared_context/PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
  `AGENT_HANDOFF.md`

### 45.4 External

None. No external source was fetched. No framework documentation, SDK, or
service was consulted, installed, or contacted during this review. The only
network operation was one authorized read-only `git fetch clean-origin`.
