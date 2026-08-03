"""Immutable Cloudflare read-only adapter contracts.

These types describe provider semantics and synthetic fixture normalization.
They contain no transport, credential resolution, or runtime-enablement path.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional, Tuple

from ..contracts import (
    AdapterErrorCode,
    CapabilityDescriptor,
    CapabilityId,
    ProviderDescriptor,
)


class CloudflareSemanticsState(str, Enum):
    """Truthful provider-specific implementation state."""

    CONCRETE_READ_ONLY = "concrete_read_only"


class CloudflareIdentityVariant(str, Enum):
    """Identity-specific concrete registration variants."""

    DELEGATED = "delegated"
    SERVICE = "service"


class CloudflareAdapterInclusion(str, Enum):
    """Closed classification used for all 58 accepted capabilities."""

    IN_SCOPE_READ_ONLY = "IN_SCOPE_READ_ONLY"
    OUT_OF_SCOPE_PROPOSAL = "OUT_OF_SCOPE_PROPOSAL"
    OUT_OF_SCOPE_MUTATION = "OUT_OF_SCOPE_MUTATION"
    OUT_OF_SCOPE_CONTAINMENT = "OUT_OF_SCOPE_CONTAINMENT"
    OUT_OF_SCOPE_RESTRICTED_TOOL = "OUT_OF_SCOPE_RESTRICTED_TOOL"
    OUT_OF_SCOPE_UNREPRESENTABLE = "OUT_OF_SCOPE_UNREPRESENTABLE"


class CloudflareEntityFamily(str, Enum):
    """Normalized entity families discovered from the Cloudflare contract."""

    ACCOUNT = "account"
    ZONE = "zone"
    API_OPERATION = "api_operation"
    ENDPOINT_LABEL = "endpoint_label"
    SCHEMA = "schema"
    SCHEMA_SETTINGS = "schema_settings"
    OPERATION_SETTINGS = "operation_settings"
    AUTHENTICATION_FINDING = "authentication_finding"
    RULESET = "ruleset"
    SECURITY_EVENT = "security_event"
    AUDIT_EVENT = "audit_event"


class CloudflareFixtureTrust(str, Enum):
    """Trust posture for provider-authored fixture text."""

    UNTRUSTED_PROVIDER_CONTENT = "untrusted_provider_content"


class CloudflareCompleteness(str, Enum):
    """Completeness values admitted by offline fixture results."""

    COMPLETE = "complete"
    TRUNCATED = "truncated"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class CloudflareErrorCode(str, Enum):
    """Cloudflare-local failures that never imply a provider call."""

    INVALID_FIXTURE_SHAPE = "INVALID_FIXTURE_SHAPE"
    FIXTURE_NORMALIZATION_FAILED = "FIXTURE_NORMALIZATION_FAILED"
    MISSING_CLOUDFLARE_SCOPE = "MISSING_CLOUDFLARE_SCOPE"
    SENSITIVE_FIXTURE_VALUE = "SENSITIVE_FIXTURE_VALUE"
    UNEXPECTED_MUTATION_FIELD = "UNEXPECTED_MUTATION_FIELD"
    UNSUPPORTED_CLOUDFLARE_CAPABILITY = "UNSUPPORTED_CLOUDFLARE_CAPABILITY"
    UNSUPPORTED_IDENTITY_VARIANT = "UNSUPPORTED_IDENTITY_VARIANT"
    EXECUTION_DISABLED = AdapterErrorCode.EXECUTION_DISABLED.value


@dataclass(frozen=True)
class CloudflareProviderDescriptor(ProviderDescriptor):
    """One descriptor: concrete semantics over an inert generic scaffold."""

    provider_semantics_state: CloudflareSemanticsState
    fixture_normalization_supported: bool
    mutation_supported: bool
    provider_registration_state: str


@dataclass(frozen=True)
class CloudflareCapabilityDescriptor(CapabilityDescriptor):
    """One identity-bound Cloudflare capability registration."""

    identity_variant: CloudflareIdentityVariant
    provider_requirement_label: str
    read_operation_plan_ref: str
    authentication_mode_treatment: str


@dataclass(frozen=True)
class CloudflareCapabilityClassification:
    """One row of the complete accepted 58-capability classification."""

    contract_key: str
    domain: str
    capability_id: CapabilityId
    risk_tier: str
    operation_kind: str
    identity_modes: Tuple[str, ...]
    scope: str
    verification: str
    adapter_inclusion: CloudflareAdapterInclusion


@dataclass(frozen=True)
class CloudflareAuthenticationModeMetadata:
    """Non-runtime documentation of the scaffold authentication-mode gap."""

    provider_account_modes: Tuple[str, ...]
    runtime_selectable: bool
    credential_resolution_supported: bool
    binding_authority: str


@dataclass(frozen=True)
class CloudflareReadOperationPlan:
    """Transport-independent metadata for one identity-bound read operation."""

    plan_ref: str
    provider_id: str
    capability_id: CapabilityId
    provider_native_operation_id: str
    declared_resource_class: CloudflareEntityFamily
    required_scope_names: Tuple[str, ...]
    identity_variant: CloudflareIdentityVariant
    credential_profile_class: str
    acting_identity_type: str
    authentication_target: str
    expected_entity_family: CloudflareEntityFamily
    pagination_metadata: str
    cursor_execution_supported: bool
    verification_expectation: str
    provider_contract_revision: str
    adapter_revision: str


@dataclass(frozen=True)
class CloudflareApiOperation:
    """Normalized synthetic API Shield operation entity."""

    canonical_ref: str
    provider_native_ref: str
    host: str
    path: str
    operation_method: str
    description: str
    trust: CloudflareFixtureTrust
    injection_suspected: bool
    fixture_only: bool
    contract_revision: str


@dataclass(frozen=True)
class CloudflareNormalizedError:
    """Sanitized provider-specific error for local fixture work."""

    code: CloudflareErrorCode
    message: str
    field: Optional[str]
    provider_request_occurred: bool

    def __post_init__(self) -> None:
        if self.provider_request_occurred:
            raise ValueError("fixture errors cannot claim a provider request")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code.value,
            "message": self.message,
            "field": self.field,
            "provider_request_occurred": self.provider_request_occurred,
        }


class CloudflareFixtureError(Exception):
    """Typed deterministic denial for malformed synthetic fixtures."""

    def __init__(self, error: CloudflareNormalizedError) -> None:
        self.error = error
        super().__init__("{}: {}".format(error.code.value, error.message))


@dataclass(frozen=True)
class CloudflareFixtureReadResult:
    """Offline normalized read result that cannot claim provider activity."""

    capability_id: CapabilityId
    tenant_ref: str
    account_ref: str
    zone_ref: str
    observed_at: str
    state_digest: str
    completeness: CloudflareCompleteness
    items: Tuple[CloudflareApiOperation, ...]
    provenance: Tuple[Tuple[str, str], ...]
    trust: CloudflareFixtureTrust
    fixture_only: bool
    provider_request_id: Optional[str]
    provider_authenticated: bool
    provider_request_occurred: bool

    def __post_init__(self) -> None:
        if not self.fixture_only:
            raise ValueError("Cloudflare fixture results must be fixture-only")
        if self.provider_request_id is not None:
            raise ValueError("Cloudflare fixture results have no request ID")
        if self.provider_authenticated or self.provider_request_occurred:
            raise ValueError(
                "Cloudflare fixture results cannot claim provider activity"
            )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "capability_id": self.capability_id.value,
            "tenant_ref": self.tenant_ref,
            "account_ref": self.account_ref,
            "zone_ref": self.zone_ref,
            "observed_at": self.observed_at,
            "state_digest": self.state_digest,
            "completeness": self.completeness.value,
            "items": tuple(item.__dict__.copy() for item in self.items),
            "provenance": dict(self.provenance),
            "trust": self.trust.value,
            "fixture_only": self.fixture_only,
            "provider_request_id": self.provider_request_id,
            "provider_authenticated": self.provider_authenticated,
            "provider_request_occurred": self.provider_request_occurred,
        }
