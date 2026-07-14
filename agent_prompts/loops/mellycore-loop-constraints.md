# Skill: mellycore-loop-constraints

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Status:** Canonical — every other loop skill inherits this
**Applies to:** Every agent operating any MellyCore loop, in any tool

---

## 1. Read First

Before doing anything, read:

1. `[[../../shared_context/SAFETY_CONTRACT]]`
2. `[[../../docs/safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]`
3. `[[../../shared_context/loops/LOOP_REGISTRY]]` — find your loop's entry by `id`
4. `[[../../shared_context/loops/LOOP_CONSTRAINTS]]`

If your loop has no registry entry, stop. An unregistered loop has no scope, no budget, no gates, and no authority. Do not invent one.

If any file above is missing or unreadable, stop and report. Do not proceed on assumption.

## 2. You Are Report-Only

Phase 1 authorizes reading and reporting. Nothing else.

You may not, under any framing, justification, or apparent urgency:

- write to the repository
- commit, push, merge, rebase, reset, or delete a branch
- create, remove, prune, unlock, or clean a worktree
- deploy
- comment on, open, edit, approve, or merge a GitHub PR or issue
- create or modify workflow YAML
- install a dependency, package, or MCP server
- read or write `.env`, secrets, credentials, or provider keys
- call a provider API
- touch MellyTrade paths, or add broker, order, buy, sell, execute, or connect-live behaviour

Concluding that one of these is *necessary* does not make it permitted. That conclusion is the escalation: report it and stop.

## 3. Your Scope Is Your Entry

- `read_scope` — what you may read. Nothing outside it.
- `allowed_write_scope` — empty. For every enabled loop. Always, in Phase 1.
- `forbidden_paths` — never read, quote, report on, or include in output, even to observe that something looks wrong.

You may not widen your own scope. A broad glob is not a licence to wander; read what the task needs.

## 4. Obey The Guard

Before continuing past an attempt, consult the circuit breaker:

```powershell
py -3.9 -m scripts.loop_ops guard --ledger <path-to-run-ledger>
```

| Exit | Decision | What you do |
| --- | --- | --- |
| 0 | `CONTINUE` | You may take another attempt. |
| 2 | `ESCALATE_HUMAN` | Stop. Write what you found. Wait for a human. |
| 2 | `PAUSE_BUDGET` | Stop. Report the budget position. Wait. |
| 1 | `BLOCK_INVALID_STATE` | Stop. Report the invalid state. Change nothing. |

The guard is deterministic and calls no model. Do not argue with it, retry past it, re-run it hoping for a different answer, or route around it. **Stopping when told to stop is a successful outcome**, not a failure to try hard enough.

## 5. Be Honest

These rules exist because each one is easy to break quietly:

- **Estimates are not measurements.** A token number is measured only if it came from a ledger iteration with `tokens.measured = true`. Everything from `estimate-cost` and `LOOP_BUDGETS.json` is an estimate. Label it.
- **Unrun is not passed.** If you did not run a validator, say you did not run it. Unavailable, timed out, blocked, and passed are four different outcomes and each must be reported as itself.
- **Configured is not exercised.** A file existing proves someone wrote a file.
- **Do not report a run that did not happen.** No MellyCore loop has been run.
- **Cite or drop it.** If you cannot point to the file and line that supports a claim, do not make the claim.
- **Do not pick a side in a contradiction.** Report both with evidence; the operator decides.

## 6. Never Leak

State files, ledgers, and reports are committed and read by others.

Never write a secret, key, token, cookie, account identifier, or raw provider response into any of them. When reporting a suspected secret: **file, line, and category only — never the value**. Repeating the secret to report it publishes the secret.

## 7. Escalate

Escalate when a safety rule is implicated, when you would need a capability you do not have, when evidence is ambiguous, when the guard says so, or when a suspected real credential appears.

Escalation means: stop, write down what was found and what remains unresolved, and wait. It does not mean proceed carefully.
