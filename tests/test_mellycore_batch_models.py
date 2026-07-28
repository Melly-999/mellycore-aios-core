"""Tests for MellyCore Batch API domain models.

Pure in-memory construction only -- no files, no network.
"""

from __future__ import annotations

import unittest

from scripts.mellycore_batch.models import (
    BatchLedgerSummary,
    BatchManifest,
    BatchRequest,
    BatchRequestResult,
    BatchResultSet,
    LiveConnectionPolicy,
    MIGRATION_TRIGGER_5_LABEL,
)
from tests.mellycore_batch_fixtures import make_request


class BatchRequestTests(unittest.TestCase):
    def test_to_jsonl_dict_shape(self) -> None:
        request = BatchRequest(
            custom_id="req-1", method="POST", url="/v1/responses", body={"model": "m", "input": "hi"}
        )
        self.assertEqual(
            {"custom_id": "req-1", "method": "POST", "url": "/v1/responses", "body": {"model": "m", "input": "hi"}},
            request.to_jsonl_dict(),
        )


class BatchManifestTests(unittest.TestCase):
    def test_models_property_deduplicates_preserving_order(self) -> None:
        requests = (
            BatchRequest("a", "POST", "/v1/responses", {"model": "m1", "input": "x"}),
            BatchRequest("b", "POST", "/v1/responses", {"model": "m2", "input": "x"}),
            BatchRequest("c", "POST", "/v1/responses", {"model": "m1", "input": "x"}),
        )
        manifest = BatchManifest(task_id="t", endpoint="/v1/responses", requests=requests, output_dir=".")
        self.assertEqual(("m1", "m2"), manifest.models)

    def test_models_property_empty_when_no_requests(self) -> None:
        manifest = BatchManifest(task_id="t", endpoint="/v1/responses", requests=(), output_dir=".")
        self.assertEqual((), manifest.models)


class LiveConnectionPolicyTests(unittest.TestCase):
    def test_to_dict_round_trips_fields(self) -> None:
        policy = LiveConnectionPolicy(allowed=False, reason="x", blocking_trigger=MIGRATION_TRIGGER_5_LABEL)
        self.assertEqual(
            {"allowed": False, "reason": "x", "blocking_trigger": MIGRATION_TRIGGER_5_LABEL},
            policy.to_dict(),
        )


class BatchLedgerSummaryTests(unittest.TestCase):
    def test_to_dict_uses_none_honestly_for_unavailable_data(self) -> None:
        summary = BatchLedgerSummary(
            schema_version="1",
            task_id="t",
            batch_id=None,
            provider="openai",
            endpoint="/v1/responses",
            completion_window="24h",
            models=("m1",),
            created_at=None,
            started_at=None,
            completed_at=None,
            status="planned",
            request_count=2,
            completed_count=None,
            failed_count=None,
            missing_count=None,
            duplicate_count=None,
            input_tokens=None,
            cached_input_tokens=None,
            output_tokens=None,
            total_tokens=None,
            input_file_sha256=None,
            input_file_size=None,
            output_file_id=None,
            error_file_id=None,
            provider_request_ids=(),
            live_connection_authorized=False,
            blocking_policy="migration_trigger_5_first_live_provider_connection",
        )
        data = summary.to_dict()
        self.assertIsNone(data["batch_id"])
        self.assertIsNone(data["completed_count"])
        self.assertIsNone(data["input_tokens"])
        self.assertFalse(data["live_connection_authorized"])
        self.assertEqual(["m1"], data["models"])
        self.assertEqual([], data["provider_request_ids"])


def _result(custom_id: str, usage) -> BatchRequestResult:
    return BatchRequestResult(
        custom_id=custom_id,
        batch_request_id="req_{}".format(custom_id),
        status_code=200,
        request_id="r-{}".format(custom_id),
        response_body={},
        usage=usage,
    )


class TotalTokensByKindTests(unittest.TestCase):
    def test_fully_populated_usage_summed(self) -> None:
        result_set = BatchResultSet(
            results=(
                _result(
                    "a",
                    {"input_tokens": 10, "cached_input_tokens": 2, "output_tokens": 5, "total_tokens": 15},
                ),
            ),
            errors=(),
            duplicate_custom_ids=(),
            missing_custom_ids=(),
            malformed_lines=(),
        )
        totals = result_set.total_tokens_by_kind()
        self.assertEqual(
            {"input_tokens": 10, "cached_input_tokens": 2, "output_tokens": 5, "total_tokens": 15}, totals
        )

    def test_partial_usage_leaves_unreported_fields_absent(self) -> None:
        result_set = BatchResultSet(
            results=(_result("a", {"input_tokens": 10}),),
            errors=(),
            duplicate_custom_ids=(),
            missing_custom_ids=(),
            malformed_lines=(),
        )
        totals = result_set.total_tokens_by_kind()
        self.assertEqual({"input_tokens": 10}, totals)
        self.assertNotIn("output_tokens", totals)
        self.assertNotIn("cached_input_tokens", totals)
        self.assertNotIn("total_tokens", totals)

    def test_explicit_zero_is_preserved_as_reported(self) -> None:
        result_set = BatchResultSet(
            results=(_result("a", {"input_tokens": 10, "cached_input_tokens": 0}),),
            errors=(),
            duplicate_custom_ids=(),
            missing_custom_ids=(),
            malformed_lines=(),
        )
        totals = result_set.total_tokens_by_kind()
        self.assertIn("cached_input_tokens", totals)
        self.assertEqual(0, totals["cached_input_tokens"])

    def test_absent_usage_across_all_results_returns_empty(self) -> None:
        result_set = BatchResultSet(
            results=(_result("a", None), _result("b", {})),
            errors=(),
            duplicate_custom_ids=(),
            missing_custom_ids=(),
            malformed_lines=(),
        )
        self.assertEqual({}, result_set.total_tokens_by_kind())

    def test_mixed_results_partial_and_full_usage_not_fabricated(self) -> None:
        result_set = BatchResultSet(
            results=(
                _result("a", {"input_tokens": 10}),
                _result("b", {"input_tokens": 5, "output_tokens": 3}),
            ),
            errors=(),
            duplicate_custom_ids=(),
            missing_custom_ids=(),
            malformed_lines=(),
        )
        totals = result_set.total_tokens_by_kind()
        self.assertEqual(15, totals["input_tokens"])
        self.assertEqual(3, totals["output_tokens"])
        self.assertNotIn("cached_input_tokens", totals)
        self.assertNotIn("total_tokens", totals)


class FixtureSanityTests(unittest.TestCase):
    def test_make_request_produces_official_shape(self) -> None:
        request = make_request("req-x")
        self.assertEqual({"custom_id", "method", "url", "body"}, set(request.keys()))
        self.assertEqual("POST", request["method"])
        self.assertEqual("/v1/responses", request["url"])


if __name__ == "__main__":
    unittest.main()
