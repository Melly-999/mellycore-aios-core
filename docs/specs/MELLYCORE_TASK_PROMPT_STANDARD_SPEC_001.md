# MellyCore Task Prompt Standard

**Task ID:** MELLYCORE-PROMPT-STANDARDIZATION-001
**Version:** 1.0
**Status:** Canonical, specification-level. Applies to **future** task
prompts only — see Section 7 (Migration). Not independently reviewed yet;
`MELLYCORE-PROMPT-STANDARDIZATION-REVIEW-001` is the next canonical task.
**This status does not authorize:** rewriting any historical prompt or
task report, frontend/runtime/provider/MCP work of any kind, or any
implementation this document merely uses as an illustrative example.

---

## 1. Why this exists

`AGENTS.md` is the canonical shared **policy** owner: authority hierarchy,
edit discipline, safety posture, validation honesty, review principles,
stop conditions. It answers *what an agent must never do* and *how an
agent must report*. It deliberately does not answer *how a task prompt
should be shaped* so that those rules are easy to apply consistently —
that is this document's job.

`[[../../agent_prompts/loops/README]]` already proved the pattern this
document follows: write the canonical version once, in one place, and let
every consumer point at it instead of restating it. This document does
the same thing for one-off task prompts that `agent_prompts/loops/` did
for recurring loop skills.

**The concrete problem this solves:** three recent tasks in this
repository —
`[[../tasks/CLAUDE-CODE-WORKFLOW-HARDENING-001]]`,
`[[../tasks/CLAUDE-CODE-WORKFLOW-HARDENING-LANDING-001]]`, and the
independent review between them — showed both what works and what drifts
without a shared shape. What worked: explicit PREFLIGHT steps that caught
a wrong-repository review before it produced a fabricated verdict, and
explicit STOP CONDITIONS that turned an unverifiable premise into a
`BLOCKED` report instead of a guess. What drifted: the hardening task's
own handoff entry stated, as settled fact, that a prior review outcome
was durable repository evidence — when the very task it cited as
precedent had already disclosed that the same claim was only
operator-attested, not repository-verified. No section of that prompt
required the author to distinguish "I verified this" from "a prior report
told me this." That gap is exactly what Section 3.9 (VALIDATION) and
Section 3.11 (SELF-CRITIQUE) below are designed to close.

## 2. What this document is not

- It is not a restatement of `AGENTS.md`. Every section below that
  touches safety, validation honesty, or stop conditions says "as
  `AGENTS.md`" and adds only what is specific to *shaping a prompt*, not
  to *behaving safely*.
- It is not a procedure an agent runs. `[[../../.claude/commands/plan-task]]`,
  `[[../../.claude/commands/review]]`, and `[[../../.claude/commands/diff-audit]]`
  are procedures an agent executes during a task. This document is what a
  human (or another agent, planning a delegation) writes *before* a task
  starts, so the agent receiving it has a scoped, checkable prompt.
- It is not mandatory retroactively. See Section 7.

## 3. Required sections

Every non-trivial MellyCore task prompt should contain these thirteen
sections, in this order. A trivial one-line request does not need this
scaffolding — see Section 4 for which task modes can compress or skip
sections.

### 3.1 ROLE

**Purpose:** Tell the agent what expertise lens to apply, so its defaults
(what it double-checks, what it treats as obvious) match the task.
**Required:** One to a few named roles relevant to the actual work.
**Forbidden:** A role list so broad it authorizes scope creep (e.g.
naming "product implementation engineer" for a docs-only task).
**Common failure mode:** Copy-pasting an unrelated role list from a prior
prompt because it "sounds thorough."
**Example:** `Act as a senior repository governance engineer and Git
evidence reviewer.`

### 3.2 TASK

**Purpose:** Name the exact task ID and the exact prior artifacts it
consumes, so provenance is checkable.
**Required:** A task ID matching this repository's `MELLYCORE-<NAME>-NNN`
or `CLAUDE-CODE-<NAME>-NNN` convention; explicit references to any input
task/review by ID and commit SHA if applicable.
**Forbidden:** "Continue from where we left off" or other context-only
references that cannot be independently verified from the repository.
**Common failure mode:** Naming an input task without its commit SHA,
forcing the executing agent to trust chat history instead of `git log`.
**Example:** `Use the landed hardening (commits 2e3e63d, fd5ec32,
ba9580e on docs/claude-code-workflow-hardening-landing-001) as input.
Verify these from Git before using them.`

### 3.3 GOAL

