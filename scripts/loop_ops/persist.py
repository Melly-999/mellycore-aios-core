"""Guarded, human-approved persistence of real MellyCore loop run evidence.

Implements the contract specified (design-only, not built) by
``docs/research/LOOP_STATE_PERSISTENCE_REVIEW_001.md``:

1. **Immutable run evidence** lives at
   ``shared_context/loops/runs/<loop-id>/<run-id>.json``. Write-once. Never
   rewritten. Identical bytes at an existing destination may only be used to
   recover an interrupted state update; different bytes are always refused.
2. **Derived loop state** lives at
   ``shared_context/loops/states/<loop-id>.state.json``. It is always fully
   rebuilt from the complete set of that loop's persisted evidence files (plus
   whatever operator-set fields -- ``human_approval``, ``notes`` -- cannot be
   derived from evidence and so are carried forward). This is what makes state
   reconstructible from evidence alone, by construction, rather than by
   convention.
3. **Persistence is a separate, explicit, human-approved action.** Nothing in
   this module is called as a side effect of running a loop or of ``guard``.
   The only entry points are :func:`dry_run` (validates and writes nothing)
   and :func:`apply` (requires ``operator_approval_id`` and ``expected_head``,
   both supplied by a human through the CLI).

What this module deliberately does NOT do:

- It does not implement corrections to an already-persisted ledger, or
  deletion of one. Phase 1 has no ``--force`` and no correction mechanism.
- It does not grant a loop write scope, mark a loop ``human_approved``, mark a
  loop ``production_enabled``, or promote a loop's lifecycle status beyond
  ``REPORT_ONLY``.
- The ``--operator-approval-id`` recorded in a persisted record is audit
  metadata supplied by whoever invoked the CLI. It is not cryptographic proof
  of operator identity, and this module makes no claim otherwise.

Required *input* ledger fields for persistence (beyond the base contract in
``RUN_LEDGER_SCHEMA.json``, which ``registry.parse_ledger`` already enforces):
``repository``, ``branch``, ``head_sha``, ``completed_at``, ``outcome``,
``repository_mutation_count``, ``remote_action_count``. The guard's decision,
its exit code, validation results, and a final classification are *not*
required as input -- they are computed at persist time and written into the
persisted record alongside the submitted ledger, specifically so that a
persisted record's account of "what the guard decided" is never merely
trusted from the submitter's own claim.
"""

from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import guard as guard_module
from .models import InvalidInputError, LoopOpsError, PHASE1_FORBIDDEN_STATUSES, Registry, RunLedger
from .redaction import scan_text
from .registry import load_json, load_registry, parse_ledger, repo_root, resolve_path

RUNS_DIRNAME = "shared_context/loops/runs"
STATES_DIRNAME = "shared_context/loops/states"

#: <loop-id>--<UTC timestamp>--<12 lowercase hex characters>, e.g.
#: ``project-health--20260715T180000Z--a1b2c3d4e5f6``. The loop-id segment is
#: intentionally permissive here (tightened separately by
#: :func:`validate_loop_id_format`); what this pattern anchors is the overall
#: three-part shape and the timestamp/suffix segments, since a run_id is used
#: directly to construct a filesystem path.
RUN_ID_PATTERN = re.compile(
    r"^(?P<loop_id>[a-z0-9][a-z0-9-]{0,63})--(?P<timestamp>[0-9]{8}T[0-9]{6}Z)--(?P<suffix>[0-9a-f]{12})$"
)

LOOP_ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

PERSIST_ONLY_REQUIRED_FIELDS = (
    "repository",
    "branch",
    "head_sha",
    "completed_at",
    "outcome",
    "repository_mutation_count",
    "remote_action_count",
)

OUTCOME_VALUES = ("success", "failure", "escalated", "paused", "blocked")


class PersistenceError(LoopOpsError):
    """Base class for a refused or partially-completed persist attempt."""


