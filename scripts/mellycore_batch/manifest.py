"""Manifest loading and pre-flight validation for Batch jobs.

A manifest describes one prospective Batch job entirely locally: which
requests, which endpoint, where to write the generated input file. Loading
and validating a manifest never writes anything and never reaches the
network.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .jsonl import default_runtime_dir, render_jsonl_bytes
from .models import (
    COMPLETION_WINDOW,
    ENDPOINT_RESPONSES,
    MAX_INPUT_FILE_SIZE_BYTES,
    MAX_REQUESTS_PER_BATCH,
    SUPPORTED_ENDPOINTS,
    BatchManifest,
    BatchRequest,
    InvalidInputError,
)
from .validation import validate_requests


def _parse_request(raw: Dict[str, Any], index: int) -> BatchRequest:
    if not isinstance(raw, dict):
        raise InvalidInputError("manifest request at index {} must be an object".format(index))
    missing = [key for key in ("custom_id", "method", "url", "body") if key not in raw]
    if missing:
        raise InvalidInputError(
            "manifest request at index {} is missing required field(s): {}".format(
                index, ", ".join(missing)
            )
        )
    return BatchRequest(
        custom_id=str(raw["custom_id"]),
        method=str(raw["method"]),
        url=str(raw["url"]),
        body=raw["body"],
    )


def parse_manifest_dict(data: Dict[str, Any]) -> BatchManifest:
    """Parse a raw manifest mapping (as loaded from JSON) into a typed :class:`BatchManifest`.

    Parsing only checks structural shape (required fields present, correct
    types). Contract-level checks -- limits, duplicate IDs, credential
    fields -- happen in :func:`validate_manifest`.
    """
    task_id = data.get("task_id")
    if not isinstance(task_id, str) or not task_id.strip():
        raise InvalidInputError("manifest must set a non-empty 'task_id'")

    endpoint = data.get("endpoint", ENDPOINT_RESPONSES)
    if not isinstance(endpoint, str):
        raise InvalidInputError("manifest 'endpoint' must be a string")

    raw_requests = data.get("requests")
    if not isinstance(raw_requests, list):
        raise InvalidInputError("manifest must set 'requests' as a list")
    requests = tuple(_parse_request(raw, index) for index, raw in enumerate(raw_requests))

    output_dir = data.get("output_dir")
    if output_dir is None:
        output_dir = str(default_runtime_dir())
    elif not isinstance(output_dir, str):
        raise InvalidInputError("manifest 'output_dir' must be a string")

    overwrite_raw = data.get("overwrite", False)
    if not isinstance(overwrite_raw, bool):
        # Deliberately not `bool(overwrite_raw)`: Python truthiness would
        # coerce a JSON string `"false"` (or any other non-empty string, or
        # `1`) to `True`, silently enabling overwrite for a manifest that
        # visibly says it should not. Ambiguous input is rejected outright.
        raise InvalidInputError(
            "manifest 'overwrite' must be a JSON boolean (true/false), got {!r}".format(overwrite_raw)
        )
    overwrite = overwrite_raw

    completion_window = data.get("completion_window", COMPLETION_WINDOW)
    if not isinstance(completion_window, str):
        raise InvalidInputError("manifest 'completion_window' must be a string")

    metadata = data.get("metadata", {})
    if not isinstance(metadata, dict):
        raise InvalidInputError("manifest 'metadata' must be an object")

    return BatchManifest(
        task_id=task_id,
        endpoint=endpoint,
        requests=requests,
        output_dir=output_dir,
        overwrite=overwrite,
        completion_window=completion_window,
        metadata=metadata,
    )


def load_manifest_file(path: Path) -> BatchManifest:
    """Load and parse a manifest JSON file. Read-only."""
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise InvalidInputError("cannot read manifest {}: {}".format(path, exc)) from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise InvalidInputError("manifest {} is not valid JSON: {}".format(path, exc)) from exc
    if not isinstance(data, dict):
        raise InvalidInputError("manifest {} must contain a JSON object".format(path))
    return parse_manifest_dict(data)


def validate_manifest(manifest: BatchManifest) -> None:
    """Validate a manifest against the official Batch contract and this package's safety rules.

    Fails before any submission plan or JSONL file would be produced when a
    limit is exceeded. Raises :class:`InvalidInputError` on the first
    violation found.
    """
    if manifest.endpoint not in SUPPORTED_ENDPOINTS:
        raise InvalidInputError(
            "unsupported manifest endpoint {!r}; supported endpoints: {}".format(
                manifest.endpoint, ", ".join(SUPPORTED_ENDPOINTS)
            )
        )

    if manifest.completion_window != COMPLETION_WINDOW:
        raise InvalidInputError(
            "unsupported completion_window {!r}; only {!r} is currently supported".format(
                manifest.completion_window, COMPLETION_WINDOW
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

    projected_size = len(render_jsonl_bytes(manifest.requests))
    if projected_size > MAX_INPUT_FILE_SIZE_BYTES:
        raise InvalidInputError(
            "manifest {!r} would generate a {}-byte input file, exceeding the official limit of {} bytes".format(
                manifest.task_id, projected_size, MAX_INPUT_FILE_SIZE_BYTES
            )
        )
