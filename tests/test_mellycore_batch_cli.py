"""Tests for the Batch foundation CLI.

Covers both halves of the contract: local commands must fully work and never
touch the network, and provider-backed commands must be blocked no matter
what flags or environment variables are supplied.
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from datetime import datetime, timezone
from io import StringIO
from pathlib import Path
from unittest import mock

from scripts.mellycore_batch import cli as batch_cli
from scripts.mellycore_batch.activation import STAGE_B_MODEL
from scripts.mellycore_batch.cli import RepositoryIdentity, main
from scripts.mellycore_batch.models import (
    EXIT_INVALID,
    EXIT_LIVE_BLOCKED,
    EXIT_OK,
    InvalidInputError,
)
from tests.mellycore_batch_fixtures import make_manifest_dict, make_request, no_network


_TRUSTED_NOW = datetime(2026, 7, 29, tzinfo=timezone.utc)
_CANONICAL_BASE_SHA = "81b1baf9da5363ef088fe236de93d6cd3713b659"
_ACTIVATION_SHA = "1" * 40
_REPOSITORY_IDENTITY = RepositoryIdentity(
    repository_root=Path("source-derived-repository"),
    canonical_base_sha=_CANONICAL_BASE_SHA,
    activation_commit_sha=_ACTIVATION_SHA,
    canonical_remote_url="https://github.com/Melly-999/mellycore-aios-core.git",
)


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
        clock_patcher = mock.patch.object(
            batch_cli, "_trusted_utc_now", return_value=_TRUSTED_NOW
        )
        self.trusted_clock = clock_patcher.start()
        self.addCleanup(clock_patcher.stop)
        identity_patcher = mock.patch.object(
            batch_cli,
            "_resolve_repository_identity",
            return_value=_REPOSITORY_IDENTITY,
        )
        self.repository_identity = identity_patcher.start()
        self.addCleanup(identity_patcher.stop)
        self.root = Path(self._tmp.name)
        self.manifest_path = self.root / "stageb_manifest.json"
        self.manifest_path.write_text(
            json.dumps(_stage_b_manifest_dict(output_dir=str(self.root))),
            encoding="utf-8",
        )

    def _write_authorization(self, **overrides) -> Path:
        artifact = {
            "schema_version": 1,
            "authorization_id": "auth-cli-001",
            "task_id": "stageb-task-1",
            "issued_at": "2026-07-29T00:00:00Z",
            "expires_at": "2026-07-29T00:10:00Z",
            "canonical_base_sha": _CANONICAL_BASE_SHA,
            "activation_commit_sha": _ACTIVATION_SHA,
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
        artifact.update(overrides)
        auth_path = self.root / "authorization.json"
        auth_path.write_text(json.dumps(artifact), encoding="utf-8")
        return auth_path

    def test_valid_manifest_preflight_passes_and_reports_unauthorized(self) -> None:
        with no_network():
            code, out = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
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
                    "--json",
                ]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_expired_pricing_evidence_rejected(self) -> None:
        self.trusted_clock.return_value = datetime(
            2030, 1, 1, tzinfo=timezone.utc
        )
        with no_network():
            code, _ = _run(
                ["activation-preflight", "--manifest", str(self.manifest_path), "--json"]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_exact_pricing_expiry_fails_closed(self) -> None:
        self.trusted_clock.return_value = datetime(
            2026, 8, 27, 22, 0, 34, tzinfo=timezone.utc
        )
        with no_network():
            code, _ = _run(
                ["activation-preflight", "--manifest", str(self.manifest_path), "--json"]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_removed_now_option_is_rejected_by_argparse(self) -> None:
        for raw_now in ("2020-01-01T00:00:00Z", "2030-01-01T00:00:00Z"):
            with self.subTest(raw_now=raw_now):
                with self.assertRaises(SystemExit) as raised:
                    with no_network():
                        _run(
                            [
                                "activation-preflight",
                                "--manifest",
                                str(self.manifest_path),
                                "--now",
                                raw_now,
                                "--json",
                            ]
                        )
                self.assertEqual(2, raised.exception.code)

    def test_preflight_help_exposes_no_clock_or_commit_override(self) -> None:
        stdout = StringIO()
        with self.assertRaises(SystemExit) as raised:
            with mock.patch("sys.stdout", stdout):
                main(["activation-preflight", "--help"])
        self.assertEqual(0, raised.exception.code)
        output = stdout.getvalue()
        self.assertNotIn("--now", output)
        self.assertNotIn("--canonical-commit-sha", output)
        self.assertNotIn("--activation-commit-sha", output)

    def test_removed_commit_options_are_rejected_by_argparse(self) -> None:
        for option, value in (
            ("--canonical-commit-sha", _CANONICAL_BASE_SHA),
            ("--activation-commit-sha", _ACTIVATION_SHA),
        ):
            with self.subTest(option=option):
                with self.assertRaises(SystemExit) as raised:
                    with no_network():
                        _run(
                            [
                                "activation-preflight",
                                "--manifest",
                                str(self.manifest_path),
                                option,
                                value,
                                "--json",
                            ]
                        )
                self.assertEqual(2, raised.exception.code)

    def test_never_prints_credential_value(self) -> None:
        fake_key = "TEST-CREDENTIAL-SHOULD-NEVER-APPEAR-IN-PREFLIGHT-OUTPUT"
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": fake_key}, clear=False):
            with no_network():
                code, out = _run(
                    [
                        "activation-preflight",
                        "--manifest",
                        str(self.manifest_path),
                        "--json",
                    ]
                )
        self.assertEqual(EXIT_OK, code)
        self.assertNotIn(fake_key, out)
        payload = json.loads(out)
        self.assertTrue(payload["credential_present"])
        self.assertFalse(payload["credential_value_logged"])

    def test_trusted_clock_sampled_once_and_shared_by_both_validators(self) -> None:
        auth_path = self._write_authorization()
        with mock.patch.object(
            batch_cli, "validate_pricing_evidence"
        ) as pricing_validator:
            with mock.patch.object(
                batch_cli, "validate_authorization_artifact"
            ) as authorization_validator:
                with no_network():
                    code, _ = _run(
                        [
                            "activation-preflight",
                            "--manifest",
                            str(self.manifest_path),
                            "--authorization",
                            str(auth_path),
                            "--json",
                        ]
                    )
        self.assertEqual(EXIT_OK, code)
        self.trusted_clock.assert_called_once_with()
        self.assertIs(_TRUSTED_NOW, pricing_validator.call_args.args[1])
        self.assertIs(_TRUSTED_NOW, authorization_validator.call_args.kwargs["now"])

    def test_authorization_exact_expiry_uses_trusted_clock(self) -> None:
        auth_path = self._write_authorization()
        self.trusted_clock.return_value = datetime(
            2026, 7, 29, 0, 10, tzinfo=timezone.utc
        )
        with no_network():
            code, _ = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
                    "--authorization",
                    str(auth_path),
                    "--json",
                ]
            )
        self.assertEqual(EXIT_INVALID, code)

    def test_artifact_cannot_redefine_derived_expected_sha(self) -> None:
        for override in (
            {"canonical_base_sha": "0" * 40},
            {"activation_commit_sha": "2" * 40},
        ):
            with self.subTest(override=override):
                auth_path = self._write_authorization(**override)
                with no_network():
                    code, _ = _run(
                        [
                            "activation-preflight",
                            "--manifest",
                            str(self.manifest_path),
                            "--authorization",
                            str(auth_path),
                            "--json",
                        ]
                    )
                self.assertEqual(EXIT_INVALID, code)

    def test_authorization_artifact_validated_but_never_consumed(self) -> None:
        auth_path = self._write_authorization()
        with no_network():
            code, out = _run(
                [
                    "activation-preflight",
                    "--manifest",
                    str(self.manifest_path),
                    "--authorization",
                    str(auth_path),
                    "--json",
                ]
            )
        self.assertEqual(EXIT_OK, code)
        payload = json.loads(out)
        self.assertEqual("auth-cli-001", payload["authorization_id"])
        self.assertEqual(_CANONICAL_BASE_SHA, payload["canonical_commit_sha"])
        self.assertEqual(_ACTIVATION_SHA, payload["activation_commit_sha"])
        self.assertEqual("local_git_repository", payload["commit_identity_source"])
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
                ]
            )
        self.assertNotIn("openai", sys.modules)


class RepositoryIdentityTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name).resolve()
        self.commands = []

    def _valid_git_result(self, repository_root, arguments, expect_output=True):
        self.commands.append((repository_root, list(arguments), expect_output))
        if arguments == ["rev-parse", "--show-toplevel"]:
            return str(self.root)
        if arguments == ["remote", "get-url", "clean-origin"]:
            return "https://github.com/Melly-999/mellycore-aios-core.git"
        if arguments == ["rev-parse", "--verify", "HEAD^{commit}"]:
            return _ACTIVATION_SHA
        if arguments == [
            "show-ref",
            "--verify",
            "--hash",
            "refs/remotes/clean-origin/main",
        ]:
            return _CANONICAL_BASE_SHA
        if arguments == [
            "merge-base",
            "HEAD",
            "refs/remotes/clean-origin/main",
        ]:
            return _CANONICAL_BASE_SHA
        if arguments == [
            "merge-base",
            "--is-ancestor",
            _CANONICAL_BASE_SHA,
            "HEAD",
        ]:
            return ""
        self.fail("unexpected Git arguments: {!r}".format(arguments))

    def _resolve(self):
        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=self._valid_git_result
            ):
                return batch_cli._resolve_repository_identity()

    def test_valid_local_repository_identity_succeeds(self) -> None:
        identity = self._resolve()
        self.assertEqual(self.root, identity.repository_root)
        self.assertEqual(_CANONICAL_BASE_SHA, identity.canonical_base_sha)
        self.assertEqual(_ACTIVATION_SHA, identity.activation_commit_sha)

    def test_identity_resolution_is_independent_of_cwd(self) -> None:
        other_cwd = self.root / "unrelated-cwd"
        other_cwd.mkdir()
        with mock.patch("os.getcwd", return_value=str(other_cwd)):
            identity = self._resolve()
        self.assertEqual(self.root, identity.repository_root)
        self.assertTrue(all(call[0] == self.root for call in self.commands))

    def test_source_root_mismatch_fails_closed(self) -> None:
        other_root = self.root / "other-repository"
        other_root.mkdir()

        def mismatch(repository_root, arguments, expect_output=True):
            if arguments == ["rev-parse", "--show-toplevel"]:
                return str(other_root)
            return self._valid_git_result(repository_root, arguments, expect_output)

        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=mismatch
            ):
                with self.assertRaises(InvalidInputError):
                    batch_cli._resolve_repository_identity()

    def test_wrong_remote_url_fails_closed_without_echoing_it(self) -> None:
        secret_url = "https://credential-sentinel@example.invalid/repository.git"

        def wrong_remote(repository_root, arguments, expect_output=True):
            if arguments == ["remote", "get-url", "clean-origin"]:
                return secret_url
            return self._valid_git_result(repository_root, arguments, expect_output)

        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=wrong_remote
            ):
                with self.assertRaises(InvalidInputError) as raised:
                    batch_cli._resolve_repository_identity()
        self.assertNotIn(secret_url, str(raised.exception))

    def test_missing_clean_origin_fails_closed(self) -> None:
        def missing_remote(repository_root, arguments, expect_output=True):
            if arguments == ["remote", "get-url", "clean-origin"]:
                raise InvalidInputError("missing canonical remote")
            return self._valid_git_result(repository_root, arguments, expect_output)

        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=missing_remote
            ):
                with self.assertRaises(InvalidInputError):
                    batch_cli._resolve_repository_identity()

    def test_missing_remote_tracking_main_fails_closed(self) -> None:
        def missing_main(repository_root, arguments, expect_output=True):
            if arguments[:2] == ["show-ref", "--verify"]:
                raise InvalidInputError("missing canonical tracking ref")
            return self._valid_git_result(repository_root, arguments, expect_output)

        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=missing_main
            ):
                with self.assertRaises(InvalidInputError):
                    batch_cli._resolve_repository_identity()

    def test_malformed_git_sha_fails_closed(self) -> None:
        def malformed_head(repository_root, arguments, expect_output=True):
            if arguments == ["rev-parse", "--verify", "HEAD^{commit}"]:
                return "ABC123"
            return self._valid_git_result(repository_root, arguments, expect_output)

        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=malformed_head
            ):
                with self.assertRaises(InvalidInputError):
                    batch_cli._resolve_repository_identity()

    def test_non_ancestor_merge_base_fails_closed(self) -> None:
        def non_ancestor(repository_root, arguments, expect_output=True):
            if arguments[:2] == ["merge-base", "--is-ancestor"]:
                raise InvalidInputError("canonical base is not an ancestor")
            return self._valid_git_result(repository_root, arguments, expect_output)

        with mock.patch.object(
            batch_cli, "_repository_root_from_source", return_value=self.root
        ):
            with mock.patch.object(
                batch_cli, "_run_trusted_git", side_effect=non_ancestor
            ):
                with self.assertRaises(InvalidInputError):
                    batch_cli._resolve_repository_identity()

    def test_git_control_environment_is_removed(self) -> None:
        injected = {
            "PATH": "trusted-path",
            "GIT_DIR": "redirect",
            "GIT_WORK_TREE": "redirect",
            "GIT_INDEX_FILE": "redirect",
            "GIT_OBJECT_DIRECTORY": "redirect",
            "GIT_ALTERNATE_OBJECT_DIRECTORIES": "redirect",
            "GIT_COMMON_DIR": "redirect",
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": "remote.clean-origin.url",
            "GIT_CONFIG_VALUE_0": "https://example.invalid/repository.git",
            "GIT_CONFIG_GLOBAL": "redirect",
        }
        with mock.patch.dict(os.environ, injected, clear=True):
            sanitized = batch_cli._sanitized_git_environment()
        self.assertEqual({"PATH": "trusted-path"}, sanitized)

    def test_clock_environment_cannot_override_utc_sampling(self) -> None:
        with mock.patch.dict(
            os.environ,
            {"SOURCE_DATE_EPOCH": "0", "TZ": "Pacific/Kiritimati"},
            clear=False,
        ):
            with mock.patch.object(batch_cli, "datetime") as datetime_provider:
                datetime_provider.now.return_value = _TRUSTED_NOW
                sampled = batch_cli._trusted_utc_now()
        self.assertIs(_TRUSTED_NOW, sampled)
        datetime_provider.now.assert_called_once_with(timezone.utc)

    def test_git_timeout_fails_closed(self) -> None:
        with mock.patch.object(
            batch_cli.subprocess,
            "run",
            side_effect=subprocess.TimeoutExpired("git", 5),
        ):
            with self.assertRaises(InvalidInputError):
                batch_cli._run_trusted_git(
                    self.root, ["rev-parse", "--show-toplevel"]
                )

    def test_git_command_failure_is_redacted(self) -> None:
        credential_sentinel = "credential-sentinel-must-not-leak"
        completed = subprocess.CompletedProcess(
            ["git"], 1, stdout="", stderr=credential_sentinel
        )
        with mock.patch.object(
            batch_cli.subprocess, "run", return_value=completed
        ):
            with self.assertRaises(InvalidInputError) as raised:
                batch_cli._run_trusted_git(
                    self.root, ["remote", "get-url", "clean-origin"]
                )
        self.assertNotIn(credential_sentinel, str(raised.exception))

    def test_git_subprocess_uses_arrays_sanitized_env_and_bounded_timeout(self) -> None:
        completed = subprocess.CompletedProcess(
            ["git"], 0, stdout=str(self.root), stderr=""
        )
        with mock.patch.dict(
            os.environ, {"GIT_DIR": "redirect", "PATH": "trusted-path"}, clear=True
        ):
            with mock.patch.object(
                batch_cli.subprocess, "run", return_value=completed
            ) as run:
                batch_cli._run_trusted_git(
                    self.root, ["rev-parse", "--show-toplevel"]
                )
        command = run.call_args.args[0]
        kwargs = run.call_args.kwargs
        self.assertIsInstance(command, list)
        self.assertFalse(kwargs["shell"])
        self.assertEqual(5, kwargs["timeout"])
        self.assertNotIn("GIT_DIR", kwargs["env"])
        self.assertEqual(str(self.root), kwargs["cwd"])

    def test_network_git_subcommands_are_refused(self) -> None:
        with mock.patch.object(batch_cli.subprocess, "run") as run:
            with self.assertRaises(InvalidInputError):
                batch_cli._run_trusted_git(self.root, ["fetch", "clean-origin"])
        run.assert_not_called()

    def test_identity_resolver_uses_no_network_git_command(self) -> None:
        self._resolve()
        used_subcommands = {arguments[0] for _, arguments, _ in self.commands}
        self.assertTrue(
            used_subcommands.isdisjoint(batch_cli._NETWORK_GIT_SUBCOMMANDS)
        )


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
