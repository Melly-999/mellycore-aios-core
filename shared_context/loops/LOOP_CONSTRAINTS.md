# Loop Constraints

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Version:** 1.0
**Status:** Binding — Phase 1
**Scope:** The rules any agent must accept before operating any MellyCore loop

---

## 1. Read Order

Before operating a loop, read in this order:

1. `[[../SAFETY_CONTRACT]]` — repo-wide safety rules.
2. `[[../../docs/safety/MELLYCORE_LOOP_SAFETY_CONTRACT_001]]` — loop-specific safety rules.
3. `LOOP_REGISTRY.json` — the loop's own entry.
4. This file.

If any of these is missing or unreadable, stop and report. Do not proceed on assumption.

## 2. The Phase 1 Rule

**Every enabled loop is report-only.** A loop produces findings. A human decides what to do about them.

A loop may not, under any framing:

- write to the repository, including "just updating state"
- commit, push, merge, rebase, reset, or delete a branch
- create, remove, prune, unlock, or clean a worktree
- deploy anything
- comment on, open, edit, approve, or merge a GitHub PR or issue
- create or modify workflow YAML
- install a dependency, package, or MCP server
- read or write `.env`, secrets, credentials, or provider keys
- call a provider API
- touch MellyTrade paths, or add broker, order, buy, sell, execute, or connect-live behaviour

If a loop concludes that one of these is necessary, that conclusion **is** the escalation. Report it and stop.

## 3. Scope Is A Contract, Not A Hint

`read_scope` is what the loop may read. `allowed_write_scope` is empty for every Phase 1 loop. `forbidden_paths` may never be read, reported on, quoted, or included in output — even to say "this file looks wrong".

Widening scope requires editing the registry and getting operator approval. A loop may not widen its own scope, and may not treat a broad glob as license to wander.

## 4. Stopping Is A Success

The circuit breaker (`py -3.9 -m scripts.loop_ops guard`) is deterministic and calls no model. It stops a loop on:

- exceeding `max_attempts`
- the same normalized error recurring `stagnation_threshold` times
- consecutive failures reaching `max_attempts`
- no change in `progress_marker` for `no_progress_threshold` attempts
- exceeding `per_run_token_budget`, or a measured `daily_token_budget`
- the global kill switch, or `global.paused`
- a forbidden lifecycle transition

A loop that stops early and reports why has succeeded. A loop that keeps trying because it feels close has not. Do not argue with the guard, retry past it, or route around it.

## 5. Honesty Rules

These are the rules most likely to be broken quietly, so they are stated plainly:

- **Do not claim measured token usage.** A number is measured only if it comes from a ledger iteration with `tokens.measured = true`. Everything in `LOOP_BUDGETS.json` and every `estimate-cost` output is an estimate. Say so.
- **Do not claim a validator passed unless you ran it and saw it pass.** Unavailable, timed out, and blocked are all distinct from passed, and each must be reported as itself.
- **Do not infer capability from file existence.** A registry entry means configured. It does not mean validated, exercised, approved, or production-ready.
- **Do not report a run that did not happen.** No loop has been exercised.
- **Do not resolve a contradiction by picking a side.** Report both sides with evidence and let the operator decide.

## 6. The Verifier Is Independent

When `verifier_required` is true, the work and the verification must come from different agents. An agent may not verify its own output.

The verifier's default verdict is **REJECT**. It moves to ACCEPT only on evidence it has actually seen. "It looks right" is not evidence. "I ran X and observed Y" is.

## 7. Secrets

State files and ledgers are committed to the repository. Anything written into them is public to every reader of this repo.

Never write a secret, key, token, cookie, account identifier, or raw provider response into state, a ledger, a log, or a report. When reporting a suspected secret, report **file, line, and category only** — never the value. `redact-check` follows this rule and so must you.

## 8. Escalation

Escalate to the operator when:

- a safety rule is implicated
- the loop would need a capability it does not have
- evidence is ambiguous and a claim cannot be substantiated
- the guard returns `ESCALATE_HUMAN`, `PAUSE_BUDGET`, or `BLOCK_INVALID_STATE`
- a suspected real credential appears anywhere

Escalation means: stop, write down what was found and what is unresolved, and wait. It does not mean proceed carefully.
