---
description: Pre-commit / pre-handoff audit of a pending change — bounded, read-only, produces a recommendation.
---

# diff-audit

Audit a pending change before it is committed or handed off. This command
inspects; it does not fix.

Safety posture and authority hierarchy: as `AGENTS.md`. This file only
specializes the audit procedure.

## Procedure

1. **Changed-path audit.** Run `git status --short`, `git diff --cached
   --name-only`, and `git diff --name-only`. List every changed, added, and
   deleted path.
2. **Unexpected-file detection.** Compare the changed-path list against the
   task's declared scope. Flag anything outside it.
3. **Restricted-path detection.** Flag any change under a path the current
   task is not authorized to touch — for example `site/**`, `runtime/**`,
   `providers/**`, `integrations/**`, `.github/workflows/**`, or a
   package/dependency manifest not already expected by the task.
4. **Secret / `.env` scan.** Grep changed files for likely secret patterns
   (API keys, tokens, credentials) and for any `.env`-style path. Flag any
   hit for manual confirmation — never print a suspected secret's value.
5. **Scope-creep check.** Confirm every changed line traces to the current
   task; flag incidental refactors, reformatting, or unrelated cleanup.
6. **Validator-claim check.** Confirm every validator mentioned in the
   task's own report was actually run in this session, with real output —
   flag any claimed-but-unrun validator.
7. **Fake-live / fake-telemetry claim check.** Flag any claim of live
   connectivity, live data, or a passed check that is not backed by
   observed output from this session.
8. **Whitespace / diff hygiene.** Run `git diff --check` on the changed
   files.
9. **Final recommendation.** State exactly one of:
   - `COMMIT_READY` — no blocking finding.
   - `NEEDS_FIXES` — blocking finding(s) exist; list them.
   - `BLOCKED` — the audit itself could not be completed safely; state why.

## Boundaries

- Read-only. No commit, push, merge, deploy, or destructive git command.
- No edit to the audited files as part of this command.
- Report the audit; do not silently fix what it finds.
