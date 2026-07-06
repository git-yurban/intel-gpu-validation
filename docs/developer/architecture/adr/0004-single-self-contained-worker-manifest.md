# ADR-0004: Single Self-Contained Worker Manifest

**Status:** Accepted

**Date:** 2026-07-02

## Context

Validation Workers execute workloads independently across a distributed validation platform.

Workers should begin execution without requiring additional coordination with the Scheduler or Builder.

To support reliable scheduling, offline execution, retries, and deterministic validation, every assigned workload must contain all information required for execution.

The platform therefore requires a self-contained Worker Manifest.

---

## Decision

Each validation workload is described by a single immutable Worker Manifest.

The Worker Manifest contains all information required by a Validation Worker to execute the assigned workload.

After publication, the Worker Manifest is immutable.

Workers never require additional scheduling information after receiving a Worker Manifest.

---

## Worker Manifest Contents

A Worker Manifest contains:

* Validation Request
* Execution Directory Reference
* Validation metadata
* Scheduling metadata

The Worker Manifest intentionally excludes:

* Build description
* Artifact packaging information
* Worker runtime state
* Platform operational state

Those concerns belong to other architectural objects and services.

---

## Design Principles

The Worker Manifest shall be:

* Self-contained
* Immutable
* Deterministic
* Versioned
* Transportable
* Independent of Worker implementation

Validation Workers should require no additional Scheduler interaction after receiving a Worker Manifest.

---

## Worker Execution

```text
Scheduler
      │
Publish Worker Manifest
      │
      ▼
Validation Worker
      │
Resolve Execution Directory Reference
      │
      ▼
Prepare Execution Environment
      │
      ▼
Execute Validation
```

The Worker Manifest is the sole architectural contract between the Scheduler and the Validation Worker.

---

## Consequences

### Advantages

* Simplifies Worker implementation.
* Supports stateless Validation Workers.
* Enables deterministic execution.
* Simplifies retry and recovery.
* Reduces Scheduler-to-Worker coupling.

### Disadvantages

* Worker Manifests may become larger over time.
* Manifest schema evolution requires versioning.
* Additional metadata may increase publication overhead.

---

## Alternatives Considered

### Workers query the Scheduler during execution

Rejected.

Execution should remain independent of scheduling after work assignment.

### Multiple manifests per validation workload

Rejected.

Multiple manifests introduce coordination complexity and increase coupling between services.

### Mutable Worker Manifests

Rejected.

Immutability preserves deterministic execution and historical traceability.

---

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0009 — Scheduler as Control Plane
* ADR-0011 — Execution Environment Isolation
* ADR-0012 — Stateless Workers
* ADR-0018 — Capability-Based Scheduling
