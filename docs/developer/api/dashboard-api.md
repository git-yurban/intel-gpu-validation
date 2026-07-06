# Dashboard API

## Overview

The Dashboard API provides read-only access to platform information presented by the Dashboard.

It enables external tools and user interfaces to retrieve operational information without directly accessing internal platform services.

The Dashboard API is a presentation interface and does not own platform data.

---

# Purpose

The Dashboard API enables consumers to:

* Retrieve platform status.
* Retrieve validation summaries.
* Retrieve Worker Host summaries.
* Retrieve operational metrics.
* Retrieve dashboard views.

The API is intended for presentation and integration purposes.

---

# Architectural Role

The Dashboard API provides:

* Read-only presentation data.
* Aggregated operational views.
* Dashboard-oriented information.

The API does not:

* Modify Operational State.
* Schedule validation.
* Execute validation workloads.
* Manage platform services.

---

# Consumers

The Dashboard API may be consumed by:

| Consumer                 | Purpose                      |
| ------------------------ | ---------------------------- |
| User interfaces          | Display platform information |
| External reporting tools | Retrieve summaries           |
| Integration systems      | Consume dashboard data       |

---

# Operations

The Dashboard API provides the following logical operations:

| Operation                   | Description                         |
| --------------------------- | ----------------------------------- |
| Retrieve Platform Status    | Obtain overall platform status.     |
| Retrieve Validation Summary | Obtain validation summaries.        |
| Retrieve Worker Summary     | Obtain Worker Host summaries.       |
| Retrieve Dashboard Views    | Obtain dashboard presentation data. |

Transport protocols are implementation decisions.

---

# Inputs

Typical inputs include:

* Query parameters
* Filters
* Time ranges

Input representation is implementation-defined.

---

# Outputs

Typical outputs include:

* Platform summaries
* Validation summaries
* Worker summaries
* Dashboard presentation data

All outputs are read-only.

---

# Error Handling

The Dashboard API reports conditions such as:

* Requested information unavailable.
* Invalid query.
* Authorization failure (if applicable).

Errors never modify platform data.

---

# Design Principles

The Dashboard API should be:

* Read-only.
* Stateless.
* Presentation focused.
* Transport independent.
* Backward compatible whenever practical.

The Dashboard API presents information but never becomes the authoritative owner of it.

---

# Observability

Platform services publish telemetry describing:

* Dashboard queries.
* Query latency.
* Dashboard availability.
* API health.

Telemetry supports observability but is not part of the API contract.

---

# Relationship to Platform Services

The Dashboard consumes Operational State and telemetry.

The Dashboard API exposes presentation-oriented views of that information to external consumers.

The Dashboard API never bypasses the ownership boundaries established by the platform architecture.

---

# Related Documentation

* `docs/developer/services/dashboard.md`
* `docs/developer/services/operational-database.md`
* `docs/developer/platform/telemetry.md`

## Related ADRs

* ADR-0021 — Telemetry and Observability
* ADR-0022 — Dashboard as a Read-Only Platform Service
