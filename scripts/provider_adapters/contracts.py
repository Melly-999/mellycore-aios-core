"""Provider-neutral contracts for the inert MellyCore adapter scaffold.

The normative sources are the Provider Registry and Integration Gateway
contracts under ``docs/specs``.  This module intentionally contains only
immutable values and typed shapes.  It performs no I/O and grants no runtime
authority.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, Optional, Tuple


PROVIDER_ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
CAPABILITY_ID_PATTERN = re.compile(
    r"^[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+$"
)


class CredentialProfileClass(str, Enum):
    """Registry Section 13.2's closed reusable class vocabulary."""

    READ_ONLY_DELEGATED = "read_only_delegated"
    READ_ONLY_SERVICE = "read_only_service"
    CONTROLLED_WRITE = "controlled_write"
    EVENT_VERIFICATION = "event_verification"
    INTEGRATION_FABRIC_READ = "integration_fabric_read"
    INTEGRATION_FABRIC_CONTROLLED_WRITE = "integration_fabric_controlled_write"
    EMERGENCY_CONTAINMENT = "emergency_containment"
    REPORTING_ONLY = "reporting_only"
    RESTRICTED_OPERATOR_INVESTIGATION = "restricted_operator_investigation"


class ActingIdentityType(str, Enum):
    """Registry Section 7.5's raw-text canonical vocabulary."""

    DELEGATED_USER = "delegated_user"
    SERVICE_ACCOUNT = "service_account"
    MELLYCORE_OPERATOR = "mellycore_operator"


class AuthenticationTarget(str, Enum):
    """Registry Section 12.1's closed authentication targets."""

    PROVIDER_ACCOUNT = "provider_account"
    RESTRICTED_TOOL = "restricted_tool"
    INTEGRATION_FABRIC = "integration_fabric"


class ScopeApplicability(str, Enum):
    """Registry Section 11's explicit applicability values."""

    REQUIRED = "required"
    OPTIONAL = "optional"
    NOT_APPLICABLE = "not_applicable"


class ScopeFamily(str, Enum):
    """The three independent scope families owned by Registry Section 11."""

    MELLYCORE = "mellycore"
    PROVIDER_NATIVE = "provider_native"
    RESTRICTED_TOOL = "restricted_tool"


class RiskTier(str, Enum):
    """The canonical R0-R5 risk vocabulary."""

    R0 = "R0"
    R1 = "R1"
    R2 = "R2"
    R3 = "R3"
    R4 = "R4"
    R5 = "R5"


class AuthorizationFactStatus(str, Enum):
    """Status for one fact without collapsing it into aggregate readiness."""

    SATISFIED = "satisfied"
    UNSATISFIED = "unsatisfied"
    NOT_REQUIRED = "not_required"


class AdapterKind(str, Enum):
    """Kinds admitted by this first scaffold."""

    SCAFFOLD = "scaffold"


class ImplementationState(str, Enum):
    """Implementation truthfulness for the inert scaffold."""

    SCAFFOLD_ONLY = "scaffold_only"


class NetworkBehavior(str, Enum):
    """Network behavior admitted by this package."""

    DISABLED = "disabled"


class CredentialSupport(str, Enum):
    """Credential behavior admitted by this package."""

    UNSUPPORTED = "unsupported"


class ExecutionState(str, Enum):
    """Execution behavior admitted by this package."""

    DISABLED = "disabled"


class CapabilityClassification(str, Enum):
    """Registry Section 14's capability classifications."""

    READ = "read"
    PROPOSAL = "proposal"
    MUTATION = "mutation"
    PROHIBITED = "prohibited"
    INVESTIGATION = "investigation"


class ApprovalRequirement(str, Enum):
    """Static approval policy metadata; never an approval decision."""

    NOT_REQUIRED = "not_required"
    TENANT_POLICY = "tenant_policy"
    EXPLICIT_HUMAN = "explicit_human"


class ExternalContentExposure(str, Enum):
    """Whether normalized output can carry untrusted external content."""

    NONE = "none"
    UNTRUSTED = "untrusted"


class OperationOutcome(str, Enum):
    """The only outcomes representable by this inert scaffold."""

    VALIDATION_DENIED = "validation_denied"
    EXECUTION_DISABLED = "execution_disabled"
    FIXTURE_ONLY = "fixture_only"


class ErrorPhase(str, Enum):
    """Distinguish local validation denial from inert execution failure."""

    MANIFEST_VALIDATION = "manifest_validation"
    ENVELOPE_VALIDATION = "envelope_validation"
    EXECUTION = "execution"


