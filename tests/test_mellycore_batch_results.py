"""Tests for streaming result/error JSONL parsing and correlation."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.mellycore_batch.results import parse_result_files


def _line(custom_id, status_code=200, body=None, error=None, request_id="req-abc"):
    obj = {
        "id": "batch_req_{}".format(custom_id),
        "custom_id": custom_id,
        "response": None if error else {"status_code": status_code, "request_id": request_id, "body": body or {}},
        "error": error,
    }
    return json.dumps(obj)


class ResultParsingTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def _write(self, name, lines):
        path = self.root / name
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path

    def test_successful_result_parsed(self) -> None:
        output = self._write("out.jsonl", [_line("req-1", body={"output_text": "hi"})])
        result_set = parse_result_files(output_path=output)
        self.assertEqual(1, result_set.completed_count)
        self.assertEqual(0, result_set.failed_count)
        self.assertEqual("req-1", result_set.results[0].custom_id)
        self.assertEqual({"output_text": "hi"}, result_set.results[0].response_body)

    def test_failed_result_parsed(self) -> None:
        errors = self._write(
            "err.jsonl", [_line("req-2", error={"code": "rate_limit", "message": "slow down"})]
        )
        result_set = parse_result_files(error_path=errors)
        self.assertEqual(0, result_set.completed_count)
        self.assertEqual(1, result_set.failed_count)
        self.assertEqual("req-2", result_set.errors[0].custom_id)
        self.assertEqual("rate_limit", result_set.errors[0].error["code"])

    def test_mixed_output_and_error_files(self) -> None:
        output = self._write("out.jsonl", [_line("req-1")])
        errors = self._write("err.jsonl", [_line("req-2", error={"code": "x"})])
        result_set = parse_result_files(output_path=output, error_path=errors)
        self.assertEqual(1, result_set.completed_count)
        self.assertEqual(1, result_set.failed_count)

    def test_output_ordering_independent_of_input_order(self) -> None:
        output = self._write("out.jsonl", [_line("req-2"), _line("req-1")])
        result_set = parse_result_files(output_path=output, expected_custom_ids={"req-1", "req-2"})
        ids = {r.custom_id for r in result_set.results}
        self.assertEqual({"req-1", "req-2"}, ids)
        self.assertEqual((), result_set.missing_custom_ids)

    def test_missing_result_detected(self) -> None:
        output = self._write("out.jsonl", [_line("req-1")])
        result_set = parse_result_files(output_path=output, expected_custom_ids={"req-1", "req-2"})
        self.assertEqual(("req-2",), result_set.missing_custom_ids)

    def test_duplicate_result_detected(self) -> None:
        output = self._write("out.jsonl", [_line("req-1"), _line("req-1")])
        result_set = parse_result_files(output_path=output)
        self.assertEqual(("req-1",), result_set.duplicate_custom_ids)

    def test_malformed_json_line_reported_not_dropped(self) -> None:
        output = self._write("out.jsonl", ["{not valid json", _line("req-1")])
        result_set = parse_result_files(output_path=output)
        self.assertEqual(1, len(result_set.malformed_lines))
        self.assertEqual(1, result_set.malformed_lines[0].line_number)

    def test_missing_custom_id_reported_as_malformed(self) -> None:
        output = self._write("out.jsonl", [json.dumps({"id": "x", "response": {"status_code": 200, "body": {}}})])
        result_set = parse_result_files(output_path=output)
        self.assertEqual(1, len(result_set.malformed_lines))

    def test_token_usage_aggregated(self) -> None:
        output = self._write(
            "out.jsonl",
            [
                _line("req-1", body={"usage": {"input_tokens": 10, "output_tokens": 5, "total_tokens": 15}}),
                _line("req-2", body={"usage": {"input_tokens": 20, "output_tokens": 8, "total_tokens": 28}}),
            ],
        )
        result_set = parse_result_files(output_path=output)
        totals = result_set.total_tokens_by_kind()
        self.assertEqual(30, totals["input_tokens"])
        self.assertEqual(13, totals["output_tokens"])
        self.assertEqual(43, totals["total_tokens"])

    def test_token_usage_empty_when_none_reported(self) -> None:
        output = self._write("out.jsonl", [_line("req-1", body={"output_text": "no usage field"})])
        result_set = parse_result_files(output_path=output)
        self.assertEqual({}, result_set.total_tokens_by_kind())

    def test_request_and_response_ids_preserved(self) -> None:
        output = self._write("out.jsonl", [_line("req-1", request_id="req-xyz")])
        result_set = parse_result_files(output_path=output)
        self.assertEqual("req-xyz", result_set.results[0].request_id)
        self.assertEqual("batch_req_req-1", result_set.results[0].batch_request_id)

    def test_never_executes_response_body_content(self) -> None:
        # A malicious-looking body must remain inert data, never evaluated.
        output = self._write(
            "out.jsonl", [_line("req-1", body={"output_text": "__import__('os').system('echo pwned')"})]
        )
        result_set = parse_result_files(output_path=output)
        self.assertEqual(
            "__import__('os').system('echo pwned')", result_set.results[0].response_body["output_text"]
        )


if __name__ == "__main__":
    unittest.main()
