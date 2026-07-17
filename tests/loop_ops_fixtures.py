"""In-memory fixtures for the loop-ops tests.

Every fixture is built in memory. Nothing here touches a real worktree, reads a
real credential, requires the network, or contacts a provider.
"""

from __future__ import annotations

import copy
from typing import Any, Dict, List, Optional

GLOBAL_FORBIDDEN: List[str] = [
    ".env",
    "secrets/**",
    ".github/workflows/**",
]

KILL_SWITCH_FILE = "shared_context/loops/KILL_SWITCH"


def make_loop(loop_id: str = "sample-loop", **overrides: Any) -> Dict[str, Any]:
    """Build a minimal registry loop entry that passes validation by default."""
    loop: Dict[str, Any] = {
        "id": loop_id,
        "title": "Sample Loop",
        "purpose": "A fixture loop used only by tests.",
        "owner": "operator",
        "level": "L1",
        "status": "REPORT_ONLY",
        "trigger_type": "manual",
        "suggested_cadence": "daily",
        "read_scope": ["shared_context/**"],
        "allowed_write_scope": [],
        "forbidden_paths": list(GLOBAL_FORBIDDEN),
        "state_file": "shared_context/loops/states/{}.state.json".format(loop_id),
        "state_file_is_template": True,
        "verifier_required": False,
        "max_attempts": 3,
        "stagnation_threshold": 2,
        "no_progress_threshold": 2,
        "per_run_token_budget": 50000,
        "daily_token_budget": 100000,
        "human_gates": ["report_reviewed_by_operator"],
        "kill_switch": KILL_SWITCH_FILE,
        "success_condition": "A report is produced.",
        "escalation_condition": "Anything ambiguous.",
    }
    loop.update(overrides)
    return loop


def make_registry(loops: Optional[List[Dict[str, Any]]] = None, **overrides: Any) -> Dict[str, Any]:
    """Build a minimal registry document that passes validation by default."""
    registry: Dict[str, Any] = {
        "schema_version": "1.0",
        "registry_id": "TEST_REGISTRY",
        "phase": 1,
        "global_kill_switch": {
            "file": KILL_SWITCH_FILE,
            "semantics": "If present, halt.",
            "present_by_default": False,
        },
        "global_forbidden_paths": list(GLOBAL_FORBIDDEN),
        "lifecycle_states": [
            "DRAFT",
            "REPORT_ONLY",
            "ASSISTED",
            "WAITING_HUMAN",
            "PAUSED",
            "BLOCKED",
            "COMPLETED",
            "DISABLED",
        ],
        "levels": {"L0": "manual", "L1": "report", "L2": "assisted", "L3": "unattended"},
        "loops": loops if loops is not None else [make_loop()],
    }
    registry.update(overrides)
    return copy.deepcopy(registry)


def make_iteration(
    index: int = 1,
    outcome: str = "success",
    error_signature: Optional[str] = None,
    progress_marker: Optional[str] = "step-{}",
    tokens_total: Optional[int] = None,
    measured: bool = False,
    verdict: str = "NOT_RUN",
) -> Dict[str, Any]:
    """Build one ledger iteration.

    Under the corrected token contract, an unmeasured iteration must never
    carry a numeric total, not even zero. ``tokens_total`` therefore defaults
    to ``None``: when ``measured=False`` (the default) the built iteration has
    ``total: null``, a valid "no claim made" iteration. When ``measured=True``
    and ``tokens_total`` is left at ``None``, it defaults to a real measured
    zero. Passing an explicit ``tokens_total`` together with
    ``measured=False`` intentionally builds an *invalid* ledger (useful only
    for asserting that ``parse_ledger`` rejects it).
    """
    if outcome == "failure" and error_signature is None:
        error_signature = "generic_failure"
    marker = progress_marker.format(index) if progress_marker and "{}" in progress_marker else progress_marker
    if tokens_total is None:
        total = 0 if measured else None
    else:
        total = tokens_total
    return {
        "index": index,
        "started_at": "2026-01-01T00:0{}:00Z".format(min(index, 9)),
        "outcome": outcome,
        "error_signature": error_signature,
        "progress_marker": marker,
        "tokens": {"input": None, "output": None, "total": total, "measured": measured},
        "verifier": {"verdict": verdict, "verified_by": None, "evidence": None},
    }


