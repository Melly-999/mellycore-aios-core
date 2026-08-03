"""Fail-closed static validation for provider-adapter scaffold contracts.

Validation is deterministic and standard-library-only.  It never parses the
Registry's rendered Markdown, reads credentials, contacts a provider, or
authorizes an operation.
"""

from __future__ import annotations

import hashlib
import re
from enum import Enum
from typing import Any, Dict, Optional, Sequence, Set, Tuple, Type, TypeVar

from .contracts import (
    ActingIdentityType,
    AdapterErrorCode,
    AdapterKind,
    AdapterValidationError,
    ApprovalRequirement,
    AuthenticationTarget,
    AuthorizationFactStatus,
    CapabilityClassification,
    CapabilityDescriptor,
    ContractScopeDimension,
    CredentialProfileClass,
    CredentialSupport,
    ErrorPhase,
    ExecutionState,
    ExternalContentExposure,
    ImplementationState,
    NetworkBehavior,
    NormalizedAdapterError,
    ProviderDescriptor,
    ResolvedExecutionEnvelope,
    RiskTier,
    ScopeApplicability,
    ScopeApplicabilityEntry,
    ScopeFamily,
)


_EnumT = TypeVar("_EnumT", bound=Enum)

_NAME_PATTERN = re.compile(r"^[a-z][a-z0-9_]*$")
_OPAQUE_REFERENCE_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{2,127}$")
_SENSITIVE_VALUE_PATTERNS = (
    re.compile(r"(?i)\bbearer\s+[a-z0-9._-]+"),
    re.compile(r"(?i)\b(?:api[_-]?key|client[_-]?secret|password)\s*[:=]"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{12,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
)

_CLASS_IDENTITIES = {
    CredentialProfileClass.READ_ONLY_DELEGATED: {
        ActingIdentityType.DELEGATED_USER
    },
    CredentialProfileClass.READ_ONLY_SERVICE: {
        ActingIdentityType.SERVICE_ACCOUNT
    },
    CredentialProfileClass.CONTROLLED_WRITE: {
        ActingIdentityType.DELEGATED_USER,
        ActingIdentityType.SERVICE_ACCOUNT,
    },
    CredentialProfileClass.EVENT_VERIFICATION: set(),
    CredentialProfileClass.INTEGRATION_FABRIC_READ: {
        ActingIdentityType.DELEGATED_USER,
        ActingIdentityType.SERVICE_ACCOUNT,
    },
    CredentialProfileClass.INTEGRATION_FABRIC_CONTROLLED_WRITE: {
        ActingIdentityType.DELEGATED_USER,
        ActingIdentityType.SERVICE_ACCOUNT,
    },
    CredentialProfileClass.EMERGENCY_CONTAINMENT: {
        ActingIdentityType.SERVICE_ACCOUNT
    },
    CredentialProfileClass.REPORTING_ONLY: {
        ActingIdentityType.SERVICE_ACCOUNT
    },
    CredentialProfileClass.RESTRICTED_OPERATOR_INVESTIGATION: {
        ActingIdentityType.MELLYCORE_OPERATOR
    },
}

_CLASS_TARGETS = {
    CredentialProfileClass.READ_ONLY_DELEGATED: {
        AuthenticationTarget.PROVIDER_ACCOUNT
    },
    CredentialProfileClass.READ_ONLY_SERVICE: {
        AuthenticationTarget.PROVIDER_ACCOUNT
    },
    CredentialProfileClass.CONTROLLED_WRITE: {
        AuthenticationTarget.PROVIDER_ACCOUNT
    },
    CredentialProfileClass.EVENT_VERIFICATION: {
        AuthenticationTarget.PROVIDER_ACCOUNT
    },
    CredentialProfileClass.INTEGRATION_FABRIC_READ: {
        AuthenticationTarget.INTEGRATION_FABRIC
    },
    CredentialProfileClass.INTEGRATION_FABRIC_CONTROLLED_WRITE: {
        AuthenticationTarget.INTEGRATION_FABRIC
    },
    CredentialProfileClass.EMERGENCY_CONTAINMENT: {
        AuthenticationTarget.PROVIDER_ACCOUNT
    },
    CredentialProfileClass.REPORTING_ONLY: {
        AuthenticationTarget.PROVIDER_ACCOUNT
    },
    CredentialProfileClass.RESTRICTED_OPERATOR_INVESTIGATION: {
        AuthenticationTarget.RESTRICTED_TOOL
    },
}

_RESTRICTED_TOOL_DIMENSIONS = {
    "restricted_tool_id",
    "tool_contract_revision",
    "tool_capability",
    "operator",
    "tenant",
    "environment",
    "allowed_resource_class",
}


def _deny(
    code: AdapterErrorCode,
    phase: ErrorPhase,
    message: str,
    field: Optional[str],
) -> None:
    raise AdapterValidationError(
        NormalizedAdapterError(
            code=code,
            phase=phase,
            message=message,
            field=field,
            provider_request_occurred=False,
        )
    )


def parse_canonical_value(
    enum_type: Type[_EnumT], value: str, field: str
) -> _EnumT:
    """Parse one exact enum value without coercion, aliasing, or fallback."""

    try:
        return enum_type(value)
    except (TypeError, ValueError):
        _deny(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            ErrorPhase.MANIFEST_VALIDATION,
            "field contains an unknown canonical value",
            field,
        )
    raise AssertionError("unreachable")


def _require_enum(
    value: Any,
    enum_type: Type[_EnumT],
    field: str,
    phase: ErrorPhase,
) -> _EnumT:
    if not isinstance(value, enum_type):
        _deny(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            phase,
            "field must contain one exact canonical enum value",
            field,
        )
    return value


def _require_text(value: Any, field: str, phase: ErrorPhase) -> str:
    if not isinstance(value, str) or not value.strip():
        code = (
            AdapterErrorCode.MISSING_CONTRACT_REVISION
            if "revision" in field
            else AdapterErrorCode.MANIFEST_MISMATCH
        )
        _deny(code, phase, "required text field is missing", field)
    return value


def _looks_sensitive(value: str) -> bool:
    return any(pattern.search(value) for pattern in _SENSITIVE_VALUE_PATTERNS)


def _require_opaque_reference(
    value: Any, field: str, phase: ErrorPhase
) -> str:
    if (
        not isinstance(value, str)
        or not _OPAQUE_REFERENCE_PATTERN.fullmatch(value)
        or _looks_sensitive(value)
    ):
        _deny(
            AdapterErrorCode.SENSITIVE_VALUE_REJECTED,
            phase,
            "field must contain one non-sensitive opaque reference",
            field,
        )
    return value


def public_reference(value: Any) -> str:
    """Return a safe correlation reference without exposing rejected input."""

    if (
        isinstance(value, str)
        and _OPAQUE_REFERENCE_PATTERN.fullmatch(value)
        and not _looks_sensitive(value)
    ):
        return value
    digest = hashlib.sha256(str(value).encode("utf-8")).hexdigest()[:16]
    return "redacted-{}".format(digest)


def _scope_key(item: Any) -> Tuple[ScopeFamily, str]:
    return item.family, item.name


def _validate_contract_scope_dimensions(
    dimensions: Sequence[ContractScopeDimension],
    phase: ErrorPhase,
) -> Dict[Tuple[ScopeFamily, str], ContractScopeDimension]:
    if not isinstance(dimensions, tuple) or not dimensions:
        _deny(
            AdapterErrorCode.MISSING_SCOPE_APPLICABILITY,
            phase,
            "provider contract scope dimensions must be an immutable non-empty tuple",
            "contract_scope_dimensions",
        )
    resolved: Dict[Tuple[ScopeFamily, str], ContractScopeDimension] = {}
    for item in dimensions:
        if not isinstance(item, ContractScopeDimension):
            _deny(
                AdapterErrorCode.INVALID_CANONICAL_VALUE,
                phase,
                "scope dimension must use the canonical typed shape",
                "contract_scope_dimensions",
            )
        _require_enum(item.family, ScopeFamily, "scope_family", phase)
        if not isinstance(item.name, str) or not _NAME_PATTERN.fullmatch(item.name):
            _deny(
                AdapterErrorCode.UNKNOWN_SCOPE_DIMENSION,
                phase,
                "scope dimension name is not canonical",
                "contract_scope_dimensions",
            )
        key = _scope_key(item)
        if key in resolved:
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                phase,
                "provider contract scope dimension is duplicated",
                "contract_scope_dimensions",
            )
        resolved[key] = item
    return resolved


def _validate_scope_applicability(
    contract_dimensions: Dict[Tuple[ScopeFamily, str], ContractScopeDimension],
    entries: Sequence[ScopeApplicabilityEntry],
    phase: ErrorPhase,
) -> Dict[Tuple[ScopeFamily, str], ScopeApplicabilityEntry]:
    if not isinstance(entries, tuple) or not entries:
        _deny(
            AdapterErrorCode.MISSING_SCOPE_APPLICABILITY,
            phase,
            "scope applicability must be an immutable complete declaration",
            "scope_applicability",
        )
    resolved: Dict[Tuple[ScopeFamily, str], ScopeApplicabilityEntry] = {}
    for entry in entries:
        if not isinstance(entry, ScopeApplicabilityEntry):
            _deny(
                AdapterErrorCode.INVALID_CANONICAL_VALUE,
                phase,
                "scope applicability must use the canonical typed shape",
                "scope_applicability",
            )
        _require_enum(entry.family, ScopeFamily, "scope_family", phase)
        _require_enum(
            entry.applicability,
            ScopeApplicability,
            "scope_applicability",
            phase,
        )
        key = _scope_key(entry)
        if key not in contract_dimensions:
            _deny(
                AdapterErrorCode.UNKNOWN_SCOPE_DIMENSION,
                phase,
                "scope applicability names an undeclared dimension",
                "scope_applicability",
            )
        if key in resolved:
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                phase,
                "scope applicability dimension is duplicated",
                "scope_applicability",
            )
        contract_dimension = contract_dimensions[key]
        if (
            entry.applicability is ScopeApplicability.OPTIONAL
            and not contract_dimension.optional_absence_permitted
        ):
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                phase,
                "optional applicability is not permitted by the provider contract",
                "scope_applicability",
            )
        if (
            entry.applicability is ScopeApplicability.NOT_APPLICABLE
            and not contract_dimension.not_applicable_permitted
        ):
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                phase,
                "not-applicable is not permitted by the provider contract",
                "scope_applicability",
            )
        resolved[key] = entry
    if set(resolved) != set(contract_dimensions):
        _deny(
            AdapterErrorCode.MISSING_SCOPE_APPLICABILITY,
            phase,
            "scope applicability declaration is incomplete",
            "scope_applicability",
        )
    return resolved


