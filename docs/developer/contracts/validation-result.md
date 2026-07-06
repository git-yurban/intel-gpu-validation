# Validation Request

## Overview

A Validation Request is the Architectural Contract that describes a validation workload to be scheduled and executed.

It identifies the Build to validate, specifies the validation requirements, and provides the information required for the Scheduler to coordinate execution.

A Validation Request is immutable after submission.

---

# Purpose

A Validation Request enables the platform to:

* Request validation of a published Build.
* Describe validation requirements.
* Initiate the scheduling process.
* Decouple validation intent from execution.

A Validation Request describes **what** should be validated, not **where** or **how** it will execute.

---

# Architectural Role

A Validation Request provides:

* Build Identity.
* Validation requirements.
* Execution constraints.
* Request metadata.

A Validation Request does not:

* Select a Worker Host.
* Describe Worker Capabilities.
* Reference an Execution Directory.
* Define execution results.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component                     | Responsibility             |
| ----------------------------- | -------------------------- |
| Client or Platform Automation | Create Validation Request  |
| Scheduler                     | Consume Validation Request |
| Scheduler                     | Create Worker Manifest     |

The creator is the authoritative source of the Validation Request.

The Scheduler never modifies a submitted Validation Request.

---

# Lifecycle

```text id="w5k2ta"
Client
      │
Create Validation Request
      │
Submit
      ▼
Scheduler
      │
Capability Matching
      │
Create Worker Manifest
```

The Validation Request remains immutable throughout its lifecycle.

---

# Request Contents

A Validation Request should describe:

* Build Identity.
* Validation suite or workload.
* Validation requirements.
* Execution constraints.
* Request metadata.

The exact serialization format is implementation-defined.

---

# Build Reference

A Validation Request references a Build using its Build Identity.

It does not reference:

* Artifact Packages.
* Build Manifest contents.
* Execution Directories.

Resolution of the Build is performed by the Scheduler and Artifact Manager.

---

# Immutability

Validation Requests are immutable.

After submission:

* Build Identity never changes.
* Validation requirements never change.
* Execution constraints never change.

Any modification requires creation of a new Validation Request.

---

# Versioning

Validation Requests should support versioning.

Versioning enables:

* Backward compatibility.
* Forward evolution.
* Independent platform upgrades.

Versioning strategy is implementation-defined.

---

# Design Principles

Validation Requests should be:

* Immutable.
* Declarative.
* Self-contained.
* Deterministic.
* Versioned.

The request should describe validation intent without embedding scheduling or execution decisions.

---

# Relationship to Platform Services

Platform automation or clients create Validation Requests.

The Scheduler consumes Validation Requests to coordinate execution.

The Scheduler produces a Worker Manifest describing the scheduled execution.

Validation Workers never consume Validation Requests directly.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/contracts/build-manifest.md`
* `docs/developer/contracts/worker-manifest.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/platform/scheduling.md`

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0018 — Capability-Based Scheduling
* ADR-0020 — Data Classification
