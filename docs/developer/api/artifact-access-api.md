# Artifact Access API

## Overview

The Artifact Access API is the platform interface used to retrieve published Artifact Packages from Artifact Storage.

It provides transport-independent access to immutable published artifacts and abstracts the underlying storage implementation.

The API is consumed by the Artifact Manager and other platform components that require access to published Artifact Packages.

---

# Purpose

The Artifact Access API enables platform services to:

* Retrieve published Artifact Packages.
* Verify artifact availability.
* Verify artifact integrity.
* Resolve artifact references contained in Build Manifests.

The API does not expose storage implementation details.

---

# Architectural Role

The Artifact Access API provides:

* Artifact retrieval.
* Artifact discovery.
* Artifact integrity verification.

The API does not:

* Build software.
* Publish artifacts.
* Modify artifacts.
* Delete artifacts.
* Manage retention policy.

These responsibilities remain with the Builder and Artifact Storage.

---

# Consumers

The Artifact Access API is consumed by:

| Consumer         | Purpose                                                        |
| ---------------- | -------------------------------------------------------------- |
| Artifact Manager | Retrieve Artifact Packages for Execution Directory preparation |

Additional consumers may be introduced without changing the interface contract.

---

# Operations

The Artifact Access API provides the following logical operations:

| Operation         | Description                                           |
| ----------------- | ----------------------------------------------------- |
| Resolve Artifact  | Resolve an artifact reference.                        |
| Retrieve Artifact | Retrieve a published Artifact Package.                |
| Verify Integrity  | Verify the integrity of a published Artifact Package. |

Transport protocols are implementation decisions.

---

# Inputs

Typical inputs include:

* Build Identity
* Artifact identifier
* Artifact reference

Input representation is implementation-defined.

---

# Outputs

Typical outputs include:

* Artifact Package
* Artifact metadata
* Integrity verification status

Artifact Packages remain immutable after publication.

---

# Error Handling

The Artifact Access API reports conditions such as:

* Artifact not found.
* Integrity verification failure.
* Artifact unavailable.
* Authorization failure (if applicable).

Errors never modify published artifacts.

---

# Design Principles

The Artifact Access API should be:

* Read-only.
* Stateless.
* Transport independent.
* Versioned.
* Backward compatible whenever practical.

The API should expose logical artifact operations rather than storage implementation details.

---

# Observability

Platform services publish telemetry describing:

* Artifact retrieval requests.
* Retrieval latency.
* Retrieval failures.
* Integrity verification.
* Service health.

Telemetry supports observability but is not part of the API contract.

---

# Relationship to Platform Services

The Builder publishes Artifact Packages.

Artifact Storage becomes the authoritative owner of published Artifact Packages.

The Artifact Access API provides read-only access to those published artifacts.

The Artifact Manager consumes the API to prepare Execution Directories.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/services/artifact-storage.md`
* `docs/developer/services/artifact-manager.md`

## Related ADRs

* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
* ADR-0020 — Data Classification
