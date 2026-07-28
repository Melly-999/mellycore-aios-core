"""The single source of truth for whether a live OpenAI connection is allowed.

This module exists so exactly one place in the whole package decides that
question. Every other module -- the CLI, the provider adapter -- must call
:func:`enforce_live_connection_allowed` before doing anything that would
reach a network client, and must not implement its own bypass.

Canonical state: migration trigger #5 ("first live provider connection", see
``shared_context/PROJECT_STATE.md``'s "Mandatory, blocking migration
triggers") is currently blocking. :func:`get_active_policy` therefore always
returns a policy with ``allowed=False``.

There is deliberately no parameter, environment variable, or configuration
file this module reads to decide that answer -- :func:`get_active_policy`
takes no arguments and consults nothing external. The only way to change the
outcome is to edit the hardcoded policy below in a future, separately
authorized task, after Model B reconsideration
(``MELLYCORE-MODEL-B-LIVE-PROVIDER-TRIGGER-5-DECISION-002``, outcome
``APPROVE_CONSTRAINED_MODEL_B_TRIGGER_5_TRANSITION_002`` --
``STAGE_B_IMPLEMENTATION_AUTHORIZED`` only; ``STAGE_C_LIVE_BATCH_SMOKE_NOT_AUTHORIZED``
and ``MIGRATION_TRIGGER_5_NOT_YET_CROSSED`` both remain true). See
``scripts/mellycore_batch/activation.py`` for the Stage B activation-control
layer this decision authorized; it does not itself flip this policy. CLI flags and
environment variables such as ``--execute``, ``OPENAI_API_KEY``, and
``MELLYCORE_ALLOW_LIVE_BATCH`` are never read by this module and cannot
influence its answer.
"""

from __future__ import annotations

import os

from .models import (
    MIGRATION_TRIGGER_5_ID,
    MIGRATION_TRIGGER_5_LABEL,
    LiveConnectionBlockedError,
    LiveConnectionPolicy,
)

#: The canonical, hardcoded policy. Not a default that something else can
#: override -- this is the entire policy. Changing this value is itself the
#: only supported "activation" mechanism, and doing so is out of scope for
#: this task by design.
_CANONICAL_POLICY = LiveConnectionPolicy(
    allowed=False,
    reason=MIGRATION_TRIGGER_5_ID,
    blocking_trigger=MIGRATION_TRIGGER_5_LABEL,
)

#: Environment variable names this module explicitly acknowledges exist and
#: explicitly refuses to honor as a bypass. Listed here (not read for a
#: decision) purely so :func:`credential_material_detected` can report,
#: without ever reading their values into a decision path, whether an
#: operator has an API key sitting in their environment.
_OPENAI_API_KEY_ENV_VAR = "OPENAI_API_KEY"


def get_active_policy() -> LiveConnectionPolicy:
    """Return the current, canonical live-connection policy.

    Always returns the same hardcoded, blocking policy. Takes no arguments;
    there is nothing for a caller to pass that would change the result.
    """
    return _CANONICAL_POLICY


def enforce_live_connection_allowed(command: str) -> None:
    """Raise :class:`LiveConnectionBlockedError` unless a live connection is currently allowed.

    ``command`` is used only to make the resulting message specific about
    which CLI command was refused; it has no effect on the decision itself.
    """
    policy = get_active_policy()
    if not policy.allowed:
        raise LiveConnectionBlockedError(
            "{} ({}): command {!r} requires a live provider connection, which is not "
            "authorized while {} is blocking. See "
            "MELLYCORE-MODEL-B-LIVE-PROVIDER-TRIGGER-5-DECISION-002.".format(
                LiveConnectionBlockedError.code,
                policy.reason,
                command,
                policy.blocking_trigger,
            )
        )


def credential_material_present() -> bool:
    """Report only whether an OpenAI API key is present in the environment.

    Returns a boolean. Never reads, returns, logs, or otherwise exposes the
    value itself, anywhere -- including in exceptions, JSON output, or CLI
    text. This function exists solely so ``plan-live`` can honestly report
    "credentials detected: yes/no" without revealing what they are, and its
    result never participates in the allow/block decision above.
    """
    return bool(os.environ.get(_OPENAI_API_KEY_ENV_VAR))
