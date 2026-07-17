"""Read-only computed audit for the canonical ContextSource store.

The audit reads canonical records, the derived index, and the aggregate-safe
refusal log. It never opens a file for writing and never emits claims, notes,
source identities, private paths, or refused content.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .index import (
    INDEX_RELPATH,
    LoadedRecord,
    build_index_payload,
    load_canonical_records,
    validation_issues,
)
from .models import (
    DECISIONS,
    SENSITIVITY_LEVELS,
    SOURCE_TYPES,
    TRUST_LEVELS,
    VALIDATION_OUTCOMES,
    deterministic_json_bytes,
    is_nonempty_string,
    parse_date,
)
from .store import REFUSAL_LOG_RELPATH

AUDIT_VERSION = "MELLYCORE_CONTEXT_PROVENANCE_AUDIT_001"
EXPIRING_WINDOW_DAYS = 30
REFUSAL_FIELDS = {
    "refused_at",
    "reason_code",
    "proposed_by",
    "batch_id",
    "gate_spec_version",
}
REASON_CODE_RE = re.compile(r"^[a-z][a-z0-9_]{0,63}$")
FRESHNESS_LABELS = ("immutable", "fresh", "expiring", "stale", "superseded")


@dataclass(frozen=True)
class AuditFinding:
    code: str
    file: Optional[str] = None
    field: Optional[str] = None
    source_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code,
            "file": self.file,
            "field": self.field,
            "source_id": self.source_id,
        }


def _enum_counts(records: Sequence[LoadedRecord], field: str, labels: Iterable[str]) -> Dict[str, int]:
    counts = Counter(
        str(record.data.get(field))
        for record in records
        if record.data is not None and record.data.get(field) is not None
    )
    return {label: counts.get(label, 0) for label in labels}


def _validation_outcome_counts(records: Sequence[LoadedRecord]) -> Dict[str, int]:
    counts: Counter = Counter()
    for record in records:
        if record.data is None:
            continue
        gate_audit = record.data.get("gate_audit")
        if isinstance(gate_audit, Mapping):
            outcome = gate_audit.get("validation_outcome")
            if isinstance(outcome, str):
                counts[outcome] += 1
    return {label: counts.get(label, 0) for label in VALIDATION_OUTCOMES}


def _latest_gate_audit(records: Sequence[LoadedRecord]) -> Optional[Dict[str, str]]:
    candidates: List[Tuple[str, str]] = []
    for record in records:
        if record.data is None:
            continue
        gate_audit = record.data.get("gate_audit")
        if not isinstance(gate_audit, Mapping):
            continue
        validated_at = gate_audit.get("validated_at")
        mode = gate_audit.get("mode")
        if isinstance(validated_at, str) and isinstance(mode, str):
            candidates.append((validated_at, mode))
    if not candidates:
        return None
    validated_at = max(item[0] for item in candidates)
    modes = sorted({mode for candidate_date, mode in candidates if candidate_date == validated_at})
    return {"mode": modes[0] if len(modes) == 1 else "mixed", "validated_at": validated_at}


def _supersession_state(
    records: Sequence[LoadedRecord],
) -> Tuple[Dict[str, Mapping[str, Any]], Tuple[AuditFinding, ...], Tuple[Tuple[str, ...], ...]]:
    by_id: Dict[str, Mapping[str, Any]] = {}
    for record in records:
        if record.data is None:
            continue
        source_id = record.data.get("source_id")
        if isinstance(source_id, str):
            by_id[source_id] = record.data

    findings: List[AuditFinding] = []
    edges: Dict[str, str] = {}
    for source_id, record in by_id.items():
        target = record.get("superseded_by")
        if not isinstance(target, str):
            continue
        edges[source_id] = target
        if target not in by_id:
            findings.append(AuditFinding("orphaned_superseded_by", source_id=source_id))

    chains: List[Tuple[str, ...]] = []
    consumed = set()
    targets = set(edges.values())
    starts = sorted(source_id for source_id in edges if source_id not in targets)
    starts.extend(sorted(source_id for source_id in edges if source_id not in starts))
    for start in starts:
        if start in consumed:
            continue
        chain = [start]
        seen = {start}
        current = start
        while current in edges and edges[current] in by_id:
            target = edges[current]
            chain.append(target)
            consumed.add(current)
            if target in seen:
                findings.append(AuditFinding("supersession_cycle", source_id=start))
                break
            seen.add(target)
            current = target
        if len(chain) > 1:
            chains.append(tuple(chain))

    findings.sort(key=lambda item: (item.code, item.source_id or ""))
    chains.sort()
    return by_id, tuple(findings), tuple(chains)


def _freshness_counts(
    records: Sequence[LoadedRecord], by_id: Mapping[str, Mapping[str, Any]], as_of: date
) -> Dict[str, int]:
    counts = Counter()
    expiring_through = as_of + timedelta(days=EXPIRING_WINDOW_DAYS)
    for record in records:
        if record.data is None:
            continue
        data = record.data
        target = data.get("superseded_by")
        if isinstance(target, str) and target in by_id:
            counts["superseded"] += 1
            continue
        if data.get("staleness_policy") == "immutable_historical":
            counts["immutable"] += 1
            continue
        review_after = parse_date(data.get("review_after"))
        if review_after is None:
            continue
        if review_after < as_of:
            counts["stale"] += 1
        elif review_after <= expiring_through:
            counts["expiring"] += 1
        else:
            counts["fresh"] += 1
    return {label: counts.get(label, 0) for label in FRESHNESS_LABELS}


def _refusal_counts(root: Path) -> Tuple[Dict[str, int], Tuple[AuditFinding, ...], int]:
    path = root / REFUSAL_LOG_RELPATH
    if not path.exists():
        return {}, (AuditFinding("refusal_log_missing", file=path.name),), 0
    if path.is_symlink() or not path.is_file():
        return {}, (AuditFinding("invalid_refusal_log", file=path.name),), 0
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        return {}, (AuditFinding("invalid_refusal_log", file=path.name),), 0

    counts: Counter = Counter()
    findings: List[AuditFinding] = []
    valid_lines = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            findings.append(AuditFinding("invalid_refusal_log_entry", file=path.name))
            continue
        if not isinstance(entry, Mapping) or set(entry) != REFUSAL_FIELDS:
            findings.append(AuditFinding("invalid_refusal_log_entry", file=path.name))
            continue
        reason_code = entry.get("reason_code")
        valid = (
            isinstance(reason_code, str)
            and REASON_CODE_RE.fullmatch(reason_code) is not None
            and parse_date(entry.get("refused_at")) is not None
            and all(is_nonempty_string(entry.get(field)) for field in REFUSAL_FIELDS - {"reason_code", "refused_at"})
        )
        if not valid:
            findings.append(AuditFinding("invalid_refusal_log_entry", file=path.name))
            continue
        counts[reason_code] += 1
        valid_lines += 1
    findings.sort(key=lambda item: item.code)
    return dict(sorted(counts.items())), tuple(findings), valid_lines


def _index_state(
    root: Path, records: Sequence[LoadedRecord], record_findings: Sequence[AuditFinding]
) -> Tuple[str, Tuple[AuditFinding, ...]]:
    path = root / INDEX_RELPATH
    if not path.exists():
        return "missing", (AuditFinding("index_missing", file=path.name),)
    if path.is_symlink() or not path.is_file():
        return "invalid", (AuditFinding("index_invalid", file=path.name),)
    if record_findings:
        return "unverifiable", ()
    expected = deterministic_json_bytes(build_index_payload(records))
    try:
        actual = path.read_bytes()
    except OSError:
        return "invalid", (AuditFinding("index_invalid", file=path.name),)
    if actual != expected:
        return "drifted", (AuditFinding("index_drift", file=path.name),)
    return "current", ()


def audit_store(root: Path, *, as_of: Optional[date] = None) -> Dict[str, Any]:
    """Compute a content-free audit report. This function performs no writes."""

    audit_date = as_of or date.today()
    records = load_canonical_records(root)
    raw_record_issues = validation_issues(records)
    record_findings = tuple(
        AuditFinding(issue.code, file=issue.file, field=issue.field) for issue in raw_record_issues
    )
    valid_records = tuple(record for record in records if record.valid)

    by_id, supersession_findings, chains = _supersession_state(valid_records)
    freshness = _freshness_counts(valid_records, by_id, audit_date)
    refusal_counts, refusal_findings, refusal_entries = _refusal_counts(root)
    index_status, index_findings = _index_state(root, records, record_findings)

    findings = list(record_findings + supersession_findings + refusal_findings + index_findings)
    findings.sort(
        key=lambda item: (item.code, item.file or "", item.field or "", item.source_id or "")
    )

    decisions = _enum_counts(valid_records, "decision", DECISIONS)
    decisions["pending"] = sum(
        1 for record in valid_records if record.data is not None and record.data.get("decision") is None
    )
    blocked_or_parked = decisions.get("deferred", 0) + decisions.get("pending", 0)

    return {
        "audit_version": AUDIT_VERSION,
        "as_of": audit_date.isoformat(),
        "blocked_or_parked_count": blocked_or_parked,
        "counts": {
            "by_decision": decisions,
            "by_freshness": freshness,
            "by_sensitivity": _enum_counts(valid_records, "sensitivity_level", SENSITIVITY_LEVELS),
            "by_source_type": _enum_counts(valid_records, "source_type", SOURCE_TYPES),
            "by_trust": _enum_counts(valid_records, "trust_level", TRUST_LEVELS),
            "by_validation_outcome": _validation_outcome_counts(valid_records),
            "record_files": len(records),
            "valid_records": len(valid_records),
        },
        "expiring_window_days": EXPIRING_WINDOW_DAYS,
        "finding_count": len(findings),
        "findings": [finding.to_dict() for finding in findings],
        "index_status": index_status,
        "latest_gate_audit": _latest_gate_audit(valid_records),
        "refusal_counts": refusal_counts,
        "refusal_entries": refusal_entries,
        "stale_implicated_count": freshness["stale"],
        "superseded_chains": [list(chain) for chain in chains],
        "writes_performed": 0,
    }
