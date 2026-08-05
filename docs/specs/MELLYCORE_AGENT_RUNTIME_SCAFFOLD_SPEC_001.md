# MellyCore Agent Runtime Scaffold Spec

**Task ID:** MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-001
**Contract ID:** MELLYCORE_AGENT_RUNTIME_SCAFFOLD_001
**Version:** 1.2 — remediation of Review 002 findings. The authoritative version
history is §44.1; `runtime_scaffold_spec_version` is **`1.2`**.
**Amends:** version 1.1, under
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002`, resolving the one P2
and six P3 findings recorded by
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-002`
(`[[../research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_002]]`). Version 1.1
had itself amended version 1.0 under
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001`, resolving all seven P2
and five P3 findings recorded by
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-001`
(`[[../research/MELLYCORE_AGENT_RUNTIME_SCAFFOLD_SPEC_REVIEW_001]]`). Version 1.0
held the pre-review outcome `AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED`; Review
001 then returned `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 7 / P3 5),
and Review 002 returned `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 1 /
P3 6). **All twelve Review 001 closures are preserved by version 1.2.**
**Verification status:** **Version 1.2 is unverified.** Review 002 accepted
version 1.1 as documentation only under nine constraints; this version
remediates the findings recorded against it and **is not accepted** until
`MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003` completes with a passing gate
decision, in the same sequence used for
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`,
`[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]`,
`[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]`, and
`[[MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001]]`.
**Status:** Drafted, specification-level only, pending independent review.
**This status does not authorize:** creation of any Python package, module,
source file, test, fixture, configuration file, or dependency; any Agent Runtime,
Framework Adapter, Shared Context Bridge, package loader, policy engine, or
provider integration; any framework or SDK import, installation, or execution;
any model call, tool execution, MCP connection, command, hook, or plugin
activation; any Batch Orchestration, worktree creation, network operation, Git
mutation, frontend, backend, or deployment. It fixes the contract a later,
separately authorized implementation task must satisfy.
**Scope:** Defines the **Agent Runtime Scaffold** — the structural, inert,
import-safe code boundary that a future authorized implementation task will
create so that the Agent Runtime's contracts become expressible in code
**without acquiring any runtime authority**.

---

## 1. Purpose and scope

### 1.1 The problem this specification solves

**Agent Runtime Architecture §37**
(`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`) already fixes the
**Inert v1 boundary** — what a first Agent Runtime Scaffold may and may not
implement — and §40 item 5 sequences it behind the Agent Package, Framework
Bridge, and Shared Context Bridge contracts plus separate Operator
authorization. Those three contracts are now accepted as documentation, and that
authorization has been given for this specification.

What Agent Runtime Architecture §37 does **not** fix is the *structure*: which
modules exist, where the composition boundary sits, which dependency seams are
injected rather than resolved, what "import-safe" means as a testable property,
which side-effect categories are prohibited, and how a later implementation is
mechanically checked for inertness. Without those, a code task would have to
invent architecture while writing code.

This specification supplies exactly that structural contract, and **nothing
else**. It consumes Agent Runtime Architecture §37 unchanged: where a rule here
expresses one of that section's requirements, it does so as an explicitly cited
**subordinate implementation constraint** and never as an independent normative
source.

**Reference convention (normative).** Throughout this document a reference to
the owner's inert boundary is written in full as **"Agent Runtime Architecture
§37"**. A bare `§37` always denotes **this document's own §37 (Security
considerations)** and never the owner's section.

### 1.2 In scope

The intended repository boundary; the module inventory; the composition root;
import safety and construction safety; the runtime configuration boundary;
dependency injection seams; typed runtime ports; the no-op versus fail-closed
distinction; per-operation scaffold dispositions; the execution boundary;
per-subsystem boundaries; scaffold-level error and result behavior; the
cancellation boundary; inert observability records; library-safe logging; data
records; an ordered scaffold validation model; the inert-mode invariant; the
side-effect inventory; framework identifier handling; the future testing
contract; the static validation strategy; the future repository allowlist;
security considerations; the Batch Orchestration boundary; non-goals; deferred
dependencies; acceptance criteria; document metrics; references; and amendment
rules.

### 1.3 Explicitly out of scope

1. Any scaffold implementation, source file, module, or Python package.
2. Any test, fixture, or `conftest`.
3. Any dependency, packaging, or configuration file change.
4. Agent Runtime implementation (owned by
   `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`, unchanged here).
5. Framework Adapter implementation, SDK installation, or framework execution.
6. Shared Context Bridge implementation, context storage, database, or vector
   store.
7. Agent Package loading, installation, activation, or execution.
8. Command, hook, plugin, skill, or MCP runtime.
9. Provider connection, credential configuration, model call, or network
   operation.
10. Batch Orchestration, worktree creation, or parallel execution.
11. Frontend, backend, or deployment.
12. Any push, pull request, merge, or remote branch operation.
13. Any MellyTrade interaction, trading, broker, or order behavior.

### 1.4 Current implementation state (normative, truthful)

| Dimension | State |
| --- | --- |
| Agent Runtime Scaffold specification | **This document; unverified, not accepted** |
| Agent Runtime Scaffold code | `NOT_IMPLEMENTED` — no module, package, or source file exists |
| Agent Runtime | `NOT_IMPLEMENTED` |
| Framework Adapters (all six) | `NONE_EXIST` |
| Shared Context Bridge | `NOT_IMPLEMENTED` |
| Agent Package loader, Package Validator, Agent Registry | `NOT_IMPLEMENTED` |
| Policy engine, Model Router, provider integration | `NOT_IMPLEMENTED` |
| Runtime ports, composition root, no-op adapters | **Specified only; zero exist** |
| Agents executed, model calls, tool executions | **Zero** |
| Framework SDKs | `NOT_INSTALLED` / `NOT_IMPORTED` / `NOT_EXECUTED` |
| Empirical framework validation | **`NOT_PERFORMED`** — unchanged by this task |
| Evidence class for every future flow below | `future_live` per `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` §8.1 |

No row above may be advanced by this documentation task. A validator that did
not run records `NOT_RUN`, never a defaulted pass.

### 1.5 Relationship to migration triggers

This specification implements nothing, so it crosses no migration trigger in
`shared_context/PROJECT_STATE.md`'s Model A contract. Triggers **#1**, **#4**,
**#5**, **#6**, and **#7** remain uncrossed. A future scaffold implementation
task is inert by construction and, on its own, still crosses none — but any
later task that would make an agent execution-capable requires the Model B
reconsideration of trigger #6 before it may proceed
(`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §40).

## 2. Terminology

Normative definitions. Where a term is already canonically defined elsewhere,
this section cites the owner instead of redefining it.

| Term | Definition |
| --- | --- |
| **Agent Runtime Scaffold** | The future inert, import-safe code boundary specified by this document. It is a structural shell: it expresses contracts as types and seams and holds **no** runtime authority. |
| **Inert Runtime** | The scaffold operating under its default configuration with no externally injected implementations. Per Agent Runtime Architecture §37, its execution outcome set contains **no success member**. |
| **Composition Root** | The single explicit future location where a caller assembles ports into a runtime object graph. Construction is always caller-initiated and never a side effect of import (§7). |
| **Runtime Port** | A typed boundary declaring what the scaffold *would* require from an external capability. A port is a declaration, never an implementation, and never evidence one exists (§12). |
| **Runtime Adapter** | A future implementation of one port, supplied by injection. This document specifies **no** adapter. |
| **Baseline Inert Composition** | A composition using the default inert configuration, with **no live external implementation injected**, and containing only repository-approved inert fixtures or unavailable ports (§31.1). |
| **Baseline Inert Invariant** | The scaffold's primary machine-testable safety property, scoped exactly to a baseline inert composition (§31.1). It makes **no claim** about a composition containing an injected live implementation. |
| **Injected Component Eligibility** | The seven separate validations an externally injected component must pass before it may participate in any future authorized mode (§31.2). Interface conformance alone confers nothing. |
| **Deferred Effect** | Any effect produced after `__init__` — by a lazy or cached property, descriptor, finalizer, default factory, context-manager entry, deferred import, or first-method-call path. Bound by §9.1 exactly as a constructor is. |
| **Baseline Inert Invariant Property Register** | The authoritative, machine-enumerable list of every property the Baseline Inert Invariant asserts (§31.1.1). §34 obligation 18 MUST cover it in full; a proper subset does not satisfy that obligation. |
| **Scaffold Zero-Execution Evidence** | A scaffold-owned, derived, correlation-scoped, explicitly non-canonical audit record (§27.1). It is **affirmative-only**: emitted solely when its evidence scope is complete. It is not a Runtime result, not a status dimension, and not a global guarantee. |
| **`EVIDENCE_INCOMPLETE`** | The distinct, non-affirmative scaffold-domain validation outcome recorded **in place of** Scaffold Zero-Execution Evidence whenever evidence scope is incomplete (§27.1). It is not zero-execution evidence, not a Runtime result, not a Control Plane status, and **not an error class** — §24's taxonomy is unchanged. |
| **No-Op Adapter** | An adapter that deliberately performs nothing for an operation **whose absence does not matter**, and which reports that it did nothing (§13). |
| **Fail-Closed Stub** | An adapter that refuses an operation **whose absence does matter**, returning a determinate refusal with an owner-defined class. Never a silent success (§13). |
| **Runtime Service** | A future scaffold-internal component that composes ports without performing external I/O. |
| **Runtime Record** | An immutable typed value representing owner-defined data. A record is data, never authority (§29). |
| **Runtime Configuration** | The declarative, secret-free input describing which ports are injected and in which inert mode the scaffold is being assembled (§10). |
| **Runtime Capability** | An agent capability class as owned by `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §14.1 fact 6 and declared by `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]`. Referenced by **semantic name only** (§21). |
| **Runtime Dependency** | An external capability the scaffold does not implement and must receive by explicit injection (§11). |
| **Execution Envelope** | The run envelope owned by `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §15. The scaffold may represent it; it mints no envelope authority. |
| **Runtime Validation** | The ordered scaffold-level layer evaluation of §30. It establishes only what §30.11 says it establishes; it authorizes nothing. |
| **Runtime Eligibility** | The state in which a scaffold-level validation has passed. It is **not** execution authorization and **not** any of the eleven authorization facts. |
| **Runtime Activation** | The hypothetical transition to live execution. **The scaffold never performs it** (§15). |
| **Runtime Handle** | An opaque reference to a hypothetical operation. Because the scaffold starts nothing, every handle it can produce refers to no active work (§26). |
| **Runtime Event** | A normalized event type per `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §26. The scaffold may define types; it emits no execution event. |
| **Side Effect** | Any observable effect outside the calling process's own memory, classified by §32. |
| **External State** | Any state not owned by the calling process: filesystem, network, provider, Git, Shared Context, environment, or another process. |
| **Import Safety** | The property that importing any scaffold module produces **zero** side effects from §32's prohibited categories (§8). |
| **Construction Safety** | The property that constructing any scaffold object produces zero prohibited side effects and performs no hidden registration (§9). |
| **Execution Boundary** | The line the scaffold never crosses: every execution request terminates in an explicit fail-closed result (§15). |

## 3. Architectural ownership

No concern below is owned by more than one document. Where this specification
*consumes* another owner's concept, it is named "consumes," never "owns."

| Concern | Canonical owner | This specification's responsibility | Explicit non-responsibility |
| --- | --- | --- | --- |
| **The inert v1 boundary** | **Agent Runtime Architecture §37** (`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]`) | **Consumes unchanged**; adds only subordinate structural detail Agent Runtime Architecture §37 leaves open | MUST NOT restate uncited, extend, narrow, or reinterpret Agent Runtime Architecture §37's may/must-not lists |
| Agent identity | Agent Registry; Runtime §8.1 | References `agent_definition_id`, `installed_agent_id` | MUST NOT mint agent identity or register an agent |
| Run identity | Agent Runtime §8.1 | References `run_id`, `attempt_id`, `step_id`, `sub_run_id`, `trace_id` | MUST NOT mint a run identity outside an injected Identifier Port |
| Run lifecycle | Agent Runtime §12 (seventeen `run_state` values) | May represent the state machine as data | MUST NOT add, rename, alias, or extend a `run_state` value |
| Runtime operations | Agent Runtime §16 (nine bridge), §17.1 (seven context) | Assigns each a scaffold disposition (§14) | MUST NOT define an eighth context operation or a tenth bridge operation |
| Package identity and validation | `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` | May represent declared metadata as input | MUST NOT discover, install, activate, execute, or validate a package |
| Framework projection | `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` | Declares a port only | MUST NOT own projection, result normalization, or adapter selection |
| Shared Context projection | `[[MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001]]` | Declares a port and inert records only | MUST NOT read, project, validate, propose, or mutate context |
| Canonical Shared Context state | Shared Context Layer; Context Gate; Control Plane §9.3 | None | MUST NOT read or mutate canonical context |
| Context ingestion and admission | Context Ingestion Gate; Context Gate Implementation | None | MUST NOT define proposal lifecycle, precedence, or admission |
| Model routing | Model Router (Runtime §23; `shared_context/MODEL_ROUTING.md`) | Declares a port; may represent a routing **request** | MUST NOT select a model or produce a routing decision |
| Provider facts | `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` §21.1 | Declares a read port; may consume explicitly supplied static records in tests | MUST NOT query a registry, connect a provider, or resolve credentials |
| Capability resolution | `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §12 | References resolved results by semantic name | MUST NOT resolve a capability |
| Permission and approval | Gateway §17, §18; Control Plane §16; Runtime §14 (eleven facts) | May represent fact **evidence references** | MUST NOT evaluate policy, grant permission, or record an approval |
| Secrets and credentials | Provider Registry; Integration Gateway | None | MUST NOT read, hold, request, derive, cache, forward, or log any secret |
| Observability | Control Plane §7.1, §8.1; Runtime §34; `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` §5 | Supplies inert scaffold-domain projections (§27) | MUST NOT create a status dimension or a cost schema |
| Errors | Runtime §33; Gateway §25.2; Agent Package §21; Framework Bridge §23.3 | Consumes owner classes (§24) | MUST NOT duplicate, re-own, or arbitrate an owner class |
| Cancellation | Runtime §27 | Distinguishes inert cancellation states (§26) | MUST NOT claim cancellation of work it never started |
| Result normalization | Framework Bridge Contract / Runtime §16 `normalize_result` | None | MUST NOT define, own, resolve, or substitute for `normalize_result` |
| Cost attribution | Control Plane; AI Operations §5; Operations Data Contract | Declares a port only | MUST NOT define a cost schema or compute a cost |
| Run Ledger | Runtime §25; AI Operations §5 | Declares a port only; interfaces, not persistence (Agent Runtime Architecture §37) | MUST NOT persist a ledger record |
| Batch Orchestration | Future Batch Orchestration contract | None (§38) | MUST NOT create worktrees, spawn agents, or execute batch plans |
| Git and worktree ownership | Operator; `shared_context/SAFETY_CONTRACT.md`; `scripts/loop_ops` | None | MUST NOT inspect or mutate Git state |
| Source-code layout | Repository convention (`scripts/<package>/`) | Describes a **non-normative future** layout (§5) | MUST NOT create any file |
| Test layout | Repository convention (`tests/test_*.py`, `tests/*_fixtures.py`) | Describes future obligations (§34) | MUST NOT create any test |
| Future runtime implementation tasks | Separately gated tasks | Records them as deferred (§40) | MUST NOT authorize or begin any of them |

