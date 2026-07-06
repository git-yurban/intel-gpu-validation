# ADR-0014: Transient Work Queue

**Status:** Accepted

**Date:** 2026-07-02

## Context

The Scheduler distributes validation workloads to Validation Workers.

Reliable delivery requires an asynchronous mechanism for transporting work between independent platform services.

The transport mechanism should remain independent of scheduling decisions, operational state, and validation execution.

The platform therefore requires a transient work queue.

---

## Decision

The platform adopts a **Transient Work Queue** as the transport mechanism between the Scheduler and Validation Workers.

The queue transports Worker Manifests.

The queue is not an authoritative source of platform state and does not own validation work.

---

## Responsibilities

The Transient Work Queue is responsible for:

* Transporting Worker Manifests.
* Providing asynchronous delivery.
* Supporting reliable message delivery.
* Decoupling the Scheduler from Validation Workers.

The Transient Work Queue is not responsible for:

* Scheduling validation.
* Persisting operational state.
* Tracking validation progress.
* Storing validation results.
* Executing validation workloads.

---

## Queue Model

The queue transports immutable Worker Manifests.

Messages remain transient.

Validation ownership remains with the Scheduler until a Validation Worker accepts the Worker Manifest.

Operational state remains the responsibility of the Operational Database.

---

## Message Flow

```text id="8l7vpm"
Scheduler
      │
Publish Worker Manifest
      │
      ▼
Transient Work Queue
      │
Deliver Worker Manifest
      │
      ▼
Validation Worker
```

The queue's architectural responsibility ends once delivery has been successfully completed.

---

## Design Principles

The Transient Work Queue should be:

* Asynchronous
* Reliable
* Stateless
* Replaceable
* Independent of implementation technology

Queue technology is an implementation decision.

---

## Consequences

### Advantages

* Decouples scheduling from execution.
* Improves platform scalability.
* Simplifies Validation Worker deployment.
* Supports retry and recovery.
* Enables asynchronous execution.

### Disadvantages

* Introduces an additional platform service.
* Requires reliable message delivery.
* Adds operational infrastructure.

---

## Alternatives Considered

### Scheduler communicates directly with Validation Workers

Rejected.

Direct communication tightly couples scheduling and execution, reducing scalability and operational flexibility.

### Queue stores operational state

Rejected.

Operational state belongs in the Operational Database.

### Persistent work queue as the system of record

Rejected.

The queue is a transport mechanism rather than an authoritative source of platform state.

---

## Related ADRs

* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0012 — Stateless Workers
