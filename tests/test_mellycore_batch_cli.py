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

from scripts.mellycore_batch.activation import STAGE_B_MODEL
from scripts.mellycore_batch.cli import main
from scripts.mellycore_batch.models import EXIT_INVALID, EXIT_LIVE_BLOCKED, EXIT_OK
from tests.mellycore_batch_fixtures import make_manifest_dict, make_request, no_network


def _stage_b_manifest_dict(
    task_id="stageb-task-1", output_dir=None, request_count=1, max_output_tokens=100
):
    requests = [
        make_request(
            "r{}".format(i),
            model=STAGE_B_MODEL,
            extra_body={"max_output_tokens": max_output_tokens},
        )
        for i in range(1, request_count + 1)
    ]
    return make_manifest_dict(task_id=task_id, requests=requests, output_dir=output_dir)


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
        self.manifest_path.write_text(
            json.dumps(make_manifest_dict(output_dir=str(self.root))), encoding="utf-8"
        )

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
            code, out = _run(
                ["validate", "--manifest", str(self.manifest_path), "--json"]
            )
        self.assertEqual(EXIT_OK, code)
        self.assertTrue(json.loads(out)["valid"])

    def test_validate_jsonl_reports_findings(self) -> None:
        bad = self.root / "bad.jsonl"
        bad.write_text("{not valid json\n", encoding="utf-8")
        with no_network():
            code, out = _run(["validate", "--jsonl", str(bad), "--json"])
        self.assertEqual(EXIT_INVALID, code)
        self.assertFalse(json.loads(out)["valid"])

    def test_validate_jsonl_rejects_unsafe_body(self) -> None:
        fake_value = "TEST-CREDENTIAL-NOT-REAL-VALUE"
        unsafe = self.root / "unsafe.jsonl"
        unsafe.write_text(
            json.dumps(
                {
                    "custom_id": "a",
                    "method": "POST",
                    "url": "/v1/responses",
                    "body": {
                        "model": "m",
                        "input": "x",
                        "stream": True,
                        "api_key": fake_value,
                    },
                }
            )
            + "\n",
            encoding="utf-8",
        )
        with no_network():
            code, out = _run(["validate", "--jsonl", str(unsafe), "--json"])
        self.assertEqual(EXIT_INVALID, code)
        payload = json.loads(out)
        self.assertFalse(payload["valid"])
        self.assertTrue(payload["findings"])
        self.assertNotIn(fake_value, out)

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
            code, out = _run(
                ["plan-live", "--manifest", str(self.manifest_path), "--json"]
            )
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertFalse(payload["execution_allowed"])
        self.assertFalse(payload["live_connection_policy"]["allowed"])

    def test_plan_live_never_prints_env_var_value(self) -> None:
        fake_key = "TEST-CREDENTIAL-SHOULD-NEVER-APPEAR-ANYWHERE-IN-OUTPUT"
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": fake_key}, clear=False):
            with no_network():
                code, out = _run(
                    ["plan-live", "--manifest", str(self.manifest_path), "--json"]
                )
        self.assertEqual(EXIT_OK, code)
        self.assertNotIn(fake_key, out)
        payload = json.loads(out)
        self.assertTrue(payload["credentials_detected"])


class ActivationPreflightCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.manifest_path = self.root / "stageb_manifest.json"
        self.manifest_path.write_text(
            json.dumps(_stage_b_manifest_dict(output_dir=str(self.root))),
            encoding="utf-8",
        )

    def test_valid_manifest_preflight_passes_and_reports_unauthorized(self) -> None:
        with no_network():
            code, out = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
                    "--now",
                    "2026-07-29T00:00:00Z",
                    "--json",
                ]
            )
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertEqual(STAGE_B_MODEL, payload["model"])
        self.assertFalse(payload["execution_authorized"])
        self.assertFalse(payload["migration_trigger_5_crossed"])
        self.assertFalse(payload["automatic_resubmission"])
        self.assertEqual(0, payload["automatic_retries"])
        self.assertFalse(payload["credential_value_logged"])
        self.assertIsNone(payload["batch_id"])
        self.assertIsNone(payload["input_file_id"])

    def test_wrong_model_rejected(self) -> None:
        manifest_path = self.root / "wrong_model.json"
        manifest_dict = _stage_b_manifest_dict(
            task_id="wrong-model", output_dir=str(self.root)
        )
        manifest_dict["requests"] = [
            make_request("r1", model="gpt-4o", extra_body={"max_output_tokens": 10})
        ]
        manifest_path.write_text(json.dumps(manifest_dict), encoding="utf-8")
        with no_network():
            code, out = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(manifest_path),
                    "--now",
                    "2026-07-29T00:00:00Z",
                    "--json",
                ]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_too_many_requests_rejected(self) -> None:
        manifest_path = self.root / "too_many.json"
        manifest_path.write_text(
            json.dumps(
                _stage_b_manifest_dict(
                    task_id="too-many", output_dir=str(self.root), request_count=4
                )
            ),
            encoding="utf-8",
        )
        with no_network():
            code, _ = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(manifest_path),
                    "--now",
                    "2026-07-29T00:00:00Z",
                    "--json",
                ]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_missing_max_output_tokens_rejected(self) -> None:
        manifest_path = self.root / "no_mot.json"
        manifest_path.write_text(
            json.dumps(
                {
                    **make_manifest_dict(
                        task_id="no-mot",
                        requests=[make_request("r1", model=STAGE_B_MODEL)],
                        output_dir=str(self.root),
                    )
                }
            ),
            encoding="utf-8",
        )
        with no_network():
            code, _ = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(manifest_path),
                    "--now",
                    "2026-07-29T00:00:00Z",
                    "--json",
                ]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_expired_pricing_evidence_rejected(self) -> None:
        with no_network():
            code, _ = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
                    "--now",
                    "2030-01-01T00:00:00Z",
                    "--json",
                ]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_never_prints_credential_value(self) -> None:
        fake_key = "TEST-CREDENTIAL-SHOULD-NEVER-APPEAR-IN-PREFLIGHT-OUTPUT"
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": fake_key}, clear=False):
            with no_network():
                code, out = _run(
                    [
                        "activation-preflight",
                        "--manifest",
                        str(self.manifest_path),
                        "--now",
                        "2026-07-29T00:00:00Z",
                        "--json",
                    ]
                )
        self.assertEqual(EXIT_OK, code)
        self.assertNotIn(fake_key, out)
        payload = json.loads(out)
        self.assertTrue(payload["credential_present"])
        self.assertFalse(payload["credential_value_logged"])

    def test_authorization_artifact_validated_but_never_consumed(self) -> None:
        auth_path = self.root / "authorization.json"
        auth_path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "authorization_id": "auth-cli-001",
                    "task_id": "stageb-task-1",
                    "issued_at": "2026-07-29T00:00:00Z",
                    "expires_at": "2026-08-05T00:00:00Z",
                    "canonical_base_sha": "81b1baf9da5363ef088fe236de93d6cd3713b659",
                    "activation_commit_sha": "1" * 40,
                    "provider": "openai",
                    "endpoint": "/v1/responses",
                    "model": STAGE_B_MODEL,
                    "maximum_cost": "0.01",
                    "maximum_requests": 3,
                    "maximum_input_bytes": 65536,
                    "maximum_output_tokens_per_request": 512,
                    "maximum_total_output_tokens": 1536,
                    "one_time_use": True,
                }
            ),
            encoding="utf-8",
        )
        with no_network():
            code, out = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
                    "--authorization",
                    str(auth_path),
                    "--canonical-commit-sha",
                    "81b1baf9da5363ef088fe236de93d6cd3713b659",
                    "--activation-commit-sha",
                    "1" * 40,
                    "--now",
                    "2026-07-29T00:00:00Z",
                    "--json",
                ]
            )
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertEqual("auth-cli-001", payload["authorization_id"])
        self.assertFalse(payload["execution_authorized"])
        from scripts.mellycore_batch.activation import default_authorization_ledger_dir

        self.assertFalse(
            (default_authorization_ledger_dir() / "auth-cli-001.consumed").exists()
        )

    def test_never_imports_openai_sdk(self) -> None:
        import sys

        with no_network():
            _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
                    "--now",
                    "2026-07-29T00:00:00Z",
                ]
            )
        self.assertNotIn("openai", sys.modules)


class BlockedCommandTests(unittest.TestCase):
    """Every provider-backed command must be blocked, unconditionally."""

    def _assert_blocked(self, argv) -> None:
        with no_network():
            code, out = _run(argv + ["--json"])
        self.assertEqual(EXIT_LIVE_BLOCKED, code)
        payload = json.loads(out)
        self.assertEqual(
            "LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5", payload["error"]
        )
        self.assertFalse(payload["execution_allowed"])

    def test_submit_blocked_with_no_credentials(self) -> None:
        self._assert_blocked(["submit"])

    def test_submit_blocked_with_fake_key_and_execute_flag(self) -> None:
        with mock.patch.dict(
            os.environ,
            {
                "OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE",
                "MELLYCORE_ALLOW_LIVE_BATCH": "1",
            },
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
                {
                    "OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE",
                    "MELLYCORE_ALLOW_LIVE_BATCH": "1",
                },
                clear=False,
            ):
                with no_network():
                    code, _ = _run(["submit", "--execute", "--json"])
        self.assertEqual(EXIT_LIVE_BLOCKED, code)
        mocked_init.assert_not_called()


if __name__ == "__main__":
    unittest.main()
