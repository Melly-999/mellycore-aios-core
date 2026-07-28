"""Stage B controlled-activation layer for the MellyCore OpenAI Batch integration.

This module owns every deterministic, local, no-network check an operator
needs before a live Batch submission could ever be considered: pricing
evidence loading and integrity, exact-model and request-envelope
enforcement, Decimal cost estimation against a hard dollar cap, one-time
authorization-artifact validation and consumption, and local preflight-record
construction.

Scope boundary (Stage B): everything in this module is planning and
validation only. Nothing here imports the ``openai`` package, constructs a
provider client, opens a socket, or reads/prints a credential *value*.
:mod:`scripts.mellycore_batch.policy` remains the single source of truth for
whether a live connection is allowed, and that answer stays hardcoded
``False`` regardless of anything this module computes. See
``stage_b_kill_switch_state`` below: ``stage_c_live_execution_authorized`` is
a hardcoded constant, not derived from any manifest, artifact, environment
variable, or CLI flag accepted by this module.

Pricing-evidence digest canonicalization rule (authoritative; used by both
:func:`compute_pricing_evidence_digest` and
:func:`verify_pricing_evidence_digest`):

    1. Take the pricing-manifest mapping and drop the ``evidence_digest`` key
       itself, if present (a digest cannot cover its own value).
    2. Serialize the remaining mapping with
       ``json.dumps(payload, sort_keys=True, separators=(",", ":"),
       ensure_ascii=True)`` -- deterministic key order, no incidental
       whitespace, pure-ASCII output so the digest never depends on how a
       given Python build normalizes non-ASCII text.
    3. UTF-8 encode the resulting string.
    4. SHA-256 the bytes and hex-encode the digest, lowercase.

There is exactly one accepted serialization; any other canonicalization
(different key order, added whitespace, different float/decimal formatting)
produces a different digest and is treated as *wrong* evidence, never as
"equivalent" evidence that happens to hash differently.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from .jsonl import repo_root
from .models import BatchOpsError, BatchRequest

# --- Stage B dual-lock constants ---------------------------------------------
# These are hardcoded in Python and are one half of the "dual lock". The
# pricing manifest (openai_batch_pricing.json) is the other half. Activation
# planning is refused unless the two agree exactly -- see
# `enforce_manifest_matches_constants`. The JSON manifest alone can never
# widen any of these values: a manifest claiming a larger limit, a cheaper
# cap, or a different model than the constants below is treated as invalid
# evidence, not as an authoritative override.

STAGE_B_PROVIDER = "openai"
STAGE_B_ENDPOINT = "/v1/responses"
STAGE_B_MODEL = "gpt-5.4-nano-2026-03-17"
STAGE_B_PROCESSING_REGION = "standard"

STAGE_B_MAX_REQUESTS = 3
STAGE_B_MAX_INPUT_BYTES = 65536
STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST = 512
STAGE_B_MAX_TOTAL_OUTPUT_TOKENS = 1536
STAGE_B_HARD_COST_CAP_USD = Decimal("0.01")
STAGE_B_AUTOMATIC_RETRIES = 0
STAGE_B_AUTOMATIC_RESUBMISSION = False

#: Approved Batch API prices per 1,000,000 tokens (Decimal only -- never a
#: binary float). Cached-input tokens are always assumed to be zero (the most
#: conservative assumption) when estimating cost; the cached-input rate is
#: retained here only for dual-lock agreement with the pricing manifest.
STAGE_B_PRICE_INPUT_PER_MILLION = Decimal("0.10")
STAGE_B_PRICE_CACHED_INPUT_PER_MILLION = Decimal("0.01")
STAGE_B_PRICE_OUTPUT_PER_MILLION = Decimal("0.625")
STAGE_B_PRICING_UNIT_TOKENS_INT = 1_000_000
STAGE_B_PRICING_UNIT_TOKENS = Decimal(STAGE_B_PRICING_UNIT_TOKENS_INT)

#: Only these top-level request-body keys are ever accepted. Anything else --
#: tools, tool_choice, service_tier, region overrides, or any other
#: provider-specific capability this package has not explicitly reviewed --
#: is rejected outright as an "unrecognized capability" rather than silently
#: stripped. This is an allowlist, not a blocklist, so a *new* OpenAI request
#: field this package has never seen is refused by default, not accepted by
#: default.
STAGE_B_ALLOWED_BODY_KEYS = frozenset({"model", "input", "max_output_tokens"})

#: Content-item ``type`` values that indicate a non-text-only capability
#: (image, file, or audio input) and must be refused.
_PROHIBITED_CONTENT_TYPES = frozenset(
    {
        "input_image",
        "input_file",
        "input_audio",
        "image_url",
        "output_image",
        "computer_call",
        "computer_call_output",
        "web_search",
        "web_search_preview",
        "file_search",
        "code_interpreter",
    }
)

_EXTERNAL_URL_PATTERN = re.compile(r"(?i)\b(?:https?|ftp)://")
_PROHIBITED_NESTED_KEYS = frozenset(
    {
        "tools",
        "tool_choice",
        "web_search",
        "file_search",
        "code_interpreter",
        "file_id",
        "file_url",
        "image_url",
        "audio",
        "audio_url",
        "retrieval",
        "remote_url",
        "service_tier",
        "processing_region",
        "region",
        "data_residency",
        "retry",
        "retries",
        "resubmit",
        "resubmission",
    }
)
_AUTHORIZATION_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,199}$")
_TASK_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,199}$")
_COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")

#: Default location of the pricing-evidence manifest shipped with this package.
DEFAULT_PRICING_MANIFEST_PATH = (
    Path(__file__).resolve().parent / "openai_batch_pricing.json"
)

_REQUIRED_PRICING_FIELDS: Dict[str, type] = {
    "schema_version": int,
    "provider": str,
    "endpoint": str,
    "model": str,
    "processing_region": str,
    "currency": str,
    "pricing_unit_tokens": int,
    "synchronous": dict,
    "batch": dict,
    "batch_discount_percent": str,
    "cached_input_assumed": bool,
    "verified_at": str,
    "valid_until": str,
    "maximum_requests": int,
    "maximum_input_bytes": int,
    "maximum_output_tokens_per_request": int,
    "maximum_total_output_tokens": int,
    "hard_cost_cap_usd": str,
    "automatic_retries": int,
    "automatic_resubmission": bool,
    "tools_allowed": bool,
    "files_allowed": bool,
    "images_allowed": bool,
    "external_retrieval_allowed": bool,
    "source_urls": list,
    "evidence_digest": str,
}

_REQUIRED_AUTHORIZATION_FIELDS: Dict[str, type] = {
    "schema_version": int,
    "authorization_id": str,
    "task_id": str,
    "issued_at": str,
    "expires_at": str,
    "canonical_base_sha": str,
    "activation_commit_sha": str,
    "provider": str,
    "endpoint": str,
    "model": str,
    "maximum_cost": str,
    "maximum_requests": int,
    "maximum_input_bytes": int,
    "maximum_output_tokens_per_request": int,
    "maximum_total_output_tokens": int,
    "one_time_use": bool,
}


# --- Exceptions ----------------------------------------------------------------


class ActivationError(BatchOpsError):
    """Base class for all Stage B activation-control failures."""


class PricingManifestError(ActivationError):
    """The pricing-evidence manifest is missing, malformed, or untrustworthy."""


class PricingManifestSchemaError(PricingManifestError):
    """The pricing manifest is missing a required field or has the wrong type."""


class PricingManifestDigestMismatchError(PricingManifestError):
    """The pricing manifest's stored ``evidence_digest`` does not match its content."""


