# ADR-0017: Worker Capability Model

**Status:** Accepted

**Date:** 2026-07-02

## Context

Validation workloads require specific hardware, software, drivers, operating systems, and runtime environments.

Worker Hosts differ in their available resources and supported execution environments.

The platform therefore requires a consistent architectural model for describing the execution capabilities of Worker Hosts.

---

## Decision

The platform adopts a **Worker Capability Model** that describes the execution capabilities of each Worker Host.

Worker Capabilities are registered with the platform and maintained as operational state.

Scheduling decisions consume Worker Capabilities but do not define them.

---

## Responsibilities

The Worker Capability Model is responsible for describing:

* Hardware capabilities
* GPU capabilities
* Operating system
* Driver information
* Runtime environment
* Platform-defined execution capabilities

The Worker Capability Model is not responsible for:

* Scheduling policy
* Worker selection
* Validation execution
* Operational metrics

---

## Capability Model

Each Worker Host publishes its current Worker Capability.

Capabilities describe **what the Worker Host can execute**, not **what it is currently executing**.

Capability representation is an implementation decision.

---

## Capability Lifecycle

```text id="lkm4oh"
Worker Host
      │
Discover Capabilities
      │
      ▼
Register Worker Capability
      │
      ▼
Operational Database
      │
      ▼
Scheduler
```

Worker Capabilities may be updated as the execution environment of a Worker Host changes.

---

## Design Principles

Worker Capabilities should be:

* Declarative
* Platform-defined
* Versioned
* Extensible
* Independent of scheduling algorithms

The architecture intentionally separates capability description from capability matching.

---

## Consequences

### Advantages

* Provides a consistent execution capability model.
* Decouples capability definition from scheduling.
* Supports heterogeneous Worker Hosts.
* Enables future platform evolution.

### Disadvantages

* Requires capability registration.
* Requires capability version management.
* Requires synchronization when capabilities change.

---

## Alternatives Considered

### Scheduler-specific capability definitions

Rejected.

Capability definitions should remain independent of scheduling implementation.

### Worker self-selection

Rejected.

Validation Workers describe their capabilities but do not decide which workloads to execute.

### Static capability definitions

Rejected.

Worker Host capabilities may change as hardware, drivers, operating systems, or runtime environments evolve.

---

## Related ADRs

* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0016 — Worker Host Identification
* ADR-0018 — Capability-Based Scheduling
