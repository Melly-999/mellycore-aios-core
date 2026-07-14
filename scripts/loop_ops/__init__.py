"""MellyCore Loop Operations.

Read-only tooling for defining, inspecting, validating, estimating, and safely
operating recurring MellyCore agent workflows ("loops").

Phase 1 is report-only. Nothing in this package writes to the repository,
pushes, merges, deploys, installs anything, calls a provider API, or reaches the
network. The one exception to "no subprocess" is ``worktrees``, which runs
read-only git inspection commands.

Standard library only. Python 3.9 compatible. No runtime dependencies.

Entry point:
    py -3.9 -m scripts.loop_ops <command>

See ``shared_context/loops/README.md`` for the registry and
``docs/architecture/MELLYCORE_LOOP_OPERATIONS_ARCHITECTURE_001.md`` for design.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "1.0.0"
