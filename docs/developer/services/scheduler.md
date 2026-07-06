# Scheduler

## Overview

The Scheduler is the control plane of the Intel GPU Validation Lab.

It coordinates validation execution by matching validation workload requirements against registered Worker Capabilities, requesting Execution Directories, selecting eligible Worker Hosts, and producing immutable Worker Manifests.

The Scheduler coordinates validation execution but never executes validation workloads.

---

# Responsibilities

The Scheduler is responsible for:

* Receiving validation requests.
* Evaluating validation requirements.
* Determining eligible Worker Hosts through capability matching.
* Requesting Execution Directories from the Artifact Manager.
* Selecting a Worker Host according to scheduling policy.
* Creating Worker Manifests.
* Publishing Worker Manifests to the Transient Work Queue.

The Scheduler's architectural responsibility ends after successful publication of the Worker Manifest.

---

# Architectural Responsibilities

The Scheduler owns:

* Validation coordination
* Capability-based scheduling
* Worker Host selection
* Worker Manifest creation

The Scheduler does not own:

* Build generation
* Artifact persistence
* Execution Directory preparation
* Validation execution
* Operational State

These responsibilities belong to other platform services.

---

# Dependencies

The Scheduler depends on:

* Artifact Manager
* Operational Database
* Transient Work Queue

The Scheduler consumes Worker Capabilities maintained in the Operational Database.

The Scheduler serves:

* Validation Workers (through the Transient Work Queue)

---

# Inputs

The Scheduler consumes:

* Validation requests
* Worker Capabilities
* Execution Directory References

Worker Capabilities are mutable Operational State.

Execution Directory References are transient platform references.

---

# Outputs

The Scheduler produces:

| Output          | Classification                   |
| --------------- | -------------------------------- |
| Worker Manifest | Immutable Architectural Contract |

The Worker Manifest defines the complete execution contract for a validation workload.

---

# Scheduling Workflow

```text id="tdo0pc"
Validation Request
        │
Determine Requirements
        │
        ▼
Worker Capabilities
        │
Capability Matching
        │
        ▼
Eligible Worker Hosts
        │
Request Execution Directory
        ▼
Artifact Manager
        │
Execution Directory Reference
        ▼
Scheduler
        │
Select Worker Host
        │
Create Worker Manifest
        │
Publish
        ▼
Transient Work Queue
```

Publication marks the completion of the Scheduler's architectural responsibility.

---

# Service Boundaries

The Scheduler communicates using immutable Architectural Contracts and transient platform references.

It never:

* Builds software.
* Stores Artifact Packages.
* Prepares Execution Directories.
* Executes validation workloads.
* Owns Operational State.

The Scheduler is intentionally isolated from runtime execution.

---

# Failure Handling

If scheduling fails:

* No Worker Manifest is published.
* No validation workload is assigned.
* Validation execution does not begin.
* The failure is reported as Operational State.

Worker Manifests are published only after successful capability matching, Execution Directory preparation, and Worker Host selection.

---

# Scalability

The Scheduler is designed to scale independently of the remainder of the platform.

Scheduling throughput may increase independently of:

* Builder
* Artifact Storage
* Artifact Manager
* Validation Workers

---

# Observability

The Scheduler publishes telemetry describing:

* Validation requests
* Capability matching
* Scheduling decisions
* Worker Manifest publication
* Scheduling failures
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/artifact-manager.md`
* `docs/developer/services/worker.md`

## Related ADRs

* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0014 — Transient Work Queue
* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
