"""Tests for the Stage B activation-control layer (scripts.mellycore_batch.activation).

Covers: pricing-evidence schema/digest/freshness/dual-lock; exact-model and
request-envelope boundary enforcement; Decimal cost-cap exactness; prohibited
-capability rejection; authorization-artifact validation and one-time
consumption (including atomicity and dry-run non-consumption); and the
hardcoded Stage C kill switch. Nothing here reaches the network or imports
the OpenAI SDK.
"""

from __future__ import annotations

import copy
import json
import os
import tempfile
import threading
import unittest
from datetime import datetime, timezone
from decimal import (
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_EVEN,
    ROUND_UP,
    Decimal,
    localcontext,
)
from pathlib import Path

from scripts.mellycore_batch import activation as act
from scripts.mellycore_batch.models import BatchRequest

_NOW = datetime(2026, 7, 29, 0, 0, 0, tzinfo=timezone.utc)


def _make_request(custom_id="r1", max_output_tokens=100, model=None, extra_body=None):
    body = {
        "model": model or act.STAGE_B_MODEL,
        "input": "hello",
        "max_output_tokens": max_output_tokens,
    }
    if extra_body:
        body.update(extra_body)
    return BatchRequest(
        custom_id=custom_id, method="POST", url=act.STAGE_B_ENDPOINT, body=body
    )


def _make_authorization_dict(**overrides):
    base = {
        "schema_version": 1,
        "authorization_id": "auth-001",
        "task_id": "MELLYCORE-OPENAI-BATCH-API-CONTROLLED-ACTIVATION-001",
        "issued_at": "2026-07-29T00:00:00Z",
        "expires_at": "2026-07-29T00:10:00Z",
        "canonical_base_sha": "81b1baf9da5363ef088fe236de93d6cd3713b659",
        "activation_commit_sha": "1111111111111111111111111111111111111111",
        "provider": act.STAGE_B_PROVIDER,
        "endpoint": act.STAGE_B_ENDPOINT,
        "model": act.STAGE_B_MODEL,
        "maximum_cost": "0.01",
        "maximum_requests": act.STAGE_B_MAX_REQUESTS,
        "maximum_input_bytes": act.STAGE_B_MAX_INPUT_BYTES,
        "maximum_output_tokens_per_request": act.STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST,
        "maximum_total_output_tokens": act.STAGE_B_MAX_TOTAL_OUTPUT_TOKENS,
        "one_time_use": True,
    }
    base.update(overrides)
    return base


class PricingManifestSchemaTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = act.load_pricing_manifest()

    def test_default_manifest_loads_and_validates(self) -> None:
        act.validate_pricing_evidence(self.manifest, _NOW)

    def test_missing_field_rejected(self) -> None:
        tampered = dict(self.manifest)
        del tampered["hard_cost_cap_usd"]
        with self.assertRaises(act.PricingManifestSchemaError):
            act.validate_pricing_manifest_schema(tampered)

    def test_wrong_type_rejected(self) -> None:
        tampered = dict(self.manifest)
        tampered["maximum_requests"] = "3"
        with self.assertRaises(act.PricingManifestSchemaError):
            act.validate_pricing_manifest_schema(tampered)

    def test_bool_not_accepted_as_int(self) -> None:
        tampered = dict(self.manifest)
        tampered["maximum_requests"] = True
        with self.assertRaises(act.PricingManifestSchemaError):
            act.validate_pricing_manifest_schema(tampered)

    def test_unexpected_top_level_field_rejected(self) -> None:
        tampered = dict(self.manifest)
        tampered["future_override"] = True
        with self.assertRaises(act.PricingManifestSchemaError):
            act.validate_pricing_manifest_schema(tampered)


