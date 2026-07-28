"""Validation for individual Batch requests and request collections.

Validation is strict and refuses to silently rewrite anything: a request
either satisfies the official Batch API contract and this package's safety
rules, or it is rejected with a specific, itemized reason. Nothing here
performs I/O or reaches the network.
"""

from __future__ import annotations

import json
import re
from typing import Any, Dict, List, Sequence

from .models import (
    CREDENTIAL_FIELD_WORDS,
    SUPPORTED_ENDPOINTS,
    SUPPORTED_METHOD,
    BatchRequest,
    InvalidInputError,
)

_CREDENTIAL_FIELD_RE = re.compile(r"(?i)^(" + "|".join(CREDENTIAL_FIELD_WORDS) + r")$")

#: External-looking URL schemes/hosts that must never appear inside a request
#: body. The Batch endpoint itself is validated separately against
#: ``SUPPORTED_ENDPOINTS``; this guards against a body smuggling a second,
#: arbitrary destination (e.g. a webhook or callback field).
_EXTERNAL_URL_RE = re.compile(r"(?i)\b(?:https?|ftp)://")


def _find_credential_fields(value: Any, path: str = "body") -> List[str]:
    """Recursively locate dict keys that look like credential-bearing fields.

    Returns field paths only, never values -- consistent with this
    repository's redaction convention of reporting *where*, not *what*.
    """
    findings: List[str] = []
    if isinstance(value, dict):
        for key, sub_value in value.items():
            key_path = "{}.{}".format(path, key)
            if _CREDENTIAL_FIELD_RE.match(str(key)):
                findings.append(key_path)
            findings.extend(_find_credential_fields(sub_value, key_path))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.extend(_find_credential_fields(item, "{}[{}]".format(path, index)))
    return findings


def _find_external_urls(value: Any, path: str = "body") -> List[str]:
    """Recursively locate string values that look like external URLs."""
    findings: List[str] = []
    if isinstance(value, dict):
        for key, sub_value in value.items():
            findings.extend(_find_external_urls(sub_value, "{}.{}".format(path, key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.extend(_find_external_urls(item, "{}[{}]".format(path, index)))
    elif isinstance(value, str):
        if _EXTERNAL_URL_RE.search(value):
            findings.append(path)
    return findings


def _assert_json_serializable(value: Any, path: str = "body") -> None:
    try:
        json.dumps(value)
    except (TypeError, ValueError) as exc:
        raise InvalidInputError(
            "request body at {!r} is not JSON-serializable: {}".format(path, exc)
        ) from exc


def validate_request(request: BatchRequest) -> None:
    """Validate one :class:`BatchRequest` against the official contract and this package's rules.

    Raises :class:`InvalidInputError` on the first violation found; never
    mutates or rewrites the request.
    """
    if not request.custom_id or not request.custom_id.strip():
        raise InvalidInputError("custom_id must be non-empty")

    if request.method != SUPPORTED_METHOD:
        raise InvalidInputError(
            "unsupported method {!r} for custom_id {!r}; only {!r} is supported".format(
                request.method, request.custom_id, SUPPORTED_METHOD
            )
        )

    if request.url not in SUPPORTED_ENDPOINTS:
        raise InvalidInputError(
            "unsupported endpoint {!r} for custom_id {!r}; supported endpoints: {}".format(
                request.url, request.custom_id, ", ".join(SUPPORTED_ENDPOINTS)
            )
        )

    if not isinstance(request.body, dict) or not request.body:
        raise InvalidInputError(
            "request body for custom_id {!r} must be a non-empty object".format(request.custom_id)
        )

    _assert_json_serializable(request.body)

    model = request.body.get("model")
    if not isinstance(model, str) or not model.strip():
        raise InvalidInputError(
            "request body for custom_id {!r} must set a non-empty explicit 'model'".format(
                request.custom_id
            )
        )

    input_value = request.body.get("input")
    if input_value is None or (isinstance(input_value, str) and not input_value.strip()):
        raise InvalidInputError(
            "request body for custom_id {!r} must set a non-empty 'input'".format(request.custom_id)
        )
    if isinstance(input_value, (list, dict)) and not input_value:
        raise InvalidInputError(
            "request body for custom_id {!r} must set a non-empty 'input'".format(request.custom_id)
        )

    if request.body.get("stream") is True:
        raise InvalidInputError(
            "request body for custom_id {!r} sets stream=true; streaming is not supported by the Batch API".format(
                request.custom_id
            )
        )

    credential_fields = _find_credential_fields(request.body)
    if credential_fields:
        raise InvalidInputError(
            "request body for custom_id {!r} contains credential-shaped field(s): {}".format(
                request.custom_id, ", ".join(credential_fields)
            )
        )

    external_urls = _find_external_urls(request.body)
    if external_urls:
        raise InvalidInputError(
            "request body for custom_id {!r} contains external URL(s) at: {}".format(
                request.custom_id, ", ".join(external_urls)
            )
        )


def validate_requests(requests: Sequence[BatchRequest]) -> None:
    """Validate a full collection: each request individually, plus uniqueness across the set."""
    seen: Dict[str, int] = {}
    for index, request in enumerate(requests):
        validate_request(request)
        if request.custom_id in seen:
            raise InvalidInputError(
                "duplicate custom_id {!r} at request index {} (first seen at index {})".format(
                    request.custom_id, index, seen[request.custom_id]
                )
            )
        seen[request.custom_id] = index

    if not requests:
        raise InvalidInputError("request collection must contain at least one request")
