"""Shared data models and constants for the MellyCore Batch API foundation.

Standard library only, Python 3.9 compatible. Nothing in this module performs
I/O, calls a model, or reaches the network. It defines the typed shapes every
other module in this package operates on.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

# --- Contract versions -------------------------------------------------------

SCHEMA_VERSION = "1"

# --- Exit codes ---------------------------------------------------------------
# Deterministic and stable. Callers and CI may depend on these.

EXIT_OK = 0
EXIT_INVALID = 1
#: Reserved for a command that would require a live provider connection while
#: migration trigger #5 is blocking. Never reused for any other condition.
EXIT_LIVE_BLOCKED = 78

# --- Official OpenAI Batch API contract (verified, `/v1/responses`) ----------

ENDPOINT_RESPONSES = "/v1/responses"

#: Endpoints this foundation currently supports. Adding another endpoint is a
#: deliberate, separate change -- it is not accepted merely because a manifest
#: names it.
SUPPORTED_ENDPOINTS = (ENDPOINT_RESPONSES,)

SUPPORTED_METHOD = "POST"

#: Official limits as currently documented by OpenAI for the Batch API.
MAX_REQUESTS_PER_BATCH = 50_000
MAX_INPUT_FILE_SIZE_BYTES = 200 * 1024 * 1024
COMPLETION_WINDOW = "24h"
UPLOAD_PURPOSE = "batch"

# --- Migration trigger #5 (canonical, blocking) -------------------------------

MIGRATION_TRIGGER_5_ID = "migration_trigger_5_first_live_provider_connection"
MIGRATION_TRIGGER_5_LABEL = "Trigger #5: First live provider connection"
LIVE_BLOCKED_CODE = "LIVE_PROVIDER_CONNECTION_BLOCKED_BY_MIGRATION_TRIGGER_5"

#: Field names that must never appear as keys inside a request body. Matching
#: a name is enough to reject the request outright; the value is never read
#: out or echoed anywhere in this package.
CREDENTIAL_FIELD_WORDS = (
    "api[_-]?key",
    "apikey",
    "secret",
    "client[_-]?secret",
    "token",
    "auth[_-]?token",
    "access[_-]?key",
    "private[_-]?key",
    "password",
    "passwd",
    "credential",
    "authorization",
    "bearer",
)


class BatchOpsError(Exception):
    """Base class for Batch-foundation failures that should exit non-zero cleanly."""


class InvalidInputError(BatchOpsError):
    """A manifest, request, or file violates its contract."""


class LiveConnectionBlockedError(BatchOpsError):
    """Raised whenever a command would require a live provider connection.

    Carries :data:`LIVE_BLOCKED_CODE` as ``code`` so callers can render a
    stable machine-readable outcome without string-matching the message.
    """

    code = LIVE_BLOCKED_CODE

    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(
            message
            or "{} ({})".format(LIVE_BLOCKED_CODE, MIGRATION_TRIGGER_5_LABEL)
        )


@dataclass(frozen=True)
class BatchRequest:
    """One line of a Batch API JSONL input file.

    Mirrors the official request-object shape exactly:
    ``{"custom_id", "method", "url", "body"}``. Construction alone does not
    validate; use :func:`scripts.mellycore_batch.validation.validate_request`
    before trusting an instance.
    """

    custom_id: str
    method: str
    url: str
    body: Dict[str, Any]

    def to_jsonl_dict(self) -> Dict[str, Any]:
        """Return the exact object this request serializes to on its JSONL line."""
        return {
            "custom_id": self.custom_id,
            "method": self.method,
            "url": self.url,
            "body": self.body,
        }


@dataclass(frozen=True)
class BatchManifest:
    """A local, pre-submission description of one Batch job."""

    task_id: str
    endpoint: str
    requests: Tuple[BatchRequest, ...]
    output_dir: str
    overwrite: bool = False
    completion_window: str = COMPLETION_WINDOW
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def models(self) -> Tuple[str, ...]:
        """Distinct model IDs referenced by this manifest's requests, in first-seen order."""
        seen: List[str] = []
        for request in self.requests:
            model = request.body.get("model")
            if isinstance(model, str) and model not in seen:
                seen.append(model)
        return tuple(seen)


@dataclass(frozen=True)
class BatchInputSummary:
    """Deterministic facts about a generated JSONL input file."""

    path: str
    request_count: int
    byte_size: int
    sha256: str
    endpoint: str
    completion_window: str
    models: Tuple[str, ...]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "path": self.path,
            "request_count": self.request_count,
            "byte_size": self.byte_size,
            "sha256": self.sha256,
            "endpoint": self.endpoint,
            "completion_window": self.completion_window,
            "models": list(self.models),
        }


@dataclass(frozen=True)
class LiveConnectionPolicy:
    """The current, canonical live-connection policy.

    ``allowed`` is always ``False`` while migration trigger #5 is blocking.
    There is no field, flag, or environment variable that can construct an
    ``allowed=True`` instance through any code path reachable from the CLI --
    see :mod:`scripts.mellycore_batch.policy` for the single source of truth.
    """

    allowed: bool
    reason: str
    blocking_trigger: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "allowed": self.allowed,
            "reason": self.reason,
            "blocking_trigger": self.blocking_trigger,
        }


