"""Strict normalization for synthetic Cloudflare API Shield fixtures only."""

from __future__ import annotations

import hashlib
import re
from typing import Any, Dict, Tuple

from ..contracts import CapabilityId
from .contracts import (
    CloudflareApiOperation,
    CloudflareCompleteness,
    CloudflareErrorCode,
    CloudflareFixtureError,
    CloudflareFixtureReadResult,
    CloudflareFixtureTrust,
    CloudflareNormalizedError,
)
from .manifest import CLOUDFLARE_CONTRACT_REVISION

_OPAQUE_REFERENCE_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{2,127}$")
_SYNTHETIC_HOST_PATTERN = re.compile(
    r"(?=.{1,253}\Z)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"(?:invalid|test|example)"
)
_SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"(?i)\bbearer\s+[a-z0-9._-]+"),
    re.compile(r"(?i)\b(?:api[_-]?key|client[_-]?secret|password)\s*[:=]"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
)
_SENSITIVE_KEYS = {
    "authorization",
    "api_key",
    "apikey",
    "bearer",
    "client_secret",
    "password",
    "secret",
    "token",
}
_MUTATION_KEYS = {
    "action",
    "apply",
    "delete",
    "deploy",
    "enabled",
    "execute",
    "mitigation",
    "mutation",
    "patch",
    "write",
}
_INJECTION_PATTERNS = (
    re.compile(r"(?i)ignore\s+(?:all\s+)?previous"),
    re.compile(r"(?i)system\s+(?:message|instruction)"),
    re.compile(r"(?i)operator\s+approval\s+(?:is|was)\s+granted"),
)
_BIDI_CONTROLS = {
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",
    "\u2066",
    "\u2067",
    "\u2068",
    "\u2069",
}
_MAX_DEPTH = 6
_MAX_ITEMS = 64
_MAX_TEXT = 512
_TOP_LEVEL_KEYS = {
    "fixture_only",
    "source",
    "capability_id",
    "tenant_ref",
    "account_ref",
    "zone_ref",
    "observed_at",
    "completeness",
    "items",
}
_ITEM_KEYS = {
    "canonical_ref",
    "provider_native_ref",
    "host",
    "path",
    "operation_method",
    "description",
}
_NORMALIZABLE_CAPABILITIES = {
    "cloudflare.endpoint_management.operations.list",
    "cloudflare.endpoint_management.operations.get",
}


def _deny(code: CloudflareErrorCode, message: str, field: str) -> None:
    raise CloudflareFixtureError(
        CloudflareNormalizedError(
            code=code,
            message=message,
            field=field,
            provider_request_occurred=False,
        )
    )


def _require_depth(value: Any, depth: int = 0) -> None:
    if depth > _MAX_DEPTH:
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture nesting exceeds the closed normalization bound",
            "fixture",
        )
    if isinstance(value, tuple):
        for item in value:
            _require_depth(item, depth + 1)
    elif isinstance(value, (str, int, bool, type(None))):
        return
    else:
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture contains an unsupported mutable or untyped value",
            "fixture",
        )


def _require_non_sensitive(value: Any, field: str) -> None:
    if isinstance(value, str):
        if (
            len(value) > _MAX_TEXT
            or value.lower() in _SENSITIVE_KEYS
            or any(pattern.search(value) for pattern in _SENSITIVE_VALUE_PATTERNS)
        ):
            _deny(
                CloudflareErrorCode.SENSITIVE_FIXTURE_VALUE,
                "fixture contains sensitive-shaped text",
                field,
            )
        return
    if isinstance(value, tuple):
        for item in value:
            _require_non_sensitive(item, field)


def _pairs_to_dict(value: Any, field: str) -> Dict[str, Any]:
    if not isinstance(value, tuple):
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture object must be an immutable tuple of key-value pairs",
            field,
        )
    resolved: Dict[str, Any] = {}
    for item in value:
        if (
            not isinstance(item, tuple)
            or len(item) != 2
            or not isinstance(item[0], str)
        ):
            _deny(
                CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
                "fixture entry is not one closed key-value pair",
                field,
            )
        key, item_value = item
        lowered = key.lower()
        if lowered in _SENSITIVE_KEYS:
            _deny(
                CloudflareErrorCode.SENSITIVE_FIXTURE_VALUE,
                "fixture contains a sensitive-shaped field",
                field,
            )
        if lowered in _MUTATION_KEYS:
            _deny(
                CloudflareErrorCode.UNEXPECTED_MUTATION_FIELD,
                "fixture contains a mutation-shaped field",
                field,
            )
        if key in resolved:
            _deny(
                CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
                "fixture object contains a duplicate field",
                field,
            )
        resolved[key] = item_value
    return resolved


def _require_exact_keys(value: Dict[str, Any], expected: set, field: str) -> None:
    if set(value) != expected:
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture object does not match the closed schema",
            field,
        )


def _require_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture text field is missing or has the wrong type",
            field,
        )
    return value


def _require_reference(value: Any, field: str) -> str:
    text = _require_text(value, field)
    if not _OPAQUE_REFERENCE_PATTERN.fullmatch(text):
        _deny(
            CloudflareErrorCode.SENSITIVE_FIXTURE_VALUE,
            "fixture reference must be opaque and non-sensitive",
            field,
        )
    return text


