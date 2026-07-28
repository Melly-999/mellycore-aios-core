"""Tests for Batch request validation.

Every rejection case must raise :class:`InvalidInputError` without silently
rewriting the offending request.
"""

from __future__ import annotations

import unittest

from scripts.mellycore_batch.models import BatchRequest, InvalidInputError
from scripts.mellycore_batch.validation import validate_request, validate_requests


def _req(custom_id="req-1", method="POST", url="/v1/responses", body=None):
    if body is None:
        body = {"model": "gpt-test", "input": "hello"}
    return BatchRequest(custom_id=custom_id, method=method, url=url, body=body)


class ValidRequestTests(unittest.TestCase):
    def test_valid_request_passes(self) -> None:
        validate_request(_req())  # must not raise

    def test_valid_collection_passes(self) -> None:
        validate_requests([_req("a"), _req("b")])


class RejectionTests(unittest.TestCase):
    def test_empty_custom_id_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(custom_id=""))

    def test_whitespace_only_custom_id_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(custom_id="   "))

    def test_duplicate_custom_id_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_requests([_req("dup"), _req("dup")])

    def test_unsupported_method_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(method="GET"))

    def test_unsupported_endpoint_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(url="/v1/chat/completions"))

    def test_empty_body_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={}))

    def test_missing_model_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={"input": "hi"}))

    def test_empty_input_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={"model": "m", "input": ""}))

    def test_stream_true_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={"model": "m", "input": "hi", "stream": True}))

    def test_authorization_header_field_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(
                _req(body={"model": "m", "input": "hi", "headers": {"Authorization": "Bearer x"}})
            )

    def test_api_key_field_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={"model": "m", "input": "hi", "api_key": "sk-fake"}))

    def test_bearer_token_field_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={"model": "m", "input": "hi", "bearer": "token-value"}))

    def test_nested_secret_field_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(
                _req(body={"model": "m", "input": "hi", "extra": {"nested": {"secret": "x"}}})
            )

    def test_external_url_in_body_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(
                _req(body={"model": "m", "input": "hi", "webhook": "https://evil.example.com/callback"})
            )

    def test_non_serializable_body_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_request(_req(body={"model": "m", "input": "hi", "bad": object()}))

    def test_empty_collection_rejected(self) -> None:
        with self.assertRaises(InvalidInputError):
            validate_requests([])

    def test_rejection_does_not_mutate_request(self) -> None:
        request = _req(body={"model": "m", "input": "hi", "api_key": "sk-fake"})
        original_body = dict(request.body)
        with self.assertRaises(InvalidInputError):
            validate_request(request)
        self.assertEqual(original_body, request.body)


if __name__ == "__main__":
    unittest.main()
