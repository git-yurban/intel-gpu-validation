# Operational Query API

## Overview

The Operational Query API is the platform interface used to retrieve Operational State.

It provides read-only access to the current and historical operational information maintained by the Operational Database.

The API abstracts the storage implementation from its consumers.

---

# Purpose

The Operational Query API enables platform services and user interfaces to:

* Retrieve Worker Host information.
* Retrieve Worker Capability.
* Retrieve validation execution state.
* Retrieve validation results.
* Retrieve operational history.

The API does not expose database implementation details.

---

# Architectural Role

The Operational Query API provides read-only access to mutable Operational State.

The API does not:

* Modify Operational State.
* Publish validation results.
* Execute validation workloads.
* Schedule validation.

These responsibilities remain with other platform services.

---

# Consumers

The Operational Query API is consumed by:

| Consumer         | Purpose                    |
| ---------------- | -------------------------- |
| Dashboard        | Display platform status    |
| Scheduler        | Retrieve Worker Capability |
| Platform tooling | Query Operational State    |

Additional consumers may be introduced without changing the interface contract.

---

# Operations

The Operational Query API provides the following logical operations:

| Operation                   | Description                    |
| --------------------------- | ------------------------------ |
| Retrieve Worker Hosts       | Query registered Worker Hosts. |
| Retrieve Worker Capability  | Query Worker Capabilities.     |
| Retrieve Validation Status  | Query execution state.         |
| Retrieve Validation Results | Query validation results.      |

Transport protocols are implementation decisions.

---

# Inputs

Typical inputs include:

* Worker Host identifier
* Validation identifier
* Build Identity
* Query parameters

Input representation is implementation-defined.

---

# Outputs

Typical outputs include:

| Output                  | Description                  |
| ----------------------- | ---------------------------- |
| Worker Host information | Current Operational State    |
| Worker Capability       | Current Operational State    |
| Validation status       | Current Operational State    |
| Validation results      | Historical Operational State |

Operational State remains mutable.

---

# Error Handling

The Operational Query API reports conditions such as:

* Resource not found.
* Invalid query.
* Query unavailable.
* Authorization failure (if applicable).

Queries never modify Operational State.

---

# Design Principles

The Operational Query API should be:

* Read-only.
* Stateless.
* Transport independent.
* Versioned.
* Backward compatible whenever practical.

The API exposes Operational State rather than database implementation details.

---

# Observability

Platform services publish telemetry describing:

* Query requests.
* Query latency.
* Query failures.
* Service health.

Telemetry supports observability but is not part of the API contract.

---

# Relationship to Platform Services

Validation Workers publish validation results.

The Operational Database stores Operational State.

The Operational Query API provides read-only access to that state.

The Dashboard and Scheduler consume the API without becoming authoritative owners of Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/services/operational-database.md`
* `docs/developer/services/dashboard.md`

## Related ADRs

* ADR-0010 — Operational Database
* ADR-0017 — Worker Capability Model
* ADR-0020 — Data Classification
* ADR-0022 — Dashboard as a Read-Only Platform Service