class PricingEvidenceExpiredError(PricingManifestError):
    """The pricing evidence is outside its verified validity window."""


class PricingManifestConstantMismatchError(PricingManifestError):
    """The pricing manifest disagrees with the hardcoded Stage B constants.

    This is the dual-lock failure mode: the JSON manifest can never widen the
    envelope beyond what is hardcoded in this module, so any disagreement --
    in either direction -- is fail-closed, not resolved by taking whichever
    value is more permissive.
    """


class ModelMismatchError(ActivationError):
    """A request body names a model other than the exact approved model."""


class RequestEnvelopeExceededError(ActivationError):
    """A manifest exceeds the approved Stage B request/input/output envelope."""


class ProhibitedCapabilityError(ActivationError):
    """A request body uses a capability Stage B does not permit."""


class CostCapExceededError(ActivationError):
    """The estimated maximum cost exceeds the authorized hard-dollar cap."""


class AuthorizationArtifactError(ActivationError):
    """Base class for one-time authorization-artifact failures."""


class AuthorizationArtifactSchemaError(AuthorizationArtifactError):
    """The authorization artifact is missing a required field or has the wrong type."""


class AuthorizationArtifactInvalidError(AuthorizationArtifactError):
    """The authorization artifact does not bind to the expected activation context."""


class AuthorizationArtifactExpiredError(AuthorizationArtifactError):
    """The authorization artifact's ``expires_at`` has passed."""


class AuthorizationAlreadyConsumedError(AuthorizationArtifactError):
    """The authorization artifact has already been consumed once."""


# --- Dataclasses -----------------------------------------------------------------


@dataclass(frozen=True)
class StageBKillSwitch:
    """The hardcoded Stage B / Stage C authorization state.

    ``stage_c_live_execution_authorized`` is a literal constant below, not a
    field computed from any manifest, authorization artifact, environment
    variable, or CLI flag this module accepts. There is no code path in this
    module, or in any module that imports it, that can set it to ``True``.
    """

    stage_b_activation_controls_implemented: bool
    stage_c_live_execution_authorized: bool

    def to_dict(self) -> Dict[str, Any]:
        return {
            "stage_b_activation_controls_implemented": self.stage_b_activation_controls_implemented,
            "stage_c_live_execution_authorized": self.stage_c_live_execution_authorized,
        }


def stage_b_kill_switch_state() -> StageBKillSwitch:
    """Return the current, hardcoded Stage B/C authorization state.

    Always ``stage_b_activation_controls_implemented=True`` (this module
    exists) and ``stage_c_live_execution_authorized=False`` (Stage C remains
    separately unauthorized). Takes no arguments; there is nothing a caller
    can pass that changes the result.
    """
    return StageBKillSwitch(
        stage_b_activation_controls_implemented=True,
        stage_c_live_execution_authorized=False,
    )


@dataclass(frozen=True)
class BoundedPollingConfig:
    """Definition-only bounded-polling parameters.

    Nothing in this package executes a polling loop. This dataclass exists so
    a future, separately authorized Stage C implementation has a single,
    already-reviewed place to read these bounds from, and so this task can
    assert their values without writing any loop that would run them.
    """

    max_polling_attempts: int = 12
    min_polling_interval_seconds: int = 60
    automatic_retries: int = STAGE_B_AUTOMATIC_RETRIES
    automatic_resubmission: bool = STAGE_B_AUTOMATIC_RESUBMISSION


STAGE_B_POLLING_CONFIG = BoundedPollingConfig()


@dataclass(frozen=True)
class RequestEnvelopeReport:
    """Facts established while enforcing the Stage B request envelope."""

    request_count: int
    input_byte_count: int
    total_max_output_tokens: int
    per_request_max_output_tokens: Tuple[int, ...]


@dataclass(frozen=True)
class CostEstimate:
    """A Decimal cost estimate and the cap it was checked against."""

    input_byte_count: int
    total_max_output_tokens: int
    input_cost: Decimal
    output_cost: Decimal
    estimated_maximum_cost: Decimal
    hard_cost_cap_usd: Decimal

    def to_dict(self) -> Dict[str, Any]:
        return {
            "input_byte_count": self.input_byte_count,
            "total_max_output_tokens": self.total_max_output_tokens,
            "input_cost": str(self.input_cost),
            "output_cost": str(self.output_cost),
            "estimated_maximum_cost": str(self.estimated_maximum_cost),
            "hard_cost_cap_usd": str(self.hard_cost_cap_usd),
        }


