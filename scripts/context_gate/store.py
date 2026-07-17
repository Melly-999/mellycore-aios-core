"""Guarded write path for Context Gate implementation Phase I2.

Reuses the loop-evidence persistence conventions proven by
``scripts/loop_ops/persist.py`` verbatim rather than inventing a second
immutability model (gate spec Section 2, implementation spec throughout):
dry-run/preview is the only default, apply requires a non-empty operator
approval id and an expected-HEAD match against the repository's actual
current HEAD, every write is write-once (identical bytes are idempotent
recovery, differing bytes are always refused), and every destination path is
checked for symlink and case-collision attacks before anything is written.

This module adds one requirement `persist.py` does not have: a **clean
working tree** is required before ``apply`` may write anything (implementation
spec Section 5.3, this task's explicit "clean-tree ... guard" requirement).

Three write operations exist, all gated by :func:`require_apply_gating`:

1. :func:`migrate_preview_records` -- the one-time, hash-verified relocation
   of the six admitted preview records into the canonical store (Section 3
   of the implementation spec). A tampered or non-conforming record aborts
   the whole migration loudly, before anything is written.
2. :func:`apply_batch` -- writes new, already-decided ``ContextSource``
   records from a batch manifest (Section 5.3). Individual item refusal is
   aggregate-safe (Section 4) and does not abort the rest of the batch.
3. :func:`apply` -- the single orchestration entry point the CLI calls,
   checking gating exactly once and then running migration and/or batch
   application as requested.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from . import checks as checks_module
from .models import (
    GATE_SPEC_VERSION,
    RECORD_FIELDS,
    REQUIRED_DECISION_FIELDS,
    SOURCE_ID_RE,
    ContextGateError,
    InvalidInputError,
    deterministic_json_bytes,
    is_nonempty_string,
)

CANONICAL_DIRNAME = "shared_context/context_provenance"
RECORDS_DIRNAME = CANONICAL_DIRNAME + "/records"
REFUSALS_DIRNAME = CANONICAL_DIRNAME + "/refusals"
REFUSAL_LOG_RELPATH = REFUSALS_DIRNAME + "/REFUSAL_LOG.jsonl"
MIGRATION_REPORT_RELPATH = CANONICAL_DIRNAME + "/MIGRATION_001.md"
CANONICAL_README_RELPATH = CANONICAL_DIRNAME + "/README.md"
PREVIEW_DIRNAME = "shared_context/context_provenance_preview"
PREVIEW_README_RELPATH = PREVIEW_DIRNAME + "/README.md"

EXPECTED_PREVIEW_SOURCE_IDS = frozenset(
    {
        "ctx-2026-07-17-dashboard-preview-committed",
        "ctx-2026-07-17-gate-spec-exists",
        "ctx-2026-07-17-milestone-a-closed",
        "ctx-2026-07-17-project-health-two-runs",
        "ctx-2026-07-17-provenance-spec-exists",
        "ctx-2026-07-17-safety-posture-summary",
    }
)

#: The dry run's one historical refusal, backfilled as the refusal log's
#: first line during migration (implementation spec Section 4). Sourced from
#: ``docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001.md``'s "C7
#: refusal detail" section -- never re-derived, never guessed.
C7_BACKFILL = {
    "refused_at": "2026-07-17",
    "reason_code": "trust_cap_violation",
    "proposed_by": "MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001",
    "batch_id": "MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001",
    "gate_spec_version": GATE_SPEC_VERSION,
}


class StoreError(ContextGateError):
    """Base class for a refused or aborted write attempt."""


class ApplyRefused(StoreError):
    """A write was refused before anything was written. ``code`` is stable
    and machine-readable, matching the ``PersistenceRefused`` pattern."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


class MigrationAborted(StoreError):
    """Migration failed a defense-in-depth check and wrote nothing new.

    Unlike a single batch item's refusal (aggregate-safe, non-fatal to the
    rest of the batch), a migration failure means an already-decided,
    previously-reviewed record no longer matches what it once did or no
    longer passes the gate's hard rules -- an integrity problem, not an
    ordinary refusal path. It must fail loudly (implementation spec Section
    3 item 5).
    """

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


# --- git identity and clean-tree check (subprocess only; no dependency) ----


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


