# Artifact Manager API

## Overview

The Artifact Manager API is the platform interface used to prepare an Execution Directory from a published Build.

It retrieves immutable Artifact Packages through the Artifact Access API, assembles the files required for execution, and returns an Execution Directory Reference.

The API abstracts artifact retrieval and execution directory preparation from its consumers.

---

# Purpose

The Artifact Manager API enables platform services to:

* Prepare an Execution Directory for a published Build.
* Resolve Build Manifest references.
* Verify artifact integrity before execution.
* Obtain an Execution Directory Reference.

The API does not expose the implementation of execution directory preparation.

---

# Architectural Role

The Artifact Manager API provides:

* Execution Directory preparation.
* Build resolution.
* Artifact assembly.

The API does not:

* Build software.
* Publish Artifact Packages.
* Schedule validation workloads.
* Execute validation workloads.

These responsibilities remain with other platform services.

---

# Consumers

The Artifact Manager API is consumed by:

| Consumer  | Purpose                                       |
| --------- | --------------------------------------------- |
| Scheduler | Request preparation of an Execution Directory |

Additional consumers may be introduced without changing the interface contract.

---

# Operations

The Artifact Manager API provides the following logical operations:

| Operation                              | Description                                                      |
| -------------------------------------- | ---------------------------------------------------------------- |
| Prepare Execution Directory            | Prepare an Execution Directory for a published Build.            |
| Retrieve Execution Directory Reference | Return a reference identifying the prepared Execution Directory. |

Transport protocols are implementation decisions.

---

# Inputs

Typical inputs include:

* Build Identity
* Build Manifest reference

Input representation is implementation-defined.

---

# Outputs

Typical outputs include:

| Output                        | Description                                  |
| ----------------------------- | -------------------------------------------- |
| Execution Directory Reference | Identifies the prepared Execution Directory. |

The Execution Directory itself remains a transient execution resource.

---

# Error Handling

The Artifact Manager API reports conditions such as:

* Build not found.
* Artifact unavailable.
* Artifact integrity verification failure.
* Execution Directory preparation failure.

Errors never modify published Artifact Packages.

---

# Design Principles

The Artifact Manager API should be:

* Stateless.
* Transport independent.
* Versioned.
* Deterministic.
* Backward compatible whenever practical.

The API exposes preparation of execution resources rather than their internal representation.

---

# Observability

Platform services publish telemetry describing:

* Preparation requests.
* Preparation latency.
* Artifact retrieval.
* Preparation failures.
* Service health.

Telemetry supports observability but is not part of the API contract.

---

# Relationship to Platform Services

The Scheduler requests preparation of an Execution Directory.

The Artifact Manager retrieves published Artifact Packages through the Artifact Access API.

The Artifact Manager returns an Execution Directory Reference.

The Validation Worker later consumes that reference as part of validation execution.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/services/artifact-manager.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/api/artifact-access-api.md`

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0011 — Execution Environment Isolation
* ADR-0020 — Data Classification