@dataclass(frozen=True)
class BatchJobSnapshot:
    """A point-in-time view of a (real or modelled) Batch job's status."""

    batch_id: str
    status: str
    endpoint: str
    completion_window: str
    input_file_id: Optional[str] = None
    output_file_id: Optional[str] = None
    error_file_id: Optional[str] = None
    created_at: Optional[str] = None
    in_progress_at: Optional[str] = None
    completed_at: Optional[str] = None
    failed_at: Optional[str] = None
    cancelled_at: Optional[str] = None
    request_counts: Dict[str, int] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "batch_id": self.batch_id,
            "status": self.status,
            "endpoint": self.endpoint,
            "completion_window": self.completion_window,
            "input_file_id": self.input_file_id,
            "output_file_id": self.output_file_id,
            "error_file_id": self.error_file_id,
            "created_at": self.created_at,
            "in_progress_at": self.in_progress_at,
            "completed_at": self.completed_at,
            "failed_at": self.failed_at,
            "cancelled_at": self.cancelled_at,
            "request_counts": dict(self.request_counts),
            "metadata": dict(self.metadata),
        }


@dataclass(frozen=True)
class BatchRequestResult:
    """One successful result line from a downloaded Batch output file."""

    custom_id: str
    batch_request_id: Optional[str]
    status_code: Optional[int]
    request_id: Optional[str]
    response_body: Dict[str, Any]
    usage: Optional[Dict[str, Any]] = None


@dataclass(frozen=True)
class BatchRequestError:
    """One failed result line from a downloaded Batch error file."""

    custom_id: str
    batch_request_id: Optional[str]
    status_code: Optional[int]
    request_id: Optional[str]
    error: Dict[str, Any]


@dataclass(frozen=True)
class MalformedLine:
    """A line from a result or error file that could not be parsed as a structured record."""

    source: str
    line_number: int
    reason: str


@dataclass(frozen=True)
class BatchResultSet:
    """The fully correlated, deterministic outcome of parsing Batch output/error files."""

    results: Tuple[BatchRequestResult, ...]
    errors: Tuple[BatchRequestError, ...]
    duplicate_custom_ids: Tuple[str, ...]
    missing_custom_ids: Tuple[str, ...]
    malformed_lines: Tuple[MalformedLine, ...]

    @property
    def completed_count(self) -> int:
        return len(self.results)

    @property
    def failed_count(self) -> int:
        return len(self.errors)

    def total_tokens_by_kind(self) -> Dict[str, int]:
        """Sum token-usage fields present on successful results.

        Missing usage data is simply not counted -- never assumed to be zero
        versus "not reported"; callers distinguish the two via
        :class:`BatchLedgerSummary`'s ``None`` fields.
        """
        totals = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
        any_usage = False
        for result in self.results:
            usage = result.usage or {}
            if not usage:
                continue
            any_usage = True
            for key in totals:
                value = usage.get(key)
                if isinstance(value, int):
                    totals[key] += value
        return totals if any_usage else {}


@dataclass(frozen=True)
class BatchLedgerSummary:
    """Run Ledger-compatible local summary of a Batch job.

    Every field the schema promises is always present; unavailable data is
    ``None`` rather than omitted or guessed.
    """

    schema_version: str
    task_id: str
    batch_id: Optional[str]
    provider: str
    endpoint: str
    completion_window: str
    models: Tuple[str, ...]
    created_at: Optional[str]
    started_at: Optional[str]
    completed_at: Optional[str]
    status: str
    request_count: int
    completed_count: Optional[int]
    failed_count: Optional[int]
    missing_count: Optional[int]
    duplicate_count: Optional[int]
    input_tokens: Optional[int]
    cached_input_tokens: Optional[int]
    output_tokens: Optional[int]
    total_tokens: Optional[int]
    input_file_sha256: Optional[str]
    input_file_size: Optional[int]
    output_file_id: Optional[str]
    error_file_id: Optional[str]
    provider_request_ids: Tuple[str, ...]
    live_connection_authorized: bool
    blocking_policy: Optional[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "task_id": self.task_id,
            "batch_id": self.batch_id,
            "provider": self.provider,
            "endpoint": self.endpoint,
            "completion_window": self.completion_window,
            "models": list(self.models),
            "created_at": self.created_at,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "status": self.status,
            "request_count": self.request_count,
            "completed_count": self.completed_count,
            "failed_count": self.failed_count,
            "missing_count": self.missing_count,
            "duplicate_count": self.duplicate_count,
            "input_tokens": self.input_tokens,
            "cached_input_tokens": self.cached_input_tokens,
            "output_tokens": self.output_tokens,
            "total_tokens": self.total_tokens,
            "input_file_sha256": self.input_file_sha256,
            "input_file_size": self.input_file_size,
            "output_file_id": self.output_file_id,
            "error_file_id": self.error_file_id,
            "provider_request_ids": list(self.provider_request_ids),
            "live_connection_authorized": self.live_connection_authorized,
            "blocking_policy": self.blocking_policy,
        }