def current_head(root: Path) -> str:
    return _run_git(["rev-parse", "HEAD"], root)


def is_clean_working_tree(root: Path) -> bool:
    return _run_git(["status", "--porcelain"], root) == ""


# --- path safety (mirrors scripts/loop_ops/persist.py exactly) -------------


def _check_no_symlink_ancestors(path: Path, stop_at: Path) -> None:
    current = path
    while True:
        if current.exists() and current.is_symlink():
            raise ApplyRefused("SYMLINK_IN_PATH", "path component is a symlink: {}".format(current))
        if current == current.parent or current == stop_at:
            break
        current = current.parent


def _check_case_collision(parent: Path, name: str) -> None:
    if not parent.exists():
        return
    folded = name.casefold()
    for entry in parent.iterdir():
        if entry.name != name and entry.name.casefold() == folded:
            raise ApplyRefused(
                "CASE_COLLISION",
                "an entry differing only in case already exists at {}: {!r} vs {!r}".format(
                    parent, entry.name, name
                ),
            )


def _relpath(path: Path, root: Path) -> str:
    return str(path.relative_to(root)).replace("\\", "/")


def resolve_record_path(source_id: str, root: Path) -> Path:
    if not is_nonempty_string(source_id) or not SOURCE_ID_RE.fullmatch(source_id):
        raise ApplyRefused("INVALID_SOURCE_ID", "source_id {!r} does not match the required format".format(source_id))
    records_root = root / RECORDS_DIRNAME
    target = records_root / (source_id + ".json")
    try:
        target.resolve().relative_to(records_root.resolve())
    except ValueError:
        raise ApplyRefused("PATH_ESCAPE", "resolved record path {} escapes the canonical records directory".format(target))
    return target


def _atomic_write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=".tmp-context-gate-", suffix=".json", dir=str(path.parent))
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


def check_existing_record(path: Path, new_bytes: bytes) -> str:
    """Returns ``"absent"`` or ``"identical"``; raises on a byte-for-byte
    conflict. Canonical records are write-once, exactly like run evidence."""

    if not path.exists():
        return "absent"
    try:
        existing = path.read_bytes()
    except OSError as exc:
        raise ApplyRefused("RECORD_UNREADABLE", "existing record file cannot be read: {}".format(exc)) from exc
    if existing == new_bytes:
        return "identical"
    raise ApplyRefused(
        "RECORD_CONFLICT",
        "a record already exists at {} with different content; canonical records are write-once and "
        "are never overwritten".format(path),
    )


# --- apply gating (approval id, expected-HEAD, clean working tree) ---------


def require_apply_gating(root: Path, operator_approval_id: Optional[str], expected_head: Optional[str]) -> None:
    if not operator_approval_id or not str(operator_approval_id).strip():
        raise ApplyRefused(
            "MISSING_APPROVAL", "--operator-approval-id is required and must be non-empty to apply"
        )
    if not expected_head or not str(expected_head).strip():
        raise ApplyRefused("MISSING_EXPECTED_HEAD", "--expected-head is required to apply")

    actual_head = current_head(root)
    if str(expected_head).strip() != actual_head:
        raise ApplyRefused(
            "HEAD_MISMATCH",
            "expected-head {!r} does not match the repository's actual current HEAD {!r}; refusing to "
            "apply against a branch that has moved since approval".format(expected_head, actual_head),
        )

    if not is_clean_working_tree(root):
        raise ApplyRefused(
            "DIRTY_WORKING_TREE",
            "the working tree is not clean (git status --porcelain is non-empty); refusing to apply "
            "against uncommitted changes",
        )


# --- refusal log: structurally whitelisted, append-only, aggregate-safe ----


@dataclass(frozen=True)
class RefusalLogEntry:
    """Exactly the five fields the implementation spec's Section 4 whitelists.

    No content field, no claim, no ``source_identity`` can be attached to
    this object -- passing one raises ``TypeError`` at construction, before
    any I/O happens, which is what makes aggregate-safety a property of the
    type system rather than something a reviewer has to catch.
    """

    refused_at: str
    reason_code: str
    proposed_by: str
    batch_id: str
    gate_spec_version: str

    def to_dict(self) -> Dict[str, str]:
        return {
            "refused_at": self.refused_at,
            "reason_code": self.reason_code,
            "proposed_by": self.proposed_by,
            "batch_id": self.batch_id,
            "gate_spec_version": self.gate_spec_version,
        }

    def to_json_line(self) -> str:
        return json.dumps(self.to_dict(), sort_keys=True, ensure_ascii=False)


