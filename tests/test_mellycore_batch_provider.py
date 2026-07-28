"""Tests for the provider boundary: the OpenAI adapter must never connect,
and the fake provider must support a full mocked lifecycle.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.mellycore_batch.jsonl import build_jsonl
from scripts.mellycore_batch.manifest import parse_manifest_dict
from scripts.mellycore_batch.models import LiveConnectionBlockedError
from scripts.mellycore_batch.openai_provider import OpenAIBatchProvider
from scripts.mellycore_batch.provider import BatchProvider
from tests.mellycore_batch_fixtures import (
    FakeBatchProvider,
    make_manifest_dict,
    no_network,
)


class OpenAIAdapterBlockedTests(unittest.TestCase):
    def test_construction_raises_without_credentials(self) -> None:
        with self.assertRaises(LiveConnectionBlockedError):
            OpenAIBatchProvider()

    def test_construction_raises_even_with_fake_api_key(self) -> None:
        placeholder = "TEST-CREDENTIAL-NOT-REAL-VALUE"
        with self.assertRaises(LiveConnectionBlockedError):
            OpenAIBatchProvider(api_key=placeholder)

    def test_adapter_satisfies_provider_protocol_shape(self) -> None:
        # Structural check only -- this does not construct the adapter.
        self.assertTrue(hasattr(OpenAIBatchProvider, "upload_input_file"))
        self.assertTrue(hasattr(OpenAIBatchProvider, "create_batch"))
        self.assertTrue(hasattr(OpenAIBatchProvider, "retrieve_batch"))
        self.assertTrue(hasattr(OpenAIBatchProvider, "list_batches"))
        self.assertTrue(hasattr(OpenAIBatchProvider, "cancel_batch"))
        self.assertTrue(hasattr(OpenAIBatchProvider, "download_file"))

    def test_openai_sdk_not_imported_at_module_load_time(self) -> None:
        import sys

        # scripts.mellycore_batch.openai_provider is already imported above by
        # this test module; the real 'openai' package must not have been
        # pulled in as a side effect of that import.
        self.assertNotIn("openai", sys.modules)

    def test_methods_blocked_even_after_bypassing_init_via_new(self) -> None:
        # Stage B requirement: an attacker or test that bypasses __init__
        # entirely (object.__new__ never calls __init__) must still be
        # blocked the moment any method is called, because every method body
        # -- not just __init__ -- calls enforce_live_connection_allowed as
        # its first action, independent of how the instance was constructed.
        instance = object.__new__(OpenAIBatchProvider)
        # No _api_key attribute was ever set by __init__; if any method below
        # skipped its own enforcement call and instead touched self._api_key
        # or a client first, this would raise AttributeError instead of
        # LiveConnectionBlockedError, which would itself be a control gap.
        with self.assertRaises(LiveConnectionBlockedError):
            instance._client()
        with self.assertRaises(LiveConnectionBlockedError):
            instance.upload_input_file(Path("does-not-matter.jsonl"), purpose="batch")
        with self.assertRaises(LiveConnectionBlockedError):
            instance.create_batch(
                input_file_id="file-x",
                endpoint="/v1/responses",
                completion_window="24h",
                metadata={},
            )
        with self.assertRaises(LiveConnectionBlockedError):
            instance.retrieve_batch("batch-x")
        with self.assertRaises(LiveConnectionBlockedError):
            instance.list_batches()
        with self.assertRaises(LiveConnectionBlockedError):
            instance.cancel_batch("batch-x")
        with self.assertRaises(LiveConnectionBlockedError):
            instance.download_file("file-x", Path("out.jsonl"))


class FakeProviderLifecycleTests(unittest.TestCase):
    """Exercises the full mocked lifecycle: upload -> create -> poll -> download / cancel."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        self.provider = FakeBatchProvider()
        manifest = parse_manifest_dict(make_manifest_dict(output_dir=str(self.root)))
        self.input_summary = build_jsonl(manifest)

    def test_fake_provider_satisfies_protocol(self) -> None:
        self.assertIsInstance(self.provider, BatchProvider)

    def test_full_lifecycle_upload_create_poll_download(self) -> None:
        with no_network():
            file_id = self.provider.upload_input_file(
                Path(self.input_summary.path), purpose="batch"
            )
            self.assertTrue(file_id)

            snapshot = self.provider.create_batch(
                input_file_id=file_id,
                endpoint="/v1/responses",
                completion_window="24h",
                metadata={"task_id": "batch-task-1"},
            )
            self.assertEqual("validating", snapshot.status)

            self.provider.set_batch_status(
                snapshot.batch_id,
                status="completed",
                output_file_id="out-1",
                completed_at="2026-01-01T00:00:00Z",
            )
            completed = self.provider.retrieve_batch(snapshot.batch_id)
            self.assertEqual("completed", completed.status)
            self.assertEqual("out-1", completed.output_file_id)

            self.provider.register_file_content("out-1", b'{"custom_id": "req-1"}\n')
            downloaded = self.provider.download_file(
                "out-1", self.root / "downloaded.jsonl"
            )
            self.assertTrue(downloaded.exists())

    def test_lifecycle_cancel_path(self) -> None:
        with no_network():
            file_id = self.provider.upload_input_file(
                Path(self.input_summary.path), purpose="batch"
            )
            snapshot = self.provider.create_batch(
                input_file_id=file_id,
                endpoint="/v1/responses",
                completion_window="24h",
                metadata={},
            )
            cancelled = self.provider.cancel_batch(snapshot.batch_id)
            self.assertEqual("cancelled", cancelled.status)

    def test_list_batches_returns_created_batches(self) -> None:
        with no_network():
            file_id = self.provider.upload_input_file(
                Path(self.input_summary.path), purpose="batch"
            )
            self.provider.create_batch(
                input_file_id=file_id,
                endpoint="/v1/responses",
                completion_window="24h",
                metadata={},
            )
            batches = self.provider.list_batches()
            self.assertEqual(1, len(batches))

    def test_provider_calls_are_recorded(self) -> None:
        with no_network():
            file_id = self.provider.upload_input_file(
                Path(self.input_summary.path), purpose="batch"
            )
            self.provider.create_batch(
                input_file_id=file_id,
                endpoint="/v1/responses",
                completion_window="24h",
                metadata={},
            )
        self.assertEqual(["upload_input_file", "create_batch"], self.provider.calls)


if __name__ == "__main__":
    unittest.main()