class StrictSecurityJSONTests(unittest.TestCase):
    def _assert_pricing_duplicate_rejected(self, original, replacement) -> None:
        manifest = act.load_pricing_manifest()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "pricing.json"
            path.write_text(
                json.dumps(manifest, indent=2).replace(original, replacement, 1),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                act.PricingManifestSchemaError, "duplicate JSON object key"
            ) as raised:
                act.load_pricing_manifest(path)
        self.assertNotIn("duplicate-secret-value", str(raised.exception))

    def _assert_authorization_duplicate_rejected(self, original, replacement) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "authorization.json"
            path.write_text(
                json.dumps(_make_authorization_dict(), indent=2).replace(
                    original, replacement, 1
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(
                act.AuthorizationArtifactSchemaError, "duplicate JSON object key"
            ) as raised:
                act.load_authorization_artifact(path)
        self.assertNotIn("duplicate-secret-value", str(raised.exception))

    def test_duplicate_top_level_pricing_key_rejected(self) -> None:
        self._assert_pricing_duplicate_rejected(
            '  "maximum_requests": 3,',
            '  "maximum_requests": 99,\n  "maximum_requests": 3,',
        )

    def test_duplicate_nested_pricing_key_rejected(self) -> None:
        self._assert_pricing_duplicate_rejected(
            '    "input": "0.20",',
            '    "input": "duplicate-secret-value",\n    "input": "0.20",',
        )

    def test_duplicate_pricing_model_rejected(self) -> None:
        self._assert_pricing_duplicate_rejected(
            '  "model": "gpt-5.4-nano-2026-03-17",',
            '  "model": "other",\n  "model": "gpt-5.4-nano-2026-03-17",',
        )

    def test_duplicate_pricing_hard_cap_rejected(self) -> None:
        self._assert_pricing_duplicate_rejected(
            '  "hard_cost_cap_usd": "0.01",',
            '  "hard_cost_cap_usd": "9",\n  "hard_cost_cap_usd": "0.01",',
        )

    def test_duplicate_pricing_timestamp_rejected(self) -> None:
        self._assert_pricing_duplicate_rejected(
            '  "valid_until": "2026-08-27T22:00:34Z",',
            '  "valid_until": "2126-08-27T22:00:34Z",\n'
            '  "valid_until": "2026-08-27T22:00:34Z",',
        )

    def test_duplicate_authorization_field_rejected(self) -> None:
        self._assert_authorization_duplicate_rejected(
            '  "maximum_requests": 3,',
            '  "maximum_requests": 99,\n  "maximum_requests": 3,',
        )

    def test_duplicate_authorization_model_rejected(self) -> None:
        self._assert_authorization_duplicate_rejected(
            '  "model": "gpt-5.4-nano-2026-03-17",',
            '  "model": "other",\n  "model": "gpt-5.4-nano-2026-03-17",',
        )

    def test_duplicate_authorization_timestamp_rejected(self) -> None:
        self._assert_authorization_duplicate_rejected(
            '  "expires_at": "2026-07-29T00:10:00Z",',
            '  "expires_at": "2126-07-29T00:00:00Z",\n'
            '  "expires_at": "2026-07-29T00:10:00Z",',
        )


class PricingManifestDigestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = act.load_pricing_manifest()

    def test_digest_matches_shipped_manifest(self) -> None:
        act.verify_pricing_evidence_digest(self.manifest)

    def test_digest_is_deterministic(self) -> None:
        first = act.compute_pricing_evidence_digest(self.manifest)
        second = act.compute_pricing_evidence_digest(dict(self.manifest))
        self.assertEqual(first, second)

    def test_digest_excludes_itself(self) -> None:
        without_digest = {
            k: v for k, v in self.manifest.items() if k != "evidence_digest"
        }
        with_digest = dict(without_digest)
        with_digest["evidence_digest"] = "not-the-real-digest"
        self.assertEqual(
            act.compute_pricing_evidence_digest(without_digest),
            act.compute_pricing_evidence_digest(with_digest),
        )

    def test_tampered_content_fails_digest(self) -> None:
        tampered = dict(self.manifest)
        tampered["hard_cost_cap_usd"] = "999.00"
        with self.assertRaises(act.PricingManifestDigestMismatchError):
            act.verify_pricing_evidence_digest(tampered)

    def test_tampered_digest_value_itself_fails(self) -> None:
        tampered = dict(self.manifest)
        tampered["evidence_digest"] = "0" * 64
        with self.assertRaises(act.PricingManifestDigestMismatchError):
            act.verify_pricing_evidence_digest(tampered)


class PricingFreshnessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = act.load_pricing_manifest()

    def test_within_window_passes(self) -> None:
        act.enforce_pricing_freshness(self.manifest, _NOW)

    def test_one_second_before_expiry_passes(self) -> None:
        act.enforce_pricing_freshness(
            self.manifest,
            datetime(2026, 8, 27, 22, 0, 33, tzinfo=timezone.utc),
        )

    def test_exactly_at_expiry_fails_closed(self) -> None:
        valid_until = datetime(2026, 8, 27, 22, 0, 34, tzinfo=timezone.utc)
        with self.assertRaises(act.PricingEvidenceExpiredError):
            act.enforce_pricing_freshness(self.manifest, valid_until)

    def test_one_second_past_expiry_fails(self) -> None:
        past_expiry = datetime(2026, 8, 27, 22, 0, 35, tzinfo=timezone.utc)
        with self.assertRaises(act.PricingEvidenceExpiredError):
            act.enforce_pricing_freshness(self.manifest, past_expiry)

    def test_before_verified_at_fails(self) -> None:
        too_early = datetime(2020, 1, 1, tzinfo=timezone.utc)
        with self.assertRaises(act.PricingEvidenceExpiredError):
            act.enforce_pricing_freshness(self.manifest, too_early)

    def test_naive_datetime_rejected(self) -> None:
        naive_now = datetime(2026, 7, 29, 0, 0, 0)
        with self.assertRaises(act.PricingManifestSchemaError):
            act.enforce_pricing_freshness(self.manifest, naive_now)

    def test_noncanonical_pricing_timestamp_strings_rejected(self) -> None:
        for raw_timestamp in (
            "2026-07-28T22:00:34",
            "2026-07-28T23:00:34+01:00",
            "2026-07-28T22:00:34.000Z",
            "2026-06-30T23:59:60Z",
        ):
            with self.subTest(raw_timestamp=raw_timestamp):
                tampered = copy.deepcopy(self.manifest)
                tampered["verified_at"] = raw_timestamp
                with self.assertRaises(act.PricingManifestSchemaError):
                    act.enforce_pricing_freshness(tampered, _NOW)


class DualLockConstantAgreementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = act.load_pricing_manifest()

    def _assert_recomputed_digest_mutation_rejected(self, mutate) -> None:
        tampered = copy.deepcopy(self.manifest)
        mutate(tampered)
        tampered["evidence_digest"] = act.compute_pricing_evidence_digest(tampered)
        with self.assertRaises(
            (
                act.PricingManifestConstantMismatchError,
                act.PricingManifestSchemaError,
            )
        ):
            act.validate_pricing_evidence(tampered, _NOW)

    def test_shipped_manifest_agrees_with_constants(self) -> None:
        act.enforce_manifest_matches_constants(self.manifest)

    def test_manifest_cannot_widen_max_requests(self) -> None:
        tampered = dict(self.manifest)
        tampered["maximum_requests"] = act.STAGE_B_MAX_REQUESTS + 1
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_narrow_either_fails_closed(self) -> None:
        # Even a *tighter* value than the Python constant is rejected: the
        # dual lock requires exact agreement, not "manifest <= constant".
        tampered = dict(self.manifest)
        tampered["maximum_requests"] = act.STAGE_B_MAX_REQUESTS - 1
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_change_model(self) -> None:
        tampered = dict(self.manifest)
        tampered["model"] = "gpt-4o"
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_change_hard_cost_cap(self) -> None:
        tampered = dict(self.manifest)
        tampered["hard_cost_cap_usd"] = "1.00"
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_change_batch_price(self) -> None:
        tampered = copy.deepcopy(self.manifest)
        tampered["batch"]["input"] = "0.01"
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_change_pricing_unit(self) -> None:
        tampered = dict(self.manifest)
        tampered["pricing_unit_tokens"] = 1
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_enable_prohibited_capability(self) -> None:
        tampered = dict(self.manifest)
        tampered["tools_allowed"] = True
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_change_automatic_retries(self) -> None:
        tampered = dict(self.manifest)
        tampered["automatic_retries"] = 1
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_manifest_cannot_enable_automatic_resubmission(self) -> None:
        tampered = dict(self.manifest)
        tampered["automatic_resubmission"] = True
        with self.assertRaises(act.PricingManifestConstantMismatchError):
            act.enforce_manifest_matches_constants(tampered)

    def test_recomputed_digest_cannot_change_synchronous_input(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["synchronous"].__setitem__("input", "0.19")
        )

    def test_recomputed_digest_cannot_change_synchronous_cached_input(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["synchronous"].__setitem__(
                "cached_input", "0.01"
            )
        )

    def test_recomputed_digest_cannot_change_synchronous_output(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["synchronous"].__setitem__("output", "1.24")
        )

    def test_recomputed_digest_cannot_change_batch_discount(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest.__setitem__("batch_discount_percent", "49")
        )

    def test_recomputed_digest_cannot_replace_source_url(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["source_urls"].__setitem__(
                0, "https://unreviewed.invalid/"
            )
        )

    def test_recomputed_digest_cannot_add_source_url(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["source_urls"].append(
                "https://unreviewed.invalid/"
            )
        )

    def test_recomputed_digest_cannot_remove_source_url(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["source_urls"].pop()
        )

    def test_recomputed_digest_cannot_change_verified_timestamp(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest.__setitem__(
                "verified_at", "2026-07-28T22:00:33Z"
            )
        )

    def test_recomputed_digest_cannot_extend_expiry(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest.__setitem__(
                "valid_until", "2026-08-27T22:00:35Z"
            )
        )

    def test_recomputed_digest_cannot_change_prohibited_flag(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest.__setitem__("external_retrieval_allowed", True)
        )

    def test_exponent_form_price_rejected(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest["batch"].__setitem__("input", "1E-1")
        )

    def test_alternate_cost_cap_representation_rejected(self) -> None:
        self._assert_recomputed_digest_mutation_rejected(
            lambda manifest: manifest.__setitem__("hard_cost_cap_usd", "0.010")
        )

    def test_every_reviewed_authority_category_is_dual_locked(self) -> None:
        mutations = (
            ("schema_version", lambda m: m.__setitem__("schema_version", 2)),
            ("provider", lambda m: m.__setitem__("provider", "other")),
            ("endpoint", lambda m: m.__setitem__("endpoint", "/v1/other")),
            ("model", lambda m: m.__setitem__("model", "other")),
            (
                "processing_region",
                lambda m: m.__setitem__("processing_region", "regional"),
            ),
            ("currency", lambda m: m.__setitem__("currency", "EUR")),
            (
                "pricing_unit_tokens",
                lambda m: m.__setitem__("pricing_unit_tokens", 1000),
            ),
            (
                "synchronous_input",
                lambda m: m["synchronous"].__setitem__("input", "0.19"),
            ),
            (
                "synchronous_cached_input",
                lambda m: m["synchronous"].__setitem__("cached_input", "0.01"),
            ),
            (
                "synchronous_output",
                lambda m: m["synchronous"].__setitem__("output", "1.24"),
            ),
            ("batch_input", lambda m: m["batch"].__setitem__("input", "0.09")),
            (
                "batch_cached_input",
                lambda m: m["batch"].__setitem__("cached_input", "0.009"),
            ),
            ("batch_output", lambda m: m["batch"].__setitem__("output", "0.624")),
            (
                "batch_discount_percent",
                lambda m: m.__setitem__("batch_discount_percent", "49"),
            ),
            (
                "cached_input_assumed",
                lambda m: m.__setitem__("cached_input_assumed", True),
            ),
            (
                "verified_at",
                lambda m: m.__setitem__("verified_at", "2026-07-28T22:00:33Z"),
            ),
            (
                "valid_until",
                lambda m: m.__setitem__("valid_until", "2026-08-27T22:00:35Z"),
            ),
            ("maximum_requests", lambda m: m.__setitem__("maximum_requests", 4)),
            (
                "maximum_input_bytes",
                lambda m: m.__setitem__("maximum_input_bytes", 65537),
            ),
            (
                "maximum_output_tokens_per_request",
                lambda m: m.__setitem__("maximum_output_tokens_per_request", 513),
            ),
            (
                "maximum_total_output_tokens",
                lambda m: m.__setitem__("maximum_total_output_tokens", 1537),
            ),
            (
                "hard_cost_cap_usd",
                lambda m: m.__setitem__("hard_cost_cap_usd", "0.02"),
            ),
            (
                "automatic_retries",
                lambda m: m.__setitem__("automatic_retries", 1),
            ),
            (
                "automatic_resubmission",
                lambda m: m.__setitem__("automatic_resubmission", True),
            ),
            ("tools_allowed", lambda m: m.__setitem__("tools_allowed", True)),
            ("files_allowed", lambda m: m.__setitem__("files_allowed", True)),
            ("images_allowed", lambda m: m.__setitem__("images_allowed", True)),
            (
                "external_retrieval_allowed",
                lambda m: m.__setitem__("external_retrieval_allowed", True),
            ),
            (
                "source_urls",
                lambda m: m["source_urls"].__setitem__(
                    0, "https://unreviewed.invalid/"
                ),
            ),
        )
        for label, mutate in mutations:
            with self.subTest(label=label):
                self._assert_recomputed_digest_mutation_rejected(mutate)


class ExactModelEnforcementTests(unittest.TestCase):
    def test_exact_model_accepted(self) -> None:
        act.enforce_exact_model(act.STAGE_B_MODEL)

    def test_alias_rejected(self) -> None:
        with self.assertRaises(act.ModelMismatchError):
            act.enforce_exact_model("gpt-5.4-nano")

    def test_different_model_rejected(self) -> None:
        with self.assertRaises(act.ModelMismatchError):
            act.enforce_exact_model("gpt-4o")

    def test_missing_model_rejected(self) -> None:
        with self.assertRaises(act.ModelMismatchError):
            act.enforce_exact_model(None)

    def test_non_string_model_rejected(self) -> None:
        with self.assertRaises(act.ModelMismatchError):
            act.enforce_exact_model(12345)


class RequestEnvelopeBoundaryTests(unittest.TestCase):
    def test_at_the_limit_accepted(self) -> None:
        requests = [
            _make_request("r{}".format(i), max_output_tokens=512) for i in range(1, 4)
        ]
        report = act.enforce_request_envelope(
            requests, input_byte_count=act.STAGE_B_MAX_INPUT_BYTES
        )
        self.assertEqual(3, report.request_count)
        self.assertEqual(1536, report.total_max_output_tokens)

    def test_zero_requests_rejected(self) -> None:
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope([], input_byte_count=0)

    def test_one_over_request_count_rejected(self) -> None:
        requests = [
            _make_request("r{}".format(i), max_output_tokens=1) for i in range(1, 5)
        ]
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope(requests, input_byte_count=10)

    def test_input_bytes_at_limit_accepted(self) -> None:
        requests = [_make_request("r1", max_output_tokens=1)]
        act.enforce_request_envelope(
            requests, input_byte_count=act.STAGE_B_MAX_INPUT_BYTES
        )

    def test_input_bytes_one_over_rejected(self) -> None:
        requests = [_make_request("r1", max_output_tokens=1)]
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope(
                requests, input_byte_count=act.STAGE_B_MAX_INPUT_BYTES + 1
            )

    def test_per_request_max_output_tokens_at_limit_accepted(self) -> None:
        requests = [
            _make_request(
                "r1", max_output_tokens=act.STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST
            )
        ]
        act.enforce_request_envelope(requests, input_byte_count=10)

    def test_per_request_max_output_tokens_one_over_rejected(self) -> None:
        requests = [
            _make_request(
                "r1", max_output_tokens=act.STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST + 1
            )
        ]
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope(requests, input_byte_count=10)

    def test_total_max_output_tokens_over_budget_rejected(self) -> None:
        # With max_requests=3 and a 512 per-request cap, 3 * 512 == 1536 is
        # exactly the total cap -- so any request shape that pushes the total
        # over budget necessarily also trips the per-request cap first (there
        # is no way to have 3 requests each <=512 sum to more than 1536).
        # This confirms the combination is still rejected, whichever specific
        # check fires first.
        requests = [
            _make_request("r1", max_output_tokens=512),
            _make_request("r2", max_output_tokens=512),
            _make_request("r3", max_output_tokens=513),
        ]
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope(requests, input_byte_count=10)

    def test_total_max_output_tokens_exactly_at_cap_accepted(self) -> None:
        requests = [
            _make_request("r1", max_output_tokens=512),
            _make_request("r2", max_output_tokens=512),
            _make_request("r3", max_output_tokens=512),
        ]
        report = act.enforce_request_envelope(requests, input_byte_count=10)
        self.assertEqual(
            act.STAGE_B_MAX_TOTAL_OUTPUT_TOKENS, report.total_max_output_tokens
        )

    def test_max_output_tokens_missing_rejected(self) -> None:
        body = {"model": act.STAGE_B_MODEL, "input": "hi"}
        request = BatchRequest(
            custom_id="r1", method="POST", url=act.STAGE_B_ENDPOINT, body=body
        )
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope([request], input_byte_count=10)

    def test_max_output_tokens_zero_rejected(self) -> None:
        requests = [_make_request("r1", max_output_tokens=0)]
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope(requests, input_byte_count=10)

    def test_max_output_tokens_bool_rejected(self) -> None:
        body = {"model": act.STAGE_B_MODEL, "input": "hi", "max_output_tokens": True}
        request = BatchRequest(
            custom_id="r1", method="POST", url=act.STAGE_B_ENDPOINT, body=body
        )
        with self.assertRaises(act.RequestEnvelopeExceededError):
            act.enforce_request_envelope([request], input_byte_count=10)

    def test_wrong_model_in_one_request_rejected(self) -> None:
        requests = [_make_request("r1", max_output_tokens=1, model="gpt-4o")]
        with self.assertRaises(act.ModelMismatchError):
            act.enforce_request_envelope(requests, input_byte_count=10)


class ProhibitedCapabilityTests(unittest.TestCase):
    def test_clean_body_has_no_findings(self) -> None:
        body = {"model": act.STAGE_B_MODEL, "input": "hello", "max_output_tokens": 10}
        self.assertEqual([], act.detect_prohibited_capabilities(body))

    def test_tools_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": "hi",
            "max_output_tokens": 1,
            "tools": [{"type": "web_search"}],
        }
        findings = act.detect_prohibited_capabilities(body)
        self.assertTrue(any("tools" in f for f in findings))

    def test_tool_choice_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": "hi",
            "max_output_tokens": 1,
            "tool_choice": "auto",
        }
        self.assertTrue(act.detect_prohibited_capabilities(body))

    def test_service_tier_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": "hi",
            "max_output_tokens": 1,
            "service_tier": "priority",
        }
        self.assertTrue(act.detect_prohibited_capabilities(body))

    def test_region_override_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": "hi",
            "max_output_tokens": 1,
            "processing_region": "eu",
        }
        self.assertTrue(act.detect_prohibited_capabilities(body))

    def test_image_input_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": [
                {"type": "input_image", "image_url": "https://example.invalid/x.png"}
            ],
            "max_output_tokens": 1,
        }
        findings = act.detect_prohibited_capabilities(body)
        self.assertTrue(any("input_image" in f for f in findings))

    def test_file_input_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": [{"type": "input_file", "file_id": "file-abc"}],
            "max_output_tokens": 1,
        }
        self.assertTrue(act.detect_prohibited_capabilities(body))

    def test_audio_input_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": [{"type": "input_audio", "audio": "base64=="}],
            "max_output_tokens": 1,
        }
        self.assertTrue(act.detect_prohibited_capabilities(body))

    def test_remote_url_in_input_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": "please fetch https://example.invalid/data and summarize it",
            "max_output_tokens": 1,
        }
        findings = act.detect_prohibited_capabilities(body)
        self.assertTrue(any("external_url_at" in f for f in findings))

    def test_unrecognized_top_level_key_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": "hi",
            "max_output_tokens": 1,
            "some_future_openai_capability": True,
        }
        findings = act.detect_prohibited_capabilities(body)
        self.assertTrue(
            any(
                "unrecognized_body_key:some_future_openai_capability" in f
                for f in findings
            )
        )

    def test_nested_execution_capability_rejected(self) -> None:
        body = {
            "model": act.STAGE_B_MODEL,
            "input": [{"role": "user", "content": "hi", "retry": 1}],
            "max_output_tokens": 1,
        }
        findings = act.detect_prohibited_capabilities(body)
        self.assertTrue(any("prohibited_nested_key" in finding for finding in findings))

    def test_prohibited_capability_blocks_envelope_enforcement(self) -> None:
        requests = [_make_request("r1", max_output_tokens=1, extra_body={"tools": []})]
        with self.assertRaises(act.ProhibitedCapabilityError):
            act.enforce_request_envelope(requests, input_byte_count=10)