def append_refusal_log(entry: RefusalLogEntry, root: Path) -> None:
    if not isinstance(entry, RefusalLogEntry):
        raise TypeError("append_refusal_log requires a RefusalLogEntry")
    path = root / REFUSAL_LOG_RELPATH
    path.parent.mkdir(parents=True, exist_ok=True)
    _check_no_symlink_ancestors(path.parent, root)
    if path.exists() and path.is_symlink():
        raise ApplyRefused("SYMLINK_IN_PATH", "refusal log destination is a symlink: {}".format(path))
    line = (entry.to_json_line() + "\n").encode("utf-8")
    with open(path, "ab") as handle:
        handle.write(line)
        handle.flush()
        os.fsync(handle.fileno())


def read_refusal_log(root: Path) -> Tuple[Dict[str, str], ...]:
    path = root / REFUSAL_LOG_RELPATH
    if not path.exists():
        return ()
    lines = path.read_text(encoding="utf-8").splitlines()
    return tuple(json.loads(line) for line in lines if line.strip())


# --- canonical record construction ------------------------------------------


def _build_canonical_record(
    item: Mapping[str, Any], *, validation_outcome: str, warnings: Sequence[str], as_of: date, mode: str
) -> Dict[str, Any]:
    record: Dict[str, Any] = {field_name: item.get(field_name) for field_name in RECORD_FIELDS}
    record["gate_audit"] = {
        "gate_spec_version": GATE_SPEC_VERSION,
        "validation_outcome": validation_outcome,
        "warnings": list(warnings),
        "validated_at": as_of.isoformat(),
        "mode": mode,
    }
    record["envelope"] = {"store": "canonical", "migrated_from": None, "migrated_at": None}
    return record


def _has_human_decision(item: Mapping[str, Any]) -> bool:
    from .models import DECISIONS

    if item.get("decision") not in DECISIONS:
        return False
    return all(is_nonempty_string(item.get(field_name)) for field_name in REQUIRED_DECISION_FIELDS)


# --- batch application (new decided records) --------------------------------


@dataclass(frozen=True)
class AppliedItem:
    item_index: int
    status: str  # "written" | "identical" | "skipped_no_decision" | "refused"
    source_id: Optional[str] = None
    reason_codes: Tuple[str, ...] = ()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "item_index": self.item_index,
            "status": self.status,
            "source_id": self.source_id,
            "reason_codes": list(self.reason_codes),
        }


@dataclass(frozen=True)
class ApplyBatchResult:
    batch_id: str
    items: Tuple[AppliedItem, ...]

    @property
    def writes_performed(self) -> int:
        return sum(1 for item in self.items if item.status == "written")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "batch_id": self.batch_id,
            "writes_performed": self.writes_performed,
            "items": [item.to_dict() for item in self.items],
        }


