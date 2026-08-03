# MellyCore Cloudflare API Shield Read-Only Adapter Review 002

## 1. Title and status

- Task: `MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002`
- Status: `PASS_WITH_NON_BLOCKING_FINDINGS`
- Severity counts: P0 = 0, P1 = 0, P2 = 2, P3 = 1.
- Review date: 2026-08-03.

## 2. Purpose

Independently determine whether remediation commit
`1a9acd2f1ad7b4597bce795d5d626424f34466e2` closes Review 001 findings `P1-01`,
`P2-01`, and `P2-02`, without trusting the remediation report and without
repairing anything.

## 3. Scope

The complete ten-path remediation commit, the five Cloudflare source modules,
the focused Cloudflare test module, the neutral scaffold, the canonical
contracts, Review 001 and its task report, and the remediation report were
reviewed. Only this assurance record, its task report, and bounded
shared-context decision updates are mutable.

## 4. Starting repository state

| Item | Verified value |
| --- | --- |
| Root | `C:/AI/MellyCore_Workspace/01_Repo/mellycore-aios` |
| Branch | `fix/mellycore-cloudflare-api-shield-read-only-adapter-remediation-001` |
| HEAD | `1a9acd2f1ad7b4597bce795d5d626424f34466e2` |
| Parent | `81fbe401ac6b901d7e0bc5c47903be084133de7b` |
| Subject | `fix: bind Cloudflare read authentication modes` |
| Worktree / index | Clean before and after review edits |
| Canonical remote | `clean-origin` -> `https://github.com/Melly-999/mellycore-aios-core.git` |
| Fresh canonical main | `947f33d27d5546775186e96bdc61e30db78c0b3d` |
| Review 002 branches before creation | Local absent; `clean-origin` absent |
| Network | Exactly one authorized `git fetch clean-origin`; no later network |

`clean-origin/main` was re-resolved after the authorized fetch and matched the
expected value exactly, so no canonical-main drift condition applies.

## 5. Reviewed commits

| Commit | Role | Subject |
| --- | --- | --- |
| `3de6a4961a6ba4d20b7bc133298292ff1f0fc71c` | Adapter implementation | `feat: add Cloudflare API Shield read-only adapter` |
| `81fbe401ac6b901d7e0bc5c47903be084133de7b` | Review 001 | `docs: review Cloudflare API Shield read-only adapter` |
| `1a9acd2f1ad7b4597bce795d5d626424f34466e2` | Remediation 001, under review | `fix: bind Cloudflare read authentication modes` |

`git show --name-only` returned exactly ten paths for the remediation commit,
matching the reported set: four Cloudflare modules, one focused test module,
one new task report, and four shared-context files.
`scripts/provider_adapters/cloudflare/adapter.py` was **not** touched.

## 6. Reviewed files

Read completely rather than by hunk:

- `scripts/provider_adapters/cloudflare/__init__.py`
- `scripts/provider_adapters/cloudflare/adapter.py`
- `scripts/provider_adapters/cloudflare/contracts.py`
- `scripts/provider_adapters/cloudflare/manifest.py`
- `scripts/provider_adapters/cloudflare/normalization.py`
- `tests/test_cloudflare_provider_adapter.py`

Also read: the neutral scaffold modules and tests, Review 001 and its task
report, the remediation report, and the four shared-context files.

## 7. Canonical contracts

Authority was taken from the Provider Registry contract extension (§§11–13,
§25, §26), the Cloudflare API Shield connector contract (§8.7, §11.1.1, §11.2),
the Integration Gateway security contract (§14.2), the Cybersecurity Provider
Pack (§12), Scaffold Review 001 (§34), Review 001, `SAFETY_CONTRACT.md`, and
`VALIDATION.md`. The remediation report was evidence to challenge, never
authority.

## 8. Independent method

Exact Git identity and history gates; one freshly fetched canonical ref;
SHA-256 baselines; complete source and test reading; independent reconstruction
of the authentication-mode compatibility rules from the Registry and Cloudflare
contracts; a 58-row classification matrix rebuilt from Review 001's own table
and compared to production data; AST scanning of all five modules; an import
audit hook installed before the package was imported; runtime probes over all
32 concrete descriptors and all 32 operation plans; 15 adversarial tuple
constructions; 5 plan-level mismatch constructions; 4 global-metadata
contradiction constructions; 46 fixture-host inputs; 6 non-string / hostile
host objects; a 17-case scope matrix; execution replay for both variants; and
in-memory simulated-defect injection against the test oracle. All probe code
lived outside the repository and no repository file was mutated to simulate a
defect.

