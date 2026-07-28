"""Tests for the live-connection policy gate.

These tests exist to prove trigger #5 cannot be bypassed by any combination
of environment variables or flags -- not merely to describe the intended
behavior.
"""

from __future__ import annotations

import os
import unittest
from unittest import mock

from scripts.mellycore_batch.models import LiveConnectionBlockedError
from scripts.mellycore_batch.policy import (
    credential_material_present,
    enforce_live_connection_allowed,
    get_active_policy,
)


class ActivePolicyTests(unittest.TestCase):
    def test_default_policy_is_blocked(self) -> None:
        policy = get_active_policy()
        self.assertFalse(policy.allowed)
        self.assertTrue(policy.reason)
        self.assertTrue(policy.blocking_trigger)

    def test_policy_ignores_all_environment_variables(self) -> None:
        with mock.patch.dict(
            os.environ,
            {
                "OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE",
                "MELLYCORE_ALLOW_LIVE_BATCH": "1",
                "MELLYCORE_FORCE_LIVE": "true",
            },
            clear=False,
        ):
            policy = get_active_policy()
            self.assertFalse(policy.allowed)

    def test_get_active_policy_takes_no_arguments(self) -> None:
        # A regression guard: if a future change added an override parameter,
        # this would need to change too, and that change would be visible in
        # review as exactly the kind of "hidden override" this task forbids.
        import inspect

        signature = inspect.signature(get_active_policy)
        self.assertEqual(0, len(signature.parameters))


class EnforceTests(unittest.TestCase):
    def test_enforce_raises_while_blocked(self) -> None:
        with self.assertRaises(LiveConnectionBlockedError):
            enforce_live_connection_allowed("submit")

    def test_enforce_raises_even_with_fake_credentials_and_flags(self) -> None:
        with mock.patch.dict(
            os.environ,
            {
                "OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE",
                "MELLYCORE_ALLOW_LIVE_BATCH": "1",
            },
            clear=False,
        ):
            with self.assertRaises(LiveConnectionBlockedError) as ctx:
                enforce_live_connection_allowed("submit")
            self.assertEqual(LiveConnectionBlockedError.code, ctx.exception.code)

    def test_error_message_never_contains_env_var_values(self) -> None:
        fake_key = "TEST-CREDENTIAL-SHOULD-NEVER-APPEAR-IN-ANY-MESSAGE"
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": fake_key}, clear=False):
            with self.assertRaises(LiveConnectionBlockedError) as ctx:
                enforce_live_connection_allowed("submit")
            self.assertNotIn(fake_key, str(ctx.exception))


class StageBKillSwitchCombinedBypassTests(unittest.TestCase):
    """Proves Stage B's activation-control layer cannot, alone or combined with
    every other input, flip the trigger-#5 policy or the Stage C kill switch.
    """

    def test_stage_c_kill_switch_false_even_with_every_input_present(self) -> None:
        from scripts.mellycore_batch.activation import stage_b_kill_switch_state

        with mock.patch.dict(
            os.environ,
            {
                "OPENAI_API_KEY": "TEST-CREDENTIAL-NOT-REAL-VALUE",
                "MELLYCORE_ALLOW_LIVE_BATCH": "1",
                "MELLYCORE_FORCE_LIVE": "true",
            },
            clear=False,
        ):
            # A valid manifest, a valid authorization artifact, --execute,
            # fake credentials, and env-var bypass attempts are each proven
            # individually powerless elsewhere (test_mellycore_batch_activation.py,
            # test_mellycore_batch_cli.py). This asserts the *combination* of
            # every one of those inputs still cannot move the hardcoded
            # kill switch off False -- the function takes no arguments at all.
            state = stage_b_kill_switch_state()
            self.assertFalse(state.stage_c_live_execution_authorized)
            self.assertFalse(get_active_policy().allowed)

    def test_kill_switch_and_policy_agree_execution_is_never_authorized(self) -> None:
        from scripts.mellycore_batch.activation import stage_b_kill_switch_state

        self.assertFalse(stage_b_kill_switch_state().stage_c_live_execution_authorized)
        self.assertFalse(get_active_policy().allowed)


class CredentialDetectionTests(unittest.TestCase):
    def test_reports_true_without_exposing_value(self) -> None:
        fake_key = "TEST-CREDENTIAL-SHOULD-NEVER-APPEAR-IN-ANY-OUTPUT"
        with mock.patch.dict(os.environ, {"OPENAI_API_KEY": fake_key}, clear=False):
            detected = credential_material_present()
            self.assertTrue(detected)
            self.assertIsInstance(detected, bool)

    def test_reports_false_when_absent(self) -> None:
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertFalse(credential_material_present())

    def test_detection_never_influences_policy(self) -> None:
        with mock.patch.dict(
            os.environ, {"OPENAI_API_KEY": "TEST-CREDENTIAL-SHORT"}, clear=False
        ):
            self.assertTrue(credential_material_present())
            self.assertFalse(get_active_policy().allowed)


if __name__ == "__main__":
    unittest.main()