def _normalize_untrusted_text(value: Any, field: str) -> Tuple[str, bool]:
    text = _require_text(value, field)
    sanitized = "".join(
        "\ufffd" if character in _BIDI_CONTROLS or ord(character) < 32 else character
        for character in text
    )
    suspected = sanitized != text or any(
        pattern.search(sanitized) for pattern in _INJECTION_PATTERNS
    )
    return sanitized, suspected


def _require_synthetic_host(value: Any) -> str:
    host = _require_text(value, "host")
    if not _SYNTHETIC_HOST_PATTERN.fullmatch(host):
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture host must be a bounded synthetic hostname",
            "host",
        )
    return host


def _normalize_item(value: Any) -> CloudflareApiOperation:
    item = _pairs_to_dict(value, "items")
    _require_exact_keys(item, _ITEM_KEYS, "items")
    canonical_ref = _require_reference(item["canonical_ref"], "canonical_ref")
    provider_native_ref = _require_reference(
        item["provider_native_ref"], "provider_native_ref"
    )
    host = _require_synthetic_host(item["host"])
    path, path_flag = _normalize_untrusted_text(item["path"], "path")
    operation_method, method_flag = _normalize_untrusted_text(
        item["operation_method"], "operation_method"
    )
    description, description_flag = _normalize_untrusted_text(
        item["description"], "description"
    )
    return CloudflareApiOperation(
        canonical_ref=canonical_ref,
        provider_native_ref=provider_native_ref,
        host=host,
        path=path,
        operation_method=operation_method,
        description=description,
        trust=CloudflareFixtureTrust.UNTRUSTED_PROVIDER_CONTENT,
        injection_suspected=(path_flag or method_flag or description_flag),
        fixture_only=True,
        contract_revision=CLOUDFLARE_CONTRACT_REVISION,
    )


def _state_digest(items: Tuple[CloudflareApiOperation, ...]) -> str:
    canonical = tuple(
        (
            item.canonical_ref,
            item.provider_native_ref,
            item.host,
            item.path,
            item.operation_method,
            item.description,
            item.injection_suspected,
        )
        for item in items
    )
    return hashlib.sha256(repr(canonical).encode("utf-8")).hexdigest()


def normalize_api_operations_fixture(fixture: Any) -> CloudflareFixtureReadResult:
    """Normalize one immutable synthetic fixture without provider execution."""

    _require_depth(fixture)
    _require_non_sensitive(fixture, "fixture")
    resolved = _pairs_to_dict(fixture, "fixture")
    _require_exact_keys(resolved, _TOP_LEVEL_KEYS, "fixture")
    if resolved["fixture_only"] is not True:
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture must carry the explicit fixture-only marker",
            "fixture_only",
        )
    if resolved["source"] != "synthetic-cloudflare-fixture":
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture source is not the synthetic source marker",
            "source",
        )
    capability_id = _require_text(resolved["capability_id"], "capability_id")
    if capability_id not in _NORMALIZABLE_CAPABILITIES:
        _deny(
            CloudflareErrorCode.UNSUPPORTED_CLOUDFLARE_CAPABILITY,
            "fixture capability is not in the bounded normalizer allowlist",
            "capability_id",
        )
    tenant_ref = _require_reference(resolved["tenant_ref"], "tenant_ref")
    account_ref = _require_reference(resolved["account_ref"], "account_ref")
    zone_ref = _require_reference(resolved["zone_ref"], "zone_ref")
    observed_at = _require_text(resolved["observed_at"], "observed_at")
    if not observed_at.startswith("fixture-"):
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture observation marker cannot appear live",
            "observed_at",
        )
    try:
        completeness = CloudflareCompleteness(resolved["completeness"])
    except (TypeError, ValueError):
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture completeness is not canonical",
            "completeness",
        )
        raise AssertionError("unreachable")
    fixture_items = resolved["items"]
    if not isinstance(fixture_items, tuple) or len(fixture_items) > _MAX_ITEMS:
        _deny(
            CloudflareErrorCode.INVALID_FIXTURE_SHAPE,
            "fixture items must be an immutable bounded tuple",
            "items",
        )
    items = tuple(_normalize_item(item) for item in fixture_items)
    canonical_refs = tuple(item.canonical_ref for item in items)
    provider_refs = tuple(item.provider_native_ref for item in items)
    if len(set(canonical_refs)) != len(canonical_refs):
        _deny(
            CloudflareErrorCode.FIXTURE_NORMALIZATION_FAILED,
            "fixture contains a duplicate canonical entity",
            "items",
        )
    if len(set(provider_refs)) != len(provider_refs):
        _deny(
            CloudflareErrorCode.FIXTURE_NORMALIZATION_FAILED,
            "fixture contains a conflicting provider entity reference",
            "items",
        )
    return CloudflareFixtureReadResult(
        capability_id=CapabilityId(capability_id),
        tenant_ref=tenant_ref,
        account_ref=account_ref,
        zone_ref=zone_ref,
        observed_at=observed_at,
        state_digest=_state_digest(items),
        completeness=completeness,
        items=items,
        provenance=(
            ("source", "synthetic-cloudflare-fixture"),
            ("evidence_class", "fixture-only"),
            ("provider_request", "not-performed"),
        ),
        trust=CloudflareFixtureTrust.UNTRUSTED_PROVIDER_CONTENT,
        fixture_only=True,
        provider_request_id=None,
        provider_authenticated=False,
        provider_request_occurred=False,
    )