## 9. Immutable baselines

| Reviewed surface | SHA-256 (first 16) | Result |
| --- | --- | --- |
| Cloudflare `__init__.py` | `DA581077DBA60DC3` | Remediation-changed, then immutable |
| Cloudflare `adapter.py` | `F20588039874CA52` | Byte-identical to Review 001 |
| Cloudflare `contracts.py` | `EB0D77269895FDD8` | Remediation-changed, then immutable |
| Cloudflare `manifest.py` | `EB8B7C6F39D937D8` | Remediation-changed, then immutable |
| Cloudflare `normalization.py` | `3A9EDCEFB2C959B0` | Remediation-changed, then immutable |
| Cloudflare focused test | `FEDFFEC128CEC95A` | Remediation-changed, then immutable |
| Generic exports | `8C2336B1363924CC` | Byte-identical to Review 001 |
| Generic adapters | `BE77D7CB1930D382` | Byte-identical to Review 001 |
| Generic contracts | `3044146AA1BD02AA` | Byte-identical to Review 001 |
| Generic validation | `0A9B98FD2E17C6BE` | Byte-identical to Review 001 |
| Generic tests | `6257A59C7178DBB2` | Byte-identical to Review 001 |
| Registry contract | `327D3715C884015F` | Byte-identical to Review 001 |
| Cloudflare contract | `33D3AD42FDB8496B` | Byte-identical to Review 001 |
| Gateway contract | `134AFB244AD3700D` | Byte-identical to Review 001 |
| Cybersecurity pack | `635004BB4AF85F99` | Byte-identical to Review 001 |
| Scaffold Review 001 | `2B56018C972AED02` | Byte-identical to Review 001 |
| Review 001 record | `D5EC81A82973F76F` | Unmodified by remediation |
| Review 001 task report | `03A5E51DACBF7AC1` | Unmodified by remediation |
| Remediation 001 report | `27275B96845802AA` | Unmodified by this review |
| `SAFETY_CONTRACT.md` | `D7AD99EC0335FD7F` | Byte-identical to Review 001 |
| `VALIDATION.md` | `CC89FC215340D69F` | Byte-identical to Review 001 |

The twelve values marked "Byte-identical to Review 001" reproduce Review 001
Section 9 exactly, independently confirming that the remediation altered no
scaffold, contract, or prior-review surface.

Recorded counts: remediation commit paths = 10; authentication-mode enum
members = 2 (`delegated_oauth`, `api_token`); delegated concrete entries = 16;
service concrete entries = 16; total concrete manifest entries = 32; operation
plans = 32; capability-classification rows = 58; independent oracle rows = 58;
focused tests = 60; neutral scaffold tests = 62; full-suite baseline = 696;
public Cloudflare exports = 31; declared entity families = 11.

## 10. Review 001 finding baseline

Reconstructed from the Review 001 record, which owns the definitions:

- **P1-01** — no capability descriptor carried `authentication_mode`; the
  delegated variant therefore lacked the only mode compatible with
  `read_only_delegated`; the sole Cloudflare metadata was an unbound
  `provider_account_modes=("api_token",)` tuple; Scaffold Review 001
  constraint 5 required an explicit `CapabilityDescriptor` extension with
  binding rules; resolution appeared to require architectural interpretation.
- **P2-01** — an endpoint-URL-shaped fixture `host` was accepted verbatim and
  unflagged.
- **P2-02** — focused tests were not an independent contract oracle and omitted
  mandated negative cases, including the authentication conformance case.

## 11. Closure matrix

