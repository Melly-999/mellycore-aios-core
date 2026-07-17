"""Models and structural validation for the read-only Context Gate.

Standard library only, Python 3.9 compatible. This module performs no I/O and
has no write path. Validation findings carry field names and stable codes only;
they never carry rejected field values.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from typing import Any, Dict, List, Mapping, Optional, Tuple

GATE_SPEC_VERSION = "MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001 v1.0"

EXIT_OK = 0
EXIT_INVALID = 1
EXIT_REFUSED = 2

SOURCE_TYPES = (
    "user_provided",
    "repo_derived",
    "generated",
    "externally_sourced",
)
VERIFICATION_STATES = ("verified", "unverified")
TRUST_LEVELS = ("low", "medium", "high")
SENSITIVITY_LEVELS = (
    "public",
    "internal",
    "private",
    "secret",
    "regulated_high_risk",
)
ALLOWED_USES = (
    "must_not_be_ingested",
    "internal_reasoning_only",
    "internal_summary_display",
    "public_display",
)
STALENESS_POLICIES = ("immutable_historical", "volatile", "periodic_review")
DECISIONS = ("admitted", "rejected", "deferred")
VALIDATION_OUTCOMES = (
    "REFUSE",
    "CONTRADICTION_FOUND",
    "NEEDS_HUMAN_REVIEW",
    "ACCEPT_WITH_WARNINGS",
    "ACCEPT",
)

TRUST_DEFAULTS = {
    ("user_provided", "verified"): "high",
    ("user_provided", "unverified"): "medium",
    ("repo_derived", "verified"): "high",
    ("repo_derived", "unverified"): "medium",
    ("generated", "verified"): "medium",
    ("generated", "unverified"): "low",
    ("externally_sourced", "verified"): "medium",
    ("externally_sourced", "unverified"): "low",
}

ALLOWED_USE_DEFAULTS = {
    "public": "public_display",
    "internal": "internal_summary_display",
    "private": "internal_reasoning_only",
    "secret": "must_not_be_ingested",
    "regulated_high_risk": "must_not_be_ingested",
}

TRUST_RANK = {"low": 0, "medium": 1, "high": 2}
USE_RANK = {
    "must_not_be_ingested": 0,
    "internal_reasoning_only": 1,
    "internal_summary_display": 2,
    "public_display": 3,
}

RECORD_FIELDS = (
    "source_id",
    "source_identity",
    "source_type",
    "verification_state",
    "trust_level",
    "trust_level_rationale",
    "sensitivity_level",
    "allowed_use",
    "allowed_use_override_rationale",
    "claim",
    "captured_at",
    "staleness_policy",
    "review_after",
    "proposed_by",
    "reviewed_by",
    "reviewed_at",
    "decision",
    "decision_at",
    "decision_rationale",
    "superseded_by",
    "notes",
)

CANDIDATE_REQUIRED_FIELDS = (
    "source_id",
    "source_identity",
    "source_type",
    "verification_state",
    "sensitivity_level",
    "allowed_use",
    "claim",
    "captured_at",
    "staleness_policy",
    "proposed_by",
)

RECORD_ENVELOPE_FIELDS = {"preview", "record_status", "gate_audit", "envelope"}

#: Fields Phase I2's ``apply`` requires, already filled with a human Step 7
#: decision, before it will ever write a record. ``apply`` decides nothing;
#: it only writes what a human has already decided (provenance spec Section
#: 3, gate spec Section 8 Layer 1, implementation spec Section 5.3).
REQUIRED_DECISION_FIELDS = (
    "reviewed_by",
    "reviewed_at",
    "decision",
    "decision_at",
    "decision_rationale",
)

SOURCE_ID_RE = re.compile(r"^ctx-[a-z0-9][a-z0-9-]{2,127}$")

_FIELD_NAME_RE = re.compile(
    r"(?i)[\"']?(?:api[_-]?key|apikey|secret|client[_-]?secret|token|"
    r"auth[_-]?token|access[_-]?key|private[_-]?key|password|passwd|"
    r"credential|session[_-]?cookie|bearer|account[_-]?id)[\"']?\s*(?::|=)"
)

_SECRET_VALUE_PATTERNS = (
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"npg_[A-Za-z0-9]{20,}"),
    re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\."),
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    re.compile(
        r"(?i)\b(?:postgres|postgresql|mysql|mongodb|redis|amqp)"
        r"(?:\+\w+)?://[^\s:@/]+:[^\s:@/]+@"
    ),
)


class ContextGateError(Exception):
    """Base class for clean, aggregate-safe CLI failures."""


class InvalidInputError(ContextGateError):
    """Input is missing, unparseable, or structurally invalid."""


@dataclass(frozen=True)
class RecordFinding:
    """A structural finding with no rejected value attached."""

    code: str
    field: Optional[str]
    message: str

    def to_dict(self) -> Dict[str, Optional[str]]:
        return {"code": self.code, "field": self.field, "message": self.message}


@dataclass(frozen=True)
class ContextSource:
    """Normalized ContextSource preview/canonical semantic shape."""

    source_id: str
    source_identity: str
    source_type: str
    verification_state: str
    trust_level: str
    trust_level_rationale: Optional[str]
    sensitivity_level: str
    allowed_use: str
    allowed_use_override_rationale: Optional[str]
    claim: str
    captured_at: str
    staleness_policy: str
    review_after: Optional[str]
    proposed_by: str
    reviewed_by: Optional[str]
    reviewed_at: Optional[str]
    decision: Optional[str]
    decision_at: Optional[str]
    decision_rationale: Optional[str]
    superseded_by: Optional[str]
    notes: Optional[str]

    @classmethod
    def from_mapping(cls, data: Mapping[str, Any]) -> "ContextSource":
        findings = validate_record_shape(data)
        if findings:
            raise InvalidInputError(
                "record failed structural validation ({})".format(
                    ", ".join(f.code for f in findings)
                )
            )
        return cls(**{field: data.get(field) for field in RECORD_FIELDS})

    def to_dict(self) -> Dict[str, Any]:
        return {field: getattr(self, field) for field in RECORD_FIELDS}


def parse_date(value: Any) -> Optional[date]:
    """Return an exact ISO date, or ``None`` for malformed input."""

    if not isinstance(value, str):
        return None
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return None
    return parsed if parsed.isoformat() == value else None


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def text_is_secret_shaped(value: Any) -> bool:
    """Detect a secret shape without returning or retaining the matched value."""

    if not isinstance(value, str):
        return False
    return bool(_FIELD_NAME_RE.search(value)) or any(
        pattern.search(value) for pattern in _SECRET_VALUE_PATTERNS
    )


def deterministic_json_bytes(data: Mapping[str, Any]) -> bytes:
    """Canonical UTF-8/LF JSON bytes used by preview and future apply."""

    return (
        json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    ).encode("utf-8")


def _finding(code: str, field: Optional[str], message: str) -> RecordFinding:
    return RecordFinding(code=code, field=field, message=message)


def validate_record_shape(
    data: Mapping[str, Any], *, raw_bytes: Optional[bytes] = None
) -> Tuple[RecordFinding, ...]:
    """Validate a draft, decided, preview, or canonical ContextSource record."""

    if not isinstance(data, Mapping):
        return (_finding("record_not_object", None, "record must be a JSON object"),)

    findings: List[RecordFinding] = []
    allowed_fields = set(RECORD_FIELDS) | RECORD_ENVELOPE_FIELDS
    for field in sorted(set(data) - allowed_fields):
        findings.append(_finding("unknown_field", field, "field is not part of the record shape"))

    for field in RECORD_FIELDS:
        if field not in data:
            findings.append(_finding("missing_field", field, "required record field is missing"))

    for field in (
        "source_id",
        "source_identity",
        "source_type",
        "verification_state",
        "trust_level",
        "sensitivity_level",
        "allowed_use",
        "claim",
        "captured_at",
        "staleness_policy",
        "proposed_by",
    ):
        if field in data and not is_nonempty_string(data.get(field)):
            findings.append(_finding("invalid_field", field, "field must be a non-empty string"))

    source_id = data.get("source_id")
    if is_nonempty_string(source_id) and not SOURCE_ID_RE.fullmatch(source_id):
        findings.append(_finding("invalid_source_id", "source_id", "source_id format is invalid"))

    enum_checks = (
        ("source_type", SOURCE_TYPES),
        ("verification_state", VERIFICATION_STATES),
        ("trust_level", TRUST_LEVELS),
        ("sensitivity_level", SENSITIVITY_LEVELS),
        ("allowed_use", ALLOWED_USES),
        ("staleness_policy", STALENESS_POLICIES),
    )
    for field, allowed in enum_checks:
        value = data.get(field)
        if value is not None and value not in allowed:
            findings.append(_finding("invalid_enum", field, "field contains an unsupported label"))

    decision = data.get("decision")
    if decision is not None and decision not in DECISIONS:
        findings.append(_finding("invalid_enum", "decision", "field contains an unsupported label"))

    for field in ("captured_at", "review_after", "reviewed_at", "decision_at"):
        value = data.get(field)
        if value is not None and parse_date(value) is None:
            findings.append(_finding("invalid_date", field, "field must be YYYY-MM-DD or null"))

    policy = data.get("staleness_policy")
    if policy in ("volatile", "periodic_review") and parse_date(data.get("review_after")) is None:
        findings.append(
            _finding(
                "missing_review_after",
                "review_after",
                "volatile and periodic_review records require review_after",
            )
        )

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
        value = data.get(field)
        if value is not None and not is_nonempty_string(value):
            findings.append(_finding("invalid_field", field, "field must be null or a non-empty string"))

    if decision is not None:
        for field in ("reviewed_by", "reviewed_at", "decision_at", "decision_rationale"):
            if not is_nonempty_string(data.get(field)):
                findings.append(
                    _finding("missing_decision_metadata", field, "decided records require this field")
                )

    source_type = data.get("source_type")
    verification = data.get("verification_state")
    proposed_trust = data.get("trust_level")
    default_trust = TRUST_DEFAULTS.get((source_type, verification))
    if (
        default_trust is not None
        and proposed_trust in TRUST_LEVELS
        and proposed_trust != default_trust
        and not is_nonempty_string(data.get("trust_level_rationale"))
    ):
        findings.append(
            _finding(
                "missing_trust_rationale",
                "trust_level_rationale",
                "a trust-level override requires a rationale",
            )
        )

    sensitivity = data.get("sensitivity_level")
    allowed_use = data.get("allowed_use")
    default_use = ALLOWED_USE_DEFAULTS.get(sensitivity)
    if (
        default_use is not None
        and allowed_use in ALLOWED_USES
        and allowed_use != default_use
        and not is_nonempty_string(data.get("allowed_use_override_rationale"))
    ):
        findings.append(
            _finding(
                "missing_allowed_use_rationale",
                "allowed_use_override_rationale",
                "an allowed-use override requires a rationale",
            )
        )

    for field in ("claim", "notes", "decision_rationale"):
        if text_is_secret_shaped(data.get(field)):
            findings.append(
                _finding("field_level_secret", field, "field contains secret-shaped content")
            )

    gate_audit = data.get("gate_audit")
    if gate_audit is not None:
        if not isinstance(gate_audit, Mapping):
            findings.append(_finding("invalid_gate_audit", "gate_audit", "gate_audit must be an object"))
        else:
            required_audit = {
                "gate_spec_version",
                "validation_outcome",
                "warnings",
                "validated_at",
                "mode",
            }
            if set(gate_audit) != required_audit:
                findings.append(
                    _finding("invalid_gate_audit", "gate_audit", "gate_audit fields do not match the contract")
                )
            if gate_audit.get("validation_outcome") not in VALIDATION_OUTCOMES:
                findings.append(
                    _finding("invalid_gate_audit", "gate_audit", "validation_outcome is invalid")
                )
            warnings = gate_audit.get("warnings")
            if not isinstance(warnings, list) or not all(is_nonempty_string(v) for v in warnings):
                findings.append(
                    _finding("invalid_gate_audit", "gate_audit", "warnings must be a list of reason codes")
                )
            if parse_date(gate_audit.get("validated_at")) is None:
                findings.append(
                    _finding("invalid_gate_audit", "gate_audit", "validated_at must be YYYY-MM-DD")
                )

    envelope = data.get("envelope")
    if envelope is not None:
        expected = {"store", "migrated_from", "migrated_at"}
        if not isinstance(envelope, Mapping) or set(envelope) != expected:
            findings.append(_finding("invalid_envelope", "envelope", "canonical envelope is malformed"))
        elif envelope.get("store") != "canonical":
            findings.append(_finding("invalid_envelope", "envelope", "canonical envelope store is invalid"))

    if isinstance(envelope, Mapping) and envelope.get("store") == "canonical" and raw_bytes is not None:
        if raw_bytes != deterministic_json_bytes(data):
            findings.append(
                _finding(
                    "non_deterministic_serialization",
                    None,
                    "canonical record bytes are not sorted UTF-8/LF deterministic JSON",
                )
            )

    return tuple(findings)