def _validate_binding(capability: CapabilityDescriptor) -> None:
    credential_class = _require_enum(
        capability.required_credential_profile_class,
        CredentialProfileClass,
        "required_credential_profile_class",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    identity = _require_enum(
        capability.required_acting_identity_type,
        ActingIdentityType,
        "required_acting_identity_type",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    target = _require_enum(
        capability.required_authentication_target,
        AuthenticationTarget,
        "required_authentication_target",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    if identity not in _CLASS_IDENTITIES[credential_class]:
        _deny(
            AdapterErrorCode.INCOMPATIBLE_ACTING_IDENTITY,
            ErrorPhase.MANIFEST_VALIDATION,
            "acting identity is incompatible with the canonical credential class",
            "required_acting_identity_type",
        )
    if target not in _CLASS_TARGETS[credential_class]:
        _deny(
            AdapterErrorCode.INCOMPATIBLE_AUTHENTICATION_TARGET,
            ErrorPhase.MANIFEST_VALIDATION,
            "authentication target is incompatible with the canonical credential class",
            "required_authentication_target",
        )


def _validate_restricted_tool_capability(
    capability: CapabilityDescriptor,
    applicability: Dict[Tuple[ScopeFamily, str], ScopeApplicabilityEntry],
) -> None:
    if (
        capability.required_credential_profile_class
        is not CredentialProfileClass.RESTRICTED_OPERATOR_INVESTIGATION
    ):
        return
    if capability.classification is not CapabilityClassification.INVESTIGATION:
        _deny(
            AdapterErrorCode.INCOMPATIBLE_CREDENTIAL_CLASS,
            ErrorPhase.MANIFEST_VALIDATION,
            "restricted operator class is validation-only investigation scope",
            "classification",
        )
    if capability.risk_tier not in {RiskTier.R0, RiskTier.R1, RiskTier.R2}:
        _deny(
            AdapterErrorCode.INCOMPATIBLE_CREDENTIAL_CLASS,
            ErrorPhase.MANIFEST_VALIDATION,
            "restricted operator class cannot serve this risk tier",
            "risk_tier",
        )
    provider_entries = {
        key: entry
        for key, entry in applicability.items()
        if key[0] is ScopeFamily.PROVIDER_NATIVE
    }
    if not provider_entries or any(
        entry.applicability is not ScopeApplicability.NOT_APPLICABLE
        for entry in provider_entries.values()
    ):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.MANIFEST_VALIDATION,
            "restricted operator capability requires explicit provider-native non-applicability",
            "scope_applicability",
        )
    restricted_entries = {
        key[1]: entry
        for key, entry in applicability.items()
        if key[0] is ScopeFamily.RESTRICTED_TOOL
    }
    if set(restricted_entries) != _RESTRICTED_TOOL_DIMENSIONS or any(
        entry.applicability is not ScopeApplicability.REQUIRED
        for entry in restricted_entries.values()
    ):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.MANIFEST_VALIDATION,
            "restricted operator capability requires the exact restricted-tool scope",
            "scope_applicability",
        )


def validate_manifest(
    descriptor: ProviderDescriptor,
    capabilities: Sequence[CapabilityDescriptor],
) -> None:
    """Validate one inert static descriptor and capability manifest."""

    if not isinstance(descriptor, ProviderDescriptor):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.MANIFEST_VALIDATION,
            "descriptor must use the immutable ProviderDescriptor shape",
            "descriptor",
        )
    _require_text(descriptor.display_name, "display_name", ErrorPhase.MANIFEST_VALIDATION)
    _require_text(
        descriptor.provider_family,
        "provider_family",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    _require_text(descriptor.contract_ref, "contract_ref", ErrorPhase.MANIFEST_VALIDATION)
    _require_text(
        descriptor.contract_revision,
        "contract_revision",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    _require_text(
        descriptor.capability_manifest_revision,
        "capability_manifest_revision",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    _require_text(
        descriptor.adapter_revision,
        "adapter_revision",
        ErrorPhase.MANIFEST_VALIDATION,
    )
    if (
        not isinstance(descriptor.supported_environments, tuple)
        or not descriptor.supported_environments
        or len(set(descriptor.supported_environments))
        != len(descriptor.supported_environments)
    ):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.MANIFEST_VALIDATION,
            "supported environments must be an explicit unique tuple",
            "supported_environments",
        )
    for environment in descriptor.supported_environments:
        _require_opaque_reference(
            environment, "supported_environments", ErrorPhase.MANIFEST_VALIDATION
        )
    if descriptor.adapter_kind is not AdapterKind.SCAFFOLD:
        _deny(
            AdapterErrorCode.UNSUPPORTED_EXECUTION,
            ErrorPhase.MANIFEST_VALIDATION,
            "only scaffold adapter kind is permitted",
            "adapter_kind",
        )
    if descriptor.implementation_state is not ImplementationState.SCAFFOLD_ONLY:
        _deny(
            AdapterErrorCode.UNSUPPORTED_EXECUTION,
            ErrorPhase.MANIFEST_VALIDATION,
            "implementation state must remain scaffold-only",
            "implementation_state",
        )
    if descriptor.network_behavior is not NetworkBehavior.DISABLED:
        _deny(
            AdapterErrorCode.UNSUPPORTED_EXECUTION,
            ErrorPhase.MANIFEST_VALIDATION,
            "network behavior must remain disabled",
            "network_behavior",
        )
    if descriptor.credential_support is not CredentialSupport.UNSUPPORTED:
        _deny(
            AdapterErrorCode.UNSUPPORTED_EXECUTION,
            ErrorPhase.MANIFEST_VALIDATION,
            "credential behavior must remain unsupported",
            "credential_support",
        )
    if descriptor.execution_state is not ExecutionState.DISABLED:
        _deny(
            AdapterErrorCode.UNSUPPORTED_EXECUTION,
            ErrorPhase.MANIFEST_VALIDATION,
            "execution state must remain disabled",
            "execution_state",
        )
    if not isinstance(capabilities, tuple):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.MANIFEST_VALIDATION,
            "capability manifest must be an immutable tuple",
            "capabilities",
        )
    seen: Set[str] = set()
    for capability in capabilities:
        if not isinstance(capability, CapabilityDescriptor):
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                ErrorPhase.MANIFEST_VALIDATION,
                "capability must use the immutable descriptor shape",
                "capabilities",
            )
        if capability.capability_id.value in seen:
            _deny(
                AdapterErrorCode.DUPLICATE_CAPABILITY_ID,
                ErrorPhase.MANIFEST_VALIDATION,
                "capability ID is duplicated",
                "capability_id",
            )
        seen.add(capability.capability_id.value)
        if capability.provider_id != descriptor.provider_id:
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                ErrorPhase.MANIFEST_VALIDATION,
                "capability provider does not match the descriptor",
                "provider_id",
            )
        if not capability.capability_id.value.startswith(
            descriptor.provider_id.value + "."
        ):
            _deny(
                AdapterErrorCode.INVALID_CAPABILITY_ID,
                ErrorPhase.MANIFEST_VALIDATION,
                "capability ID is not prefixed by the canonical provider ID",
                "capability_id",
            )
        _require_text(
            capability.capability_version,
            "capability_version",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_text(
            capability.provider_contract_ref,
            "provider_contract_ref",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_text(
            capability.provider_contract_revision,
            "provider_contract_revision",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_text(
            capability.provider_native_capability_ref,
            "provider_native_capability_ref",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_text(
            capability.data_sensitivity_ref,
            "data_sensitivity_ref",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        if (
            capability.provider_contract_ref != descriptor.contract_ref
            or capability.provider_contract_revision
            != descriptor.contract_revision
        ):
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                ErrorPhase.MANIFEST_VALIDATION,
                "capability contract does not match the adapter descriptor",
                "provider_contract_revision",
            )
        _require_enum(
            capability.risk_tier,
            RiskTier,
            "risk_tier",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_enum(
            capability.classification,
            CapabilityClassification,
            "classification",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_enum(
            capability.approval_requirement,
            ApprovalRequirement,
            "approval_requirement",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _require_enum(
            capability.external_content_exposure,
            ExternalContentExposure,
            "external_content_exposure",
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _validate_binding(capability)
        dimensions = _validate_contract_scope_dimensions(
            capability.contract_scope_dimensions,
            ErrorPhase.MANIFEST_VALIDATION,
        )
        applicability = _validate_scope_applicability(
            dimensions,
            capability.scope_applicability,
            ErrorPhase.MANIFEST_VALIDATION,
        )
        _validate_restricted_tool_capability(capability, applicability)
        if capability.risk_tier in {RiskTier.R4, RiskTier.R5} and (
            capability.approval_requirement
            is not ApprovalRequirement.EXPLICIT_HUMAN
        ):
            _deny(
                AdapterErrorCode.INVALID_APPROVAL_STATUS,
                ErrorPhase.MANIFEST_VALIDATION,
                "R4-R5 capabilities require explicit human approval metadata",
                "approval_requirement",
            )
        if (
            capability.classification is CapabilityClassification.MUTATION
            and not capability.verification_required
        ):
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                ErrorPhase.MANIFEST_VALIDATION,
                "mutation capability requires verification metadata",
                "verification_required",
            )
        if not capability.audit_required:
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                ErrorPhase.MANIFEST_VALIDATION,
                "capability audit metadata cannot be disabled",
                "audit_required",
            )


def _validate_fact_statuses(envelope: ResolvedExecutionEnvelope) -> None:
    facts = envelope.authorization_facts
    standing = (
        ("provider_registered", facts.provider_registered),
        ("adapter_implemented", facts.adapter_implemented),
        ("credential_configured", facts.credential_configured),
        ("credential_verified", facts.credential_verified),
        ("tenant_authorized", facts.tenant_authorized),
        ("capability_authorized", facts.capability_authorized),
        ("runtime_enabled", facts.runtime_enabled),
    )
    for field, status in standing:
        _require_enum(
            status,
            AuthorizationFactStatus,
            field,
            ErrorPhase.ENVELOPE_VALIDATION,
        )
        if status is AuthorizationFactStatus.NOT_REQUIRED:
            _deny(
                AdapterErrorCode.INVALID_CANONICAL_VALUE,
                ErrorPhase.ENVELOPE_VALIDATION,
                "standing authorization fact cannot be not-required",
                field,
            )
    approval = _require_enum(
        facts.operation_approved,
        AuthorizationFactStatus,
        "operation_approved",
        ErrorPhase.ENVELOPE_VALIDATION,
    )
    if envelope.risk_tier in {RiskTier.R3, RiskTier.R4, RiskTier.R5}:
        if approval is not AuthorizationFactStatus.SATISFIED:
            _deny(
                AdapterErrorCode.INVALID_APPROVAL_STATUS,
                ErrorPhase.ENVELOPE_VALIDATION,
                "risk tier requires a separately satisfied operation approval",
                "operation_approved",
            )
        if envelope.approval_ref is None:
            _deny(
                AdapterErrorCode.INVALID_APPROVAL_STATUS,
                ErrorPhase.ENVELOPE_VALIDATION,
                "satisfied operation approval requires an opaque reference",
                "approval_ref",
            )
    elif approval is AuthorizationFactStatus.NOT_REQUIRED:
        if envelope.approval_ref is not None:
            _deny(
                AdapterErrorCode.INVALID_APPROVAL_STATUS,
                ErrorPhase.ENVELOPE_VALIDATION,
                "not-required approval cannot carry an approval reference",
                "approval_ref",
            )
    elif approval is AuthorizationFactStatus.SATISFIED and envelope.approval_ref is None:
        _deny(
            AdapterErrorCode.INVALID_APPROVAL_STATUS,
            ErrorPhase.ENVELOPE_VALIDATION,
            "satisfied operation approval requires an opaque reference",
            "approval_ref",
        )


def _validate_envelope_references(envelope: ResolvedExecutionEnvelope) -> None:
    required = (
        ("request_id", envelope.request_id),
        ("request_fingerprint", envelope.request_fingerprint),
        ("tenant_ref", envelope.tenant_ref),
        ("environment", envelope.environment),
        ("acting_identity_ref", envelope.acting_identity_ref),
        ("credential_profile_ref", envelope.credential_profile_ref),
        ("correlation_ref", envelope.correlation_ref),
    )
    for field, value in required:
        _require_opaque_reference(value, field, ErrorPhase.ENVELOPE_VALIDATION)
    for field, value in (
        ("runtime_enablement_ref", envelope.runtime_enablement_ref),
        ("approval_ref", envelope.approval_ref),
        ("audit_intent_ref", envelope.audit_intent_ref),
    ):
        if value is not None:
            _require_opaque_reference(value, field, ErrorPhase.ENVELOPE_VALIDATION)
    if not isinstance(envelope.authorization_record_refs, tuple):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "authorization references must be an immutable tuple",
            "authorization_record_refs",
        )
    for value in envelope.authorization_record_refs:
        _require_opaque_reference(
            value, "authorization_record_refs", ErrorPhase.ENVELOPE_VALIDATION
        )


def validate_envelope(
    descriptor: ProviderDescriptor,
    capabilities: Sequence[CapabilityDescriptor],
    envelope: ResolvedExecutionEnvelope,
) -> None:
    """Validate a resolved envelope without authorizing or executing it."""

    validate_manifest(descriptor, capabilities)
    if not isinstance(envelope, ResolvedExecutionEnvelope):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "envelope must use the immutable resolved shape",
            "envelope",
        )
    capability = next(
        (
            item
            for item in capabilities
            if item.capability_id == envelope.capability_id
        ),
        None,
    )
    if capability is None:
        _deny(
            AdapterErrorCode.UNKNOWN_CAPABILITY,
            ErrorPhase.ENVELOPE_VALIDATION,
            "capability is not present in the static manifest",
            "capability_id",
        )
    if envelope.provider_id != descriptor.provider_id:
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "envelope provider does not match the adapter descriptor",
            "provider_id",
        )
    comparisons = (
        (
            "capability_version",
            envelope.capability_version,
            capability.capability_version,
            AdapterErrorCode.MANIFEST_MISMATCH,
        ),
        (
            "credential_profile_class",
            envelope.credential_profile_class,
            capability.required_credential_profile_class,
            AdapterErrorCode.INCOMPATIBLE_CREDENTIAL_CLASS,
        ),
        (
            "acting_identity_type",
            envelope.acting_identity_type,
            capability.required_acting_identity_type,
            AdapterErrorCode.INCOMPATIBLE_ACTING_IDENTITY,
        ),
        (
            "authentication_target",
            envelope.authentication_target,
            capability.required_authentication_target,
            AdapterErrorCode.INCOMPATIBLE_AUTHENTICATION_TARGET,
        ),
        (
            "risk_tier",
            envelope.risk_tier,
            capability.risk_tier,
            AdapterErrorCode.MANIFEST_MISMATCH,
        ),
        (
            "provider_contract_revision",
            envelope.provider_contract_revision,
            capability.provider_contract_revision,
            AdapterErrorCode.MISSING_CONTRACT_REVISION,
        ),
        (
            "adapter_revision",
            envelope.adapter_revision,
            descriptor.adapter_revision,
            AdapterErrorCode.MANIFEST_MISMATCH,
        ),
    )
    for field, actual, expected, code in comparisons:
        if actual != expected:
            _deny(
                code,
                ErrorPhase.ENVELOPE_VALIDATION,
                "envelope field does not match the static capability contract",
                field,
            )
    if envelope.environment not in descriptor.supported_environments:
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "environment is not declared by the static adapter descriptor",
            "environment",
        )
    if envelope.credential_profile_match_count == 0:
        _deny(
            AdapterErrorCode.MISSING_CREDENTIAL_MATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "zero credential-profile matches deny",
            "credential_profile_match_count",
        )
    if envelope.credential_profile_match_count != 1:
        _deny(
            AdapterErrorCode.AMBIGUOUS_CREDENTIAL_MATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "multiple credential-profile matches deny",
            "credential_profile_match_count",
        )
    dimensions = _validate_contract_scope_dimensions(
        capability.contract_scope_dimensions,
        ErrorPhase.ENVELOPE_VALIDATION,
    )
    manifest_applicability = _validate_scope_applicability(
        dimensions,
        capability.scope_applicability,
        ErrorPhase.ENVELOPE_VALIDATION,
    )
    envelope_applicability = _validate_scope_applicability(
        dimensions,
        envelope.scope_applicability,
        ErrorPhase.ENVELOPE_VALIDATION,
    )
    if envelope_applicability != manifest_applicability:
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "envelope applicability differs from the immutable manifest",
            "scope_applicability",
        )
    if not isinstance(envelope.scope_references, tuple):
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "scope references must be an immutable tuple",
            "scope_references",
        )
    references: Dict[Tuple[ScopeFamily, str], str] = {}
    for reference in envelope.scope_references:
        key = _scope_key(reference)
        if key not in manifest_applicability:
            _deny(
                AdapterErrorCode.UNKNOWN_SCOPE_DIMENSION,
                ErrorPhase.ENVELOPE_VALIDATION,
                "resolved scope contains an undeclared dimension",
                "scope_references",
            )
        if key in references:
            _deny(
                AdapterErrorCode.MANIFEST_MISMATCH,
                ErrorPhase.ENVELOPE_VALIDATION,
                "resolved scope dimension is duplicated",
                "scope_references",
            )
        references[key] = _require_opaque_reference(
            reference.value_ref,
            "scope_references",
            ErrorPhase.ENVELOPE_VALIDATION,
        )
    for key, entry in manifest_applicability.items():
        if entry.applicability is ScopeApplicability.REQUIRED and key not in references:
            _deny(
                AdapterErrorCode.MISSING_REQUIRED_SCOPE,
                ErrorPhase.ENVELOPE_VALIDATION,
                "required scope reference is missing",
                "scope_references",
            )
        if (
            entry.applicability is ScopeApplicability.NOT_APPLICABLE
            and key in references
        ):
            _deny(
                AdapterErrorCode.UNEXPECTED_SCOPE_FOR_NOT_APPLICABLE,
                ErrorPhase.ENVELOPE_VALIDATION,
                "scope value was supplied for a not-applicable dimension",
                "scope_references",
            )
    expected_external = (
        capability.external_content_exposure is ExternalContentExposure.UNTRUSTED
    )
    if envelope.external_content is not expected_external:
        _deny(
            AdapterErrorCode.EXTERNAL_CONTENT_VALIDATION_FAILED,
            ErrorPhase.ENVELOPE_VALIDATION,
            "external-content marker does not match the capability contract",
            "external_content",
        )
    _validate_fact_statuses(envelope)
    _validate_envelope_references(envelope)
    if capability.audit_required and envelope.audit_intent_ref is None:
        _deny(
            AdapterErrorCode.MANIFEST_MISMATCH,
            ErrorPhase.ENVELOPE_VALIDATION,
            "audit-required capability must carry an opaque audit-intent reference",
            "audit_intent_ref",
        )
