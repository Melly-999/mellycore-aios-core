"""Shared fixtures for MellyCore Batch API foundation tests.

Includes a network-denial context manager: patches the socket layer so any
test using it fails loudly, rather than silently, if code under test ever
attempts a real network connection.
"""

from __future__ import annotations

import socket
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, List, Optional
from unittest import mock

from scripts.mellycore_batch.models import BatchJobSnapshot


def make_request(
    custom_id: str = "req-1",
    model: str = "gpt-test-model",
    input_text: str = "hello world",
    endpoint: str = "/v1/responses",
    extra_body: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    body: Dict[str, Any] = {"model": model, "input": input_text}
    if extra_body:
        body.update(extra_body)
    return {
        "custom_id": custom_id,
        "method": "POST",
        "url": endpoint,
        "body": body,
    }


def make_manifest_dict(
    task_id: str = "batch-task-1",
    requests: Optional[List[Dict[str, Any]]] = None,
    output_dir: Optional[str] = None,
    overwrite: bool = False,
    endpoint: str = "/v1/responses",
    completion_window: str = "24h",
) -> Dict[str, Any]:
    if requests is None:
        requests = [make_request("req-1"), make_request("req-2")]
    manifest: Dict[str, Any] = {
        "task_id": task_id,
        "endpoint": endpoint,
        "completion_window": completion_window,
        "requests": requests,
        "overwrite": overwrite,
    }
    if output_dir is not None:
        manifest["output_dir"] = output_dir
    return manifest


class FakeBatchProvider:
    """An in-memory, non-network :class:`~scripts.mellycore_batch.provider.BatchProvider`.

    Used to exercise lifecycle logic (upload -> create -> poll -> cancel/
    download) entirely locally. Records every call it receives so a test can
    assert it was never invoked.
    """

    def __init__(self) -> None:
        self.calls: List[str] = []
        self._uploaded_files: Dict[str, bytes] = {}
        self._batches: Dict[str, BatchJobSnapshot] = {}
        self._file_contents: Dict[str, bytes] = {}
        self._next_file_id = 1
        self._next_batch_id = 1

    def upload_input_file(self, path: Path, purpose: str) -> str:
        self.calls.append("upload_input_file")
        file_id = "file-{}".format(self._next_file_id)
        self._next_file_id += 1
        self._uploaded_files[file_id] = Path(path).read_bytes()
        return file_id

    def create_batch(
        self,
        input_file_id: str,
        endpoint: str,
        completion_window: str,
        metadata: Dict[str, Any],
    ) -> BatchJobSnapshot:
        self.calls.append("create_batch")
        batch_id = "batch-{}".format(self._next_batch_id)
        self._next_batch_id += 1
        snapshot = BatchJobSnapshot(
            batch_id=batch_id,
            status="validating",
            endpoint=endpoint,
            completion_window=completion_window,
            input_file_id=input_file_id,
            metadata=dict(metadata),
        )
        self._batches[batch_id] = snapshot
        return snapshot

    def retrieve_batch(self, batch_id: str) -> BatchJobSnapshot:
        self.calls.append("retrieve_batch")
        return self._batches[batch_id]

    def list_batches(self, limit: int = 20) -> List[BatchJobSnapshot]:
        self.calls.append("list_batches")
        return list(self._batches.values())[:limit]

    def cancel_batch(self, batch_id: str) -> BatchJobSnapshot:
        self.calls.append("cancel_batch")
        existing = self._batches[batch_id]
        cancelled = BatchJobSnapshot(
            batch_id=existing.batch_id,
            status="cancelled",
            endpoint=existing.endpoint,
            completion_window=existing.completion_window,
            input_file_id=existing.input_file_id,
            output_file_id=existing.output_file_id,
            error_file_id=existing.error_file_id,
            cancelled_at="2026-01-01T00:00:00Z",
            metadata=dict(existing.metadata),
        )
        self._batches[batch_id] = cancelled
        return cancelled

    def set_batch_status(self, batch_id: str, **fields: Any) -> None:
        """Test-only helper: advance a stored batch's fields to simulate progress."""
        existing = self._batches[batch_id]
        merged = existing.to_dict()
        merged.update(fields)
        self._batches[batch_id] = BatchJobSnapshot(
            batch_id=merged["batch_id"],
            status=merged["status"],
            endpoint=merged["endpoint"],
            completion_window=merged["completion_window"],
            input_file_id=merged.get("input_file_id"),
            output_file_id=merged.get("output_file_id"),
            error_file_id=merged.get("error_file_id"),
            created_at=merged.get("created_at"),
            in_progress_at=merged.get("in_progress_at"),
            completed_at=merged.get("completed_at"),
            failed_at=merged.get("failed_at"),
            cancelled_at=merged.get("cancelled_at"),
            request_counts=merged.get("request_counts", {}),
            metadata=merged.get("metadata", {}),
        )

    def register_file_content(self, file_id: str, content: bytes) -> None:
        """Test-only helper: seed content for a later download_file call."""
        self._file_contents[file_id] = content

    def download_file(self, file_id: str, destination: Path) -> Path:
        self.calls.append("download_file")
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(self._file_contents.get(file_id, b""))
        return destination


@contextmanager
def no_network():
    """Patch the socket layer so any real network attempt raises loudly.

    Used to prove, rather than merely assert by inspection, that a code path
    under test never reaches the network.
    """

    def _deny(*args: Any, **kwargs: Any) -> Any:
        raise AssertionError("network access attempted during a test that must not use the network")

    with mock.patch.object(socket.socket, "connect", side_effect=_deny), mock.patch.object(
        socket, "create_connection", side_effect=_deny
    ):
        yield