| Finding | Original contradiction | Remediation source | Contract evidence | Test evidence | Independent probe | Result | Gate impact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `P1-01` | No concrete mode field; delegated entries incompatible with `read_only_delegated`; unbound global `api_token` tuple | `contracts.py` adds `CloudflareAuthenticationMode`, `authentication_mode` and `authentication_mode_treatment` on `CloudflareCapabilityDescriptor`, `__post_init__` closure on descriptor, plan and metadata; `manifest.py` `_identity_binding` constructs one mode per variant and copies it into every plan; `provider_account_modes` removed | Registry §13.2 permits `read_only_delegated` only with `delegated_oauth`; §13.2 plus Registry §26.1 and Cloudflare §11.2 rule 8 leave scoped `api_token` as the only permitted service mode for Cloudflare; Gateway §14.2 requires a pinned mode the Gateway never chooses; Scaffold Review 001 constraint 5 satisfied by an explicit `CapabilityDescriptor` extension with binding rules | 6 dedicated tests: exact per-variant binding, mismatch/unknown/alias/case/whitespace/missing denial, global-metadata contradiction denial, operator-identity denial, plan preservation and immutability, metadata cannot enable execution | All 32 entries yield exactly one tuple per variant; 15 adversarial descriptor constructions, 5 plan constructions and 4 metadata constructions all deny; enum has 2 members, no `_missing_`, no coercion; descriptor and plan modes agree for all 32 | `CLOSED` | Non-blocking |
| `P2-01` | Endpoint URL accepted verbatim as `host` | `normalization.py` `_SYNTHETIC_HOST_PATTERN` plus `_require_synthetic_host` full-match gate | Contract requires fixture-only, non-executable, non-live-claiming synthetic evidence; no endpoint may be representable | 3 dedicated tests covering 11 rejected shapes with non-echo assertions plus the accepted synthetic case | 46 host inputs: every scheme, path, query, fragment, user-info, slash, backslash, port, whitespace, control, uppercase, empty label, leading/trailing hyphen, repeated dot, Unicode confusable, overlong total, overlong label, real TLD, `localhost` and IP literal deny; no denial echoed its input | `CLOSED` | Non-blocking |
| `P2-02` | Tests derived expectations from the implementation and omitted mandated negatives | `tests/test_cloudflare_provider_adapter.py` adds `EXPECTED_CLOUDFLARE_CONTRACT`, a literal 58-row dict of plain string tuples, plus 18 new tests | Cloudflare contract §13's 58 accepted capabilities and their domains and risk tiers | Focused tests grew 42 -> 60; full-equality assertion against the oracle; manifest IDs compared to the oracle's included set | Oracle is a distinct object from production data (`is` comparison false), holds only plain string tuples, and is not produced by calling classification functions; in-memory injection of a missing, extra, renamed, recategorized and risk-drifted capability each caused test failures | `CLOSED` | Non-blocking |

No finding is classified as partially closed. All three closures rest on direct
independent evidence, not on remediation prose.

## 12. Authentication-mode vocabulary

`CloudflareAuthenticationMode` is a closed `str, Enum` with exactly two
members: `DELEGATED_OAUTH = "delegated_oauth"` and `API_TOKEN = "api_token"`.
Verified independently:

- No third member, no alias, no deprecated spelling.
- No `_missing_` hook, so unknown values raise rather than resolve.
- No case normalization: `"DELEGATED_OAUTH"` and `"Delegated_OAuth"` raise.
- No whitespace normalization: `" delegated_oauth"` and `"delegated_oauth "`
  raise.
- Raw strings are never coerced where an enum is required: every binding check
  uses `is` identity against enum members, so even the exact string
  `"delegated_oauth"` is denied in a descriptor or plan.
- Serialization is deterministic via the fixed `.value`, and storage is on
  frozen dataclasses.

Canonical contract evidence for the two required bindings:

- `read_only_delegated` -> `delegated_oauth`: Registry §13.2 lists exactly one
  permitted mode for this class. There is no second candidate, so the value is
  determined by the closed table rather than chosen.
- `read_only_service` -> `api_token`: Registry §13.2 permits one of four
  service modes generally. Registry §26.1 narrows the Cloudflare provider API
  to scoped `api_token`, Cloudflare §8.7 describes only scoped API-token
  permission groups, and Cloudflare §11.2 rule 8 prohibits the Global API Key.
  `service_account_oauth`, `scoped_personal_token` and `workload_identity` have
  no Cloudflare-track authority, so `api_token` is uniquely determined. The
  contracts therefore do not leave the service mode ambiguous for this provider.

## 13. Delegated binding review

All 16 delegated concrete entries collapse to exactly one distinct tuple:

`('delegated', 'delegated_user', 'read_only_delegated', 'provider_account',
'delegated_oauth')`

This matches Cloudflare §11.1.1's concrete-registration rule, which selects
`read_only_delegated` from `CF_READ` when `required_acting_identity_type` is
`delegated_user`, and matches Registry §13.2's single permitted mode and
`provider_account` target for that class.

## 14. Service binding review

All 16 service concrete entries collapse to exactly one distinct tuple:

`('service', 'service_account', 'read_only_service', 'provider_account',
'api_token')`

This matches Cloudflare §11.1.1's `service_account` selection and the
Cloudflare-narrowed service mode established in Section 12.

## 15. Concrete tuple review

