"""Static Cloudflare descriptor, complete classification, and read manifests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from ..contracts import (
    ActingIdentityType,
    AdapterKind,
    ApprovalRequirement,
    AuthenticationTarget,
    CapabilityClassification,
    CapabilityId,
    ContractScopeDimension,
    CredentialProfileClass,
    CredentialSupport,
    ExecutionState,
    ExternalContentExposure,
    ImplementationState,
    NetworkBehavior,
    ProviderId,
    RiskTier,
    ScopeApplicability,
    ScopeApplicabilityEntry,
    ScopeFamily,
)
from .contracts import (
    CloudflareAdapterInclusion,
    CloudflareAuthenticationModeMetadata,
    CloudflareCapabilityClassification,
    CloudflareCapabilityDescriptor,
    CloudflareEntityFamily,
    CloudflareIdentityVariant,
    CloudflareProviderDescriptor,
    CloudflareReadOperationPlan,
    CloudflareSemanticsState,
)

CLOUDFLARE_PROVIDER_ID = ProviderId("cloudflare")
CLOUDFLARE_CONTRACT_REF = "MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_001"
CLOUDFLARE_CONTRACT_REVISION = "1.0"
CLOUDFLARE_ADAPTER_REVISION = "cloudflare-read-only-adapter-1"
CLOUDFLARE_CAPABILITY_VERSION = "1.0"
CLOUDFLARE_MANIFEST_REVISION = "cloudflare-read-only-manifest-1"


CLOUDFLARE_PROVIDER_DESCRIPTOR = CloudflareProviderDescriptor(
    provider_id=CLOUDFLARE_PROVIDER_ID,
    display_name="Cloudflare Application & API Security Provider",
    provider_family="cybersecurity",
    contract_ref=CLOUDFLARE_CONTRACT_REF,
    contract_revision=CLOUDFLARE_CONTRACT_REVISION,
    adapter_kind=AdapterKind.SCAFFOLD,
    supported_environments=("local", "test"),
    capability_manifest_revision=CLOUDFLARE_MANIFEST_REVISION,
    adapter_revision=CLOUDFLARE_ADAPTER_REVISION,
    implementation_state=ImplementationState.SCAFFOLD_ONLY,
    network_behavior=NetworkBehavior.DISABLED,
    credential_support=CredentialSupport.UNSUPPORTED,
    execution_state=ExecutionState.DISABLED,
    provider_semantics_state=CloudflareSemanticsState.CONCRETE_READ_ONLY,
    fixture_normalization_supported=True,
    mutation_supported=False,
    provider_registration_state="not_registered",
)


CLOUDFLARE_AUTHENTICATION_MODE_METADATA = CloudflareAuthenticationModeMetadata(
    provider_account_modes=("api_token",),
    runtime_selectable=False,
    credential_resolution_supported=False,
    binding_authority=CLOUDFLARE_CONTRACT_REF,
)


_MELLYCORE_SCOPE_NAMES = (
    "tenant",
    "capability",
    "acting_identity",
    "environment",
    "runtime_state",
)
_PROVIDER_SCOPE_NAMES = ("account", "zone", "resource")
_RESTRICTED_SCOPE_NAMES = (
    "restricted_tool_id",
    "tool_contract_revision",
    "tool_capability",
    "operator",
    "tenant",
    "environment",
    "allowed_resource_class",
)


def _scope_dimensions() -> Tuple[ContractScopeDimension, ...]:
    mellycore = tuple(
        ContractScopeDimension(
            family=ScopeFamily.MELLYCORE,
            name=name,
            optional_absence_permitted=False,
            not_applicable_permitted=False,
        )
        for name in _MELLYCORE_SCOPE_NAMES
    )
    provider = tuple(
        ContractScopeDimension(
            family=ScopeFamily.PROVIDER_NATIVE,
            name=name,
            optional_absence_permitted=True,
            not_applicable_permitted=False,
        )
        for name in _PROVIDER_SCOPE_NAMES
    )
    restricted = tuple(
        ContractScopeDimension(
            family=ScopeFamily.RESTRICTED_TOOL,
            name=name,
            optional_absence_permitted=False,
            not_applicable_permitted=True,
        )
        for name in _RESTRICTED_SCOPE_NAMES
    )
    return mellycore + provider + restricted


CLOUDFLARE_SCOPE_DIMENSIONS = _scope_dimensions()


def _scope_applicability(
    scope: str, resource_required: bool
) -> Tuple[ScopeApplicabilityEntry, ...]:
    if scope not in {"account", "zone", "account_or_zone"}:
        raise ValueError("unknown static Cloudflare scope")
    mellycore = tuple(
        ScopeApplicabilityEntry(
            family=ScopeFamily.MELLYCORE,
            name=name,
            applicability=ScopeApplicability.REQUIRED,
        )
        for name in _MELLYCORE_SCOPE_NAMES
    )
    provider_values = (
        ("account", ScopeApplicability.REQUIRED),
        (
            "zone",
            (
                ScopeApplicability.REQUIRED
                if scope == "zone"
                else ScopeApplicability.OPTIONAL
            ),
        ),
        (
            "resource",
            (
                ScopeApplicability.REQUIRED
                if resource_required
                else ScopeApplicability.OPTIONAL
            ),
        ),
    )
    provider = tuple(
        ScopeApplicabilityEntry(
            family=ScopeFamily.PROVIDER_NATIVE,
            name=name,
            applicability=applicability,
        )
        for name, applicability in provider_values
    )
    restricted = tuple(
        ScopeApplicabilityEntry(
            family=ScopeFamily.RESTRICTED_TOOL,
            name=name,
            applicability=ScopeApplicability.NOT_APPLICABLE,
        )
        for name in _RESTRICTED_SCOPE_NAMES
    )
    return mellycore + provider + restricted


@dataclass(frozen=True)
class _ReadDefinition:
    contract_key: str
    capability_id: str
    provider_family: str
    scope: str
    entity_family: CloudflareEntityFamily
    risk_tier: RiskTier
    data_sensitivity: str
    pagination_metadata: str
    resource_required: bool


_READ_DEFINITIONS = (
    _ReadDefinition(
        "D1-01",
        "cloudflare.accounts.list",
        "accounts",
        "account",
        CloudflareEntityFamily.ACCOUNT,
        RiskTier.R0,
        "config-metadata",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-02",
        "cloudflare.zones.list",
        "zones",
        "account",
        CloudflareEntityFamily.ZONE,
        RiskTier.R0,
        "config-metadata",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-03",
        "cloudflare.zones.get",
        "zones",
        "zone",
        CloudflareEntityFamily.ZONE,
        RiskTier.R0,
        "config-metadata",
        "not-paginated",
        True,
    ),
    _ReadDefinition(
        "D1-04",
        "cloudflare.endpoint_management.operations.list",
        "endpoint-management",
        "zone",
        CloudflareEntityFamily.API_OPERATION,
        RiskTier.R1,
        "api-surface-topology",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-05",
        "cloudflare.endpoint_management.operations.get",
        "endpoint-management",
        "zone",
        CloudflareEntityFamily.API_OPERATION,
        RiskTier.R1,
        "api-surface-topology",
        "not-paginated",
        True,
    ),
    _ReadDefinition(
        "D1-06",
        "cloudflare.endpoint_labels.list",
        "endpoint-labels",
        "zone",
        CloudflareEntityFamily.ENDPOINT_LABEL,
        RiskTier.R0,
        "config-metadata",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-07",
        "cloudflare.endpoint_labels.get",
        "endpoint-labels",
        "zone",
        CloudflareEntityFamily.ENDPOINT_LABEL,
        RiskTier.R0,
        "config-metadata",
        "not-paginated",
        True,
    ),
    _ReadDefinition(
        "D1-08",
        "cloudflare.schema_validation.schemas.list",
        "schema-validation-2",
        "zone",
        CloudflareEntityFamily.SCHEMA,
        RiskTier.R1,
        "api-surface-topology",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-09",
        "cloudflare.schema_validation.schemas.get",
        "schema-validation-2",
        "zone",
        CloudflareEntityFamily.SCHEMA,
        RiskTier.R1,
        "schema-body-sensitive",
        "not-paginated",
        True,
    ),
    _ReadDefinition(
        "D1-10",
        "cloudflare.schema_validation.settings.get",
        "schema-validation-2",
        "zone",
        CloudflareEntityFamily.SCHEMA_SETTINGS,
        RiskTier.R1,
        "security-posture",
        "not-paginated",
        True,
    ),
    _ReadDefinition(
        "D1-11",
        "cloudflare.schema_validation.operation_settings.list",
        "schema-validation-2",
        "zone",
        CloudflareEntityFamily.OPERATION_SETTINGS,
        RiskTier.R1,
        "security-posture",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-12",
        "cloudflare.authentication_posture.findings.list",
        "authentication-posture",
        "zone",
        CloudflareEntityFamily.AUTHENTICATION_FINDING,
        RiskTier.R1,
        "security-finding",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-13",
        "cloudflare.waf.rulesets.list",
        "rulesets",
        "account_or_zone",
        CloudflareEntityFamily.RULESET,
        RiskTier.R1,
        "security-control-config",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-14",
        "cloudflare.waf.rulesets.get",
        "rulesets",
        "account_or_zone",
        CloudflareEntityFamily.RULESET,
        RiskTier.R1,
        "security-control-config",
        "not-paginated",
        True,
    ),
    _ReadDefinition(
        "D1-15",
        "cloudflare.security_events.search",
        "security-events",
        "zone",
        CloudflareEntityFamily.SECURITY_EVENT,
        RiskTier.R1,
        "security-sensitive-request-data",
        "declared-metadata-only",
        False,
    ),
    _ReadDefinition(
        "D1-16",
        "cloudflare.audit_events.search",
        "audit-events",
        "account",
        CloudflareEntityFamily.AUDIT_EVENT,
        RiskTier.R1,
        "security-sensitive-actor-data",
        "declared-metadata-only",
        False,
    ),
)


_PROPOSAL_IDS = (
    "cloudflare.endpoint_management.operations.add.propose",
    "cloudflare.endpoint_management.operations.delete.propose",
    "cloudflare.endpoint_labels.bindings.diff",
    "cloudflare.schema_validation.schemas.upload.propose",
    "cloudflare.schema_validation.rollout.propose",
    "cloudflare.schema_validation.operation_change.propose",
    "cloudflare.waf.rules.create.propose",
    "cloudflare.waf.rules.update.propose",
    "cloudflare.waf.rules.reorder.propose",
    "cloudflare.waf.rules.delete.propose",
    "cloudflare.api_posture.report",
    "cloudflare.schema_coverage.report",
    "cloudflare.schema_drift.report",
    "cloudflare.unprotected_endpoints.report",
    "cloudflare.shadow_endpoints.report",
    "cloudflare.rate_limiting.propose",
)


_MUTATION_DEFINITIONS = (
    ("D3-01", "cloudflare.endpoint_management.operations.add", "R4", "zone"),
    ("D3-02", "cloudflare.endpoint_management.operations.delete", "R5", "zone"),
    ("D3-03", "cloudflare.endpoint_labels.bindings.replace", "R4", "zone"),
    ("D3-04", "cloudflare.schema_validation.schemas.upload", "R4", "zone"),
    ("D3-05", "cloudflare.schema_validation.schemas.delete", "R5", "zone"),
    ("D3-06", "cloudflare.schema_validation.schemas.enable", "R4", "zone"),
    ("D3-07", "cloudflare.schema_validation.schemas.disable", "R4", "zone"),
    ("D3-08", "cloudflare.schema_validation.zone_default.set_none", "R4", "zone"),
    ("D3-09", "cloudflare.schema_validation.zone_default.set_log", "R4", "zone"),
    ("D3-10", "cloudflare.schema_validation.zone_default.set_block", "R5", "zone"),
    ("D3-12", "cloudflare.schema_validation.operation.set_log", "R4", "zone"),
    ("D3-13", "cloudflare.schema_validation.operation.set_block", "R4", "zone"),
    ("D3-15", "cloudflare.waf.rulesets.create", "R4", "account_or_zone"),
    ("D3-16", "cloudflare.waf.rulesets.update", "R4", "account_or_zone"),
    ("D3-17", "cloudflare.waf.entrypoint.execute_rule.add", "R5", "account_or_zone"),
    ("D3-19", "cloudflare.waf.rules.create", "R4", "account_or_zone"),
    ("D3-20", "cloudflare.waf.rules.update", "R4", "account_or_zone"),
    ("D3-21", "cloudflare.waf.rules.reorder", "R4", "account_or_zone"),
    ("D3-23", "cloudflare.waf.rules.delete", "R5", "account_or_zone"),
)


_CONTAINMENT_DEFINITIONS = (
    ("D3-11", "cloudflare.schema_validation.operation.set_none", "R4", "zone"),
    ("D3-14", "cloudflare.schema_validation.zone_override.set_none", "R4", "zone"),
    ("D3-18", "cloudflare.waf.entrypoint.execute_rule.remove", "R5", "account_or_zone"),
    ("D3-22", "cloudflare.waf.rules.disable", "R4", "account_or_zone"),
)


_RESTRICTED_TOOL_IDS = (
    "cloudflare.docs.search",
    "cloudflare.api_surface.discover",
    "cloudflare.mcp.documentation_session",
)


def _read_classifications() -> Tuple[CloudflareCapabilityClassification, ...]:
    return tuple(
        CloudflareCapabilityClassification(
            contract_key=item.contract_key,
            domain="D1",
            capability_id=CapabilityId(item.capability_id),
            risk_tier=item.risk_tier.value,
            operation_kind="read",
            identity_modes=("delegated_user", "service_account"),
            scope=item.scope,
            verification="read-evidence-only",
            adapter_inclusion=CloudflareAdapterInclusion.IN_SCOPE_READ_ONLY,
        )
        for item in _READ_DEFINITIONS
    )


def _excluded_classifications() -> Tuple[CloudflareCapabilityClassification, ...]:
    proposals = tuple(
        CloudflareCapabilityClassification(
            contract_key="D2-{:02d}".format(index),
            domain="D2",
            capability_id=CapabilityId(capability_id),
            risk_tier="R2",
            operation_kind="proposal",
            identity_modes=("delegated_user", "service_account"),
            scope="provider_native",
            verification="proposal-input-completeness",
            adapter_inclusion=CloudflareAdapterInclusion.OUT_OF_SCOPE_PROPOSAL,
        )
        for index, capability_id in enumerate(_PROPOSAL_IDS, 1)
    )
    mutations = tuple(
        CloudflareCapabilityClassification(
            contract_key=key,
            domain="D3",
            capability_id=CapabilityId(capability_id),
            risk_tier=risk,
            operation_kind="mutation",
            identity_modes=("delegated_user", "service_account"),
            scope=scope,
            verification="read-after-write-required",
            adapter_inclusion=CloudflareAdapterInclusion.OUT_OF_SCOPE_MUTATION,
        )
        for key, capability_id, risk, scope in _MUTATION_DEFINITIONS
    )
    containment = tuple(
        CloudflareCapabilityClassification(
            contract_key=key,
            domain="D3",
            capability_id=CapabilityId(capability_id),
            risk_tier=risk,
            operation_kind="containment",
            identity_modes=("service_account",),
            scope=scope,
            verification="read-after-write-required",
            adapter_inclusion=CloudflareAdapterInclusion.OUT_OF_SCOPE_CONTAINMENT,
        )
        for key, capability_id, risk, scope in _CONTAINMENT_DEFINITIONS
    )
    restricted = tuple(
        CloudflareCapabilityClassification(
            contract_key="D4-{:02d}".format(index),
            domain="D4",
            capability_id=CapabilityId(capability_id),
            risk_tier="R0",
            operation_kind="investigation",
            identity_modes=("mellycore_operator",),
            scope="restricted_tool",
            verification="restricted-tool-contract",
            adapter_inclusion=(CloudflareAdapterInclusion.OUT_OF_SCOPE_RESTRICTED_TOOL),
        )
        for index, capability_id in enumerate(_RESTRICTED_TOOL_IDS, 1)
    )
    return proposals + mutations + containment + restricted


CLOUDFLARE_CAPABILITY_CLASSIFICATION = (
    _read_classifications() + _excluded_classifications()
)


def _identity_binding(
    identity_variant: CloudflareIdentityVariant,
) -> Tuple[CredentialProfileClass, ActingIdentityType]:
    if identity_variant is CloudflareIdentityVariant.DELEGATED:
        return (
            CredentialProfileClass.READ_ONLY_DELEGATED,
            ActingIdentityType.DELEGATED_USER,
        )
    if identity_variant is CloudflareIdentityVariant.SERVICE:
        return (
            CredentialProfileClass.READ_ONLY_SERVICE,
            ActingIdentityType.SERVICE_ACCOUNT,
        )
    raise ValueError("unsupported static Cloudflare identity variant")


def _manifest(
    identity_variant: CloudflareIdentityVariant,
) -> Tuple[CloudflareCapabilityDescriptor, ...]:
    credential_class, identity = _identity_binding(identity_variant)
    return tuple(
        CloudflareCapabilityDescriptor(
            provider_id=CLOUDFLARE_PROVIDER_ID,
            capability_id=CapabilityId(item.capability_id),
            capability_version=CLOUDFLARE_CAPABILITY_VERSION,
            provider_contract_ref=CLOUDFLARE_CONTRACT_REF,
            provider_contract_revision=CLOUDFLARE_CONTRACT_REVISION,
            provider_native_capability_ref="cf-{}".format(item.contract_key.lower()),
            risk_tier=item.risk_tier,
            required_credential_profile_class=credential_class,
            required_acting_identity_type=identity,
            required_authentication_target=AuthenticationTarget.PROVIDER_ACCOUNT,
            contract_scope_dimensions=CLOUDFLARE_SCOPE_DIMENSIONS,
            scope_applicability=_scope_applicability(
                item.scope, item.resource_required
            ),
            data_sensitivity_ref=item.data_sensitivity,
            external_content_exposure=ExternalContentExposure.UNTRUSTED,
            classification=CapabilityClassification.READ,
            verification_required=False,
            approval_requirement=ApprovalRequirement.NOT_REQUIRED,
            audit_required=True,
            identity_variant=identity_variant,
            provider_requirement_label="CF_READ",
            read_operation_plan_ref="cf-plan-{}-{}".format(
                identity_variant.value, item.contract_key.lower()
            ),
            authentication_mode_treatment="non-runtime-contract-metadata-only",
        )
        for item in _READ_DEFINITIONS
    )


CLOUDFLARE_DELEGATED_READ_MANIFEST = _manifest(CloudflareIdentityVariant.DELEGATED)
CLOUDFLARE_SERVICE_READ_MANIFEST = _manifest(CloudflareIdentityVariant.SERVICE)


def _operation_plans(
    manifest: Tuple[CloudflareCapabilityDescriptor, ...],
) -> Tuple[CloudflareReadOperationPlan, ...]:
    definitions = {item.capability_id: item for item in _READ_DEFINITIONS}
    plans = []
    for capability in manifest:
        definition = definitions[capability.capability_id.value]
        required_scope_names = tuple(
            "{}:{}".format(entry.family.value, entry.name)
            for entry in capability.scope_applicability
            if entry.applicability is ScopeApplicability.REQUIRED
        )
        plans.append(
            CloudflareReadOperationPlan(
                plan_ref=capability.read_operation_plan_ref,
                provider_id=CLOUDFLARE_PROVIDER_ID.value,
                capability_id=capability.capability_id,
                provider_native_operation_id=(
                    capability.provider_native_capability_ref
                ),
                declared_resource_class=definition.entity_family,
                required_scope_names=required_scope_names,
                identity_variant=capability.identity_variant,
                credential_profile_class=(
                    capability.required_credential_profile_class.value
                ),
                acting_identity_type=(capability.required_acting_identity_type.value),
                authentication_target=(capability.required_authentication_target.value),
                expected_entity_family=definition.entity_family,
                pagination_metadata=definition.pagination_metadata,
                cursor_execution_supported=False,
                verification_expectation="offline-fixture-shape-only",
                provider_contract_revision=CLOUDFLARE_CONTRACT_REVISION,
                adapter_revision=CLOUDFLARE_ADAPTER_REVISION,
            )
        )
    return tuple(plans)


CLOUDFLARE_DELEGATED_READ_PLANS = _operation_plans(CLOUDFLARE_DELEGATED_READ_MANIFEST)
CLOUDFLARE_SERVICE_READ_PLANS = _operation_plans(CLOUDFLARE_SERVICE_READ_MANIFEST)