class CostCalculationTests(unittest.TestCase):
    def test_worst_case_envelope_matches_reference_numbers(self) -> None:
        estimate = act.estimate_cost(
            input_byte_count=act.STAGE_B_MAX_INPUT_BYTES,
            total_max_output_tokens=act.STAGE_B_MAX_TOTAL_OUTPUT_TOKENS,
        )
        self.assertEqual(Decimal("0.0065536"), estimate.input_cost)
        self.assertEqual(Decimal("0.00096"), estimate.output_cost)
        self.assertEqual(Decimal("0.0075136"), estimate.estimated_maximum_cost)
        margin = estimate.estimated_maximum_cost * Decimal("1.25")
        self.assertEqual(Decimal("0.009392000"), margin)
        self.assertLess(estimate.estimated_maximum_cost, act.STAGE_B_HARD_COST_CAP_USD)
        self.assertLess(margin, act.STAGE_B_HARD_COST_CAP_USD)

    def test_cost_uses_decimal_not_float(self) -> None:
        estimate = act.estimate_cost(100, 100)
        self.assertIsInstance(estimate.input_cost, Decimal)
        self.assertIsInstance(estimate.output_cost, Decimal)
        self.assertIsInstance(estimate.estimated_maximum_cost, Decimal)

    def test_zero_usage_is_zero_cost(self) -> None:
        estimate = act.estimate_cost(0, 0)
        self.assertEqual(Decimal(0), estimate.estimated_maximum_cost)

    def test_cost_within_cap_accepted(self) -> None:
        estimate = act.estimate_cost(
            input_byte_count=act.STAGE_B_MAX_INPUT_BYTES,
            total_max_output_tokens=act.STAGE_B_MAX_TOTAL_OUTPUT_TOKENS,
        )
        act.enforce_cost_cap(estimate)  # must not raise

    def test_cost_over_cap_rejected(self) -> None:
        estimate = act.estimate_cost(
            input_byte_count=200_000_000, total_max_output_tokens=1536
        )
        with self.assertRaises(act.CostCapExceededError):
            act.enforce_cost_cap(estimate)

    def test_cost_exactly_at_cap_accepted(self) -> None:
        # Solve for an input byte count that lands exactly on the cap with
        # zero output tokens: bytes * 0.10 / 1e6 == 0.01 -> bytes == 100000.
        estimate = act.estimate_cost(
            input_byte_count=100_000, total_max_output_tokens=0
        )
        self.assertEqual(act.STAGE_B_HARD_COST_CAP_USD, estimate.estimated_maximum_cost)
        act.enforce_cost_cap(
            estimate
        )  # boundary: equal to cap is accepted, not rejected

    def test_cost_one_unit_over_cap_rejected(self) -> None:
        estimate = act.estimate_cost(
            input_byte_count=100_001, total_max_output_tokens=0
        )
        self.assertGreater(
            estimate.estimated_maximum_cost, act.STAGE_B_HARD_COST_CAP_USD
        )
        with self.assertRaises(act.CostCapExceededError):
            act.enforce_cost_cap(estimate)

    def test_hostile_ambient_context_never_changes_authorization(self) -> None:
        for precision in (1, 2):
            for rounding in (
                ROUND_DOWN,
                ROUND_FLOOR,
                ROUND_HALF_EVEN,
                ROUND_UP,
            ):
                with self.subTest(precision=precision, rounding=rounding):
                    with localcontext() as hostile:
                        hostile.prec = precision
                        hostile.rounding = rounding
                        approved = act.estimate_cost(
                            act.STAGE_B_MAX_INPUT_BYTES,
                            act.STAGE_B_MAX_TOTAL_OUTPUT_TOKENS,
                        )
                        self.assertEqual(
                            Decimal("0.0075136"),
                            approved.estimated_maximum_cost,
                        )
                        act.enforce_cost_cap(approved)
                        exact_cap = act.estimate_cost(100_000, 0)
                        self.assertEqual(
                            Decimal("0.01"), exact_cap.estimated_maximum_cost
                        )
                        act.enforce_cost_cap(exact_cap)
                        over_cap = act.estimate_cost(100_001, 0)
                        self.assertEqual(
                            Decimal("0.0100001"),
                            over_cap.estimated_maximum_cost,
                        )
                        with self.assertRaises(act.CostCapExceededError):
                            act.enforce_cost_cap(over_cap)

    def test_unexpected_fractional_and_boolean_counts_rejected(self) -> None:
        for value in (True, Decimal("1.5"), 1.5):
            with self.subTest(value=value):
                with self.assertRaises(act.ActivationError):
                    act.estimate_cost(value, 0)


