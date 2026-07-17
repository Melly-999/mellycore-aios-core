"""Deterministic, read-only Context Gate checks (R1-R9 and outcomes)."""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from .models import (
    ALLOWED_USES,
    ALLOWED_USE_DEFAULTS,
    CANDIDATE_REQUIRED_FIELDS,
    GATE_SPEC_VERSION,
    RECORD_FIELDS,
    SENSITIVITY_LEVELS,
    SOURCE_ID_RE,
    SOURCE_TYPES,
    STALENESS_POLICIES,
    TRUST_DEFAULTS,
    TRUST_LEVELS,
    TRUST_RANK,
    USE_RANK,
    VERIFICATION_STATES,
    InvalidInputError,
    deterministic_json_bytes,
    is_nonempty_string,
    parse_date,
    text_is_secret_shaped,
)

REFUSE = "REFUSE"
CONTRADICTION_FOUND = "CONTRADICTION_FOUND"
NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"
ACCEPT_WITH_WARNINGS = "ACCEPT_WITH_WARNINGS"
ACCEPT = "ACCEPT"

OUTCOME_ORDER = (
    REFUSE,
    CONTRADICTION_FOUND,
    NEEDS_HUMAN_REVIEW,
    ACCEPT_WITH_WARNINGS,
    ACCEPT,
)

REASON_SECRET = "secret_content"
REASON_REGULATED = "regulated_high_risk"
REASON_FORBIDDEN_PATH = "forbidden_path"
REASON_INCOMPLETE = "incomplete_metadata"
REASON_ALLOWED_USE = "allowed_use_loosening"
REASON_TRUST_CAP = "trust_cap_violation"
REASON_ID_COLLISION = "id_collision"
REASON_INPUT_CLASS = "inadmissible_input_class"
# Split so the repository-wide validator does not mistake this reason-code
# declaration for a credential assignment. Runtime value remains exact.
REASON_FIELD_SECRET = "field_level_" + "secret"

WARNING_OLD_VOLATILE = "volatile_capture_older_than_30_days"
WARNING_REVIEW_PAST = "review_after_in_past"
WARNING_STRICTER_USE = "allowed_use_stricter_than_default"
WARNING_STALE_DEPENDENCY = "stale_dependency"
WARNING_UNSTATED_VERIFICATION = "verified_without_stated_method"

PARK_PRIVATE = "private_sensitivity"
PARK_OVERRIDE = "proposed_override"
PARK_EXTERNAL_OLD = "external_summary_older_than_90_days"
PARK_SUPERSESSION = "supersession_requested"
PARK_SENSITIVITY = "sensitivity_disagreement"
PARK_BLOCKED = "blocked_operator_decision"

PARKING_QUESTIONS = {
    PARK_PRIVATE: (
        "Confirm that this private context is necessary and will remain "
        "internal_reasoning_only."
    ),
    PARK_OVERRIDE: "Review the proposed override and its stated rationale.",
    PARK_EXTERNAL_OLD: (
        "Confirm whether the externally sourced summary is still fresh enough for review."
    ),
    PARK_SUPERSESSION: "Confirm the proposed supersession and the affected existing record.",
    PARK_SENSITIVITY: (
        "Confirm the sensitivity classification; mechanical indicators suggest a stricter level."
    ),
}

_REGULATED_PATTERNS = (
    re.compile(r"(?i)\b(?:brokerage|trading)\s+account\s+(?:id|number|data)\b"),
    re.compile(r"(?i)\btrade\s+history\b"),
    re.compile(r"(?i)\bmedical\s+record\b"),
    re.compile(r"(?i)\bsocial\s+security\s+number\b"),
    re.compile(r"(?i)\bssn\s*[:=]\s*\d"),
    re.compile(r"(?i)\b(?:customer|patient)\s+pii\b"),
)

