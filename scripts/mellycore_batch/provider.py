"""The Batch provider boundary.

:class:`BatchProvider` is the interface every provider adapter -- real or
fake -- implements. Defining this interface does not authorize a live
connection; see :mod:`scripts.mellycore_batch.policy` for the single place
that decision is made.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Protocol, runtime_checkable

from .models import BatchJobSnapshot


@runtime_checkable
class BatchProvider(Protocol):
    """Operations a Batch provider adapter must implement.

    An object satisfying this protocol is not, by itself, a live connection
    -- it becomes one only once a caller actually invokes one of these
    methods. The CLI's local commands (``build``, ``validate``, ``inspect``,
    ``summarize``, ``plan-live``) never construct or call an implementation
    of this protocol. The provider-backed commands (``submit``, ``status``,
    ``list``, ``download``, ``cancel``) are refused by
    :func:`scripts.mellycore_batch.policy.enforce_live_connection_allowed`
    before any implementation of this protocol is constructed.
    """

    def upload_input_file(self, path: Path, purpose: str) -> str:
        """Upload a local JSONL file and return its provider file ID."""
        ...

    def create_batch(
        self,
        input_file_id: str,
        endpoint: str,
        completion_window: str,
        metadata: Dict[str, Any],
    ) -> BatchJobSnapshot:
        """Create a Batch job from an already-uploaded input file."""
        ...

    def retrieve_batch(self, batch_id: str) -> BatchJobSnapshot:
        """Fetch the current status of one Batch job."""
        ...

    def list_batches(self, limit: int = 20) -> List[BatchJobSnapshot]:
        """List recent Batch jobs."""
        ...

    def cancel_batch(self, batch_id: str) -> BatchJobSnapshot:
        """Request cancellation of an in-progress Batch job."""
        ...

    def download_file(self, file_id: str, destination: Path) -> Path:
        """Download a provider file (output or error JSONL) to a local path."""
        ...
