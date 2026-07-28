"""Deterministic Batch API JSONL generation and streaming validation.

Nothing in this module reaches the network. It only reads and writes local
files under an explicit path (normally the ignored ``.runtime/batch/``
directory) and never overwrites an existing file unless explicitly told to.
"""

from __future__ import annotations

import hashlib
import json
import re
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
from .validation import validate_request, validate_requests

#: A derived output path is built as ``<output_dir>/<task_id>.jsonl``.
#: ``task_id`` comes from a manifest -- untrusted input -- so it must never be
#: trusted as a raw path component. This charset excludes path separators,
#: drive letters, ``.``/``..``, NUL, and control characters outright rather
#: than trying to sanitize an unsafe value into a different, possibly
#: colliding, one.
_SAFE_TASK_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,199}$")


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
    # Local import: manifest.py imports from this module at module load time,
    # so importing manifest.py back at *this* module's top level would create
    # an import cycle. By the time build_jsonl() actually runs, both modules
    # are already fully loaded, so a function-scoped import is safe.
    from .manifest import validate_manifest

    # The single authoritative manifest contract check -- this is what closes
    # the gap where `build` previously accepted manifests with an unsupported
    # completion_window that `validate --manifest` and `plan-live` would both
    # reject. The checks below are kept as an additional, redundant layer
    # (and to preserve their independently-monkeypatchable module-level
    # constants for existing tests) rather than removed.
    validate_manifest(manifest)

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
        output_path = _safe_default_output_path(manifest.output_dir, manifest.task_id)
    else:
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


def _safe_default_output_path(output_dir: str, task_id: str) -> Path:
    """Build the default ``<output_dir>/<task_id>.jsonl`` path.

    Only used when no explicit ``output_path`` is given to :func:`build_jsonl`.
    An explicit, caller-supplied ``output_path`` is never routed through this
    function and its behavior is unchanged.
    """
    if not _SAFE_TASK_ID_RE.match(task_id):
        raise InvalidInputError(
            "task_id {!r} is not a safe filesystem identifier for a derived output path "
            "(only letters, digits, '-', and '_' are allowed, and it must start with a "
            "letter or digit); pass an explicit output path if you need another value".format(
                task_id
            )
        )

    base_dir = Path(output_dir).resolve()
    candidate = (base_dir / "{}.jsonl".format(task_id)).resolve()
    if candidate.parent != base_dir:
        # Defense in depth: should be unreachable given the charset check
        # above, but path containment is never trusted to a single layer.
        raise InvalidInputError(
            "derived output path {} would not be located directly inside output_dir {}".format(
                candidate, base_dir
            )
        )
    return candidate


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

            line_ok = True

            custom_id = obj.get("custom_id")
            if not isinstance(custom_id, str) or not custom_id.strip():
                yield {"line": line_number, "code": "missing_custom_id", "message": "custom_id missing or empty"}
                line_ok = False
            elif custom_id in seen_ids:
                yield {
                    "line": line_number,
                    "code": "duplicate_custom_id",
                    "message": "duplicate custom_id {!r}".format(custom_id),
                }
                line_ok = False
            else:
                seen_ids.add(custom_id)

            if obj.get("method") != SUPPORTED_METHOD:
                yield {
                    "line": line_number,
                    "code": "unsupported_method",
                    "message": "unsupported method {!r}".format(obj.get("method")),
                }
                line_ok = False
            if obj.get("url") not in SUPPORTED_ENDPOINTS:
                yield {
                    "line": line_number,
                    "code": "unsupported_endpoint",
                    "message": "unsupported url {!r}".format(obj.get("url")),
                }
                line_ok = False

            # Only reachable once custom_id/method/url have each already
            # passed their own check above. Reuses the same authoritative
            # per-request validator the build/manifest path relies on, so a
            # raw JSONL file cannot be reported "valid" while carrying a
            # missing model/input, `stream: true`, an external URL, or a
            # credential-shaped field anywhere in its body.
            if line_ok:
                request = BatchRequest(
                    custom_id=custom_id,
                    method=obj.get("method"),
                    url=obj.get("url"),
                    body=obj.get("body"),
                )
                try:
                    validate_request(request)
                except InvalidInputError as exc:
                    yield {"line": line_number, "code": "invalid_body", "message": str(exc)}

    if request_count > MAX_REQUESTS_PER_BATCH:
        yield {
            "line": 0,
            "code": "request_count_exceeded",
            "message": "{} requests exceeds the official limit of {}".format(
                request_count, MAX_REQUESTS_PER_BATCH
            ),
        }