class AuthorizationArtifactSchemaTests(unittest.TestCase):
    def test_valid_artifact_parses(self) -> None:
        artifact = act.parse_authorization_artifact(_make_authorization_dict())
        self.assertEqual("auth-001", artifact.authorization_id)
        self.assertTrue(artifact.one_time_use)

    def test_missing_field_rejected(self) -> None:
        data = _make_authorization_dict()
        del data["expires_at"]
        with self.assertRaises(act.AuthorizationArtifactSchemaError):
            act.parse_authorization_artifact(data)

    def test_wrong_type_rejected(self) -> None:
        data = _make_authorization_dict(maximum_requests="3")
        with self.assertRaises(act.AuthorizationArtifactSchemaError):
            act.parse_authorization_artifact(data)

    def test_unexpected_field_rejected(self) -> None:
        data = _make_authorization_dict()
        data["api_key"] = "TEST-CREDENTIAL-SHOULD-NEVER-BE-ACCEPTED"
        with self.assertRaises(act.AuthorizationArtifactSchemaError):
            act.parse_authorization_artifact(data)

    def test_legitimate_field_names_containing_token_substring_not_flagged(
        self,
    ) -> None:
        # Regression guard: field names like maximum_output_tokens_per_request
        # contain the substring "token" but must not be treated as
        # credential-shaped -- the schema check is an allowlist of exact
        # field names, not a substring/keyword search.
        artifact = act.parse_authorization_artifact(_make_authorization_dict())
        self.assertEqual(
            act.STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST,
            artifact.maximum_output_tokens_per_request,
        )

    def test_one_time_use_false_rejected_at_validation(self) -> None:
        artifact = act.parse_authorization_artifact(
            _make_authorization_dict(one_time_use=False)
        )
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_malformed_identifier_rejected(self) -> None:
        with self.assertRaises(act.AuthorizationArtifactSchemaError):
            act.parse_authorization_artifact(
                _make_authorization_dict(authorization_id="../../unsafe")
            )

    def test_noncanonical_authorization_identifiers_rejected(self) -> None:
        invalid_ids = (
            "Auth-001",
            "auth.001",
            " auth-001",
            "auth/001",
            "auth\\001",
            "auth:001",
            "-auth",
            "_auth",
            "ąuth",
            "a" * 65,
            "",
        )
        for authorization_id in invalid_ids:
            with self.subTest(authorization_id=authorization_id):
                with self.assertRaises(act.AuthorizationArtifactSchemaError):
                    act.parse_authorization_artifact(
                        _make_authorization_dict(
                            authorization_id=authorization_id
                        )
                    )

    def test_windows_reserved_authorization_identifiers_rejected(self) -> None:
        reserved = ("con", "prn", "aux", "nul") + tuple(
            "com{}".format(index) for index in range(1, 10)
        ) + tuple("lpt{}".format(index) for index in range(1, 10))
        for authorization_id in reserved:
            with self.subTest(authorization_id=authorization_id):
                with self.assertRaises(act.AuthorizationArtifactSchemaError):
                    act.parse_authorization_artifact(
                        _make_authorization_dict(
                            authorization_id=authorization_id
                        )
                    )

    def test_malformed_commit_sha_rejected(self) -> None:
        with self.assertRaises(act.AuthorizationArtifactSchemaError):
            act.parse_authorization_artifact(
                _make_authorization_dict(activation_commit_sha="not-a-sha")
            )


