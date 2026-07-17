"""Deterministic, content-free ContextSource index for Phase I3.

``INDEX.json`` is derived data. This module validates every canonical record
before constructing the index and is the only I3 code that writes anything.
It may create or replace exactly ``shared_context/context_provenance/INDEX.json``;
canonical records and the refusal log are always read-only inputs.
"""

from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from .models import InvalidInputError, deterministic_json_bytes, validate_record_shape
from .store import CANONICAL_DIRNAME, RECORDS_DIRNAME

INDEX_VERSION = "MELLYCORE_CONTEXT_PROVENANCE_INDEX_001"
INDEX_RELPATH = CANONICAL_DIRNAME + "/INDEX.json"

INDEX_ENTRY_FIELDS = (
    "source_id",
    "source_type",
    "sensitivity_level",
    "allowed_use",
    "trust_level",
    "staleness_policy",
    "review_after",
    "decision",
    "superseded_by",
)


@dataclass(frozen=True)
class RecordIssue:
    """Aggregate-safe canonical-record consistency finding.

    The finding carries only a stable code, the canonical filename, and an
    optional field name. It never includes a record value, claim, note,
    source identity, or path outside the canonical store.
    """

    code: str
    file: str
    field: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"code": self.code, "file": self.file, "field": self.field}


@dataclass(frozen=True)
class LoadedRecord:
    file_name: str
    raw_bytes: bytes
    data: Optional[Mapping[str, Any]]
    issues: Tuple[RecordIssue, ...]

    @property
    def valid(self) -> bool:
        return self.data is not None and not self.issues


@dataclass(frozen=True)
class RebuildResult:
    status: str
    record_count: int

    @property
    def writes_performed(self) -> int:
        return 1 if self.status == "written" else 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "command": "rebuild-index",
            "index": INDEX_RELPATH,
            "record_count": self.record_count,
            "status": self.status,
            "writes_performed": self.writes_performed,
        }


def _read_record(path: Path) -> LoadedRecord:
    if path.is_symlink():
        return LoadedRecord(path.name, b"", None, (RecordIssue("symlink_record", path.name),))
    try:
        raw = path.read_bytes()
    except OSError:
        return LoadedRecord(path.name, b"", None, (RecordIssue("unreadable_record", path.name),))
    try:
        data = json.loads(raw.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError):
        return LoadedRecord(path.name, raw, None, (RecordIssue("invalid_record_json", path.name),))
    if not isinstance(data, Mapping):
        return LoadedRecord(path.name, raw, None, (RecordIssue("record_not_object", path.name),))

    issues: List[RecordIssue] = [
        RecordIssue(finding.code, path.name, finding.field)
        for finding in validate_record_shape(data, raw_bytes=raw)
    ]
    source_id = data.get("source_id")
    if isinstance(source_id, str) and path.name != source_id + ".json":
        issues.append(RecordIssue("filename_source_id_mismatch", path.name, "source_id"))
    return LoadedRecord(path.name, raw, data, tuple(issues))


def load_canonical_records(root: Path) -> Tuple[LoadedRecord, ...]:
    records_dir = root / RECORDS_DIRNAME
    if not records_dir.exists() or not records_dir.is_dir():
        raise InvalidInputError("canonical records directory is missing or invalid")
    if records_dir.is_symlink():
        raise InvalidInputError("canonical records directory must not be a symlink")

    records = tuple(
        _read_record(path)
        for path in sorted(records_dir.glob("*.json"), key=lambda item: item.name.casefold())
    )
    return records


def validation_issues(records: Sequence[LoadedRecord]) -> Tuple[RecordIssue, ...]:
    issues: List[RecordIssue] = [issue for record in records for issue in record.issues]
    by_source_id: Dict[str, List[str]] = {}
    for record in records:
        if record.data is None:
            continue
        source_id = record.data.get("source_id")
        if isinstance(source_id, str):
            by_source_id.setdefault(source_id, []).append(record.file_name)
    for files in by_source_id.values():
        if len(files) > 1:
            issues.extend(RecordIssue("duplicate_source_id", file_name, "source_id") for file_name in files)
    return tuple(sorted(issues, key=lambda item: (item.code, item.file, item.field or "")))


def _entry(record: LoadedRecord) -> Dict[str, Any]:
    if record.data is None:
        raise InvalidInputError("cannot index an invalid canonical record")
    gate_audit = record.data.get("gate_audit")
    validation_outcome = gate_audit.get("validation_outcome") if isinstance(gate_audit, Mapping) else None
    entry = {field: record.data.get(field) for field in INDEX_ENTRY_FIELDS}
    entry["validation_outcome"] = validation_outcome
    entry["file"] = record.file_name
    return entry


def build_index_payload(records: Sequence[LoadedRecord]) -> Dict[str, Any]:
    issues = validation_issues(records)
    if issues:
        codes = sorted({issue.code for issue in issues})
        raise InvalidInputError(
            "canonical record validation failed with {} finding(s): {}".format(
                len(issues), ",".join(codes)
            )
        )
    entries = sorted((_entry(record) for record in records), key=lambda item: item["source_id"])
    return {
        "index_version": INDEX_VERSION,
        "record_count": len(entries),
        "records": entries,
    }


def expected_index_bytes(root: Path) -> bytes:
    return deterministic_json_bytes(build_index_payload(load_canonical_records(root)))


def _check_index_path(target: Path, root: Path) -> None:
    canonical_root = (root / CANONICAL_DIRNAME).resolve()
    try:
        target.resolve().relative_to(canonical_root)
    except ValueError as exc:
        raise InvalidInputError("derived index path escapes the canonical provenance store") from exc

    current = target
    while True:
        if current.exists() and current.is_symlink():
            raise InvalidInputError("derived index path contains a symlink")
        if current == root or current == current.parent:
            break
        current = current.parent


def rebuild_index(root: Path) -> RebuildResult:
    """Validate canonical records and atomically replace only ``INDEX.json``."""

    data = expected_index_bytes(root)
    target = root / INDEX_RELPATH
    _check_index_path(target, root)
    target.parent.mkdir(parents=True, exist_ok=True)

    if target.exists():
        try:
            if target.read_bytes() == data:
                payload = json.loads(data.decode("utf-8"))
                return RebuildResult("identical", int(payload["record_count"]))
        except OSError as exc:
            raise InvalidInputError("existing derived index is unreadable") from exc

    fd, tmp_name = tempfile.mkstemp(prefix=".tmp-context-index-", suffix=".json", dir=str(target.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_name, str(target))
    except Exception:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise

    payload = json.loads(data.decode("utf-8"))
    return RebuildResult("written", int(payload["record_count"]))
