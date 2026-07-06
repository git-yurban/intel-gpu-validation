# ADR-0003: Build and Worker Manifest Model

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform separates build generation from validation execution.

The Builder produces immutable Builds, while the Scheduler assigns validation work to Validation Workers.

To preserve separation of concerns, platform services exchange immutable architectural objects rather than implementation-specific data structures.

The platform therefore requires a well-defined manifest model that describes published Builds and assigned validation work.

---

## Decision

The platform defines two immutable architectural manifests:

* **Build Manifest**
* **Worker Manifest**

Each manifest has a single authoritative producer, a clearly defined purpose, and an immutable lifecycle.

The manifests together define the architectural contracts between the Builder, Artifact Manager, Scheduler, and Validation Workers.

---

## Build Manifest

The Build Manifest is produced exclusively by the Builder.

It is the authoritative description of a published Build.

The Build Manifest identifies:

* Build Identity
* Published Artifact Packages
* Build metadata
* Version information
* Integrity metadata

The Build Manifest describes **what was built**.

It contains no scheduling or execution information.

---

## Worker Manifest

The Worker Manifest is produced exclusively by the Scheduler.

It is the authoritative description of validation work assigned to a Validation Worker.

The Worker Manifest identifies:

* Validation Request
* Execution Directory Reference
* Validation metadata
* Scheduling metadata

The Worker Manifest describes **what should be executed**.

It contains no build description or artifact packaging information.

---

## Manifest Relationships

```text
Builder
    │
    ▼
Build Manifest
    │
    ▼
Artifact Manager
    │
Prepare Execution Directory
    │
Create Execution Directory Reference
    │
    ▼
Scheduler
    │
    ▼
Worker Manifest
    │
    ▼
Validation Worker
```

The Build Manifest describes the published Build.

The Worker Manifest describes the validation workload derived from that Build.

---

## Manifest Lifecycle

Both manifest types:

* Are immutable once published.
* Must never be modified in place.
* May only be superseded by publishing a new manifest.
* Are referenced through immutable identities.
* Form stable architectural contracts between platform services.

---

## Ownership

| Manifest        | Authoritative Producer |
| --------------- | ---------------------- |
| Build Manifest  | Builder                |
| Worker Manifest | Scheduler              |

Each manifest has exactly one authoritative producer.

---

## Consequences

### Advantages

* Clearly separates build generation from validation execution.
* Defines stable architectural contracts.
* Enables deterministic validation.
* Supports independent evolution of platform services.
* Simplifies auditing and debugging.

### Disadvantages

* Introduces multiple manifest types.
* Requires manifest schema versioning.
* Requires services to understand their respective manifest contracts.

---

## Alternatives Considered

### Single platform manifest

Rejected.

A single manifest would tightly couple build generation, scheduling, and execution.

### Workers consume Build Manifests directly

Rejected.

Validation Workers should execute assigned workloads rather than interpret build metadata or scheduling decisions.

### Mutable manifests

Rejected.

Mutable manifests would compromise reproducibility and invalidate historical execution records.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0005 — Artifact Storage
* ADR-0007 — Build Identity
* ADR-0009 — Scheduler as Control Plane
* ADR-0012 — Stateless Workers
* ADR-0013 — Builder as an Independent Service