Every one of the 32 entries carries exactly one mode; no entry carries a list,
a default, or an absent value. `CloudflareCapabilityDescriptor.__post_init__`
admits only the two tuples above and raises a fixed sanitized `ValueError`
otherwise. `CloudflareReadOperationPlan.__post_init__` applies the equivalent
closure over the plan's own class, identity, target and mode. The mode is
copied from the descriptor into the plan by `_operation_plans`, and an
independent cross-check confirmed the descriptor and plan modes agree for all
32 plan references, so descriptor and plan cannot disagree.

Adversarial results — every case denied deterministically before a manifest
could exist:

| # | Case | Result |
| --- | --- | --- |
| 1 | Delegated class with `api_token` | Denied |
| 2 | Service class with `delegated_oauth` | Denied |
| 3 | Delegated identity with service class | Denied |
| 4 | Service identity with delegated class | Denied |
| 5 | Operator identity with either mode | Denied (both variants) |
| 6 | Restricted-investigation class with either mode | Denied |
| 7 | Missing mode (`None`) | Denied |
| 8 | Unknown mode string | Denied |
| 9 | Uppercase mode string | Denied |
| 10 | Whitespace-padded mode string | Denied |
| 11 | Raw exact string replacing the enum | Denied |
| 12 | Mode alias (`"oauth"`) | Denied |
| 13 | Plan mode, class, identity, target or raw-string mismatch | Denied (5 of 5) |
| 14 | Global metadata contradicting a concrete mode | Denied (4 of 4) |

No runtime resolver, selector, fallback, or "best available mode" path exists.
`CloudflareDelegatedReadAdapter` and `CloudflareServiceReadAdapter` expose no
`select_identity` or `select_credential` member and each returns its own fixed
manifest object.

## 16. Global metadata review

The ambiguous `provider_account_modes=("api_token",)` tuple is gone; a
repository-wide search finds it only in Review 001, the remediation report, and
one test asserting its absence. Its replacement,
`CloudflareAuthenticationModeMetadata`, is a frozen record with
`delegated_mode`, `service_mode`, `runtime_selectable=False`,
`credential_resolution_supported=False`, and a `binding_authority` pointing at
the Cloudflare contract reference. Attempting to construct it with a swapped
delegated mode, a swapped service mode, `runtime_selectable=True`, or
`credential_resolution_supported=True` raises. Because the manifests and plans
are frozen at module construction, the metadata record cannot override an
already-bound concrete tuple; this was confirmed by re-reading all 16 delegated
modes after the metadata probes.

## 17. Authentication non-execution review

AST inspection of all five Cloudflare modules found zero prohibited import or
call nodes. No OAuth flow, authorization-URL construction, token exchange,
refresh-token handling, API-token value, header construction, credential
lookup, environment access, secret storage, transport selection, or provider
authentication state exists. The literals `Authorization` and `client_secret`
appear only inside `normalization._SENSITIVE_KEYS`, that is, as denial
patterns, never as header or credential construction. Every capability entry
carries `authentication_mode_treatment =
"non-runtime-contract-metadata-only"`. Authentication mode remains descriptive
contract metadata only.

## 18. Fixture-host grammar review

The grammar was reconstructed independently from
`_SYNTHETIC_HOST_PATTERN` and `_require_synthetic_host`, which applies
`fullmatch`:

- A length lookahead admits 1–253 characters and, because `.` excludes
  newlines, rejects any embedded newline.
- One or more dot-terminated labels, each `[a-z0-9]` optionally followed by up
  to 61 `[a-z0-9-]` characters and a final `[a-z0-9]`, giving a 1–63 character
  label with no leading or trailing hyphen and no empty label.
- A final reserved synthetic TLD from `invalid`, `test`, `example`.
- Lowercase ASCII only; the character class is not Unicode-extended.

Sensitive-pattern screening (`_require_non_sensitive`) runs over the entire
fixture before host validation, so known token shapes are rejected earlier.
Because underscores are not legal label characters, `ghp_`- and
`client_secret`-shaped material cannot form a host at all, and `sk-`-shaped
material is caught by the sensitive-value screen.

## 19. Fixture-host adversarial results

Forty-six host strings plus six non-string or hostile objects were exercised.

Accepted, correctly: `api.example`, `a.test`, `shop.api.invalid`,
`x1.invalid`, `inventory.fixture.invalid`.

