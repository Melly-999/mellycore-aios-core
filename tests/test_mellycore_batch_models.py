"""Tests for MellyCore Batch API domain models.

Pure in-memory construction only -- no files, no network.
"""

from __future__ import annotations

import unittest

from scripts.mellycore_batch.models import (
    BatchLedgerSummary,
    BatchManifest,
    BatchRequest,
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


class FixtureSanityTests(unittest.TestCase):
    def test_make_request_produces_official_shape(self) -> None:
        request = make_request("req-x")
        self.assertEqual({"custom_id", "method", "url", "body"}, set(request.keys()))
        self.assertEqual("POST", request["method"])
        self.assertEqual("/v1/responses", request["url"])


if __name__ == "__main__":
    unittest.main()
