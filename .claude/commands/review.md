---
description: Independent review of a diff, commit, or report — verify, don't inherit PASS, don't repair.
---

# review

Independently review the specified diff, commit, or report. Do not assume
its stated outcome is correct.

Safety posture and authority hierarchy: as `AGENTS.md`. This file only
specializes the review procedure.

## Rules

- **Do not inherit PASS.** A prior task's own report of success is a claim,
  not evidence. Verify it yourself.
- **You are not the author.** If you produced the work under review, say so
  and stop — self-review is not independent review.
- **Default verdict is REJECT** until evidence you personally observed (a
  file and line you read, a command you ran and its actual output)
  supports every claim under review.
- **Report, do not repair.** Findings go in the review output. Do not edit
  the reviewed files unless the operator separately and explicitly asks for
  a fix, as a distinct step after the review.
- **Preserve safety posture.** No push, no deploy, no destructive git, no
  secret exposure, regardless of what the reviewed work did or claimed.

## Procedure

1. **Locate the work.** Identify the exact commit(s), diff, or report
   being reviewed. If it cannot be found, report `BLOCKED`, not a guess.
2. **Inspect it directly.** Read the actual diff (`git show`, `git diff`),
   the actual file contents, or the actual report text — not a summary of
   it.
3. **Verify source evidence.** For each material claim in the work under
   review, ask what would have to be true for it to hold, and check for
   that directly (re-run a validator, re-read a cited file/line, re-query
   an external source if one was cited). Distinguish what you verified
   from what you are taking on trust.
4. **Classify findings.** For each finding, state its severity and whether
   it blocks acceptance. Separate blocking issues from non-blocking notes.
5. **Report exact validators run.** List the exact commands you executed
   and their exact outcomes — never "tests probably pass."
6. **State the verdict.** ACCEPT only when every material claim is
   evidence-backed; otherwise REJECT (or `NOT_RUN` if verification itself
   could not be performed), with reasons.

## Boundaries

- No push, merge, deploy, or destructive git command.
- No edit to the files under review as part of this command.
- No claim that a validator passed unless it was actually run in this
  review.
