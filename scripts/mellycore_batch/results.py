"""Streaming, deterministic parsing of downloaded Batch output/error JSONL files.

This module never executes, evaluates, or interprets returned model text --
response bodies are carried as inert data (``response_body`` / ``error``
dicts) for a caller to inspect, never as instructions. Parsing is streaming
and line-by-line so it does not require loading a large file fully into
memory.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple, Union

from .models import (
    BatchRequestError,
    BatchRequestResult,
    BatchResultSet,
    MalformedLine,
)

_ParsedLine = Union[BatchRequestResult, BatchRequestError, MalformedLine]


def _parse_line(raw_line: str, line_number: int, source: str) -> _ParsedLine:
    """Classify one JSONL line from a Batch output or error file.

    A line is a success if it carries a non-null ``response`` and no
    populated ``error``; otherwise, if it carries a populated ``error``, it is
    a failure. Any other shape is a structured parser error, never silently
    dropped.
    """
    stripped = raw_line.strip()
    if not stripped:
        return MalformedLine(source=source, line_number=line_number, reason="blank line")

    try:
        obj = json.loads(stripped)
    except json.JSONDecodeError as exc:
        return MalformedLine(
            source=source, line_number=line_number, reason="invalid JSON: {}".format(exc)
        )

    if not isinstance(obj, dict):
        return MalformedLine(source=source, line_number=line_number, reason="line is not a JSON object")

    custom_id = obj.get("custom_id")
    if not isinstance(custom_id, str) or not custom_id.strip():
        return MalformedLine(
            source=source, line_number=line_number, reason="missing or empty custom_id"
        )

    batch_request_id = obj.get("id")
    error = obj.get("error")
    response = obj.get("response")

    if error not in (None, {}):
        if not isinstance(error, dict):
            return MalformedLine(
                source=source,
                line_number=line_number,
                reason="custom_id {!r}: 'error' field is present but not an object".format(custom_id),
            )
        request_id = None
        status_code = None
        if isinstance(response, dict):
            request_id = response.get("request_id")
            status_code = response.get("status_code")
        return BatchRequestError(
            custom_id=custom_id,
            batch_request_id=batch_request_id,
            status_code=status_code,
            request_id=request_id,
            error=error,
        )

    if isinstance(response, dict):
        body = response.get("body")
        if not isinstance(body, dict):
            return MalformedLine(
                source=source,
                line_number=line_number,
                reason="custom_id {!r}: 'response.body' is missing or not an object".format(custom_id),
            )
        usage = body.get("usage") if isinstance(body.get("usage"), dict) else None
        return BatchRequestResult(
            custom_id=custom_id,
            batch_request_id=batch_request_id,
            status_code=response.get("status_code"),
            request_id=response.get("request_id"),
            response_body=body,
            usage=usage,
        )

    return MalformedLine(
        source=source,
        line_number=line_number,
        reason="custom_id {!r}: line has neither a populated 'error' nor a 'response'".format(custom_id),
    )


def iter_parse_lines(path: Path, source: str) -> Iterable[_ParsedLine]:
    """Stream-parse one JSONL file, yielding one classified record per line."""
    path = Path(path)
    with open(path, "r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            yield _parse_line(raw_line, line_number, source)


def parse_result_files(
    output_path: Optional[Path] = None,
    error_path: Optional[Path] = None,
    expected_custom_ids: Optional[Set[str]] = None,
) -> BatchResultSet:
    """Parse a downloaded output file, error file, or both, into a correlated :class:`BatchResultSet`.

    Tolerates either file's lines representing either outcome (the official
    contract allows both to appear in one file or split across two).
    Duplicate ``custom_id`` values across *either* file are reported;
    ``expected_custom_ids``, when given (normally every ``custom_id`` from the
    original input manifest), drives missing-result detection.
    """
    results: List[BatchRequestResult] = []
    errors: List[BatchRequestError] = []
    malformed: List[MalformedLine] = []
    seen_ids: Dict[str, int] = {}
    duplicates: List[str] = []

    sources: List[Tuple[Optional[Path], str]] = [
        (output_path, "output"),
        (error_path, "error"),
    ]
    for path, label in sources:
        if path is None:
            continue
        for record in iter_parse_lines(path, label):
            if isinstance(record, MalformedLine):
                malformed.append(record)
                continue
            if record.custom_id in seen_ids:
                duplicates.append(record.custom_id)
            else:
                seen_ids[record.custom_id] = 1
            if isinstance(record, BatchRequestResult):
                results.append(record)
            else:
                errors.append(record)

    missing: Tuple[str, ...] = ()
    if expected_custom_ids is not None:
        found_ids = {r.custom_id for r in results} | {e.custom_id for e in errors}
        missing = tuple(sorted(expected_custom_ids - found_ids))

    return BatchResultSet(
        results=tuple(results),
        errors=tuple(errors),
        duplicate_custom_ids=tuple(duplicates),
        missing_custom_ids=missing,
        malformed_lines=tuple(malformed),
    )