class PersistenceRefused(PersistenceError):
    """Persistence was refused outright, before any file was written.

    ``code`` is a stable, machine-readable reason. Every refusal fails closed:
    nothing is written when this is raised.
    """

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


class PartialPersistenceError(PersistenceError):
    """Evidence was written but the derived-state update failed.

    The evidence file is real and must never be deleted automatically. The
    audit (``readiness.py``) requires a state pointer to classify a loop as
    exercised, so a state-less evidence file is correctly invisible to the
    audit until state is repaired. Retrying ``apply`` with the identical
    ledger will find the existing evidence (status ``identical``) and retry
    only the state update.
    """


@dataclass
class PersistPlan:
    """Everything computed about a candidate persist, before any write happens."""

    loop_id: str
    run_id: str
    evidence_path: Path
    evidence_relpath: str
    state_path: Path
    state_relpath: str
    guard_decision: Any
    ledger_raw: Dict[str, Any]
    proposed_state: Dict[str, Any]
    warnings: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "loop_id": self.loop_id,
            "run_id": self.run_id,
            "evidence_path": self.evidence_relpath,
            "state_path": self.state_relpath,
            "guard_decision": self.guard_decision.decision,
            "guard_exit_code": self.guard_decision.exit_code,
            "proposed_state": self.proposed_state,
            "warnings": list(self.warnings),
            "notes": list(self.notes),
        }


# --- path safety ---------------------------------------------------------


def validate_loop_id_format(loop_id: str) -> None:
    if not isinstance(loop_id, str) or not LOOP_ID_PATTERN.match(loop_id):
        raise PersistenceRefused(
            "INVALID_LOOP_ID", "loop_id {!r} does not match the required kebab-case pattern".format(loop_id)
        )


def validate_run_id_format(run_id: str, loop_id: str) -> None:
    if not isinstance(run_id, str):
        raise PersistenceRefused("INVALID_RUN_ID", "run_id must be a string")
    match = RUN_ID_PATTERN.match(run_id)
    if not match:
        raise PersistenceRefused(
            "INVALID_RUN_ID",
            "run_id {!r} does not match the required <loop-id>--<UTC timestamp>--<12 lowercase hex> "
            "pattern".format(run_id),
        )
    if match.group("loop_id") != loop_id:
        raise PersistenceRefused(
            "RUN_ID_LOOP_MISMATCH",
            "run_id {!r} does not begin with its own loop_id {!r}".format(run_id, loop_id),
        )


def _check_no_symlink_ancestors(path: Path, stop_at: Path) -> None:
    current = path
    while True:
        if current.exists() and current.is_symlink():
            raise PersistenceRefused("SYMLINK_IN_PATH", "path component is a symlink: {}".format(current))
        if current == current.parent or current == stop_at:
            break
        current = current.parent


def _check_case_collision(parent: Path, name: str) -> None:
    if not parent.exists():
        return
    folded = name.casefold()
    for entry in parent.iterdir():
        if entry.name != name and entry.name.casefold() == folded:
            raise PersistenceRefused(
                "CASE_COLLISION",
                "an entry differing only in case already exists at {}: {!r} vs {!r}".format(
                    parent, entry.name, name
                ),
            )


def resolve_run_path(loop_id: str, run_id: str, root: Path) -> Path:
    """Compute the immutable-evidence path for a run, validating everything first.

    The run_id's own pattern (``^[a-z0-9][a-z0-9-]{0,63}--...$``) already
    excludes ``/``, ``\\``, and ``..``, so a match alone rules out traversal
    and absolute-path attempts. The containment check below is defense in
    depth: it never trusts that fact alone.
    """
    validate_loop_id_format(loop_id)
    validate_run_id_format(run_id, loop_id)

    runs_root = root / RUNS_DIRNAME
    target = runs_root / loop_id / (run_id + ".json")

    try:
        target.resolve().relative_to(runs_root.resolve())
    except ValueError:
        raise PersistenceRefused(
            "PATH_ESCAPE", "resolved evidence path {} escapes the canonical runs directory".format(target)
        )

    return target