### 3.1 Precedence

```text
shared_context/SAFETY_CONTRACT.md
  > Enterprise-Provider ADR
  > Provider Registry contract
  > Integration Gateway contract
  > Shared Context Layer contracts
  > Agent Runtime architecture (including Agent Runtime Architecture §37's
    inert v1 boundary)
  > Agent Package Contract / Framework Bridge Contract / Shared Context Bridge
    Contract (on their own concerns)
  > this Agent Runtime Scaffold Specification (stricter only)
  > tenant policy (stricter only)
```

This specification MAY add requirements stricter than any document above it and
MUST NOT subtract from any. Conflicts fail closed and the affected structure is
left unspecified pending owner resolution.

## 4. Scaffold status

Stated explicitly and without qualification:

1. **This specification exists.** It is unverified and not accepted.
2. **Scaffold code does not exist.** No module, package, or source file has been
   created by this task or any prior task.
3. **The Agent Runtime does not exist.** No runtime coordinator, no
   `runtime_instance_id` has ever been assigned.
4. **No adapter exists** — no Framework Adapter, no Runtime Adapter, no no-op
   adapter, no fail-closed stub.
5. **No provider connection exists.** No credential has been read, resolved, or
   stored.
6. **No framework integration exists.** No framework SDK is installed, imported,
   or executed.
7. **No package execution exists.** No Agent Package has been discovered,
   installed, activated, or executed.
8. **Zero agents have been executed. Zero model calls. Zero tool executions.
   Zero context mutations.**

## 5. Intended repository boundary

Repository conventions were inspected read-only before this section was written.
The observed convention is: Python packages live under `scripts/<package>/` with
`__init__.py` (re-exporting a curated `__all__`) and an optional `__main__.py`;
tests live at `tests/test_<package>.py` with in-memory fixtures at
`tests/<package>_fixtures.py`, importing as `from scripts.<package> import …`;
there is **no** root `pyproject.toml`, `setup.py`, or dependency manifest, and
packages are **standard library only, Python 3.9 compatible**. The accepted
`scripts/provider_adapters/` package is the repository's existing inert-scaffold
precedent and is cited by Agent Runtime Architecture §37.

The future scaffold SHOULD follow that convention exactly. The tree below is
descriptive only.

```text
NON-NORMATIVE FUTURE LAYOUT — NOT IMPLEMENTED

scripts/agent_runtime_scaffold/
    __init__.py          curated re-exports; no side effects
    records.py           immutable typed runtime records
    vocabularies.py      closed owner-aligned vocabularies
    ports.py             typed Protocol port declarations
    config.py            declarative, secret-free configuration
    validation.py        deterministic scaffold validators
    composition.py       explicit composition root
    inert.py             no-op adapters and fail-closed stubs
    observability.py     inert scaffold-domain projections
    errors.py            owner-error mapping (consumes, never re-owns)
    lifecycle.py         run_state representation (owner-owned values)

tests/
    test_agent_runtime_scaffold.py
    agent_runtime_scaffold_fixtures.py
```

**No file above exists. This task creates none of them.** Module names are a
recommendation; a later implementation MAY choose different names provided every
responsibility in §6 has exactly one home and no module violates §8 or §9.

## 6. Module inventory

The minimum logical components a future scaffold MUST provide. Each row is a
responsibility, not a mandated filename.

| # | Component | Responsibility | MUST NOT |
| --- | --- | --- | --- |
| 1 | Domain records | Immutable typed values for owner-defined data (§29) | Carry authority, secrets, or mutable global state |
| 2 | Closed vocabularies | Owner-aligned enumerations referenced by semantic name (§21, §33) | Add, rename, renumber, or alias an owner value |
| 3 | Runtime ports | Typed boundary declarations (§12) | Imply an implementation exists |
| 4 | Configuration | Declarative, secret-free assembly input (§10) | Read the environment, `.env`, or any credential store |
| 5 | Validation | Deterministic ordered scaffold validators (§30) | Authorize execution or perform I/O |
| 6 | Composition | The explicit composition root (§7) | Construct anything at import time |
| 7 | No-op adapters and fail-closed stubs | Default inert port implementations (§13) | Return success for an unavailable operation |
| 8 | Observability projection | Inert scaffold-domain records (§27) | Create a Control Plane status dimension |
| 9 | Error mapping | Mapping scaffold conditions to owner-defined classes (§24) | Duplicate, re-own, or suppress an owner class |
| 10 | Lifecycle representation | Representation of Runtime §12's `run_state` as data | Add or extend a lifecycle value |

**This task creates no source file for any row above.**

## 7. Composition root

1. The future scaffold MUST expose exactly one explicit **composition root**: a
   caller-invoked function or class that assembles ports into a runtime object
   graph.
2. **Importing any module MUST NOT invoke the composition root.**
3. The composition root MUST accept its dependencies as explicit parameters and
   MUST NOT discover them.
4. Importing a module MUST NOT construct any of: providers; model clients;
   framework SDK clients; package loaders; MCP connections; databases; vector
   stores; network clients; Git clients; subprocesses; background workers.
5. The composition root MUST be callable with **no** injected implementations,
   yielding a fully inert object graph (§31).
6. Composition MUST be deterministic: the same configuration and the same
   injected ports produce the same graph.
7. **Composition is not activation.** A composed graph has performed nothing and
   is authorized for nothing.

## 8. Import safety

Importing any scaffold module MUST NOT:

