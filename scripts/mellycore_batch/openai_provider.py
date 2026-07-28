"""The OpenAI Batch provider adapter.

This module defines the shape of a real integration with the official OpenAI
Python SDK, translating between this package's typed local objects and SDK
calls. It is deliberately inert:

* the official ``openai`` package is never imported at module load time --
  only lazily, inside each method body, and only if that method is ever
  actually called;
* the constructor enforces
  :func:`scripts.mellycore_batch.policy.enforce_live_connection_allowed`
  before storing anything, so this class cannot be instantiated at all while
  migration trigger #5 is blocking, even by code that bypasses the CLI;
* nothing in this module reads, stores, or prints ``OPENAI_API_KEY`` or any
  other credential.

Because the constructor always raises right now, no method body below can
currently execute -- this file exists to make live activation, once
separately authorized, a matter of an operator explicitly constructing this
class rather than writing new integration code.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import BatchJobSnapshot
from .policy import enforce_live_connection_allowed


class OpenAIBatchProvider:
    """A :class:`~scripts.mellycore_batch.provider.BatchProvider` backed by the OpenAI SDK.

    Construction alone enforces the live-connection policy; there is no
    method on this class that can run before that check has already passed
    the object into existence.
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        enforce_live_connection_allowed("OpenAIBatchProvider.__init__")
        # Unreachable while trigger #5 blocks: enforce_live_connection_allowed
        # always raises above. Kept for shape only -- never stores a key.
        self._api_key = api_key  # pragma: no cover

    def _client(self) -> Any:  # pragma: no cover - unreachable while blocked
        """Lazily construct the official SDK client. Never called at import time."""
        enforce_live_connection_allowed("OpenAIBatchProvider._client")
        import openai  # noqa: PLC0415 - intentionally lazy; see module docstring

        return openai.OpenAI(api_key=self._api_key)

    def upload_input_file(self, path: Path, purpose: str) -> str:  # pragma: no cover
        enforce_live_connection_allowed("OpenAIBatchProvider.upload_input_file")
        client = self._client()
        with open(path, "rb") as handle:
            uploaded = client.files.create(file=handle, purpose=purpose)
        return uploaded.id

    def create_batch(
        self,
        input_file_id: str,
        endpoint: str,
        completion_window: str,
        metadata: Dict[str, Any],
    ) -> BatchJobSnapshot:  # pragma: no cover
        enforce_live_connection_allowed("OpenAIBatchProvider.create_batch")
        client = self._client()
        batch = client.batches.create(
            input_file_id=input_file_id,
            endpoint=endpoint,
            completion_window=completion_window,
            metadata=metadata,
        )
        return _snapshot_from_sdk_batch(batch)

    def retrieve_batch(self, batch_id: str) -> BatchJobSnapshot:  # pragma: no cover
        enforce_live_connection_allowed("OpenAIBatchProvider.retrieve_batch")
        client = self._client()
        batch = client.batches.retrieve(batch_id)
        return _snapshot_from_sdk_batch(batch)

    def list_batches(self, limit: int = 20) -> List[BatchJobSnapshot]:  # pragma: no cover
        enforce_live_connection_allowed("OpenAIBatchProvider.list_batches")
        client = self._client()
        page = client.batches.list(limit=limit)
        return [_snapshot_from_sdk_batch(batch) for batch in page.data]

    def cancel_batch(self, batch_id: str) -> BatchJobSnapshot:  # pragma: no cover
        enforce_live_connection_allowed("OpenAIBatchProvider.cancel_batch")
        client = self._client()
        batch = client.batches.cancel(batch_id)
        return _snapshot_from_sdk_batch(batch)

    def download_file(self, file_id: str, destination: Path) -> Path:  # pragma: no cover
        enforce_live_connection_allowed("OpenAIBatchProvider.download_file")
        client = self._client()
        content = client.files.content(file_id)
        destination = Path(destination)
        destination.parent.mkdir(parents=True, exist_ok=True)
        content.write_to_file(destination)
        return destination


def _snapshot_from_sdk_batch(batch: Any) -> BatchJobSnapshot:  # pragma: no cover - unreachable while blocked
    """Translate an SDK batch object into this package's typed snapshot.

    Uses ``getattr`` throughout because the SDK's object shape is not this
    package's contract to enforce; missing fields become ``None`` rather than
    raising.
    """
    request_counts = getattr(batch, "request_counts", None)
    counts_dict: Dict[str, int] = {}
    if request_counts is not None:
        for key in ("total", "completed", "failed"):
            value = getattr(request_counts, key, None)
            if isinstance(value, int):
                counts_dict[key] = value

    def _optional_str(attr: str) -> Any:
        value = getattr(batch, attr, None)
        return str(value) if value is not None else None

    return BatchJobSnapshot(
        batch_id=getattr(batch, "id", ""),
        status=getattr(batch, "status", "unknown"),
        endpoint=getattr(batch, "endpoint", ""),
        completion_window=getattr(batch, "completion_window", ""),
        input_file_id=getattr(batch, "input_file_id", None),
        output_file_id=getattr(batch, "output_file_id", None),
        error_file_id=getattr(batch, "error_file_id", None),
        created_at=_optional_str("created_at"),
        in_progress_at=_optional_str("in_progress_at"),
        completed_at=_optional_str("completed_at"),
        failed_at=_optional_str("failed_at"),
        cancelled_at=_optional_str("cancelled_at"),
        request_counts=counts_dict,
        metadata=dict(getattr(batch, "metadata", None) or {}),
    )
