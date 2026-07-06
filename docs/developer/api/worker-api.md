# Worker API

## Overview

The Worker API defines the architectural interface exposed by a Validation Worker for operational management.

Validation execution is initiated through Worker Manifests published to the Transient Work Queue rather than through direct API invocation.

The Worker API supports lifecycle management and operational integration but is not part of the validation execution path.

---

# Purpose

The Worker API enables platform management to:

* Determine Worker availability.
* Determine Worker health.
* Manage Worker lifecycle.
* Retrieve Worker status.

Validation execution is intentionally excluded from this interface.

---

# Architectural Role

The Worker API provides:

* Health information.
* Operational status.
* Lifecycle management.

The API does not:

* Execute validation workloads.
* Receive validation requests.
* Schedule validation.
* Prepare Execution Directories.

Those responsibilities remain elsewhere in the platform.

---

# Consumers

The Worker API may be consumed by:

| Consumer              | Purpose              |
| --------------------- | -------------------- |
| Platform operations   | Worker management    |
| Deployment automation | Lifecycle management |
| Monitoring systems    | Health monitoring    |

---

# Operations

The Worker API provides the following logical operations:

| Operation              | Description                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| Retrieve Worker Status | Obtain current operational status.                                  |
| Retrieve Worker Health | Determine service health.                                           |
| Drain Worker           | Prevent new workloads while allowing current execution to complete. |
| Resume Worker          | Allow new workloads to be assigned.                                 |

Transport protocols are implementation decisions.

---

# Inputs

Typical inputs include:

* Worker Host identifier
* Lifecycle commands

Input representation is implementation-defined.

---

# Outputs

Typical outputs include:

* Worker status
* Worker health
* Lifecycle acknowledgement

The Worker API never returns validation results directly.

---

# Error Handling

The Worker API reports operational conditions such as:

* Worker unavailable.
* Invalid lifecycle request.
* Worker already draining.

Errors never affect running validation workloads.

---

# Design Principles

The Worker API should be:

* Stateless.
* Transport independent.
* Operationally focused.
* Backward compatible whenever practical.

Validation execution remains driven by Worker Manifests rather than API requests.

---

# Observability

Platform services publish telemetry describing:

* Worker lifecycle.
* Health.
* API requests.
* Lifecycle changes.

Telemetry supports observability but is not part of the API contract.

---

# Relationship to Platform Services

Validation Workers consume Worker Manifests from the Transient Work Queue.

The Worker API exists solely for operational management and is not part of the scheduling or execution pipeline.

---

# Related Documentation

* `docs/developer/services/worker.md`
* `docs/developer/platform/execution-environment.md`

## Related ADRs

* ADR-0012 — Stateless Workers
* ADR-0016 — Worker Host Identification
* ADR-0021 — Telemetry and Observability
