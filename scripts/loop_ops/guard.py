"""The MellyCore loop circuit breaker.

Reads a run ledger and returns a decision. It is deterministic, calls no model,
and makes no network request: the same ledger always yields the same decision.
That is the point. A breaker that asks a model whether to stop is not a breaker.

Decisions:
    CONTINUE            the loop may take another attempt (exit 0)
    ESCALATE_HUMAN      stop and hand to a human (exit 2)
    PAUSE_BUDGET        stop, budget exhausted (exit 2)
    BLOCK_INVALID_STATE the ledger or transition is invalid (exit 1)

Precedence, strongest first: invalid state, then kill switch, then escalation,
then budget. An invalid ledger is decided first because no other check can be
trusted against input that does not parse. The kill switch outranks everything
else because it is the operator saying stop now.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

from .models import (
    ALLOWED_TRANSITIONS,
    BLOCK_INVALID_STATE,
    CONTINUE,
    ESCALATE_HUMAN,
    LIFECYCLE_STATES,
    PAUSE_BUDGET,
    GuardDecision,
    InvalidInputError,
    LoopSpec,
    Registry,
    RunLedger,
)
from .registry import repo_root

PASS = "pass"
FAIL = "fail"
UNENFORCEABLE = "unenforceable"


def normalize_error(signature: Optional[str]) -> str:
    """Normalize an error signature so the same failure compares equal.

    Deliberately conservative: casefold and collapse whitespace, nothing more.
    Aggressive normalization would merge genuinely different errors and hide a
    real problem behind a false stagnation verdict.
    """
    if not signature:
        return ""
    return " ".join(str(signature).split()).casefold()


def transition_allowed(before: str, after: str) -> bool:
    """True if the lifecycle transition ``before`` -> ``after`` is permitted."""
    if before not in ALLOWED_TRANSITIONS or after not in LIFECYCLE_STATES:
        return False
    return after in ALLOWED_TRANSITIONS[before]


def kill_switch_engaged(
    registry: Registry,
    ledger: RunLedger,
    root: Optional[Path] = None,
) -> bool:
    """True if the global halt is engaged.

    Engaged by either the kill switch file existing on disk, or the ledger
    recording ``kill_switch_engaged``. Either source alone is sufficient: this
    fails safe, never requiring agreement between the two to stop.
    """
    if ledger.kill_switch_engaged:
        return True
    kill_file = registry.global_kill_switch.get("file")
    if not kill_file:
        return False
    return (( root or repo_root()) / str(kill_file)).exists()


def _count_trailing_failures(ledger: RunLedger) -> int:
    count = 0
    for iteration in reversed(ledger.iterations):
        if iteration.failed:
            count += 1
        else:
            break
    return count


def _max_repeated_error(ledger: RunLedger) -> int:
    """Highest number of times one normalized error signature appears."""
    counts: Dict[str, int] = {}
    for iteration in ledger.iterations:
        if not iteration.failed:
            continue
        key = normalize_error(iteration.error_signature)
        if not key:
            continue
        counts[key] = counts.get(key, 0) + 1
    return max(counts.values()) if counts else 0


def _trailing_unchanged_progress(ledger: RunLedger) -> int:
    """How many trailing attempts share the same progress marker.

    Returns 0 when there are fewer than two attempts: a single attempt cannot
    demonstrate a lack of progress.
    """
    if len(ledger.iterations) < 2:
        return 0
    markers = [i.progress_marker for i in ledger.iterations]
    last = markers[-1]
    run = 1
    for marker in reversed(markers[:-1]):
        if marker == last:
            run += 1
        else:
            break
    return run


def evaluate(
    ledger: RunLedger,
    registry: Registry,
    root: Optional[Path] = None,
) -> GuardDecision:
    """Evaluate a ledger against its loop's limits and return a decision."""
    root = root or repo_root()
    checks: Dict[str, str] = {}
    reasons: List[str] = []

    loop: Optional[LoopSpec] = registry.get(ledger.loop_id)
    if loop is None:
        return GuardDecision(
            decision=BLOCK_INVALID_STATE,
            reasons=["ledger references unknown loop id {!r}".format(ledger.loop_id)],
            checks={"loop_known": FAIL},
            loop_id=ledger.loop_id,
            run_id=ledger.run_id,
        )
    checks["loop_known"] = PASS

    # --- 1. Invalid state ----------------------------------------------------
    if not transition_allowed(ledger.status_before, ledger.status_after):
        checks["lifecycle_transition"] = FAIL
        return GuardDecision(
            decision=BLOCK_INVALID_STATE,
            reasons=[
                "forbidden lifecycle transition {} -> {}".format(
                    ledger.status_before, ledger.status_after
                )
            ],
            checks=checks,
            loop_id=loop.id,
            run_id=ledger.run_id,
        )
    checks["lifecycle_transition"] = PASS

    if loop.status == "DISABLED":
        checks["loop_enabled"] = FAIL
        return GuardDecision(
            decision=BLOCK_INVALID_STATE,
            reasons=["loop {!r} is DISABLED in the registry and must not run".format(loop.id)],
            checks=checks,
            loop_id=loop.id,
            run_id=ledger.run_id,
        )
    checks["loop_enabled"] = PASS

    # --- 2. Kill switch ------------------------------------------------------
    if kill_switch_engaged(registry, ledger, root=root):
        checks["kill_switch"] = FAIL
        return GuardDecision(
            decision=ESCALATE_HUMAN,
            reasons=["global kill switch engaged; all loops must halt"],
            checks=checks,
            loop_id=loop.id,
            run_id=ledger.run_id,
        )
    checks["kill_switch"] = PASS

    # --- 3. Escalation conditions -------------------------------------------
    attempts = len(ledger.iterations)
    if attempts >= loop.max_attempts:
        checks["max_attempts"] = FAIL
        reasons.append(
            "attempt count {} reached max_attempts {}".format(attempts, loop.max_attempts)
        )
    else:
        checks["max_attempts"] = PASS

    repeated = _max_repeated_error(ledger)
    if repeated >= loop.stagnation_threshold:
        checks["stagnation"] = FAIL
        reasons.append(
            "the same normalized error recurred {} times (stagnation_threshold {})".format(
                repeated, loop.stagnation_threshold
            )
        )
    else:
        checks["stagnation"] = PASS

    consecutive = _count_trailing_failures(ledger)
    if consecutive >= loop.max_attempts:
        checks["consecutive_failures"] = FAIL
        reasons.append(
            "{} consecutive failures (limit {})".format(consecutive, loop.max_attempts)
        )
    else:
        checks["consecutive_failures"] = PASS

    unchanged = _trailing_unchanged_progress(ledger)
    if unchanged >= loop.no_progress_threshold and unchanged >= 2:
        checks["no_progress"] = FAIL
        reasons.append(
            "progress_marker unchanged across {} attempts (no_progress_threshold {})".format(
                unchanged, loop.no_progress_threshold
            )
        )
    else:
        checks["no_progress"] = PASS

    if loop.verifier_required:
        rejected = [i.index for i in ledger.iterations if i.verifier_verdict == "REJECT"]
        if rejected:
            checks["verifier"] = FAIL
            reasons.append("independent verifier returned REJECT on attempt(s) {}".format(rejected))
        else:
            checks["verifier"] = PASS

    if reasons:
        return GuardDecision(
            decision=ESCALATE_HUMAN,
            reasons=reasons,
            checks=checks,
            loop_id=loop.id,
            run_id=ledger.run_id,
        )

    # --- 4. Budgets ----------------------------------------------------------
    # Only MEASURED tokens are enforced. An estimate must never trip or satisfy
    # a budget check, so unmeasured values are reported as unenforceable rather
    # than counted or treated as a pass.
    budget_reasons: List[str] = []

    measured = ledger.measured_run_tokens
    if measured > loop.per_run_token_budget:
        checks["per_run_budget"] = FAIL
        budget_reasons.append(
            "measured run tokens {} exceed per_run_token_budget {}".format(
                measured, loop.per_run_token_budget
            )
        )
    elif measured == 0 and ledger.has_unmeasured_tokens:
        checks["per_run_budget"] = UNENFORCEABLE
    else:
        checks["per_run_budget"] = PASS

    if ledger.daily_tokens_used is None:
        checks["daily_budget"] = UNENFORCEABLE
    elif ledger.daily_tokens_used > loop.daily_token_budget:
        checks["daily_budget"] = FAIL
        budget_reasons.append(
            "measured daily tokens {} exceed daily_token_budget {}".format(
                ledger.daily_tokens_used, loop.daily_token_budget
            )
        )
    else:
        checks["daily_budget"] = PASS

    if budget_reasons:
        return GuardDecision(
            decision=PAUSE_BUDGET,
            reasons=budget_reasons,
            checks=checks,
            loop_id=loop.id,
            run_id=ledger.run_id,
        )

    return GuardDecision(
        decision=CONTINUE,
        reasons=["no limit reached"],
        checks=checks,
        loop_id=loop.id,
        run_id=ledger.run_id,
    )


def evaluate_or_block(
    ledger: RunLedger,
    registry: Registry,
    root: Optional[Path] = None,
) -> GuardDecision:
    """Evaluate, converting an unexpected internal error into BLOCK_INVALID_STATE.

    Fails closed: an unexpected error must never read as CONTINUE.
    """
    try:
        return evaluate(ledger, registry, root=root)
    except InvalidInputError as exc:
        return GuardDecision(
            decision=BLOCK_INVALID_STATE,
            reasons=[str(exc)],
            checks={},
            loop_id=getattr(ledger, "loop_id", None),
            run_id=getattr(ledger, "run_id", None),
        )