class AdapterErrorCode(str, Enum):
    """Stable machine-readable error codes for the scaffold boundary."""

    INVALID_PROVIDER_ID = "INVALID_PROVIDER_ID"
    INVALID_CAPABILITY_ID = "INVALID_CAPABILITY_ID"
    INVALID_CANONICAL_VALUE = "INVALID_CANONICAL_VALUE"
    DUPLICATE_CAPABILITY_ID = "DUPLICATE_CAPABILITY_ID"
    UNKNOWN_CAPABILITY = "UNKNOWN_CAPABILITY"
    MANIFEST_MISMATCH = "MANIFEST_MISMATCH"
    INCOMPATIBLE_CREDENTIAL_CLASS = "INCOMPATIBLE_CREDENTIAL_CLASS"
    INCOMPATIBLE_ACTING_IDENTITY = "INCOMPATIBLE_ACTING_IDENTITY"
    INCOMPATIBLE_AUTHENTICATION_TARGET = "INCOMPATIBLE_AUTHENTICATION_TARGET"
    MISSING_REQUIRED_SCOPE = "MISSING_REQUIRED_SCOPE"
    UNEXPECTED_SCOPE_FOR_NOT_APPLICABLE = (
        "UNEXPECTED_SCOPE_FOR_NOT_APPLICABLE"
    )
    MISSING_SCOPE_APPLICABILITY = "MISSING_SCOPE_APPLICABILITY"
    UNKNOWN_SCOPE_DIMENSION = "UNKNOWN_SCOPE_DIMENSION"
    MISSING_CREDENTIAL_MATCH = "MISSING_CREDENTIAL_MATCH"
    AMBIGUOUS_CREDENTIAL_MATCH = "AMBIGUOUS_CREDENTIAL_MATCH"
    MISSING_CONTRACT_REVISION = "MISSING_CONTRACT_REVISION"
    UNSUPPORTED_EXECUTION = "UNSUPPORTED_EXECUTION"
    EXECUTION_DISABLED = "EXECUTION_DISABLED"
    EXTERNAL_CONTENT_VALIDATION_FAILED = (
        "EXTERNAL_CONTENT_VALIDATION_FAILED"
    )
    FIXTURE_ONLY_OPERATION = "FIXTURE_ONLY_OPERATION"
    SENSITIVE_VALUE_REJECTED = "SENSITIVE_VALUE_REJECTED"
    INVALID_APPROVAL_STATUS = "INVALID_APPROVAL_STATUS"


@dataclass(frozen=True)
class NormalizedAdapterError:
    """Sanitized error safe for outward serialization."""

    code: AdapterErrorCode
    phase: ErrorPhase
    message: str
    field: Optional[str]
    provider_request_occurred: bool

    def __post_init__(self) -> None:
        if self.provider_request_occurred:
            raise ValueError("scaffold errors cannot claim a provider request")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "code": self.code.value,
            "phase": self.phase.value,
            "message": self.message,
            "field": self.field,
            "provider_request_occurred": self.provider_request_occurred,
        }


class AdapterValidationError(Exception):
    """Typed local validation denial with a sanitized normalized error."""

    def __init__(self, error: NormalizedAdapterError) -> None:
        self.error = error
        super().__init__("{}: {}".format(error.code.value, error.message))


