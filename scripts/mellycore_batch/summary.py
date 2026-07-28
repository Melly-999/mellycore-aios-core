"""Run Ledger-compatible local summary construction for a Batch job.

Builds :class:`~scripts.mellycore_batch.models.BatchLedgerSummary` objects.
Never writes to the repository's actual Run Ledger storage or documentation
-- this produces a local, machine-readable JSON object only.
"""

from __future__ import annotations

from typing import Optional, Sequence

from .models import (
    SCHEMA_VERSION,
    BatchLedgerSummary,
    BatchResultSet,
)
from .policy import get_active_policy

PROVIDER_NAME = "openai"


def build_ledger_summary(
    task_id: str,
    endpoint: str,
    completion_window: str,
    models: Sequence[str],
    request_count: int,
    status: str,
    batch_id: Optional[str] = None,
    created_at: Optional[str] = None,
    started_at: Optional[str] = None,
    completed_at: Optional[str] = None,
    input_file_sha256: Optional[str] = None,
    input_file_size: Optional[int] = None,
    output_file_id: Optional[str] = None,
    error_file_id: Optional[str] = None,
    provider_request_ids: Sequence[str] = (),
    result_set: Optional[BatchResultSet] = None,
) -> BatchLedgerSummary:
    """Build a :class:`BatchLedgerSummary` from what is locally known right now.

    Every count and token field is ``None`` unless ``result_set`` is
    supplied, honoring the "null when unavailable" contract rather than
    guessing zero.
    """
    completed_count: Optional[int] = None
    failed_count: Optional[int] = None
    missing_count: Optional[int] = None
    duplicate_count: Optional[int] = None
    input_tokens: Optional[int] = None
    cached_input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    total_tokens: Optional[int] = None

    if result_set is not None:
        completed_count = result_set.completed_count
        failed_count = result_set.failed_count
        missing_count = len(result_set.missing_custom_ids)
        duplicate_count = len(result_set.duplicate_custom_ids)
        token_totals = result_set.total_tokens_by_kind()
        if token_totals:
            input_tokens = token_totals.get("input_tokens")
            cached_input_tokens = token_totals.get("cached_input_tokens")
            output_tokens = token_totals.get("output_tokens")
            total_tokens = token_totals.get("total_tokens")

    policy = get_active_policy()

    return BatchLedgerSummary(
        schema_version=SCHEMA_VERSION,
        task_id=task_id,
        batch_id=batch_id,
        provider=PROVIDER_NAME,
        endpoint=endpoint,
        completion_window=completion_window,
        models=tuple(models),
        created_at=created_at,
        started_at=started_at,
        completed_at=completed_at,
        status=status,
        request_count=request_count,
        completed_count=completed_count,
        failed_count=failed_count,
        missing_count=missing_count,
        duplicate_count=duplicate_count,
        input_tokens=input_tokens,
        cached_input_tokens=cached_input_tokens,
        output_tokens=output_tokens,
        total_tokens=total_tokens,
        input_file_sha256=input_file_sha256,
        input_file_size=input_file_size,
        output_file_id=output_file_id,
        error_file_id=error_file_id,
        provider_request_ids=tuple(provider_request_ids),
        live_connection_authorized=policy.allowed,
        blocking_policy=None if policy.allowed else policy.reason,
    )
