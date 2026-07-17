"""Synthetic, secret-free fixtures for Context Gate tests."""

from __future__ import annotations

from typing import Any, Dict

from scripts.context_gate.models import GATE_SPEC_VERSION, deterministic_json_bytes

AS_OF = "2026-07-17"


def candidate(**overrides: Any) -> Dict[str, Any]:
    item: Dict[str, Any] = {
        "source_id": "ctx-2026-07-17-valid-example",
        "source_identity": "docs/research/example.md",
        "source_type": "repo_derived",
        "input_class": "repo_derived",
        "verification_state": "verified",
        "trust_level": "high",
        "sensitivity_level": "internal",
        "allowed_use": "internal_summary_display",
        "claim": "The example was confirmed by direct repository read.",
        "captured_at": AS_OF,
        "staleness_policy": "immutable_historical",
        "review_after": None,
        "proposed_by": "MELLYCORE-CONTEXT-GATE-TEST-001",
        "trust_level_rationale": None,
        "allowed_use_override_rationale": None,
        "notes": "Verification method: direct repository read.",
        "depends_on": [],
        "contradicts": [],
        "supersedes": [],
    }
    item.update(overrides)
    return item


def record(**overrides: Any) -> Dict[str, Any]:
    item = candidate()
    result: Dict[str, Any] = {
        "source_id": item["source_id"],
        "source_identity": item["source_identity"],
        "source_type": item["source_type"],
        "verification_state": item["verification_state"],
        "trust_level": item["trust_level"],
        "trust_level_rationale": item["trust_level_rationale"],
        "sensitivity_level": item["sensitivity_level"],
        "allowed_use": item["allowed_use"],
        "allowed_use_override_rationale": item["allowed_use_override_rationale"],
        "claim": item["claim"],
        "captured_at": item["captured_at"],
        "staleness_policy": item["staleness_policy"],
        "review_after": item["review_after"],
        "proposed_by": item["proposed_by"],
        "reviewed_by": None,
        "reviewed_at": None,
        "decision": None,
        "decision_at": None,
        "decision_rationale": None,
        "superseded_by": None,
        "notes": item["notes"],
    }
    result.update(overrides)
    return result


def canonical_record(**overrides: Any) -> Dict[str, Any]:
    result = record()
    result.update(overrides)
    result["gate_audit"] = {
        "gate_spec_version": GATE_SPEC_VERSION,
        "validation_outcome": "ACCEPT",
        "warnings": [],
        "validated_at": AS_OF,
        "mode": "preview",
    }
    result["envelope"] = {
        "store": "canonical",
        "migrated_from": None,
        "migrated_at": None,
    }
    return result


def canonical_bytes(**overrides: Any) -> bytes:
    return deterministic_json_bytes(canonical_record(**overrides))


def preview_record(**overrides: Any) -> Dict[str, Any]:
    """A decided, admitted record shaped exactly like the six real files
    under ``shared_context/context_provenance_preview/``: full
    ``ContextSource`` fields, a filled human decision, a ``gate_audit``
    block, plus the preview-only envelope fields (``preview``,
    ``record_status``) that migration must strip."""

    base = record(
        reviewed_by="Test Operator",
        reviewed_at=AS_OF,
        decision="admitted",
        decision_at=AS_OF,
        decision_rationale="Admitted for test purposes.",
    )
    base["gate_audit"] = {
        "gate_spec_version": GATE_SPEC_VERSION,
        "validation_outcome": "ACCEPT",
        "warnings": [],
        "validated_at": AS_OF,
        "mode": "preview_hand_exercised",
    }
    base["preview"] = True
    base["record_status"] = "ADMITTED_IN_PREVIEW_LOCATION_PENDING_CANONICAL_MIGRATION"
    base.update(overrides)
    return base


def decided_candidate(**overrides: Any) -> Dict[str, Any]:
    """A batch-manifest item already carrying its human Step 7 decision --
    exactly the shape Phase I2's ``apply --batch`` requires before it will
    write anything."""

    item = candidate()
    item.update(
        {
            "reviewed_by": "Test Operator",
            "reviewed_at": AS_OF,
            "decision": "admitted",
            "decision_at": AS_OF,
            "decision_rationale": "Admitted for test purposes.",
        }
    )
    item.update(overrides)
    return item
