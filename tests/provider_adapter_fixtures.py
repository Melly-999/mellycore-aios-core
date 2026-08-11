"""In-memory fixtures for the inert provider-adapter scaffold tests."""

from __future__ import annotations

import re
from typing import Any, Optional, Tuple

from scripts.provider_adapters import (
    ActingIdentityType,
    AdapterErrorCode,
    AdapterKind,
    ApprovalRequirement,
    AuthenticationTarget,
    AuthorizationFacts,
    AuthorizationFactStatus,
    CapabilityClassification,
    CapabilityDescriptor,
    CapabilityId,
    ContractScopeDimension,
    CredentialProfileClass,
    CredentialSupport,
    DisabledProviderAdapter,
    ErrorPhase,
    ExecutionState,
    ExternalContentExposure,
    ImplementationState,
    NetworkBehavior,
    NormalizedAdapterError,
    NormalizedOperationResult,
    OperationOutcome,
    ProviderDescriptor,
    ProviderId,
    ResolvedExecutionEnvelope,
    RiskTier,
    ScopeApplicability,
    ScopeApplicabilityEntry,
    ScopeFamily,
    ScopeReference,
)


_SENSITIVE_FIXTURE_TEXT = re.compile(
    r"(?i)(?:bearer\s+|sk-[a-z0-9_-]{12,}|api[_-]?key\s*[:=]|client[_-]?secret)"
)


def fixture_descriptor() -> ProviderDescriptor:
    return ProviderDescriptor(
        provider_id=ProviderId("fixture_provider"),
        display_name="Fixture Provider (not registered)",
        provider_family="fixture",
        contract_ref="fixture-provider-contract",
        contract_revision="fixture-revision-1",
        adapter_kind=AdapterKind.SCAFFOLD,
        supported_environments=("fixture",),
        capability_manifest_revision="fixture-manifest-1",
        adapter_revision="fixture-adapter-1",
        implementation_state=ImplementationState.SCAFFOLD_ONLY,
        network_behavior=NetworkBehavior.DISABLED,
        credential_support=CredentialSupport.UNSUPPORTED,
        execution_state=ExecutionState.DISABLED,
    )


def _mellycore_dimensions() -> Tuple[ContractScopeDimension, ...]:
    return tuple(
        ContractScopeDimension(
            family=ScopeFamily.MELLYCORE,
            name=name,
            optional_absence_permitted=False,
            not_applicable_permitted=False,
        )
        for name in (
            "tenant",
            "capability",
            "acting_identity",
            "environment",
            "runtime_state",
        )
    )


def _provider_dimensions() -> Tuple[ContractScopeDimension, ...]:
    return tuple(
        ContractScopeDimension(
            family=ScopeFamily.PROVIDER_NATIVE,
            name=name,
            optional_absence_permitted=False,
            not_applicable_permitted=True,
        )
        for name in ("account", "zone", "resource")
    )


def _restricted_dimensions() -> Tuple[ContractScopeDimension, ...]:
    return tuple(
        ContractScopeDimension(
            family=ScopeFamily.RESTRICTED_TOOL,
            name=name,
            optional_absence_permitted=False,
            not_applicable_permitted=True,
        )
        for name in (
            "restricted_tool_id",
            "tool_contract_revision",
            "tool_capability",
            "operator",
            "tenant",
            "environment",
            "allowed_resource_class",
        )
    )


def fixture_scope_dimensions() -> Tuple[ContractScopeDimension, ...]:
    return _mellycore_dimensions() + _provider_dimensions() + _restricted_dimensions()


def _applicability(
    family: ScopeFamily,
    names: Tuple[str, ...],
    value: ScopeApplicability,
) -> Tuple[ScopeApplicabilityEntry, ...]:
    return tuple(
        ScopeApplicabilityEntry(family=family, name=name, applicability=value)
        for name in names
    )