Denied, correctly (all with `INVALID_FIXTURE_SHAPE`, or
`SENSITIVE_FIXTURE_VALUE` where a token shape was present):
`http://`, `https://`, `ftp://` and `gopher://` schemes; host with path, query
or fragment; `user@` and `user:pw@` user-info shapes; leading slash; trailing
slash; backslash; `:443` and `:80/x` port suffixes; leading, interior and
trailing whitespace; NUL and newline control characters; uppercase and
mixed-case; empty label; leading hyphen; trailing hyphen; hyphen-led final
label; repeated dots; trailing dot; Cyrillic homoglyph confusables; 300-
character total length; 64-character label; bearer-shaped and `sk-`-shaped
values; bare `invalid`, `test` and `example` with no label; `example.com`;
`localhost`; and `127.0.0.1`.

Non-string inputs: a plain object, an `int`, `None`, a `list` and a `dict` were
each denied by the depth or text gate.

No denial message, code or field echoed the rejected value; this was checked by
substring comparison across every denial. No URL parser is invoked, so no
parsing-time network activity is possible. An accepted host cannot enable
transport, and the operation plans carry no `url`, `headers`, `credential`,
`callback` or `transport` field, so a host never enters an executable endpoint
field.

Recorded observation, not a finding: hostnames whose first label happens to be
a sensitive word, such as `token.invalid` or `authorization.invalid`, are
accepted. They are structurally valid reserved synthetic hostnames, carry no
credential value, and cannot encode a recognised token shape under the label
grammar. Rejecting them would require a semantic word list rather than a
structural gate.

One residual behaviour is recorded as new finding **P2-03** in Section 31: a
`str` subclass passes the host gate and escapes normalization.

## 20. Sensitive error review

`CloudflareNormalizedError` is frozen, carries a typed code, a fixed message, a
bounded field name, and `provider_request_occurred=False`, and its
`__post_init__` refuses to be constructed with a provider-request claim. Every
denial observed in this review used a stable code from `CloudflareErrorCode`
and a fixed message string. No probe error exposed a fixture payload, plan,
envelope, credential-like string, provider code, or communication claim. No
secret material was read or introduced during this review.

## 21. Independent oracle review

`EXPECTED_CLOUDFLARE_CONTRACT` is a module-level literal `dict` of 58 entries
mapping a canonical capability ID to a plain `(domain, risk_tier, category)`
tuple of strings. Verified independently:

- 58 rows; 16 `IN_SCOPE_READ_ONLY` and 42 excluded.
- Category distribution: 16 proposal, 19 mutation, 4 containment, 3
  restricted-tool.
- The oracle object is not the production object (`is` comparison false) and
  holds no enum instances, so no expected value is produced by calling a
  production classification function.
- `test_implementation_matches_independent_contract_oracle` asserts full
  dictionary equality, so a missing, extra, renamed or recategorized row all
  fail rather than merely a count check.
- No circular assertion exists: expected values are literals, actual values are
  read from `CLOUDFLARE_CAPABILITY_CLASSIFICATION`.

Simulated-defect detection, performed with in-memory copies only and with no
repository file mutated: injecting a missing capability, an extra capability, a
renamed capability, a recategorized capability, and a drifted risk tier each
produced test failures. The oracle is a genuine independent contract oracle.

## 22. Review-prescribed test coverage

| Review 001 prescribed probe | Coverage |
| --- | --- |
| Authentication tuple mismatches | Directly tested |
| Missing authentication mode | Directly tested |
| Global metadata contradiction | Directly tested |
| Complete scope combinations | Directly tested |
| Optional scope behaviour | Directly tested |
| Unknown fixture fields | Directly tested |
| Nested sensitive values | Directly tested |
| Endpoint-shaped values | Directly tested |
| Dangerous `__repr__` | Directly tested for a non-string object; the `str`-subclass variant is untested — see **P2-03** |
| Mutable input after normalization | Directly tested |
| Plan immutability | Directly tested |
| Fixture / live distinction | Directly tested |
| Concrete adapter subclass and public boundary | Directly tested |
| All eight facts satisfied | Directly tested |
| Explicit runtime record still unable to execute | Directly tested |

No prescribed probe is missing. The only gap is a narrower variant of an
otherwise-covered case, and independent probing established that its behaviour
remains offline and non-executable, so it is P2 rather than P1.

## 23. Capability-classification regression

The 58-row table published in Review 001 Section 13 was parsed directly from
that record and converted to the current category vocabulary. All 58 rows
matched current production classification exactly, with no symmetric difference
and no differing row. Contract keys remain 58 and unique; `D4-01`, `D4-02` and
`D4-03` remain the only restricted-tool keys. Containment rows still declare
`('service_account',)` and D4 rows still declare `('mellycore_operator',)`. The
16 included capabilities remain the D1 R0/R1 reads with `operation_kind` of
`read`; the 42 exclusions remain 16 proposal, 19 mutation, 4 containment and 3
restricted-tool. No event-verification capability was introduced. No
classification regression exists.

