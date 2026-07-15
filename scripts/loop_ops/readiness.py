"""Capability audit for MellyCore loops.

This module exists to answer one question honestly: *what can this loop actually
do right now?*

The tempting shortcut is to score a project by counting files: registry present,
schema present, docs present, therefore ready. That is how a project talks
itself into believing it is ready for unattended operation when nothing has ever
been run. MellyCore refuses that shortcut.

Each capability tier must be earned on its own evidence:

- ``configured``          a registry entry exists. This proves authorship only.
- ``validated``           the entry passes validation.
- ``exercised``           a real run is recorded in loop state. An example file
                          never counts.
- ``human_approved``      an operator recorded explicit approval in the state.
- ``production_enabled``  unattended operation. Requires all of the above plus an
                          independent verifier and an approved enabling task.
                          Unreachable in Phase 1, by design.

A tier is never inferred from a weaker one, and every ``false`` carries a stated
reason so the gap is legible rather than implied.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import (
    CAPABILITY_TIERS,
    TIER_CONFIGURED,
    TIER_EXERCISED,
    TIER_HUMAN_APPROVED,
    TIER_PRODUCTION_ENABLED,
    TIER_VALIDATED,
    TIER_DEFINITIONS,
    InvalidInputError,
    LoopSpec,
    Registry,
)
from .registry import parse_ledger, repo_root
from .validators import ERROR, validate_loop, validate_registry_shape


def _load_state(loop: LoopSpec, root: Path) -> Optional[Dict[str, Any]]:
    """Load a loop's state file, or None if absent/unreadable.

    An unreadable state file is treated the same as a missing one: it cannot be
    used as evidence of anything.
    """
    path = root / loop.state_file
    if not path.exists() or not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _load_evidence_record(path: Path) -> Optional[Dict[str, Any]]:
    """Load a persisted evidence record, or None if absent/unreadable.

    An unreadable or missing evidence file is treated the same as absent: it
    cannot be used as evidence of anything.
    """
    if not path.exists() or not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _entry_is_real_run(entry: Any, loop: LoopSpec, root: Path) -> bool:
    """True only when a ``run_history`` entry's ``ledger_ref`` resolves to a
    real, independently-validated evidence file under this loop's own
    ``runs/`` directory whose content is internally consistent with the
    state's own claim.

    This is the fix for the gap the persistence review named D4: previously,
    a ``run_history`` entry with a ``run_id`` and ``finished_at`` was trusted
    at face value, with no check that the evidence it claims to point to
    actually exists or is valid. An entry that merely exists in state, with no
    backing evidence file (or a backing file that fails validation, or
    disagrees with the state's own claim), is not exercised -- it is an
    orphan claim.
    """
    if not isinstance(entry, dict):
        return False
    run_id = entry.get("run_id")
    finished_at = entry.get("finished_at")
    ledger_ref = entry.get("ledger_ref")
    if not run_id or not finished_at or not ledger_ref or not isinstance(ledger_ref, str):
        return False

    expected_prefix = "shared_context/loops/runs/{}/".format(loop.id)
    if not ledger_ref.startswith(expected_prefix):
        return False

    record = _load_evidence_record(root / ledger_ref)
    if record is None:
        return False
    if record.get("final_classification") != "PERSISTED":
        return False

    ledger = record.get("ledger")
    if not isinstance(ledger, dict):
        return False
    if ledger.get("loop_id") != loop.id or ledger.get("run_id") != run_id:
        return False
    if ledger.get("completed_at") != finished_at:
        return False
    if not ledger.get("repository") or not ledger.get("head_sha"):
        return False
    if ledger.get("repository_mutation_count") != 0 or ledger.get("remote_action_count") != 0:
        return False

    try:
        parse_ledger(ledger)
    except InvalidInputError:
        return False

    return True


def _real_run_count(state: Optional[Dict[str, Any]], loop: LoopSpec, root: Path) -> int:
    """Count recorded real runs.

    Only counts ``run_history`` entries whose ``ledger_ref`` resolves to real,
    independently-validated evidence. See :func:`_entry_is_real_run`.
    """
    if not state:
        return 0
    history = state.get("run_history")
    if not isinstance(history, list):
        return 0
    return sum(1 for entry in history if _entry_is_real_run(entry, loop, root))


def _human_approved(state: Optional[Dict[str, Any]]) -> bool:
    """True only when an operator explicitly recorded approval."""
    if not state:
        return False
    approval = state.get("human_approval")
    if not isinstance(approval, dict):
        return False
    return approval.get("granted") is True and bool(approval.get("granted_by"))


def audit_loop(loop: LoopSpec, registry: Registry, root: Optional[Path] = None) -> Dict[str, Any]:
    """Audit one loop's real capability."""
    root = root or repo_root()
    state = _load_state(loop, root)

    capabilities: Dict[str, Dict[str, Any]] = {}

    # configured
    capabilities[TIER_CONFIGURED] = {
        "value": True,
        "evidence": "registry entry present in LOOP_REGISTRY.json",
    }

    # validated
    findings = validate_loop(loop, registry, root=root)
    errors = [f for f in findings if f.severity == ERROR]
    capabilities[TIER_VALIDATED] = {
        "value": not errors,
        "evidence": (
            "passes scripts.loop_ops validate"
            if not errors
            else "validation errors: {}".format([f.code for f in errors])
        ),
    }

    # exercised
    runs = _real_run_count(state, loop, root)
    capabilities[TIER_EXERCISED] = {
        "value": runs > 0,
        "evidence": (
            "{} recorded run(s) in {}".format(runs, loop.state_file)
            if runs > 0
            else "no run recorded; state file {}".format(
                "absent (template)" if state is None else "present but records no finished run"
            )
        ),
    }

    # human_approved
    approved = _human_approved(state)
    capabilities[TIER_HUMAN_APPROVED] = {
        "value": approved,
        "evidence": (
            "operator approval recorded in loop state"
            if approved
            else "no operator approval recorded in loop state"
        ),
    }

    # production_enabled
    blockers: List[str] = []
    if registry.phase == 1:
        blockers.append("Phase 1 is report-only; unattended operation is not authorized")
    if not capabilities[TIER_VALIDATED]["value"]:
        blockers.append("loop does not pass validation")
    if not capabilities[TIER_EXERCISED]["value"]:
        blockers.append("loop has never been run")
    if not approved:
        blockers.append("no operator approval recorded")
    if not loop.verifier_required:
        blockers.append("no independent verifier is required by this loop")

    capabilities[TIER_PRODUCTION_ENABLED] = {
        "value": False if blockers else True,
        "evidence": (
            "blocked by: {}".format("; ".join(blockers))
            if blockers
            else "all prerequisites met and an enabling task was approved"
        ),
    }

    highest = None
    for tier in CAPABILITY_TIERS:
        if capabilities[tier]["value"]:
            highest = tier
        else:
            break

    return {
        "loop_id": loop.id,
        "title": loop.title,
        "status": loop.status,
        "level": loop.level,
        "action_capable": loop.is_action_capable,
        "enabled": loop.is_enabled,
        "verifier_required": loop.verifier_required,
        "capabilities": capabilities,
        "highest_earned_tier": highest,
    }


def audit_registry(registry: Registry, root: Optional[Path] = None) -> Dict[str, Any]:
    """Audit every loop and summarise the foundation's real readiness."""
    root = root or repo_root()
    loop_reports = [audit_loop(loop, registry, root=root) for loop in registry.loops]

    registry_errors = [f for f in validate_registry_shape(registry) if f.severity == ERROR]

    def count(tier: str) -> int:
        return sum(1 for r in loop_reports if r["capabilities"][tier]["value"])

    exercised = count(TIER_EXERCISED)

    return {
        "registry_id": registry.registry_id,
        "phase": registry.phase,
        "schema_version": registry.schema_version,
        "registry_valid": not registry_errors,
        "tier_definitions": TIER_DEFINITIONS,
        "summary": {
            "loops_total": len(loop_reports),
            "loops_enabled": sum(1 for r in loop_reports if r["enabled"]),
            "loops_disabled": sum(1 for r in loop_reports if r["status"] == "DISABLED"),
            TIER_CONFIGURED: count(TIER_CONFIGURED),
            TIER_VALIDATED: count(TIER_VALIDATED),
            TIER_EXERCISED: exercised,
            TIER_HUMAN_APPROVED: count(TIER_HUMAN_APPROVED),
            TIER_PRODUCTION_ENABLED: count(TIER_PRODUCTION_ENABLED),
        },
        "honest_assessment": (
            "Configured and validated only. No loop has been exercised, so no loop has real run "
            "evidence, and none is approved or production-enabled. Do not describe this foundation "
            "as operational or unattended-ready."
            if exercised == 0
            else "{} loop(s) have recorded run evidence. Review each loop's tiers before claiming "
            "readiness; configured is not exercised.".format(exercised)
        ),
        "loops": loop_reports,
    }
