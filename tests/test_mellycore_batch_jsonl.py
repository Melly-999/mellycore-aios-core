"""Tests for deterministic JSONL generation and streaming validation.

All I/O happens inside a temporary directory; nothing touches the real
repository tree.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.mellycore_batch.jsonl import (
    build_jsonl,
    iter_validate_jsonl_file,
    render_jsonl_bytes,
    sha256_of_file,
)
from scripts.mellycore_batch.manifest import parse_manifest_dict
from scripts.mellycore_batch.models import BatchRequest, InvalidInputError
from tests.mellycore_batch_fixtures import make_manifest_dict, make_request


class DeterminismTests(unittest.TestCase):
    def test_byte_identical_regeneration(self) -> None:
        requests = [
            BatchRequest("a", "POST", "/v1/responses", {"model": "m", "input": "x"}),
            BatchRequest("b", "POST", "/v1/responses", {"model": "m", "input": "y"}),
        ]
        first = render_jsonl_bytes(requests)
        second = render_jsonl_bytes(requests)
        self.assertEqual(first, second)

    def test_final_newline_present(self) -> None:
        requests = [BatchRequest("a", "POST", "/v1/responses", {"model": "m", "input": "x"})]
        payload = render_jsonl_bytes(requests)
        self.assertTrue(payload.endswith(b"\n"))

    def test_one_object_per_line(self) -> None:
        requests = [
            BatchRequest("a", "POST", "/v1/responses", {"model": "m", "input": "x"}),
            BatchRequest("b", "POST", "/v1/responses", {"model": "m", "input": "y"}),
        ]
        payload = render_jsonl_bytes(requests)
        lines = payload.decode("utf-8").strip("\n").split("\n")
        self.assertEqual(2, len(lines))

    def test_request_order_preserved(self) -> None:
        requests = [
            BatchRequest("z", "POST", "/v1/responses", {"model": "m", "input": "x"}),
            BatchRequest("a", "POST", "/v1/responses", {"model": "m", "input": "y"}),
        ]
        payload = render_jsonl_bytes(requests)
        lines = payload.decode("utf-8").strip("\n").split("\n")
        self.assertIn('"custom_id": "z"', lines[0])
        self.assertIn('"custom_id": "a"', lines[1])

    def test_empty_collection_produces_empty_bytes(self) -> None:
        self.assertEqual(b"", render_jsonl_bytes([]))


class BuildJsonlTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def test_build_writes_file_and_reports_summary(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root)))
        summary = build_jsonl(manifest)
        self.assertTrue(Path(summary.path).exists())
        self.assertEqual(2, summary.request_count)
        self.assertEqual(64, len(summary.sha256))
        self.assertGreater(summary.byte_size, 0)

    def test_sha256_stable_across_regeneration(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="t1", output_dir=str(self.root)))
        first = build_jsonl(manifest, output_path=self.root / "one.jsonl")
        second = build_jsonl(manifest, output_path=self.root / "two.jsonl")
        self.assertEqual(first.sha256, second.sha256)

    def test_refuses_overwrite_by_default(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root)))
        output_path = self.root / "out.jsonl"
        build_jsonl(manifest, output_path=output_path)
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest, output_path=output_path)

    def test_overwrite_flag_allows_replace(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root), overwrite=True))
        output_path = self.root / "out.jsonl"
        build_jsonl(manifest, output_path=output_path)
        build_jsonl(manifest, output_path=output_path)  # must not raise

    def test_request_count_limit_enforced(self) -> None:
        requests = [make_request("req-{}".format(i)) for i in range(3)]
        manifest = parse_manifest_dict(make_manifest_dict(requests=requests, output_dir=str(self.root)))
        object.__setattr__(manifest, "requests", manifest.requests)  # sanity: still a tuple
        # Patch the limit locally via a manifest with an inflated request count
        # is impractical without touching the real limit constant, so instead
        # verify the check fires using a monkeypatched limit.
        import scripts.mellycore_batch.jsonl as jsonl_module

        original_limit = jsonl_module.MAX_REQUESTS_PER_BATCH
        jsonl_module.MAX_REQUESTS_PER_BATCH = 2
        try:
            with self.assertRaises(InvalidInputError):
                build_jsonl(manifest)
        finally:
            jsonl_module.MAX_REQUESTS_PER_BATCH = original_limit

    def test_file_size_limit_enforced(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root)))
        import scripts.mellycore_batch.jsonl as jsonl_module

        original_limit = jsonl_module.MAX_INPUT_FILE_SIZE_BYTES
        jsonl_module.MAX_INPUT_FILE_SIZE_BYTES = 4
        try:
            with self.assertRaises(InvalidInputError):
                build_jsonl(manifest)
        finally:
            jsonl_module.MAX_INPUT_FILE_SIZE_BYTES = original_limit

    def test_sha256_of_file_matches_hashlib(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root)))
        summary = build_jsonl(manifest)
        self.assertEqual(summary.sha256, sha256_of_file(Path(summary.path)))


class StreamingValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def _write(self, name: str, lines) -> Path:
        path = self.root / name
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path

    def test_valid_file_has_no_findings(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root)))
        summary = build_jsonl(manifest)
        findings = list(iter_validate_jsonl_file(Path(summary.path)))
        self.assertEqual([], findings)

    def test_duplicate_custom_id_detected_streaming(self) -> None:
        path = self._write(
            "dup.jsonl",
            [
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", "body": {}}',
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", "body": {}}',
            ],
        )
        findings = list(iter_validate_jsonl_file(path))
        codes = {f["code"] for f in findings}
        self.assertIn("duplicate_custom_id", codes)

    def test_malformed_json_detected_streaming(self) -> None:
        good_line = '{"custom_id": "a", "method": "POST", "url": "/v1/responses", "body": {}}'
        path = self._write("bad.jsonl", ["{not json", good_line])
        findings = list(iter_validate_jsonl_file(path))
        codes = {f["code"] for f in findings}
        self.assertIn("malformed_json", codes)

    def test_unsupported_method_detected_streaming(self) -> None:
        path = self._write(
            "method.jsonl",
            ['{"custom_id": "a", "method": "GET", "url": "/v1/responses", "body": {}}'],
        )
        findings = list(iter_validate_jsonl_file(path))
        codes = {f["code"] for f in findings}
        self.assertIn("unsupported_method", codes)

    def test_safe_request_has_no_findings(self) -> None:
        path = self._write(
            "safe.jsonl",
            [
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", '
                '"body": {"model": "m", "input": "hello"}}'
            ],
        )
        self.assertEqual([], list(iter_validate_jsonl_file(path)))

    def test_stream_true_rejected_in_raw_body(self) -> None:
        path = self._write(
            "stream.jsonl",
            [
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", '
                '"body": {"model": "m", "input": "x", "stream": true}}'
            ],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual([1], [f["line"] for f in findings])
        self.assertEqual("invalid_body", findings[0]["code"])

    def test_api_key_field_rejected_in_raw_body(self) -> None:
        fake_value = "TEST-CREDENTIAL-NOT-REAL-VALUE"
        path = self._write(
            "cred.jsonl",
            [
                '{{"custom_id": "a", "method": "POST", "url": "/v1/responses", '
                '"body": {{"model": "m", "input": "x", "api_key": "{}"}}}}'.format(fake_value)
            ],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual(1, len(findings))
        self.assertEqual("invalid_body", findings[0]["code"])
        self.assertNotIn(fake_value, findings[0]["message"])

    def test_nested_credential_field_rejected_in_raw_body(self) -> None:
        path = self._write(
            "nested-cred.jsonl",
            [
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", '
                '"body": {"model": "m", "input": "x", '
                '"metadata": {"headers": [{"authorization": "x"}]}}}'
            ],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual(["invalid_body"], [f["code"] for f in findings])

    def test_missing_model_rejected_in_raw_body(self) -> None:
        path = self._write(
            "no-model.jsonl",
            ['{"custom_id": "a", "method": "POST", "url": "/v1/responses", "body": {"input": "x"}}'],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual(["invalid_body"], [f["code"] for f in findings])

    def test_missing_input_rejected_in_raw_body(self) -> None:
        path = self._write(
            "no-input.jsonl",
            ['{"custom_id": "a", "method": "POST", "url": "/v1/responses", "body": {"model": "m"}}'],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual(["invalid_body"], [f["code"] for f in findings])

    def test_external_url_rejected_in_raw_body(self) -> None:
        path = self._write(
            "url.jsonl",
            [
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", '
                '"body": {"model": "m", "input": "see https://evil.example.com/callback"}}'
            ],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual(["invalid_body"], [f["code"] for f in findings])

    def test_body_not_checked_when_custom_id_already_invalid(self) -> None:
        # A structurally broken line reports only its structural finding;
        # it must not also be double-reported for body issues.
        path = self._write(
            "missing-id.jsonl",
            ['{"method": "POST", "url": "/v1/responses", "body": {"stream": true}}'],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual(["missing_custom_id"], [f["code"] for f in findings])

    def test_line_numbers_correct_for_body_findings(self) -> None:
        path = self._write(
            "lines.jsonl",
            [
                '{"custom_id": "a", "method": "POST", "url": "/v1/responses", '
                '"body": {"model": "m", "input": "ok"}}',
                '{"custom_id": "b", "method": "POST", "url": "/v1/responses", '
                '"body": {"model": "m", "input": "x", "stream": true}}',
            ],
        )
        findings = list(iter_validate_jsonl_file(path))
        self.assertEqual([2], [f["line"] for f in findings])


class BuildJsonlPathSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def test_safe_task_id_stays_under_output_dir(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="safe-task_1", output_dir=str(self.root)))
        summary = build_jsonl(manifest)
        resolved_root = self.root.resolve()
        self.assertEqual(resolved_root, Path(summary.path).resolve().parent)

    def test_posix_style_traversal_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="../escape", output_dir=str(self.root)))
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_windows_style_traversal_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="..\\escape", output_dir=str(self.root)))
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_posix_absolute_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="/absolute/path", output_dir=str(self.root)))
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_windows_drive_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(
            make_manifest_dict(task_id="C:\\absolute\\path", output_dir=str(self.root))
        )
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_separator_containing_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="has/slash", output_dir=str(self.root)))
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_dot_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id=".", output_dir=str(self.root)))
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_dotdot_task_id_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(task_id="..", output_dir=str(self.root)))
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)

    def test_explicit_output_path_bypasses_task_id_charset_rule(self) -> None:
        # An explicit output_path is caller-controlled and pre-existing
        # behavior for it is unchanged -- only the *derived default* path is
        # subject to the task_id safety rule.
        manifest = parse_manifest_dict(make_manifest_dict(task_id="batch-task-1", output_dir=str(self.root)))
        summary = build_jsonl(manifest, output_path=self.root / "custom-name.jsonl")
        self.assertTrue(Path(summary.path).exists())


class BuildJsonlCompletionWindowTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)

    def test_supported_completion_window_accepted(self) -> None:
        manifest = parse_manifest_dict(
            make_manifest_dict(output_dir=str(self.root), completion_window="24h")
        )
        build_jsonl(manifest)  # must not raise

    def test_unsupported_completion_window_rejected_by_build(self) -> None:
        manifest = parse_manifest_dict(
            make_manifest_dict(output_dir=str(self.root), completion_window="1h")
        )
        with self.assertRaises(InvalidInputError):
            build_jsonl(manifest)


if __name__ == "__main__":
    unittest.main()
