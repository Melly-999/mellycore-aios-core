"""Tests for manifest parsing and pre-flight validation."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.mellycore_batch.manifest import (
    load_manifest_file,
    parse_manifest_dict,
    validate_manifest,
)
from scripts.mellycore_batch.models import InvalidInputError
from tests.mellycore_batch_fixtures import make_manifest_dict, make_request


class ParseManifestTests(unittest.TestCase):
    def test_parses_valid_manifest(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict())
        self.assertEqual("batch-task-1", manifest.task_id)
        self.assertEqual(2, len(manifest.requests))

    def test_missing_task_id_rejected(self) -> None:
        data = make_manifest_dict()
        del data["task_id"]
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_requests_not_a_list_rejected(self) -> None:
        data = make_manifest_dict()
        data["requests"] = "not-a-list"
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_request_missing_field_rejected(self) -> None:
        data = make_manifest_dict(requests=[{"custom_id": "a"}])
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)


class OverwriteParsingTests(unittest.TestCase):
    def test_boolean_true_accepted(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = True
        manifest = parse_manifest_dict(data)
        self.assertIs(True, manifest.overwrite)

    def test_boolean_false_accepted(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = False
        manifest = parse_manifest_dict(data)
        self.assertIs(False, manifest.overwrite)

    def test_missing_value_defaults_false(self) -> None:
        data = make_manifest_dict()
        del data["overwrite"]
        manifest = parse_manifest_dict(data)
        self.assertIs(False, manifest.overwrite)

    def test_string_false_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = "false"
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_string_true_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = "true"
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_integer_one_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = 1
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_integer_zero_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = 0
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_null_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = None
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_list_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = []
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)

    def test_dict_rejected(self) -> None:
        data = make_manifest_dict()
        data["overwrite"] = {}
        with self.assertRaises(InvalidInputError):
            parse_manifest_dict(data)


class ValidateManifestTests(unittest.TestCase):
    def test_valid_manifest_passes(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict())
        validate_manifest(manifest)  # must not raise

    def test_unsupported_endpoint_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(endpoint="/v1/chat/completions"))
        with self.assertRaises(InvalidInputError):
            validate_manifest(manifest)

    def test_unsupported_completion_window_rejected(self) -> None:
        manifest = parse_manifest_dict(make_manifest_dict(completion_window="1h"))
        with self.assertRaises(InvalidInputError):
            validate_manifest(manifest)

    def test_mismatched_request_endpoint_rejected(self) -> None:
        data = make_manifest_dict(requests=[make_request("a", endpoint="/v1/responses")])
        data["requests"][0]["url"] = "/v1/other"
        manifest = parse_manifest_dict(data)
        with self.assertRaises(InvalidInputError):
            validate_manifest(manifest)

    def test_duplicate_ids_across_manifest_rejected(self) -> None:
        manifest = parse_manifest_dict(
            make_manifest_dict(requests=[make_request("dup"), make_request("dup")])
        )
        with self.assertRaises(InvalidInputError):
            validate_manifest(manifest)

    def test_request_count_limit_enforced(self) -> None:
        import scripts.mellycore_batch.manifest as manifest_module

        manifest = parse_manifest_dict(
            make_manifest_dict(requests=[make_request("a"), make_request("b"), make_request("c")])
        )
        original = manifest_module.MAX_REQUESTS_PER_BATCH
        manifest_module.MAX_REQUESTS_PER_BATCH = 2
        try:
            with self.assertRaises(InvalidInputError):
                validate_manifest(manifest)
        finally:
            manifest_module.MAX_REQUESTS_PER_BATCH = original

    def test_file_size_limit_enforced(self) -> None:
        import scripts.mellycore_batch.manifest as manifest_module

        manifest = parse_manifest_dict(make_manifest_dict())
        original = manifest_module.MAX_INPUT_FILE_SIZE_BYTES
        manifest_module.MAX_INPUT_FILE_SIZE_BYTES = 4
        try:
            with self.assertRaises(InvalidInputError):
                validate_manifest(manifest)
        finally:
            manifest_module.MAX_INPUT_FILE_SIZE_BYTES = original


class LoadManifestFileTests(unittest.TestCase):
    def test_loads_from_disk(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "manifest.json"
            path.write_text(json.dumps(make_manifest_dict()), encoding="utf-8")
            manifest = load_manifest_file(path)
            self.assertEqual("batch-task-1", manifest.task_id)

    def test_missing_file_raises_invalid_input(self) -> None:
        with self.assertRaises(InvalidInputError):
            load_manifest_file(Path("/nonexistent/manifest.json"))

    def test_invalid_json_raises_invalid_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(InvalidInputError):
                load_manifest_file(path)


if __name__ == "__main__":
    unittest.main()
