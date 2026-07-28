"""Deterministic Batch API JSONL generation and streaming validation.

Nothing in this module reaches the network. It only reads and writes local
files under an explicit path (normally the ignored ``.runtime/batch/``
directory) and never overwrites an existing file unless explicitly told to.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Iterator, Optional, Sequence, Set

from .models import (
    MAX_INPUT_FILE_SIZE_BYTES,
    MAX_REQUESTS_PER_BATCH,
    SUPPORTED_ENDPOINTS,
    SUPPORTED_METHOD,
    BatchInputSummary,
    BatchManifest,
    BatchRequest,
    InvalidInputError,
)
from .validation import validate_requests


def repo_root() -> Path:
    """Return the repository root, derived from this file's location.

    ``scripts/mellycore_batch/jsonl.py`` -> parents[2] is the repo root.
    """
    return Path(__file__).resolve().parents[2]


def default_runtime_dir() -> Path:
    """The ignored runtime directory Batch artifacts are written to by default."""
    return repo_root() / ".runtime" / "batch"


def _serialize_line(request: BatchRequest) -> str:
    """Serialize one request to its exact JSONL line.

    ``sort_keys=True`` makes the output depend only on content, never on the
    order fields happened to be inserted into a dict -- required for the
    byte-identical regeneration guarantee.
    """
    return json.dumps(request.to_jsonl_dict(), sort_keys=True, ensure_ascii=False)


def render_jsonl_bytes(requests: Sequence[BatchRequest]) -> bytes:
    """Render the exact bytes a JSONL input file would contain for ``requests``.

    Preserves request order as given (never reorders). Always ends with a
    single trailing newline. Pure function: identical input always produces
    identical bytes.
    """
    lines = [_serialize_line(request) for request in requests]
    text = "\n".join(lines) + ("\n" if lines else "")
    return text.encode("utf-8")


def build_jsonl(manifest: BatchManifest, output_path: Optional[Path] = None) -> BatchInputSummary:
    """Validate ``manifest`` and write its deterministic JSONL input file.

    Raises :class:`InvalidInputError` before writing anything if the manifest
    violates the official request-count or file-size limits, or if any
    request fails validation. Refuses to overwrite an existing file unless
    ``manifest.overwrite`` is true.
    """
    if manifest.endpoint not in SUPPORTED_ENDPOINTS:
        raise InvalidInputError(
            "unsupported manifest endpoint {!r}; supported endpoints: {}".format(
                manifest.endpoint, ", ".join(SUPPORTED_ENDPOINTS)
            )
        )

    mismatched = [r.url for r in manifest.requests if r.url != manifest.endpoint]
    if mismatched:
        raise InvalidInputError(
            "all requests in a manifest must target the manifest's endpoint {!r}; "
            "found {} request(s) targeting a different url".format(manifest.endpoint, len(mismatched))
        )

    validate_requests(manifest.requests)

    if len(manifest.requests) > MAX_REQUESTS_PER_BATCH:
        raise InvalidInputError(
            "manifest {!r} has {} requests, exceeding the official limit of {}".format(
                manifest.task_id, len(manifest.requests), MAX_REQUESTS_PER_BATCH
            )
        )

    payload = render_jsonl_bytes(manifest.requests)
    if len(payload) > MAX_INPUT_FILE_SIZE_BYTES:
        raise InvalidInputError(
            "manifest {!r} would generate a {}-byte input file, exceeding the official limit of {} bytes".format(
                manifest.task_id, len(payload), MAX_INPUT_FILE_SIZE_BYTES
            )
        )

    if output_path is None:
        output_path = Path(manifest.output_dir) / "{}.jsonl".format(manifest.task_id)
    output_path = Path(output_path)

    if output_path.exists() and not manifest.overwrite:
        raise InvalidInputError(
            "refusing to overwrite existing file {} (pass overwrite=True / --overwrite to replace it)".format(
                output_path
            )
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(payload)

    digest = hashlib.sha256(payload).hexdigest()

    return BatchInputSummary(
        path=str(output_path),
        request_count=len(manifest.requests),
        byte_size=len(payload),
        sha256=digest,
        endpoint=manifest.endpoint,
        completion_window=manifest.completion_window,
        models=manifest.models,
    )


def sha256_of_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """Stream-hash a file without loading it fully into memory."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            chunk = handle.read(chunk_size)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def iter_validate_jsonl_file(path: Path) -> Iterator[Dict[str, Any]]:
    """Stream-validate an existing JSONL input file line by line.

    Yields one finding dict per problem encountered: ``{"line": int,
    "code": str, "message": str}``. Never loads the whole file into memory --
    reads and discards each line as it goes, retaining only the small set of
    ``custom_id`` values seen so far for duplicate detection.
    """
    seen_ids: Set[str] = set()
    request_count = 0
    with open(path, "r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            stripped = raw_line.rstrip("\n")
            if not stripped:
                continue
            request_count += 1
            try:
                obj = json.loads(stripped)
            except json.JSONDecodeError as exc:
                yield {"line": line_number, "code": "malformed_json", "message": str(exc)}
                continue

            if not isinstance(obj, dict):
                yield {"line": line_number, "code": "not_an_object", "message": "line is not a JSON object"}
                continue

            custom_id = obj.get("custom_id")
            if not isinstance(custom_id, str) or not custom_id.strip():
                yield {"line": line_number, "code": "missing_custom_id", "message": "custom_id missing or empty"}
            elif custom_id in seen_ids:
                yield {
                    "line": line_number,
                    "code": "duplicate_custom_id",
                    "message": "duplicate custom_id {!r}".format(custom_id),
                }
            else:
                seen_ids.add(custom_id)

            if obj.get("method") != SUPPORTED_METHOD:
                yield {
                    "line": line_number,
                    "code": "unsupported_method",
                    "message": "unsupported method {!r}".format(obj.get("method")),
                }
            if obj.get("url") not in SUPPORTED_ENDPOINTS:
                yield {
                    "line": line_number,
                    "code": "unsupported_endpoint",
                    "message": "unsupported url {!r}".format(obj.get("url")),
                }

    if request_count > MAX_REQUESTS_PER_BATCH:
        yield {
            "line": 0,
            "code": "request_count_exceeded",
            "message": "{} requests exceeds the official limit of {}".format(
                request_count, MAX_REQUESTS_PER_BATCH
            ),
        }