@dataclass(frozen=True)
class AuthorizationArtifact:
    """A local, non-secret, one-time Stage C authorization artifact.

    Never carries an API key, credential value, or account identifier --
    only identifiers, timestamps, and the exact caps it authorizes.
    """

    schema_version: int
    authorization_id: str
    task_id: str
    issued_at: str
    expires_at: str
    canonical_base_sha: str
    activation_commit_sha: str
    provider: str
    endpoint: str
    model: str
    maximum_cost: str
    maximum_requests: int
    maximum_input_bytes: int
    maximum_output_tokens_per_request: int
    maximum_total_output_tokens: int
    one_time_use: bool


@dataclass(frozen=True)
class PreflightRecord:
    """The truthful, local, no-network audit record a preflight run produces.

    Every Stage B run of this record sets ``execution_authorized=False`` and
    ``migration_trigger_5_crossed=False`` unconditionally -- these are not
    derived from the rest of the record's contents. All provider-side fields
    stay ``None``: nothing in this package ever populates them, because
    nothing in this package ever reaches the provider.
    """

    task_id: str
    authorization_id: Optional[str]
    canonical_commit_sha: str
    activation_commit_sha: str
    provider: str
    endpoint: str
    model: str
    request_count: int
    input_jsonl_sha256: Optional[str]
    input_jsonl_size: int
    completion_window: str
    maximum_output_tokens_per_request: int
    maximum_total_output_tokens: int
    pricing_verified_at: str
    pricing_valid_until: str
    estimated_maximum_cost: str
    authorized_hard_cost_cap: str
    processing_region: str
    automatic_retries: int
    automatic_resubmission: bool
    credential_present: bool
    credential_value_logged: bool
    execution_authorized: bool
    migration_trigger_5_crossed: bool
    input_file_id: Optional[str] = None
    batch_id: Optional[str] = None
    output_file_id: Optional[str] = None
    error_file_id: Optional[str] = None
    provider_request_id: Optional[str] = None
    actual_token_usage: Optional[Dict[str, int]] = None
    actual_cost: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "task_id": self.task_id,
            "authorization_id": self.authorization_id,
            "canonical_commit_sha": self.canonical_commit_sha,
            "activation_commit_sha": self.activation_commit_sha,
            "provider": self.provider,
            "endpoint": self.endpoint,
            "model": self.model,
            "request_count": self.request_count,
            "input_jsonl_sha256": self.input_jsonl_sha256,
            "input_jsonl_size": self.input_jsonl_size,
            "completion_window": self.completion_window,
            "maximum_output_tokens_per_request": self.maximum_output_tokens_per_request,
            "maximum_total_output_tokens": self.maximum_total_output_tokens,
            "pricing_verified_at": self.pricing_verified_at,
            "pricing_valid_until": self.pricing_valid_until,
            "estimated_maximum_cost": self.estimated_maximum_cost,
            "authorized_hard_cost_cap": self.authorized_hard_cost_cap,
            "processing_region": self.processing_region,
            "automatic_retries": self.automatic_retries,
            "automatic_resubmission": self.automatic_resubmission,
            "credential_present": self.credential_present,
            "credential_value_logged": self.credential_value_logged,
            "execution_authorized": self.execution_authorized,
            "migration_trigger_5_crossed": self.migration_trigger_5_crossed,
            "input_file_id": self.input_file_id,
            "batch_id": self.batch_id,
            "output_file_id": self.output_file_id,
            "error_file_id": self.error_file_id,
            "provider_request_id": self.provider_request_id,
            "actual_token_usage": self.actual_token_usage,
            "actual_cost": self.actual_cost,
        }


# --- Pricing-evidence manifest: loading, schema, digest, freshness -------------


def load_pricing_manifest(path: Optional[Path] = None) -> Dict[str, Any]:
    """Load and schema-validate the pricing-evidence manifest. Read-only, no network."""
    manifest_path = Path(path) if path is not None else DEFAULT_PRICING_MANIFEST_PATH
    try:
        text = manifest_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise PricingManifestError(
            "cannot read pricing manifest {}: {}".format(manifest_path, exc)
        ) from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PricingManifestSchemaError(
            "pricing manifest {} is not valid JSON: {}".format(manifest_path, exc)
        ) from exc
    if not isinstance(data, dict):
        raise PricingManifestSchemaError(
            "pricing manifest {} must contain a JSON object".format(manifest_path)
        )
    validate_pricing_manifest_schema(data)
    return data


def validate_pricing_manifest_schema(manifest: Dict[str, Any]) -> None:
    """Check every required pricing-manifest field is present with the correct type."""
    missing = [key for key in _REQUIRED_PRICING_FIELDS if key not in manifest]
    if missing:
        raise PricingManifestSchemaError(
            "pricing manifest is missing required field(s): {}".format(
                ", ".join(sorted(missing))
            )
        )
    unexpected = sorted(set(manifest) - set(_REQUIRED_PRICING_FIELDS))
    if unexpected:
        raise PricingManifestSchemaError(
            "pricing manifest contains unexpected field(s): {}".format(
                ", ".join(unexpected)
            )
        )
    wrong_type = []
    for key, expected_type in _REQUIRED_PRICING_FIELDS.items():
        value = manifest[key]
        if expected_type is bool:
            if not isinstance(value, bool):
                wrong_type.append(key)
        elif expected_type is int:
            if isinstance(value, bool) or not isinstance(value, int):
                wrong_type.append(key)
        elif not isinstance(value, expected_type):
            wrong_type.append(key)
    if wrong_type:
        raise PricingManifestSchemaError(
            "pricing manifest field(s) have the wrong type: {}".format(
                ", ".join(sorted(wrong_type))
            )
        )
    if manifest["schema_version"] != 1:
        raise PricingManifestSchemaError(
            "pricing manifest 'schema_version' must be exactly 1"
        )
    for pricing_block_name in ("synchronous", "batch"):
        block = manifest[pricing_block_name]
        unexpected_pricing_fields = sorted(
            set(block) - {"input", "cached_input", "output"}
        )
        if unexpected_pricing_fields:
            raise PricingManifestSchemaError(
                "pricing manifest {!r} block contains unexpected field(s): {}".format(
                    pricing_block_name, ", ".join(unexpected_pricing_fields)
                )
            )
        for sub_key in ("input", "cached_input", "output"):
            if sub_key not in block or not isinstance(block[sub_key], str):
                raise PricingManifestSchemaError(
                    "pricing manifest {!r} block is missing string field {!r}".format(
                        pricing_block_name, sub_key
                    )
                )


