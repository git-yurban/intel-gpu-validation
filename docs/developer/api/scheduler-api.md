# Scheduler API

## Overview

The Scheduler API is the platform interface used to submit validation requests for execution.

It accepts validation requests, coordinates scheduling, and initiates the validation lifecycle by producing a Worker Manifest for an eligible Worker Host.

The API abstracts scheduling policy and execution coordination from its consumers.

---

# Purpose

The Scheduler API enables platform services and external automation to:

* Submit validation requests.
* Initiate validation scheduling.
* Obtain a scheduling result.

The API does not expose scheduling implementation details.

---

# Architectural Role

The Scheduler API provides:

* Validation request submission.
* Scheduling initiation.
* Scheduling acknowledgement.

The API does not:

* Prepare Execution Directories.
* Select Worker Hosts directly.
* Execute validation workloads.
* Return validation results.

Those responsibilities remain with other platform components.

---

# Consumers

The Scheduler API is consumed by:

| Consumer                       | Purpose                    |
| ------------------------------ | -------------------------- |
| Platform automation            | Submit validation requests |
| External orchestration systems | Submit validation requests |

Additional consumers may be introduced without changing the interface contract.

---

# Operations

The Scheduler API provides the following logical operations:

| Operation                  | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| Submit Validation Request  | Submit a validation request for scheduling.                     |
| Retrieve Scheduling Status | Retrieve the current scheduling status for a submitted request. |

Transport protocols are implementation decisions.

---

# Inputs

Typical inputs include:

* Validation Request
* Build Identity
* Validation requirements
* Scheduling options

Input representation is implementation-defined.

---

# Outputs

Typical outputs include:

| Output                     | Description                                      |
| -------------------------- | ------------------------------------------------ |
| Scheduling acknowledgement | Confirms acceptance or rejection of the request. |
| Scheduling status          | Indicates the progress of scheduling.            |

The Worker Manifest is an internal Architectural Contract and is not returned through this interface.

---

# Error Handling

The Scheduler API reports conditions such as:

* Invalid validation request.
* Unknown Build Identity.
* Unsatisfiable validation requirements.
* Scheduling unavailable.

Errors never modify immutable Architectural Contracts.

---

# Design Principles

The Scheduler API should be:

* Stateless.
* Transport independent.
* Versioned.
* Deterministic.
* Backward compatible whenever practical.

The API exposes scheduling as a platform capability rather than exposing Scheduler implementation details.

---

# Observability

Platform services publish telemetry describing:

* Validation request submission.
* Scheduling latency.
* Scheduling outcomes.
* Scheduling failures.
* Service health.

Telemetry supports observability but is not part of the API contract.

---

# Relationship to Platform Services

The Scheduler API accepts validation requests.

The Scheduler coordinates capability matching, requests an Execution Directory from the Artifact Manager, selects an eligible Worker Host, creates a Worker Manifest, and publishes it to the Transient Work Queue.

The Validation Worker later consumes the Worker Manifest to execute the validation workload.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/platform/scheduling.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/api/artifact-manager-api.md`

## Related ADRs

* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
* ADR-0023 — Configuration over Customization
