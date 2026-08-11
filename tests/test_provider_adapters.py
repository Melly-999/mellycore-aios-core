"""Contract and fail-closed tests for the provider-adapter scaffold."""

from __future__ import annotations

import dataclasses
import os
import socket
import unittest
from dataclasses import replace
from pathlib import Path
from unittest import mock

from scripts.provider_adapters import (
    ActingIdentityType,
    AdapterErrorCode,
    AdapterValidationError,
    AuthenticationTarget,
    AuthorizationFacts,
    AuthorizationFactStatus,
    CapabilityClassification,
    CapabilityId,
    CredentialProfileClass,
    DisabledProviderAdapter,
    ErrorPhase,
    ExecutionState,
    OperationOutcome,
    ProviderAdapter,
    ProviderId,
    RiskTier,
    ScopeApplicability,
    ScopeFamily,
    ScopeReference,
    parse_canonical_value,
    validate_envelope,
    validate_manifest,
)
from tests.provider_adapter_fixtures import (
    FixtureProviderAdapter,
    api_capability,
    fixture_descriptor,
    fixture_envelope,
    fixture_facts,
    restricted_capability,
)


class AdapterContractTestCase(unittest.TestCase):
    def assert_denied(self, code, action):
        with self.assertRaises(AdapterValidationError) as caught:
            action()
        self.assertEqual(code, caught.exception.error.code)
        self.assertFalse(caught.exception.error.provider_request_occurred)
        return caught.exception.error


class CanonicalVocabularyTests(AdapterContractTestCase):
    def test_all_nine_credential_classes_are_exact(self) -> None:
        expected = (
            "read_only_delegated",
            "read_only_service",
            "controlled_write",
            "event_verification",
            "integration_fabric_read",
            "integration_fabric_controlled_write",
            "emergency_containment",
            "reporting_only",
            "restricted_operator_investigation",
        )
        self.assertEqual(expected, tuple(item.value for item in CredentialProfileClass))
        for value in expected:
            self.assertIsInstance(
                parse_canonical_value(CredentialProfileClass, value, "credential"),
                CredentialProfileClass,
            )

    def test_unknown_credential_class_is_rejected(self) -> None:
        self.assert_denied(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            lambda: parse_canonical_value(
                CredentialProfileClass, "provider_read_alias", "credential"
            ),
        )

    def test_all_three_acting_identities_are_exact(self) -> None:
        expected = ("delegated_user", "service_account", "mellycore_operator")
        self.assertEqual(expected, tuple(item.value for item in ActingIdentityType))
        for value in expected:
            self.assertEqual(value, ActingIdentityType(value).value)

    def test_unknown_acting_identity_is_rejected(self) -> None:
        self.assert_denied(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            lambda: parse_canonical_value(
                ActingIdentityType, "administrator", "identity"
            ),
        )

    def test_all_three_authentication_targets_are_exact(self) -> None:
        expected = ("provider_account", "restricted_tool", "integration_fabric")
        self.assertEqual(expected, tuple(item.value for item in AuthenticationTarget))

    def test_unknown_authentication_target_is_rejected(self) -> None:
        self.assert_denied(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            lambda: parse_canonical_value(
                AuthenticationTarget, "provider_default", "target"
            ),
        )

    def test_all_three_scope_applicability_values_are_exact(self) -> None:
        expected = ("required", "optional", "not_applicable")
        self.assertEqual(expected, tuple(item.value for item in ScopeApplicability))

    def test_unknown_scope_applicability_is_rejected(self) -> None:
        self.assert_denied(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            lambda: parse_canonical_value(
                ScopeApplicability, "missing_means_na", "scope"
            ),
        )

    def test_all_six_risk_tiers_are_exact(self) -> None:
        self.assertEqual(
            ("R0", "R1", "R2", "R3", "R4", "R5"),
            tuple(item.value for item in RiskTier),
        )

    def test_unknown_risk_tier_is_rejected(self) -> None:
        self.assert_denied(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            lambda: parse_canonical_value(RiskTier, "unknown", "risk_tier"),
        )


