# Capability Model

## Overview

The Capability Model defines how the platform describes the execution capabilities of Worker Hosts.

It provides a consistent, declarative representation of hardware, software, and execution characteristics used by the Scheduler to determine where validation workloads may execute.

The Capability Model is a shared platform capability rather than a platform service.

---

# Purpose

The Capability Model enables the platform to:

* Describe Worker Host capabilities.
* Match validation requirements to eligible Worker Hosts.
* Support heterogeneous hardware and software environments.
* Enable deterministic capability-based scheduling.

The Capability Model defines **what** a Worker Host can execute, not **how** scheduling decisions are made.

---

# Architectural Role

The Capability Model provides:

* A declarative description of Worker Host capabilities.
* A common language between Validation Workers and the Scheduler.
* A stable representation of execution capabilities.

The Capability Model does not:

* Schedule validation workloads.
* Execute validation workloads.
* Store Operational State.
* Define scheduling policy.

Those responsibilities remain with other platform services.

---

# Participants

The Capability Model is used by:

| Component            | Responsibility                           |
| -------------------- | ---------------------------------------- |
| Validation Worker    | Publish Worker Capability                |
| Operational Database | Store Worker Capability                  |
| Scheduler            | Consume Worker Capability for scheduling |

Each component has a clearly defined responsibility.

---

# Capability Lifecycle

```text id="9mz2tx"
Validation Worker
        │
Publish Worker Capability
        │
        ▼
Operational Database
        │
Store Capability
        │
        ▼
Scheduler
        │
Capability Matching
        │
        ▼
Eligible Worker Hosts
```

Worker Capabilities are mutable Operational State.

---

# Capability Characteristics

Worker Capabilities should be:

* Declarative
* Accurate
* Version-independent where practical
* Deterministic
* Independently extensible

Capability descriptions should express execution characteristics rather than implementation details.

---

# Design Principles

The Capability Model should:

* Describe execution capability, not scheduling policy.
* Remain independent of individual validation workloads.
* Support heterogeneous execution environments.
* Allow capabilities to evolve without changing platform architecture.

The model should be extensible while preserving backward compatibility whenever practical.

---

# Failure Handling

If Worker Capability information is unavailable or invalid:

* The affected Worker Host is not considered eligible for scheduling.
* Validation workloads are not assigned based on incomplete capability information.
* Capability publication failures are reported as Operational State.

Capability information must be authoritative before scheduling decisions are made.

---

# Scalability

The Capability Model is designed to support growth in:

* Worker Host count.
* Hardware diversity.
* Software diversity.
* Validation workload diversity.

Platform growth should not require architectural changes to the capability model.

---

# Observability

Platform services publish telemetry describing:

* Capability publication
* Capability updates
* Capability matching
* Matching failures

Telemetry supports observability but is not Worker Capability or Operational State.

---

# Relationship to Platform Services

The Capability Model is shared by multiple platform services.

Validation Workers publish Worker Capability.

The Operational Database stores Worker Capability as mutable Operational State.

The Scheduler consumes Worker Capability during capability-based scheduling.

The Capability Model itself owns no platform data.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/services/worker.md`
* `docs/developer/services/operational-database.md`

## Related ADRs

* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
* ADR-0020 — Data Classification
