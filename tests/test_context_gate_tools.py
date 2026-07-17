"""CLI and record-shape tests for Context Gate Phases I1-I2."""

from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from context_gate_fixtures import candidate, canonical_bytes, canonical_record, record
from scripts.context_gate.cli import build_parser, main
from scripts.context_gate.models import (
    EXIT_INVALID,
    EXIT_OK,
    EXIT_REFUSED,
    deterministic_json_bytes,
    validate_record_shape,
)

ROOT = Path(__file__).resolve().parents[1]


class ContextSourceModelTests(unittest.TestCase):
    def test_valid_draft_record(self):
        self.assertEqual((), validate_record_shape(record()))

    def test_invalid_draft_record(self):
        invalid = record()
        del invalid["source_identity"]
        findings = validate_record_shape(invalid)
        self.assertIn("missing_field", {finding.code for finding in findings})

    def test_decided_record_requires_human_metadata(self):
        findings = validate_record_shape(record(decision="admitted"))
        self.assertIn("missing_decision_metadata", {finding.code for finding in findings})

    def test_all_seven_shipped_canonical_records_validate(self):
        records_dir = ROOT / "shared_context" / "context_provenance" / "records"
        paths = sorted(records_dir.glob("ctx-*.json"))
        self.assertEqual(7, len(paths))
        decisions = []
        for path in paths:
            with self.subTest(path=path.name):
                raw = path.read_bytes()
                data = json.loads(raw.decode("utf-8"))
                self.assertEqual((), validate_record_shape(data, raw_bytes=raw))
                decisions.append(data["decision"])
        self.assertEqual(6, decisions.count("admitted"))
        self.assertEqual(1, decisions.count("rejected"))

    def test_canonical_deterministic_serialization_passes(self):
        data = canonical_record()
        raw = canonical_bytes()
        self.assertEqual((), validate_record_shape(data, raw_bytes=raw))

    def test_canonical_non_deterministic_serialization_fails(self):
        data = canonical_record()
        raw = (json.dumps(data, indent=2, sort_keys=False) + "\n").encode("utf-8")
        findings = validate_record_shape(data, raw_bytes=raw)
        self.assertIn("non_deterministic_serialization", {finding.code for finding in findings})


class ContextGateCliTests(unittest.TestCase):
    def _write_json(self, directory: Path, name: str, payload) -> Path:
        path = directory / name
        path.write_bytes(deterministic_json_bytes(payload))
        return path

    def test_help_exposes_i1_and_i2_commands_only(self):
        parser = build_parser()
        help_text = parser.format_help()
        self.assertIn("preview", help_text)
        self.assertIn("validate-record", help_text)
        self.assertIn("apply", help_text)
        subcommands = next(
            action.choices
            for action in parser._actions
            if isinstance(action, __import__("argparse")._SubParsersAction)
        )
        # I3 (rebuild-index, audit) and I4 (dashboard) do not exist yet.
        self.assertEqual({"preview", "validate-record", "apply"}, set(subcommands))

    def test_no_command_is_exit_one_and_writes_nothing(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            exit_code = main([])
        self.assertEqual(EXIT_INVALID, exit_code)
        self.assertIn("usage:", out.getvalue())

    def test_validate_record_json_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_json(Path(tmp), "record.json", record())
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                exit_code = main(["validate-record", "--file", str(path), "--json"])
            payload = json.loads(out.getvalue())
            self.assertEqual(EXIT_OK, exit_code)
            self.assertTrue(payload["valid"])
            self.assertEqual(0, payload["writes_performed"])

    def test_validate_record_invalid_exit_one(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_json(Path(tmp), "record.json", {"source_id": "invalid"})
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                exit_code = main(["validate-record", "--file", str(path), "--json"])
            self.assertEqual(EXIT_INVALID, exit_code)
            self.assertFalse(json.loads(out.getvalue())["valid"])

    def test_preview_accept_exit_zero_and_no_files_written(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            manifest = self._write_json(
                directory,
                "batch.json",
                {"batch_id": "batch-cli-accept", "items": [candidate()]},
            )
            before = {path.name: path.read_bytes() for path in directory.iterdir()}
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                exit_code = main(["preview", "--batch", str(manifest), "--json"])
            after = {path.name: path.read_bytes() for path in directory.iterdir()}
            payload = json.loads(out.getvalue())
            self.assertEqual(EXIT_OK, exit_code)
            self.assertEqual(0, payload["writes_performed"])
            self.assertEqual(before, after)

    def test_preview_refusal_exit_two_and_output_is_aggregate_safe(self):
        synthetic = "sk-" + ("TEST" * 5)
        refused = candidate(
            source_identity="private candidate identity",
            claim="Synthetic fixture {}".format(synthetic),
        )
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self._write_json(
                Path(tmp),
                "batch.json",
                {"batch_id": "batch-cli-refuse", "items": [refused]},
            )
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                exit_code = main(["preview", "--batch", str(manifest), "--json"])
            rendered = out.getvalue()
            payload = json.loads(rendered)
            self.assertEqual(EXIT_REFUSED, exit_code)
            self.assertEqual(["field_level_secret"], payload["items"][0]["reason_codes"])
            self.assertNotIn(synthetic, rendered)
            self.assertNotIn("private candidate identity", rendered)
            self.assertNotIn("source_id", payload["items"][0])

    def test_preview_json_is_byte_deterministic_for_same_day(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = self._write_json(
                Path(tmp),
                "batch.json",
                {"batch_id": "batch-cli-deterministic", "items": [candidate()]},
            )
            outputs = []
            for _ in range(2):
                out = io.StringIO()
                with contextlib.redirect_stdout(out):
                    self.assertEqual(
                        EXIT_OK, main(["preview", "--batch", str(manifest), "--json"])
                    )
                outputs.append(out.getvalue())
            self.assertEqual(outputs[0], outputs[1])

    def test_malformed_manifest_is_exit_one_without_echoing_file_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            marker = "CONTENT_MUST_NOT_BE_ECHOED"
            path.write_text("{" + marker, encoding="utf-8")
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                exit_code = main(["preview", "--batch", str(path), "--json"])
            self.assertEqual(EXIT_INVALID, exit_code)
            self.assertNotIn(marker, err.getvalue())


if __name__ == "__main__":
    unittest.main()
