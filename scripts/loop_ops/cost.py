"""Deterministic token-cost estimator for MellyCore loops.

Everything this module produces is an ESTIMATE. MellyCore has never run a loop
and therefore has no measured token spend. Every result carries
``basis: ESTIMATE_NOT_MEASURED`` so that an estimate cannot be quoted later as
if it were an observation.

A number may only be called measured when it comes from a run ledger iteration
with ``tokens.measured = true``. See ``guard.py``, which enforces budgets on
measured values only.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from .models import InvalidInputError, LoopSpec

BASIS = "ESTIMATE_NOT_MEASURED"

SCENARIOS = ("no_op", "report", "assisted_action")


def _scenario_tokens(budgets: Dict[str, Any], scenario: str) -> int:
    model = budgets.get("estimation_model") or {}
    scenarios = model.get("scenarios") or {}
    spec = scenarios.get(scenario)
    if not isinstance(spec, dict):
        raise InvalidInputError("budgets: missing estimation_model.scenarios.{}".format(scenario))
    total = 0
    for key in ("input_tokens", "output_tokens"):
        value = spec.get(key)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise InvalidInputError(
                "budgets: estimation_model.scenarios.{}.{} must be an integer >= 0".format(scenario, key)
            )
        total += value
    return total


def _multiplier(budgets: Dict[str, Any], name: str, default: float) -> float:
    model = budgets.get("estimation_model") or {}
    multipliers = model.get("multipliers") or {}
    spec = multipliers.get(name)
    if not isinstance(spec, dict):
        return default
    value = spec.get("value", default)
    if not isinstance(value, (int, float)) or isinstance(value, bool) or value <= 0:
        raise InvalidInputError(
            "budgets: estimation_model.multipliers.{}.value must be a positive number".format(name)
        )
    return float(value)


def estimate_scenario(
    loop: LoopSpec,
    budgets: Dict[str, Any],
    scenario: str,
    parallel_agents: float = 1.0,
    apply_maker_checker: Optional[bool] = None,
) -> Dict[str, Any]:
    """Estimate one scenario for one loop.

    Args:
        loop: The loop being estimated.
        budgets: The parsed ``LOOP_BUDGETS.json`` document.
        scenario: One of ``SCENARIOS``.
        parallel_agents: Hypothetical fan-out multiplier. Phase 1 runs one agent.
        apply_maker_checker: Override the loop's ``verifier_required``. When
            None, the loop's own setting decides.

    Returns:
        A dict describing the estimate, including every multiplier applied so the
        arithmetic is auditable rather than a bare number.
    """
    if scenario not in SCENARIOS:
        raise InvalidInputError(
            "unknown scenario {!r}; expected one of {}".format(scenario, list(SCENARIOS))
        )
    if parallel_agents <= 0:
        raise InvalidInputError("parallel_agents must be greater than zero")

    base = _scenario_tokens(budgets, scenario)
    retry = _multiplier(budgets, "retry_overhead", 1.25)

    use_checker = loop.verifier_required if apply_maker_checker is None else apply_maker_checker
    checker = _multiplier(budgets, "maker_checker", 2.0) if use_checker else 1.0

    total = base * retry * checker * parallel_agents

    return {
        "scenario": scenario,
        "basis": BASIS,
        "base_tokens": base,
        "multipliers": {
            "retry_overhead": retry,
            "maker_checker": checker,
            "maker_checker_applied": bool(use_checker),
            "parallel_agents": float(parallel_agents),
        },
        "estimated_tokens": int(round(total)),
        "per_run_token_budget": loop.per_run_token_budget,
        "within_per_run_budget": int(round(total)) <= loop.per_run_token_budget,
    }


def estimate_realistic(
    loop: LoopSpec,
    budgets: Dict[str, Any],
    parallel_agents: float = 1.0,
    apply_maker_checker: Optional[bool] = None,
) -> Dict[str, Any]:
    """Estimate a weighted mix of scenarios.

    Most runs of a healthy report-only loop find nothing. Quoting the
    full-report figure as the expected cost would overstate it, and quoting the
    no-op figure would understate it; the weighted mix is the honest middle.
    """
    model = budgets.get("estimation_model") or {}
    mix = model.get("realistic_mix") or {}
    weights = mix.get("weights")
    if not isinstance(weights, dict) or not weights:
        raise InvalidInputError("budgets: missing estimation_model.realistic_mix.weights")

    total_weight = 0.0
    for scenario, weight in weights.items():
        if scenario not in SCENARIOS:
            raise InvalidInputError("budgets: unknown scenario {!r} in realistic_mix".format(scenario))
        if not isinstance(weight, (int, float)) or isinstance(weight, bool) or weight < 0:
            raise InvalidInputError(
                "budgets: realistic_mix weight for {!r} must be a number >= 0".format(scenario)
            )
        total_weight += float(weight)

    if abs(total_weight - 1.0) > 0.001:
        raise InvalidInputError(
            "budgets: realistic_mix weights must sum to 1.0, got {}".format(total_weight)
        )

    weighted = 0.0
    breakdown: Dict[str, Any] = {}
    for scenario, weight in weights.items():
        single = estimate_scenario(
            loop, budgets, scenario, parallel_agents=parallel_agents, apply_maker_checker=apply_maker_checker
        )
        contribution = single["estimated_tokens"] * float(weight)
        weighted += contribution
        breakdown[scenario] = {
            "weight": float(weight),
            "estimated_tokens": single["estimated_tokens"],
            "contribution": int(round(contribution)),
        }

    return {
        "scenario": "realistic",
        "basis": BASIS,
        "weights": {k: float(v) for k, v in weights.items()},
        "breakdown": breakdown,
        "estimated_tokens": int(round(weighted)),
        "per_run_token_budget": loop.per_run_token_budget,
        "within_per_run_budget": int(round(weighted)) <= loop.per_run_token_budget,
    }


def estimate_loop(
    loop: LoopSpec,
    budgets: Dict[str, Any],
    parallel_agents: float = 1.0,
    apply_maker_checker: Optional[bool] = None,
) -> Dict[str, Any]:
    """Estimate every scenario plus the realistic mix for one loop."""
    scenarios: List[Dict[str, Any]] = [
        estimate_scenario(loop, budgets, s, parallel_agents, apply_maker_checker) for s in SCENARIOS
    ]
    realistic = estimate_realistic(loop, budgets, parallel_agents, apply_maker_checker)
    return {
        "loop_id": loop.id,
        "status": loop.status,
        "level": loop.level,
        "verifier_required": loop.verifier_required,
        "basis": BASIS,
        "basis_note": (
            "Estimated from planning inputs in LOOP_BUDGETS.json. Not measured. No MellyCore loop "
            "has been run, so no measured token spend exists."
        ),
        "scenarios": scenarios,
        "realistic": realistic,
    }
