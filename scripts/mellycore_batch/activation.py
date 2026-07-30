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
import ntpath
import os
import re
import stat
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from decimal import (
    ROUND_HALF_EVEN,
    Clamped,
    Context,
    Decimal,
    DecimalException,
    DivisionByZero,
    Inexact,
    InvalidOperation,
    Overflow,
    Rounded,
    Subnormal,
    Underflow,
    localcontext,
)
from pathlib import Path, PureWindowsPath
from typing import Any, Dict, List, Optional, Sequence, Tuple

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
STAGE_B_SYNCHRONOUS_PRICE_INPUT = "0.20"
STAGE_B_SYNCHRONOUS_PRICE_CACHED_INPUT = "0.02"
STAGE_B_SYNCHRONOUS_PRICE_OUTPUT = "1.25"
STAGE_B_BATCH_PRICE_INPUT = "0.10"
STAGE_B_BATCH_PRICE_CACHED_INPUT = "0.01"
STAGE_B_BATCH_PRICE_OUTPUT = "0.625"
STAGE_B_BATCH_DISCOUNT_PERCENT = "50"
STAGE_B_HARD_COST_CAP_USD_TEXT = "0.01"
STAGE_B_PRICING_VERIFIED_AT = "2026-07-28T22:00:34Z"
STAGE_B_PRICING_VALID_UNTIL = "2026-08-27T22:00:34Z"
STAGE_B_SOURCE_URLS = (
    "https://developers.openai.com/api/docs/models/gpt-5.4-nano",
    "https://developers.openai.com/api/docs/pricing",
    "https://developers.openai.com/api/docs/guides/batch",
    "https://help.openai.com/en/articles/9197833-batch-api-faq",
)
STAGE_B_MAX_AUTHORIZATION_LIFETIME = timedelta(minutes=15)

_SECURITY_DECIMAL_CONTEXT = Context(
    prec=50,
    rounding=ROUND_HALF_EVEN,
)
for _decimal_signal in (
    InvalidOperation,
    DivisionByZero,
    Overflow,
    Underflow,
    Subnormal,
    Clamped,
    Inexact,
    Rounded,
):
    _SECURITY_DECIMAL_CONTEXT.traps[_decimal_signal] = True

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
_AUTHORIZATION_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_-]{0,63}$", re.ASCII)
_TASK_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,199}$")
_COMMIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_CANONICAL_DECIMAL_RE = re.compile(r"^(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$", re.ASCII)
_CANONICAL_UTC_TIMESTAMP_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", re.ASCII
)
_WINDOWS_RESERVED_NAMES = frozenset(
    {"con", "prn", "aux", "nul"}
    | {"com{}".format(index) for index in range(1, 10)}
    | {"lpt{}".format(index) for index in range(1, 10)}
)

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


class _DuplicateJSONKeyError(ValueError):
    """Internal sentinel used to reject duplicate JSON keys without echoing input."""


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


class AuthorizationLedgerSafetyError(AuthorizationArtifactError):
    """The local consumption ledger cannot meet the required filesystem boundary."""


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


def _reject_duplicate_object_pairs(
    pairs: Sequence[Tuple[str, Any]]
) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJSONKeyError("duplicate JSON object key detected")
        result[key] = value
    return result


def _reject_nonfinite_json_constant(_value: str) -> None:
    raise ValueError("non-finite JSON number is not permitted")