def compute_pricing_evidence_digest(manifest: Dict[str, Any]) -> str:
    """Compute the canonical evidence digest for a pricing manifest.

    See the module docstring for the exact, authoritative canonicalization
    rule. ``evidence_digest`` itself is excluded from what gets hashed.
    """
    payload = {
        key: value for key, value in manifest.items() if key != "evidence_digest"
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def verify_pricing_evidence_digest(manifest: Dict[str, Any]) -> None:
    """Fail closed unless ``manifest['evidence_digest']`` matches its own content."""
    stored = manifest.get("evidence_digest")
    if not isinstance(stored, str) or not stored:
        raise PricingManifestSchemaError(
            "pricing manifest is missing a string 'evidence_digest'"
        )
    computed = compute_pricing_evidence_digest(manifest)
    if not _constant_time_eq(stored.lower(), computed.lower()):
        raise PricingManifestDigestMismatchError(
            "pricing manifest evidence_digest {!r} does not match its computed digest {!r}; "
            "the manifest content may have been altered after being verified".format(
                stored, computed
            )
        )


def enforce_pricing_freshness(manifest: Dict[str, Any], now: datetime) -> None:
    """Fail closed unless ``now`` falls within the manifest's verified validity window.

    ``now`` is always supplied by the caller (never read from the wall clock
    inside this function), so this check is deterministic and testable.
    """
    now = _ensure_aware_utc(now)
    verified_at = _parse_iso8601(manifest["verified_at"], field_name="verified_at")
    valid_until = _parse_iso8601(manifest["valid_until"], field_name="valid_until")
    if valid_until <= verified_at:
        raise PricingEvidenceExpiredError(
            "pricing manifest 'valid_until' ({}) must be after 'verified_at' ({})".format(
                manifest["valid_until"], manifest["verified_at"]
            )
        )
    if verified_at > now:
        raise PricingEvidenceExpiredError(
            "pricing manifest 'verified_at' ({}) is in the future relative to now ({})".format(
                manifest["verified_at"], now.isoformat()
            )
        )
    if now > valid_until:
        raise PricingEvidenceExpiredError(
            "pricing evidence expired: 'valid_until' ({}) is before now ({})".format(
                manifest["valid_until"], now.isoformat()
            )
        )


def enforce_manifest_matches_constants(manifest: Dict[str, Any]) -> None:
    """Fail closed unless the pricing manifest agrees exactly with the hardcoded constants.

    This is the dual lock: the JSON manifest can only ever narrow or match the
    Python constants, never widen them. Any disagreement in either direction
    -- not just ones that would be more permissive -- blocks activation
    planning outright, so a manifest edited to *tighten* a limit without a
    matching code change also fails closed rather than being silently
    accepted as "even safer".
    """
    mismatches: List[str] = []

    def _check(field_name: str, expected: Any) -> None:
        actual = manifest.get(field_name)
        if actual != expected:
            mismatches.append(
                "{}: manifest={!r} constant={!r}".format(field_name, actual, expected)
            )

    _check("provider", STAGE_B_PROVIDER)
    _check("endpoint", STAGE_B_ENDPOINT)
    _check("model", STAGE_B_MODEL)
    _check("processing_region", STAGE_B_PROCESSING_REGION)
    _check("currency", "USD")
    _check("pricing_unit_tokens", STAGE_B_PRICING_UNIT_TOKENS_INT)
    _check("cached_input_assumed", False)
    _check("maximum_requests", STAGE_B_MAX_REQUESTS)
    _check("maximum_input_bytes", STAGE_B_MAX_INPUT_BYTES)
    _check("maximum_output_tokens_per_request", STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST)
    _check("maximum_total_output_tokens", STAGE_B_MAX_TOTAL_OUTPUT_TOKENS)
    _check("automatic_retries", STAGE_B_AUTOMATIC_RETRIES)
    _check("automatic_resubmission", STAGE_B_AUTOMATIC_RESUBMISSION)
    _check("tools_allowed", False)
    _check("files_allowed", False)
    _check("images_allowed", False)
    _check("external_retrieval_allowed", False)

    if _to_decimal(manifest.get("hard_cost_cap_usd")) != STAGE_B_HARD_COST_CAP_USD:
        mismatches.append(
            "hard_cost_cap_usd: manifest={!r} constant={!r}".format(
                manifest.get("hard_cost_cap_usd"), str(STAGE_B_HARD_COST_CAP_USD)
            )
        )

    batch_prices = manifest.get("batch") or {}
    price_checks = (
        ("batch.input", batch_prices.get("input"), STAGE_B_PRICE_INPUT_PER_MILLION),
        (
            "batch.cached_input",
            batch_prices.get("cached_input"),
            STAGE_B_PRICE_CACHED_INPUT_PER_MILLION,
        ),
        ("batch.output", batch_prices.get("output"), STAGE_B_PRICE_OUTPUT_PER_MILLION),
    )
    for label, raw_value, expected_decimal in price_checks:
        if _to_decimal(raw_value) != expected_decimal:
            mismatches.append(
                "{}: manifest={!r} constant={!r}".format(
                    label, raw_value, str(expected_decimal)
                )
            )

    if mismatches:
        raise PricingManifestConstantMismatchError(
            "pricing manifest disagrees with hardcoded Stage B constants (dual lock failed): {}".format(
                "; ".join(mismatches)
            )
        )


def validate_pricing_evidence(manifest: Dict[str, Any], now: datetime) -> None:
    """Run every pricing-evidence check activation planning depends on, in order."""
    validate_pricing_manifest_schema(manifest)
    verify_pricing_evidence_digest(manifest)
    enforce_manifest_matches_constants(manifest)
    enforce_pricing_freshness(manifest, now)


# --- Request envelope, exact-model, and prohibited-capability enforcement ------


def enforce_exact_model(model: Any, *, custom_id: str = "") -> None:
    """Fail closed unless ``model`` is exactly :data:`STAGE_B_MODEL`.

    Rejects aliases, a different model string, a missing model, and any
    non-string value -- there is no fuzzy or prefix match.
    """
    if not isinstance(model, str) or model != STAGE_B_MODEL:
        raise ModelMismatchError(
            "request {!r} names model {!r}; Stage B only approves the exact model {!r}".format(
                custom_id or "<unknown>", model, STAGE_B_MODEL
            )
        )


def detect_prohibited_capabilities(body: Dict[str, Any]) -> List[str]:
    """Return a list of findings for any capability Stage B does not permit.

    Uses an allowlist for top-level body keys (see
    :data:`STAGE_B_ALLOWED_BODY_KEYS`) so an unrecognized provider-specific
    field is rejected by default, then recursively scans the ``input`` value
    for embedded image/file/audio content items and external URLs. An empty
    list means no prohibited capability was found; this function never
    mutates or strips anything.
    """
    findings: List[str] = []
    for key in body.keys():
        if key not in STAGE_B_ALLOWED_BODY_KEYS:
            findings.append("unrecognized_body_key:{}".format(key))
    findings.extend(_scan_for_prohibited_content(body.get("input"), "input"))
    return findings


def _scan_for_prohibited_content(value: Any, path: str) -> List[str]:
    findings: List[str] = []
    if isinstance(value, str):
        if _EXTERNAL_URL_PATTERN.search(value):
            findings.append("external_url_at:{}".format(path))
    elif isinstance(value, dict):
        type_field = value.get("type")
        if isinstance(type_field, str) and type_field in _PROHIBITED_CONTENT_TYPES:
            findings.append("prohibited_content_type_at:{}={}".format(path, type_field))
        for key, sub_value in value.items():
            if key in _PROHIBITED_NESTED_KEYS:
                findings.append("prohibited_nested_key_at:{}.{}".format(path, key))
            findings.extend(
                _scan_for_prohibited_content(sub_value, "{}.{}".format(path, key))
            )
    elif isinstance(value, list):
        for index, item in enumerate(value):
            findings.extend(
                _scan_for_prohibited_content(item, "{}[{}]".format(path, index))
            )
    return findings


def enforce_request_envelope(
    requests: Sequence[BatchRequest], input_byte_count: int
) -> RequestEnvelopeReport:
    """Fail closed unless ``requests`` fits entirely inside the Stage B envelope.

    Checks, in order: at least one request; request count within
    :data:`STAGE_B_MAX_REQUESTS`; input byte size within
    :data:`STAGE_B_MAX_INPUT_BYTES`; every request names the exact approved
    model; every request has a present, positive, integer
    ``max_output_tokens`` within :data:`STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST`;
    no request uses a prohibited capability; and the sum of every request's
    ``max_output_tokens`` is within :data:`STAGE_B_MAX_TOTAL_OUTPUT_TOKENS`.
    """
    if (
        isinstance(input_byte_count, bool)
        or not isinstance(input_byte_count, int)
        or input_byte_count < 0
    ):
        raise RequestEnvelopeExceededError(
            "input_byte_count must be a non-negative integer; got {!r}".format(
                input_byte_count
            )
        )

    if not requests:
        raise RequestEnvelopeExceededError("at least one request is required")

    if len(requests) > STAGE_B_MAX_REQUESTS:
        raise RequestEnvelopeExceededError(
            "{} requests exceeds the Stage B maximum of {}".format(
                len(requests), STAGE_B_MAX_REQUESTS
            )
        )

    if input_byte_count > STAGE_B_MAX_INPUT_BYTES:
        raise RequestEnvelopeExceededError(
            "{}-byte input exceeds the Stage B maximum of {} bytes".format(
                input_byte_count, STAGE_B_MAX_INPUT_BYTES
            )
        )

    per_request_tokens: List[int] = []
    for request in requests:
        body = request.body if isinstance(request.body, dict) else {}
        enforce_exact_model(body.get("model"), custom_id=request.custom_id)

        max_output_tokens = body.get("max_output_tokens")
        if isinstance(max_output_tokens, bool) or not isinstance(
            max_output_tokens, int
        ):
            raise RequestEnvelopeExceededError(
                "request {!r} must set an integer 'max_output_tokens'; got {!r}".format(
                    request.custom_id, max_output_tokens
                )
            )
        if max_output_tokens <= 0:
            raise RequestEnvelopeExceededError(
                "request {!r} 'max_output_tokens' must be > 0; got {}".format(
                    request.custom_id, max_output_tokens
                )
            )
        if max_output_tokens > STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST:
            raise RequestEnvelopeExceededError(
                "request {!r} 'max_output_tokens' {} exceeds the Stage B per-request maximum of {}".format(
                    request.custom_id,
                    max_output_tokens,
                    STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST,
                )
            )
        per_request_tokens.append(max_output_tokens)

        findings = detect_prohibited_capabilities(body)
        if findings:
            raise ProhibitedCapabilityError(
                "request {!r} uses prohibited capability/capabilities: {}".format(
                    request.custom_id, ", ".join(findings)
                )
            )

    total_max_output_tokens = sum(per_request_tokens)
    if total_max_output_tokens > STAGE_B_MAX_TOTAL_OUTPUT_TOKENS:
        raise RequestEnvelopeExceededError(
            "total max_output_tokens {} exceeds the Stage B maximum of {}".format(
                total_max_output_tokens, STAGE_B_MAX_TOTAL_OUTPUT_TOKENS
            )
        )

    return RequestEnvelopeReport(
        request_count=len(requests),
        input_byte_count=input_byte_count,
        total_max_output_tokens=total_max_output_tokens,
        per_request_max_output_tokens=tuple(per_request_tokens),
    )


# --- Decimal cost estimation -----------------------------------------------------


def estimate_cost(input_byte_count: int, total_max_output_tokens: int) -> CostEstimate:
    """Estimate the worst-case cost of a Stage B batch using Decimal arithmetic only.

    Assumes zero cached input tokens (the most conservative assumption).
    Never rounds down and never uses a binary float anywhere in the
    computation.
    """
    for field_name, value in (
        ("input_byte_count", input_byte_count),
        ("total_max_output_tokens", total_max_output_tokens),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ActivationError(
                "{} must be a non-negative integer; got {!r}".format(field_name, value)
            )
    input_cost = (
        Decimal(input_byte_count)
        * STAGE_B_PRICE_INPUT_PER_MILLION
        / STAGE_B_PRICING_UNIT_TOKENS
    )
    output_cost = (
        Decimal(total_max_output_tokens)
        * STAGE_B_PRICE_OUTPUT_PER_MILLION
        / STAGE_B_PRICING_UNIT_TOKENS
    )
    estimated_maximum_cost = input_cost + output_cost
    return CostEstimate(
        input_byte_count=input_byte_count,
        total_max_output_tokens=total_max_output_tokens,
        input_cost=input_cost,
        output_cost=output_cost,
        estimated_maximum_cost=estimated_maximum_cost,
        hard_cost_cap_usd=STAGE_B_HARD_COST_CAP_USD,
    )


def enforce_cost_cap(estimate: CostEstimate) -> None:
    """Fail closed unless ``estimate.estimated_maximum_cost`` is within the hard cap."""
    if estimate.estimated_maximum_cost > estimate.hard_cost_cap_usd:
        raise CostCapExceededError(
            "estimated maximum cost {} exceeds the authorized hard cost cap {}".format(
                estimate.estimated_maximum_cost, estimate.hard_cost_cap_usd
            )
        )


# --- One-time authorization artifact: parsing, validation, consumption ---------


def parse_authorization_artifact(data: Dict[str, Any]) -> AuthorizationArtifact:
    """Parse and schema-validate a raw authorization-artifact mapping."""
    if not isinstance(data, dict):
        raise AuthorizationArtifactSchemaError(
            "authorization artifact must be a JSON object"
        )

    missing = [key for key in _REQUIRED_AUTHORIZATION_FIELDS if key not in data]
    if missing:
        raise AuthorizationArtifactSchemaError(
            "authorization artifact is missing required field(s): {}".format(
                ", ".join(sorted(missing))
            )
        )

    wrong_type = []
    for key, expected_type in _REQUIRED_AUTHORIZATION_FIELDS.items():
        value = data[key]
        if expected_type is bool:
            if not isinstance(value, bool):
                wrong_type.append(key)
        elif expected_type is int:
            if isinstance(value, bool) or not isinstance(value, int):
                wrong_type.append(key)
        elif not isinstance(value, expected_type):
            wrong_type.append(key)
    if wrong_type:
        raise AuthorizationArtifactSchemaError(
            "authorization artifact field(s) have the wrong type: {}".format(
                ", ".join(sorted(wrong_type))
            )
        )

    #: Defense in depth: an authorization artifact is explicitly documented as
    #: non-secret (identifiers, timestamps, and caps only). Rather than
    #: pattern-matching key names against a credential-word list -- which
    #: would false-positive on legitimate reviewed fields like
    #: ``maximum_output_tokens_per_request`` (it contains "token") -- this
    #: allowlists the exact reviewed schema: any key beyond the required set
    #: is refused outright, whatever it is named or contains.
    unexpected = sorted(set(data.keys()) - set(_REQUIRED_AUTHORIZATION_FIELDS.keys()))
    if unexpected:
        raise AuthorizationArtifactSchemaError(
            "authorization artifact contains unexpected field(s) outside the reviewed schema, "
            "refusing to load (never accepts credential values or any other extra field): {}".format(
                ", ".join(unexpected)
            )
        )
    if data["schema_version"] != 1:
        raise AuthorizationArtifactSchemaError(
            "authorization artifact 'schema_version' must be exactly 1"
        )
    if not _AUTHORIZATION_ID_RE.fullmatch(data["authorization_id"]):
        raise AuthorizationArtifactSchemaError(
            "authorization artifact 'authorization_id' is malformed"
        )
    if not _TASK_ID_RE.fullmatch(data["task_id"]):
        raise AuthorizationArtifactSchemaError(
            "authorization artifact 'task_id' is malformed"
        )
    for field_name in ("canonical_base_sha", "activation_commit_sha"):
        if not _COMMIT_SHA_RE.fullmatch(data[field_name]):
            raise AuthorizationArtifactSchemaError(
                "authorization artifact {!r} must be a lowercase 40-character commit SHA".format(
                    field_name
                )
            )

    return AuthorizationArtifact(
        schema_version=data["schema_version"],
        authorization_id=data["authorization_id"],
        task_id=data["task_id"],
        issued_at=data["issued_at"],
        expires_at=data["expires_at"],
        canonical_base_sha=data["canonical_base_sha"],
        activation_commit_sha=data["activation_commit_sha"],
        provider=data["provider"],
        endpoint=data["endpoint"],
        model=data["model"],
        maximum_cost=data["maximum_cost"],
        maximum_requests=data["maximum_requests"],
        maximum_input_bytes=data["maximum_input_bytes"],
        maximum_output_tokens_per_request=data["maximum_output_tokens_per_request"],
        maximum_total_output_tokens=data["maximum_total_output_tokens"],
        one_time_use=data["one_time_use"],
    )


def load_authorization_artifact(path: Path) -> AuthorizationArtifact:
    """Load and parse an authorization-artifact JSON file. Read-only, no network."""
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise AuthorizationArtifactSchemaError(
            "cannot read authorization artifact {}: {}".format(path, exc)
        ) from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise AuthorizationArtifactSchemaError(
            "authorization artifact {} is not valid JSON: {}".format(path, exc)
        ) from exc
    return parse_authorization_artifact(data)


def validate_authorization_artifact(
    artifact: AuthorizationArtifact,
    *,
    now: datetime,
    expected_canonical_base_sha: str,
    expected_activation_commit_sha: str,
    expected_task_id: Optional[str] = None,
    expected_model: str = STAGE_B_MODEL,
    expected_provider: str = STAGE_B_PROVIDER,
    expected_endpoint: str = STAGE_B_ENDPOINT,
    expected_max_cost: Decimal = STAGE_B_HARD_COST_CAP_USD,
    expected_max_requests: int = STAGE_B_MAX_REQUESTS,
    expected_max_input_bytes: int = STAGE_B_MAX_INPUT_BYTES,
    expected_max_output_tokens_per_request: int = STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST,
    expected_max_total_output_tokens: int = STAGE_B_MAX_TOTAL_OUTPUT_TOKENS,
    ledger_dir: Optional[Path] = None,
) -> None:
    """Fail closed unless ``artifact`` binds exactly to the expected activation context.

    Validation only -- never consumes the artifact. See
    :func:`consume_authorization` for the separate, one-time consumption step.
    """
    if not artifact.one_time_use:
        raise AuthorizationArtifactInvalidError(
            "authorization artifact {!r} does not set one_time_use=true".format(
                artifact.authorization_id
            )
        )

    now = _ensure_aware_utc(now)
    issued_at = _parse_authorization_timestamp(
        artifact.issued_at, field_name="issued_at"
    )
    expires_at = _parse_authorization_timestamp(
        artifact.expires_at, field_name="expires_at"
    )
    if now > expires_at:
        raise AuthorizationArtifactExpiredError(
            "authorization artifact {!r} expired at {} (now: {})".format(
                artifact.authorization_id, artifact.expires_at, now.isoformat()
            )
        )
    if expires_at <= issued_at:
        raise AuthorizationArtifactInvalidError(
            "authorization artifact {!r} expires_at must be after issued_at".format(
                artifact.authorization_id
            )
        )
    if issued_at > now:
        raise AuthorizationArtifactInvalidError(
            "authorization artifact {!r} issued_at is in the future".format(
                artifact.authorization_id
            )
        )
    mismatches: List[str] = []
    if expected_task_id is not None and artifact.task_id != expected_task_id:
        mismatches.append(
            "task_id: artifact={!r} expected={!r}".format(
                artifact.task_id, expected_task_id
            )
        )
    if artifact.canonical_base_sha != expected_canonical_base_sha:
        mismatches.append(
            "canonical_base_sha: artifact={!r} expected={!r}".format(
                artifact.canonical_base_sha, expected_canonical_base_sha
            )
        )
    if artifact.activation_commit_sha != expected_activation_commit_sha:
        mismatches.append(
            "activation_commit_sha: artifact={!r} expected={!r}".format(
                artifact.activation_commit_sha, expected_activation_commit_sha
            )
        )
    if artifact.provider != expected_provider:
        mismatches.append(
            "provider: artifact={!r} expected={!r}".format(
                artifact.provider, expected_provider
            )
        )
    if artifact.endpoint != expected_endpoint:
        mismatches.append(
            "endpoint: artifact={!r} expected={!r}".format(
                artifact.endpoint, expected_endpoint
            )
        )
    if artifact.model != expected_model:
        mismatches.append(
            "model: artifact={!r} expected={!r}".format(artifact.model, expected_model)
        )
    try:
        artifact_maximum_cost = _to_decimal(artifact.maximum_cost)
    except PricingManifestSchemaError as exc:
        raise AuthorizationArtifactInvalidError(str(exc)) from exc
    if artifact_maximum_cost != expected_max_cost:
        mismatches.append(
            "maximum_cost: artifact={!r} expected={!r}".format(
                artifact.maximum_cost, str(expected_max_cost)
            )
        )
    if artifact.maximum_requests != expected_max_requests:
        mismatches.append(
            "maximum_requests: artifact={!r} expected={!r}".format(
                artifact.maximum_requests, expected_max_requests
            )
        )
    if artifact.maximum_input_bytes != expected_max_input_bytes:
        mismatches.append(
            "maximum_input_bytes: artifact={!r} expected={!r}".format(
                artifact.maximum_input_bytes, expected_max_input_bytes
            )
        )
    if (
        artifact.maximum_output_tokens_per_request
        != expected_max_output_tokens_per_request
    ):
        mismatches.append(
            "maximum_output_tokens_per_request: artifact={!r} expected={!r}".format(
                artifact.maximum_output_tokens_per_request,
                expected_max_output_tokens_per_request,
            )
        )
    if artifact.maximum_total_output_tokens != expected_max_total_output_tokens:
        mismatches.append(
            "maximum_total_output_tokens: artifact={!r} expected={!r}".format(
                artifact.maximum_total_output_tokens, expected_max_total_output_tokens
            )
        )

    if mismatches:
        raise AuthorizationArtifactInvalidError(
            "authorization artifact {!r} does not bind to the expected activation context: {}".format(
                artifact.authorization_id, "; ".join(mismatches)
            )
        )
    if is_authorization_consumed(artifact.authorization_id, ledger_dir):
        raise AuthorizationAlreadyConsumedError(
            "authorization {!r} has already been consumed".format(
                artifact.authorization_id
            )
        )


def default_authorization_ledger_dir() -> Path:
    """The ignored, untracked local directory one-time authorization consumption is recorded in."""
    return repo_root() / ".runtime" / "batch" / "authorizations"


def is_authorization_consumed(
    authorization_id: str, ledger_dir: Optional[Path] = None
) -> bool:
    """Read-only check: has ``authorization_id`` already been consumed?"""
    ledger_dir = (
        Path(ledger_dir)
        if ledger_dir is not None
        else default_authorization_ledger_dir()
    )
    safe_id = _safe_ledger_filename(authorization_id)
    return (ledger_dir / "{}.consumed".format(safe_id)).exists()


def consume_authorization(
    authorization_id: str, ledger_dir: Optional[Path] = None
) -> Path:
    """Atomically, irreversibly mark ``authorization_id`` as consumed.

    Uses an exclusive file create (``O_CREAT | O_EXCL``) so two concurrent
    callers can never both succeed for the same ``authorization_id`` -- the
    second raises :class:`AuthorizationAlreadyConsumedError`. The marker file
    lives entirely under the ignored ``.runtime/batch/`` tree, never a
    tracked repository path.

    This function is never called from any Stage B CLI command -- Stage B
    preflight only *validates* an authorization artifact, it never consumes
    one. It is exposed here so its atomicity and reuse-rejection behavior are
    directly unit-testable without Stage C existing yet: only a hypothetical
    future, separately authorized Stage C execution attempt would call it,
    and that code path does not exist in this package.
    """
    safe_id = _safe_ledger_filename(authorization_id)
    ledger_dir = (
        Path(ledger_dir)
        if ledger_dir is not None
        else default_authorization_ledger_dir()
    )
    ledger_dir.mkdir(parents=True, exist_ok=True)
    marker = ledger_dir / "{}.consumed".format(safe_id)
    try:
        fd = os.open(str(marker), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise AuthorizationAlreadyConsumedError(
            "authorization {!r} has already been consumed".format(authorization_id)
        ) from exc
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "authorization_id": authorization_id,
                        "consumed_at": datetime.now(timezone.utc).isoformat(),
                    }
                )
            )
    except Exception:
        # Best-effort cleanup if writing the marker body fails after creation;
        # the exclusive-create above is what actually guarantees one-time use.
        try:
            marker.unlink()
        except OSError:
            pass
        raise
    return marker


