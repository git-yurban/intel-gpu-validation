# ADR-0013: Builder as an Independent Service

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform builds software independently of validation execution.

Build generation is compute-intensive, has its own lifecycle, and evolves independently of scheduling and validation.

Coupling build generation to other platform services would reduce scalability, complicate deployments, and blur architectural responsibilities.

The platform therefore requires a dedicated Builder service.

---

## Decision

The platform adopts the **Builder** as an independent platform service responsible for build generation.

The Builder is the sole authoritative producer of published Builds, Build Manifests, and published Artifact Packages.

The Builder operates independently of scheduling and validation execution.

---

## Responsibilities

The Builder is responsible for:

* Producing Builds
* Creating Build Identities
* Creating Build Manifests
* Creating Artifact Packages
* Publishing Artifact Packages

The Builder is not responsible for:

* Artifact persistence
* Scheduling validation
* Preparing Execution Directories
* Executing validation workloads
* Persisting operational state

---

## Build Flow

```text id="xnt2om"
Source
   │
   ▼
Builder
   │
Create Build
   │
Create Build Manifest
   │
Create Artifact Packages
   │
Publish
   │
   ▼
Artifact Storage
```

The Builder's architectural responsibility ends after successful publication of the Build Manifest and Artifact Packages.

---

## Service Boundaries

The Builder owns:

* Build generation
* Build Identity creation
* Build Manifest creation
* Artifact Package creation

The Builder does not own:

* Artifact Storage
* Artifact lifecycle after publication
* Validation scheduling
* Validation execution
* Operational data

These responsibilities belong to other platform services.

---

## Design Principles

The Builder should be:

* Independent
* Deterministic
* Scalable
* Replaceable
* Focused solely on build generation

The Builder operates independently of Validation Workers.

---

## Consequences

### Advantages

* Clear separation of responsibilities.
* Independent scaling.
* Simplified deployments.
* Independent release cadence.
* Reduced architectural coupling.

### Disadvantages

* Introduces an additional platform service.
* Requires publication coordination with Artifact Storage.
* Requires communication with downstream platform services.

---

## Alternatives Considered

### Builder integrated into Scheduler

Rejected.

Scheduling and build generation have different responsibilities, scaling characteristics, and lifecycles.

### Validation Workers perform builds

Rejected.

Validation Workers should execute validation workloads rather than generate Builds.

### Shared Builder and Artifact Storage service

Rejected.

Build generation and artifact persistence are separate architectural responsibilities and should evolve independently.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0007 — Build Identity
* ADR-0010 — Operational Database