def apply_batch(manifest: Mapping[str, Any], *, root: Path) -> ApplyBatchResult:
    """Write new, already-decided records from a batch manifest.

    Assumes :func:`require_apply_gating` has already been called by the
    caller (:func:`apply`) -- this function performs no gating itself, only
    the per-item decision/refusal/write logic, so gating is checked exactly
    once per invocation regardless of how many operations are combined.
    """

    if not isinstance(manifest, Mapping):
        raise InvalidInputError("batch manifest must be a JSON object")
    batch_id = manifest.get("batch_id")
    items = manifest.get("items")
    if not is_nonempty_string(batch_id):
        raise InvalidInputError("batch manifest requires a non-empty batch_id")
    if not isinstance(items, list) or not items:
        raise InvalidInputError("batch manifest requires a non-empty items list")
    if not all(isinstance(item, Mapping) for item in items):
        raise InvalidInputError("every batch item must be a JSON object")

    today = date.today()
    existing: List[Mapping[str, Any]] = list(checks_module.load_records(root / RECORDS_DIRNAME))
    results: List[AppliedItem] = []

    for index, item in enumerate(items, start=1):
        source_id = str(item.get("source_id")) if item.get("source_id") else None

        if not _has_human_decision(item):
            results.append(AppliedItem(item_index=index, status="skipped_no_decision", source_id=source_id))
            continue

        # Exclude any existing record with this item's own source_id before
        # the R7 collision recheck -- mirrors persist.py excluding the
        # current run_id from existing_records before deriving state. A
        # write-once *resubmission* of the same id is a content-match
        # question (check_existing_record, below), never an R7 collision
        # against itself.
        existing_for_recheck = [r for r in existing if str(r.get("source_id")) != source_id]
        refusal = checks_module.recheck_record_for_write(item, root=root, existing=existing_for_recheck)
        if refusal:
            append_refusal_log(
                RefusalLogEntry(
                    refused_at=today.isoformat(),
                    reason_code=refusal,
                    proposed_by=str(item.get("proposed_by")),
                    batch_id=str(batch_id),
                    gate_spec_version=GATE_SPEC_VERSION,
                ),
                root,
            )
            results.append(
                AppliedItem(item_index=index, status="refused", source_id=source_id, reason_codes=(refusal,))
            )
            continue

        # Full ACCEPT/ACCEPT_WITH_WARNINGS classification (with warnings) is
        # a preview-time concern already surfaced to the human before this
        # item carried a decision; recheck_record_for_write only re-verifies
        # the hard R1-R9 rules at write time (defense in depth), so the audit
        # block records that recheck outcome, not a re-derived warning set.
        canonical = _build_canonical_record(
            item,
            validation_outcome="ACCEPT",
            warnings=(),
            as_of=today,
            mode="apply",
        )
        path = resolve_record_path(str(item.get("source_id")), root)
        _check_no_symlink_ancestors(path.parent, root)
        if path.exists() and path.is_symlink():
            raise ApplyRefused("SYMLINK_IN_PATH", "record destination is a symlink: {}".format(path))
        _check_case_collision(root / RECORDS_DIRNAME, path.name)

        canonical_bytes = deterministic_json_bytes(canonical)
        status = check_existing_record(path, canonical_bytes)
        if status == "absent":
            _atomic_write_bytes(path, canonical_bytes)

        existing = list(existing) + [canonical]
        results.append(AppliedItem(item_index=index, status="written" if status == "absent" else status, source_id=source_id))

    return ApplyBatchResult(batch_id=str(batch_id), items=tuple(results))


# --- migration of the six admitted preview records --------------------------


@dataclass
class MigrationRecordReport:
    source_id: str
    preview_sha256: str
    canonical_sha256: str
    fields_identical: bool


@dataclass
class MigrationResult:
    records: Tuple[MigrationRecordReport, ...] = field(default_factory=tuple)
    refusal_log_backfilled: bool = False

    @property
    def writes_performed(self) -> int:
        return len(self.records)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "records_migrated": len(self.records),
            "refusal_log_backfilled": self.refusal_log_backfilled,
            "records": [
                {
                    "source_id": r.source_id,
                    "preview_sha256": r.preview_sha256,
                    "canonical_sha256": r.canonical_sha256,
                    "fields_identical": r.fields_identical,
                }
                for r in self.records
            ],
        }


def _verify_field_identity(preview_data: Mapping[str, Any], canonical_data: Mapping[str, Any], source_id: str) -> None:
    """Parsed-field comparison, not trust: every ContextSource + gate_audit
    field must be byte-for-byte equal to the preview record. Only the
    envelope-era fields (``preview``, ``record_status`` removed; ``envelope``
    added) may differ."""

    for field_name in RECORD_FIELDS:
        if canonical_data.get(field_name) != preview_data.get(field_name):
            raise MigrationAborted(
                "MIGRATION_FIELD_MISMATCH",
                "{}: field {!r} changed during migration ({!r} -> {!r})".format(
                    source_id, field_name, preview_data.get(field_name), canonical_data.get(field_name)
                ),
            )
    if canonical_data.get("gate_audit") != preview_data.get("gate_audit"):
        raise MigrationAborted(
            "MIGRATION_FIELD_MISMATCH", "{}: gate_audit changed during migration".format(source_id)
        )