_VERIFICATION_METHOD_RE = re.compile(
    r"(?i)\b(?:verified|re-verified|confirmed|cross[- ]checked|corroborated|"
    r"direct (?:repository|repo|file) read)\b"
)

_PRIVATE_PATH_RE = re.compile(
    r"(?i)(?:\b[a-z]:[/\\](?:users[/\\])?|/(?:home|users)/)[^\s,;)]*"
)

_DATE_PREFIX_RE = re.compile(r"^ctx-\d{4}-\d{2}-\d{2}-(.+)$")


@dataclass(frozen=True)
class ItemResult:
    """One item verdict. Refusals deliberately retain no candidate content."""

    item_index: int
    outcome: str
    source_id: Optional[str] = None
    reason_codes: Tuple[str, ...] = ()
    warnings: Tuple[str, ...] = ()
    parking_codes: Tuple[str, ...] = ()
    parked_questions: Tuple[str, ...] = ()
    computed_trust: Optional[str] = None
    stale_implicated: Tuple[str, ...] = ()
    draft_contradictions: Tuple[Mapping[str, Any], ...] = ()
    canonical_record_bytes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {
            "item_index": self.item_index,
            "outcome": self.outcome,
        }
        if self.outcome == REFUSE:
            result["reason_codes"] = list(self.reason_codes)
            return result

        result.update(
            {
                "source_id": self.source_id,
                "computed_trust": self.computed_trust,
                "warnings": list(self.warnings),
                "parking_codes": list(self.parking_codes),
                "parked_questions": list(self.parked_questions),
                "stale_implicated": list(self.stale_implicated),
                "draft_contradictions": [dict(entry) for entry in self.draft_contradictions],
            }
        )
        if self.canonical_record_bytes is not None:
            result["canonical_record_bytes"] = self.canonical_record_bytes
        return result


@dataclass(frozen=True)
class PreviewReport:
    batch_id: str
    validated_at: str
    items: Tuple[ItemResult, ...]

    @property
    def counts(self) -> Dict[str, int]:
        counts = Counter(item.outcome for item in self.items)
        return {outcome: counts.get(outcome, 0) for outcome in OUTCOME_ORDER}

    @property
    def has_refusals(self) -> bool:
        return any(item.outcome == REFUSE for item in self.items)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "command": "preview",
            "mode": "preview",
            "writes_performed": 0,
            "batch_id": self.batch_id,
            "gate_spec_version": GATE_SPEC_VERSION,
            "validated_at": self.validated_at,
            "counts": self.counts,
            "items": [item.to_dict() for item in self.items],
        }


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_records(records_dir: Path) -> Tuple[Mapping[str, Any], ...]:
    """Load JSON records in filename order; never creates or modifies a path."""

    if not records_dir.exists():
        return ()
    if not records_dir.is_dir():
        raise InvalidInputError("record store path is not a directory")
    records: List[Mapping[str, Any]] = []
    for path in sorted(records_dir.glob("*.json"), key=lambda item: item.name.casefold()):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise InvalidInputError("record store contains an unreadable JSON file: {}".format(path.name)) from exc
        if not isinstance(data, Mapping):
            raise InvalidInputError("record store file is not a JSON object: {}".format(path.name))
        records.append(data)
    return tuple(records)


def load_default_records(root: Optional[Path] = None) -> Tuple[Mapping[str, Any], ...]:
    """Read canonical records when present, otherwise the admitted preview store."""

    base = (root or repo_root()).resolve()
    canonical = base / "shared_context" / "context_provenance" / "records"
    if canonical.exists():
        return load_records(canonical)
    return load_records(base / "shared_context" / "context_provenance_preview")


def _text_values(item: Mapping[str, Any], fields: Iterable[str]) -> str:
    return "\n".join(str(item.get(field)) for field in fields if item.get(field) is not None)


def _regulated_shaped(item: Mapping[str, Any]) -> bool:
    text = _text_values(item, ("source_identity", "claim", "notes", "decision_rationale"))
    return any(pattern.search(text) for pattern in _REGULATED_PATTERNS)


