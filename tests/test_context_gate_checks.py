"""Unit coverage for Context Gate R1-R9, outcomes, and deterministic preview."""

from __future__ import annotations

import copy
import json
import unittest
from datetime import date

from tests.context_gate_fixtures import AS_OF, candidate, record
from scripts.context_gate.checks import (
    ACCEPT,
    ACCEPT_WITH_WARNINGS,
    CONTRADICTION_FOUND,
    NEEDS_HUMAN_REVIEW,
    REFUSE,
    REASON_ALLOWED_USE,
    REASON_FIELD_SECRET,
    REASON_FORBIDDEN_PATH,
    REASON_ID_COLLISION,
    REASON_INCOMPLETE,
    REASON_INPUT_CLASS,
    REASON_REGULATED,
    REASON_SECRET,
    REASON_TRUST_CAP,
    WARNING_OLD_VOLATILE,
    WARNING_REVIEW_PAST,
    WARNING_STALE_DEPENDENCY,
    WARNING_STRICTER_USE,
    WARNING_UNSTATED_VERIFICATION,
    preview_batch,
)
from scripts.context_gate.models import TRUST_DEFAULTS

TODAY = date.fromisoformat(AS_OF)


def run_one(item, existing=()):
    report = preview_batch(
        {"batch_id": "batch-test-001", "items": [item]},
        existing_records=existing,
        as_of=TODAY,
    )
    return report.items[0]


class ImmediateRefusalTests(unittest.TestCase):
    def assert_refused(self, item, reason, existing=()):
        result = run_one(item, existing)
        self.assertEqual(REFUSE, result.outcome)
        self.assertEqual((reason,), result.reason_codes)
        self.assertIsNone(result.source_id)
        self.assertIsNone(result.canonical_record_bytes)

    def test_r1_secret_classification(self):
        self.assert_refused(candidate(sensitivity_level="secret"), REASON_SECRET)

    def test_r2_regulated_classification(self):
        self.assert_refused(
            candidate(sensitivity_level="regulated_high_risk"), REASON_REGULATED
        )

    def test_r2_regulated_shaped_claim(self):
        self.assert_refused(candidate(claim="A brokerage account number was supplied."), REASON_REGULATED)

    def test_r3_forbidden_path(self):
        self.assert_refused(candidate(source_identity=".env.local"), REASON_FORBIDDEN_PATH)

    def test_r3_mellytrade_path(self):
        forbidden = (
            "C:/AI/MellyTrade/private.md",
            ".github/workflows/publish.yml",
            "db/local.db",
            "node_modules/package/index.js",
            "shared_context/PROVIDER_SETUP.md",
        )
        for path in forbidden:
            with self.subTest(path=path):
                self.assert_refused(candidate(source_identity=path), REASON_FORBIDDEN_PATH)

    def test_r4_missing_metadata(self):
        item = candidate()
        del item["captured_at"]
        self.assert_refused(item, REASON_INCOMPLETE)

    def test_r4_missing_review_after(self):
        self.assert_refused(
            candidate(staleness_policy="volatile", review_after=None), REASON_INCOMPLETE
        )

    def test_r5_allowed_use_loosening(self):
        self.assert_refused(
            candidate(
                sensitivity_level="private",
                allowed_use="internal_summary_display",
            ),
            REASON_ALLOWED_USE,
        )

    def test_r6_generated_high_trust(self):
        self.assert_refused(
            candidate(
                source_type="generated",
                input_class="generated",
                verification_state="verified",
                trust_level="high",
            ),
            REASON_TRUST_CAP,
        )

    def test_r7_existing_id_collision(self):
        existing = record()
        self.assert_refused(candidate(), REASON_ID_COLLISION, existing=(existing,))

    def test_r7_same_batch_collision_refuses_both_items(self):
        first = candidate()
        second = candidate(claim="A different direct repository read was confirmed.")
        report = preview_batch(
            {"batch_id": "batch-duplicate", "items": [first, second]}, as_of=TODAY
        )
        self.assertEqual([REFUSE, REFUSE], [item.outcome for item in report.items])
        self.assertTrue(all(item.reason_codes == (REASON_ID_COLLISION,) for item in report.items))

    def test_r8_inadmissible_input_class(self):
        self.assert_refused(candidate(input_class="binary"), REASON_INPUT_CLASS)

    def test_r8_mismatched_input_class(self):
        self.assert_refused(candidate(input_class="generated"), REASON_INPUT_CLASS)

    def test_r9_secret_shaped_free_text(self):
        synthetic = "sk-" + ("TEST" * 5)
        self.assert_refused(candidate(claim="Synthetic fixture {}".format(synthetic)), REASON_FIELD_SECRET)

    def test_refusal_precedence_beats_parking_and_contradiction(self):
        existing = record(source_id="ctx-2026-06-01-same", subject="same", claim="A")
        item = candidate(
            source_id="ctx-2026-07-17-other",
            subject="same",
            claim="B",
            sensitivity_level="secret",
        )
        self.assert_refused(item, REASON_SECRET, existing=(existing,))

    def test_passing_twins_clear_each_hard_rule(self):
        variants = [
            candidate(),
            candidate(sensitivity_level="internal"),
            candidate(source_identity="docs/research/safe.md"),
            candidate(review_after=None),
            candidate(allowed_use="internal_summary_display"),
            candidate(
                source_type="generated",
                input_class="generated",
                verification_state="verified",
                trust_level="medium",
                notes="Verified by direct file read.",
            ),
            candidate(source_id="ctx-2026-07-17-unique"),
            candidate(input_class="repo_derived"),
            candidate(claim="Synthetic fixtures contain no credential values."),
        ]
        for item in variants:
            with self.subTest(item=item["source_id"], claim=item["claim"]):
                self.assertNotEqual(REFUSE, run_one(item).outcome)


