# MELLYCORE-PROMPT-STANDARDIZATION-001
## Final Report

## 1. RESULT

`PASS_WITH_LIMITATIONS`

## 2. BASELINE

Repository: `C:\AI\MellyCore_Workspace\01_Repo\mellycore-aios`
Branch: `docs/claude-code-workflow-hardening-landing-001`
Start HEAD: `ba9580e2e83c96ce05053f4d8c1bab754c7bab0b`
End HEAD: recorded in this session's tool output rather than guessed in
advance within this file's own content (this file is part of the commit
that produces it).
Initial status: clean tracked tree; 7 pre-existing untracked
screenshot/image files under `docs/`, unrelated to this task.
Final status: identical unrelated untracked files, plus this task's own
new files.

## 3. INPUTS USED

Hardening landing found: YES — `git rev-parse --show-toplevel` confirmed
the scoped repo root (not `C:/` or `C:\`); `git branch --show-current`
confirmed `docs/claude-code-workflow-hardening-landing-001`; `git cat-file
-t` confirmed all three expected commits (`2e3e63d`, `fd5ec32`, `ba9580e`)
exist; `git merge-base --is-ancestor` confirmed all three are ancestors of
HEAD.
AGENTS.md read: YES (in full, from the working tree).
CLAUDE.md read: YES (in full, from the working tree).
Command files read: YES — `.claude/commands/plan-task.md`, `review.md`,
`diff-audit.md`, all read in full in the prior review task and confirmed
still present and unmodified in this task's `git status`.
Existing prompt conventions inspected: `agent_prompts/loops/README.md`
and `agent_prompts/claude/README.md` (canonical-owner-plus-thin-wrapper
pattern and `[[wiki-link]]` cross-reference convention), `docs/specs/`
directory listing (established `MELLYCORE_<NAME>_SPEC_NNN.md`
underscore-separated naming for durable reference documents, distinct
from `docs/tasks/`'s hyphenated one-off task-report naming), and
`docs/specs/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001.md`'s header format
(Task ID / Version / Status / explicit non-authorization disclaimer),
used as the template for this task's own new spec header.

## 4. FILES CHANGED

- `docs/specs/MELLYCORE_TASK_PROMPT_STANDARD_SPEC_001.md` (new — the
  canonical prompt standard)
- `docs/tasks/MELLYCORE-PROMPT-STANDARDIZATION-001.md` (new — this report)
- `shared_context/AGENT_HANDOFF.md` (modified — new handoff entry, in a
  separate commit)

No other file was created, modified, or deleted. The 7 pre-existing
unrelated untracked screenshot files were left untouched.

## 5. PROMPT STANDARD CREATED

Canonical owner path:
`docs/specs/MELLYCORE_TASK_PROMPT_STANDARD_SPEC_001.md`

Template path if separate: none — the compact copy-paste template is
Section 5 within the same file, not a separate file. Decision rationale
in Section 6 below.

Required sections included: all 13 — ROLE, TASK, GOAL, CONTEXT,
PREFLIGHT, SCOPE, SAFETY POSTURE, IMPLEMENTATION RULES, VALIDATION, STOP
CONDITIONS, SELF-CRITIQUE, FINAL REPORT, COMMIT / NO PUSH — each with
Purpose / Required / Forbidden / Common failure mode / Example, confirmed
present via grep (Section 8).

Task-mode variants included: all 5 requested — A. Planning-only, B.
Read-only review, C. Docs-only mutation, D. Implementation task, E.
External research task — as a single comparison table (mutation allowed,
commit allowed, expected validators, final report shape, typical stop
conditions per mode).

Migration note included: YES (Section 7 of the spec) — future prompts
only; no retroactive rewrite of historical prompts or task reports;
reuse-triggered updates only; any bulk migration is explicitly deferred
to a separate, later, independently-reviewed task.

## 6. DESIGN DECISIONS

**Why this owner path:** `docs/prompts/MELLYCORE_TASK_PROMPT_STANDARD.md`
(the task prompt's own fallback suggestion) would have introduced a new
top-level directory with no precedent in this repository. `docs/specs/`
already holds 10+ durable, versioned reference documents using exactly
this naming shape (`MELLYCORE_<NAME>_SPEC_NNN.md`), and a canonical
task-prompt standard is structurally the same kind of artifact — a
durable specification, not a one-off task record. This is the "closer
existing equivalent" the task prompt asked to prefer over the fallback.

**Why one file, not a separate template file:** The task prompt allowed
a separate template "if appropriate." A second file would need its own
canonical-owner decision (where does it live, what governs its
relationship to the spec) for content that is, in practice, one clearly
delimited section (Section 5) inside the explanatory document. Given this
task's "be surgical" instruction and the general principle (stated in the
new spec itself, Section 2) against unnecessary duplication, a single
file with an internal template section was judged lower-risk than
introducing a second canonical location. The template section itself
(Section 5 of the new spec) is kept short and copy-paste-ready
independent of the surrounding explanatory prose, which achieves the same
practical goal.

**How duplication with AGENTS.md is avoided:** every section of the new
spec that touches safety, validation honesty, or stop conditions
explicitly says "as `AGENTS.md`" and states only the *prompt-shape*
guidance specific to that section, never re-deriving or restating
`AGENTS.md`'s actual rules. Section 2 of the new spec states this
constraint explicitly as a design rule for anyone editing the document
later. Verified: the new spec file contains zero copies of `AGENTS.md`'s
verbatim rule text (its Rules, Validation honesty, Review principles, or
Stop conditions sections) — confirmed by reading both files side by side
during authoring; not re-verified by an automated diff, since the spec's
prose is original commentary *about* those rules, not a restatement of
them, so a textual diff would not be a meaningful check here.

**How historical prompts are treated:** left entirely untouched. No file
under `docs/tasks/` or `agent_prompts/` other than this task's own two new
files was modified. `git status` before and after this task shows
identical unrelated content, confirming no incidental touch occurred.

## 7. SCOPE / SAFETY CHECK

Frontend changed: NO
Runtime changed: NO
Provider/router changed: NO
MCP/tool changed: NO
Workflow YAML changed: NO
Package/dependency changed: NO
Secrets exposed: NO
.env created: NO
Push performed: NO
Deploy performed: NO

## 8. VALIDATION EXECUTED

- `git -C <repo> rev-parse --show-toplevel` → `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` (not `C:/` or `C:\`)
- `git -C <repo> branch --show-current` → `docs/claude-code-workflow-hardening-landing-001` (matches expected)
- `git -C <repo> rev-parse HEAD` → `ba9580e2e83c96ce05053f4d8c1bab754c7bab0b`
- `git -C <repo> status --short --branch --untracked-files=all` → clean tracked tree, 7 unrelated untracked files only
- `git -C <repo> diff --cached --name-only` / `git diff --name-only` → both empty at preflight
- `git -C <repo> cat-file -t 2e3e63d|fd5ec32|ba9580e` → `commit` for all three
- `git -C <repo> merge-base --is-ancestor <each> HEAD` → YES for all three
- Section-name check: `grep -qi -- "<section>"` for all 13 required section names against the new spec file → all 13 FOUND (see Section 5 above)
- `git -C <repo> diff --cached --check` → run after staging, clean (see below)
- Forbidden-path scan (`site/`, `runtime/`, `providers/`, `integrations/`, `.github/workflows/`, package manifests) over changed paths → no matches (only `docs/specs/*` and `docs/tasks/*` touched)
- `.env`-path scan over changed paths → no matches
- Secret-pattern scan (`api[_-]?key|secret|token|password|bearer|AKIA[0-9A-Z]{16}|-----BEGIN`) over the new file's content → matches only this document's own prose about secret-pattern scanning and validation honesty (e.g. "secret-pattern scan," "provider tokens" in the anti-patterns list) — confirmed not credential values by direct reading, not just pattern-count
- Unsupported production/frontend/provider authorization claim scan → the new spec explicitly states, in its own header, that its status does not authorize any implementation; no claim of live connectivity, deployment, or provider access appears anywhere in the file
- Markdown lint: not available in this environment — not run, consistent with prior tasks' disclosure of the same limitation
- Application/product test suites: not run — correctly out of scope for a docs-only spec/report change

## 9. FINDINGS / LIMITATIONS

- This task creates the standard but does not apply it to any existing
  prompt. The three prompts that produced this very session (the
  hardening review, its rerun, and the landing task) predate this
  standard and were not retroactively reshaped to match it — consistent
  with Section 7 (Migration) of the new spec, but worth naming explicitly
  as a limitation rather than leaving it implicit.
- The new spec's "how duplication with AGENTS.md is avoided" claim
  (Section 6 above) was checked by direct reading rather than an
  automated diff/grep, since the two documents' relationship is
  intentionally about tone and reference rather than textual overlap. A
  future independent review could reasonably re-check this more
  mechanically if desired.
- This task remains on the same feature branch as the hardening landing
  (`docs/claude-code-workflow-hardening-landing-001`), which is itself not
  yet merged into any integration branch — this task does not change that
  status.

## 10. SELF-CRITIQUE

1. Did I align the standard with AGENTS.md rather than duplicate it? Yes — every safety/validation/stop-condition reference in the new spec points to `AGENTS.md` rather than restating its rules; verified by reading, see Section 6.
2. Did I include all required sections? Yes — all 13, confirmed by grep (Section 8).
3. Did I include practical task-mode variants? Yes — all 5 requested modes (A-E), as a single comparison table covering mutation/commit/validators/report/stop-conditions per mode.
4. Did I avoid mass rewriting historical prompts? Yes — `git status` confirms zero files under `docs/tasks/` or `agent_prompts/` were touched other than this task's own two new files.
5. Did I avoid frontend/runtime/provider/MCP changes? Yes — confirmed by the forbidden-path scan in Section 8, and the changed-file list in Section 4 contains only two new docs files.
6. Did I report only validators actually run? Yes — Section 8 lists exact commands and outcomes; the one item not mechanically re-verified (duplication-with-AGENTS.md check) is explicitly disclosed as read-based, not grep-based, rather than overstated.
7. Did I keep the template reusable rather than bloated? Yes — the compact template (Section 5 of the new spec) is a self-contained ~50-line copy-paste block; the surrounding explanatory material is a separate, clearly delimited reference section a task author consults, not something copied into every prompt.
8. Did I leave the review task as next canonical step? Yes — Section 13 below names `MELLYCORE-PROMPT-STANDARDIZATION-REVIEW-001` and this task does not execute it.

## 11. COMMIT

Commit SHA(s): recorded after this file is committed (see repository log)
— two commits planned: one for the spec + this report, one for the
handoff entry.

## 12. NEXT CANONICAL TASK

`MELLYCORE-PROMPT-STANDARDIZATION-REVIEW-001` — an independent, read-only
review of this task's changes, verifying the new standard's alignment
with `AGENTS.md`, its non-duplication, its coverage of all 13 required
sections and 5 task-mode variants, and that no historical prompt was
touched. This task does not execute it.
