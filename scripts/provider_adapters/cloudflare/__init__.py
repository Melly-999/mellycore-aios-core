"""Cloudflare API Shield read-only adapter surface.

Importing this package performs no I/O and grants no provider authority.
"""

from __future__ import annotations

from .adapter import CloudflareDelegatedReadAdapter, CloudflareServiceReadAdapter
from .contracts import (
    CloudflareAdapterInclusion,
    CloudflareApiOperation,
    CloudflareAuthenticationModeMetadata,
    CloudflareCapabilityClassification,
    CloudflareCapabilityDescriptor,
    CloudflareCompleteness,
    CloudflareEntityFamily,
    CloudflareErrorCode,
    CloudflareFixtureError,
    CloudflareFixtureReadResult,
    CloudflareFixtureTrust,
    CloudflareIdentityVariant,
    CloudflareNormalizedError,
    CloudflareProviderDescriptor,
    CloudflareReadOperationPlan,
    CloudflareSemanticsState,
)
from .manifest import (
    CLOUDFLARE_ADAPTER_REVISION,
    CLOUDFLARE_AUTHENTICATION_MODE_METADATA,
    CLOUDFLARE_CAPABILITY_CLASSIFICATION,
    CLOUDFLARE_CONTRACT_REF,
    CLOUDFLARE_CONTRACT_REVISION,
    CLOUDFLARE_DELEGATED_READ_MANIFEST,
    CLOUDFLARE_DELEGATED_READ_PLANS,
    CLOUDFLARE_PROVIDER_DESCRIPTOR,
    CLOUDFLARE_PROVIDER_ID,
    CLOUDFLARE_SERVICE_READ_MANIFEST,
    CLOUDFLARE_SERVICE_READ_PLANS,
)
from .normalization import normalize_api_operations_fixture

__all__ = [
    "CLOUDFLARE_ADAPTER_REVISION",
    "CLOUDFLARE_AUTHENTICATION_MODE_METADATA",
    "CLOUDFLARE_CAPABILITY_CLASSIFICATION",
    "CLOUDFLARE_CONTRACT_REF",
    "CLOUDFLARE_CONTRACT_REVISION",
    "CLOUDFLARE_DELEGATED_READ_MANIFEST",
    "CLOUDFLARE_DELEGATED_READ_PLANS",
    "CLOUDFLARE_PROVIDER_DESCRIPTOR",
    "CLOUDFLARE_PROVIDER_ID",
    "CLOUDFLARE_SERVICE_READ_MANIFEST",
    "CLOUDFLARE_SERVICE_READ_PLANS",
    "CloudflareAdapterInclusion",
    "CloudflareApiOperation",
    "CloudflareAuthenticationModeMetadata",
    "CloudflareCapabilityClassification",
    "CloudflareCapabilityDescriptor",
    "CloudflareCompleteness",
    "CloudflareDelegatedReadAdapter",
    "CloudflareEntityFamily",
    "CloudflareErrorCode",
    "CloudflareFixtureError",
    "CloudflareFixtureReadResult",
    "CloudflareFixtureTrust",
    "CloudflareIdentityVariant",
    "CloudflareNormalizedError",
    "CloudflareProviderDescriptor",
    "CloudflareReadOperationPlan",
    "CloudflareSemanticsState",
    "CloudflareServiceReadAdapter",
    "normalize_api_operations_fixture",
]
