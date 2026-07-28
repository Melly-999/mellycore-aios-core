"""Tests for the Batch foundation CLI.

Covers both halves of the contract: local commands must fully work and never
touch the network, and provider-backed commands must be blocked no matter
what flags or environment variables are supplied.
"""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from io import StringIO
from pathlib import Path
from unittest import mock

from scripts.mellycore_batch.cli import main
from scripts.mellycore_batch.models import EXIT_INVALID, EXIT_LIVE_BLOCKED, EXIT_OK
from tests.mellycore_batch_fixtures import make_manifest_dict, no_network


def _run(argv):
    stdout = StringIO()
    with mock.patch("sys.stdout", stdout):
        code = main(argv)
    return code, stdout.getvalue()


class HelpTests(unittest.TestCase):
    def test_help_exits_cleanly_with_no_command(self) -> None:
        code, _ = _run([])
        self.assertEqual(EXIT_INVALID, code)


class LocalCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.manifest_path = self.root / "manifest.json"
        self.manifest_path.write_text(json.dumps(make_manifest_dict(output_dir=str(self.root))), encoding="utf-8")

    def test_build_writes_deterministic_jsonl(self) -> None:
        with no_network():
            code, out = _run(["build", "--manifest", str(self.manifest_path), "--json"])
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertEqual(2, payload["request_count"])
        self.assertTrue(Path(payload["path"]).exists())

    def test_build_refuses_overwrite_without_flag(self) -> None:
        with no_network():
            _run(["build", "--manifest", str(self.manifest_path), "--json"])
            code, out = _run(["build", "--manifest", str(self.manifest_path), "--json"])
        self.assertEqual(EXIT_INVALID, code)

    def test_validate_manifest(self) -> None:
        with no_network():
            code, out = _run(["validate", "--manifest", str(self.manifest_path), "--json"])
        self.assertEqual(EXIT_OK, code)
        self.assertTrue(json.loads(out)["valid"])

    def test_validate_jsonl_reports_findings(self) -> None:
        bad = self.root / "bad.jsonl"
        bad.write_text("{not valid json\n", encoding="utf-8")
        with no_network():
            code, out = _run(["validate", "--jsonl", str(bad), "--json"])
        self.assertEqual(EXIT_INVALID, code)
        self.assertFalse(json.loads(out)["valid"])

    def test_inspect_reports_hash_and_size(self) -> None:
        with no_network():
            _run(["build", "--manifest", str(self.manifest_path), "--json"])
            jsonl_path = self.root / "batch-task-1.jsonl"
            code, out = _run(["inspect", "--jsonl", str(jsonl_path), "--json"])
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertEqual(64, len(payload["sha256"]))

    def test_summarize_parses_local_result_file(self) -> None:
        output_file = self.root / "out.jsonl"
        output_file.write_text(
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
        with no_network():
            code, out = _run(
                [
                    "summarize",
                    "--task-id",
                    "t1",
                    "--output-file",
                    str(output_file),
                    "--json",
                ]
            )
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertEqual(1, payload["completed_count"])
        self.assertFalse(payload["live_connection_authorized"])

    def test_plan_live_reports_execution_not_allowed(self) -> None:
        with no_network():
            code, out = _run(["plan-live", "--manifest", str(self.manifest_path), "--json"])
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertFalse(payload["execution_allowed"])
        self.assertFalse(payload["live_connection_policy"]["allowed"])

    def test_plan_live_never_prints_env_var_value(self) -> None:
        fake_key = "TEST-CREDENTIAL-SHOULD-NEVER-APPEAR-ANYWHERE-IN-OUTPUT"
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": fake_key}, clear=False):
            with no_network():
                code, out = _run(["plan-live", "--manifest", str(self.manifest_path), "--json"])
        self.assertEqual(EXIT_OK, code)
        self.assertNotIn(fake_key, out)
        payload = json.loads(out)
        self.assertTrue(payload["credentials_detected"])


class BlockedCommandTests(unittest.TestCase):
    """Every provider-backed command must be blocked, unconditionally."""

    def _assert_blocked(self, argv) -> None:
        with no_network():
            code, out = _run(argv + ["--json"])
        self.assertEqual(EXIT_LIVE_BLOCKED, code)
        payload = json.loads(out)
        self.assertEqual("LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5", payload["error"])
        self.assertFalse(payload["execution_allowed"])

    def test_submit_blocked_with_no_credentials(self) -> None:
        self._assert_blocked(["submit"])

    def test_submit_blocked_with_fake_key_and_execute_flag(self) -> None:
        with mock.patch.dict(
            os.environ,
            {"OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE", "MELLYCORE_ALLOW_LIVE_BATCH": "1"},
            clear=False,
        ):
            self._assert_blocked(["submit", "--execute"])

    def test_status_blocked(self) -> None:
        self._assert_blocked(["status"])

    def test_list_blocked(self) -> None:
        self._assert_blocked(["list"])

    def test_download_blocked(self) -> None:
        self._assert_blocked(["download"])

    def test_cancel_blocked(self) -> None:
        self._assert_blocked(["cancel"])

    def test_provider_never_constructed_for_blocked_command(self) -> None:
        with mock.patch(
            "scripts.mellycore_batch.openai_provider.OpenAIBatchProvider.__init__"
        ) as mocked_init:
            with mock.patch.dict(
                os.environ,
                {"OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE", "MELLYCORE_ALLOW_LIVE_BATCH": "1"},
                clear=False,
            ):
                with no_network():
                    code, _ = _run(["submit", "--execute", "--json"])
        self.assertEqual(EXIT_LIVE_BLOCKED, code)
        mocked_init.assert_not_called()


if __name__ == "__main__":
    unittest.main()
