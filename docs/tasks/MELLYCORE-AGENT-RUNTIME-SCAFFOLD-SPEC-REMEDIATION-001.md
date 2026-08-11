# MellyCore Agent Runtime Scaffold Spec Remediation 001 — Task Report

## 1. Task identity and Operator authorization

- Task ID: `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001`
- **Authorized by explicit Operator authorization in this session**, scoped to
  remediation of findings recorded by
  `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001`.
- **Explicitly not authorized, and not performed:** scaffold implementation;
  source-code creation; test-code creation; Python package creation; dependency
  changes; Runtime execution; framework integration; provider integration;
  Shared Context access; network operations; push; PR creation; merge;
  deployment.

| Item | Authorized value |
| --- | --- |
| Specification edited | `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md` (1.0 → **1.1**) |
| Task report | `docs/tasks/MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001.md` |
| Branch | `docs/mellycore-agent-runtime-scaffold-spec-remediation-001` |
| Commit subject | `docs: remediate inert agent runtime scaffold spec` |

## 2. Repository baseline

- Root: `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios`
- Starting branch: `docs/mellycore-agent-runtime-scaffold-spec-review-001`
- Starting HEAD: `0969a316a23e2dee0ef04e92746638b059832ffc` (short `0969a31`)
- Latest subject at start: `docs: review inert agent runtime scaffold`
- Starting worktree/index: clean
- Upstream tracking: **none**
- Remotes `origin`, `clean-origin` — **neither contacted**
- Branch created from verified HEAD `0969a31`:
  `docs/mellycore-agent-runtime-scaffold-spec-remediation-001` (did not
  previously exist)

**No network operation occurred at any point in this task.**

### 2.1 Git-scope protection