def resolve_state_path(loop_id: str, root: Path) -> Path:
    validate_loop_id_format(loop_id)
    states_root = root / STATES_DIRNAME
    target = states_root / "{}.state.json".format(loop_id)

    try:
        target.resolve().relative_to(states_root.resolve())
    except ValueError:
        raise PersistenceRefused(
            "PATH_ESCAPE", "resolved state path {} escapes the canonical states directory".format(target)
        )

    return target


def _relpath(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


# --- git identity (subprocess only; no new dependency) --------------------


def _run_git(args: List[str], cwd: Path) -> str:
    try:
        completed = subprocess.run(
            ["git"] + args,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=30,
        )
    except FileNotFoundError as exc:
        raise InvalidInputError("git executable not found") from exc
    except subprocess.TimeoutExpired as exc:
        raise InvalidInputError("git command timed out: git {}".format(" ".join(args))) from exc
    if completed.returncode != 0:
        raise InvalidInputError(
            "git {} failed: {}".format(" ".join(args), completed.stderr.decode("utf-8", "replace").strip())
        )
    return completed.stdout.decode("utf-8", "replace").strip()


def current_branch(root: Path) -> str:
    return _run_git(["rev-parse", "--abbrev-ref", "HEAD"], root)


def current_head(root: Path) -> str:
    return _run_git(["rev-parse", "HEAD"], root)


def validate_repository_identity(raw: Dict[str, Any], root: Path) -> List[str]:
    """Record (never block on) any mismatch between the ledger's declared
    repository identity and the repository persist-run is actually running
    in. Historical evidence from elsewhere or a different commit is still
    real evidence -- the mismatch must be visible, not hidden or refused.
    """
    notes: List[str] = []
    actual_branch = current_branch(root)
    actual_head = current_head(root)
    declared_branch = raw.get("branch")
    declared_head = raw.get("head_sha")
    if declared_branch != actual_branch:
        notes.append(
            "branch mismatch: ledger declares branch {!r}, current repository branch is {!r}".format(
                declared_branch, actual_branch
            )
        )
    if declared_head != actual_head:
        notes.append(
            "head_sha mismatch: ledger declares head_sha {!r}, current repository HEAD is {!r}".format(
                declared_head, actual_head
            )
        )
    return notes


# --- timestamp validation ---------------------------------------------------


def _parse_iso8601_z(value: Any, field_name: str) -> datetime.datetime:
    if not isinstance(value, str):
        raise PersistenceRefused("INVALID_TIMESTAMP", "{} must be a string".format(field_name))
    text = value.strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.datetime.fromisoformat(text)
    except ValueError as exc:
        raise PersistenceRefused(
            "INVALID_TIMESTAMP", "{} {!r} is not a valid ISO-8601 timestamp: {}".format(field_name, value, exc)
        ) from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=datetime.timezone.utc)
    return parsed.astimezone(datetime.timezone.utc)


def validate_timestamps(raw: Dict[str, Any], now: Optional[datetime.datetime] = None) -> None:
    now = now or datetime.datetime.now(datetime.timezone.utc)
    started = _parse_iso8601_z(raw.get("started_at"), "started_at")
    completed = _parse_iso8601_z(raw.get("completed_at"), "completed_at")
    if completed < started:
        raise PersistenceRefused("FINISHED_BEFORE_STARTED", "completed_at is earlier than started_at")
    if started > now or completed > now:
        raise PersistenceRefused(
            "FUTURE_TIMESTAMP",
            "a ledger timestamp is after the persist action's own wall clock; refusing to persist "
            "evidence from the future",
        )


# --- ledger validation for persistence --------------------------------------


def load_ledger_document(path: Any) -> Dict[str, Any]:
    return load_json(resolve_path(path))