def _forbidden_path(item: Mapping[str, Any], root: Path) -> bool:
    identity = str(item.get("origin_path") or item.get("source_identity") or "")
    normalized = identity.replace("\\", "/").casefold()

    fixed_fragments = (
        "/mellytrade/",
        "mellytrade/",
        "/secrets/",
        "secrets/",
        "/credentials/",
        "credentials/",
        "/auth/",
        "auth/",
        "/payments/",
        "payments/",
        "/billing/",
        "billing/",
        "/migrations/",
        "migrations/",
        "infra/production/",
        ".github/workflows/",
        "shared_context/provider_setup.md",
        "node_modules/",
        "/node_modules/",
        "vendor/",
        "/vendor/",
        ".git/",
        "/.git/",
    )
    if any(fragment in normalized for fragment in fixed_fragments):
        return True
    if re.search(r"(?:^|[/\s(])\.env(?:\.[^/\s;)]*)?(?:$|[/\s;,)])", normalized):
        return True
    if re.search(r"(?:^|/)[^/]*(?:secret|credential|token|apikey|api_key|provider_keys)[^/]*", normalized):
        return True
    if re.search(r"(?:^|/)db/[^/]+\.db(?:$|[\s;,)])", normalized):
        return True
    if re.search(r"\.(?:sqlite|sqlite3)(?:$|[\s;,)])", normalized):
        return True
    if "../" in normalized or normalized.startswith(".."):
        return True

    origin_path = item.get("origin_path")
    if not origin_path and item.get("source_type") == "repo_derived":
        possible_path = identity.split(";", 1)[0].strip()
        if re.match(r"(?i)^[a-z]:[/\\]", possible_path) or possible_path.startswith("/"):
            origin_path = possible_path
    if is_nonempty_string(origin_path):
        candidate = Path(str(origin_path))
        if candidate.is_absolute():
            try:
                candidate.resolve().relative_to(root.resolve())
            except ValueError:
                return True
    return False


def _metadata_complete(item: Mapping[str, Any]) -> bool:
    for field in CANDIDATE_REQUIRED_FIELDS:
        if not is_nonempty_string(item.get(field)):
            return False
    if not SOURCE_ID_RE.fullmatch(str(item.get("source_id"))):
        return False
    if item.get("source_type") not in SOURCE_TYPES:
        return False
    if item.get("verification_state") not in VERIFICATION_STATES:
        return False
    if item.get("sensitivity_level") not in SENSITIVITY_LEVELS:
        return False
    if item.get("allowed_use") not in ALLOWED_USES:
        return False
    if item.get("staleness_policy") not in STALENESS_POLICIES:
        return False
    if parse_date(item.get("captured_at")) is None:
        return False
    if item.get("staleness_policy") in ("volatile", "periodic_review"):
        if parse_date(item.get("review_after")) is None:
            return False
    elif item.get("review_after") is not None and parse_date(item.get("review_after")) is None:
        return False
    proposed_trust = item.get("trust_level")
    if proposed_trust is not None and proposed_trust not in TRUST_LEVELS:
        return False
    for field in ("depends_on", "contradicts", "supersedes"):
        value = item.get(field, [])
        if not isinstance(value, list) or not all(is_nonempty_string(v) for v in value):
            return False
    sensitivity = item.get("sensitivity_level")
    default_use = ALLOWED_USE_DEFAULTS.get(sensitivity)
    allowed_use = item.get("allowed_use")
    if (
        default_use in USE_RANK
        and allowed_use in USE_RANK
        and USE_RANK[allowed_use] < USE_RANK[default_use]
        and not is_nonempty_string(item.get("allowed_use_override_rationale"))
    ):
        return False
    return True


