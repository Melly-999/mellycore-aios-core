# Skill: mellycore-loop-budget-guard

**Task ID:** MELLYCORE-LOOP-OPERATIONS-FOUNDATION-001
**Status:** Canonical — deterministic, no model involved
**Inherits:** `mellycore-loop-constraints.md` (read it first; every rule there applies here)

---

## 1. Purpose

Consult the circuit breaker and obey it. That is the whole skill.

The breaker exists because an agent is the worst possible judge of whether it should keep going. An agent that has failed four times is exactly the agent most convinced that the fifth attempt will work.

## 2. The Command

```powershell
py -3.9 -m scripts.loop_ops guard --ledger <path>
py -3.9 -m scripts.loop_ops guard --ledger <path> --json
```

It reads a run ledger, applies the loop's registry limits, and returns a decision. It is deterministic: the same ledger always yields the same decision. **It calls no model.** Your judgment is not an input.

## 3. Decisions

| Exit | Decision | Meaning | Your action |
| --- | --- | --- | --- |
| 0 | `CONTINUE` | No limit reached | You may take one more attempt |
| 2 | `ESCALATE_HUMAN` | A limit was reached | Stop. Report. Wait |
| 2 | `PAUSE_BUDGET` | Measured budget exhausted | Stop. Report position. Wait |
| 1 | `BLOCK_INVALID_STATE` | Ledger or transition invalid | Stop. Report. Change nothing |

`CONTINUE` authorizes **one** further attempt, then you consult again. It is not a licence to loop freely.

## 4. What It Checks

- `max_attempts` reached
- the same normalized error recurring `stagnation_threshold` times
- consecutive failures
- `progress_marker` unchanged for `no_progress_threshold` attempts
- measured tokens over `per_run_token_budget`
- measured daily tokens over `daily_token_budget`
- the global kill switch, and `global.paused`
- a forbidden lifecycle transition

Precedence: invalid state, then kill switch, then escalation, then budget.

## 5. Measured Versus Estimated

The guard enforces budgets on **measured** tokens only — a ledger iteration with `tokens.measured = true`.

Unmeasured values report as `unenforceable`, not `pass`. That distinction is deliberate and you must preserve it when reporting: "the daily budget could not be enforced because no measured total exists" is true; "the daily budget passed" is not.

An estimate must never trip or satisfy a budget check. `estimate-cost` output is planning material and never enters the ledger.

## 6. Your Obligations

- **Consult before continuing.** Not after; before.
- **Obey the decision.** Do not retry past it, re-run hoping for a different answer, edit the ledger to change the outcome, lower a threshold, or start a fresh run to reset the counters. Each of those is defeating the breaker, and defeating the breaker is the specific failure this whole design exists to prevent.
- **Never rewrite history.** The ledger is append-only. Editing out a failure is falsifying the record. `parse_ledger` rejects duplicate and out-of-order indexes for this reason, but the rule binds you regardless of enforcement.
- **Report the decision verbatim**, including the reasons.
- **Treat stopping as success.** A loop that halts at its limit and explains why has worked correctly.

## 7. Report Shape

```
GUARD: <loop id> / <run id>
DECISION: <CONTINUE | ESCALATE_HUMAN | PAUSE_BUDGET | BLOCK_INVALID_STATE>
EXIT: <0 | 1 | 2>
REASONS:
- <verbatim from the guard>
CHECKS:
- <check>: <pass | fail | unenforceable>
ACTION TAKEN: <continued one attempt | stopped and escalated | stopped, budget>
```