def make_ledger(
    loop_id: str = "sample-loop",
    iterations: Optional[List[Dict[str, Any]]] = None,
    status_before: str = "REPORT_ONLY",
    status_after: str = "REPORT_ONLY",
    daily_tokens_used: Optional[int] = None,
    kill_switch_engaged: bool = False,
    **overrides: Any,
) -> Dict[str, Any]:
    """Build a run ledger document."""
    ledger: Dict[str, Any] = {
        "schema_version": "1.0",
        "loop_id": loop_id,
        "run_id": "test-run-0001",
        "started_at": "2026-01-01T00:00:00Z",
        "status_before": status_before,
        "status_after": status_after,
        "iterations": iterations if iterations is not None else [make_iteration(1)],
        "daily_tokens_used": daily_tokens_used,
        "kill_switch_engaged": kill_switch_engaged,
    }
    ledger.update(overrides)
    return copy.deepcopy(ledger)


def make_run_id(
    loop_id: str = "sample-loop",
    timestamp: str = "20260101T000000Z",
    suffix: str = "a1b2c3d4e5f6",
) -> str:
    """Build a canonical <loop-id>--<UTC timestamp>--<12 lowercase hex> run id."""
    return "{}--{}--{}".format(loop_id, timestamp, suffix)


def make_persistable_ledger(
    loop_id: str = "sample-loop",
    run_id: Optional[str] = None,
    iterations: Optional[List[Dict[str, Any]]] = None,
    status_before: str = "REPORT_ONLY",
    status_after: str = "REPORT_ONLY",
    repository: str = "mellycore-aios",
    branch: str = "publish/mellycore-main-001",
    head_sha: str = "a" * 40,
    started_at: str = "2026-01-01T00:00:00Z",
    completed_at: str = "2026-01-01T00:05:00Z",
    outcome: str = "success",
    repository_mutation_count: int = 0,
    remote_action_count: int = 0,
    **overrides: Any,
) -> Dict[str, Any]:
    """Build a run ledger document that also satisfies persist-run's additional
    persistence-only field requirements (repository, branch, head_sha,
    completed_at, outcome, and the two zero-by-default Phase 1 counters).
    """
    run_id = run_id or make_run_id(loop_id)
    ledger = make_ledger(
        loop_id=loop_id,
        iterations=iterations,
        status_before=status_before,
        status_after=status_after,
        run_id=run_id,
        started_at=started_at,
    )
    ledger.update(
        {
            "repository": repository,
            "branch": branch,
            "head_sha": head_sha,
            "completed_at": completed_at,
            "outcome": outcome,
            "repository_mutation_count": repository_mutation_count,
            "remote_action_count": remote_action_count,
        }
    )
    ledger.update(overrides)
    return copy.deepcopy(ledger)


def make_budgets(**overrides: Any) -> Dict[str, Any]:
    """Build a budgets document for the estimator."""
    budgets: Dict[str, Any] = {
        "schema_version": "1.0",
        "basis": "ESTIMATE_NOT_MEASURED",
        "global": {
            "paused": False,
            "kill_switch_file": KILL_SWITCH_FILE,
            "daily_token_budget_all_loops": 400000,
            "max_parallel_loops": 1,
        },
        "estimation_model": {
            "scenarios": {
                "no_op": {"input_tokens": 4000, "output_tokens": 500},
                "report": {"input_tokens": 25000, "output_tokens": 3000},
                "assisted_action": {"input_tokens": 60000, "output_tokens": 8000},
            },
            "realistic_mix": {"weights": {"no_op": 0.6, "report": 0.35, "assisted_action": 0.05}},
            "multipliers": {
                "maker_checker": {"value": 2.0},
                "parallel_agents_default": {"value": 1.0},
                "retry_overhead": {"value": 1.25},
            },
        },
    }
    budgets.update(overrides)
    return copy.deepcopy(budgets)