`C:\` is itself a separate Git repository with unrelated local changes. **Every
Git command was explicitly scoped** with
`git -C "C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios"`. **No unscoped Git
command ran**, and the outer `C:\` repository was never inspected, staged,
reset, cleaned, or committed.

### 2.2 Implementation absence confirmed

A repository-wide search for `agent_runtime_scaffold`, `AgentRuntimeScaffold`,
`RuntimePort`, `composition_root`, `CompositionRoot`, and `InertRuntime` across
`scripts/`, `tests/`, and `site/` returned **zero matches**; no scaffold package
or test file exists; the tracked `scripts` + `tests` file count is **71**,
unchanged.

## 3. Review 001 gate and counts consumed

**`PASS_WITH_NON_BLOCKING_FINDINGS` — P0 = 0, P1 = 0, P2 = 7, P3 = 5.**
Verified directly from
`docs/research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_001.md` lines 10–11,
and by counting the enumerated finding headings (7 P2, 5 P3). The reviewed
specification was at version 1.0.

## 4. Complete finding inventory

All twelve findings were reconstructed from the committed review record — not
from the task prompt and not from prior summaries. Exact IDs, severities,
locations, owners, and required corrections were parsed mechanically from the
record's finding blocks.

| Finding | Severity | Exact specification location | Canonical owner | Required correction (verbatim intent) |
| --- | --- | --- | --- | --- |
| `NEW-P2-01` | P2 | §31 | This specification | Restrict rule 2 to the fail-closed conjunct; keep the zero-side-effect conjunct scoped to the default, uninjected composition |
| `NEW-P2-02` | P2 | §31 rule 3; §34 obligations | This specification | Add an invariant obligation; correct the citation; add zero-filesystem-read, logging-silence, deferred-effect and randomness obligations |
| `NEW-P2-03` | P2 | §8 rule 4, against §3 row 1 and §17 prohibition 2 | **Agent Runtime §37** | Attribute the first sentence to Runtime §37; keep the second sentence scaffold-owned; re-point §17 prohibition 2 at the owner |
| `NEW-P2-04` | P2 | §32, §39, whole document | **Agent Runtime §37** | Add queues to non-goals and add a §32 category or explicit §6 exclusion |
| `NEW-P2-05` | P2 | §27 field 12 and §27 rule 4 | This specification | Scope the field to what the scaffold can establish; render `unknown` when a port is injected |
| `NEW-P2-06` | P2 | §10, against §7 rule 3 | This specification | Prohibit executable content; state that "declared injected port names" is descriptive metadata, not a resolution mechanism |
| `NEW-P2-07` | P2 | §9 | This specification | Extend §9 to cover lazy/cached properties, finalizers, default factories, descriptors and class-creation hooks; pair with test obligations |
| `NEW-P3-01` | P3 | tracked canonical state | — | Record the outcome code in a tracked file |
| `NEW-P3-02` | P3 | bare `§37` references | — | Qualify every cross-document reference |
| `NEW-P3-03` | P3 | §8 | — | Add a filesystem-read row; extend rule 4 to non-importing presence detection |
| `NEW-P3-04` | P3 | §26 | — | State which states are reachable in the inert default |
| `NEW-P3-05` | P3 | §32 | — | Add a logging-output category and a randomness determinism rule |

**Every finding has exactly one disposition. No alternative finding ID was
minted. No finding was deferred, waived, or partially closed.**

## 5. Finding-by-finding correction matrix

| Finding | Original problem | Correction applied | Specification section | Owner preserved | Verification |
| --- | --- | --- | --- | --- | --- |
| `NEW-P2-01` | §31 rule 2 demanded the invariant hold "regardless of … injected ports" while the invariant itself was scoped to "no externally injected implementations" | §31 split into **§31.1 Baseline Inert Invariant** (scoped to a three-condition *baseline inert composition*) and **§31.2 Injected Component Eligibility**. §31.1 rule 2 now states the scope is exact and that the invariant makes **no claim** about injected live implementations. §31.2 rule 4 isolates the one property that does hold regardless — the §15 execution refusal | §31.1, §31.2 | This spec | Scope-contradiction scan: the three surviving "regardless of" hits are the execution refusal (§15 rule 3), §31.2 rule 4, and acceptance criterion 32 |
| `NEW-P2-02` | The invariant was asserted by no test; §31 rule 3 cited obligation 12 (zero-context-mutation); the spec's own task report said 13 | Added **obligation 18** asserting §31.1 in full with side-effect sentinels; §31.1 rule 3 now cites it. Added obligations **19** (zero-filesystem-read), **20** (logging silence), **21** (deferred effects), **22** (zero-queue), **23** (determinism), **24** (injected-component non-inheritance). New §34 rules 4–5 state that 18 asserts the whole and 2–12/19–23 assert conjuncts | §31.1 rule 3, §34 | This spec | Obligations recount: 17 → **24**; §31.1 rule 3 cites obligation 18 |
| `NEW-P2-03` | §8 rule 4 restated a Runtime §37 must-not item uncited; §17 cited §8 rule 4 as the authority | §8 rule 4 now opens **"Per Agent Runtime Architecture §37, which prohibits 'any framework SDK import on any reachable path', the following subordinate implementation constraint applies"**, with the presence-testing sentence explicitly marked *"Additionally, and owned by this specification"*. §17 prohibition 2 re-pointed at **Agent Runtime Architecture §37** | §8 rule 4, §17 | **Agent Runtime §37** | Ownership audit: restatement is cited and labelled subordinate; §17 names the owner |
| `NEW-P2-04` | "Queues" — one of §37's eleven must-not items — appeared nowhere; no §32 category could detect one | Queue treatment added to **all seven required areas**: §8 row 16 (import), §9.1 row 18 (deferred), §32 row 21 (category) and rule 7, §31.1 invariant text, §34 obligation 22, §37 threat 20, §39 non-goal 19 | §8, §9.1, §31.1, §32, §34, §37, §39 | **Agent Runtime §37** | Queue audit: mentions in §8 (2), §9 (2), §31 (2), §32 (11), §34 (4), §37 (2), §39 (2) — all present |
| `NEW-P2-05` | "Zero-execution confirmation" was an unscoped claim about the world that could become false under injection | Renamed to **Scaffold Zero-Execution Evidence** and given a normative **§27.1** with eight required properties: derived not asserted; scoped to one correlation ID or validation run; explicitly non-canonical; not a Control Plane dimension; states only what its evidence boundary covers; not a Runtime run result; not equivalent to Runtime success; **not emitted when evidence is incomplete**. Rule 2 requires `unknown` for every category an injected port could affect; rule 4 forbids fabricating a live run identifier | §27 field 12, §27.1 | This spec | Old name appears only in the renaming sentence; all eight properties present |
| `NEW-P2-06` | §10's eight prohibitions omitted executable content while permitting "declared injected port names" | Prohibitions extended **8 → 22**, adding rows 9–22: import-by-string paths, executable callbacks, serialized callables, pickled objects, dynamic expressions, template expressions, shell commands, subprocess arrays, plugin entry points, framework auto-import directives, module-level factory names, code snippets, deserialization hooks, and secret/executable environment interpolation. New rule 5 requires **fail-closed rejection** (wired into §30 layer 5); rule 6 states "declared injected port names" is **inert descriptive metadata, never a resolution mechanism**; rule 7 permits a static symbolic reference only under five conditions | §10, §30 layer 5 | This spec | Configuration prohibitions recount: 8 → **22**; fail-closed rejection stated |
| `NEW-P2-07` | §9 governed constructors only; deferred mechanisms could bypass it | New **§9.1 "Deferred construction effects"** enumerating **nineteen** mechanisms (`__post_init__`, lazy and cached properties, descriptors, class-level registration, metaclass hooks, default factories, callable defaults, dependency factories, finalizers, sync and async context-manager entry, background and scheduled callbacks, deferred imports, deferred socket/thread/process/**queue** creation, first-method-call init) with four rules binding them to §32 exactly as constructors are | §9.1 | This spec | Nineteen rows present; §34 obligation 21 covers them |
| `NEW-P3-01` | Outcome code recorded in no tracked file | `AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED` now recorded in the specification header, this report, `TASK_INDEX.md`, `PROJECT_STATE.md`, and `PROJECT_HISTORY.md`, framed as the **pre-review** outcome superseded by Review 001 | Spec header; state files | — | Tracked-file search now returns matches |
| `NEW-P3-02` | `§37` ambiguous between this document's §37 (Security) and Runtime §37 | All fifteen cross-document references rewritten as **"Agent Runtime Architecture §37"**, plus a normative **reference convention** in §1.1 stating that a bare `§37` always denotes this document's own §37 | §1.1 and throughout | **Agent Runtime §37** | Ambiguity scan: no bare cross-document `§37` remains |
| `NEW-P3-03` | §8 omitted filesystem reads and non-importing presence testing | Import prohibitions extended **12 → 19**, adding row 6 (**read a file**, distinct from row 8 mutate), row 7 (**scan/enumerate a directory**), row 12 (**probe for SDK/package/distribution/entry-point presence** by file test, metadata query, or package-manager access). New rule 5 permits only import-system-supplied metadata that performs no additional access | §8 | This spec | Import prohibitions recount: 12 → **19**; rows 6, 7, 12 present |
| `NEW-P3-04` | §26 did not say which cancellation states are reachable inertly | §26 gained a **reachability column** per state, an explicit **unreachable-outcomes** list (successful cancellation of active work; cancellation of a live operation; any outcome implying work was stopped), and new rules 1, 3 and 4 — including **"MUST NOT create mutable live-operation state merely to distinguish these outcomes"** | §26 | Runtime §27, §33 | Five states retained; reachability stated per row |
| `NEW-P3-05` | §32 omitted logging output and randomness | Categories extended **20 → 24**: row 20 logging output (prohibited by default; only a future injected inert sink, side-effect declared and observable), row 21 queue/scheduler, row 22 system randomness, row 23 clock access. New rules 5–7 cover randomness determinism, logging-as-side-effect, and queue scope | §32 | This spec | Categories recount: 20 → **24** |

## 6. Baseline Inert Invariant decision

§31 now defines **two distinct properties that MUST NOT be conflated**.

**§31.1 — Baseline Inert Invariant.** Applies to a *baseline inert composition*,
defined by three simultaneous conditions: default inert configuration; **no live
external implementation injected**; only repository-approved inert fixtures or
unavailable ports present. In such a composition the scaffold performs zero side
effects across all twenty-four §32 categories — network, subprocess, thread,
**queue/worker/scheduler**, filesystem read and mutation, Git, environment,
secret, logging, randomness, clock — represents no execution success, terminates
every execution request in a fail-closed refusal with an owner-defined class,
creates no live Runtime Handle, and performs no framework, provider, model,
package, tool, MCP, or Shared Context action. It holds across all combinations of
Runtime §14's eleven authorization facts including the all-eleven-satisfied case
(Agent Runtime Architecture §37).

**No live-mode invariant was invented.** §31.2 rule 2 states so explicitly.

## 7. Injected-component eligibility decision

**§31.2** states that an externally injected component **MUST NOT inherit inert
eligibility merely because it satisfies a Python interface**. Structural
conformance to a §12 port is not evidence of safety and §31.1 confers nothing on
it. An injected component may participate only in a future explicitly authorized
mode, and only after **seven separate validations**: side-effect declaration;
import safety; construction safety; capability boundary; permission boundary;
fixture identity; observability behavior. An unvalidated component is treated as
**unavailable** (§13 disposition 2), never as present. The safety posture
`port injected ≠ port safe` and `interface conformance ≠ execution eligibility`
is stated normatively.

## 8. Queue-safety correction

The future inert scaffold MUST NOT, during import, construction, deferred
effects, default validation, or attempted execution: create an in-process, async
or worker queue; enqueue background work; consume queued work; start a queue
processor; register a queue callback; or create scheduler-backed, delayed or
deferred jobs. Represented across import safety (§8 row 16), construction and
deferred effects (§9.1 row 18), the side-effect inventory (§32 row 21, rule 7),
the invariant (§31.1), future tests (§34 obligation 22), security (§37 threat
20), and non-goals (§39 item 19). **No queue inspection or queue runtime
behavior is implemented or specified** — §32 rule 7 states the scaffold neither
creates nor observes a queue.

## 9. Zero-execution evidence correction

See §5 row `NEW-P2-05`. The concept is renamed because the prior name falsely
implied a global guarantee; it is now a scaffold-owned, derived,
correlation-scoped, explicitly non-canonical audit record that renders `unknown`
rather than a confirmation whenever a port is injected or sentinel coverage is
incomplete, is never a Runtime result or Control Plane dimension, and fabricates
no run identifier.

## 10. Executable configuration correction

See §5 row `NEW-P2-06`. Fourteen executable-content categories added; fail-closed
rejection wired into §30 layer 5; "declared injected port names" clarified as
inert metadata; static symbolic references permitted only when they cannot
trigger an import, construction, or code invocation, remain inert metadata, and
require future explicit resolution by a separately authorized owner.

## 11. Deferred construction-effect correction

See §5 row `NEW-P2-07`. New §9.1 binds nineteen deferred mechanisms to §32
exactly as constructors are bound, states that postponing a prohibited action to
first property access, first method call, context entry, or destruction is **the
same violation**, and confirms that moving an optional SDK import into a function
body does not remove it from a reachable path.

## 12. Import filesystem-read correction

See §5 row `NEW-P3-03`. Reads are now separated from writes (row 6 vs row 8),
directory scanning is prohibited (row 7), and presence probing by file test,
metadata query, or package-manager access is prohibited (row 12). Rule 5 draws
the boundary deterministically: metadata **already supplied by the import
system** — a module's own `__name__`, `__doc__`, or a constant defined in the
package — may be inspected; anything requiring additional filesystem,
package-manager, entry-point, or environment access is prohibited.

## 13. Cancellation reachability correction

See §5 row `NEW-P3-04`. Each of the five states now carries an explicit
reachability verdict for a baseline inert composition; three outcomes are named
**unreachable**; and the scaffold is forbidden from creating mutable
live-operation state, a handle table, or a cancellation ledger merely to
distinguish outcomes.

## 14. Logging and randomness correction

See §5 row `NEW-P3-05`. Logging is treated as a side effect (§32 row 20, rule 6):
root-logger mutation and automatic handler creation prohibited; default console,
stdout and stderr output prohibited; a future injected inert test sink must be
side-effect declared and observable; no secret or sensitive payload logged.
Randomness (§32 row 22, rule 5): implicit randomness prohibited in a baseline
inert composition; random identifiers, seeds, and nondeterministic ordering
prohibited; identifiers and timestamps come only from injected ports or fixed
fixtures; **default construction MUST NOT access system randomness**. Neither is
treated as harmless merely because no provider is invoked.

## 15. Tracked outcome-code correction

`AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED` is now recorded in tracked files.
The state makes clear that it was the **pre-review specification outcome**, that
Review 001 subsequently issued `PASS_WITH_NON_BLOCKING_FINDINGS`, that the
specification is now at version 1.1 under this remediation, and that **no
implementation exists**. **No Review 001 evidence was rewritten** — both Review
001 artifacts are byte-identical.

## 16. Files changed

**Edited (1):** `docs/specs/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_001.md`
(1.0 → 1.1).
**Created (1):** this report.
**State synchronization (6):** `PROJECT_STATE.md`, `ROADMAP.md`, `RUN_QUEUE.md`,
`AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md`.

**Exactly eight files changed**, matching the allowlist printed before editing.
**No source file, test, Python package, dependency, or configuration file was
created or modified.**

## 17. Metrics before and after

All values recomputed mechanically. **Every row of §42 reproduces against the
document — zero drift.**

| Metric | v1.0 | v1.1 | Changed by |
| --- | --- | --- | --- |
| Specification sections | 44 | 44 | — |
| Terminology entries | 23 | **28** | `NEW-P2-01`, `-05`, `-07` (five new concepts) |
| Architectural ownership rows | 26 | 26 | — |
| Scaffold status statements | 8 | 8 | — |
| Module inventory rows | 10 | 10 | — |
| Composition-root rules | 7 | 7 | — |
| Import-safety prohibitions | 12 | **19** | `NEW-P3-03`, `NEW-P2-04`, `NEW-P3-05` |
| Construction-safety rules | 8 | 8 | — |
| **Deferred-effect mechanisms** | — | **19** (new) | `NEW-P2-07` |
| Configuration prohibitions | 8 | **22** | `NEW-P2-06` |
| Dependency-injection rules | 6 | 6 | — |
| Runtime ports | 14 | 14 | — |
| No-op / fail-closed dispositions | 6 | 6 | — |
| Operation-coverage rows | 16 | 16 | — |
| Package prohibitions | 8 | 8 | — |
| Framework Bridge prohibitions | 8 | 8 | — |
| Shared Context Bridge prohibitions | 10 | 10 | — |
| Cancellation states | 5 | 5 | `NEW-P3-04` (reachability column added, count unchanged) |
| Observability fields | 12 | 12 | — |
| **Zero-execution evidence properties** | — | **8** (new) | `NEW-P2-05` |
| Logging rules | 7 | 7 | — |
| Validation layers | 10 | 10 | — |
| **Injected-component validations** | — | **7** (new) | `NEW-P2-01`, `NEW-P2-05` |
| Side-effect categories | 20 | **24** | `NEW-P2-04`, `NEW-P3-05` |
| Testing obligations | 17 | **24** | `NEW-P2-02` |
| Static validation techniques | 7 | 7 | — |
| Security threats | 20 | **26** | `NEW-P2-04`, `-06`, `-07`, `-01`, `-05`, `NEW-P3-05` |
| Non-goals | 21 | **22** | `NEW-P2-04` |
| Deferred dependencies | 28 | 28 | — |
| Acceptance criteria | 31 | **39** | all seven P2 plus `NEW-P3-02`, `-04`, `-05` |

§42 now carries **30 metric rows** (three added).

## 18. Validators and exact outcomes

1. `git diff --check` → exit `0` (benign LF/CRLF warnings only), baseline and
   post-commit.
2. `py -3.9 scripts/validate_project_state.py` (Python 3.9.13) → `PASS MellyCore
   project scaffold validation passed`, exit `0`, baseline and post-commit.
3. **Changed-file allowlist check** → exactly the eight files of §16.
4. **Finding inventory completeness** → 12 / 12 findings, each with exactly one
   documented disposition.
5. **Baseline invariant consistency** → three surviving "regardless of" clauses,
   each correctly scoped to the §15 execution refusal, §31.2 rule 4, or
   acceptance criterion 32. **No contradictory scope statement remains.**
6. **Queue audit** → covered in §8, §9.1, §31.1, §32, §34, §37, §39 (all seven
   required areas).
7. **Executable configuration audit** → fourteen categories added; fail-closed
   rejection stated; §30 layer 5 updated.
8. **Deferred-effect audit** → nineteen mechanisms enumerated and bound to §32.
9. **Import filesystem-read audit** → rows 6, 7 and 12 present; rule 5 draws the
   metadata boundary.
10. **Cancellation reachability audit** → per-state reachability plus three named
    unreachable outcomes.
11. **Logging and randomness audit** → §32 rows 20, 22, 23 and rules 5–6.
12. **Runtime §37 ownership audit** → every restatement cited and labelled
    subordinate; **no bare cross-document `§37` remains**; owner unchanged.
13. **Zero-execution evidence audit** → scoped, evidentiary, non-canonical, not a
    success result; all eight properties present.
14. **Runtime operation coverage audit** → owner set re-derived from the two
    `Operation` tables in the Agent Runtime specification; **16 / 16 still
    named**, zero missing.
15. **Fifteen-upstream-P2 containment audit** → all fifteen rows present in §40;
    `PROJECTION_UNSUPPORTED` and `BRIDGE_UNSUPPORTED_BEHAVIOR` appear only in
    denials and deferrals; **zero cross-contract capability ordinals**.
16. **Full metrics recount** → **30 / 30 rows reproduce, zero drift**;
    44 sections contiguous.
17. **Cross-reference and wikilink check** → all wikilinks resolve; all internal
    `§N` within 1–44; the single `§48` is owner-qualified to the Shared Context
    Bridge Contract.
18. **Normative-modal audit** → 161 MUST / 109 MUST NOT / 5 SHOULD / 16 MAY /
    **0 SHALL**; **zero inverted `No X MUST` constructions**.
19. **Overclaim scan** → clean; no bare positive-state assertion.
20. **Secret and configuration scope check** → no `.env`; no secret, credential,
    token, or provider key; no workflow YAML; no source, test, dependency, or
    runtime configuration file changed.
21. **Immutable-source verification** → before edits and after commit (§19).

### 18.1 Validators unavailable or not run

- `pytest`, `black`, `flake8`, `mypy` — **not run and not claimed passing.** None
  applies to a documentation-only change touching no source or test file.
- **Empirical framework, provider, model, and runtime execution:
  `NOT_PERFORMED`.**
- No repository gate validator was unavailable.

## 19. Immutable-source verification

Twenty-eight named files plus the aggregate `.py` digest were hashed before
editing and re-verified after the commit. **All are byte-identical**, including:

- the **original Scaffold task report** — `6e82bdfea9de665d`;
- **Review 001 record** — `c1fc492fa33411b7`;
- **Review 001 task report** — `02e74bd6d70baac8`;
- Agent Runtime specification and both reviews;
- Agent Package, Framework Bridge, and Shared Context Bridge chains;
- Control Plane, Provider Registry, Integration Gateway, AI Operations,
  Operations Data Contract, Context Graph Schema, Safety Contract, Model Routing;
- the four `scripts/provider_adapters` source files and both provider-adapter
  test files;
- aggregate digest of every tracked `.py` under `scripts/` and `tests/` —
  `4e6028746b186b09`, tracked count unchanged at **71**.

## 20. Remaining limitations

1. **Version 1.1 is unverified.** It has not been independently reviewed; Review
   001's acceptance applied to version 1.0 under eleven constraints.
2. **Nothing is implemented.** No scaffold module, Python package, source file,
   test, fixture, dependency, or configuration exists. Agents executed, model
   calls, tool executions, provider requests, and context mutations remain
   **zero**.
3. **All fifteen upstream P2 findings remain open** — three Agent Package, four
   Framework Bridge, eight Shared Context Bridge. This remediation resolved none
   of them and depends normatively on none.
4. **Port method signatures remain unspecified**; a later implementation task
   derives them from the owner contracts under its own review.
5. This remediation **corrected its own reviewed findings**. No independent party
   has confirmed the closures, and **the Review 001 gate is not re-opened by this
   task**.
6. `NEW-P2-05`'s correction reduces the evidence record's claim to what sentinels
   can observe. Whether an implementation's sentinel coverage is genuinely
   complete is decidable only by the tests §34 obliges.

## 21. Recommended next task

`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002` — an independent, read-only
re-review of this remediation, responsible for deciding whether all twelve
Review 001 findings are genuinely closed and whether version 1.1 introduces any
new finding.

**Not started, not authorized by this task.** The Agent Runtime Scaffold
implementation remains **blocked**, requiring Review 002 to pass **and** separate
explicit Operator authorization **and** its own exact file allowlist. The global
higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged.
