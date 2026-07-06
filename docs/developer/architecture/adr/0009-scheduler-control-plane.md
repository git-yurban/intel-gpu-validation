# ADR-0009: Scheduler as Control Plane

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform distributes validation workloads across a fleet of stateless Validation Workers.

Build generation, artifact management, scheduling, and validation execution are independent architectural concerns.

To preserve separation of responsibilities, scheduling decisions should remain independent of build preparation and validation execution.

The platform therefore requires a dedicated Scheduler responsible solely for coordinating validation work.

---

## Decision

The platform adopts a dedicated **Scheduler** as the control plane for validation execution.

The Scheduler coordinates validation work by consuming Validation Requests and publishing immutable Worker Manifests.

The Scheduler never executes validation, prepares execution environments, or manages published artifacts.

---

## Responsibilities

The Scheduler is responsible for:

* Receiving Validation Requests
* Selecting appropriate Validation Workers
* Applying scheduling policy
* Publishing immutable Worker Manifests
* Tracking scheduling state
* Supporting retry and recovery

The Scheduler is not responsible for:

* Producing Builds
* Publishing Build Manifests
* Managing Artifact Packages
* Preparing Execution Directories
* Executing validation workloads
* Persisting validation results

---

## Control Plane Model

The Scheduler operates exclusively on immutable architectural objects.

Inputs include:

* Validation Request
* Worker Capability
* Scheduling configuration

Output:

* Worker Manifest

The Worker Manifest contains the Execution Directory Reference required by the Validation Worker to execute the assigned workload.

The Scheduler does not resolve or manipulate Execution Directory References.

---

## Scheduling Flow

```text id="c0n0lh"
Receive Validation Request
            │
            ▼
Evaluate Available Workers
            │
            ▼
Match Worker Capability
            │
            ▼
Apply Scheduling Policy
            │
            ▼
Create Worker Manifest
            │
            ▼
Assign Validation Worker
            │
            ▼
Publish Worker Manifest
```

The Scheduler's responsibility ends when the Worker Manifest has been successfully published.

---

## Worker Assignment

Worker selection may consider:

* Worker Capability
* Worker availability
* Validation requirements
* Scheduling configuration

The scheduling algorithm is an implementation decision.

---

## Failure Recovery

Scheduling failures should:

* Prevent duplicate work assignment.
* Preserve published Worker Manifests.
* Support deterministic retry.
* Produce actionable diagnostics.

Recovery occurs by publishing a new Worker Manifest rather than modifying an existing one.

---

## Consequences

### Advantages

* Clean separation between orchestration and execution.
* Independent scaling of the Scheduler.
* Deterministic scheduling decisions.
* Immutable scheduling contracts.
* Simplified Validation Worker implementation.

### Disadvantages

* Introduces Worker Manifest management.
* Requires scheduling state management.
* Requires coordination with Worker availability.

---

## Alternatives Considered

### Validation Workers self-schedule

Rejected.

Validation Workers should execute assigned workloads rather than coordinate platform-wide scheduling.

### Scheduler executes validation

Rejected.

Scheduling and execution are separate architectural responsibilities.

### Scheduler prepares Execution Directories

Rejected.

Execution preparation belongs to the Artifact Manager.

The Scheduler coordinates work using immutable architectural objects rather than runtime artifacts.

---

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0012 — Stateless Workers
* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
