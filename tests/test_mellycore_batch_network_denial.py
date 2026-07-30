"""Explicit network-denial coverage for the Batch foundation.

Two things are proven here: first, that the ``no_network`` fixture itself
actually fails a test the instant a socket connection is attempted (so it is
not a fixture that silently does nothing); second, that a full local
CLI workflow -- including a deliberately blocked live command -- completes
entirely without tripping it.
"""

from __future__ import annotations

import json
import socket
import tempfile
import unittest
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from unittest import mock

from scripts.mellycore_batch.activation import STAGE_B_MODEL
from scripts.mellycore_batch.cli import main
from scripts.mellycore_batch.models import EXIT_LIVE_BLOCKED, EXIT_OK
from tests.mellycore_batch_fixtures import make_manifest_dict, make_request, no_network


def _run(argv):
    stdout = StringIO()
    with mock.patch("sys.stdout", stdout):
        code = main(argv)
    return code, stdout.getvalue()


class NoNetworkFixtureSelfTest(unittest.TestCase):
    def test_fixture_raises_on_real_connect_attempt(self) -> None:
        with no_network():
            with self.assertRaises(AssertionError):
                socket.create_connection(("example.invalid", 80), timeout=1)

    def test_fixture_raises_on_raw_socket_connect(self) -> None:
        with no_network():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                with self.assertRaises(AssertionError):
                    sock.connect(("example.invalid", 80))


class FullLocalWorkflowUnderNetworkDenialTests(unittest.TestCase):
    def test_build_validate_inspect_summarize_plan_and_blocked_submit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "manifest.json"
            manifest_path.write_text(
                json.dumps(make_manifest_dict(output_dir=str(root))), encoding="utf-8"
            )

            with no_network():
                code, out = _run(["build", "--manifest", str(manifest_path), "--json"])
                self.assertEqual(EXIT_OK, code)
                jsonl_path = json.loads(out)["path"]

                code, _ = _run(["validate", "--jsonl", jsonl_path, "--json"])
                self.assertEqual(EXIT_OK, code)

                code, _ = _run(["inspect", "--jsonl", jsonl_path, "--json"])
                self.assertEqual(EXIT_OK, code)

                code, _ = _run(
                    [
                        "plan-live",
                        "--manifest",
                        str(manifest_path),
                        "--jsonl",
                        jsonl_path,
                        "--json",
                    ]
                )
                self.assertEqual(EXIT_OK, code)

                code, _ = _run(["submit", "--execute", "--json"])
                self.assertEqual(EXIT_LIVE_BLOCKED, code)


class ActivationPreflightUnderNetworkDenialTests(unittest.TestCase):
    def test_activation_preflight_completes_with_no_network_and_no_sdk_import(
        self,
    ) -> None:
        import sys

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest_path = root / "manifest.json"
            requests = [
                make_request(
                    "r1", model=STAGE_B_MODEL, extra_body={"max_output_tokens": 10}
                )
            ]
            manifest_path.write_text(
                json.dumps(make_manifest_dict(requests=requests, output_dir=str(root))),
                encoding="utf-8",
            )

            with mock.patch(
                "scripts.mellycore_batch.cli._trusted_utc_now",
                return_value=datetime(2026, 7, 29, tzinfo=timezone.utc),
            ):
                with no_network():
                    code, out = _run(
                        [
                            "activation-preflight",
                            "--manifest",
                            str(manifest_path),
                            "--json",
                        ]
                    )
            self.assertEqual(EXIT_OK, code)
            payload = json.loads(out)
            self.assertFalse(payload["execution_authorized"])
            self.assertFalse(payload["migration_trigger_5_crossed"])
        self.assertNotIn("openai", sys.modules)


if __name__ == "__main__":
    unittest.main()