**Purpose:** State the outcome in one or two sentences, independent of
implementation detail, so scope disputes can be resolved by asking "does
this serve the goal."
**Required:** A plain statement of the end state, and — if relevant —
what does *not* change even though the task succeeds (e.g. "this does not
close the milestone").
**Forbidden:** Restating the TASK section in different words with no new
information.
**Common failure mode:** A goal so vague ("make things better") that
every IMPLEMENTATION RULE becomes independently arguable.

### 3.4 CONTEXT

**Purpose:** Give the agent the minimum background needed to make
judgment calls without re-deriving history from scratch.
**Required:** What prior tasks established, in plain prose; what remains
open or unresolved.
**Forbidden:** Pasting an entire prior report verbatim. Link to it
(`[[../tasks/TASK-ID]]`) instead — the agent can read the source if it
needs more than the summary, and a summary that drifts from its source
is instantly checkable by any reviewer who follows the link.
**Common failure mode:** Treating this section as the place to assert
conclusions ("the hardening was independently accepted") rather than
facts an agent can check ("a review returned PASS_WITH_NON_BLOCKING_FINDINGS
— see link").

### 3.5 PREFLIGHT

**Purpose:** Force verification of repository state *before* any
judgment or mutation, so a wrong-repo or wrong-branch session fails fast
and visibly instead of producing a plausible-looking wrong answer.
**Required:** Exact commands to run (`git rev-parse --show-toplevel`,
`branch --show-current`, `status --short --branch --untracked-files=all`,
plus `cat-file -t` / `merge-base --is-ancestor` for any commit the task
depends on) and what result to reject on. If a task depends on a
specific branch or commit, PREFLIGHT must say what to do if reality
doesn't match — continue with a caveat, or stop.
**Forbidden:** Preflight steps with no defined reject condition ("check
the branch" without saying what wrong looks like).
**Common failure mode:** Assuming the repository root, branch, or a
cited commit's ancestry rather than checking it — this is precisely what
produced a `BLOCKED` result in `CLAUDE-CODE-WORKFLOW-HARDENING-REVIEW-001`'s
first run (git root was `C:/`, the whole drive, not the intended repo).

### 3.6 SCOPE

**Purpose:** Draw the boundary of what files/directories this task may
touch, as an allowlist plus an explicit denylist.
**Required:** An `ALLOWED` list specific enough to check a diff against
it; a `NOT ALLOWED` list naming concrete paths or path patterns (`site/**`,
`runtime/**`, `.github/workflows/**`, package manifests), not just
categories.
**Forbidden:** "Only touch what's needed" with no enumerated files —
that is not checkable by a diff-audit.
**Common failure mode:** An allowlist wide enough to include files the
task doesn't actually need, which then get touched "while we're at it."

### 3.7 SAFETY POSTURE

**Purpose:** Restate, briefly, the subset of `AGENTS.md`'s safety floor
most relevant to this specific task — not the whole floor.
**Required:** "As `AGENTS.md`" plus any task-specific distinctions that
matter here (e.g. "prompt standard created != old prompts migrated").
**Forbidden:** Copying `AGENTS.md`'s full Rules section into the prompt.
If a rule needs elaboration for this task, that elaboration belongs in
IMPLEMENTATION RULES, not a duplicate safety section.
**Common failure mode:** A safety section that silently contradicts
`AGENTS.md` because it was hand-written instead of referenced, and then
drifts the next time `AGENTS.md` is updated.

### 3.8 IMPLEMENTATION RULES

**Purpose:** The task-specific "how," once ROLE/TASK/GOAL/SCOPE have
established the "what."
**Required:** Concrete, numbered rules an agent can follow without
re-deriving policy — landing strategy, which conflicts are in-bounds to
resolve, how to phrase a correction versus an in-place edit, etc.
**Forbidden:** Restating universal `AGENTS.md` rules here under a new
name.
**Common failure mode:** Rules general enough to apply to any task ("be
careful," "do it well") that give the executing agent no actual
constraint to check its own work against.

### 3.9 VALIDATION

**Purpose:** Name the exact commands to run and require that only
commands *actually run* be reported, with their *actual* output.
**Required:** An enumerated list of validators appropriate to the task
mode (Section 4); an explicit instruction not to claim a validator ran if
it didn't.
**Forbidden:** "Run appropriate tests" with no named commands — this
cannot be checked after the fact, and it is exactly the ambiguity that
lets `planned` quietly become `verified`.
**Common failure mode:** A validator listed in the prompt but never
actually invoked in the final report, or a report that states a result
("Secrets exposed: NO") without the scan that produced it being listed in
VALIDATION EXECUTED.

### 3.10 STOP CONDITIONS

**Purpose:** Convert judgment calls into pre-committed decisions, so an
agent facing an ambiguous or broken state has an instruction to follow
instead of an incentive to guess and keep going.
**Required:** A numbered list of concrete, checkable conditions ("commits
X/Y cannot be found," "git root is `C:/`," "a secret is encountered") each
paired with the required response (`BLOCKED`, with reason).
**Forbidden:** "Use good judgment" as a stop condition — it is not one.
**Common failure mode:** Stop conditions that exist in the prompt but
that the task's own IMPLEMENTATION RULES contradict by encouraging the
agent to "work around" the blocking issue instead of stopping.

### 3.11 SELF-CRITIQUE

**Purpose:** Require the agent to audit its own claims against the
prompt's own SCOPE, VALIDATION, and STOP CONDITIONS before finalizing —
catching self-contradiction while it is still cheap to fix.
**Required:** A short, numbered list of yes/no questions specific to this
task's SCOPE and STOP CONDITIONS (not generic ones like "did I do a good
job").
**Forbidden:** Rhetorical questions the agent is clearly meant to answer
"yes" to regardless of what happened.
**Common failure mode:** A self-critique that re-asserts the final
report's conclusions instead of checking them independently — e.g.
answering "did I avoid duplication?" with "yes" without re-running the
grep that would confirm it.

### 3.12 FINAL REPORT

**Purpose:** Give every task a single, predictable, gradeable output
shape, so a reviewer (human or agent) can locate RESULT, files changed,
and validation evidence without reading prose.
**Required:** A fixed template matching this document's own reports
(RESULT / BASELINE / SCOPE / VALIDATION EXECUTED / FINDINGS / COMMIT /
NEXT CANONICAL TASK, adapted per task mode).
**Forbidden:** A report format invented per-task — that is precisely what
makes automated or skimmed review impossible.
**Common failure mode:** A report claiming `PASS` while a required
section (e.g. VALIDATION EXECUTED) is empty or missing.

### 3.13 COMMIT / NO PUSH

**Purpose:** State explicitly whether this task may create a local
commit, and reiterate — every time, regardless of how obvious it seems —
that push/merge/deploy require separate, explicit approval.
**Required:** "Do NOT push. Do NOT merge. Do NOT deploy." even when the
task is docs-only and the omission seems harmless; suggested commit
message(s) if commits are allowed.
**Forbidden:** Silence on this point. Never assume the executing agent
will infer the no-push default without it being restated per task.
**Common failure mode:** Omitting this section because "it's obviously
docs-only" — the instruction costs one line and the failure mode it
guards against (an agent inferring standing push authorization from a
successful local commit) is not hypothetical elsewhere in this industry.

## 4. Task-mode variants

| Mode | Mutation allowed? | Commit allowed? | Validators expected | Final report | Typical stop conditions |
| --- | --- | --- | --- | --- | --- |
| **A. Planning-only** | No | No | Preflight only (branch/HEAD/status) | A plan, not a completion report — see `[[../../.claude/commands/plan-task]]` | Scope cannot be resolved without the operator; repo state unclear |
| **B. Read-only review** | No (unless a separate, later task asks for a fix) | No | Whatever the reviewed work claims, re-run or re-checked directly — never re-stated on trust | Verdict (`ACCEPT`/`REJECT`/`BLOCKED`) + findings — see `[[../../.claude/commands/review]]` | Work under review not found; reviewer is the work's own author |
| **C. Docs-only mutation** | Yes, scoped to docs/policy/config files | Yes, local only | `git diff --check`, forbidden-path scan, secret/`.env` scan, changed-path audit — see `[[../../.claude/commands/diff-audit]]` | Files changed + validation results | Forbidden path touched; secret found; scope creep beyond the allowlist |
| **D. Implementation task** | Yes, code | Yes, local (or PR-ready per repo convention) | Everything in mode C, plus build/test/lint appropriate to the language/framework, actually run | As mode C, plus real test/build output | As mode C, plus failing build/tests, or any of `AGENTS.md`'s nine migration triggers being crossed |
| **E. External research task** | No to the repository itself; may produce one new `docs/research/*` file | Optional, single commit for the research artifact only | Source citation / evidence traceability for every material claim | Findings + sources, explicitly marked "external, not MellyCore canonical truth" per `AGENTS.md`'s authority hierarchy | Source unavailable, paywalled, or self-contradictory without resolution |

## 5. Compact reusable template

Copy this, fill in the brackets, and delete any section a trivial task
genuinely doesn't need — do not leave a bracket unfilled and do not
inflate a simple task into every section at full length. Task-mode
guidance is in Section 4.

```markdown
# [TASK_ID]
## [One-line task name]

## ROLE
[1-3 relevant roles, no more]

## TASK
Perform: [TASK_ID]
Input: [prior task ID(s) + exact commit SHA(s), verify from Git before use]

## GOAL
[1-2 sentences: end state. What this does NOT do/close, if relevant.]

## CONTEXT
[Plain-prose summary of what prior tasks established. Link sources —
do not paste them.]

## PREFLIGHT
1. Verify repo root is: [CANONICAL_BASELINE]
   Reject if git root is C:/ or C:\.
2. Verify current branch is: [EXPECTED_BRANCH]. If different, [say what
   to do].
3. Record branch, HEAD, `git status --short --branch --untracked-files=all`.
4. Verify [any depended-on commit] exists and is/isn't an ancestor of HEAD.

## SCOPE
ALLOWED: [ALLOWED_FILES]
NOT ALLOWED: [FORBIDDEN_FILES — name concrete paths, not categories]

## SAFETY POSTURE
As AGENTS.md. Task-specific distinctions: [only if any apply]

## IMPLEMENTATION RULES
1. [...]

## VALIDATION
Run and report only validators actually executed:
[VALIDATORS — exact commands]

## STOP CONDITIONS
Stop and report BLOCKED if:
1. [...]

## SELF-CRITIQUE
1. [Task-specific yes/no question]

## FINAL REPORT
[Fixed structure matching Section 3.12 above, adapted to this task's mode]

## COMMIT / NO PUSH
If validation passes: [COMMIT_MESSAGE]
Do NOT push. Do NOT merge. Do NOT deploy.
```

## 6. Anti-patterns

- **Vague task.** No task ID, no named input commits, no checkable GOAL.
- **No stop conditions.** Any ambiguity becomes the executing agent's
  judgment call instead of a pre-committed decision.
- **No validation, or validation with no named commands.** "Run tests"
  is not a validator; `py -3.9 -m unittest discover -s tests` is.
- **Huge context dump.** Pasting an entire prior report instead of
  linking it — turns CONTEXT into unmaintainable, driftable duplication.
- **Hidden implementation inside a review task.** A prompt titled
  "review" whose IMPLEMENTATION RULES quietly authorize edits is not a
  review; it is an unreviewed self-approval wearing a review's name.
- **Fake-live / fake-telemetry claims.** Stating a connection, deploy, or
  live data source is active without an observed command proving it.
- **Broad refactor riding along with a docs/policy change.** SCOPE exists
  specifically to prevent this; an allowlist with one unrelated file in
  it is a defect in the prompt, not a convenience.
- **Test claims without commands.** "Tests pass" is not evidence;
  `pytest -q` and its actual output is.
- **Mixing product implementation with governance docs in one task.**
  `AGENTS.md`/`CLAUDE.md`/`.claude/commands/*` changes and product code
  changes belong in separate tasks with separate SCOPE sections, even if
  one was motivated by the other.
- **Treating an external report as canonical truth without durable
  evidence.** This is the exact failure this document exists to prevent
  — see Section 1. An external or prior-task claim is persuasive input
  per `AGENTS.md`'s authority hierarchy, never MellyCore canonical truth,
  until something in this repository (a file, a commit, a command output)
  actually verifies it.

## 7. Migration note

This standard governs **future** task prompts written from this task
onward. It does **not** retroactively apply to, or require rewriting,
any prompt or task report already in `docs/tasks/` or `agent_prompts/` —
those remain historical artifacts exactly as written, including the ones
this document itself cites as examples of what drifted (Section 1).

- Future prompts should follow this standard.
- Old prompts are not touched by this task and do not need to be
  rewritten to "catch up."
- If an old prompt is actively reused as a template for new work, it
  should be updated to this standard **at that point**, as part of
  whatever task reuses it — not proactively, and not in bulk.
- A dedicated bulk migration of historical prompts, if ever wanted, is
  its own separate, explicitly-scoped task, reviewed independently like
  any other change to `docs/` or `agent_prompts/`. This document does not
  authorize one and none is planned.

## 8. Cross-references

- `[[../../AGENTS.md]]` — canonical shared policy this document defers to
- `[[../../CLAUDE.md]]` — thin Claude Code wrapper
- `[[../../.claude/commands/plan-task]]` — planning-only procedure (mode A)
- `[[../../.claude/commands/review]]` — independent review procedure (mode B)
- `[[../../.claude/commands/diff-audit]]` — pre-commit audit procedure (used by modes C/D)
- `[[../../agent_prompts/loops/README]]` — the canonical-owner-plus-thin-wrapper pattern this document follows
- `[[../tasks/CLAUDE-CODE-WORKFLOW-HARDENING-001]]`, `[[../tasks/CLAUDE-CODE-WORKFLOW-HARDENING-LANDING-001]]` — the concrete tasks that motivated Section 1 and the anti-pattern in Section 6