class ProviderAndCapabilityIdentityTests(AdapterContractTestCase):
    def test_valid_canonical_provider_id_is_accepted(self) -> None:
        self.assertEqual("cloudflare", ProviderId("cloudflare").value)
        self.assertEqual("fixture_provider", ProviderId("fixture_provider").value)

    def test_dotted_and_malformed_provider_ids_are_rejected(self) -> None:
        for value in ("cloudflare.application", "Cloudflare", "_provider", ""):
            self.assert_denied(
                AdapterErrorCode.INVALID_PROVIDER_ID,
                lambda candidate=value: ProviderId(candidate),
            )

    def test_provider_prefixed_capability_id_is_accepted(self) -> None:
        capability = CapabilityId("fixture_provider.inventory.read")
        self.assertEqual("fixture_provider.inventory.read", capability.value)

    def test_duplicate_capability_ids_are_rejected(self) -> None:
        capability = restricted_capability()
        self.assert_denied(
            AdapterErrorCode.DUPLICATE_CAPABILITY_ID,
            lambda: validate_manifest(
                fixture_descriptor(), (capability, capability)
            ),
        )

    def test_unknown_capability_is_rejected_without_redirect(self) -> None:
        capability = restricted_capability()
        envelope = replace(
            fixture_envelope(capability),
            capability_id=CapabilityId("fixture_provider.unknown.read"),
        )
        self.assert_denied(
            AdapterErrorCode.UNKNOWN_CAPABILITY,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_missing_provider_contract_revision_is_rejected(self) -> None:
        capability = replace(restricted_capability(), provider_contract_revision="")
        self.assert_denied(
            AdapterErrorCode.MISSING_CONTRACT_REVISION,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_provider_local_credential_label_is_not_a_runtime_class(self) -> None:
        capability = replace(
            restricted_capability(),
            required_credential_profile_class="fixture_read_label",
        )
        self.assert_denied(
            AdapterErrorCode.INVALID_CANONICAL_VALUE,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_provider_id_alias_or_fuzzy_match_is_not_accepted(self) -> None:
        capability = replace(
            restricted_capability(), provider_id=ProviderId("fixture_provider_alt")
        )
        self.assert_denied(
            AdapterErrorCode.MANIFEST_MISMATCH,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_static_descriptor_has_no_hidden_selection_defaults(self) -> None:
        selection_fields = {
            "provider_id",
            "adapter_kind",
            "implementation_state",
            "network_behavior",
            "credential_support",
            "execution_state",
        }
        fields = {item.name: item for item in dataclasses.fields(fixture_descriptor())}
        for name in selection_fields:
            self.assertIs(dataclasses.MISSING, fields[name].default)
            self.assertIs(dataclasses.MISSING, fields[name].default_factory)


class ScopeValidationTests(AdapterContractTestCase):
    def test_complete_restricted_scope_fixture_validates(self) -> None:
        capability = restricted_capability()
        validate_envelope(
            fixture_descriptor(), (capability,), fixture_envelope(capability)
        )

    def test_missing_required_scope_is_rejected(self) -> None:
        capability = restricted_capability()
        envelope = fixture_envelope(capability)
        envelope = replace(envelope, scope_references=envelope.scope_references[1:])
        self.assert_denied(
            AdapterErrorCode.MISSING_REQUIRED_SCOPE,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_optional_missing_scope_requires_explicit_contract_permission(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_DELEGATED,
            ActingIdentityType.DELEGATED_USER,
        )
        dimensions = tuple(
            replace(item, optional_absence_permitted=True)
            if item.family is ScopeFamily.PROVIDER_NATIVE and item.name == "account"
            else item
            for item in capability.contract_scope_dimensions
        )
        applicability = tuple(
            replace(item, applicability=ScopeApplicability.OPTIONAL)
            if item.family is ScopeFamily.PROVIDER_NATIVE and item.name == "account"
            else item
            for item in capability.scope_applicability
        )
        capability = replace(
            capability,
            contract_scope_dimensions=dimensions,
            scope_applicability=applicability,
        )
        envelope = fixture_envelope(capability)
        validate_envelope(fixture_descriptor(), (capability,), envelope)

    def test_optional_scope_without_contract_permission_is_rejected(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_DELEGATED,
            ActingIdentityType.DELEGATED_USER,
        )
        applicability = tuple(
            replace(item, applicability=ScopeApplicability.OPTIONAL)
            if item.family is ScopeFamily.PROVIDER_NATIVE and item.name == "account"
            else item
            for item in capability.scope_applicability
        )
        capability = replace(capability, scope_applicability=applicability)
        self.assert_denied(
            AdapterErrorCode.MANIFEST_MISMATCH,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_value_for_not_applicable_scope_is_rejected(self) -> None:
        capability = restricted_capability()
        envelope = fixture_envelope(capability)
        unexpected = ScopeReference(
            family=ScopeFamily.PROVIDER_NATIVE,
            name="account",
            value_ref="fixture-account-ref",
        )
        envelope = replace(
            envelope, scope_references=envelope.scope_references + (unexpected,)
        )
        self.assert_denied(
            AdapterErrorCode.UNEXPECTED_SCOPE_FOR_NOT_APPLICABLE,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_missing_applicability_declaration_is_rejected(self) -> None:
        capability = restricted_capability()
        capability = replace(
            capability, scope_applicability=capability.scope_applicability[:-1]
        )
        self.assert_denied(
            AdapterErrorCode.MISSING_SCOPE_APPLICABILITY,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_unknown_scope_dimension_fails_closed(self) -> None:
        capability = restricted_capability()
        envelope = fixture_envelope(capability)
        unknown = ScopeReference(
            family=ScopeFamily.PROVIDER_NATIVE,
            name="unknown_dimension",
            value_ref="fixture-unknown-ref",
        )
        envelope = replace(
            envelope, scope_references=envelope.scope_references + (unknown,)
        )
        self.assert_denied(
            AdapterErrorCode.UNKNOWN_SCOPE_DIMENSION,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_restricted_tool_fixture_requires_exact_tool_scope(self) -> None:
        capability = restricted_capability()
        envelope = fixture_envelope(capability)
        references = tuple(
            item
            for item in envelope.scope_references
            if not (
                item.family is ScopeFamily.RESTRICTED_TOOL
                and item.name == "tool_contract_revision"
            )
        )
        envelope = replace(envelope, scope_references=references)
        self.assert_denied(
            AdapterErrorCode.MISSING_REQUIRED_SCOPE,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )


class IdentityCredentialAndTargetTests(AdapterContractTestCase):
    def test_delegated_identity_with_delegated_class_validates(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_DELEGATED,
            ActingIdentityType.DELEGATED_USER,
        )
        validate_manifest(fixture_descriptor(), (capability,))

    def test_delegated_identity_with_service_class_is_rejected(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_SERVICE,
            ActingIdentityType.DELEGATED_USER,
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_ACTING_IDENTITY,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_service_identity_with_service_class_validates(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_SERVICE,
            ActingIdentityType.SERVICE_ACCOUNT,
        )
        validate_manifest(fixture_descriptor(), (capability,))

    def test_service_identity_with_delegated_class_is_rejected(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_DELEGATED,
            ActingIdentityType.SERVICE_ACCOUNT,
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_ACTING_IDENTITY,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_operator_restricted_class_validates_only_as_investigation(self) -> None:
        validate_manifest(fixture_descriptor(), (restricted_capability(),))

    def test_operator_identity_with_provider_account_target_is_rejected(self) -> None:
        capability = replace(
            restricted_capability(),
            required_authentication_target=AuthenticationTarget.PROVIDER_ACCOUNT,
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_AUTHENTICATION_TARGET,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_restricted_class_with_provider_api_classification_is_rejected(self) -> None:
        capability = replace(
            restricted_capability(), classification=CapabilityClassification.READ
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_CREDENTIAL_CLASS,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_provider_class_with_restricted_target_is_rejected(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_SERVICE,
            ActingIdentityType.SERVICE_ACCOUNT,
            AuthenticationTarget.RESTRICTED_TOOL,
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_AUTHENTICATION_TARGET,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_integration_fabric_target_is_never_inferred(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_SERVICE,
            ActingIdentityType.SERVICE_ACCOUNT,
            AuthenticationTarget.INTEGRATION_FABRIC,
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_AUTHENTICATION_TARGET,
            lambda: validate_manifest(fixture_descriptor(), (capability,)),
        )

    def test_zero_credential_matches_deny(self) -> None:
        capability = restricted_capability()
        envelope = replace(
            fixture_envelope(capability), credential_profile_match_count=0
        )
        self.assert_denied(
            AdapterErrorCode.MISSING_CREDENTIAL_MATCH,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_multiple_credential_matches_deny(self) -> None:
        capability = restricted_capability()
        envelope = replace(
            fixture_envelope(capability), credential_profile_match_count=2
        )
        self.assert_denied(
            AdapterErrorCode.AMBIGUOUS_CREDENTIAL_MATCH,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_identity_mismatch_does_not_fallback(self) -> None:
        capability = api_capability(
            CredentialProfileClass.READ_ONLY_DELEGATED,
            ActingIdentityType.DELEGATED_USER,
        )
        envelope = replace(
            fixture_envelope(capability),
            acting_identity_type=ActingIdentityType.SERVICE_ACCOUNT,
        )
        self.assert_denied(
            AdapterErrorCode.INCOMPATIBLE_ACTING_IDENTITY,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )


class AuthorizationFactTests(AdapterContractTestCase):
    def test_eight_facts_are_separate_fields(self) -> None:
        self.assertEqual(8, len(dataclasses.fields(AuthorizationFacts)))
        self.assertEqual(
            {
                "provider_registered",
                "adapter_implemented",
                "credential_configured",
                "credential_verified",
                "tenant_authorized",
                "capability_authorized",
                "runtime_enabled",
                "operation_approved",
            },
            {item.name for item in dataclasses.fields(AuthorizationFacts)},
        )

    def test_setting_seven_facts_does_not_infer_the_eighth(self) -> None:
        facts = fixture_facts()
        seven = replace(
            facts,
            provider_registered=AuthorizationFactStatus.SATISFIED,
            adapter_implemented=AuthorizationFactStatus.SATISFIED,
            credential_configured=AuthorizationFactStatus.SATISFIED,
            credential_verified=AuthorizationFactStatus.SATISFIED,
            tenant_authorized=AuthorizationFactStatus.SATISFIED,
            capability_authorized=AuthorizationFactStatus.SATISFIED,
            runtime_enabled=AuthorizationFactStatus.SATISFIED,
        )
        self.assertIs(
            AuthorizationFactStatus.NOT_REQUIRED, seven.operation_approved
        )

    def test_adapter_implementation_does_not_infer_runtime_enablement(self) -> None:
        facts = replace(
            fixture_facts(),
            adapter_implemented=AuthorizationFactStatus.SATISFIED,
        )
        self.assertIs(
            AuthorizationFactStatus.UNSATISFIED, facts.runtime_enabled
        )

    def test_runtime_enablement_does_not_infer_operation_approval(self) -> None:
        facts = replace(
            fixture_facts(), runtime_enabled=AuthorizationFactStatus.SATISFIED
        )
        self.assertIs(
            AuthorizationFactStatus.NOT_REQUIRED, facts.operation_approved
        )


class DisabledAndFixtureExecutionTests(AdapterContractTestCase):
    def setUp(self) -> None:
        self.capability = restricted_capability()
        self.adapter = DisabledProviderAdapter(
            fixture_descriptor(), (self.capability,)
        )
        self.envelope = fixture_envelope(self.capability)

    def test_disabled_adapter_satisfies_protocol(self) -> None:
        self.assertIsInstance(self.adapter, ProviderAdapter)
        self.assertIs(ExecutionState.DISABLED, self.adapter.execution_state)

    def test_every_execution_attempt_returns_execution_disabled(self) -> None:
        result = self.adapter.execute(self.envelope)
        self.assertIs(OperationOutcome.EXECUTION_DISABLED, result.outcome)
        self.assertIs(AdapterErrorCode.EXECUTION_DISABLED, result.error.code)
        self.assertIs(ErrorPhase.EXECUTION, result.error.phase)

    def test_execution_performs_no_network_call(self) -> None:
        with mock.patch.object(
            socket.socket,
            "connect",
            side_effect=AssertionError("network access attempted"),
        ), mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network access attempted"),
        ):
            result = self.adapter.execute(self.envelope)
        self.assertIs(OperationOutcome.EXECUTION_DISABLED, result.outcome)

    def test_execution_performs_no_environment_access(self) -> None:
        with mock.patch.object(
            os,
            "getenv",
            side_effect=AssertionError("environment access attempted"),
        ):
            result = self.adapter.execute(self.envelope)
        self.assertIs(OperationOutcome.EXECUTION_DISABLED, result.outcome)

    def test_execution_has_no_credential_resolution_surface(self) -> None:
        self.assertFalse(hasattr(self.adapter, "resolve_credentials"))
        self.assertFalse(hasattr(self.adapter, "authenticate"))

    def test_disabled_execution_never_returns_success_state(self) -> None:
        result = self.adapter.execute(self.envelope)
        self.assertNotIn("success", {item.value for item in OperationOutcome})
        self.assertIsNone(result.provider_request_id)
        self.assertFalse(result.provider_authenticated)
        self.assertFalse(result.provider_mutation_completed)

    def test_fixture_result_is_explicitly_fixture_only(self) -> None:
        adapter = FixtureProviderAdapter(
            fixture_descriptor(), (self.capability,)
        )
        result = adapter.normalize_fixture(
            self.envelope,
            (("summary", "bounded fixture data"), ("item_count", 1)),
        )
        self.assertIs(OperationOutcome.FIXTURE_ONLY, result.outcome)
        self.assertTrue(result.fixture_only)
        self.assertIs(AdapterErrorCode.FIXTURE_ONLY_OPERATION, result.error.code)
        self.assertIsNone(result.provider_request_id)

    def test_fixture_adapter_execute_is_still_disabled(self) -> None:
        adapter = FixtureProviderAdapter(
            fixture_descriptor(), (self.capability,)
        )
        result = adapter.execute(self.envelope)
        self.assertIs(OperationOutcome.EXECUTION_DISABLED, result.outcome)

    def test_fixture_normalization_performs_no_network_or_environment_access(self) -> None:
        adapter = FixtureProviderAdapter(
            fixture_descriptor(), (self.capability,)
        )
        with mock.patch.object(
            socket.socket,
            "connect",
            side_effect=AssertionError("network access attempted"),
        ), mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network access attempted"),
        ), mock.patch.object(
            os,
            "getenv",
            side_effect=AssertionError("environment access attempted"),
        ):
            result = adapter.normalize_fixture(
                self.envelope, (("summary", "fixture data"),)
            )
        self.assertIs(OperationOutcome.FIXTURE_ONLY, result.outcome)

    def test_fixture_normalization_rejects_sensitive_shaped_text(self) -> None:
        adapter = FixtureProviderAdapter(
            fixture_descriptor(), (self.capability,)
        )
        sensitive = "{} {}".format("Bear" + "er", "sensitive-material")
        with self.assertRaises(ValueError):
            adapter.normalize_fixture(
                self.envelope, (("summary", sensitive),)
            )

    def test_all_satisfied_fixture_facts_still_cannot_execute(self) -> None:
        facts = AuthorizationFacts(
            provider_registered=AuthorizationFactStatus.SATISFIED,
            adapter_implemented=AuthorizationFactStatus.SATISFIED,
            credential_configured=AuthorizationFactStatus.SATISFIED,
            credential_verified=AuthorizationFactStatus.SATISFIED,
            tenant_authorized=AuthorizationFactStatus.SATISFIED,
            capability_authorized=AuthorizationFactStatus.SATISFIED,
            runtime_enabled=AuthorizationFactStatus.SATISFIED,
            operation_approved=AuthorizationFactStatus.NOT_REQUIRED,
        )
        result = self.adapter.execute(
            replace(self.envelope, authorization_facts=facts)
        )
        self.assertIs(OperationOutcome.EXECUTION_DISABLED, result.outcome)


class ErrorsRedactionAndReviewConstraintTests(AdapterContractTestCase):
    def test_normalized_error_has_stable_code_and_no_provider_request(self) -> None:
        adapter = DisabledProviderAdapter(
            fixture_descriptor(), (restricted_capability(),)
        )
        error = adapter.execute(fixture_envelope()).error.to_dict()
        self.assertEqual("EXECUTION_DISABLED", error["code"])
        self.assertFalse(error["provider_request_occurred"])

    def test_execution_redacts_sensitive_shaped_request_reference(self) -> None:
        sensitive = "{} {}".format("Bear" + "er", "sensitive-material")
        envelope = replace(fixture_envelope(), request_id=sensitive)
        adapter = DisabledProviderAdapter(
            fixture_descriptor(), (restricted_capability(),)
        )
        serialized = str(adapter.execute(envelope).to_dict())
        self.assertNotIn(sensitive, serialized)
        self.assertIn("redacted-", serialized)

    def test_validation_error_never_echoes_sensitive_reference(self) -> None:
        sensitive = "{}-{}".format("s" + "k", "sensitive-placeholder-1234567890")
        capability = restricted_capability()
        envelope = replace(
            fixture_envelope(capability), credential_profile_ref=sensitive
        )
        error = self.assert_denied(
            AdapterErrorCode.SENSITIVE_VALUE_REJECTED,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )
        self.assertNotIn(sensitive, str(error.to_dict()))

    def test_external_content_must_match_manifest_posture(self) -> None:
        capability = restricted_capability()
        envelope = replace(fixture_envelope(capability), external_content=False)
        self.assert_denied(
            AdapterErrorCode.EXTERNAL_CONTENT_VALIDATION_FAILED,
            lambda: validate_envelope(fixture_descriptor(), (capability,), envelope),
        )

    def test_package_does_not_parse_registry_markdown(self) -> None:
        source = self._package_source()
        self.assertNotIn("read_text(", source)
        self.assertNotIn("readlines(", source)
        self.assertNotIn("from pathlib import Path", source)
        self.assertNotIn("open(", source)

    def test_package_uses_no_field_ordinals_or_retired_scope_name(self) -> None:
        source = self._package_source()
        retired_name = "required" + "_provider_scope"
        self.assertNotIn(retired_name, source)
        self.assertNotIn("field 15", source.lower())
        self.assertNotIn("field 20", source.lower())

    def test_restricted_oauth_authority_is_not_selectable_or_enabled(self) -> None:
        source = self._package_source()
        mode_name = "mcp" + "_oauth_grant"
        self.assertNotIn(mode_name, source)
        envelope_fields = {item.name for item in dataclasses.fields(fixture_envelope())}
        self.assertNotIn("authentication_mode", envelope_fields)
        self.assertIs(
            ExecutionState.DISABLED, fixture_descriptor().execution_state
        )

    def test_scaffold_has_no_network_environment_or_sdk_imports(self) -> None:
        source = self._package_source()
        prohibited = (
            "import requests",
            "import httpx",
            "import urllib",
            "import socket",
            "process.env",
            "os.environ",
            "os.getenv",
            "import openai",
            "http://",
            "https://",
        )
        for token in prohibited:
            self.assertNotIn(token, source)

    @staticmethod
    def _package_source() -> str:
        root = Path(__file__).resolve().parents[1] / "scripts" / "provider_adapters"
        return "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(root.glob("*.py"))
        )


if __name__ == "__main__":
    unittest.main()