def _safe_ledger_filename(authorization_id: str) -> str:
    if not isinstance(authorization_id, str) or not _AUTHORIZATION_ID_RE.fullmatch(
        authorization_id
    ):
        raise AuthorizationArtifactInvalidError(
            "authorization_id {!r} is not a safe ledger filename (letters, digits, '-', '_' only)".format(
                authorization_id
            )
        )
    return authorization_id


# --- Preflight record construction ------------------------------------------------


def build_preflight_record(
    *,
    task_id: str,
    authorization_id: Optional[str],
    canonical_commit_sha: str,
    activation_commit_sha: str,
    endpoint: str,
    completion_window: str,
    envelope: RequestEnvelopeReport,
    pricing_manifest: Dict[str, Any],
    cost_estimate: CostEstimate,
    input_jsonl_sha256: Optional[str],
    credential_present: bool,
) -> PreflightRecord:
    """Assemble the truthful local Stage B preflight audit record.

    ``execution_authorized`` and ``migration_trigger_5_crossed`` are always
    ``False`` here, independent of every other argument -- this function does
    not accept a parameter that could set either to ``True``.
    """
    if not isinstance(credential_present, bool):
        raise ActivationError("credential_present must be an actual Boolean")
    kill_switch = stage_b_kill_switch_state()
    return PreflightRecord(
        task_id=task_id,
        authorization_id=authorization_id,
        canonical_commit_sha=canonical_commit_sha,
        activation_commit_sha=activation_commit_sha,
        provider=STAGE_B_PROVIDER,
        endpoint=endpoint,
        model=STAGE_B_MODEL,
        request_count=envelope.request_count,
        input_jsonl_sha256=input_jsonl_sha256,
        input_jsonl_size=envelope.input_byte_count,
        completion_window=completion_window,
        maximum_output_tokens_per_request=STAGE_B_MAX_OUTPUT_TOKENS_PER_REQUEST,
        maximum_total_output_tokens=STAGE_B_MAX_TOTAL_OUTPUT_TOKENS,
        pricing_verified_at=pricing_manifest["verified_at"],
        pricing_valid_until=pricing_manifest["valid_until"],
        estimated_maximum_cost=str(cost_estimate.estimated_maximum_cost),
        authorized_hard_cost_cap=str(STAGE_B_HARD_COST_CAP_USD),
        processing_region=STAGE_B_PROCESSING_REGION,
        automatic_retries=STAGE_B_AUTOMATIC_RETRIES,
        automatic_resubmission=STAGE_B_AUTOMATIC_RESUBMISSION,
        credential_present=credential_present,
        credential_value_logged=False,
        execution_authorized=kill_switch.stage_c_live_execution_authorized,
        migration_trigger_5_crossed=False,
    )