def _migration_report_markdown(records: Sequence[MigrationRecordReport], migrated_at: str) -> str:
    lines = [
        "# Migration 001 -- Preview to Canonical",
        "",
        "Migrated by `MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001`'s `apply --migrate-preview`,",
        "per `docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md` Section 3.",
        "",
        "Relocation, not re-decision: every `ContextSource` and `gate_audit` field below was",
        "verified byte-for-byte identical between the preview and canonical copy before either",
        "file was written. Only the envelope (`preview`/`record_status` removed, `envelope` added)",
        "changed.",
        "",
        "Migrated at: {}".format(migrated_at),
        "",
        "| source_id | preview SHA-256 | canonical SHA-256 | fields identical |",
        "|---|---|---|---|",
    ]
    for r in records:
        lines.append(
            "| `{}` | `{}` | `{}` | {} |".format(
                r.source_id, r.preview_sha256, r.canonical_sha256, "yes" if r.fields_identical else "NO"
            )
        )
    lines.append("")
    lines.append(
        "The refusal log's first line (`shared_context/context_provenance/refusals/REFUSAL_LOG.jsonl`) "
        "is the C7 historical backfill from "
        "`docs/tasks/MELLYCORE-CONTEXT-INGESTION-GATE-DRY-RUN-001.md`'s \"C7 refusal detail\" section, "
        "so the log is complete from the workflow's true beginning."
    )
    lines.append("")
    lines.append(
        "This migration is one-time and idempotent: re-running it once `MIGRATION_001.md` exists is "
        "refused (`ALREADY_MIGRATED`), not repeated."
    )
    lines.append("")
    return "\n".join(lines)


def _canonical_readme_markdown() -> str:
    return "\n".join(
        [
            "# Context Provenance -- Canonical Store",
            "",
            "This is the canonical `ContextSource` record store, created by",
            "`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001` per",
            "`docs/specs/MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001.md` Section 2.",
            "",
            "Rules:",
            "",
            "- `records/*.json` files are **write-once**: an identical-bytes rewrite is idempotent",
            "  recovery (a no-op); any differing write to an existing file is refused. The only",
            "  permitted mutation to a decided record is setting `superseded_by`, and even that is",
            "  done only via a future, separately approved `apply` call, never by hand.",
            "- `refusals/REFUSAL_LOG.jsonl` is append-only and aggregate-safe: reason code, date,",
            "  `proposed_by`, `batch_id`, `gate_spec_version` only -- never refused content or",
            "  identity. See the gate spec Section 4/7.",
            "- `MIGRATION_001.md` is the hash-verified manifest of the one-time relocation of the",
            "  project's first six admitted `ContextSource` records from",
            "  `shared_context/context_provenance_preview/`.",
            "- `INDEX.json` does not exist yet -- it is derived data reserved for implementation",
            "  Phase I3 (`rebuild-index`). Nothing in this store depends on it existing.",
            "- No secrets, credentials, `.env` values, account identifiers, or MellyTrade content",
            "  may ever appear in any file in this directory.",
            "",
        ]
    )


def _preview_tombstone_markdown() -> str:
    return "\n".join(
        [
            "# Context Provenance -- PREVIEW LOCATION (retired)",
            "",
            "**This directory is retired.** The six records formerly admitted here were migrated,",
            "byte-for-byte content unchanged, to the canonical store at",
            "`shared_context/context_provenance/records/` by",
            "`MELLYCORE-CONTEXT-GATE-IMPLEMENTATION-I2-001`'s `apply --migrate-preview`. See",
            "`shared_context/context_provenance/MIGRATION_001.md` for the hash-verified migration",
            "manifest, and this commit's history for the original preview-era files.",
            "",
            "Do not place new draft records here. The gate's Phase I1 `preview` command and any",
            "future draft workflow should target the canonical store's own draft/staging convention",
            "once one exists; this location is history only.",
            "",
        ]
    )


