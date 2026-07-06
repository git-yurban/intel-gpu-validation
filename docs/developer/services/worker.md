# Validation Worker

## Overview

The Validation Worker is a stateless platform service responsible for executing validation workloads.

It consumes immutable Worker Manifests, resolves Execution Directory References, prepares isolated Execution Environments, executes validation workloads, and publishes validation results.

The Validation Worker owns transient execution resources but does not own persistent platform state.

---

# Responsibilities

The Validation Worker is responsible for:

* Receiving Worker Manifests.
* Resolving Execution Directory References.
* Preparing isolated Execution Environments.
* Executing validation workloads.
* Collecting validation results.
* Publishing validation results.
* Cleaning up transient execution resources.

The Validation Worker's architectural responsibility ends after publishing validation results and completing cleanup of transient execution resources.

---

# Architectural Responsibilities

The Validation Worker owns:

* Validation execution
* Execution Environment preparation
* Execution Environment lifecycle
* Transient execution resources

The Validation Worker does not own:

* Build generation
* Artifact persistence
* Execution Directory preparation
* Validation scheduling
* Operational State

These responsibilities belong to other platform services.

---

# Dependencies

The Validation Worker depends on:

* Transient Work Queue
* Artifact Manager
* Operational Database

The Validation Worker consumes:

* Worker Manifest
* Execution Directory Reference

The Validation Worker publishes validation results to the Operational Database.

---

# Inputs

The Validation Worker consumes:

| Input                         | Classification                   |
| ----------------------------- | -------------------------------- |
| Worker Manifest               | Immutable Architectural Contract |
| Execution Directory Reference | Transient platform reference     |

---

# Outputs

The Validation Worker produces:

| Output             | Classification            |
| ------------------ | ------------------------- |
| Validation Results | Mutable Operational State |
| Telemetry          | Operational telemetry     |

Execution Environments, Execution Directories, Worker Artifact Caches, and temporary files remain transient execution resources and are never published.

---

# Execution Workflow

```text id="n08uix"
Transient Work Queue
        │
Receive Worker Manifest
        │
        ▼
Validation Worker
        │
Resolve Execution Directory Reference
        │
        ▼
Artifact Manager
        │
Access Execution Directory
        ▼
Validation Worker
        │
Prepare Execution Environment
        │
Execute Validation Workload
        │
Collect Validation Results
        │
Publish Results
        ▼
Operational Database
```

Publishing validation results marks the completion of validation execution.

Transient execution resources are removed during cleanup.

---

# Service Boundaries

The Validation Worker communicates using immutable Architectural Contracts, transient platform references, and mutable Operational State.

It never:

* Builds software.
* Stores Artifact Packages.
* Creates Execution Directories.
* Schedules validation.
* Owns Operational State.

The Validation Worker is intentionally isolated from scheduling and build generation.

---

# Failure Handling

If validation execution fails:

* Validation results record the failure.
* Transient execution resources are cleaned up.
* Execution Environments are destroyed.
* The failure is reported as Operational State.

Cleanup is performed regardless of validation outcome.

---

# Scalability

Validation Workers are designed to scale independently.

Each Worker Host runs a single Validation Worker.

Platform throughput increases by adding additional Worker Hosts.

Validation Workers remain stateless and independently deployable.

---

# Observability

The Validation Worker publishes telemetry describing:

* Worker lifecycle events
* Validation execution
* Execution duration
* Validation failures
* Cleanup operations
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/services/artifact-manager.md`

## Related ADRs

* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0011 — Execution Environment Isolation
* ADR-0012 — Stateless Workers
* ADR-0016 — Worker Host Identification
* ADR-0017 — Worker Capability Model
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