def restricted_capability() -> CapabilityDescriptor:
    scope = (
        _applicability(
            ScopeFamily.MELLYCORE,
            ("tenant", "capability", "acting_identity", "environment", "runtime_state"),
            ScopeApplicability.REQUIRED,
        )
        + _applicability(
            ScopeFamily.PROVIDER_NATIVE,
            ("account", "zone", "resource"),
            ScopeApplicability.NOT_APPLICABLE,
        )
        + _applicability(
            ScopeFamily.RESTRICTED_TOOL,
            (
                "restricted_tool_id",
                "tool_contract_revision",
                "tool_capability",
                "operator",
                "tenant",
                "environment",
                "allowed_resource_class",
            ),
            ScopeApplicability.REQUIRED,
        )
    )
    return CapabilityDescriptor(
        provider_id=ProviderId("fixture_provider"),
        capability_id=CapabilityId("fixture_provider.documentation.inspect"),
        capability_version="fixture-capability-1",
        provider_contract_ref="fixture-provider-contract",
        provider_contract_revision="fixture-revision-1",
        provider_native_capability_ref="fixture-native-docs-inspect",
        risk_tier=RiskTier.R0,
        required_credential_profile_class=(
            CredentialProfileClass.RESTRICTED_OPERATOR_INVESTIGATION
        ),
        required_acting_identity_type=ActingIdentityType.MELLYCORE_OPERATOR,
        required_authentication_target=AuthenticationTarget.RESTRICTED_TOOL,
        contract_scope_dimensions=fixture_scope_dimensions(),
        scope_applicability=scope,
        data_sensitivity_ref="fixture-public-docs",
        external_content_exposure=ExternalContentExposure.UNTRUSTED,
        classification=CapabilityClassification.INVESTIGATION,
        verification_required=False,
        approval_requirement=ApprovalRequirement.NOT_REQUIRED,
        audit_required=True,
    )


def api_capability(
    credential_class: CredentialProfileClass,
    identity: ActingIdentityType,
    target: AuthenticationTarget = AuthenticationTarget.PROVIDER_ACCOUNT,
) -> CapabilityDescriptor:
    scope = (
        _applicability(
            ScopeFamily.MELLYCORE,
            ("tenant", "capability", "acting_identity", "environment", "runtime_state"),
            ScopeApplicability.REQUIRED,
        )
        + _applicability(
            ScopeFamily.PROVIDER_NATIVE,
            ("account", "zone", "resource"),
            ScopeApplicability.REQUIRED,
        )
        + _applicability(
            ScopeFamily.RESTRICTED_TOOL,
            (
                "restricted_tool_id",
                "tool_contract_revision",
                "tool_capability",
                "operator",
                "tenant",
                "environment",
                "allowed_resource_class",
            ),
            ScopeApplicability.NOT_APPLICABLE,
        )
    )
    return CapabilityDescriptor(
        provider_id=ProviderId("fixture_provider"),
        capability_id=CapabilityId("fixture_provider.inventory.read"),
        capability_version="fixture-capability-1",
        provider_contract_ref="fixture-provider-contract",
        provider_contract_revision="fixture-revision-1",
        provider_native_capability_ref="fixture-native-inventory-read",
        risk_tier=RiskTier.R1,
        required_credential_profile_class=credential_class,
        required_acting_identity_type=identity,
        required_authentication_target=target,
        contract_scope_dimensions=fixture_scope_dimensions(),
        scope_applicability=scope,
        data_sensitivity_ref="fixture-sensitive-read",
        external_content_exposure=ExternalContentExposure.NONE,
        classification=CapabilityClassification.READ,
        verification_required=False,
        approval_requirement=ApprovalRequirement.NOT_REQUIRED,
        audit_required=True,
    )


