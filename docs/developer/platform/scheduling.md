# Scheduling

## Overview

Scheduling is the platform capability responsible for coordinating validation workloads across available Worker Hosts.

The scheduling process evaluates validation requirements, identifies eligible Worker Hosts using the Capability Model, prepares execution resources, selects an execution target, and produces a Worker Manifest.

Scheduling is a shared platform capability rather than a platform service.

---

# Purpose

Scheduling enables the platform to:

* Coordinate validation execution.
* Match validation workloads to eligible Worker Hosts.
* Support heterogeneous hardware and software environments.
* Maximize platform utilization.
* Preserve deterministic execution.

Scheduling determines **where** a workload executes, not **how** it executes.

---

# Architectural Role

Scheduling provides:

* Validation workload coordination.
* Capability-based Worker Host selection.
* Execution resource coordination.
* Worker Manifest generation.

Scheduling does not:

* Build software.
* Prepare Execution Directories.
* Execute validation workloads.
* Store Operational State.

Those responsibilities remain with the appropriate platform services.

---

# Participants

| Component            | Responsibility              |
| -------------------- | --------------------------- |
| Scheduler            | Coordinate scheduling       |
| Artifact Manager     | Prepare Execution Directory |
| Operational Database | Provide Worker Capability   |
| Validation Worker    | Execute assigned workload   |

Each participant performs a single architectural responsibility.

---

# Scheduling Lifecycle

```text id="r9x4mk"
Validation Request
        │
Determine Requirements
        │
        ▼
Capability Matching
        │
        ▼
Eligible Worker Hosts
        │
Request Execution Directory
        │
        ▼
Artifact Manager
        │
Execution Directory Reference
        │
        ▼
Select Worker Host
        │
Create Worker Manifest
        │
Publish Worker Manifest
        │
        ▼
Transient Work Queue
        │
        ▼
Validation Worker
```

Publishing the Worker Manifest completes the scheduling process.

---

# Capability Matching

Scheduling compares validation workload requirements against published Worker Capabilities.

Only Worker Hosts satisfying all required capabilities are considered eligible for execution.

Capability matching determines eligibility.

Scheduling policy determines selection.

---

# Scheduling Policy

Scheduling policy selects one Worker Host from the eligible candidates.

Examples of scheduling considerations include:

* Worker availability
* Queue depth
* Platform utilization
* Administrative policy

Scheduling policy is configurable and independent of the Capability Model.

---

# Design Principles

Scheduling should be:

* Deterministic
* Capability-driven
* Scalable
* Independent of execution
* Independent of build generation

Scheduling coordinates platform services without assuming their responsibilities.

---

# Failure Handling

If scheduling cannot complete:

* No Worker Manifest is published.
* No Validation Worker is assigned.
* Validation execution does not begin.
* The failure is recorded as Operational State.

Scheduling failures do not affect published Builds or Artifact Packages.

---

# Scalability

Scheduling is designed to support growth in:

* Validation workload volume.
* Worker Host count.
* Hardware diversity.
* Software diversity.

Scheduling throughput may scale independently of execution capacity.

---

# Observability

Platform services publish telemetry describing:

* Validation requests
* Capability matching
* Worker Host selection
* Scheduling latency
* Scheduling failures

Telemetry supports observability but is not scheduling state.

---

# Relationship to Platform Services

Scheduling coordinates several platform services:

* Scheduler coordinates the scheduling process.
* Artifact Manager prepares Execution Directories.
* Operational Database provides Worker Capability.
* Validation Workers execute scheduled workloads.

Scheduling itself owns no persistent platform data.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/platform/capability-model.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/services/artifact-manager.md`
* `docs/developer/services/worker.md`

## Related ADRs

* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0014 — Transient Work Queue
* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
* ADR-0023 — Configuration over Customization