class TrustAndWarningTests(unittest.TestCase):
    def test_all_eight_trust_lookup_cells(self):
        for index, ((source_type, verification), expected) in enumerate(TRUST_DEFAULTS.items()):
            item = candidate(
                source_id="ctx-2026-07-17-trust-{}".format(index),
                source_type=source_type,
                input_class=source_type,
                verification_state=verification,
                trust_level=expected,
                notes=(
                    "Verified by direct repository read."
                    if verification == "verified"
                    else "Not independently checked."
                ),
            )
            with self.subTest(source_type=source_type, verification=verification):
                self.assertEqual(expected, run_one(item).computed_trust)

    def test_below_default_suggestion_is_ignored_in_favor_of_computed(self):
        result = run_one(
            candidate(trust_level="low", trust_level_rationale="Conservative proposer suggestion.")
        )
        self.assertEqual("high", result.computed_trust)
        self.assertNotEqual(REFUSE, result.outcome)

    def test_old_volatile_capture_warning(self):
        result = run_one(
            candidate(
                captured_at="2026-05-01",
                staleness_policy="volatile",
                review_after="2026-08-01",
            )
        )
        self.assertEqual(ACCEPT_WITH_WARNINGS, result.outcome)
        self.assertIn(WARNING_OLD_VOLATILE, result.warnings)

    def test_past_review_after_warning_not_refusal(self):
        result = run_one(
            candidate(staleness_policy="periodic_review", review_after="2026-07-16")
        )
        self.assertEqual(ACCEPT_WITH_WARNINGS, result.outcome)
        self.assertIn(WARNING_REVIEW_PAST, result.warnings)

    def test_stricter_allowed_use_warning(self):
        result = run_one(
            candidate(
                allowed_use="internal_reasoning_only",
                allowed_use_override_rationale="Keep the generated compression reviewer-only.",
            )
        )
        self.assertEqual(ACCEPT_WITH_WARNINGS, result.outcome)
        self.assertIn(WARNING_STRICTER_USE, result.warnings)

    def test_stale_dependency_warning(self):
        stale = record(
            source_id="ctx-2026-06-01-stale-dependency",
            staleness_policy="volatile",
            review_after="2026-07-16",
        )
        result = run_one(
            candidate(depends_on=[stale["source_id"]]), existing=(stale,)
        )
        self.assertEqual(ACCEPT_WITH_WARNINGS, result.outcome)
        self.assertIn(WARNING_STALE_DEPENDENCY, result.warnings)

    def test_verified_without_method_warning(self):
        result = run_one(candidate(claim="The example exists.", notes="No method supplied."))
        self.assertEqual(ACCEPT_WITH_WARNINGS, result.outcome)
        self.assertIn(WARNING_UNSTATED_VERIFICATION, result.warnings)