def validate_ledger_for_persistence(raw: Dict[str, Any]) -> RunLedger:
    """Full validation: the base ledger contract (which enforces the corrected
    token semantics) plus the additional fields required before evidence may
    be persisted. Raises :class:`PersistenceRefused` or
    :class:`~scripts.loop_ops.models.InvalidInputError` on any violation.
    """
    ledger = parse_ledger(raw)

    missing = [f for f in PERSIST_ONLY_REQUIRED_FIELDS if raw.get(f) in (None, "")]
    if missing:
        raise PersistenceRefused(
            "MISSING_PERSIST_FIELDS",
            "ledger is missing field(s) required for persistence: {}".format(missing),
        )

    if raw.get("outcome") not in OUTCOME_VALUES:
        raise PersistenceRefused(
            "INVALID_OUTCOME", "outcome {!r} must be one of {}".format(raw.get("outcome"), OUTCOME_VALUES)
        )

    for count_field in ("repository_mutation_count", "remote_action_count"):
        value = raw.get(count_field)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise PersistenceRefused(
                "INVALID_COUNT", "{} must be a non-negative integer, got {!r}".format(count_field, value)
            )

    for field_name in ("repository", "branch", "head_sha", "completed_at"):
        value = raw.get(field_name)
        if not isinstance(value, str) or not value.strip():
            raise PersistenceRefused(
                "MISSING_PERSIST_FIELDS", "{!r} must be a non-empty string".format(field_name)
            )

    return ledger


# --- evidence and state I/O -------------------------------------------------