def fixture_facts() -> AuthorizationFacts:
    return AuthorizationFacts(
        provider_registered=AuthorizationFactStatus.UNSATISFIED,
        adapter_implemented=AuthorizationFactStatus.UNSATISFIED,
        credential_configured=AuthorizationFactStatus.UNSATISFIED,
        credential_verified=AuthorizationFactStatus.UNSATISFIED,
        tenant_authorized=AuthorizationFactStatus.UNSATISFIED,
        capability_authorized=AuthorizationFactStatus.UNSATISFIED,
        runtime_enabled=AuthorizationFactStatus.UNSATISFIED,
        operation_approved=AuthorizationFactStatus.NOT_REQUIRED,
    )


def _required_scope_references(
    capability: CapabilityDescriptor,
) -> Tuple[ScopeReference, ...]:
    references = []
    for entry in capability.scope_applicability:
        if entry.applicability is ScopeApplicability.REQUIRED:
            references.append(
                ScopeReference(
                    family=entry.family,
                    name=entry.name,
                    value_ref="ref-{}-{}".format(entry.family.value, entry.name),
                )
            )
    return tuple(references)


def fixture_envelope(
    capability: Optional[CapabilityDescriptor] = None,
) -> ResolvedExecutionEnvelope:
    if capability is None:
        capability = restricted_capability()
    return ResolvedExecutionEnvelope(
        request_id="fixture-request-1",
        request_fingerprint="fixture-fingerprint-1",
        tenant_ref="fixture-tenant-1",
        provider_id=capability.provider_id,
        capability_id=capability.capability_id,
        capability_version=capability.capability_version,
        environment="fixture",
        acting_identity_type=capability.required_acting_identity_type,
        acting_identity_ref="fixture-actor-1",
        credential_profile_class=capability.required_credential_profile_class,
        credential_profile_ref="fixture-profile-1",
        credential_profile_match_count=1,
        authentication_target=capability.required_authentication_target,
        scope_applicability=capability.scope_applicability,
        scope_references=_required_scope_references(capability),
        risk_tier=capability.risk_tier,
        provider_contract_revision=capability.provider_contract_revision,
        adapter_revision="fixture-adapter-1",
        authorization_record_refs=(),
        runtime_enablement_ref=None,
        approval_ref=None,
        audit_intent_ref="fixture-audit-intent-1",
        external_content=(
            capability.external_content_exposure
            is ExternalContentExposure.UNTRUSTED
        ),
        correlation_ref="fixture-correlation-1",
        authorization_facts=fixture_facts(),
    )


class FixtureProviderAdapter(DisabledProviderAdapter):
    """Test-only, in-memory normalizer that cannot claim provider success."""

    _ALLOWED_KEYS = {"summary", "item_count", "source_note"}

    def normalize_fixture(
        self,
        envelope: ResolvedExecutionEnvelope,
        payload: Tuple[Tuple[str, Any], ...],
    ) -> NormalizedOperationResult:
        self.validate(envelope)
        if not isinstance(payload, tuple):
            raise ValueError("fixture payload must be an immutable tuple")
        for key, value in payload:
            if key not in self._ALLOWED_KEYS:
                raise ValueError("fixture payload field is not allowlisted")
            if not isinstance(value, (str, int, bool, type(None))):
                raise ValueError("fixture payload value must be scalar")
            if isinstance(value, str) and _SENSITIVE_FIXTURE_TEXT.search(value):
                raise ValueError("fixture payload contains sensitive-shaped text")
        error = NormalizedAdapterError(
            code=AdapterErrorCode.FIXTURE_ONLY_OPERATION,
            phase=ErrorPhase.EXECUTION,
            message="normalized result is fixture-only; no provider request occurred",
            field=None,
            provider_request_occurred=False,
        )
        return NormalizedOperationResult(
            request_id=envelope.request_id,
            provider_id=envelope.provider_id,
            capability_id=envelope.capability_id,
            outcome=OperationOutcome.FIXTURE_ONLY,
            fixture_only=True,
            provider_request_id=None,
            provider_authenticated=False,
            provider_mutation_completed=False,
            payload=payload,
            error=error,
            provenance=(("source", "in-memory-fixture"),),
        )