## 24. Manifest and plan regression

Each identity variant still yields 16 concrete entries and 16 plans, for 32 and
32. Manifest IDs equal the oracle's included set for both variants, with no
extras. Both manifests pass generic `validate_manifest`. Plans remain frozen,
uniquely referenced, and free of transport fields, and `cursor_execution_supported`
remains false for all 32. Public Cloudflare exports rose from 30 to 31, the
single addition being the `CloudflareAuthenticationMode` enum required by the
remediation; declared entity families remain 11.

## 25. Scope regression

A 17-case scope matrix was replayed. Fifteen cases denied fail-closed and two
were accepted, matching Review 001's result exactly:

- Accepted: the complete required-scope baseline, and supplying an optional
  `zone` on an account-scoped row, which Registry §11 explicitly permits as
  narrowing and which grants no zone authority.
- Denied: missing required `tenant`, `environment`, `account`, `zone` and
  `resource` (`MISSING_REQUIRED_SCOPE`); unpermitted `not_applicable` for
  `account`, `zone` and `resource` (`MANIFEST_MISMATCH`); a restricted-tool
  scope value (`SENSITIVE_VALUE_REJECTED`); an unknown dimension
  (`UNKNOWN_SCOPE_DIMENSION`); omitted applicability
  (`MISSING_SCOPE_APPLICABILITY`); applicability copied from another
  capability (`MANIFEST_MISMATCH`); empty and whitespace-only value references
  (`SENSITIVE_VALUE_REJECTED`); and a duplicated `account` dimension
  (`MANIFEST_MISMATCH`).

No missing scope became `not_applicable` and no unexpected value was ignored.

## 26. Fixture normalization regression

The normalizer still requires immutable tuple pairs, a closed top-level and
item schema, the synthetic source marker, the fixture-only marker, a
`fixture-` observation prefix, bounded depth, item count and text length, and
one of two allow-listed operation-inventory capabilities. Duplicate and
conflicting identifiers, unknown and missing fields, mutable inputs, sensitive
and mutation-shaped fields, excessive nesting, live-looking timestamps, and
unsupported capabilities all still deny. Bidi and control characters are still
replaced and flagged, and injection-shaped text is preserved as data with
`injection_suspected` set. Results remain deterministic and structurally
incapable of claiming a provider request, authentication, or success. The
`path`, `operation_method` and `description` fields are rebuilt as plain
strings by `_normalize_untrusted_text`.

## 27. Execution-disabled regression

`OperationOutcome` contains only `VALIDATION_DENIED`, `EXECUTION_DISABLED` and
`FIXTURE_ONLY`; no success member exists. Replay over both variants with all
eight facts false, all eight facts true, an explicit runtime-enablement record
present, correct and incorrect authentication modes, a valid envelope, a
malformed envelope, and fixture-normalized input produced `EXECUTION_DISABLED`
in every executable case, and an `AttributeError` before any provider concept
for the malformed envelope. Satisfying fact 7 without an explicit
`runtime_enablement_ref` denies at validation for both variants, and `execute`
still returns `EXECUTION_DISABLED` afterwards. Runtime subclassing of both
concrete classes raises `TypeError`. The public surface is limited to
`capability_manifest`, `descriptor`, `execute`, `execution_state`,
`operation_plans` and `validate`; no `run`, `invoke`, `call`, `dispatch`,
`request`, `send`, `connect`, `apply`, `mutate`, `fetch`, `authenticate` or
`resolve_credential` member exists. Authentication metadata satisfies and
infers no authorization fact.

## 28. Network, environment, and secret review

AST inspection of all five modules found no import of `socket`, `ssl`, `http`,
`urllib`, `requests`, `httpx`, `aiohttp`, `subprocess`, `os`, a Cloudflare SDK,
`dotenv`, `importlib`, `ctypes` or `asyncio`, and no `__import__`, `eval`,
`exec`, `compile` or `open` call node. An audit hook installed before import
recorded no socket, subprocess, network or environment event; the only
non-`scripts` modules pulled in were `__future__`, `hashlib` with its
accelerators, and `typing`. Importing the package performs no network, DNS,
filesystem write, environment read, subprocess, or provider access. No
`os.environ`, `os.getenv`, `.env`, token exchange, authorization-header
construction, endpoint literal, or filesystem credential load exists. No secret
material is present or introduced.

## 29. Generic scaffold immutability

