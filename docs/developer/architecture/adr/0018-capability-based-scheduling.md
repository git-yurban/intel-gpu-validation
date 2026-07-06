# ADR-0018: Capability-Based Scheduling

**Status:** Accepted

**Date:** 2026-07-02

## Context

Validation workloads have execution requirements that may depend on hardware, GPU architecture, operating system, drivers, runtime environments, or other platform-defined capabilities.

Worker Hosts provide different execution capabilities.

The Scheduler must assign validation workloads only to Worker Hosts capable of executing them while remaining independent of execution implementation details.

The platform therefore adopts capability-based scheduling.

---

## Decision

The Scheduler assigns validation workloads by matching workload requirements against registered Worker Capabilities.

Scheduling decisions are based on declared capabilities rather than implementation-specific knowledge of Worker Hosts.

Capability matching determines eligibility for execution.

Scheduling policy determines which eligible Worker Host receives the workload.

---

## Responsibilities

Capability-Based Scheduling is responsible for:

* Evaluating workload requirements.
* Evaluating registered Worker Capabilities.
* Determining execution eligibility.
* Providing eligible Worker Hosts to the Scheduler.

Capability-Based Scheduling is not responsible for:

* Defining Worker Capabilities.
* Executing validation workloads.
* Maintaining operational state.
* Defining scheduling algorithms.

---

## Scheduling Model

Scheduling consists of two independent steps:

1. Determine eligible Worker Hosts through capability matching.
2. Select one eligible Worker Host according to scheduling policy.

Capability matching and scheduling policy are intentionally independent architectural concerns.

---

## Scheduling Flow

```text id="2khgg8"
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
Apply Scheduling Policy
        │
        ▼
Selected Worker Host
        │
Create Worker Manifest
```

The scheduling algorithm used to choose among eligible Worker Hosts is an implementation decision.

---

## Design Principles

Capability-Based Scheduling should be:

* Deterministic
* Declarative
* Extensible
* Independent of scheduling policy
* Independent of Worker implementation

The architecture intentionally separates capability evaluation from workload selection.

---

## Consequences

### Advantages

* Supports heterogeneous Worker Hosts.
* Simplifies capability evolution.
* Decouples capability modeling from scheduling policy.
* Enables future scheduling strategies without changing capability definitions.
* Improves architectural flexibility.

### Disadvantages

* Requires accurate capability registration.
* Introduces capability evaluation before scheduling.
* Requires capability schema evolution over time.

---

## Alternatives Considered

### Static Worker assignment

Rejected.

Static assignment does not scale to heterogeneous Worker Hosts or changing execution requirements.

### Worker self-selection

Rejected.

Scheduling decisions remain the responsibility of the Scheduler.

### Scheduling based only on availability

Rejected.

Availability alone does not ensure a Worker Host can correctly execute a validation workload.

---

## Related ADRs

* ADR-0009 — Scheduler as Control Plane
* ADR-0016 — Worker Host Identification
* ADR-0017 — Worker Capability Model