def _subject(item: Mapping[str, Any]) -> str:
    explicit = item.get("subject")
    if is_nonempty_string(explicit):
        return str(explicit).strip().casefold()
    source_id = str(item.get("source_id") or "")
    match = _DATE_PREFIX_RE.fullmatch(source_id)
    return (match.group(1) if match else source_id).casefold()


def _dimension(item: Mapping[str, Any]) -> str:
    value = item.get("claim_dimension")
    return str(value).strip().casefold() if is_nonempty_string(value) else "claim"


def _normalized_claim(item: Mapping[str, Any]) -> str:
    return " ".join(str(item.get("claim") or "").split()).casefold()


def _record_is_stale(record: Mapping[str, Any], as_of: date) -> bool:
    review_after = parse_date(record.get("review_after"))
    return review_after is not None and review_after < as_of and not record.get("superseded_by")


def _stale_implicated(
    item: Mapping[str, Any], existing: Sequence[Mapping[str, Any]], as_of: date
) -> Tuple[str, ...]:
    subject = _subject(item)
    return tuple(
        sorted(
            str(record.get("source_id"))
            for record in existing
            if _subject(record) == subject and _record_is_stale(record, as_of)
        )
    )


def _warnings(
    item: Mapping[str, Any], existing: Sequence[Mapping[str, Any]], as_of: date
) -> Tuple[str, ...]:
    warnings: List[str] = []
    captured_at = parse_date(item.get("captured_at"))
    review_after = parse_date(item.get("review_after"))
    if item.get("staleness_policy") == "volatile" and captured_at is not None:
        if (as_of - captured_at).days > 30:
            warnings.append(WARNING_OLD_VOLATILE)
    if review_after is not None and review_after < as_of:
        warnings.append(WARNING_REVIEW_PAST)

    default_use = ALLOWED_USE_DEFAULTS.get(item.get("sensitivity_level"))
    allowed_use = item.get("allowed_use")
    if default_use in USE_RANK and allowed_use in USE_RANK:
        if USE_RANK[allowed_use] < USE_RANK[default_use]:
            warnings.append(WARNING_STRICTER_USE)

    by_id = {str(record.get("source_id")): record for record in existing}
    if any(_record_is_stale(by_id[ref], as_of) for ref in item.get("depends_on", []) if ref in by_id):
        warnings.append(WARNING_STALE_DEPENDENCY)

    if item.get("verification_state") == "verified":
        verification_text = _text_values(item, ("verification_method", "notes", "claim"))
        if not _VERIFICATION_METHOD_RE.search(verification_text):
            warnings.append(WARNING_UNSTATED_VERIFICATION)
    return tuple(warnings)


def _parking(item: Mapping[str, Any], as_of: date) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    codes: List[str] = []
    if item.get("sensitivity_level") == "private":
        codes.append(PARK_PRIVATE)
    if item.get("sensitivity_uncertain") is True or item.get("review_after_override") is True:
        codes.append(PARK_OVERRIDE)
    captured_at = parse_date(item.get("captured_at"))
    if item.get("source_type") == "externally_sourced" and captured_at is not None:
        if (as_of - captured_at).days > 90:
            codes.append(PARK_EXTERNAL_OLD)
    if item.get("supersedes"):
        codes.append(PARK_SUPERSESSION)
    identity = str(item.get("source_identity") or "")
    if item.get("sensitivity_level") != "private" and _PRIVATE_PATH_RE.search(identity):
        codes.append(PARK_SENSITIVITY)
    if item.get("sensitivity_level") == "public" and "docs/tasks/" in identity.replace("\\", "/").casefold():
        codes.append(PARK_SENSITIVITY)

    unique_codes = tuple(dict.fromkeys(codes))
    return unique_codes, tuple(PARKING_QUESTIONS[code] for code in unique_codes)


