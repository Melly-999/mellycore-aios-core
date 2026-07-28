"""MellyCore local OpenAI Batch API foundation.

Standard library only, Python 3.9 compatible. This package builds, validates,
and inspects OpenAI Batch API JSONL payloads entirely locally. It also defines
a provider adapter boundary for a future, separately authorized live
connection.

Canonical safety boundary: migration trigger #5 ("first live provider
connection") is currently blocking. Every command that would reach a real
provider is hard-refused by :mod:`scripts.mellycore_batch.policy` before any
network client is constructed, regardless of CLI flags or environment
variables. See ``shared_context/PROJECT_STATE.md`` for the canonical trigger
list and ``shared_context/SAFETY_CONTRACT.md`` for the Model A contract this
package operates under.
"""

from __future__ import annotations