`scripts/provider_adapters/__init__.py`, `adapters.py`, `contracts.py`,
`validation.py` and `tests/test_provider_adapters.py` are byte-identical
between `81fbe401…` and the reviewed HEAD, and their SHA-256 values reproduce
Review 001's recorded baselines. `scripts/provider_adapters/cloudflare/adapter.py`
is likewise unchanged. The remediation required no neutral public-contract or
execution-envelope change.

## 30. Canonical-contract immutability

The Registry contract extension, Cloudflare connector contract, Integration
Gateway security contract, Cybersecurity Provider Pack, Scaffold Review 001,
Review 001 and its task report, `SAFETY_CONTRACT.md` and `VALIDATION.md` are
byte-identical across the implementation, review and remediation commits, and
their hashes reproduce Review 001's baselines. The remediation report is
unmodified by this review.

## 31. New findings

### P0 — Critical

None.

### P1 — Blocking

None.

### P2 — Material, non-blocking

**P2-03 — a `str` subclass escapes fixture normalization and can forge
`state_digest`.** `_require_depth`, `_require_non_sensitive`, `_require_text`,
`_require_reference` and `_require_synthetic_host` all gate on
`isinstance(value, str)` and return the original object, so a `str` subclass
passes every check and is stored verbatim in `host`, `canonical_ref` and
`provider_native_ref`. `_state_digest` then computes `repr()` over the item
tuple, which invokes the caller-supplied `__repr__`. An independent probe
constructed a subclass whose `__repr__` returns `'api.example'` while the value
is `other.example`, and obtained a **digest collision**: two materially
different fixtures produced identical `state_digest` values. The subclass also
survives into `to_dict()`, where a downstream consumer would see its
`__str__`/`__repr__` rather than the normalized value. The existing dangerous-
`__repr__` test covers only a non-string object, which is correctly denied.
Impact is bounded: no provider execution, network, credential, transport, or
success path is reachable, every structural case remains fail-closed, and
fixtures are synthetic and constructed in-process. This affects evidence
fidelity, not offline adapter safety, so it is P2. It should be closed before
any renderer, evidence-store, or live-response work consumes `state_digest` or
normalized string fields.

**P2-04 — the Cloudflare provider record does not enumerate `delegated_oauth`
as an offered provider-API mode.** Registry §26.1 records Cloudflare
`supported_auth_modes` as, for the provider API, scoped `api_token` with the
Global API Key prohibited; the string `delegated_oauth` appears nowhere in the
Cloudflare connector contract. The concrete delegated binding is nonetheless
correct and forced: Registry §13.2 permits `read_only_delegated` only with
`delegated_oauth`, and Cloudflare §11.1.1 explicitly authorizes selecting
`read_only_delegated` for a `delegated_user` identity, so no interpretation was
needed to derive the value. What remains open is a specification-level question
about whether Cloudflare offers a delegated OAuth path for its provider API at
all. That question belongs to provider-record registration and credential-
profile creation, both of which are explicitly not performed here:
`provider_registration_state` is `not_registered`, `credential_support` is
`unsupported`, `network_behavior` and `execution_state` are `disabled`, and
Registry §25.1 rule 4's fail-closed conflict rule is satisfied structurally
because no capability can execute. It therefore does not block this gate, but
it must be resolved before any Cloudflare provider record, credential profile,
or live read is created.

### P3 — Editorial or maintainability

**P3-01 — `_require_reference` reports structurally malformed references as
sensitive.** A reference that merely fails `_OPAQUE_REFERENCE_PATTERN` — for
example one that is too short, or contains an uppercase letter — is denied with
`CloudflareErrorCode.SENSITIVE_FIXTURE_VALUE` and the message "fixture
reference must be opaque and non-sensitive". The denial itself is correct and
fail-closed, and no input is echoed, but the code conflates a shape violation
with a sensitivity violation and could mislead a triager or inflate a
sensitive-value metric. Runtime and security behaviour are unaffected.

## 32. Finding counts

| Severity | Count |
| --- | --- |
| P0 | 0 |
| P1 | 0 |
| P2 | 2 |
| P3 | 1 |

## 33. Gate decision

`PASS_WITH_NON_BLOCKING_FINDINGS`. P0 and P1 are both zero; `P1-01`, `P2-01`
and `P2-02` are each independently verified `CLOSED`; all authentication-mode
bindings are deterministic and fail-closed; fixture-host validation is
fail-closed; the contract oracle is genuinely independent; no provider
execution, network, credential, OAuth flow, MCP, webhook, mutation, or
live-success path exists; and all 58 capability classifications remain correct.
The two new P2 findings and one P3 finding concern evidence fidelity,
specification-level provider-record representability, and error-code precision;
none affects deterministic offline adapter safety, and none is a prerequisite
for Agent Runtime architecture work.