| # | Prohibited at import |
| --- | --- |
| 1 | Read `.env` or any dotenv-style file |
| 2 | Read a secret, token, credential, or provider key from any source |
| 3 | Open a socket or perform any network operation |
| 4 | Access a provider API |
| 5 | Spawn a thread, process, or subprocess |
| 6 | **Read a file** — including a configuration file, package manifest, repository file, or Git file |
| 7 | **Scan, enumerate, or list a directory** |
| 8 | Mutate a file |
| 9 | Inspect Git state |
| 10 | Create a directory |
| 11 | Initialize a framework or import a framework SDK |
| 12 | **Probe for the presence of an optional SDK, package, distribution, or entry point** — by file test, metadata query, or package-manager access |
| 13 | Register a global hook, signal handler, or `atexit` handler |
| 14 | Configure logging globally, including the root logger (§28) |
| 15 | Emit any logging output (§28; §32's **Logging output** category) |
| 16 | **Create, enqueue to, consume from, or start any queue, worker, or scheduler** (§32's **Queue or scheduler activity** category) |
| 17 | Access system randomness (§32's **System randomness** category) |
| 18 | Read the system clock for a recorded value (§32's **System clock access** category) |
| 19 | Read or mutate Shared Context |

Rules:

1. Import MUST be **idempotent and observation-free**: importing twice is
   indistinguishable from importing once.
2. Module-level code MUST be limited to imports, type definitions, immutable
   constants, and function or class definitions.
3. A module MUST NOT read `os.environ` or equivalent at import time.
4. **Per Agent Runtime Architecture §37, which prohibits "any framework SDK
   import on any reachable path", the following subordinate implementation
   constraint applies:** optional third-party imports MUST NOT appear on any
   reachable import path. *Additionally, and owned by this specification:* a
   framework SDK MUST NOT be imported **to test for its presence**, and presence
   MUST NOT be detected by any non-importing mechanism either — including
   `importlib.metadata`, distribution or entry-point queries, `pkgutil`
   enumeration, or filesystem probing (row 12).
5. **Module metadata already supplied by the import system** — for example a
   module's own `__name__`, `__doc__`, or a constant defined in this package —
   MAY be inspected, because doing so performs no additional filesystem,
   package-manager, entry-point, or environment access. Any metadata access that
   would perform such an access is prohibited by rows 6, 7, and 12.
6. Import safety MUST be mechanically testable (§34 obligations 1, 19, 20, 22,
   23; §35).

## 9. Construction safety

Constructing any scaffold object MUST remain inert.

1. A constructor MUST NOT perform filesystem, network, process, or provider I/O.
2. A constructor MUST NOT read the environment or any secret.
3. A constructor MUST NOT perform hidden registration into any global registry,
   singleton, module-level mutable, or class-level cache.
4. A constructor MAY validate its arguments deterministically and MAY raise a
   determinate validation error, following the accepted
   `scripts/provider_adapters` precedent in which the disabled adapter validates
   its static manifest at construction.
5. A constructor MUST NOT resolve a dependency it was not given.
6. A constructed object MUST NOT begin background work.
7. **Construction is not authorization.** A successfully constructed object
   satisfies none of Runtime §14's eleven authorization facts.
8. Construction MUST be side-effect free with respect to every prohibited
   category in §32.

### 9.1 Deferred construction effects (normative)

**Construction safety MUST NOT be bypassable by postponing a prohibited action.**
Deferring an effect past `__init__` does not make it permitted. Every mechanism
below is bound by rules 1–8 and by §32 exactly as a constructor is:

| # | Deferred-effect mechanism |
| --- | --- |
| 1 | `__post_init__` and equivalent post-initialization hooks |
| 2 | Lazy properties (`@property` performing work on first access) |
| 3 | Cached properties (`functools.cached_property` and equivalents) |
| 4 | Descriptors, including `__get__`, `__set__`, and `__set_name__` |
| 5 | Class-level registration at class-body evaluation |
| 6 | Metaclass hooks and `__init_subclass__` |
| 7 | Default factories (`dataclasses.field(default_factory=…)`) |
| 8 | Callable defaults in function or method signatures |
| 9 | Dependency factories and provider callables |
| 10 | Object finalizers and destructors (`__del__`, `weakref` callbacks) |
| 11 | Context-manager entry (`__enter__`, `__exit__`) |
| 12 | Async context-manager entry (`__aenter__`, `__aexit__`) |
| 13 | Background callbacks |
| 14 | Scheduled callbacks and timers |
| 15 | Deferred imports performed inside a function or method body |
| 16 | Deferred socket creation |
| 17 | Deferred thread or process creation |
| 18 | **Deferred queue creation, enqueueing, or consumption** |
| 19 | First-method-call initialization |

Rules:

1. **No mechanism in the table above may perform any §32 prohibited category**,
   at any time, in a baseline inert composition.
2. A prohibited action postponed until first property access, first method call,
   context entry, or object destruction is **the same violation** as performing
   it in `__init__`.
3. Deferred imports (row 15) are subject to §8 rules 4–5 exactly as
   module-level imports are; moving an optional SDK import into a function body
   does not remove it from a reachable path.
4. These mechanisms MUST be covered by **§34 obligation 21**.

## 10. Runtime configuration boundary

Configuration is a **logical contract**, not a file format. This specification
mandates no serialization, file location, or loader.

Configuration MAY contain: references to owner-defined records; declared inert
mode; **the names of ports that were injected, recorded as inert descriptive
metadata only** (rule 6); declared validation strictness; declared observability
verbosity; and correlation identifiers supplied by the caller.

Configuration MUST NOT contain:

| # | Prohibited in configuration |
| --- | --- |
| 1 | A secret value of any kind |
| 2 | A provider key or token |
| 3 | A live credential or credential-store reference that resolves to a value |
| 4 | Implicit environment loading |
| 5 | An auto-connect flag |
| 6 | An auto-execute flag |
| 7 | A destructive Git instruction |
| 8 | Any value that would make an inert mode indistinguishable from a live mode |
| 9 | **An import-by-string implementation path** (dotted module or attribute path intended to be resolved) |
| 10 | **An executable Python callback or callable reference** |
| 11 | **A serialized callable** |
| 12 | **A pickled or otherwise deserializable executable object** |
| 13 | **A dynamic expression** (`eval`/`exec`-style content) |
| 14 | **A template expression capable of executing code** |
| 15 | **A shell command** |
| 16 | **A subprocess command array** |
| 17 | **A plugin entry point** |
| 18 | **A framework auto-import directive** |
| 19 | **A module-level factory name intended to be resolved to an object** |
| 20 | **An arbitrary code snippet in any language** |
| 21 | **An object deserialization hook** |
| 22 | **Environment-variable interpolation that resolves a secret or an executable target** |

Rules:

1. Configuration MUST be explicit; there is no default that enables anything.
2. An absent or unknown configuration value **denies**; it is never defaulted to
   a permissive value.
3. Configuration validity is **not** execution authorization (§22).
4. The inert modes the scaffold may declare are owner-defined: Runtime §36's
   `validation_only`, `dry_run`, `simulated`, and `fixture_only`. The scaffold
   MUST NOT declare `locally_executable`, `externally_connected`, or
   `production_enabled`, and MUST NOT invent a mode.
5. **Configuration validation MUST reject executable content fail-closed** (§30
   layer 5). Detection of any row 9–22 value denies the composition; it is never
   sanitized, ignored, or downgraded to a warning.
6. **"Declared injected port names" is inert descriptive metadata recording
   which §12 ports received an implementation. It is never a resolution
   mechanism.** Dependencies arrive only as explicit parameters to the
   composition root (§7 rule 3); a name in configuration MUST NOT be resolved to
   a module, attribute, class, or object.
7. A **static symbolic reference** MAY appear in configuration only when it
   satisfies **all five** of the following: it cannot trigger an import; it
   cannot trigger object construction; it cannot invoke code; it remains inert
   metadata; and it requires future explicit resolution by a separately
   authorized owner.
8. **Configuration parsed ≠ configuration safe**, and **static reference ≠
   implementation resolved.**

## 11. Dependency injection

1. Every external capability MUST be represented by a port (§12) and supplied by
   **explicit injection**.
2. **No external dependency may be resolved through hidden global state** —
   no module-level singleton, no ambient registry, no import-time lookup, no
   environment-based discovery, no entry-point scanning, no plugin auto-load.
3. A missing injection MUST yield the default inert implementation (§13), never
   a silently constructed real one.
4. Injection MUST be per-composition, never process-global.
5. The scaffold MUST NOT provide a mechanism for an injected port to inject
   further ports transitively without the caller's explicit participation.
6. An injected port that is itself unavailable MUST be representable as such
   (§13) rather than being replaced by a substitute.

## 12. Runtime ports

Ports declare boundaries only. **A declared port MUST NOT imply that an
implementation exists, is installed, is available, or is authorized.**

| # | Port | Declares the boundary to | Owner of the real capability |
| --- | --- | --- | --- |
| 1 | Package Validation Port | Package metadata validation | `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` |
| 2 | Framework Bridge Port | Framework projection operations | `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` |
| 3 | Shared Context Bridge Port | Context selection, projection, proposal | `[[MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001]]` |
| 4 | Model Routing Port | Routing requests and decisions | Model Router (Runtime §23) |
| 5 | Provider Registry Read Port | Provider and MCP record reads | `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` |
| 6 | Policy Evaluation Port | Policy evaluation | `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` §17 |
| 7 | Approval Port | Operator approval records | Control Plane §16; Gateway §18 |
| 8 | Tool Gateway Port | Tool registration, authorization, invocation | Tool Gateway (Runtime §21) |
| 9 | Observability Port | Observability record emission | Control Plane; AI Operations §5 |
| 10 | Run Ledger Port | Run ledger records | Runtime §25; AI Operations §5 |
| 11 | Cost Attribution Port | Cost estimates and actuals | Control Plane; Operations Data Contract |
| 12 | Clock Port | Current time | Injected; the scaffold reads no ambient clock for recorded values |
| 13 | Identifier Port | Identifier minting | Runtime §8.1 and §8.2's rules |
| 14 | Cancellation Port | Cancellation requests | Runtime §27 |

Rules:

1. A port MUST be a typed structural declaration. The repository precedent is
   `typing.Protocol` with `runtime_checkable`, as used by
   `scripts/provider_adapters`.
2. **Port declared ≠ implementation available.** Conformance to a port grants no
   runtime authority.
3. A port MUST NOT expose a generic escape hatch — no untyped `execute(**kwargs)`,
   no raw request passthrough, no dynamic method dispatch by name.
4. A port MUST NOT accept or return a secret value.
5. Ports 12 and 13 exist specifically so that time and identity are injected
   rather than ambient, keeping validation and observability deterministic.
6. This specification declares no port method signatures; a later implementation
   task derives them from the owner contracts under its own review.

## 13. No-op and fail-closed implementations

The distinction below is load-bearing and MUST be preserved exactly.

| # | Disposition | Meaning | Permitted when |
| --- | --- | --- | --- |
| 1 | **No-op** | The operation was deliberately not performed, and its absence does not change correctness | And only when the operation is genuinely optional, e.g. emitting an optional observability record |
| 2 | **Unavailable** | No implementation is injected for this port | Always representable; never a success |
| 3 | **Unsupported** | The operation cannot be expressed at this boundary | Always representable; never a success |
| 4 | **Denied** | An owner-defined authorization or policy determination refused it | Only when an owner made the determination |
| 5 | **Unimplemented** | The scaffold deliberately implements nothing here | Always representable; never a success |
| 6 | **Invalid configuration** | The configuration failed §30 validation | Always representable; never a success |

Rules:

1. **A no-op MUST NOT produce a false success for an operation whose absence
   matters.** Dispositions 2–6 are refusals and MUST be surfaced as such.
2. Following Agent Runtime Architecture §37 and the
   accepted Provider Adapter Scaffold precedent, **no execution-success outcome
   may be representable** in the inert scaffold. The scaffold's execution
   outcome vocabulary MUST NOT contain a success member at all — absence is
   structural, not conventional.
3. A refusal MUST carry an owner-defined class where one exists (§24) and MUST
   preserve the original cause.
4. A refusal MUST record that no external effect occurred, following the
   precedent field `provider_request_occurred=False` in
   `scripts/provider_adapters`.
5. The six dispositions are distinct and MUST NOT be collapsed, aliased, or
   defaulted into one another.

## 14. Runtime operation coverage

The canonical operation lists were reconstructed mechanically from the owner
document: `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §17.1 (**seven**
Shared Context operations) and §16 (**nine** framework bridge operations),
**sixteen** operations in total. Every one has a disposition below; none is
omitted by relying on prose-level "consumption."

| # | Operation | Canonical owner | Scaffold exposure | Inert behavior | Error or outcome | Side effects |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `read_snapshot` | Runtime §17.1 | Shared Context Bridge Port | Unavailable unless injected | `CONTEXT_ACCESS_DENIED` (owner) when refused; never a snapshot | **None** |
| 2 | `propose_update` | Runtime §17.1 | Shared Context Bridge Port | Unimplemented; creates no proposal | Refusal; never a created proposal | **None** |
| 3 | `append_evidence` | Runtime §17.1 | Shared Context Bridge Port | Unimplemented; appends nothing | Refusal | **None** |
| 4 | `create_derived_context` | Runtime §17.1 | Shared Context Bridge Port | Unimplemented | Refusal | **None** |
| 5 | `request_canonical_mutation` | Runtime §17.1 | Shared Context Bridge Port | Unimplemented; the scaffold never enters an approval path | Refusal | **None** |
| 6 | `create_handoff_context` | Runtime §17.1 | Shared Context Bridge Port | Unimplemented | Refusal | **None** |
| 7 | `invalidate_derived_context` | Runtime §17.1 | Shared Context Bridge Port | Unimplemented | Refusal | **None** |
| 8 | `validate_package_compatibility` | Runtime §16 | Framework Bridge Port | Unavailable unless injected; the scaffold performs no compatibility determination | Owner class `PACKAGE_MISMATCH` only when an injected owner determines it; otherwise unavailable | **None** |
| 9 | `prepare_invocation` | Runtime §16 | Framework Bridge Port | Unimplemented; builds no framework-local state | Refusal; never `failed` from execution, because nothing executed | **None** |
| 10 | `translate_envelope` | Runtime §16 | Framework Bridge Port | Unimplemented | Refusal; the scaffold emits **neither** `BRIDGE_UNSUPPORTED_BEHAVIOR` **nor** `PROJECTION_UNSUPPORTED` (§24 rule 4) | **None** |
| 11 | `start_execution` | Runtime §16 | Framework Bridge Port | **Always fails closed** (§15) | `EXECUTION_BLOCKED` (Runtime §33) | **None** |
| 12 | `stream_events` | Runtime §16 | Framework Bridge Port | Yields no execution event; the scaffold starts nothing to observe | Empty; never a synthesized event | **None** |
| 13 | `request_cancellation` | Runtime §16 / Cancellation Port | Cancellation Port | **Implementation unavailable — §26 state 5, the inert default**; a malformed reference yields state 4 first | Selected by §26's normative order; `INVALID_REFERENCE_SHAPE` for a malformed reference, otherwise the unavailable disposition; never a claimed cancellation | **None** |
| 14 | `normalize_result` | Runtime §16 | **Not exposed** | The scaffold defines no result normalization | None — this specification owns no part of it (§25) | **None** |
| 15 | `normalize_failure` | Runtime §16 | **Not exposed** | The scaffold maps only its own refusals (§24) | None | **None** |
| 16 | `report_unsupported_behavior` | Runtime §16 | Framework Bridge Port | May report the scaffold's own declared limitations honestly | Declarative only | **None** |

Rules:

1. **Not one operation performs an external side effect in the inert scaffold.**
2. Operations 14 and 15 are deliberately **not exposed**: `normalize_result` is
   the subject of an open Framework Bridge finding and this specification owns
   no part of it (§25, §40).
3. The scaffold defines **no eighth context operation and no tenth bridge
   operation**.
4. Exposure of a port for an operation is not a claim that the operation can be
   performed.

## 15. Execution boundary

1. **The future scaffold MUST NOT execute an agent.**
2. Any execution request MUST terminate through an explicit fail-closed result
   carrying an owner-defined class — `EXECUTION_BLOCKED` per Runtime §33, whose
   definition already names "the inert-v1 boundary" as a cause.
3. The refusal MUST hold **regardless of configuration**, and — following
   Agent Runtime Architecture §37 — **across all combinations of the eleven
   authorization facts,
   including the case where all eleven are satisfied**.
4. No configuration value, injected port, environment condition, or test hook
   may make execution succeed.
5. The scaffold MUST NOT start a framework process, invoke a model, execute a
   tool, or reach a provider.
6. **Execution requested ≠ execution started.** The scaffold never transitions a
   run to a live-executing `run_state`.

## 16. Agent Package boundary

The scaffold MAY represent, as inert input data, the package metadata and
validation inputs that `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` and
Runtime §10.1 define, referenced by semantic name.

The scaffold MUST NOT:

1. discover packages automatically, by scan, entry point, or convention;
2. install a package;
3. activate a package;
4. execute a package;
5. resolve a dependency;
6. grant a package capability;
7. determine package verification (Runtime §14.1 fact 2) on its own;
8. define a package-lifecycle rendering field (§40).

Rules:

1. **Package known ≠ package validated**, and **package validated ≠ package
   executable.**
2. A package declaration is a request statement and grants nothing.
3. The scaffold asserts **no** Agent Package contract version as canonically
   current (§40).

## 17. Framework Bridge boundary

The scaffold MAY expose the Framework Bridge Port (§12 port 2).

It MUST NOT:

1. install a framework;
2. import an optional framework SDK on any reachable import path — prohibited by
   **Agent Runtime Architecture §37** and expressed as a subordinate constraint
   in §8 rule 4 — or detect its presence by any non-importing mechanism (§8
   row 12);
3. initialize a framework;
4. validate framework compatibility empirically;
5. select a Framework Adapter;
6. execute a bridge operation;
7. own result normalization (§25);
8. resolve the Framework Bridge error overlap (§24 rule 4).

Rules:

1. **Framework identified ≠ framework validated**, and **framework validated ≠
   framework authorized.**
2. **No framework profile is treated as runtime-eligible.** Empirical framework
   validation remains `NOT_PERFORMED` and is owned by the Framework Bridge
   Contract and the future per-framework adapter specifications (§40).
3. Adapter declared ≠ adapter installed.

## 18. Shared Context Bridge boundary

The scaffold MAY expose inert context-request and context-proposal **records**
as typed data, and the Shared Context Bridge Port (§12 port 3).

It MUST NOT:

1. read canonical Shared Context automatically or otherwise;
2. project context;
3. validate returned context;
4. create a context proposal;
5. determine canonical mutation eligibility;
6. mutate canonical context;
7. define proposal-lifecycle precedence or quarantine/rejection precedence;
8. redefine the Shared Context memory taxonomy;
9. replace Control Plane's `ContextPacket` ownership;
10. claim replay protection.

Rules:

1. **Context record represented ≠ context read**, and **context proposal
   represented ≠ context created.**
2. A represented record is inert data with no admission meaning whatsoever.
3. The scaffold MUST NOT use "subtractive or equal" as an implemented,
   measurable property; no owner-defined validator for it exists (§40).

## 19. Model Router boundary

1. The scaffold MAY represent a **routing request** carrying only the fields
   Runtime §23.2 permits.
2. It MUST NOT produce a routing decision unless a future authorized owner
   implementation is injected through the Model Routing Port.
3. It MUST NOT select a model by name.
4. It MUST NOT invoke a model under any condition.
5. **Model requested ≠ model selected**, and **model selected ≠ model invoked.**

## 20. Provider Registry boundary

1. The scaffold MAY consume **static, explicitly supplied** provider records in
   tests and fixtures.
2. It MUST NOT query a live registry.
3. It MUST NOT connect a provider.
4. It MUST NOT resolve, read, or hold a credential.
5. It MUST NOT interpret provider availability as authorization.
6. **Provider known ≠ provider connected**, and **provider available ≠ provider
   permitted.**
7. Provider authorization remains Provider Registry §21.1's eight facts
   evaluated by Integration Gateway §17; the scaffold evaluates none of them.

## 21. Capability and permission model

1. Runtime capabilities and package capabilities MUST be referenced by
   **semantic name** from the canonical owner contracts.
2. The scaffold MUST NOT create a parallel ordinal capability model and MUST NOT
   cite any capability or capability state by cross-document ordinal position.
3. Owner-owned states MUST be represented without renumbering, reordering, or
   aliasing.
4. The scaffold MUST NOT define a `ready` boolean or any aggregate standing for
   two or more of Runtime §14's eleven authorization facts (Runtime §14.3 rule
   1).
5. The eleven facts are conjunctive and independently established; the scaffold
   may represent **evidence references** only, never derive a fact.

## 22. Policy and approval

1. Configuration validity, structural validation, port availability, framework
   compatibility, package metadata completeness, and successful construction
   **MUST NOT** equal policy approval or Operator authorization.
2. The scaffold evaluates no policy and records no approval.
3. An approval is one exact, typed, versioned, digest-bound target binding owned
   by Control Plane §16 and Gateway §18; the scaffold may hold a **reference**
   to such a record and MUST NOT synthesize, infer, extend, or replay one.
4. **Configuration valid ≠ execution authorized.**
5. **Validation passed ≠ external action authorized.**

## 23. Runtime lifecycle treatment

1. The scaffold MUST NOT invent, extend, rename, alias, or renumber any Runtime
   §12 `run_state` value.
2. It MAY represent the seventeen owner-defined states and their allowed
   transitions as inert data, and MAY implement the state machine as Agent
   Runtime Architecture §37 permits.
3. Because the scaffold starts nothing, the states it can legitimately reach in
   an inert composition are limited to those reachable without execution; it
   MUST NOT synthesize a live-executing state.
4. The scaffold MUST NOT project `run_state` onto any Control Plane §8.1
   dimension; that projection is owned by Runtime §12.2 and is not restated
   here.
5. The absence of a live run MUST be representable explicitly rather than as an
   empty or defaulted state.

## 24. Error taxonomy

The canonical error surfaces were audited before defining anything:
Runtime §33 (49 Agent Runtime-layer classes, one-class-per-row); Integration
Gateway §25.2 (the provider-boundary set, including the classes Runtime §33
explicitly adopts and leaves owned by the Gateway); Agent Package §21;
Framework Bridge §23.3.

Rules:

1. **The scaffold MUST prefer consuming an owner-defined class over defining
   one.** For every condition an owner class already covers, the owner class is
   used unchanged.
2. Owner classes the inert scaffold is expected to surface include, at minimum:
   `EXECUTION_BLOCKED` (execution refused by the inert-v1 boundary),
   `CONTEXT_ACCESS_DENIED`, `AUTHORIZATION_DENIED`, `TENANT_ISOLATION_VIOLATION`,
   `INVALID_REFERENCE_SHAPE`, `INVALID_CANONICAL_TYPE`, `UNSUPPORTED_FRAMEWORK`,
   `UNSUPPORTED_VALUE`, and `CANCELLATION_UNSUPPORTED` — each cited to Runtime
   §33 as its owner.
3. Any scaffold-owned error class MUST have: unique ownership; a deterministic
   trigger; no semantic overlap with an owner-defined class; a stable
   observability mapping; and preservation of the original cause.
4. **The scaffold emits neither `PROJECTION_UNSUPPORTED` nor
   `BRIDGE_UNSUPPORTED_BEHAVIOR`** and does not arbitrate, resolve, or select
   between them; that overlap is an open Framework Bridge finding (§40).
5. **The scaffold emits no Shared Context Bridge-owned rejection class** and does
   not select among that contract's unresolved error neighbours (§40).
6. An error MUST NOT contain a secret value; rejection records the field path and
   class, never the value (Runtime §33).
7. Suppressing or replacing a more specific owner-defined error is prohibited.

## 25. Result behavior

1. **The scaffold MUST NOT return a coerced success.**
2. No execution-success outcome is representable (§13 rule 2).
3. Unavailable execution MUST NOT be represented as successful execution, an
   empty success, a partial success, or a defaulted result.
4. **This specification does not define, own, resolve, or substitute for the
   Framework Bridge / Runtime §16 `normalize_result` operation**, nor for the
   open Framework Bridge finding concerning it. Nothing here may be cited as
   satisfying that obligation.
5. A result MUST state honestly whether any external effect occurred; in the
   inert scaffold the answer is always that none did.

## 26. Cancellation boundary

The scaffold creates no running work. Cancellation behavior MUST distinguish:

| # | State | Meaning | Reachable in a baseline inert composition? |
| --- | --- | --- | --- |
| 1 | No active operation | Nothing was started; there is nothing to cancel | **Only** with a well-formed owner-supplied reference **and** an injected or approved-fixture Cancellation Port (order step 3) |
| 2 | Unsupported cancellation | The boundary cannot express cancellation — owner class `CANCELLATION_UNSUPPORTED` (Runtime §33) | **Only** under that canonical owner condition, at order step 3 |
| 3 | Already terminal | The referenced record is already in a terminal state | **Only** from owner-supplied immutable fixture state, at order step 3; never derived by the scaffold |
| 4 | Invalid handle | The reference is malformed or unknown — owner class `INVALID_REFERENCE_SHAPE` | **Yes** — a shape check, requiring no port and no state (order step 1) |
| 5 | Implementation unavailable | No Cancellation Port implementation is injected | **Yes — the inert default** (order step 2) |

**Selection order (normative).** The applicable state MUST be determined by this
total order, so that the inert response is deterministic and no two states can
both apply:

1. **If the supplied reference is malformed or unknown → state 4.** This is a
   pure shape check requiring no port and no operation state.
2. **Else if no Cancellation Port implementation is injected → state 5.** This
   is the **inert default** and the outcome a baseline inert composition
   reaches whenever a well-formed reference is supplied.
3. **Else** — an implementation or approved inert fixture is present — the
   owner-supplied input selects among states 2, 3, and 1, in that order: the
   canonical `CANCELLATION_UNSUPPORTED` condition first, then owner-supplied
   immutable terminal state, then a well-formed reference known not to identify
   active work.

**Unreachable outcomes.** Because the inert scaffold creates no running work,
the following are **unreachable and MUST NOT be represented** at any step:

1. successful cancellation of active work;
2. cancellation of a live operation;
3. any outcome implying that work was stopped.

Rules:

1. The five states MUST NOT be collapsed into one another. Applying the
   selection order above — reaching state 5 when a well-formed reference is
   supplied and no implementation is injected — is a **selection, not a
   collapse**.
2. **The scaffold MUST NOT claim to have cancelled work it never started.**
3. **The scaffold MUST NOT create mutable live-operation state merely to
   distinguish these outcomes.** State 3 is representable only from
   owner-supplied immutable input; the scaffold maintains no operation registry,
   no handle table, and no cancellation ledger.
4. **Cancellation requested ≠ active work exists.**
5. Cancellation honesty follows Runtime §27; the scaffold defines no competing
   cancellation model and never reports a local stop as an external stop.

## 27. Observability

Information architecture only. Every field below is **typed entity data** under
Control Plane §7.1. **No new Control Plane status dimension is created.**

| # | Inert observability field |
| --- | --- |
| 1 | Scaffold specification version |
| 2 | Configuration identity (a digest or equivalent of the declarative configuration) |
| 3 | Component inventory (§6 rows present) |
| 4 | Injected port inventory (which of §12's ports received an implementation) |
| 5 | No-op or unavailable component list |
| 6 | Validation outcome, per layer, never collapsed to one boolean |
| 7 | Attempted prohibited operation |
| 8 | Denial reason, with its owner-defined class |
| 9 | Canonical owner reference for each denial |
| 10 | Correlation identifier supplied by the caller |
| 11 | Run identifier **only** where one is owner-supplied |
| 12 | **Scaffold Zero-Execution Evidence** record when its evidence scope is complete, or the non-affirmative **`EVIDENCE_INCOMPLETE`** outcome in its place when it is not — never both, never neither (§27.1) |

Rules:

1. Scaffold fields MUST be labeled scaffold-domain data and MUST NOT be rendered
   as a `lifecycle_status`, `evidence_state`, or `approval_state` value.
2. No projection may synthesize a universal "healthy", "ready", or green state.
3. `NOT_RUN` / `NOT_IMPLEMENTED` never renders as pass.
4. Field 12 is governed entirely by §27.1.
5. Observability output MUST NOT contain a secret value or a full sensitive
   context payload.
6. The scaffold MUST NOT mint a `run_id`; field 11 is populated only from an
   owner-supplied value.

### 27.1 Scaffold Zero-Execution Evidence (normative)

The concept previously named "zero-execution confirmation" is **renamed**,
because that name falsely implied a global guarantee about system-wide activity.
It is defined here narrowly.

**Scaffold Zero-Execution Evidence** is a scaffold-owned **audit and validation
evidence record**, and nothing more.

| # | Required property |
| --- | --- |
| 1 | It is **derived** from the observed attempted operation and the relevant §32 side-effect sentinels — never asserted |
| 2 | It is **scoped to exactly one correlation identifier or one validation run** |
| 3 | It is **explicitly non-canonical** scaffold-domain data |
| 4 | It is **not** a Control Plane status dimension |
| 5 | It states **only** what its own evidence boundary covers |
| 6 | It is **not** a Runtime run result |
| 7 | It is **not** equivalent to Runtime success |
| 8 | It is emitted **only when its evidence scope is complete**. Incomplete evidence never yields a zero-execution record; it yields `EVIDENCE_INCOMPLETE` instead (rules 2–4) |

**Emission model (normative).** The record is **affirmative-only**: it exists
solely to state a bounded negative that its own sentinels actually established.
There is **no partial, `unknown`, or tri-state zero-execution record**, because
a record named "zero-execution evidence" must not be emitted in a state where it
cannot evidence zero execution.

Rules:

1. **The record makes no claim about activity outside its evidence boundary.**
   It states that, within one identified validation run, the scaffold's own
   sentinels observed no execution, model call, tool invocation, provider
   request, or Shared Context access or mutation.
2. **Evidence scope is complete only when both hold:** sentinel coverage exists
   for every §32 category the record speaks to, **and** no §12 port has an
   injected implementation. An injected implementation makes the scope
   incomplete by definition, because the scaffold cannot observe behavior behind
   a port.
3. **When evidence scope is incomplete, no Scaffold Zero-Execution Evidence
   record is emitted at all.** The validation run instead records the distinct,
   non-affirmative outcome **`EVIDENCE_INCOMPLETE`**, naming the categories whose
   coverage is absent and, where applicable, the injected ports responsible.
4. **`EVIDENCE_INCOMPLETE` is not zero-execution evidence.** It is a
   scaffold-domain validation outcome and MUST NOT be represented as
   zero-execution evidence, as a Runtime result, as Runtime success, as a
   Control Plane status dimension or §8.1 enum value, or as any positive
   assertion about what did or did not occur. It is **not** an error class and
   adds nothing to §24's taxonomy, which remains owner-owned.
   **Incomplete evidence ≠ affirmative zero-execution evidence.**
5. **A record of either kind MUST NOT fabricate a live run identifier.** Each
   carries only the caller-supplied correlation identifier, or an owner-supplied
   `run_id` where one exists (§27 rule 6).
6. **Zero-execution evidence ≠ Runtime result**, and **zero-execution evidence ≠
   global system status.**
7. A record of either kind MUST NOT be rendered as, or coerced into, any Control
   Plane §8.1 enum value.
8. Both outcomes MUST be covered by **§34 obligation 16**.

## 28. Logging

The future scaffold is a library and MUST behave as one.

1. It MUST NOT configure the root logger, call `basicConfig`, add handlers to
   the root logger, or alter global logging levels.
2. It SHOULD obtain a module-scoped logger and attach no handler, leaving
   configuration entirely to the application.
3. It MUST NOT emit a secret value, provider key, token, or credential.
4. It MUST NOT log a full sensitive context payload.
5. It MUST NOT claim that external execution occurred.
6. It MUST NOT suppress or swallow an original error.
7. It MUST NOT log at import time.

## 29. Data records

1. Records SHOULD be immutable typed structures. The repository precedent is
   frozen dataclasses and `(str, Enum)` closed vocabularies, standard library
   only, Python 3.9 compatible.
2. Records MUST remain owner-aligned: field names and vocabulary values come
   from the canonical owner contract, referenced by semantic name.
3. A record MUST NOT carry authority, a secret, or mutable global state.
4. Serialization MUST be defined only where a canonical contract permits it;
   where a digest is required, Runtime §8.3's canonical serialization and type
   discipline apply and are consumed unchanged.
5. Records MUST NOT be deserialized from untrusted input by a mechanism capable
   of executing code (§37 threat 12).
6. **A record is data, never an authorization.**

## 30. Validation model

Ordered scaffold-level layers. Later layers MUST NOT run before earlier layers
reach a determination.

| # | Layer | Input | Output |
| --- | --- | --- | --- |
| 1 | Configuration structure | Declarative configuration | Structurally valid, or invalid configuration |
| 2 | Dependency declaration | Declared injections | Every declared dependency is a §12 port, or invalid |
| 3 | Port availability | Injected implementations | Per-port available or unavailable — never substituted |
| 4 | Owner-version compatibility reference | Declared owner contract references | References resolve, or invalid |
| 5 | Forbidden capability detection | Configuration and declared ports | No prohibited capability requested and **no executable configuration content** (§10's executable-content prohibitions), or denied fail-closed |
| 6 | Import-safety policy | Module surface | Conforms to §8, or non-conforming |
| 7 | Construction-safety policy | Constructed graph | Conforms to §9, or non-conforming |
| 8 | Side-effect declaration | Declared side-effect categories | Only permitted categories declared (§32), or denied |
| 9 | Observability readiness | §27 fields | Producible, or ineligible |
| 10 | Inert-mode guarantee | The composed graph | §31.1's Baseline Inert Invariant holds, or the composition is rejected |

### 30.11 What scaffold validation does not do

Validation MUST NOT:

1. authorize execution;
2. authorize provider, model, or tool access;
3. satisfy or derive any of Runtime §14's eleven authorization facts;
4. grant a package capability;
5. establish framework validation;
6. imply trust in any input.

Correspondingly: **`validation passed ≠ external action authorized`** and
**`runtime eligibility ≠ runtime activation`**.

## 31. Inert-mode invariant

This section defines **two distinct properties**. They have different scopes and
MUST NOT be conflated, merged, or cited interchangeably.

### 31.1 The Baseline Inert Invariant

The **Baseline Inert Invariant** is the scaffold's primary machine-testable
safety property. It applies to a **baseline inert composition**, defined as a
composition in which **all three** of the following hold:

1. the default inert configuration is used;
2. **no live external implementation is injected**; and
3. only repository-approved inert fixtures (§35 technique 5) or unavailable
   ports (§13 disposition 2) are present.

> **In a baseline inert composition, the composed scaffold performs zero side
> effects in every prohibited category of §32 — including network access,
> subprocess and thread creation, **queue, worker, and scheduler creation,
> enqueueing, or consumption**, filesystem read and mutation, Git inspection and
> mutation, environment and secret access, logging output, system randomness,
> and clock access; represents no execution success; terminates every execution
> request in an explicit fail-closed refusal carrying an owner-defined class;
> creates no live Runtime Handle; and performs no framework, provider, model,
> package, tool, MCP, or Shared Context action.**

Rules:

1. The Baseline Inert Invariant MUST hold across **all** combinations of Runtime
   §14's eleven authorization facts, **including the case in which all eleven
   are satisfied** (Agent Runtime Architecture §37).
2. **Scope is exact.** The Baseline Inert Invariant makes **no claim whatsoever**
   about a composition containing an externally injected live implementation.
   Such a composition is governed by §31.2, not by this invariant.
3. The Baseline Inert Invariant MUST be asserted by **§34 obligation 18**, over
   the complete property register of §31.1.1 — never over a subset.
4. A composition that cannot establish the Baseline Inert Invariant MUST be
   rejected by §30 layer 10.
5. The prose statement above is a summary. **§31.1.1 is the authoritative,
   enumerable definition** of what the invariant asserts; where the two appear to
   differ, §31.1.1 governs.

#### 31.1.1 Baseline Inert Invariant property register (normative)

This register is the **single, deterministic, machine-enumerable definition** of
the Baseline Inert Invariant. Every property is individually observable by a
side-effect sentinel (§35 technique 3) or by a structural check. **§34
obligation 18 MUST assert every row; a run that asserts a proper subset does not
satisfy obligation 18.** A future amendment that adds a §32 category MUST add
the corresponding register row and recompute §42.

| # | Property asserted in a baseline inert composition | Anchor |
| --- | --- | --- |
| 1 | Zero filesystem read | §32 **Filesystem read** |
| 2 | Zero filesystem write | §32 **Filesystem write** |
| 3 | Zero directory creation | §32 **Filesystem write**; §8's directory-creation prohibition |
| 4 | Zero network access | §32 **Network access** |
| 5 | Zero process or subprocess creation | §32 **Process creation** |
| 6 | Zero thread creation | §32 **Thread or worker creation** |
| 7 | Zero worker creation | §32 **Thread or worker creation** |
| 8 | Zero queue creation, enqueueing, or consumption | §32 **Queue or scheduler activity** |
| 9 | Zero scheduler, delayed, or deferred job activity | §32 **Queue or scheduler activity** |
| 10 | Zero Git inspection | §32 **Git inspection** |
| 11 | Zero Git mutation | §32 **Git mutation** |
| 12 | Zero environment access | §32 **Environment access**; §8 rule 3 |
| 13 | Zero secret access | §32 **Secret access** |
| 14 | Zero provider access | §32 **Provider access** |
| 15 | Zero model invocation | §32 **Model invocation** |
| 16 | Zero framework initialization | §32 **Framework initialization** |
| 17 | Zero package activation | §32 **Package activation** |
| 18 | Zero command execution | §32 **Command execution** |
| 19 | Zero hook registration or execution | §32 **Hook execution**; §8's hook-registration prohibition |
| 20 | Zero plugin loading | §32 **Plugin loading** |
| 21 | Zero MCP connection | §32 **MCP connection** |
| 22 | Zero Shared Context read | §32 **Shared Context read** |
| 23 | Zero Shared Context mutation | §32 **Shared Context mutation** |
| 24 | Zero telemetry export | §32 **Telemetry export** |
| 25 | Zero logging output and zero logger mutation | §32 **Logging output**; §28 |
| 26 | Zero system randomness access | §32 **System randomness** |
| 27 | Zero system clock access for a recorded value | §32 **System clock access** |
| 28 | Zero scaffold-originated identifier generation — identifiers arrive only from the Identifier Port or a fixed fixture | §12's Identifier Port; §32 rule 5 |
| 29 | **Absence of any global registry, singleton, module-level mutable, class-level cache, or service locator** | §9 rule 3; §11 rule 2 |
| 30 | Every execution request terminates in an explicit fail-closed refusal carrying an owner-defined class | §15; §24 |
| 31 | **Absence of any success representation** in the execution outcome vocabulary | §13 rule 2; §25 |
| 32 | **Absence of any live Runtime Handle** and of mutable live-operation state | §2 *Runtime Handle*; §26 rule 3 |

### 31.2 Injected Component Eligibility

**An externally injected component MUST NOT inherit inert eligibility merely
because it satisfies a Python interface.** Structural conformance to a §12 port
is not evidence of safety, and §31.1 confers nothing on it.

An injected component MAY participate only in a future, **explicitly authorized**
test or implementation mode, and only after separate validation of **all seven**
of the following:

| # | Required validation |
| --- | --- |
| 1 | Side-effect declaration — which §32 categories it may perform |
| 2 | Import safety (§8) |
| 3 | Construction safety (§9) |
| 4 | Capability boundary (§21) |
| 5 | Permission boundary (§22) |
| 6 | Fixture identity — whether it is an approved inert fixture or a live implementation |
| 7 | Observability behavior (§27) |

Rules:

1. **Port injected ≠ port safe**, and **interface conformance ≠ execution
   eligibility.**
2. This specification defines **no live-mode invariant** and authorizes no
   injected live implementation. Both are future, separately gated concerns
   (§40).
3. An unvalidated injected component MUST be treated as **unavailable** (§13
   disposition 2), never as present.
4. **The one property that holds regardless of configuration, injected ports,
   environment, or test hooks is the execution refusal of §15** — no injection
   can make execution succeed (§15 rule 4). No other conjunct of §31.1 extends
   beyond a baseline inert composition.

## 32. Side-effect inventory

The categories below are the closed baseline. A later implementation MAY extend
the list additively but MUST NOT remove or merge a category.

| # | Category | Inert scaffold |
| --- | --- | --- |
| 1 | Filesystem read | **Prohibited** |
| 2 | Filesystem write | **Prohibited** |
| 3 | Process creation | **Prohibited** |
| 4 | Thread or worker creation | **Prohibited** |
| 5 | Network access | **Prohibited** |
| 6 | Provider access | **Prohibited** |
| 7 | Model invocation | **Prohibited** |
| 8 | Secret access | **Prohibited** |
| 9 | Environment access | **Prohibited** |
| 10 | Git inspection | **Prohibited** |
| 11 | Git mutation | **Prohibited** |
| 12 | Shared Context read | **Prohibited** |
| 13 | Shared Context mutation | **Prohibited** |
| 14 | Package activation | **Prohibited** |
| 15 | Command execution | **Prohibited** |
| 16 | Hook execution | **Prohibited** |
| 17 | Plugin loading | **Prohibited** |
| 18 | MCP connection | **Prohibited** |
| 19 | Framework initialization | **Prohibited** |
| 20 | Logging output | **Prohibited** by default (§28); permitted only through a future explicitly injected inert test sink, which must be side-effect declared and observable |
| 21 | **Queue or scheduler activity** — creating an in-process, async, or worker queue; enqueueing background work; consuming queued work; starting a queue processor; registering a queue callback; creating scheduler-backed, delayed, or deferred jobs | **Prohibited** |
| 22 | System randomness | **Prohibited** — see rule 5 |
| 23 | System clock access for a recorded value | **Prohibited** — values come from the injected Clock Port (§12 port 12) |
| 24 | Telemetry export | **Prohibited** |

Rules:

1. **All twenty-four categories are prohibited in a baseline inert composition**
   (§31.1). The scaffold's permitted effects are confined to in-process
   computation and returning values to its caller.
2. A category becomes possible only through an explicitly injected
   implementation supplied by a separately authorized future task and validated
   under §31.2 — never by default and never by discovery.
3. Prohibition MUST be mechanically checkable (§34, §35).
4. Filesystem read is prohibited to the scaffold package itself; a **test** may
   read scaffold source for static assertions, following the existing
   `tests/test_provider_adapters.py` precedent.
5. **Randomness (the System randomness category).** Implicit randomness is
   prohibited in a baseline inert composition. Random identifiers, random seeds,
   and nondeterministic iteration or ordering are prohibited. Identifier and
   timestamp values MUST come from the injected Identifier Port and Clock Port
   (§12's Clock Port and Identifier Port) or from fixed deterministic fixtures.
   **Default construction MUST NOT access system randomness.**
   **Randomness ≠ deterministic fixture.**
6. **Logging (the Logging output category).** Logging is a side effect and is treated as one.
   Root-logger mutation and automatic handler creation are prohibited (§28);
   default console, stdout, or stderr output is prohibited; output through a
   future explicitly injected inert test sink MUST be side-effect declared and
   observable; and no secret or sensitive payload may be logged. **Logging ≠
   harmless side effect** — it is not exempt merely because it invokes no
   provider.
7. **Queues (the Queue or scheduler activity category).** Queue and scheduler
   activity is prohibited at import (§8's queue-and-scheduler prohibition), at
   construction and in every deferred-effect mechanism (§9.1's deferred
   queue-creation mechanism), during default validation, and during any
   attempted execution. The scaffold implements **no** queue inspection and
   **no** queue runtime behavior; it neither creates nor observes a queue.

## 33. Framework identifier handling

1. The scaffold MUST use the canonical closed vocabulary of Runtime §11.1
   exactly: `claude_code`, `openai_agents_sdk`, `langgraph`, `crewai`,
   `autogen`, `mellycore_custom`.
2. There is no `other`, `generic`, or `auto` member, and `custom` is **not** an
   alias for `mellycore_custom`.
3. An unknown value denies with `UNSUPPORTED_FRAMEWORK` (Runtime §33).
4. The scaffold MUST NOT claim empirical support, validation, or compatibility
   for any framework.
5. Being `mellycore_custom` confers no relaxation of any rule in this document.

## 34. Testing contract for future implementation

This section defines **test obligations only**. **No test is created by this
task.**

| # | Obligation | Asserts |
| --- | --- | --- |
| 1 | Import-safety test | Importing every module produces no prohibited side effect |
| 2 | Zero-network test | No socket or connection is attempted (sentinel-patched) |
| 3 | Zero-subprocess test | No process is spawned |
| 4 | Zero-thread test | No thread or worker is created |
| 5 | Zero-filesystem-mutation test | No file or directory is written or created |
| 6 | Zero-secret-access test | No secret, `.env`, or credential source is read |
| 7 | Zero-environment-access test | The environment is not read at import or construction |
| 8 | Zero-provider-call test | No provider request occurs |
| 9 | Zero-model-call test | No model invocation occurs |
| 10 | Zero-framework-import test | No framework SDK is imported on any reachable path |
| 11 | Zero-package-activation test | No package is discovered, installed, or activated |
| 12 | Zero-context-mutation test | No Shared Context read or mutation occurs |
| 13 | Fail-closed execution test | Every execution request refuses, including with all eleven facts satisfied |
| 14 | Deterministic configuration validation | Identical configuration yields identical validation output |
| 15 | Error-owner mapping test | Each surfaced class is owner-defined and correctly attributed |
| 16 | Observability record test | §27's fields are produced; a complete evidence scope yields a Scaffold Zero-Execution Evidence record, an incomplete one yields **`EVIDENCE_INCOMPLETE`** instead, and **never both and never neither** (§27.1) |
| 17 | No-success-outcome test | No execution-success member exists in the outcome vocabulary |
| 18 | **Baseline Inert Invariant test** | **Every row of the §31.1.1 property register**, over a baseline inert composition, each asserted by a side-effect sentinel (§35 technique 3) or a structural check. The test MUST enumerate the register mechanically and **fail if any row is unasserted**; asserting a proper subset does not satisfy this obligation (§31.1 rule 3) |
| 19 | Zero-filesystem-read test | No file, directory listing, package manifest, or metadata file is read at import, construction, or default validation (§8's file-read and directory-scan prohibitions; §32's **Filesystem read** category) |
| 20 | Logging-silence test | Default inert composition writes nothing to stdout, stderr, or any handler; the root logger is unmodified (§28) |
| 21 | Deferred-effect test | No `__post_init__`, lazy or cached property, descriptor, metaclass or class-creation hook, default factory, callable default, dependency factory, finalizer, context-manager entry, or first-method-call path performs any §32 category (§9.1) |
| 22 | Zero-queue test | No in-process, async, worker, or scheduler-backed queue is created, enqueued to, consumed, or processed (§32's **Queue or scheduler activity** category) |
| 23 | Determinism test | Repeated composition and validation yield byte-identical output; no system randomness is accessed; identifiers and timestamps originate only from injected ports or fixed fixtures (§32's **System randomness** and **System clock access** categories) |
| 24 | Injected-component non-inheritance test | A component satisfying a §12 port but lacking §31.2's seven validations is treated as **unavailable**, not present |
| 25 | **Registry and service-locator absence test** | No global registry, singleton, module-level mutable, class-level cache, or service locator is created or written at import, construction, or default validation (§9 rule 3, §11 rule 2; register row 29) |
| 26 | **No-live-Runtime-handle test** | No live Runtime Handle is created and no mutable live-operation state, operation registry, handle table, or cancellation ledger exists (§26 rule 3; register row 32) |
| 27 | **Cancellation selection-order test** | §26's normative selection order is applied deterministically: a malformed reference yields state 4; otherwise, with no injected implementation, state 5 is reached; no outcome implies work was stopped |

Rules:

1. Tests MUST run fully offline.
2. Tests MUST NOT require a framework SDK, provider, credential, or network.
3. Obligation 13 MUST enumerate the fact combinations rather than sampling.
4. **Obligation 18 asserts the §31.1.1 register in full**; obligations 2–12 and
   19–27 assert individual rows of it and do not substitute for it.
5. No obligation may assert §31.1 over a composition containing an injected live
   implementation; §31.2 governs that case and no such composition is authorized
   here.
6. **Register coverage is mechanical, not editorial.** Obligation 18 MUST derive
   its assertion list from §31.1.1 itself, so that adding a register row without
   adding an assertion fails the obligation rather than silently narrowing it.

## 35. Static validation strategy

A later implementation SHOULD be checked using the following techniques, all of
which already exist in this repository and require no new dependency:

1. **Import inspection** — import each module in isolation and assert no
   prohibited effect.
2. **Dependency graph inspection** — assert the package imports only the
   standard library.
3. **Monkeypatched side-effect sentinels** — patch `socket.socket.connect`,
   `socket.create_connection`, process-spawn entry points, and file-write entry
   points with raising sentinels, exactly as `tests/test_provider_adapters.py`
   already does for network access.
4. **Fake ports** — inject in-memory port doubles from a fixtures module.
5. **Deterministic fixtures** — in-memory only, following
   `tests/provider_adapter_fixtures.py`.
6. **Offline test runs** — no network, no credentials, no SDKs.
7. **Source allowlists and prohibited-import checks** — scan the package source
   for prohibited tokens, following the existing precedent that asserts absence
   of `import socket`, `import requests`, `import httpx`, `import urllib`,
   `os.environ`, `os.getenv`, `http://`, and `https://`. The scaffold's list
   SHOULD additionally cover framework SDK module names and `subprocess`,
   `threading`, and `open(`.

**This specification creates none of these checks.**

## 36. Repository allowlist for later implementation

The future expected areas are `scripts/agent_runtime_scaffold/` and the two test
files named in §5. **Naming them here authorizes nothing.**

1. Any later implementation task MUST receive its **own** explicit file
   allowlist and separate Operator approval.
2. A later task MUST NOT modify an owner contract, a review artifact, an
   unrelated package, a dependency manifest, workflow YAML, or any configuration
   file.
3. A later task MUST NOT add a third-party dependency.
4. This specification does not pre-approve any path.

## 37. Security considerations

| # | Threat | Mitigation posture |
| --- | --- | --- |
| 1 | Import-time secret access | Import reads no environment, `.env`, or credential source (§8's dotenv-read and secret-read prohibitions) |
| 2 | Hidden network initialization | No socket, client, or transport is constructed at import or construction (§7 rule 4, §8's socket-and-network prohibition, §9 rule 1) |
| 3 | Dependency side effects | Standard library only; dependency-graph inspection asserts it (§35 technique 2) |
| 4 | Provider auto-discovery | No discovery mechanism exists; providers arrive only by explicit injection (§11 rule 2, §20) |
| 5 | Framework auto-loading | No framework SDK on any reachable import path (§8 rule 4, §17) |
| 6 | Package auto-activation | No discovery, installation, or activation (§16) |
| 7 | Command registration | The scaffold registers no command and enumerates no protected command class (§40) |
| 8 | Hook registration | No global hook, signal handler, or `atexit` handler — **§8's prohibition on registering a global hook, signal handler, or `atexit` handler**, reinforced by §9 rule 3 and threat 15 |
| 9 | Plugin loading | No plugin mechanism, entry-point scan, or dynamic loader (§11 rule 2, §32's **Plugin loading** category) |
| 10 | MCP auto-connection | No connection is created, requested, or implied (§32's **MCP connection** category) |
| 11 | Context leakage | No context is read or projected; observability carries no payload (§18, §27 rule 5) |
| 12 | Unsafe deserialization | No code-executing deserialization of untrusted input (§29 rule 5) |
| 13 | Path traversal | The scaffold performs no filesystem access at all (§32's **Filesystem read** and **Filesystem write** categories) |
| 14 | Subprocess execution | No process creation (§32's **Process creation** category) |
| 15 | Global state mutation | No hidden registration, singleton, module-level mutable, or class-level cache (§9 rule 3, §11 rule 2); asserted by §34 obligation 25 |
| 16 | Logging of sensitive data | No secret, key, or full sensitive payload is logged (§28 rules 3–4) |
| 17 | False-success stubs | No execution-success outcome is representable; a no-op never stands in for a matter-ing operation (§13 rules 1–2) |
| 18 | Test-to-production configuration drift | Test doubles are injected, never defaulted; the invariant is asserted under default configuration (§11 rule 4, §31) |
| 19 | Environment-variable trust | The environment is never read, so it is never trusted — **§8 rule 3**, which prohibits reading `os.environ` or equivalent at import; §10's **implicit environment loading** prohibition; §32's **Environment access** category |
| 20 | **Background work smuggled through a queue** | Queue and scheduler activity is prohibited at import, construction, deferred effects, validation, and execution (§8's queue-and-scheduler prohibition, §9.1's deferred queue-creation mechanism, §32's **Queue or scheduler activity** category), and asserted by §34 obligation 22 |
| 21 | **Executable configuration content** | §10's fourteen executable-content prohibitions bar import-by-string paths, callbacks, serialized callables, dynamic expressions, and shell commands; §30 layer 5 rejects them fail-closed; §7 rule 3 forbids resolving a name to an object |
| 22 | **Deferred-effect bypass of construction safety** | §9.1 binds nineteen deferred mechanisms to §32 exactly as constructors are bound; asserted by §34 obligation 21 |
| 23 | **Injected component treated as inert by interface conformance** | §31.2 requires seven separate validations; an unvalidated component is treated as unavailable; asserted by §34 obligation 24 |
| 24 | **Nondeterminism via system randomness or clock** | §32's **System randomness** and **System clock access** categories prohibit both; identifiers and timestamps come from injected ports or fixed fixtures (§32 rule 5); asserted by §34 obligation 23 |
| 25 | **Unscoped zero-execution claim** | §27.1 makes the evidence record derived, scoped, and non-canonical, and **prohibits any affirmative record whenever evidence is incomplete** — including whenever a §12 port is injected; incompleteness is recorded only as the non-affirmative `EVIDENCE_INCOMPLETE` outcome (§27.1 rules 2–4) |
| 26 | Supply-chain substitution | No third-party dependency; no dynamic import by name; source allowlist checks (§35 technique 7, §36 rule 3) |

## 38. Batch Orchestration boundary

**Batch Orchestration is not specified, implemented, or authorized by this
document.**

The scaffold MUST NOT create a worktree, spawn a parallel agent, execute a batch
plan, mutate a file, push, create a pull request, merge, or deploy. Batch
compatibility is not declared here at all; it remains owned by the future Batch
Orchestration contract (§40).

## 39. Non-goals

1. Scaffold implementation.
2. Agent Runtime implementation.
3. Framework Adapter implementation.
4. Framework SDK installation or execution.
5. Agent Package loader.
6. Provider integration.
7. Model execution.
8. Tool execution.
9. Shared Context Bridge implementation.
10. Context storage, database, or vector-store integration.
11. Memory service.
12. Policy engine.
13. Command runtime.
14. Hook runtime.
15. Plugin runtime.
16. MCP runtime.
17. Batch Orchestration.
18. Run Ledger persistence.
19. Queues, queue processors, schedulers, and background or deferred job
    execution of any kind.
20. Frontend.
21. Backend.
22. Deployment.

## 40. Deferred dependencies

None is started or authorized by this document. Each remains owned by the
document named.

| # | Deferred dependency | Owner | This specification's containment |
| --- | --- | --- | --- |
| 1 | Agent Package `NEW-P2-01` — package-lifecycle rendering field undefined | Agent Package Contract | §16 rule: defines no such field |
| 2 | Agent Package `NEW-P2-02` — contract-version discrepancy | Agent Package Contract | §16 rule 3: asserts no version canonically current |
| 3 | Agent Package `NEW-P2-03` — protected command classes unenumerated | Agent Package Contract / future Command Registry | §37 threat 7: enumerates none |
| 4 | Framework Bridge `NEW-P2-01` — Runtime §16 coverage incl. `normalize_result` | Framework Bridge Contract | §14 rule 2, §25 rule 4: owns no part of it |
| 5 | Framework Bridge `NEW-P2-02` — `PROJECTION_UNSUPPORTED` / `BRIDGE_UNSUPPORTED_BEHAVIOR` overlap | Framework Bridge Contract | §24 rule 4: emits neither, resolves nothing |
| 6 | Framework Bridge `NEW-P2-03` — capability numbering divergence | Framework Bridge / Agent Package Contract | §21 rule 2: semantic names only, no ordinal |
| 7 | Framework Bridge `NEW-P2-04` — validation obligation not wired to eligibility | Framework Bridge Contract | §17 rule 2: no profile is runtime-eligible |
| 8 | Shared Context Bridge `NEW-P2-01` — four owner error neighbours undiscriminated | Shared Context Bridge Contract | §24 rule 5: emits no SCB class, selects among none |
| 9 | Shared Context Bridge `NEW-P2-02` — `INJECTION_SUSPECTED` owner misattributed | Shared Context Bridge Contract | §24 rule 1: cites Gateway §25.2 as owner where relevant |
| 10 | Shared Context Bridge `NEW-P2-03` — proposal lifecycle overlaps Ingestion Gate | Shared Context Bridge Contract | §18 rule 7: defines no lifecycle precedence |
| 11 | Shared Context Bridge `NEW-P2-04` — quarantine/rejection precedence absent | Shared Context Bridge Contract | §18 rule 7: defines no precedence |
| 12 | Shared Context Bridge `NEW-P2-05` — memory scopes unmapped to Runtime §18 | Shared Context Bridge Contract | §18 rule 8: redefines no memory taxonomy |
| 13 | Shared Context Bridge `NEW-P2-06` — envelope overlaps Control Plane `ContextPacket` | Shared Context Bridge / Control Plane | §18 rule 9: replaces no Control Plane entity |
| 14 | Shared Context Bridge `NEW-P2-07` — proposal-replay mitigation unsupported | Shared Context Bridge Contract | §18 rule 10: claims no replay protection |
| 15 | Shared Context Bridge `NEW-P2-08` — "subtractive or equal" unmeasured | Shared Context Bridge Contract | §18 rule 3: never asserted as an implemented property |
| 16 | The six per-framework Framework Adapter specifications | Future, separate tasks | §17: declares a port only |
| 17 | Shared Context runtime implementation | Future, separate task | §18: port and inert records only |
| 18 | Agent Package loader implementation | Future, separate task | §16: no loading |
| 19 | Policy engine implementation | Future, separate task | §22: evaluates no policy |
| 20 | Provider integration | Future, separate task | §20: no connection |
| 21 | Model routing implementation | Future, separate task | §19: no decision |
| 22 | Observability implementation | Future, separate task | §27: information architecture only |
| 23 | Run Ledger persistence | Future, separate task | §12 port 10: interfaces, not persistence |
| 24 | **Agent Runtime Scaffold implementation task** | Future, separate task | This document specifies it; authorizes it not at all |
| 25 | **Agent Runtime Scaffold implementation review** | Future, separate task | Required after the implementation task |
| 26 | Cross-Agent Smoke (inert modes only) | Future, separate task | Not addressed here |
| 27 | Integration Review | Future, separate task | Not addressed here |
| 28 | Future Batch Orchestration contract | Future, separate task | §38: no compatibility declared |

## 41. Acceptance criteria

This specification task is complete when all of the following hold:

1. All 44 sections (§1–§44) are present and each required topic is addressed.
2. Terminology (§2) defines all thirty terms, including the five concepts
   introduced by version 1.1 and the two introduced by version 1.2.
3. No concern is owned by more than one document (§3); every consumed concept
   cites its canonical owner.
4. Agent Runtime Architecture §37's inert v1 boundary is **consumed unchanged**,
   and every rule expressing one of its requirements is an explicitly cited,
   subordinate implementation constraint (§1.1, §3 row 1, §8 rule 4).
5. The scaffold status (§4) states plainly that no scaffold code, runtime,
   adapter, provider connection, framework integration, or package execution
   exists.
6. The future layout (§5) is labeled `NON-NORMATIVE FUTURE LAYOUT — NOT
   IMPLEMENTED` and no file is created.
7. Every module-inventory row (§6) has exactly one responsibility.
8. Importing a module constructs nothing (§7 rules 2 and 4).
9. All nineteen import prohibitions (§8) are stated, including filesystem read,
   directory scanning, non-importing presence probing, logging, queue activity,
   randomness, and clock access.
10. All eight construction-safety rules (§9) are stated, and construction is not
    authorization.
11. All twenty-two configuration prohibitions (§10) are stated; no secret may
    appear in configuration; and **executable content is rejected fail-closed**
    (§10 rule 5, §30 layer 5).
12. No external dependency is resolvable through hidden global state (§11 rule 2).
13. All fourteen ports (§12) are declared, and a declared port implies no
    implementation.
14. The six dispositions (§13) are distinct, and **no execution-success outcome
    is representable**.
15. All sixteen owner-defined operations (§14) carry a scaffold disposition, with
    no eighth context operation and no tenth bridge operation.
16. Every execution request fails closed, across all eleven-fact combinations
    (§15, §31).
17. Package, Framework, Shared Context, Router, and Provider boundaries (§16–§20)
    each keep their canonical owner intact.
18. Capabilities are referenced by semantic name with **no cross-document ordinal**
    (§21).
19. Validation, compatibility, availability, and construction never equal approval
    (§22).
20. No Runtime §12 lifecycle value is invented or extended (§23).
21. Owner error classes are consumed, and no scaffold error duplicates one (§24).
22. No coerced success, and `normalize_result` is not defined or resolved (§25).
23. The five cancellation states (§26) are distinct and none claims a cancellation
    that did not occur.
24. No new Control Plane status dimension is created (§27).
25. Logging is library-safe and never global (§28).
26. All twenty-four side-effect categories (§32) are prohibited in a baseline
    inert composition, including queue activity, logging output, randomness, and
    clock access.
27. The framework vocabulary is the canonical six with no alias (§33).
28. All twenty-seven testing obligations (§34) are stated as obligations only,
    with no test created, and **obligation 18 asserts every row of the §31.1.1
    property register**, deriving its assertion list mechanically so that a
    proper subset fails the obligation.
29. All twenty-six security threats (§37) are addressed with a section-citing
    mitigation.
30. **Open-finding containment holds:** all fifteen upstream P2 findings are
    recorded as deferred, none is resolved, and no normative rule depends on any
    of them (§40).
31. No implementation, source file, test, package, dependency, configuration,
    execution, provider connection, credential, or deployment is created or
    claimed anywhere (§1.4, §4).
32. **§31.1 and §31.2 are separate**: the Baseline Inert Invariant is scoped to a
    baseline inert composition and makes no claim about injected live
    implementations, and no rule asserts it "regardless of injected ports".
33. **Injected components inherit nothing** from interface conformance; §31.2's
    seven validations are required, and an unvalidated component is treated as
    unavailable.
34. **Queue and scheduler activity is prohibited** at import, construction,
    deferred effects, validation, and execution, and is represented in §8, §9.1,
    §32, §31.1, §34, §37, and §39.
35. **Scaffold Zero-Execution Evidence** (§27.1) is derived, correlation-scoped,
    explicitly non-canonical, never a Runtime result, never a status dimension,
    **affirmative-only** — emitted solely when its evidence scope is complete,
    with `EVIDENCE_INCOMPLETE` recorded in its place otherwise — and fabricates
    no run identifier.
36. **Deferred effects cannot bypass construction safety**: all nineteen §9.1
    mechanisms are bound by §32.
37. **Cancellation is deterministic** (§26): the normative selection order fixes
    a single applicable state, the inert default is *implementation
    unavailable*, unreachable outcomes are named, no mutable live-operation
    state is created, and §14's disposition states the same rule.
38. **Logging and randomness are treated as side effects** (§32's **Logging
    output** and **System randomness** categories, rules 5–6), not as harmless
    operations.
39. Every cross-document reference to the owner's inert boundary is written in
    full as "Agent Runtime Architecture §37"; a bare `§37` denotes only this
    document's own §37 (§1.1).
40. **The current version is coherent** (§44.1): the document header, §44 rule
    1, and the version-history table identify the same
    `runtime_scaffold_spec_version`, and no other location restates it as a
    literal.
41. **Cross-references to table contents are semantic, not positional**: no
    normative citation depends on a mutable table row number, so inserting or
    reordering a row cannot invalidate it.

## 42. Document metrics (normative)

Every count below was computed directly from this document's own sections. A
future amendment that changes a table MUST recompute and restate the
corresponding row; a divergence between this table and its section is a defect in
this document, following the discipline of
`[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` §1.4,
`[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` §1.4, and
`[[MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001]]` §48.

| Dimension | Count | Authoritative section |
| --- | --- | --- |
| Specification sections | 44 | §1–§44 |
| Terminology entries | 30 | §2 |
| Architectural ownership rows | 26 | §3 |
| Scaffold status statements | 8 | §4 |
| Module inventory rows | 10 | §6 |
| Composition-root rules | 7 | §7 |
| Import-safety prohibitions | 19 | §8 |
| Construction-safety rules | 8 | §9 |
| Deferred-effect mechanisms | 19 | §9.1 |
| Configuration prohibitions | 22 | §10 |
| Dependency-injection rules | 6 | §11 |
| Runtime ports | 14 | §12 |
| No-op / fail-closed dispositions | 6 | §13 |
| Operation-coverage rows | 16 | §14 |
| Package prohibitions | 8 | §16 |
| Framework Bridge prohibitions | 8 | §17 |
| Shared Context Bridge prohibitions | 10 | §18 |
| Cancellation states | 5 | §26 |
| Observability fields | 12 | §27 |
| Zero-execution evidence properties | 8 | §27.1 |
| Logging rules | 7 | §28 |
| Validation layers | 10 | §30 |
| **Baseline Inert Invariant register properties** | **32** | **§31.1.1** |
| Injected-component validations | 7 | §31.2 |
| Side-effect categories | 24 | §32 |
| Testing obligations | 27 | §34 |
| Static validation techniques | 7 | §35 |
| Security threats | 26 | §37 |
| Non-goals | 22 | §39 |
| Deferred dependencies | 28 | §40 |
| Acceptance criteria | 41 | §41 |
| Version-history entries | 3 | §44.1 |

## 43. References

### 43.1 Repository (canonical)

- `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` — §8.1 identifier
  catalogue; §8.3 canonical serialization and digests; §10.1 package metadata;
  §11.1 closed framework set; §12 run lifecycle; §14 eleven authorization facts;
  §16 nine bridge operations; §17.1 seven context operations; §21 tool access;
  §22 provider access; §23 model routing; §25 run ledger; §26 event model; §27
  cancellation; §33 error taxonomy; §34 observability; §36 runtime modes;
  **Agent Runtime Architecture §37 — the inert v1 boundary**; §40 implementation
  sequence
- `[[MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_001]]` — package identity, declared
  capabilities, §21 error taxonomy
- `[[../research/MELLYCORE_AGENT_PACKAGE_CONTRACT_SPEC_REVIEW_002]]` (research)
- `[[MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_001]]` — §23.3 bridge-owned classes
- `[[../research/MELLYCORE_FRAMEWORK_BRIDGE_CONTRACT_SPEC_REVIEW_001]]` (research)
- `[[MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_001]]` — context exchange
  boundary
- `[[../research/MELLYCORE_SHARED_CONTEXT_BRIDGE_CONTRACT_SPEC_REVIEW_001]]`
  (research)
- `[[MELLYCORE_OMNIROUTER_INSPIRED_CONTROL_PLANE_SPEC]]` — §7.1 common entity
  contract; §8.1 six status dimensions; §9.3 context entities; §16 approvals
- `[[MELLYCORE_PROVIDER_REGISTRY_CONTRACT_EXTENSION_SPEC_001]]` — §21.1 eight
  provider facts; §24 MCP records
- `[[MELLYCORE_INTEGRATION_GATEWAY_SECURITY_CONTRACT_SPEC_001]]` — §12 capability
  resolution; §17 policy order; §18 approval binding; §25.2 class table
- `[[MELLYCORE_AI_OPERATIONS_INTELLIGENCE_SPEC_001]]` — §5 ledger and evidence
- `[[MELLYCORE_OPERATIONS_DATA_CONTRACT_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_PROVENANCE_AND_SENSITIVITY_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_GATE_IMPLEMENTATION_SPEC_001]]`
- `[[MELLYCORE_CONTEXT_INGESTION_GATE_SPEC_001]]`
- `[[../decisions/MELLYCORE_AGENT_RUNTIME_CANONICAL_SEAM_DECISION_001]]`
- `shared_context/CONTEXT_GRAPH_SCHEMA.md`,
  `shared_context/CONTEXT_PACK_GENERATOR_SPEC.md`
- `shared_context/MODEL_ROUTING.md`
- `shared_context/SAFETY_CONTRACT.md`, `PROJECT_STATE.md`, `ROADMAP.md`,
  `RUN_QUEUE.md`, `AGENT_HANDOFF.md`, `PROJECT_HISTORY.md`, `TASK_INDEX.md`
- Repository convention evidence, inspected read-only and unmodified:
  `scripts/provider_adapters/` (the accepted inert-scaffold precedent cited by
  Agent Runtime Architecture §37), `tests/test_provider_adapters.py`,
  `tests/provider_adapter_fixtures.py`

### 43.2 External

**None.** No external standard, SDK, API, framework, package index, or online
documentation was consulted or is claimed.

## 44. Amendment and supersession

1. This document may be amended only additively unless a major
   `runtime_scaffold_spec_version` bump is explicitly declared. That version
   identifier names the version of **this specification document** — currently
   **`1.2`**, as recorded authoritatively in §44.1 — and is not a context,
   package, or bridge contract version.
   **§44.1 is the single source of truth for the current version.** An amendment
   MUST update §44.1 and the document header together, and MUST NOT restate the
   current version anywhere else as a literal that could fall out of step.
2. An amendment MUST recompute and restate §42's document metrics.
3. An amendment MUST NOT weaken any rule in §3.1's precedence chain.
4. An amendment MUST NOT resolve, restate, or work around any deferred
   dependency of §40 that belongs to another owner. **Silent modification of an
   owner contract's meaning through this document is prohibited.**
5. A change that would add a runtime operation, a `run_state` value, an
   authorization fact, a memory category, a framework member, a sensitivity
   level, a graph relation type, or a Control Plane dimension is **not** an
   amendment to this document — it belongs to that concept's owner and requires
   that owner's own separately reviewed amendment.
6. **A change to Agent Runtime Architecture §37's inert v1 boundary is not an
   amendment to this document.** Agent Runtime Architecture §37 is consumed
   unchanged; altering it requires an amendment to
   `[[MELLYCORE_AGENT_RUNTIME_ARCHITECTURE_SPEC_001]]` under its own review.
7. This document does not supersede, rename, or absorb any canonical owner
   document cited in §3 or §43.1; every citation remains that document's
   unmodified, unweakened text unless a separate, explicitly authorized
   amendment task states otherwise.

### 44.1 Version history (authoritative)

`runtime_scaffold_spec_version` is **`1.2`**. This table is the single source of
truth for that value; §44 rule 1 cites it rather than duplicating it.

| Version | Task | Change class | Review outcome |
| --- | --- | --- | --- |
| `1.0` | `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-001` | Initial specification | `AGENT_RUNTIME_SCAFFOLD_SPECIFIED_UNVERIFIED`, then Review 001 `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 7 / P3 5) |
| `1.1` | `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-001` | **Compatible corrective increment** — resolved all twelve Review 001 findings; added §9.1, §27.1, §31.1, §31.2 and additional prohibitions, categories, and obligations | Review 002 `PASS_WITH_NON_BLOCKING_FINDINGS` (P0 0 / P1 0 / P2 1 / P3 6) |
| **`1.2`** | `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REMEDIATION-002` | **Compatible corrective increment** — resolved the one P2 and six P3 findings of Review 002 | **Unverified**, pending `MELLYCORE-AGENT-RUNTIME-SCAFFOLD-SPEC-REVIEW-003` |

**Version 1.2 change classification against rule 1.** Version 1.2 is a
compatible corrective increment and **no major bump is required**, because every
change is one of: a citation correction with no normative effect (§37 threats 8
and 19, §43.1); an **addition** of testing obligations and asserted properties
(§34, §34.1); or the resolution of an internal contradiction **toward the
stricter branch** (§27.1's incomplete-evidence model, §14 and §26's cancellation
default). **No prohibition, boundary, port, disposition, category, or owner
constraint is removed, narrowed, or made more permissive**, and no rule in
§3.1's precedence chain is weakened (rule 3). No deferred dependency of §40 is
resolved (rule 4). No owner-owned concept is added or altered (rules 5–6). All
twelve Review 001 closures are preserved.
