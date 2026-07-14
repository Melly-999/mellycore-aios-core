"""Policy validation for the MellyCore loop registry.

``registry.py`` decides whether input can be read. This module decides whether
it is acceptable. Every rule here is deterministic and calls no model.

The rules that matter most are the Phase 1 gates: an enabled loop must be
report-only, must have no write scope, and must carry at least one human gate.
These are enforced structurally so that a mistake in the registry becomes a
failed validation rather than an agent quietly acting on a bad entry.
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from .models import (
    ACTION_CAPABLE_LEVELS,
    LEVELS,
    LIFECYCLE_STATES,
    PHASE1_FORBIDDEN_STATUSES,
    TRIGGER_TYPES,
    Finding,
    LoopSpec,
    Registry,
)
from .registry import repo_root

ERROR = "error"
WARNING = "warning"


def _error(code: str, message: str, loop_id: Optional[str] = None) -> Finding:
    return Finding(severity=ERROR, code=code, message=message, loop_id=loop_id)


def _warning(code: str, message: str, loop_id: Optional[str] = None) -> Finding:
    return Finding(severity=WARNING, code=code, message=message, loop_id=loop_id)


def validate_registry_shape(registry: Registry) -> List[Finding]:
    """Check registry-level invariants."""
    findings: List[Finding] = []

    declared = set(registry.lifecycle_states)
    known = set(LIFECYCLE_STATES)
    if declared != known:
        findings.append(
            _error(
                "LIFECYCLE_SET_MISMATCH",
                "registry lifecycle_states {} do not match the states this tool implements {}".format(
                    sorted(declared), sorted(known)
                ),
            )
        )

    if not registry.global_forbidden_paths:
        findings.append(
            _error("GLOBAL_FORBIDDEN_EMPTY", "global_forbidden_paths must not be empty")
        )

    kill_file = registry.global_kill_switch.get("file")
    if not kill_file:
        findings.append(
            _error("KILL_SWITCH_UNDEFINED", "global_kill_switch.file must name a kill switch path")
        )

    if registry.phase < 1:
        findings.append(_error("PHASE_INVALID", "phase must be >= 1"))

    return findings


def validate_unique_ids(registry: Registry) -> List[Finding]:
    """Duplicate IDs make every other check ambiguous, so they are errors."""
    findings: List[Finding] = []
    seen = set()
    for loop in registry.loops:
        if loop.id in seen:
            findings.append(
                _error("DUPLICATE_LOOP_ID", "loop id {!r} is defined more than once".format(loop.id), loop.id)
            )
        seen.add(loop.id)
    return findings


def validate_loop(loop: LoopSpec, registry: Registry, root: Optional[Path] = None) -> List[Finding]:
    """Check a single loop entry against Phase 1 policy."""
    findings: List[Finding] = []
    root = root or repo_root()

    if loop.status not in LIFECYCLE_STATES:
        findings.append(
            _error("INVALID_STATUS", "status {!r} is not a known lifecycle state".format(loop.status), loop.id)
        )

    if loop.level not in LEVELS:
        findings.append(
            _error("INVALID_LEVEL", "level {!r} is not one of {}".format(loop.level, list(LEVELS)), loop.id)
        )

    if loop.trigger_type not in TRIGGER_TYPES:
        findings.append(
            _error(
                "INVALID_TRIGGER",
                "trigger_type {!r} is not one of {}".format(loop.trigger_type, list(TRIGGER_TYPES)),
                loop.id,
            )
        )

    # --- Budgets -------------------------------------------------------------
    for name, value in (
        ("max_attempts", loop.max_attempts),
        ("stagnation_threshold", loop.stagnation_threshold),
        ("no_progress_threshold", loop.no_progress_threshold),
        ("per_run_token_budget", loop.per_run_token_budget),
        ("daily_token_budget", loop.daily_token_budget),
    ):
        if value <= 0:
            findings.append(
                _error("BUDGET_NOT_POSITIVE", "{} must be greater than zero, got {}".format(name, value), loop.id)
            )

    if loop.daily_token_budget < loop.per_run_token_budget:
        findings.append(
            _error(
                "BUDGET_INCOHERENT",
                "daily_token_budget ({}) is below per_run_token_budget ({}), so the first run would "
                "always exceed the day".format(loop.daily_token_budget, loop.per_run_token_budget),
                loop.id,
            )
        )

    # --- Human gates ---------------------------------------------------------
    if not loop.human_gates:
        findings.append(
            _error("NO_HUMAN_GATE", "at least one human gate is required; a loop with no gate is not acceptable", loop.id)
        )

    # --- Forbidden paths -----------------------------------------------------
    if not loop.forbidden_paths:
        findings.append(_error("FORBIDDEN_PATHS_EMPTY", "forbidden_paths must not be empty", loop.id))

    missing = [p for p in registry.global_forbidden_paths if p not in loop.forbidden_paths]
    if missing:
        findings.append(
            _error(
                "FORBIDDEN_PATHS_INCOMPLETE",
                "forbidden_paths must include every global baseline path; missing: {}".format(missing),
                loop.id,
            )
        )

    if loop.kill_switch != registry.global_kill_switch.get("file"):
        findings.append(
            _error(
                "KILL_SWITCH_MISMATCH",
                "kill_switch {!r} does not match the global kill switch {!r}; a loop must not opt out of "
                "the global halt".format(loop.kill_switch, registry.global_kill_switch.get("file")),
                loop.id,
            )
        )

    # --- Phase 1 gates -------------------------------------------------------
    if registry.phase == 1:
        if loop.status in PHASE1_FORBIDDEN_STATUSES:
            findings.append(
                _error(
                    "PHASE1_STATUS_FORBIDDEN",
                    "status {!r} is not permitted in Phase 1; Phase 1 is report-only".format(loop.status),
                    loop.id,
                )
            )

        if loop.is_enabled and loop.allowed_write_scope:
            findings.append(
                _error(
                    "PHASE1_ENABLED_ACTION_LOOP",
                    "loop is enabled (status {}) but declares a write scope {}; enabled loops must be "
                    "report-only in Phase 1".format(loop.status, loop.allowed_write_scope),
                    loop.id,
                )
            )

        if loop.is_enabled and loop.level in ACTION_CAPABLE_LEVELS:
            findings.append(
                _error(
                    "PHASE1_ENABLED_ACTION_LEVEL",
                    "loop is enabled (status {}) at action-capable level {}; only L0/L1 may be enabled "
                    "in Phase 1".format(loop.status, loop.level),
                    loop.id,
                )
            )

    if loop.status == "DISABLED" and not loop.raw.get("disabled_reason"):
        findings.append(
            _error("DISABLED_WITHOUT_REASON", "a DISABLED loop must state a disabled_reason", loop.id)
        )

    # --- State file ----------------------------------------------------------
    if not loop.state_file_is_template:
        state_path = root / loop.state_file
        if not state_path.exists():
            findings.append(
                _error(
                    "STATE_FILE_MISSING",
                    "state_file {!r} does not exist and is not marked as a template".format(loop.state_file),
                    loop.id,
                )
            )

    expected_prefix = "shared_context/loops/states/"
    if not loop.state_file.startswith(expected_prefix):
        findings.append(
            _warning(
                "STATE_FILE_LOCATION",
                "state_file {!r} is outside {}".format(loop.state_file, expected_prefix),
                loop.id,
            )
        )

    if not loop.read_scope:
        findings.append(_error("READ_SCOPE_EMPTY", "read_scope must not be empty", loop.id))

    return findings


def validate(registry: Registry, root: Optional[Path] = None) -> List[Finding]:
    """Run every validation rule and return all findings."""
    findings: List[Finding] = []
    findings.extend(validate_registry_shape(registry))
    findings.extend(validate_unique_ids(registry))
    for loop in registry.loops:
        findings.extend(validate_loop(loop, registry, root=root))
    return findings


def has_errors(findings: List[Finding]) -> bool:
    return any(f.severity == ERROR for f in findings)
