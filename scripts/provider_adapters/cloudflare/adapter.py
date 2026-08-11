"""Concrete Cloudflare semantics with permanently disabled execution."""

from __future__ import annotations

from typing import Tuple, final

from ..adapters import DisabledProviderAdapter
from ..contracts import (
    AdapterErrorCode,
    AdapterValidationError,
    AuthorizationFactStatus,
    ErrorPhase,
    NormalizedAdapterError,
    ResolvedExecutionEnvelope,
)
from .contracts import CloudflareReadOperationPlan
from .manifest import (
    CLOUDFLARE_DELEGATED_READ_MANIFEST,
    CLOUDFLARE_DELEGATED_READ_PLANS,
    CLOUDFLARE_PROVIDER_DESCRIPTOR,
    CLOUDFLARE_SERVICE_READ_MANIFEST,
    CLOUDFLARE_SERVICE_READ_PLANS,
)


def _require_runtime_enablement_evidence(
    envelope: ResolvedExecutionEnvelope,
) -> None:
    if (
        envelope.authorization_facts.runtime_enabled
        is AuthorizationFactStatus.SATISFIED
        and envelope.runtime_enablement_ref is None
    ):
        raise AdapterValidationError(
            NormalizedAdapterError(
                code=AdapterErrorCode.MANIFEST_MISMATCH,
                phase=ErrorPhase.ENVELOPE_VALIDATION,
                message=(
                    "Cloudflare fact 7 requires an explicit runtime record; "
                    "validation never infers it"
                ),
                field="runtime_enablement_ref",
                provider_request_occurred=False,
            )
        )


@final
class CloudflareDelegatedReadAdapter(DisabledProviderAdapter):
    """Fixed delegated manifest; it exposes no transport or extension hook."""

    def __init__(self) -> None:
        super().__init__(
            CLOUDFLARE_PROVIDER_DESCRIPTOR,
            CLOUDFLARE_DELEGATED_READ_MANIFEST,
        )

    def __init_subclass__(cls, **kwargs: object) -> None:
        raise TypeError("Cloudflare delegated adapter is final")

    def validate(self, envelope: ResolvedExecutionEnvelope) -> None:
        super().validate(envelope)
        _require_runtime_enablement_evidence(envelope)

    @property
    def operation_plans(self) -> Tuple[CloudflareReadOperationPlan, ...]:
        """Return immutable non-executable read-operation metadata."""

        return CLOUDFLARE_DELEGATED_READ_PLANS


@final
class CloudflareServiceReadAdapter(DisabledProviderAdapter):
    """Fixed service manifest; it exposes no transport or extension hook."""

    def __init__(self) -> None:
        super().__init__(
            CLOUDFLARE_PROVIDER_DESCRIPTOR,
            CLOUDFLARE_SERVICE_READ_MANIFEST,
        )

    def __init_subclass__(cls, **kwargs: object) -> None:
        raise TypeError("Cloudflare service adapter is final")

    def validate(self, envelope: ResolvedExecutionEnvelope) -> None:
        super().validate(envelope)
        _require_runtime_enablement_evidence(envelope)

    @property
    def operation_plans(self) -> Tuple[CloudflareReadOperationPlan, ...]:
        """Return immutable non-executable read-operation metadata."""

        return CLOUDFLARE_SERVICE_READ_PLANS