@dataclass(frozen=True)
class ProviderId:
    """A canonical Registry provider identifier."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not PROVIDER_ID_PATTERN.fullmatch(
            self.value
        ):
            raise AdapterValidationError(
                NormalizedAdapterError(
                    code=AdapterErrorCode.INVALID_PROVIDER_ID,
                    phase=ErrorPhase.MANIFEST_VALIDATION,
                    message="provider ID does not match the canonical grammar",
                    field="provider_id",
                    provider_request_occurred=False,
                )
            )

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class CapabilityId:
    """A stable provider-prefixed capability identifier."""

    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not CAPABILITY_ID_PATTERN.fullmatch(
            self.value
        ):
            raise AdapterValidationError(
                NormalizedAdapterError(
                    code=AdapterErrorCode.INVALID_CAPABILITY_ID,
                    phase=ErrorPhase.MANIFEST_VALIDATION,
                    message="capability ID does not match the canonical grammar",
                    field="capability_id",
                    provider_request_occurred=False,
                )
            )

    def __str__(self) -> str:
        return self.value


@dataclass(frozen=True)
class ContractScopeDimension:
    """One provider-contract-owned scope dimension and its permitted states."""

    family: ScopeFamily
    name: str
    optional_absence_permitted: bool
    not_applicable_permitted: bool


@dataclass(frozen=True)
class ScopeApplicabilityEntry:
    """One explicit applicability decision for one declared dimension."""

    family: ScopeFamily
    name: str
    applicability: ScopeApplicability


@dataclass(frozen=True)
class ScopeReference:
    """One opaque resolved reference for an applicable scope dimension."""

    family: ScopeFamily
    name: str
    value_ref: str


@dataclass(frozen=True)
class ProviderDescriptor:
    """Static adapter metadata; existence is not provider registration."""

    provider_id: ProviderId
    display_name: str
    provider_family: str
    contract_ref: str
    contract_revision: str
    adapter_kind: AdapterKind
    supported_environments: Tuple[str, ...]
    capability_manifest_revision: str
    adapter_revision: str
    implementation_state: ImplementationState
    network_behavior: NetworkBehavior
    credential_support: CredentialSupport
    execution_state: ExecutionState


@dataclass(frozen=True)
class CapabilityDescriptor:
    """Static provider-neutral capability metadata used only for validation."""

    provider_id: ProviderId
    capability_id: CapabilityId
    capability_version: str
    provider_contract_ref: str
    provider_contract_revision: str
    provider_native_capability_ref: str
    risk_tier: RiskTier
    required_credential_profile_class: CredentialProfileClass
    required_acting_identity_type: ActingIdentityType
    required_authentication_target: AuthenticationTarget
    contract_scope_dimensions: Tuple[ContractScopeDimension, ...]
    scope_applicability: Tuple[ScopeApplicabilityEntry, ...]
    data_sensitivity_ref: str
    external_content_exposure: ExternalContentExposure
    classification: CapabilityClassification
    verification_required: bool
    approval_requirement: ApprovalRequirement
    audit_required: bool


@dataclass(frozen=True)
class AuthorizationFacts:
    """The eight Registry facts, kept as eight independent fields."""

    provider_registered: AuthorizationFactStatus
    adapter_implemented: AuthorizationFactStatus
    credential_configured: AuthorizationFactStatus
    credential_verified: AuthorizationFactStatus
    tenant_authorized: AuthorizationFactStatus
    capability_authorized: AuthorizationFactStatus
    runtime_enabled: AuthorizationFactStatus
    operation_approved: AuthorizationFactStatus


@dataclass(frozen=True)
class ResolvedExecutionEnvelope:
    """Immutable adapter-bound validation input with opaque references only."""

    request_id: str
    request_fingerprint: str
    tenant_ref: str
    provider_id: ProviderId
    capability_id: CapabilityId
    capability_version: str
    environment: str
    acting_identity_type: ActingIdentityType
    acting_identity_ref: str
    credential_profile_class: CredentialProfileClass
    credential_profile_ref: str
    credential_profile_match_count: int
    authentication_target: AuthenticationTarget
    scope_applicability: Tuple[ScopeApplicabilityEntry, ...]
    scope_references: Tuple[ScopeReference, ...]
    risk_tier: RiskTier
    provider_contract_revision: str
    adapter_revision: str
    authorization_record_refs: Tuple[str, ...]
    runtime_enablement_ref: Optional[str]
    approval_ref: Optional[str]
    audit_intent_ref: Optional[str]
    external_content: bool
    correlation_ref: str
    authorization_facts: AuthorizationFacts


@dataclass(frozen=True)
class NormalizedOperationResult:
    """A local-only result shape with no representable success outcome."""

    request_id: str
    provider_id: ProviderId
    capability_id: CapabilityId
    outcome: OperationOutcome
    fixture_only: bool
    provider_request_id: Optional[str]
    provider_authenticated: bool
    provider_mutation_completed: bool
    payload: Tuple[Tuple[str, Any], ...]
    error: NormalizedAdapterError
    provenance: Tuple[Tuple[str, str], ...]

    def __post_init__(self) -> None:
        if self.provider_request_id is not None:
            raise ValueError("scaffold results cannot carry provider request IDs")
        if self.provider_authenticated or self.provider_mutation_completed:
            raise ValueError("scaffold results cannot claim provider activity")
        if self.outcome is OperationOutcome.FIXTURE_ONLY and not self.fixture_only:
            raise ValueError("fixture-only outcomes must be explicitly marked")
        if self.outcome is not OperationOutcome.FIXTURE_ONLY and self.fixture_only:
            raise ValueError("only fixture-only outcomes may carry the fixture marker")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "request_id": self.request_id,
            "provider_id": self.provider_id.value,
            "capability_id": self.capability_id.value,
            "outcome": self.outcome.value,
            "fixture_only": self.fixture_only,
            "provider_request_id": self.provider_request_id,
            "provider_authenticated": self.provider_authenticated,
            "provider_mutation_completed": self.provider_mutation_completed,
            "payload": dict(self.payload),
            "error": self.error.to_dict(),
            "provenance": dict(self.provenance),
        }