def _iso_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _load_existing_state(path: Path) -> Optional[Dict[str, Any]]:
    if not path.exists() or not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def list_persisted_ledgers(loop_id: str, root: Path) -> List[Dict[str, Any]]:
    """Every already-persisted evidence record for a loop, each carrying its
    own ``evidence_relpath``. Sorted by filename, which sorts chronologically
    because the run_id format embeds a UTC timestamp.
    """
    loop_dir = root / RUNS_DIRNAME / loop_id
    if not loop_dir.exists():
        return []
    records: List[Dict[str, Any]] = []
    for path in sorted(loop_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and isinstance(data.get("ledger"), dict):
            record = dict(data)
            record["evidence_relpath"] = _relpath(path, root)
            records.append(record)
    return records


def check_existing_evidence(evidence_path: Path, new_ledger_raw: Dict[str, Any]) -> str:
    """Returns ``"absent"`` or ``"identical"``; raises on a byte-for-byte
    conflict. Run ledgers are write-once: a different ledger at an existing
    destination is always refused, never overwritten.
    """
    if not evidence_path.exists():
        return "absent"
    try:
        existing = json.loads(evidence_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PersistenceRefused(
            "EVIDENCE_UNREADABLE", "existing evidence file cannot be read: {}".format(exc)
        ) from exc
    existing_ledger = existing.get("ledger") if isinstance(existing, dict) else None
    if existing_ledger == new_ledger_raw:
        return "identical"
    raise PersistenceRefused(
        "EVIDENCE_CONFLICT",
        "evidence already exists at {} with different content; run ledgers are immutable and are "
        "never overwritten".format(evidence_path),
    )


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=".tmp-persist-", suffix=".json", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, str(path))
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def _canonical_bytes(data: Dict[str, Any]) -> bytes:
    return (json.dumps(data, indent=2, sort_keys=True) + "\n").encode("utf-8")


def derive_state(
    loop_id: str,
    evidence_records: List[Dict[str, Any]],
    existing_state: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    """Pure function: state must always be reconstructible from the set of
    persisted ledgers plus registry defaults. Everything here is recomputed
    from ``evidence_records`` alone, except ``human_approval`` and ``notes``,
    which are operator-set facts that no ledger can ever imply and so are
    carried forward from ``existing_state`` untouched.
    """
    human_approval: Dict[str, Any] = {
        "granted": False,
        "granted_by": None,
        "granted_at": None,
        "scope": None,
    }
    notes = None
    if isinstance(existing_state, dict):
        if isinstance(existing_state.get("human_approval"), dict):
            human_approval = existing_state["human_approval"]
        notes = existing_state.get("notes")

    if not evidence_records:
        return {
            "schema_version": "1.0",
            "loop_id": loop_id,
            "status": "REPORT_ONLY",
            "updated_at": _iso_now(),
            "consecutive_failures": 0,
            "last_progress_marker": None,
            "last_error_signature": None,
            "open_escalation": None,
            "human_approval": human_approval,
            "run_history": [],
            "notes": notes,
        }

    ordered = sorted(evidence_records, key=lambda r: r["ledger"]["run_id"])

    run_history = []
    for record in ordered:
        ledger_data = record["ledger"]
        run_history.append(
            {
                "run_id": ledger_data["run_id"],
                "finished_at": ledger_data["completed_at"],
                "outcome": ledger_data["outcome"],
                "ledger_ref": record["evidence_relpath"],
            }
        )

    latest_ledger = ordered[-1]["ledger"]
    status = latest_ledger["status_after"]
    if status in PHASE1_FORBIDDEN_STATUSES:
        # Defensive only: apply()/dry_run() already refuse this before a
        # record can ever reach persisted evidence.
        status = "REPORT_ONLY"

    consecutive_failures = 0
    for record in reversed(ordered):
        if record["ledger"]["outcome"] == "success":
            break
        consecutive_failures += 1

    last_progress_marker = None
    last_error_signature = None
    for record in reversed(ordered):
        for iteration in reversed(record["ledger"].get("iterations", [])):
            if last_progress_marker is None and iteration.get("progress_marker"):
                last_progress_marker = iteration["progress_marker"]
            if (
                last_error_signature is None
                and iteration.get("outcome") == "failure"
                and iteration.get("error_signature")
            ):
                last_error_signature = iteration["error_signature"]
        if last_progress_marker is not None and last_error_signature is not None:
            break

    return {
        "schema_version": "1.0",
        "loop_id": loop_id,
        "status": status,
        "updated_at": _iso_now(),
        "consecutive_failures": consecutive_failures,
        "last_progress_marker": last_progress_marker,
        "last_error_signature": last_error_signature,
        "open_escalation": None,
        "human_approval": human_approval,
        "run_history": run_history,
        "notes": notes,
    }


# --- the two entry points ---------------------------------------------------


def dry_run(
    ledger_path: Any,
    registry_path: Optional[Any] = None,
    root: Optional[Path] = None,
    registry: Optional[Registry] = None,
) -> PersistPlan:
    """Validate a candidate persist end to end and write nothing.

    Every check ``apply`` performs is performed here first, so a caller can
    trust that a clean dry run means ``apply`` will not fail for a reason this
    function could have already caught. (``apply`` still repeats every check
    immediately before writing -- see its docstring for why.)

    ``registry``, if given, is used directly instead of loading
    ``LOOP_REGISTRY.json`` from disk -- this is how tests exercise persistence
    against an isolated fixture registry rather than the real shipped one.
    """
    root = root or repo_root()
    registry = registry if registry is not None else load_registry(registry_path)
    raw = load_ledger_document(ledger_path)
    ledger = validate_ledger_for_persistence(raw)

    loop = registry.get(ledger.loop_id)
    if loop is None:
        raise PersistenceRefused(
            "UNKNOWN_LOOP", "loop id {!r} is not present in the registry".format(ledger.loop_id)
        )

    if ledger.status_after in PHASE1_FORBIDDEN_STATUSES:
        raise PersistenceRefused(
            "LIFECYCLE_PROMOTION_FORBIDDEN",
            "status_after {!r} is not permitted; persistence must never promote a loop beyond "
            "REPORT_ONLY in Phase 1".format(ledger.status_after),
        )

    if not guard_module.transition_allowed(ledger.status_before, ledger.status_after):
        raise PersistenceRefused(
            "INVALID_TRANSITION",
            "forbidden lifecycle transition {} -> {}".format(ledger.status_before, ledger.status_after),
        )

    if registry.phase == 1:
        if raw.get("repository_mutation_count") != 0:
            raise PersistenceRefused(
                "NONZERO_MUTATION_COUNT",
                "repository_mutation_count must be 0 for a Phase 1 REPORT_ONLY loop, got {!r}".format(
                    raw.get("repository_mutation_count")
                ),
            )
        if raw.get("remote_action_count") != 0:
            raise PersistenceRefused(
                "NONZERO_REMOTE_ACTION_COUNT",
                "remote_action_count must be 0 for a Phase 1 REPORT_ONLY loop, got {!r}".format(
                    raw.get("remote_action_count")
                ),
            )

    validate_timestamps(raw)

    ledger_text = json.dumps(raw, indent=2, sort_keys=True)
    redaction_findings = scan_text(ledger_text, "<ledger:{}:{}>".format(ledger.loop_id, ledger.run_id))
    if redaction_findings:
        raise PersistenceRefused(
            "REDACTION_FINDING",
            "{} secret-shaped finding(s) in the ledger; persistence refused: {}".format(
                len(redaction_findings), "; ".join(f.render() for f in redaction_findings)
            ),
        )

    guard_decision = guard_module.evaluate_or_block(ledger, registry, root=root)
    if guard_decision.decision == guard_module.BLOCK_INVALID_STATE:
        raise PersistenceRefused(
            "GUARD_BLOCKED",
            "the guard returned BLOCK_INVALID_STATE for this ledger: {}".format(
                "; ".join(guard_decision.reasons)
            ),
        )

    evidence_path = resolve_run_path(ledger.loop_id, ledger.run_id, root)
    state_path = resolve_state_path(ledger.loop_id, root)

    _check_no_symlink_ancestors(evidence_path.parent, root / RUNS_DIRNAME)
    if evidence_path.exists() and evidence_path.is_symlink():
        raise PersistenceRefused("SYMLINK_IN_PATH", "evidence destination is a symlink: {}".format(evidence_path))
    _check_case_collision(root / RUNS_DIRNAME, ledger.loop_id)
    if evidence_path.parent.exists():
        _check_case_collision(evidence_path.parent, evidence_path.name)

    _check_no_symlink_ancestors(state_path.parent, root / STATES_DIRNAME)
    if state_path.exists() and state_path.is_symlink():
        raise PersistenceRefused("SYMLINK_IN_PATH", "state destination is a symlink: {}".format(state_path))

    mismatch_notes = validate_repository_identity(raw, root)

    evidence_relpath = _relpath(evidence_path, root)
    state_relpath = _relpath(state_path, root)

    existing_records = [
        r for r in list_persisted_ledgers(ledger.loop_id, root) if r["ledger"].get("run_id") != ledger.run_id
    ]
    existing_state = _load_existing_state(state_path)
    simulated = {"ledger": raw, "evidence_relpath": evidence_relpath}
    proposed_state = derive_state(ledger.loop_id, existing_records + [simulated], existing_state)

    return PersistPlan(
        loop_id=ledger.loop_id,
        run_id=ledger.run_id,
        evidence_path=evidence_path,
        evidence_relpath=evidence_relpath,
        state_path=state_path,
        state_relpath=state_relpath,
        guard_decision=guard_decision,
        ledger_raw=raw,
        proposed_state=proposed_state,
        warnings=mismatch_notes,
        notes=["dry run: nothing written"],
    )


def apply(
    ledger_path: Any,
    operator_approval_id: Optional[str],
    expected_head: Optional[str],
    registry_path: Optional[Any] = None,
    root: Optional[Path] = None,
    registry: Optional[Registry] = None,
) -> Dict[str, Any]:
    """Validate everything :func:`dry_run` validates, then write.

    Requires both ``operator_approval_id`` and ``expected_head`` -- both fail
    closed (no file written) if missing or blank. ``expected_head`` must equal
    the repository's actual current HEAD at the moment of the call, so an
    approval cannot silently be replayed against a branch that has since
    moved.

    Write order is evidence, then state (never the reverse): if the state
    update fails after evidence was written, :class:`PartialPersistenceError`
    is raised. The evidence is real and is never deleted automatically; a
    retry with the identical ledger will find it (status ``identical``) and
    complete only the missing state.
    """
    if not operator_approval_id or not str(operator_approval_id).strip():
        raise PersistenceRefused(
            "MISSING_APPROVAL", "--operator-approval-id is required and must be non-empty to apply persistence"
        )
    if not expected_head or not str(expected_head).strip():
        raise PersistenceRefused("MISSING_EXPECTED_HEAD", "--expected-head is required to apply persistence")

    root = root or repo_root()
    actual_head = current_head(root)
    if str(expected_head).strip() != actual_head:
        raise PersistenceRefused(
            "HEAD_MISMATCH",
            "expected-head {!r} does not match the repository's actual current HEAD {!r}; refusing to "
            "persist against a branch that has moved since approval".format(expected_head, actual_head),
        )

    plan = dry_run(ledger_path, registry_path=registry_path, root=root, registry=registry)

    evidence_status = check_existing_evidence(plan.evidence_path, plan.ledger_raw)

    actual_branch = current_branch(root)
    record = {
        "schema_version": "1.0",
        "ledger": plan.ledger_raw,
        "persisted_at": _iso_now(),
        "persisted_by": {
            "operator_approval_id": operator_approval_id,
            "note": (
                "This id is audit metadata supplied by the CLI invoker at persist time. It is not "
                "cryptographic proof of operator identity."
            ),
        },
        "guard_evaluation": {
            "decision": plan.guard_decision.decision,
            "exit_code": plan.guard_decision.exit_code,
            "reasons": list(plan.guard_decision.reasons),
            "checks": dict(plan.guard_decision.checks),
        },
        "repository_identity_check": {
            "expected_head": expected_head,
            "actual_head_at_persist": actual_head,
            "actual_branch_at_persist": actual_branch,
            "ledger_declared_head_sha": plan.ledger_raw.get("head_sha"),
            "ledger_declared_branch": plan.ledger_raw.get("branch"),
            "mismatch_notes": plan.warnings,
        },
        "validation": {"schema_valid": True, "semantic_valid": True, "redaction_clean": True},
        "final_classification": "PERSISTED",
    }

    evidence_written = False
    if evidence_status == "absent":
        _atomic_write_bytes(plan.evidence_path, _canonical_bytes(record))
        evidence_written = True
    # "identical" -> recovery path; the existing file is left untouched.

    try:
        existing_records = list_persisted_ledgers(plan.loop_id, root)
        existing_state = _load_existing_state(plan.state_path)
        new_state = derive_state(plan.loop_id, existing_records, existing_state)
        _atomic_write_bytes(plan.state_path, _canonical_bytes(new_state))
    except Exception as exc:
        raise PartialPersistenceError(
            "evidence for run {!r} was persisted at {} but the derived-state update failed: {}. The "
            "evidence file is real and must not be deleted. Retry persist-run --apply with the "
            "identical ledger to complete the missing state.".format(plan.run_id, plan.evidence_relpath, exc)
        ) from exc

    return {
        "loop_id": plan.loop_id,
        "run_id": plan.run_id,
        "evidence_path": plan.evidence_relpath,
        "evidence_written": evidence_written,
        "evidence_status": evidence_status,
        "state_path": plan.state_relpath,
        "state": new_state,
        "guard_decision": plan.guard_decision.decision,
        "guard_exit_code": plan.guard_decision.exit_code,
    }