## 34. Provider-foundation checkpoint

The offline Cloudflare adapter checkpoint is accepted and the provider-
foundation checkpoint is completed for the current milestone, under the
explicit constraints that P2-03 must be closed before `state_digest` or
normalized string fields are consumed downstream, that P2-04 must be resolved
before any Cloudflare provider record or credential profile is created, and
that P3-01 remains an open maintainability item.

## 35. Agent Runtime eligibility

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001` becomes **eligible for separate
authorization**. It is not started, not authorized, not approved, not active,
and not implemented. Its architecture does not depend on any unresolved
Cloudflare provider behaviour, because the adapter exposes no runtime,
transport, credential, or authentication path.

## 36. Live Cloudflare status

Live Cloudflare transport, credentials, authentication, OAuth, token creation,
MCP connection, webhook, provider API access including read-only calls,
mutation, containment, provider registration, runtime enablement, and
deployment all remain **blocked and unauthorized**. This review authorizes none
of them.

## 37. Exact next task

`MELLYCORE-AGENT-RUNTIME-ARCHITECTURE-SPEC-001`

Status: eligible for separate authorization.

## 38. Explicit non-authorizations

This review authorizes no implementation, source or test repair, provider
access, credential, secret, `.env`, OAuth execution, MCP or integration-fabric
connection, webhook, mutation, containment, dependency installation, workflow
change, deployment, push, PR, merge, remote branch, or MellyTrade interaction.
No finding was repaired here. The pre-existing global higher-priority pointer
`MELLYCORE-OPENAI-BATCH-LIVE-SMOKE-AUTHORIZATION-001` remains unchanged, is not
reordered or reinterpreted, and retains its independent priority and meaning.

## 39. Validation evidence

| Command | Result |
| --- | --- |
| `py -3.9 -m unittest tests.test_cloudflare_provider_adapter -v` | 60 tests, `OK` |
| `py -3.9 -m unittest tests.test_provider_adapters -v` | 62 tests, `OK` |
| `py -3.9 -m unittest discover -s tests -p 'test_*.py'` | 696 tests, `OK` |
| `py -3.9 -m compileall -q scripts/provider_adapters tests` | Exit 0 |
| `py -3.9 scripts/validate_project_state.py` | `PASS`, exit 0 |
| `git diff --check` | Exit 0 |
| Black / flake8 / mypy | `NOT_AVAILABLE`; not installed, not claimed passing |

Independent probes recorded: 2 authentication-mode vocabulary sweeps, 32
descriptor tuple reads, 32 plan reads, 15 adversarial descriptor
constructions, 5 plan constructions, 4 metadata constructions, 46 fixture-host
strings, 6 hostile host objects, 17 scope cases, 12 execution replays, 5
simulated oracle defects, 1 AST sweep over five modules, and 1 import audit
hook. All probe files live outside the repository and none was left behind.

Before commit: exactly the six approved paths differ; adapter source, adapter
tests, generic scaffold, canonical contracts, and prior reviews remain
byte-identical; all three Review 001 findings appear in the closure matrix with
direct evidence; the decision matches the finding counts; and no secret
material is introduced.

## 40. Amendment and supersession

Only a later assurance record that names this review and independently
verifies the work may close `P2-03`, `P2-04`, or `P3-01`, or reopen any closure
recorded here. Assertion in an implementation or remediation report is
insufficient.

## 41. References

- `docs/research/MELLYCORE_CLOUDFLARE_API_SHIELD_READ_ONLY_ADAPTER_REVIEW_001.md`
- `docs/tasks/MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-001.md`
- `docs/tasks/MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REMEDIATION-001.md`
- `docs/tasks/MELLYCORE-CLOUDFLARE-API-SHIELD-READ-ONLY-ADAPTER-REVIEW-002.md`
- `docs/research/MELLYCORE_PROVIDER_ADAPTER_SCAFFOLD_REVIEW_001.md`
- `docs/specs/MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001.md`
- `docs/specs/MELLYCORE_CLOUDFLARE_API_SHIELD_CONNECTOR_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001.md`
- `docs/specs/MELLYCORE_CYBERSECURITY_PROVIDER_PACK_SPEC_001.md`
- `shared_context/SAFETY_CONTRACT.md`
- `shared_context/VALIDATION.md`
