# ADR-0012: Stateless Workers

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform distributes workloads across independent Validation Workers.

Workers may be restarted, replaced, upgraded, or removed without affecting the correctness of the platform.

To support horizontal scalability, fault recovery, and operational simplicity, Workers should avoid owning persistent platform state.

The platform therefore adopts stateless Validation Workers.

---

## Decision

Validation Workers are stateless platform services.

Workers execute assigned validation workloads but do not own authoritative platform state.

All persistent platform state is owned by the appropriate platform service.

Local execution resources may exist but are considered transient implementation details.

---

## Worker Responsibilities

Validation Workers are responsible for:

* Receiving Worker Manifests
* Preparing Execution Environments
* Executing validation workloads
* Producing validation results
* Reporting operational state

Validation Workers are not responsible for:

* Scheduling
* Build generation
* Artifact publication
* Persistent platform state
* Operational data ownership

---

## Local Resources

Validation Workers may maintain transient local resources, including:

* Worker Artifact Cache
* Execution Directories
* Execution Environments
* Temporary files

These resources:

* Are local to the Validation Worker.
* Are transient.
* May be recreated at any time.
* Are never authoritative platform state.

---

## Worker Lifecycle

```text
Worker Manifest
        │
        ▼
Prepare Execution Environment
        │
        ▼
Execute Validation
        │
        ▼
Publish Validation Results
        │
        ▼
Destroy Execution Environment
```

A Validation Worker may be stopped, restarted, or replaced without affecting the architectural correctness of the platform.

---

## Design Principles

Validation Workers should be:

* Stateless
* Deterministic
* Replaceable
* Independently deployable
* Horizontally scalable

Worker replacement should require no migration of persistent platform state.

---

## Consequences

### Advantages

* Simplifies deployment.
* Simplifies recovery.
* Enables horizontal scaling.
* Improves fault tolerance.
* Reduces operational complexity.

### Disadvantages

* Requires external ownership of platform state.
* Requires Workers to retrieve required execution resources.
* Increases reliance on platform services.

---

## Alternatives Considered

### Stateful Validation Workers

Rejected.

Persisting platform state within Workers complicates recovery, scaling, and operational management.

### Worker-owned operational database

Rejected.

Operational state belongs in the Operational Database.

### Persistent execution environments

Rejected.

Execution resources should remain transient and reproducible.

---

## Related ADRs

* ADR-0008 — Worker Artifact Cache
* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0011 — Execution Environment Isolation
* ADR-0013 — Builder as an Independent Service
