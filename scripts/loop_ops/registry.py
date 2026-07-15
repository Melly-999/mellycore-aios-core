"""Loading and parsing of the MellyCore loop registry, states, and ledgers.

Parsing is separated from validation on purpose. This module answers "can this
be read at all"; ``validators`` answers "is it acceptable". Every loader raises
:class:`InvalidInputError` rather than returning a partial object, so a caller
never operates on half-understood input.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import (
    SUPPORTED_LEDGER_MAJOR,
    SUPPORTED_REGISTRY_MAJOR,
    InvalidInputError,
    Iteration,
    LoopSpec,
    Registry,
    RunLedger,
)

DEFAULT_REGISTRY_PATH = "shared_context/loops/LOOP_REGISTRY.json"
DEFAULT_BUDGETS_PATH = "shared_context/loops/LOOP_BUDGETS.json"


def repo_root() -> Path:
    """Return the repository root, derived from this file's location.

    ``scripts/loop_ops/registry.py`` -> parents[2] is the repo root. Deriving it
    from ``__file__`` rather than the process working directory means the CLI
    behaves the same regardless of where it is invoked from.
    """
    return Path(__file__).resolve().parents[2]


def resolve_path(path_like: Any, root: Optional[Path] = None) -> Path:
    """Resolve a possibly-relative path against the repo root."""
    root = root or repo_root()
    candidate = Path(str(path_like))
    if candidate.is_absolute():
        return candidate
    return root / candidate


def load_json(path: Path) -> Dict[str, Any]:
    """Load a JSON object from ``path``.

    Raises:
        InvalidInputError: if the file is missing, unreadable, not valid JSON,
            or not a JSON object.
    """
    if not path.exists():
        raise InvalidInputError("file not found: {}".format(path))
    if not path.is_file():
        raise InvalidInputError("not a file: {}".format(path))
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise InvalidInputError("cannot read {}: {}".format(path, exc)) from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise InvalidInputError("invalid JSON in {}: {}".format(path, exc)) from exc
    if not isinstance(data, dict):
        raise InvalidInputError("expected a JSON object at top level in {}".format(path))
    return data


def _major(version: Any) -> str:
    return str(version).split(".")[0].strip()


def check_schema_version(version: Any, supported_major: str, what: str) -> None:
    """Refuse a contract version we do not understand, rather than guessing."""
    if not version:
        raise InvalidInputError("{}: schema_version is required".format(what))
    if _major(version) != supported_major:
        raise InvalidInputError(
            "{}: unsupported schema_version {!r} (this tool understands major version {})".format(
                what, version, supported_major
            )
        )


def _require(data: Dict[str, Any], key: str, what: str) -> Any:
    if key not in data:
        raise InvalidInputError("{}: missing required field {!r}".format(what, key))
    return data[key]


def _as_str_list(value: Any, what: str, key: str) -> List[str]:
    if not isinstance(value, list) or any(not isinstance(v, str) for v in value):
        raise InvalidInputError("{}: {!r} must be a list of strings".format(what, key))
    return list(value)


def parse_loop(data: Dict[str, Any], index: int) -> LoopSpec:
    """Parse one registry loop entry.

    Type errors are raised here so that ``validators`` can assume well-typed
    fields and concentrate on policy.
    """
    what = "loops[{}]".format(index)
    loop_id = _require(data, "id", what)
    if not isinstance(loop_id, str) or not loop_id.strip():
        raise InvalidInputError("{}: 'id' must be a non-empty string".format(what))
    what = "loop {!r}".format(loop_id)

    for key in (
        "title",
        "purpose",
        "owner",
        "level",
        "status",
        "trigger_type",
        "suggested_cadence",
        "state_file",
        "kill_switch",
        "success_condition",
        "escalation_condition",
    ):
        value = _require(data, key, what)
        if not isinstance(value, str):
            raise InvalidInputError("{}: {!r} must be a string".format(what, key))

    for key in ("max_attempts", "stagnation_threshold", "no_progress_threshold",
                "per_run_token_budget", "daily_token_budget"):
        value = _require(data, key, what)
        # bool is an int subclass in Python; reject it explicitly.
        if not isinstance(value, int) or isinstance(value, bool):
            raise InvalidInputError("{}: {!r} must be an integer".format(what, key))

    verifier_required = _require(data, "verifier_required", what)
    if not isinstance(verifier_required, bool):
        raise InvalidInputError("{}: 'verifier_required' must be a boolean".format(what))

    template_flag = data.get("state_file_is_template", True)
    if not isinstance(template_flag, bool):
        raise InvalidInputError("{}: 'state_file_is_template' must be a boolean".format(what))

    return LoopSpec(
        id=loop_id,
        title=data["title"],
        purpose=data["purpose"],
        owner=data["owner"],
        level=data["level"],
        status=data["status"],
        trigger_type=data["trigger_type"],
        suggested_cadence=data["suggested_cadence"],
        read_scope=_as_str_list(_require(data, "read_scope", what), what, "read_scope"),
        allowed_write_scope=_as_str_list(
            _require(data, "allowed_write_scope", what), what, "allowed_write_scope"
        ),
        forbidden_paths=_as_str_list(
            _require(data, "forbidden_paths", what), what, "forbidden_paths"
        ),
        state_file=data["state_file"],
        state_file_is_template=template_flag,
        verifier_required=verifier_required,
        max_attempts=data["max_attempts"],
        stagnation_threshold=data["stagnation_threshold"],
        no_progress_threshold=data["no_progress_threshold"],
        per_run_token_budget=data["per_run_token_budget"],
        daily_token_budget=data["daily_token_budget"],
        human_gates=_as_str_list(_require(data, "human_gates", what), what, "human_gates"),
        kill_switch=data["kill_switch"],
        success_condition=data["success_condition"],
        escalation_condition=data["escalation_condition"],
        raw=dict(data),
    )


def parse_registry(data: Dict[str, Any]) -> Registry:
    """Parse a registry document into a :class:`Registry`."""
    what = "registry"
    check_schema_version(data.get("schema_version"), SUPPORTED_REGISTRY_MAJOR, what)

    phase = _require(data, "phase", what)
    if not isinstance(phase, int) or isinstance(phase, bool):
        raise InvalidInputError("registry: 'phase' must be an integer")

    kill_switch = _require(data, "global_kill_switch", what)
    if not isinstance(kill_switch, dict):
        raise InvalidInputError("registry: 'global_kill_switch' must be an object")

    loops_raw = _require(data, "loops", what)
    if not isinstance(loops_raw, list) or not loops_raw:
        raise InvalidInputError("registry: 'loops' must be a non-empty list")

    loops = []
    for index, entry in enumerate(loops_raw):
        if not isinstance(entry, dict):
            raise InvalidInputError("registry: loops[{}] must be an object".format(index))
        loops.append(parse_loop(entry, index))

    return Registry(
        schema_version=str(data["schema_version"]),
        registry_id=str(data.get("registry_id", "")),
        phase=phase,
        global_kill_switch=kill_switch,
        global_forbidden_paths=_as_str_list(
            _require(data, "global_forbidden_paths", what), what, "global_forbidden_paths"
        ),
        lifecycle_states=_as_str_list(
            _require(data, "lifecycle_states", what), what, "lifecycle_states"
        ),
        loops=loops,
        raw=dict(data),
    )


def load_registry(path: Optional[Any] = None) -> Registry:
    """Load and parse the registry from ``path`` or the default location."""
    target = resolve_path(path or DEFAULT_REGISTRY_PATH)
    return parse_registry(load_json(target))


def load_budgets(path: Optional[Any] = None) -> Dict[str, Any]:
    """Load the budgets document.

    Every figure in it is an estimate. See ``cost.py``.
    """
    target = resolve_path(path or DEFAULT_BUDGETS_PATH)
    return load_json(target)


def _parse_iteration(data: Dict[str, Any], index: int) -> Iteration:
    what = "iterations[{}]".format(index)
    if not isinstance(data, dict):
        raise InvalidInputError("{}: must be an object".format(what))

    idx = _require(data, "index", what)
    if not isinstance(idx, int) or isinstance(idx, bool) or idx < 1:
        raise InvalidInputError("{}: 'index' must be an integer >= 1".format(what))

    outcome = _require(data, "outcome", what)
    if outcome not in ("success", "failure"):
        raise InvalidInputError(
            "{}: 'outcome' must be 'success' or 'failure', got {!r}".format(what, outcome)
        )

    started_at = _require(data, "started_at", what)
    if not isinstance(started_at, str):
        raise InvalidInputError("{}: 'started_at' must be a string".format(what))

    error_signature = data.get("error_signature")
    if error_signature is not None and not isinstance(error_signature, str):
        raise InvalidInputError("{}: 'error_signature' must be a string or null".format(what))
    if outcome == "failure" and not error_signature:
        # Without a signature the same failure cannot be recognised as the same,
        # which would silently disable stagnation detection.
        raise InvalidInputError(
            "{}: a failed iteration requires a non-empty 'error_signature'".format(what)
        )

    progress_marker = data.get("progress_marker")
    if progress_marker is not None and not isinstance(progress_marker, str):
        raise InvalidInputError("{}: 'progress_marker' must be a string or null".format(what))

    tokens = data.get("tokens") or {}
    if not isinstance(tokens, dict):
        raise InvalidInputError("{}: 'tokens' must be an object".format(what))
    measured = tokens.get("measured", False)
    if not isinstance(measured, bool):
        raise InvalidInputError("{}: 'tokens.measured' must be a boolean".format(what))
    total = tokens.get("total", None)
    # The token contract is conditional on 'measured' and is asymmetric on
    # purpose: 'measured: false' must never carry a numeric total (including
    # zero), because "not measured" and "measured, and it was zero" must stay
    # distinguishable. 'measured: true' must carry a real non-negative number,
    # because a claimed measurement with no value is a contradiction, not an
    # edge case to tolerate.
    if measured:
        if total is None:
            raise InvalidInputError(
                "{}: 'tokens.total' is required and must be a non-negative integer when "
                "'tokens.measured' is true".format(what)
            )
        if not isinstance(total, int) or isinstance(total, bool) or total < 0:
            raise InvalidInputError("{}: 'tokens.total' must be a non-negative integer".format(what))
    else:
        if total is not None:
            raise InvalidInputError(
                "{}: 'tokens.total' must be null or absent when 'tokens.measured' is false; an "
                "unmeasured iteration must never carry a numeric total, including zero".format(what)
            )

    verifier = data.get("verifier") or {}
    if not isinstance(verifier, dict):
        raise InvalidInputError("{}: 'verifier' must be an object or null".format(what))
    verdict = verifier.get("verdict", "NOT_RUN")
    if verdict not in ("ACCEPT", "REJECT", "NOT_RUN"):
        raise InvalidInputError(
            "{}: 'verifier.verdict' must be ACCEPT, REJECT, or NOT_RUN".format(what)
        )

    return Iteration(
        index=idx,
        started_at=started_at,
        outcome=outcome,
        error_signature=error_signature,
        progress_marker=progress_marker,
        tokens_total=total,
        tokens_measured=measured,
        verifier_verdict=verdict,
    )


def parse_ledger(data: Dict[str, Any]) -> RunLedger:
    """Parse a run ledger document."""
    what = "ledger"
    check_schema_version(data.get("schema_version"), SUPPORTED_LEDGER_MAJOR, what)

    for key in ("loop_id", "run_id", "started_at", "status_before", "status_after"):
        value = _require(data, key, what)
        if not isinstance(value, str) or not value.strip():
            raise InvalidInputError("ledger: {!r} must be a non-empty string".format(key))

    iterations_raw = _require(data, "iterations", what)
    if not isinstance(iterations_raw, list):
        raise InvalidInputError("ledger: 'iterations' must be a list")

    iterations = [_parse_iteration(entry, i) for i, entry in enumerate(iterations_raw)]

    seen = [it.index for it in iterations]
    if seen != sorted(set(seen)):
        # A repeated or out-of-order index means the ledger was rewritten rather
        # than appended to, which would let a failure be edited out of history.
        raise InvalidInputError(
            "ledger: iteration indexes must be unique and strictly increasing, got {}".format(seen)
        )

    daily = data.get("daily_tokens_used")
    if daily is not None and (not isinstance(daily, int) or isinstance(daily, bool) or daily < 0):
        raise InvalidInputError("ledger: 'daily_tokens_used' must be an integer >= 0 or null")

    kill = data.get("kill_switch_engaged", False)
    if not isinstance(kill, bool):
        raise InvalidInputError("ledger: 'kill_switch_engaged' must be a boolean")

    return RunLedger(
        schema_version=str(data["schema_version"]),
        loop_id=data["loop_id"],
        run_id=data["run_id"],
        started_at=data["started_at"],
        status_before=data["status_before"],
        status_after=data["status_after"],
        iterations=iterations,
        daily_tokens_used=daily,
        kill_switch_engaged=kill,
        raw=dict(data),
    )


def load_ledger(path: Any) -> RunLedger:
    """Load and parse a run ledger from ``path``."""
    return parse_ledger(load_json(resolve_path(path)))
