"""Provider-neutral adapter protocol and deterministic disabled adapter.

The interface intentionally has no transport construction, credential
resolution, provider registration, dynamic discovery, or generic request
method.  ``execute`` exists only to fail closed for repository-native protocol
compatibility.
"""

from __future__ import annotations

from typing import Protocol, Tuple, runtime_checkable

from .contracts import (
    AdapterErrorCode,
    CapabilityDescriptor,
    ErrorPhase,
    ExecutionState,
    NormalizedAdapterError,
    NormalizedOperationResult,
    OperationOutcome,
    ProviderDescriptor,
    ResolvedExecutionEnvelope,
)
from .validation import public_reference, validate_envelope, validate_manifest


@runtime_checkable
class ProviderAdapter(Protocol):
    """Small static adapter boundary; conformance grants no runtime authority."""

    @property
    def descriptor(self) -> ProviderDescriptor:
        """Return immutable static adapter metadata."""
        ...

    @property
    def capability_manifest(self) -> Tuple[CapabilityDescriptor, ...]:
        """Return the immutable static capability manifest."""
        ...

    @property
    def execution_state(self) -> ExecutionState:
        """Return the adapter's explicit execution state."""
        ...

    def validate(self, envelope: ResolvedExecutionEnvelope) -> None:
        """Validate an already resolved envelope without authorizing it."""
        ...

    def execute(
        self, envelope: ResolvedExecutionEnvelope
    ) -> NormalizedOperationResult:
        """Return a deterministic disabled result and perform no I/O."""
        ...


class DisabledProviderAdapter:
    """Reference adapter that validates static metadata and never executes."""

    def __init__(
        self,
        descriptor: ProviderDescriptor,
        capability_manifest: Tuple[CapabilityDescriptor, ...],
    ) -> None:
        validate_manifest(descriptor, capability_manifest)
        self._descriptor = descriptor
        self._capability_manifest = capability_manifest

    @property
    def descriptor(self) -> ProviderDescriptor:
        return self._descriptor

    @property
    def capability_manifest(self) -> Tuple[CapabilityDescriptor, ...]:
        return self._capability_manifest

    @property
    def execution_state(self) -> ExecutionState:
        return ExecutionState.DISABLED

    def validate(self, envelope: ResolvedExecutionEnvelope) -> None:
        validate_envelope(self.descriptor, self.capability_manifest, envelope)

    def execute(
        self, envelope: ResolvedExecutionEnvelope
    ) -> NormalizedOperationResult:
        """Fail closed without validating secrets, resolving state, or doing I/O."""

        error = NormalizedAdapterError(
            code=AdapterErrorCode.EXECUTION_DISABLED,
            phase=ErrorPhase.EXECUTION,
            message="provider adapter execution is disabled by construction",
            field=None,
            provider_request_occurred=False,
        )
        return NormalizedOperationResult(
            request_id=public_reference(envelope.request_id),
            provider_id=envelope.provider_id,
            capability_id=envelope.capability_id,
            outcome=OperationOutcome.EXECUTION_DISABLED,
            fixture_only=False,
            provider_request_id=None,
            provider_authenticated=False,
            provider_mutation_completed=False,
            payload=(),
            error=error,
            provenance=(("source", "disabled-scaffold"),),
        )