class AuthorizationArtifactValidationTests(unittest.TestCase):
    def _artifact(self, **overrides):
        return act.parse_authorization_artifact(_make_authorization_dict(**overrides))

    def test_valid_artifact_validates(self) -> None:
        act.validate_authorization_artifact(
            self._artifact(),
            now=_NOW,
            expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
            expected_activation_commit_sha="1111111111111111111111111111111111111111",
        )

    def test_expired_rejected(self) -> None:
        artifact = self._artifact(expires_at="2026-07-01T00:00:00Z")
        with self.assertRaises(act.AuthorizationArtifactExpiredError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_wrong_canonical_sha_rejected(self) -> None:
        artifact = self._artifact()
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="0" * 40,
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_wrong_activation_sha_rejected(self) -> None:
        artifact = self._artifact()
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="2" * 40,
            )

    def test_wrong_model_rejected(self) -> None:
        artifact = self._artifact(model="gpt-4o")
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_wrong_task_id_rejected(self) -> None:
        artifact = self._artifact()
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
                expected_task_id="different-task",
            )

    def test_issued_in_future_rejected(self) -> None:
        artifact = self._artifact(issued_at="2026-07-30T00:00:00Z")
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_exact_expiry_rejected(self) -> None:
        artifact = self._artifact()
        with self.assertRaises(act.AuthorizationArtifactExpiredError):
            act.validate_authorization_artifact(
                artifact,
                now=datetime(2026, 7, 29, 0, 10, 0, tzinfo=timezone.utc),
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_one_second_before_expiry_accepted(self) -> None:
        artifact = self._artifact()
        act.validate_authorization_artifact(
            artifact,
            now=datetime(2026, 7, 29, 0, 9, 59, tzinfo=timezone.utc),
            expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
            expected_activation_commit_sha="1111111111111111111111111111111111111111",
        )

    def test_exactly_fifteen_minute_lifetime_accepted(self) -> None:
        artifact = self._artifact(expires_at="2026-07-29T00:15:00Z")
        act.validate_authorization_artifact(
            artifact,
            now=_NOW,
            expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
            expected_activation_commit_sha="1111111111111111111111111111111111111111",
        )

    def test_fifteen_minutes_plus_one_second_rejected(self) -> None:
        artifact = self._artifact(expires_at="2026-07-29T00:15:01Z")
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_century_long_lifetime_rejected(self) -> None:
        artifact = self._artifact(expires_at="2126-07-29T00:00:00Z")
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_naive_and_offset_authorization_timestamps_rejected(self) -> None:
        for issued_at in (
            "2026-07-29T00:00:00",
            "2026-07-29T01:00:00+01:00",
            "2026-07-29T00:00:00.000Z",
        ):
            with self.subTest(issued_at=issued_at):
                artifact = self._artifact(issued_at=issued_at)
                with self.assertRaises(act.AuthorizationArtifactInvalidError):
                    act.validate_authorization_artifact(
                        artifact,
                        now=_NOW,
                        expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                        expected_activation_commit_sha="1111111111111111111111111111111111111111",
                    )

    def test_exponent_form_maximum_cost_rejected(self) -> None:
        artifact = self._artifact(maximum_cost="1E-2")
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_expiry_must_follow_issue_time(self) -> None:
        artifact = self._artifact(
            issued_at="2026-08-01T00:00:00Z",
            expires_at="2026-08-01T00:00:00Z",
        )
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_wrong_cap_rejected(self) -> None:
        artifact = self._artifact(maximum_cost="0.02")
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_widened_maximum_requests_rejected(self) -> None:
        artifact = self._artifact(maximum_requests=act.STAGE_B_MAX_REQUESTS + 1)
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_narrower_maximum_requests_rejected_as_wrong_limit(self) -> None:
        artifact = self._artifact(maximum_requests=1)
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.validate_authorization_artifact(
                artifact,
                now=_NOW,
                expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                expected_activation_commit_sha="1111111111111111111111111111111111111111",
            )

    def test_consumed_authorization_rejected_during_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ledger_dir = Path(tmp)
            artifact = self._artifact()
            act.consume_authorization(artifact.authorization_id, ledger_dir)
            with self.assertRaises(act.AuthorizationAlreadyConsumedError):
                act.validate_authorization_artifact(
                    artifact,
                    now=_NOW,
                    expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
                    expected_activation_commit_sha="1111111111111111111111111111111111111111",
                    ledger_dir=ledger_dir,
                )


class AuthorizationConsumptionTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.ledger_dir = Path(self._tmp.name) / "authorizations"

    def test_not_consumed_initially(self) -> None:
        self.assertFalse(act.is_authorization_consumed("auth-001", self.ledger_dir))

    def test_consume_creates_marker_and_is_reflected(self) -> None:
        marker = act.consume_authorization("auth-001", self.ledger_dir)
        self.assertTrue(marker.exists())
        self.assertTrue(act.is_authorization_consumed("auth-001", self.ledger_dir))

    def test_reuse_rejected(self) -> None:
        act.consume_authorization("auth-001", self.ledger_dir)
        with self.assertRaises(act.AuthorizationAlreadyConsumedError):
            act.consume_authorization("auth-001", self.ledger_dir)

    def test_different_ids_do_not_collide(self) -> None:
        act.consume_authorization("auth-001", self.ledger_dir)
        act.consume_authorization("auth-002", self.ledger_dir)  # must not raise
        self.assertTrue(act.is_authorization_consumed("auth-001", self.ledger_dir))
        self.assertTrue(act.is_authorization_consumed("auth-002", self.ledger_dir))

    def test_two_concurrent_consumers_have_exactly_one_success(self) -> None:
        barrier = threading.Barrier(2)
        outcomes = []

        def consume() -> None:
            barrier.wait()
            try:
                act.consume_authorization("auth-race", self.ledger_dir)
                outcomes.append("success")
            except act.AuthorizationAlreadyConsumedError:
                outcomes.append("already-consumed")

        threads = [threading.Thread(target=consume) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        self.assertEqual(["already-consumed", "success"], sorted(outcomes))

    def test_symlinked_ledger_root_rejected_without_redirect(self) -> None:
        target = Path(self._tmp.name) / "redirect-target"
        target.mkdir()
        symlink = Path(self._tmp.name) / "ledger-symlink"
        os.symlink(str(target), str(symlink), target_is_directory=True)
        with self.assertRaises(act.AuthorizationLedgerSafetyError):
            act.consume_authorization("auth-symlink", symlink)
        self.assertEqual([], list(target.iterdir()))

    def test_symlinked_parent_component_rejected_without_redirect(self) -> None:
        target = Path(self._tmp.name) / "parent-target"
        target.mkdir()
        symlink = Path(self._tmp.name) / "parent-symlink"
        os.symlink(str(target), str(symlink), target_is_directory=True)
        with self.assertRaises(act.AuthorizationLedgerSafetyError):
            act.consume_authorization("auth-parent", symlink / "authorizations")
        self.assertEqual([], list(target.iterdir()))

    def test_symlinked_marker_rejected(self) -> None:
        act.consume_authorization("auth-bootstrap", self.ledger_dir)
        target = Path(self._tmp.name) / "marker-target"
        target.write_text("target", encoding="utf-8")
        marker = self.ledger_dir / "auth-marker.consumed"
        os.symlink(str(target), str(marker), target_is_directory=False)
        with self.assertRaises(act.AuthorizationLedgerSafetyError):
            act.is_authorization_consumed("auth-marker", self.ledger_dir)
        with self.assertRaises(act.AuthorizationLedgerSafetyError):
            act.consume_authorization("auth-marker", self.ledger_dir)
        self.assertEqual("target", target.read_text(encoding="utf-8"))

    def test_uppercase_case_variant_is_rejected(self) -> None:
        act.consume_authorization("auth-case", self.ledger_dir)
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.consume_authorization("AUTH-CASE", self.ledger_dir)

    def test_unsafe_authorization_id_rejected(self) -> None:
        with self.assertRaises(act.AuthorizationArtifactInvalidError):
            act.consume_authorization("../../etc/passwd", self.ledger_dir)

    def test_ledger_lives_under_runtime_batch(self) -> None:
        default_dir = act.default_authorization_ledger_dir()
        self.assertIn(".runtime", default_dir.parts)
        self.assertIn("batch", default_dir.parts)
        self.assertIn("authorizations", default_dir.parts)

    def test_dry_run_preflight_never_consumes(self) -> None:
        # Simulates what activation-preflight actually does: load, validate,
        # never call consume_authorization. Confirms no marker file appears.
        artifact = act.parse_authorization_artifact(_make_authorization_dict())
        act.validate_authorization_artifact(
            artifact,
            now=_NOW,
            expected_canonical_base_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
            expected_activation_commit_sha="1111111111111111111111111111111111111111",
        )
        self.assertFalse(
            act.is_authorization_consumed(artifact.authorization_id, self.ledger_dir)
        )
        self.assertFalse(self.ledger_dir.exists())


class LoadAuthorizationArtifactFileTests(unittest.TestCase):
    def test_round_trips_through_a_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "authorization.json"
            path.write_text(json.dumps(_make_authorization_dict()), encoding="utf-8")
            artifact = act.load_authorization_artifact(path)
            self.assertEqual("auth-001", artifact.authorization_id)

    def test_malformed_json_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "authorization.json"
            path.write_text("{not valid json", encoding="utf-8")
            with self.assertRaises(act.AuthorizationArtifactSchemaError):
                act.load_authorization_artifact(path)


class KillSwitchTests(unittest.TestCase):
    def test_stage_c_always_false(self) -> None:
        state = act.stage_b_kill_switch_state()
        self.assertTrue(state.stage_b_activation_controls_implemented)
        self.assertFalse(state.stage_c_live_execution_authorized)

    def test_kill_switch_takes_no_arguments(self) -> None:
        import inspect

        signature = inspect.signature(act.stage_b_kill_switch_state)
        self.assertEqual(0, len(signature.parameters))


class BoundedPollingConfigTests(unittest.TestCase):
    def test_definition_only_values(self) -> None:
        config = act.STAGE_B_POLLING_CONFIG
        self.assertEqual(12, config.max_polling_attempts)
        self.assertEqual(60, config.min_polling_interval_seconds)
        self.assertEqual(0, config.automatic_retries)
        self.assertFalse(config.automatic_resubmission)

    def test_no_polling_function_exists_in_this_module(self) -> None:
        # Regression guard: this module must never grow a function that
        # actually sleeps/polls -- only the config dataclass above.
        forbidden_names = {"poll", "poll_batch", "wait_for_batch", "sleep"}
        exported = set(dir(act))
        self.assertEqual(set(), forbidden_names & exported)


class PreflightRecordTests(unittest.TestCase):
    def test_build_preflight_record_is_always_unauthorized(self) -> None:
        manifest = act.load_pricing_manifest()
        requests = [_make_request("r1", max_output_tokens=100)]
        envelope = act.enforce_request_envelope(requests, input_byte_count=200)
        estimate = act.estimate_cost(
            envelope.input_byte_count, envelope.total_max_output_tokens
        )
        record = act.build_preflight_record(
            task_id="task-1",
            authorization_id=None,
            canonical_commit_sha="81b1baf9da5363ef088fe236de93d6cd3713b659",
            activation_commit_sha="unknown",
            endpoint=act.STAGE_B_ENDPOINT,
            completion_window="24h",
            envelope=envelope,
            pricing_manifest=manifest,
            cost_estimate=estimate,
            input_jsonl_sha256="deadbeef",
            credential_present=True,
        )
        self.assertFalse(record.execution_authorized)
        self.assertFalse(record.migration_trigger_5_crossed)
        self.assertFalse(record.credential_value_logged)
        self.assertEqual(0, record.automatic_retries)
        self.assertFalse(record.automatic_resubmission)
        self.assertIsNone(record.input_file_id)
        self.assertIsNone(record.batch_id)
        self.assertIsNone(record.output_file_id)
        self.assertIsNone(record.error_file_id)
        self.assertIsNone(record.provider_request_id)
        self.assertIsNone(record.actual_token_usage)
        self.assertIsNone(record.actual_cost)
        payload = record.to_dict()
        self.assertEqual(record.task_id, payload["task_id"])


class NoNetworkImportTests(unittest.TestCase):
    def test_activation_module_does_not_import_openai(self) -> None:
        import sys

        self.assertNotIn("openai", sys.modules)

    def test_activation_module_imports_no_socket_usage_symbols(self) -> None:
        # Sanity check that this module's own namespace never binds a name
        # that suggests direct socket/network usage.
        self.assertNotIn("socket", dir(act))
        self.assertNotIn("requests", dir(act))
        self.assertNotIn("urllib", dir(act))
        self.assertNotIn("http", dir(act))


if __name__ == "__main__":
    unittest.main()