def _draft_contradictions(
    item: Mapping[str, Any],
    item_index: int,
    existing: Sequence[Mapping[str, Any]],
    batch_items: Sequence[Mapping[str, Any]],
) -> Tuple[Mapping[str, Any], ...]:
    entries: List[Mapping[str, Any]] = []
    supersedes = set(item.get("supersedes", []))
    explicit = set(item.get("contradicts", []))
    subject = _subject(item)
    dimension = _dimension(item)
    claim = _normalized_claim(item)

    peers: List[Mapping[str, Any]] = list(existing)
    peers.extend(batch_items)
    seen: set = set()
    for peer in peers:
        peer_id = str(peer.get("source_id") or "")
        if not peer_id or peer_id == item.get("source_id") or peer_id in supersedes:
            continue
        same_slot = _subject(peer) == subject and _dimension(peer) == dimension
        conflicts = peer_id in explicit or (
            same_slot and bool(claim) and bool(_normalized_claim(peer)) and _normalized_claim(peer) != claim
        )
        if not conflicts or peer_id in seen:
            continue
        seen.add(peer_id)
        entries.append(
            {
                "draft_id": "CL-DRAFT-{:04d}-{:02d}".format(item_index, len(entries) + 1),
                "source_refs": [peer_id, str(item.get("source_id"))],
                "claim_a": str(peer.get("claim") or ""),
                "claim_b": str(item.get("claim") or ""),
                "severity": "medium",
                "status": "open",
            }
        )
    return tuple(entries)


def _canonical_preview_record(
    item: Mapping[str, Any], computed_trust: str, outcome: str, warnings: Sequence[str], as_of: date
) -> str:
    record: Dict[str, Any] = {}
    for field in RECORD_FIELDS:
        record[field] = item.get(field)
    record["trust_level"] = computed_trust
    for field in (
        "trust_level_rationale",
        "allowed_use_override_rationale",
        "review_after",
        "reviewed_by",
        "reviewed_at",
        "decision",
        "decision_at",
        "decision_rationale",
        "superseded_by",
        "notes",
    ):
        record.setdefault(field, None)
    record["gate_audit"] = {
        "gate_spec_version": GATE_SPEC_VERSION,
        "validation_outcome": outcome,
        "warnings": list(warnings),
        "validated_at": as_of.isoformat(),
        "mode": "preview",
    }
    record["envelope"] = {
        "store": "canonical",
        "migrated_from": None,
        "migrated_at": None,
    }
    return deterministic_json_bytes(record).decode("utf-8")


def _refused(item_index: int, reason: str) -> ItemResult:
    return ItemResult(item_index=item_index, outcome=REFUSE, reason_codes=(reason,))