# --- Small internal helpers -------------------------------------------------------


def _ensure_aware_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _parse_iso8601(value: str, *, field_name: str) -> datetime:
    if not isinstance(value, str) or not value:
        raise PricingManifestSchemaError(
            "field {!r} must be a non-empty ISO-8601 string".format(field_name)
        )
    normalized = value.replace("Z", "+00:00") if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise PricingManifestSchemaError(
            "field {!r} value {!r} is not a valid ISO-8601 timestamp: {}".format(
                field_name, value, exc
            )
        ) from exc
    return _ensure_aware_utc(parsed)


def _to_decimal(value: Any) -> Decimal:
    try:
        parsed = Decimal(str(value))
    except (
        Exception
    ) as exc:  # noqa: BLE001 - re-raised as a typed activation error below
        raise PricingManifestSchemaError(
            "value {!r} is not a valid decimal amount".format(value)
        ) from exc
    if not parsed.is_finite():
        raise PricingManifestSchemaError(
            "value {!r} must be a finite decimal amount".format(value)
        )
    return parsed


def _parse_authorization_timestamp(value: str, *, field_name: str) -> datetime:
    try:
        return _parse_iso8601(value, field_name=field_name)
    except PricingManifestSchemaError as exc:
        raise AuthorizationArtifactInvalidError(str(exc)) from exc


def _constant_time_eq(a: str, b: str) -> bool:
    """Constant-time string comparison (defense in depth; digests are not secret, but cheap to do right)."""
    if len(a) != len(b):
        return False
    result = 0
    for x, y in zip(a, b):
        result |= ord(x) ^ ord(y)
    return result == 0