def _strict_json_loads(text: str, *, document_label: str) -> Any:
    """Parse security-sensitive JSON without duplicate or non-finite values."""
    try:
        return json.loads(
            text,
            object_pairs_hook=_reject_duplicate_object_pairs,
            parse_constant=_reject_nonfinite_json_constant,
        )
    except _DuplicateJSONKeyError as exc:
        raise ValueError(
            "{} contains a duplicate JSON object key".format(document_label)
        ) from exc
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError("{} is not strict JSON".format(document_label)) from exc


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
        data = _strict_json_loads(text, document_label="pricing manifest")
    except ValueError as exc:
        raise PricingManifestSchemaError(
            "pricing manifest {} is invalid: {}".format(manifest_path, exc)
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
            if (
                _parse_canonical_decimal(
                    block[sub_key],
                    field_name="{}.{}".format(pricing_block_name, sub_key),
                )
                <= 0
            ):
                raise PricingManifestSchemaError(
                    "pricing manifest {!r}.{} must be greater than zero".format(
                        pricing_block_name, sub_key
                    )
                )
    if (
        _parse_canonical_decimal(
            manifest["batch_discount_percent"],
            field_name="batch_discount_percent",
        )
        <= 0
    ):
        raise PricingManifestSchemaError(
            "pricing manifest 'batch_discount_percent' must be greater than zero"
        )
    if (
        _parse_canonical_decimal(
            manifest["hard_cost_cap_usd"], field_name="hard_cost_cap_usd"
        )
        <= 0
    ):
        raise PricingManifestSchemaError(
            "pricing manifest 'hard_cost_cap_usd' must be greater than zero"
        )
    source_urls = manifest["source_urls"]
    if any(not isinstance(url, str) or not url for url in source_urls):
        raise PricingManifestSchemaError(
            "pricing manifest 'source_urls' must contain non-empty strings only"
        )
    if len(source_urls) != len(set(source_urls)):
        raise PricingManifestSchemaError(
            "pricing manifest 'source_urls' must not contain duplicates"
        )
    if not re.fullmatch(r"[0-9a-f]{64}", manifest["evidence_digest"], re.ASCII):
        raise PricingManifestSchemaError(
            "pricing manifest 'evidence_digest' must be 64 lowercase hexadecimal characters"
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
    if now >= valid_until:
        raise PricingEvidenceExpiredError(
            "pricing evidence expired: 'valid_until' ({}) is not after now ({})".format(
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

    _check("schema_version", 1)
    _check("provider", STAGE_B_PROVIDER)
    _check("endpoint", STAGE_B_ENDPOINT)
    _check("model", STAGE_B_MODEL)
    _check("processing_region", STAGE_B_PROCESSING_REGION)
    _check("currency", "USD")
    _check("pricing_unit_tokens", STAGE_B_PRICING_UNIT_TOKENS_INT)
    _check("batch_discount_percent", STAGE_B_BATCH_DISCOUNT_PERCENT)
    _check("cached_input_assumed", False)
    _check("verified_at", STAGE_B_PRICING_VERIFIED_AT)
    _check("valid_until", STAGE_B_PRICING_VALID_UNTIL)
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
    _check("hard_cost_cap_usd", STAGE_B_HARD_COST_CAP_USD_TEXT)
    if manifest.get("source_urls") != list(STAGE_B_SOURCE_URLS):
        mismatches.append(
            "source_urls: manifest={!r} constant={!r}".format(
                manifest.get("source_urls"), list(STAGE_B_SOURCE_URLS)
            )
        )

    synchronous_prices = manifest.get("synchronous") or {}
    batch_prices = manifest.get("batch") or {}
    price_checks = (
        (
            "synchronous.input",
            synchronous_prices.get("input"),
            STAGE_B_SYNCHRONOUS_PRICE_INPUT,
        ),
        (
            "synchronous.cached_input",
            synchronous_prices.get("cached_input"),
            STAGE_B_SYNCHRONOUS_PRICE_CACHED_INPUT,
        ),
        (
            "synchronous.output",
            synchronous_prices.get("output"),
            STAGE_B_SYNCHRONOUS_PRICE_OUTPUT,
        ),
        ("batch.input", batch_prices.get("input"), STAGE_B_BATCH_PRICE_INPUT),
        (
            "batch.cached_input",
            batch_prices.get("cached_input"),
            STAGE_B_BATCH_PRICE_CACHED_INPUT,
        ),
        (
            "batch.output",
            batch_prices.get("output"),
            STAGE_B_BATCH_PRICE_OUTPUT,
        ),
    )
    for label, raw_value, expected_text in price_checks:
        if raw_value != expected_text:
            mismatches.append(
                "{}: manifest={!r} constant={!r}".format(
                    label, raw_value, expected_text
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
    try:
        with localcontext(_SECURITY_DECIMAL_CONTEXT):
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
    except DecimalException as exc:
        raise ActivationError(
            "cost calculation was inexact, rounded, or outside the approved Decimal range"
        ) from exc
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
    monetary_values = (
        estimate.input_cost,
        estimate.output_cost,
        estimate.estimated_maximum_cost,
        estimate.hard_cost_cap_usd,
    )
    if any(
        not isinstance(value, Decimal) or not value.is_finite() or value < 0
        for value in monetary_values
    ):
        raise CostCapExceededError(
            "cost estimate contains an invalid, non-finite, or negative monetary value"
        )
    if estimate.hard_cost_cap_usd != STAGE_B_HARD_COST_CAP_USD:
        raise CostCapExceededError(
            "cost estimate hard cap does not match the Stage B authority"
        )
    if estimate.estimated_maximum_cost > STAGE_B_HARD_COST_CAP_USD:
        raise CostCapExceededError(
            "estimated maximum cost {} exceeds the authorized hard cost cap {}".format(
                estimate.estimated_maximum_cost, STAGE_B_HARD_COST_CAP_USD
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
    if not _is_safe_authorization_id(data["authorization_id"]):
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
        data = _strict_json_loads(text, document_label="authorization artifact")
    except ValueError as exc:
        raise AuthorizationArtifactSchemaError(
            "authorization artifact {} is invalid: {}".format(path, exc)
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

    try:
        now = _ensure_aware_utc(now)
    except PricingManifestSchemaError as exc:
        raise AuthorizationArtifactInvalidError(str(exc)) from exc
    issued_at = _parse_authorization_timestamp(
        artifact.issued_at, field_name="issued_at"
    )
    expires_at = _parse_authorization_timestamp(
        artifact.expires_at, field_name="expires_at"
    )
    if now >= expires_at:
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
    if expires_at - issued_at > STAGE_B_MAX_AUTHORIZATION_LIFETIME:
        raise AuthorizationArtifactInvalidError(
            "authorization artifact {!r} lifetime exceeds the 15-minute maximum".format(
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
        artifact_maximum_cost = _parse_canonical_decimal(
            artifact.maximum_cost, field_name="maximum_cost"
        )
    except PricingManifestSchemaError as exc:
        raise AuthorizationArtifactInvalidError(str(exc)) from exc
    if (
        artifact_maximum_cost != expected_max_cost
        or artifact.maximum_cost != str(expected_max_cost)
    ):
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
    if is_authorization_consumed(artifact.authorization_id):
        raise AuthorizationAlreadyConsumedError(
            "authorization {!r} has already been consumed".format(
                artifact.authorization_id
            )
        )


def default_authorization_ledger_dir() -> Path:
    """Return the fixed production ledger root selected by Windows itself."""
    return _authorization_ledger_root()


def is_authorization_consumed(authorization_id: str) -> bool:
    """Read-only, no-follow check: has ``authorization_id`` been consumed?"""
    return _is_authorization_consumed_at_validated_root(
        authorization_id, _authorization_ledger_root()
    )


def _is_authorization_consumed_at_validated_root(
    authorization_id: str, ledger_dir: Path
) -> bool:
    """Check a marker below a root already authorized by the production resolver.

    This root-taking helper is private so isolated filesystem tests can retain
    coverage of the no-follow implementation. Production callers must use
    :func:`is_authorization_consumed`, which supplies the fixed Known Folder
    root and exposes no path parameter.
    """
    ledger_path = _normalized_ledger_path(Path(ledger_dir))
    safe_id = _safe_ledger_filename(authorization_id)
    marker_name = "{}.consumed".format(safe_id)
    if os.name == "nt":
        return _windows_marker_exists(ledger_path, marker_name)
    return _posix_marker_exists(ledger_path, marker_name)


def consume_authorization(authorization_id: str) -> Path:
    """Atomically, irreversibly mark ``authorization_id`` as consumed.

    The storage root is not caller-selectable. It is derived internally from
    the Windows Local AppData Known Folder and is rejected if it overlaps the
    source repository or a Git administrative path.

    Uses a validated directory handle plus exclusive, relative creation.
    Windows production paths open each directory component and marker with
    no-reparse semantics. The private test helper retains its POSIX
    ``dir_fd``/``O_NOFOLLOW`` implementation, but the production root resolver
    is Windows-only and fails closed elsewhere. Two concurrent callers can
    never both succeed.

    This function is never called from any Stage B CLI command -- Stage B
    preflight only *validates* an authorization artifact, it never consumes
    one. It is exposed here so its atomicity and reuse-rejection behavior are
    directly unit-testable without Stage C existing yet: only a hypothetical
    future, separately authorized Stage C execution attempt would call it,
    and that code path does not exist in this package.
    """
    return _consume_authorization_at_validated_root(
        authorization_id, _authorization_ledger_root()
    )


def _consume_authorization_at_validated_root(
    authorization_id: str, ledger_dir: Path
) -> Path:
    """Consume below a root already authorized by the production resolver.

    This private helper exists only to isolate filesystem-boundary tests.
    Production call sites must first obtain the non-configurable root from
    :func:`_authorization_ledger_root` and must never accept a caller path.
    """
    safe_id = _safe_ledger_filename(authorization_id)
    ledger_path = _normalized_ledger_path(Path(ledger_dir))
    marker_name = "{}.consumed".format(safe_id)
    marker_payload = json.dumps(
        {
            "authorization_id": authorization_id,
            "consumed_at": datetime.now(timezone.utc).isoformat(),
        },
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    if os.name == "nt":
        return _windows_create_marker(
            ledger_path, marker_name, marker_payload, authorization_id
        )
    return _posix_create_marker(
        ledger_path, marker_name, marker_payload, authorization_id
    )


def _windows_known_folder_api() -> Tuple[Any, Any, Any, Any, Any]:
    import ctypes
    from ctypes import wintypes

    class Guid(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", ctypes.c_ubyte * 8),
        ]

    shell32 = ctypes.WinDLL("shell32", use_last_error=True)
    ole32 = ctypes.WinDLL("ole32", use_last_error=True)
    shell32.SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(Guid),
        wintypes.DWORD,
        wintypes.HANDLE,
        ctypes.POINTER(wintypes.LPWSTR),
    ]
    shell32.SHGetKnownFolderPath.restype = ctypes.c_long
    ole32.CoTaskMemFree.argtypes = [wintypes.LPVOID]
    ole32.CoTaskMemFree.restype = None
    return ctypes, wintypes, shell32, ole32, Guid


def _windows_local_app_data_known_folder() -> Path:
    """Return FOLDERID_LocalAppData, releasing the shell-allocated buffer."""
    if os.name != "nt":
        raise AuthorizationLedgerSafetyError(
            "the production authorization ledger requires Windows Known Folders"
        )
    ctypes, wintypes, shell32, ole32, Guid = _windows_known_folder_api()
    folder_id = Guid(
        0xF1B32785,
        0x6FBA,
        0x4FCF,
        (ctypes.c_ubyte * 8)(
            0x9D,
            0x55,
            0x7B,
            0x8E,
            0x7F,
            0x15,
            0x70,
            0x91,
        ),
    )
    allocated_path = wintypes.LPWSTR()
    result = shell32.SHGetKnownFolderPath(
        ctypes.byref(folder_id), 0, None, ctypes.byref(allocated_path)
    )
    try:
        if result != 0:
            raise AuthorizationLedgerSafetyError(
                "Windows could not resolve the Local AppData Known Folder"
            )
        value = allocated_path.value if allocated_path else None
        if not value or "\x00" in value:
            raise AuthorizationLedgerSafetyError(
                "Windows returned an invalid Local AppData Known Folder"
            )
        return Path(value)
    finally:
        if allocated_path:
            ole32.CoTaskMemFree(ctypes.cast(allocated_path, ctypes.c_void_p))


def _authorization_ledger_root() -> Path:
    """Derive the sole production ledger root without environment overrides."""
    local_app_data = _windows_local_app_data_known_folder()
    raw = os.fspath(local_app_data)
    if not raw or "\x00" in raw or not ntpath.isabs(raw):
        raise AuthorizationLedgerSafetyError(
            "Windows returned a non-absolute Local AppData Known Folder"
        )
    drive, _tail = ntpath.splitdrive(raw)
    if not drive or drive.startswith("\\\\"):
        raise AuthorizationLedgerSafetyError(
            "the Local AppData Known Folder must be on a local Windows drive"
        )
    ledger_path = Path(ntpath.normpath(raw)) / "MellyCore" / "batch" / "authorizations"
    return _validate_authorized_ledger_root(ledger_path)


def _repository_root_from_source() -> Path:
    source_path = Path(__file__)
    if not source_path.is_absolute():
        raise AuthorizationLedgerSafetyError(
            "the installed activation source path is not absolute"
        )
    return Path(ntpath.normpath(os.fspath(source_path.parent.parent.parent)))


def _canonical_windows_parts(path: Path) -> Tuple[str, ...]:
    raw = os.fspath(path)
    if not raw or "\x00" in raw or not ntpath.isabs(raw):
        raise AuthorizationLedgerSafetyError(
            "ledger boundary comparison requires an absolute Windows path"
        )
    normalized = ntpath.normcase(ntpath.normpath(raw))
    return tuple(part.casefold() for part in PureWindowsPath(normalized).parts)


def _windows_path_is_same_or_descendant(candidate: Path, parent: Path) -> bool:
    candidate_parts = _canonical_windows_parts(candidate)
    parent_parts = _canonical_windows_parts(parent)
    return (
        len(candidate_parts) >= len(parent_parts)
        and candidate_parts[: len(parent_parts)] == parent_parts
    )


def _validate_authorized_ledger_root(ledger_path: Path) -> Path:
    """Reject repository, ancestor, and Git-administrative ledger locations."""
    normalized = _normalized_ledger_path(ledger_path)
    repository_root = _repository_root_from_source()
    if _windows_path_is_same_or_descendant(
        normalized, repository_root
    ) or _windows_path_is_same_or_descendant(repository_root, normalized):
        raise AuthorizationLedgerSafetyError(
            "the production authorization ledger must be outside the repository"
        )
    if any(
        part.casefold() == ".git"
        for part in PureWindowsPath(
            ntpath.normcase(ntpath.normpath(os.fspath(normalized)))
        ).parts
    ):
        raise AuthorizationLedgerSafetyError(
            "the production authorization ledger cannot use a Git administrative path"
        )
    return normalized


def _normalized_ledger_path(ledger_dir: Path) -> Path:
    raw = os.fspath(ledger_dir)
    if not raw or "\x00" in raw:
        raise AuthorizationLedgerSafetyError("ledger directory path is invalid")
    if not Path(raw).is_absolute():
        raise AuthorizationLedgerSafetyError(
            "ledger directory must be an absolute non-root path"
        )
    absolute = Path(os.path.normpath(raw))
    if not absolute.is_absolute() or absolute == Path(absolute.anchor):
        raise AuthorizationLedgerSafetyError(
            "ledger directory must be an absolute non-root path"
        )
    if os.name == "nt":
        drive, _tail = os.path.splitdrive(str(absolute))
        if not drive or drive.startswith("\\\\"):
            raise AuthorizationLedgerSafetyError(
                "ledger directory must be on a local Windows drive"
            )
    return absolute


def _posix_open_ledger_directory(ledger_path: Path, *, create: bool) -> Optional[int]:
    flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    current_fd = os.open(ledger_path.anchor, flags)
    try:
        for component in ledger_path.parts[1:]:
            try:
                next_fd = os.open(component, flags, dir_fd=current_fd)
            except FileNotFoundError:
                if not create:
                    return None
                try:
                    os.mkdir(component, mode=0o700, dir_fd=current_fd)
                except FileExistsError:
                    pass
                next_fd = os.open(component, flags, dir_fd=current_fd)
            details = os.fstat(next_fd)
            if not stat.S_ISDIR(details.st_mode):
                os.close(next_fd)
                raise AuthorizationLedgerSafetyError(
                    "ledger path contains a non-directory component"
                )
            os.close(current_fd)
            current_fd = next_fd
        return current_fd
    except Exception:
        os.close(current_fd)
        raise


def _posix_marker_exists(ledger_path: Path, marker_name: str) -> bool:
    directory_fd = _posix_open_ledger_directory(ledger_path, create=False)
    if directory_fd is None:
        return False
    try:
        try:
            details = os.stat(marker_name, dir_fd=directory_fd, follow_symlinks=False)
        except FileNotFoundError:
            return False
        if stat.S_ISLNK(details.st_mode) or not stat.S_ISREG(details.st_mode):
            raise AuthorizationLedgerSafetyError(
                "authorization marker is a symlink or non-regular filesystem object"
            )
        return True
    finally:
        os.close(directory_fd)


def _posix_create_marker(
    ledger_path: Path,
    marker_name: str,
    payload: bytes,
    authorization_id: str,
) -> Path:
    directory_fd = _posix_open_ledger_directory(ledger_path, create=True)
    if directory_fd is None:  # pragma: no cover - create=True guarantees a handle
        raise AuthorizationLedgerSafetyError("could not create the ledger directory")
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY | getattr(os, "O_NOFOLLOW", 0)
    try:
        try:
            marker_fd = os.open(marker_name, flags, 0o600, dir_fd=directory_fd)
        except FileExistsError as exc:
            if _posix_marker_exists(ledger_path, marker_name):
                raise AuthorizationAlreadyConsumedError(
                    "authorization {!r} has already been consumed".format(
                        authorization_id
                    )
                ) from exc
            raise
        try:
            os.write(marker_fd, payload)
            os.fsync(marker_fd)
        finally:
            os.close(marker_fd)
    finally:
        os.close(directory_fd)
    return ledger_path / marker_name


def _windows_api() -> Tuple[Any, Any, Any, Any, Any]:
    import ctypes
    from ctypes import wintypes

    class UnicodeString(ctypes.Structure):
        _fields_ = [
            ("Length", wintypes.USHORT),
            ("MaximumLength", wintypes.USHORT),
            ("Buffer", wintypes.LPWSTR),
        ]

    class ObjectAttributes(ctypes.Structure):
        _fields_ = [
            ("Length", wintypes.ULONG),
            ("RootDirectory", wintypes.HANDLE),
            ("ObjectName", ctypes.POINTER(UnicodeString)),
            ("Attributes", wintypes.ULONG),
            ("SecurityDescriptor", wintypes.LPVOID),
            ("SecurityQualityOfService", wintypes.LPVOID),
        ]

    class IoStatusBlock(ctypes.Structure):
        _fields_ = [("Status", ctypes.c_void_p), ("Information", ctypes.c_size_t)]

    class FileAttributeTagInfo(ctypes.Structure):
        _fields_ = [
            ("FileAttributes", wintypes.DWORD),
            ("ReparseTag", wintypes.DWORD),
        ]

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    ntdll = ctypes.WinDLL("ntdll")
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL
    kernel32.GetFileInformationByHandleEx.argtypes = [
        wintypes.HANDLE,
        ctypes.c_int,
        wintypes.LPVOID,
        wintypes.DWORD,
    ]
    kernel32.GetFileInformationByHandleEx.restype = wintypes.BOOL
    kernel32.GetFinalPathNameByHandleW.argtypes = [
        wintypes.HANDLE,
        wintypes.LPWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
    ]
    kernel32.GetFinalPathNameByHandleW.restype = wintypes.DWORD
    kernel32.WriteFile.argtypes = [
        wintypes.HANDLE,
        wintypes.LPCVOID,
        wintypes.DWORD,
        ctypes.POINTER(wintypes.DWORD),
        wintypes.LPVOID,
    ]
    kernel32.WriteFile.restype = wintypes.BOOL
    kernel32.FlushFileBuffers.argtypes = [wintypes.HANDLE]
    kernel32.FlushFileBuffers.restype = wintypes.BOOL
    ntdll.NtCreateFile.argtypes = [
        ctypes.POINTER(wintypes.HANDLE),
        wintypes.ULONG,
        ctypes.POINTER(ObjectAttributes),
        ctypes.POINTER(IoStatusBlock),
        ctypes.c_void_p,
        wintypes.ULONG,
        wintypes.ULONG,
        wintypes.ULONG,
        wintypes.ULONG,
        ctypes.c_void_p,
        wintypes.ULONG,
    ]
    ntdll.NtCreateFile.restype = ctypes.c_long
    return (
        ctypes,
        wintypes,
        kernel32,
        ntdll,
        (UnicodeString, ObjectAttributes, IoStatusBlock, FileAttributeTagInfo),
    )


def _windows_close_handle(handle: Any) -> None:
    _ctypes, _wintypes, kernel32, _ntdll, _types = _windows_api()
    if handle:
        kernel32.CloseHandle(handle)


def _windows_nt_open_relative(
    parent_handle: Any,
    name: str,
    *,
    directory: bool,
    create_if_missing: bool,
    exclusive_create: bool = False,
) -> Optional[Any]:
    ctypes, wintypes, _kernel32, ntdll, types = _windows_api()
    UnicodeString, ObjectAttributes, IoStatusBlock, _tag_type = types
    encoded_length = len(name.encode("utf-16-le"))
    name_buffer = ctypes.create_unicode_buffer(name)
    unicode_name = UnicodeString(
        encoded_length,
        encoded_length,
        ctypes.cast(name_buffer, wintypes.LPWSTR),
    )
    attributes = ObjectAttributes(
        ctypes.sizeof(ObjectAttributes),
        parent_handle,
        ctypes.pointer(unicode_name),
        0x00000040 | 0x00001000,  # OBJ_CASE_INSENSITIVE | OBJ_DONT_REPARSE
        None,
        None,
    )
    io_status = IoStatusBlock()
    child_handle = wintypes.HANDLE()
    desired_access = 0x00100000 | 0x00000080  # SYNCHRONIZE | FILE_READ_ATTRIBUTES
    if directory:
        desired_access |= 0x00000020  # FILE_TRAVERSE
    elif exclusive_create:
        desired_access |= 0x00000002  # FILE_WRITE_DATA
    if exclusive_create:
        disposition = 2  # FILE_CREATE
        share_access = 0
    elif create_if_missing:
        disposition = 3  # FILE_OPEN_IF
        share_access = 0x00000001 | 0x00000002 | 0x00000004
    else:
        disposition = 1  # FILE_OPEN
        share_access = 0x00000001 | 0x00000002 | 0x00000004
    create_options = (
        (0x00000001 if directory else 0x00000040)
        | 0x00000020
        | 0x00200000
    )
    file_attributes = 0x00000010 if directory else 0x00000080
    status = ntdll.NtCreateFile(
        ctypes.byref(child_handle),
        desired_access,
        ctypes.byref(attributes),
        ctypes.byref(io_status),
        None,
        file_attributes,
        share_access,
        disposition,
        create_options,
        None,
        0,
    )
    status_code = ctypes.c_ulong(status).value
    if status_code == 0:
        return child_handle
    if status_code in {0xC0000034, 0xC000003A}:
        return None
    if status_code == 0xC0000035:
        raise FileExistsError(name)
    raise AuthorizationLedgerSafetyError(
        "Windows rejected a ledger filesystem object (NTSTATUS 0x{:08x})".format(
            status_code
        )
    )


def _windows_handle_is_reparse(handle: Any) -> bool:
    ctypes, _wintypes, kernel32, _ntdll, types = _windows_api()
    _unicode, _attributes, _io_status, FileAttributeTagInfo = types
    info = FileAttributeTagInfo()
    if not kernel32.GetFileInformationByHandleEx(
        handle, 9, ctypes.byref(info), ctypes.sizeof(info)
    ):
        raise AuthorizationLedgerSafetyError(
            "Windows could not inspect ledger reparse-point attributes"
        )
    return bool(info.FileAttributes & 0x00000400)


def _windows_final_path(handle: Any) -> Path:
    ctypes, wintypes, kernel32, _ntdll, _types = _windows_api()
    required = kernel32.GetFinalPathNameByHandleW(handle, None, 0, 0)
    if not required:
        raise AuthorizationLedgerSafetyError(
            "Windows could not resolve the opened ledger directory handle"
        )
    buffer = ctypes.create_unicode_buffer(required + 1)
    if not kernel32.GetFinalPathNameByHandleW(handle, buffer, len(buffer), 0):
        raise AuthorizationLedgerSafetyError(
            "Windows could not resolve the opened ledger directory handle"
        )
    value = buffer.value
    if value.startswith("\\\\?\\UNC\\"):
        value = "\\\\" + value[8:]
    elif value.startswith("\\\\?\\"):
        value = value[4:]
    return Path(value)


def _windows_open_ledger_directory(
    ledger_path: Path, *, create: bool
) -> Optional[Tuple[Any, Path]]:
    ctypes, wintypes, kernel32, _ntdll, _types = _windows_api()
    kernel32.CreateFileW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.LPVOID,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.HANDLE,
    ]
    kernel32.CreateFileW.restype = wintypes.HANDLE
    kernel32.GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
    kernel32.GetFileAttributesW.restype = wintypes.DWORD
    missing_components: List[str] = []
    existing_path = ledger_path
    while True:
        attributes = kernel32.GetFileAttributesW(str(existing_path))
        if attributes != 0xFFFFFFFF:
            if attributes & 0x00000400:
                raise AuthorizationLedgerSafetyError(
                    "ledger path contains a Windows reparse point"
                )
            if not attributes & 0x00000010:
                raise AuthorizationLedgerSafetyError(
                    "ledger path contains a non-directory component"
                )
            break
        error = ctypes.get_last_error()
        if error not in {2, 3}:
            raise AuthorizationLedgerSafetyError(
                "Windows could not inspect the ledger directory path"
            )
        if existing_path == Path(existing_path.anchor):
            raise AuthorizationLedgerSafetyError(
                "Windows could not find a trusted existing ledger ancestor"
            )
        missing_components.append(existing_path.name)
        existing_path = existing_path.parent

    current_handle = kernel32.CreateFileW(
        str(existing_path),
        0x00000020 | 0x00000080 | 0x00100000,
        0x00000001 | 0x00000002 | 0x00000004,
        None,
        3,
        0x02000000 | 0x00200000,
        None,
    )
    if current_handle == ctypes.c_void_p(-1).value:
        raise AuthorizationLedgerSafetyError(
            "Windows could not open the trusted existing ledger ancestor"
        )
    try:
        if _windows_handle_is_reparse(current_handle):
            raise AuthorizationLedgerSafetyError(
                "ledger path contains a Windows reparse point"
            )
        opened_existing_path = _windows_final_path(current_handle)
        if os.path.normcase(
            os.path.normpath(str(opened_existing_path))
        ) != os.path.normcase(os.path.normpath(str(existing_path))):
            raise AuthorizationLedgerSafetyError(
                "opened ledger ancestor does not match the intended local path"
            )
        for component in reversed(missing_components):
            next_handle = _windows_nt_open_relative(
                current_handle,
                component,
                directory=True,
                create_if_missing=create,
            )
            if next_handle is None:
                return None
            if _windows_handle_is_reparse(next_handle):
                _windows_close_handle(next_handle)
                raise AuthorizationLedgerSafetyError(
                    "ledger path contains a Windows reparse point"
                )
            _windows_close_handle(current_handle)
            current_handle = next_handle
        final_path = _windows_final_path(current_handle)
        if os.path.normcase(os.path.normpath(str(final_path))) != os.path.normcase(
            os.path.normpath(str(ledger_path))
        ):
            raise AuthorizationLedgerSafetyError(
                "opened ledger directory does not match the intended local path"
            )
        return current_handle, final_path
    except Exception:
        _windows_close_handle(current_handle)
        raise


def _windows_marker_exists(ledger_path: Path, marker_name: str) -> bool:
    opened = _windows_open_ledger_directory(ledger_path, create=False)
    if opened is None:
        return False
    directory_handle, _final_path = opened
    try:
        marker_handle = _windows_nt_open_relative(
            directory_handle,
            marker_name,
            directory=False,
            create_if_missing=False,
        )
        if marker_handle is None:
            return False
        try:
            if _windows_handle_is_reparse(marker_handle):
                raise AuthorizationLedgerSafetyError(
                    "authorization marker is a Windows reparse point"
                )
            return True
        finally:
            _windows_close_handle(marker_handle)
    finally:
        _windows_close_handle(directory_handle)


def _windows_create_marker(
    ledger_path: Path,
    marker_name: str,
    payload: bytes,
    authorization_id: str,
) -> Path:
    if _windows_marker_exists(ledger_path, marker_name):
        raise AuthorizationAlreadyConsumedError(
            "authorization {!r} has already been consumed".format(authorization_id)
        )
    opened = _windows_open_ledger_directory(ledger_path, create=True)
    if opened is None:  # pragma: no cover - create=True guarantees a handle
        raise AuthorizationLedgerSafetyError("could not create the ledger directory")
    directory_handle, final_path = opened
    try:
        try:
            marker_handle = _windows_nt_open_relative(
                directory_handle,
                marker_name,
                directory=False,
                create_if_missing=False,
                exclusive_create=True,
            )
        except FileExistsError as exc:
            raise AuthorizationAlreadyConsumedError(
                "authorization {!r} has already been consumed".format(
                    authorization_id
                )
            ) from exc
        if marker_handle is None:  # pragma: no cover - FILE_CREATE never returns None
            raise AuthorizationLedgerSafetyError(
                "Windows did not create the authorization marker"
            )
        try:
            if _windows_handle_is_reparse(marker_handle):
                raise AuthorizationLedgerSafetyError(
                    "authorization marker is a Windows reparse point"
                )
            ctypes, wintypes, kernel32, _ntdll, _types = _windows_api()
            written = wintypes.DWORD()
            buffer = ctypes.create_string_buffer(payload)
            if not kernel32.WriteFile(
                marker_handle,
                buffer,
                len(payload),
                ctypes.byref(written),
                None,
            ) or written.value != len(payload):
                raise AuthorizationLedgerSafetyError(
                    "Windows could not completely write the authorization marker"
                )
            if not kernel32.FlushFileBuffers(marker_handle):
                raise AuthorizationLedgerSafetyError(
                    "Windows could not durably flush the authorization marker"
                )
        finally:
            _windows_close_handle(marker_handle)
    finally:
        _windows_close_handle(directory_handle)
    return final_path / marker_name


def _safe_ledger_filename(authorization_id: str) -> str:
    if not _is_safe_authorization_id(authorization_id):
        raise AuthorizationArtifactInvalidError(
            "authorization_id {!r} is not a canonical safe ledger filename".format(
                authorization_id
            )
        )
    return authorization_id


def _is_safe_authorization_id(value: Any) -> bool:
    return (
        isinstance(value, str)
        and _AUTHORIZATION_ID_RE.fullmatch(value) is not None
        and value.casefold() not in _WINDOWS_RESERVED_NAMES
    )


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


def parse_canonical_utc_timestamp(value: str, *, field_name: str) -> datetime:
    """Parse exactly ``YYYY-MM-DDTHH:MM:SSZ`` without timezone coercion."""
    return _parse_iso8601(value, field_name=field_name)


def _ensure_aware_utc(value: datetime) -> datetime:
    if not isinstance(value, datetime) or value.tzinfo is None:
        raise PricingManifestSchemaError(
            "comparison time must be an explicit timezone-aware UTC datetime"
        )
    if value.utcoffset() != timedelta(0):
        raise PricingManifestSchemaError(
            "comparison time must use UTC, not a non-zero timezone offset"
        )
    return value.astimezone(timezone.utc)


def _parse_iso8601(value: str, *, field_name: str) -> datetime:
    if (
        not isinstance(value, str)
        or not _CANONICAL_UTC_TIMESTAMP_RE.fullmatch(value)
    ):
        raise PricingManifestSchemaError(
            "field {!r} must use canonical UTC format YYYY-MM-DDTHH:MM:SSZ".format(
                field_name
            )
        )
    try:
        parsed = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise PricingManifestSchemaError(
            "field {!r} is not a valid canonical UTC timestamp".format(
                field_name
            )
        ) from exc
    return parsed.replace(tzinfo=timezone.utc)


def _parse_canonical_decimal(value: Any, *, field_name: str) -> Decimal:
    if not isinstance(value, str) or not _CANONICAL_DECIMAL_RE.fullmatch(value):
        raise PricingManifestSchemaError(
            "field {!r} must be a canonical non-negative decimal string without exponent notation".format(
                field_name
            )
        )
    try:
        with localcontext(_SECURITY_DECIMAL_CONTEXT):
            parsed = Decimal(value)
    except DecimalException as exc:
        raise PricingManifestSchemaError(
            "field {!r} is not an exact decimal amount".format(field_name)
        ) from exc
    if not parsed.is_finite():
        raise PricingManifestSchemaError(
            "field {!r} must be a finite decimal amount".format(field_name)
        )
    return parsed


def _to_decimal(value: Any) -> Decimal:
    """Backward-compatible internal wrapper for canonical decimal parsing."""
    return _parse_canonical_decimal(value, field_name="decimal value")


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