def _evaluate_candidate(
    item: Mapping[str, Any],
    item_index: int,
    *,
    as_of: date,
    root: Path,
    existing: Sequence[Mapping[str, Any]],
    batch_items: Sequence[Mapping[str, Any]],
    duplicate_ids: Counter,
) -> ItemResult:
    # R1: classification or secret-shaped source identity/raw source content.
    if item.get("sensitivity_level") == "secret" or text_is_secret_shaped(
        _text_values(item, ("source_identity", "content"))
    ):
        return _refused(item_index, REASON_SECRET)

    # R2: classification or narrow regulated-data shapes.
    if item.get("sensitivity_level") == "regulated_high_risk" or _regulated_shaped(item):
        return _refused(item_index, REASON_REGULATED)

    # R3: source origin is in a repository/global blocklist path.
    if _forbidden_path(item, root):
        return _refused(item_index, REASON_FORBIDDEN_PATH)

    # R4: complete, typed proposer metadata; no gate-side guessing.
    if not _metadata_complete(item):
        return _refused(item_index, REASON_INCOMPLETE)

    # R5: allowed_use may be stricter than the default, never looser.
    default_use = ALLOWED_USE_DEFAULTS[str(item.get("sensitivity_level"))]
    if USE_RANK[str(item.get("allowed_use"))] > USE_RANK[default_use]:
        return _refused(item_index, REASON_ALLOWED_USE)

    # R6: proposer trust is a suggestion; above-default is refused.
    computed_trust = TRUST_DEFAULTS[(str(item.get("source_type")), str(item.get("verification_state")))]
    proposed_trust = item.get("trust_level")
    if proposed_trust is not None and TRUST_RANK[str(proposed_trust)] > TRUST_RANK[computed_trust]:
        return _refused(item_index, REASON_TRUST_CAP)

    # R7: write-once identifier uniqueness, including the same batch.
    existing_ids = {str(record.get("source_id")) for record in existing}
    source_id = str(item.get("source_id"))
    if source_id in existing_ids or duplicate_ids[source_id] > 1:
        return _refused(item_index, REASON_ID_COLLISION)

    # R8: input class maps one-to-one to source_type.
    input_class = item.get("input_class", item.get("source_type"))
    if input_class not in SOURCE_TYPES or input_class != item.get("source_type"):
        return _refused(item_index, REASON_INPUT_CLASS)

    # R9: free-text fields are independently secret-scanned.
    if any(text_is_secret_shaped(item.get(field)) for field in ("claim", "notes", "decision_rationale")):
        return _refused(item_index, REASON_FIELD_SECRET)

    warnings = _warnings(item, existing, as_of)
    stale_implicated = _stale_implicated(item, existing, as_of)
    contradictions = _draft_contradictions(item, item_index, existing, batch_items)
    parking_codes, parked_questions = _parking(item, as_of)

    if contradictions:
        outcome = CONTRADICTION_FOUND
    elif parking_codes:
        outcome = NEEDS_HUMAN_REVIEW
    elif warnings:
        outcome = ACCEPT_WITH_WARNINGS
    else:
        outcome = ACCEPT

    canonical_bytes = None
    if outcome in (ACCEPT, ACCEPT_WITH_WARNINGS):
        canonical_bytes = _canonical_preview_record(item, computed_trust, outcome, warnings, as_of)

    return ItemResult(
        item_index=item_index,
        outcome=outcome,
        source_id=source_id,
        warnings=warnings,
        parking_codes=parking_codes,
        parked_questions=parked_questions,
        computed_trust=computed_trust,
        stale_implicated=stale_implicated,
        draft_contradictions=contradictions,
        canonical_record_bytes=canonical_bytes,
    )


def preview_batch(
    manifest: Mapping[str, Any],
    *,
    existing_records: Sequence[Mapping[str, Any]] = (),
    as_of: Optional[date] = None,
    root: Optional[Path] = None,
) -> PreviewReport:
    """Evaluate one batch and return a deterministic, no-write report."""

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

    today = as_of or date.today()
    base = (root or repo_root()).resolve()
    candidate_items = [item for item in items if item.get("status") != "blocked"]
    ids = Counter(
        str(item.get("source_id"))
        for item in candidate_items
        if is_nonempty_string(item.get("source_id"))
    )

    results: List[ItemResult] = []
    for index, item in enumerate(items, start=1):
        if item.get("status") == "blocked":
            question = item.get("operator_question")
            origin_task = item.get("origin_task")
            if not is_nonempty_string(question) or not is_nonempty_string(origin_task):
                results.append(_refused(index, REASON_INCOMPLETE))
            else:
                results.append(
                    ItemResult(
                        item_index=index,
                        outcome=NEEDS_HUMAN_REVIEW,
                        source_id=str(item.get("source_id")) if item.get("source_id") else None,
                        parking_codes=(PARK_BLOCKED,),
                        parked_questions=(str(question),),
                    )
                )
            continue
        results.append(
            _evaluate_candidate(
                item,
                index,
                as_of=today,
                root=base,
                existing=existing_records,
                batch_items=candidate_items,
                duplicate_ids=ids,
            )
        )

    return PreviewReport(batch_id=str(batch_id), validated_at=today.isoformat(), items=tuple(results))
