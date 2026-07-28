"""Tests for Run Ledger-compatible summary construction."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.mellycore_batch.results import parse_result_files
from scripts.mellycore_batch.summary import build_ledger_summary


class SummaryTests(unittest.TestCase):
    def test_summary_without_result_set_uses_none_honestly(self) -> None:
        summary = build_ledger_summary(
            task_id="t1",
            endpoint="/v1/responses",
            completion_window="24h",
            models=["m1"],
            request_count=2,
            status="planned",
        )
        data = summary.to_dict()
        self.assertIsNone(data["completed_count"])
        self.assertIsNone(data["failed_count"])
        self.assertIsNone(data["input_tokens"])
        self.assertEqual("1", data["schema_version"])

    def test_live_connection_authorized_always_false(self) -> None:
        summary = build_ledger_summary(
            task_id="t1", endpoint="/v1/responses", completion_window="24h", models=[], request_count=1, status="x"
        )
        self.assertFalse(summary.live_connection_authorized)
        self.assertIsNotNone(summary.blocking_policy)

    def test_summary_with_result_set_populates_counts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "out.jsonl"
            output.write_text(
                json.dumps(
                    {
                        "id": "batch_req_1",
                        "custom_id": "req-1",
                        "response": {"status_code": 200, "request_id": "r1", "body": {}},
                        "error": None,
                    }
                )
                + "\n",
                encoding="utf-8",
            )
            result_set = parse_result_files(output_path=output, expected_custom_ids={"req-1", "req-2"})
            summary = build_ledger_summary(
                task_id="t1",
                endpoint="/v1/responses",
                completion_window="24h",
                models=["m1"],
                request_count=2,
                status="completed",
                result_set=result_set,
            )
            self.assertEqual(1, summary.completed_count)
            self.assertEqual(0, summary.failed_count)
            self.assertEqual(1, summary.missing_count)
            self.assertEqual(0, summary.duplicate_count)

    def test_to_dict_serializable(self) -> None:
        summary = build_ledger_summary(
            task_id="t1", endpoint="/v1/responses", completion_window="24h", models=["m1"], request_count=1, status="x"
        )
        json.dumps(summary.to_dict())  # must not raise


if __name__ == "__main__":
    unittest.main()