class ParkingStalenessAndContradictionTests(unittest.TestCase):
    def test_private_item_is_parked_with_specific_question(self):
        result = run_one(
            candidate(
                sensitivity_level="private",
                allowed_use="internal_reasoning_only",
            )
        )
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertEqual(("private_sensitivity",), result.parking_codes)
        self.assertIn("private context", result.parked_questions[0])

    def test_blocked_item_repeats_operator_question(self):
        question = "Should the machine-specific path be admitted or declined?"
        report = preview_batch(
            {
                "batch_id": "batch-blocked",
                "items": [
                    {
                        "status": "blocked",
                        "origin_task": "MELLYCORE-CONTEXT-FIRST-ADMISSION-REVIEW-001",
                        "operator_question": question,
                    }
                ],
            },
            as_of=TODAY,
        )
        result = report.items[0]
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertEqual((question,), result.parked_questions)

    def test_malformed_blocked_item_refuses_aggregate_safely(self):
        report = preview_batch(
            {"batch_id": "batch-blocked", "items": [{"status": "blocked"}]},
            as_of=TODAY,
        )
        self.assertEqual(REFUSE, report.items[0].outcome)
        self.assertEqual((REASON_INCOMPLETE,), report.items[0].reason_codes)

    def test_uncertain_sensitivity_parks(self):
        result = run_one(candidate(sensitivity_uncertain=True))
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertIn("proposed_override", result.parking_codes)

    def test_old_external_summary_parks(self):
        result = run_one(
            candidate(
                source_type="externally_sourced",
                input_class="externally_sourced",
                verification_state="unverified",
                trust_level="low",
                captured_at="2026-04-01",
                notes="Not independently checked.",
            )
        )
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertIn("external_summary_older_than_90_days", result.parking_codes)

    def test_supersession_parks_without_forcing_contradiction(self):
        existing = record(source_id="ctx-2026-06-01-current-state", claim="State A")
        result = run_one(
            candidate(
                source_id="ctx-2026-07-17-current-state",
                claim="State B",
                supersedes=[existing["source_id"]],
            ),
            existing=(existing,),
        )
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertFalse(result.draft_contradictions)

    def test_public_task_internal_source_parks_for_sensitivity(self):
        result = run_one(
            candidate(
                source_identity="docs/tasks/internal-review.md",
                sensitivity_level="public",
                allowed_use="public_display",
            )
        )
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertIn("sensitivity_disagreement", result.parking_codes)

    def test_warning_does_not_beat_private_parking(self):
        result = run_one(
            candidate(
                sensitivity_level="private",
                allowed_use="internal_reasoning_only",
                claim="The example exists.",
                notes="No method supplied.",
            )
        )
        self.assertEqual(NEEDS_HUMAN_REVIEW, result.outcome)
        self.assertIn(WARNING_UNSTATED_VERIFICATION, result.warnings)

    def test_stale_implicated_is_reported_not_auto_expired(self):
        stale = record(
            source_id="ctx-2026-06-01-project-status",
            claim="Status is stable.",
            staleness_policy="volatile",
            review_after="2026-07-16",
        )
        result = run_one(
            candidate(
                source_id="ctx-2026-07-17-project-status",
                claim="Status is stable.",
            ),
            existing=(stale,),
        )
        self.assertEqual(ACCEPT, result.outcome)
        self.assertEqual((stale["source_id"],), result.stale_implicated)

    def test_store_same_subject_and_dimension_conflict(self):
        existing = record(
            source_id="ctx-2026-06-01-project-status",
            claim="Status A",
        )
        result = run_one(
            candidate(source_id="ctx-2026-07-17-project-status", claim="Status B"),
            existing=(existing,),
        )
        self.assertEqual(CONTRADICTION_FOUND, result.outcome)
        self.assertEqual(1, len(result.draft_contradictions))
        self.assertIsNone(result.canonical_record_bytes)

    def test_same_batch_conflict(self):
        first = candidate(
            source_id="ctx-2026-07-17-first",
            subject="shared-status",
            claim="Status A",
        )
        second = candidate(
            source_id="ctx-2026-07-17-second",
            subject="shared-status",
            claim="Status B",
        )
        report = preview_batch(
            {"batch_id": "batch-conflict", "items": [first, second]}, as_of=TODAY
        )
        self.assertEqual(
            [CONTRADICTION_FOUND, CONTRADICTION_FOUND],
            [item.outcome for item in report.items],
        )

    def test_loops_vs_runs_near_miss_is_not_a_contradiction(self):
        existing = record(
            source_id="ctx-2026-06-01-project-health",
            subject="project-health",
            claim_dimension="run_count",
            claim="There are two persisted runs.",
        )
        result = run_one(
            candidate(
                source_id="ctx-2026-07-17-project-health",
                subject="project-health",
                claim_dimension="exercised_loop_count",
                claim="Audit reports exercised: 1 because it counts loops, not runs.",
            ),
            existing=(existing,),
        )
        self.assertNotEqual(CONTRADICTION_FOUND, result.outcome)

    def test_preview_is_deterministic_and_emits_stable_canonical_bytes(self):
        manifest = {"batch_id": "batch-deterministic", "items": [candidate()]}
        first = preview_batch(copy.deepcopy(manifest), as_of=TODAY)
        second = preview_batch(copy.deepcopy(manifest), as_of=TODAY)
        first_json = json.dumps(first.to_dict(), sort_keys=True, ensure_ascii=False)
        second_json = json.dumps(second.to_dict(), sort_keys=True, ensure_ascii=False)
        self.assertEqual(first_json, second_json)
        self.assertEqual(
            first.items[0].canonical_record_bytes,
            second.items[0].canonical_record_bytes,
        )


if __name__ == "__main__":
    unittest.main()