def migrate_preview_records(root: Path) -> MigrationResult:
    migration_report_path = root / MIGRATION_REPORT_RELPATH
    if migration_report_path.exists():
        raise ApplyRefused(
            "ALREADY_MIGRATED",
            "migration already completed: {} exists; migration is one-time and is not repeated".format(
                MIGRATION_REPORT_RELPATH
            ),
        )

    preview_dir = root / PREVIEW_DIRNAME
    preview_paths = sorted(preview_dir.glob("ctx-*.json"))
    if not preview_paths:
        raise ApplyRefused("NO_PREVIEW_RECORDS", "no preview records found under {}".format(PREVIEW_DIRNAME))
    discovered_names = {path.stem for path in preview_paths}
    if discovered_names != EXPECTED_PREVIEW_SOURCE_IDS:
        raise MigrationAborted(
            "MIGRATION_RECORD_SET_MISMATCH",
            "preview migration requires exactly the six admitted records; missing={!r}, unexpected={!r}".format(
                sorted(EXPECTED_PREVIEW_SOURCE_IDS - discovered_names),
                sorted(discovered_names - EXPECTED_PREVIEW_SOURCE_IDS),
            ),
        )

    preview_readme = preview_dir / "README.md"
    if not preview_readme.is_file() or preview_readme.is_symlink():
        raise MigrationAborted(
            "MIGRATION_PREVIEW_LAYOUT_INVALID",
            "the preview store must contain a regular README.md before it can be tombstoned",
        )
    original_preview_readme = preview_readme.read_bytes()

    for relpath in (REFUSAL_LOG_RELPATH, CANONICAL_README_RELPATH):
        if (root / relpath).exists():
            raise MigrationAborted(
                "MIGRATION_PARTIAL_STATE",
                "{} already exists before MIGRATION_001.md; refusing to overwrite partial canonical state".format(
                    relpath
                ),
            )

    today = date.today()
    prepared: List[Tuple[Path, bytes, MigrationRecordReport, Path, bytes]] = []

    for preview_path in preview_paths:
        raw = preview_path.read_bytes()
        try:
            preview_data = json.loads(raw.decode("utf-8"))
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise MigrationAborted(
                "MIGRATION_UNREADABLE", "{} is not readable UTF-8 JSON: {}".format(preview_path.name, exc)
            ) from exc
        if not isinstance(preview_data, Mapping):
            raise MigrationAborted("MIGRATION_UNREADABLE", "{} is not a JSON object".format(preview_path.name))

        source_id = str(preview_data.get("source_id"))
        if preview_path.name != source_id + ".json":
            raise MigrationAborted(
                "MIGRATION_FILENAME_MISMATCH",
                "{} does not match its source_id {!r}".format(preview_path.name, source_id),
            )
        if (
            preview_data.get("decision") != "admitted"
            or preview_data.get("preview") is not True
            or preview_data.get("record_status")
            != "ADMITTED_IN_PREVIEW_LOCATION_PENDING_CANONICAL_MIGRATION"
            or not _has_human_decision(preview_data)
        ):
            raise MigrationAborted(
                "MIGRATION_NOT_ADMITTED",
                "{} is not one of the fully decided, admitted preview records; refusing migration".format(source_id),
            )
        if not isinstance(preview_data.get("gate_audit"), Mapping):
            raise MigrationAborted(
                "MIGRATION_AUDIT_MISSING", "{} has no valid gate_audit block".format(source_id)
            )

        refusal = checks_module.recheck_record_for_write(preview_data, root=root, existing=())
        if refusal:
            raise MigrationAborted(
                "MIGRATION_RECHECK_FAILED",
                "{} fails a gate hard rule on re-check ({}); a previously admitted record must never "
                "violate R1-R9 today".format(source_id, refusal),
            )

        canonical_data: Dict[str, Any] = {field_name: preview_data.get(field_name) for field_name in RECORD_FIELDS}
        canonical_data["gate_audit"] = preview_data.get("gate_audit")
        canonical_data["envelope"] = {
            "store": "canonical",
            "migrated_from": _relpath(preview_path, root),
            "migrated_at": today.isoformat(),
        }
        canonical_bytes = deterministic_json_bytes(canonical_data)

        # Verify against the actual bytes about to be written, not against
        # the in-memory dict used to build them: round-trip canonical_bytes
        # back through json.loads and compare *that* to the original preview
        # data. This catches a real bug in construction/serialization, not
        # just a dict compared to itself.
        written_back = json.loads(canonical_bytes.decode("utf-8"))
        _verify_field_identity(preview_data, written_back, source_id)
        final_path = resolve_record_path(source_id, root)
        _check_no_symlink_ancestors(final_path.parent, root)
        _check_case_collision(root / RECORDS_DIRNAME, final_path.name)
        if final_path.exists():
            raise MigrationAborted(
                "MIGRATION_PARTIAL_STATE",
                "{} already exists before MIGRATION_001.md; refusing to overwrite a canonical record".format(
                    _relpath(final_path, root)
                ),
            )

        report = MigrationRecordReport(
            source_id=source_id,
            preview_sha256=hashlib.sha256(raw).hexdigest(),
            canonical_sha256=hashlib.sha256(canonical_bytes).hexdigest(),
            fields_identical=True,
        )
        prepared.append((final_path, canonical_bytes, report, preview_path, raw))

    reports = tuple(report for _f, _c, report, _p, _r in prepared)
    migration_text = _migration_report_markdown(reports, today.isoformat()).encode("utf-8")
    refusal_line = (RefusalLogEntry(**C7_BACKFILL).to_json_line() + "\n").encode("utf-8")
    outputs: List[Tuple[Path, bytes]] = [
        (final_path, canonical_bytes) for final_path, canonical_bytes, _report, _preview_path, _raw in prepared
    ]
    outputs.extend(
        [
            (root / REFUSAL_LOG_RELPATH, refusal_line),
            (root / MIGRATION_REPORT_RELPATH, migration_text),
            (root / CANONICAL_README_RELPATH, _canonical_readme_markdown().encode("utf-8")),
            (preview_readme, _preview_tombstone_markdown().encode("utf-8")),
        ]
    )

    # Stage every output before publishing any of it. If any replace or
    # preview retirement fails, restore the original preview bytes and
    # remove only outputs created by this attempt.
    staged_outputs: List[Tuple[Path, Path]] = []
    published: List[Path] = []
    try:
        for final_path, data in outputs:
            final_path.parent.mkdir(parents=True, exist_ok=True)
            _check_no_symlink_ancestors(final_path.parent, root)
            fd, tmp_name = tempfile.mkstemp(prefix=".tmp-context-migration-", dir=str(final_path.parent))
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            staged_outputs.append((Path(tmp_name), final_path))
        for tmp_path, final_path in staged_outputs:
            os.replace(str(tmp_path), str(final_path))
            published.append(final_path)
        for _final_path, _canonical_bytes, _report, preview_path, _raw in prepared:
            preview_path.unlink()
    except Exception:
        for tmp_path, _final_path in staged_outputs:
            try:
                tmp_path.unlink()
            except OSError:
                pass
        for _final_path, _canonical_bytes, _report, preview_path, raw in prepared:
            if not preview_path.exists():
                try:
                    preview_path.write_bytes(raw)
                except OSError:
                    pass
        try:
            preview_readme.write_bytes(original_preview_readme)
        except OSError:
            pass
        for final_path in published:
            if final_path != preview_readme and final_path.exists():
                try:
                    final_path.unlink()
                except OSError:
                    pass
        raise

    return MigrationResult(records=reports, refusal_log_backfilled=True)


# --- single orchestration entry point ---------------------------------------


def apply(
    *,
    root: Path,
    operator_approval_id: Optional[str],
    expected_head: Optional[str],
    batch_manifest: Optional[Mapping[str, Any]] = None,
    migrate_preview: bool = False,
) -> Dict[str, Any]:
    """The one entry point the CLI calls. Checks gating exactly once, then
    runs migration and/or batch application as requested. Migration always
    runs first, so a combined invocation's batch items see the just-migrated
    canonical records as already-existing for R7/staleness purposes."""

    require_apply_gating(root, operator_approval_id, expected_head)

    if batch_manifest is None and not migrate_preview:
        raise InvalidInputError("apply requires --batch and/or --migrate-preview")

    result: Dict[str, Any] = {"command": "apply", "writes_performed": 0}

    if migrate_preview:
        migration = migrate_preview_records(root)
        result["migration"] = migration.to_dict()
        result["writes_performed"] += migration.writes_performed

    if batch_manifest is not None:
        batch = apply_batch(batch_manifest, root=root)
        result["batch"] = batch.to_dict()
        result["writes_performed"] += batch.writes_performed

    return result
