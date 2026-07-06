# ADR-0005: Artifact Storage

**Status:** Accepted

**Date:** 2026-07-02

## Context

The Builder produces immutable published Artifact Packages that must remain available throughout their retention lifecycle.

Multiple platform services require access to published artifacts, including the Artifact Manager during execution preparation.

Build generation should remain independent of artifact persistence, retention, and retrieval.

The platform therefore requires a dedicated service responsible for durable artifact storage.

---

## Decision

The platform adopts **Artifact Storage** as the authoritative service responsible for the durable storage and retrieval of immutable published Artifact Packages.

Artifact Storage owns artifact persistence throughout the artifact lifecycle.

Artifact Storage does not produce build artifacts, prepare execution environments, schedule validation, or execute validation workloads.

---

## Responsibilities

Artifact Storage is responsible for:

* Receiving published Artifact Packages
* Persisting published Artifact Packages
* Preserving artifact immutability
* Providing the Artifact Access API
* Managing artifact metadata
* Enforcing artifact retention policy

Artifact Storage is not responsible for:

* Producing Builds
* Producing Artifact Packages
* Publishing Build Manifests
* Preparing Execution Directories
* Scheduling validation
* Executing validation workloads

---

## Artifact Lifecycle

```text id="swt8bl"
Builder
      │
Publish Artifact Package
      │
      ▼
Artifact Storage
      │
Persist Artifact Package
      │
      ▼
Artifact Access API
      │
      ▼
Artifact Manager
```

Artifact Storage becomes responsible for an Artifact Package immediately after successful publication.

---

## Immutability

Artifact Packages stored by Artifact Storage:

* Are immutable.
* Must never be modified in place.
* Are retrieved through the Artifact Access API.
* May only be removed through the artifact retention process.

Artifact Storage preserves published artifacts but does not alter them.

---

## Service Boundaries

Artifact Storage owns:

* Artifact persistence
* Artifact retrieval
* Artifact metadata
* Artifact retention

Artifact Storage does not own:

* Build generation
* Artifact packaging
* Validation execution
* Scheduling
* Worker execution

These responsibilities belong to other platform services.

---

## Consequences

### Advantages

* Separates build generation from storage.
* Enables independent scaling of storage.
* Simplifies artifact lifecycle management.
* Supports deterministic artifact retrieval.
* Centralizes artifact retention.

### Disadvantages

* Introduces an additional platform service.
* Requires storage infrastructure.
* Adds network communication between services.

---

## Alternatives Considered

### Builder owns artifact storage

Rejected.

The Builder should produce immutable artifacts, not manage long-term storage.

### Workers retrieve artifacts directly from the Builder

Rejected.

Build generation and validation execution should remain independent.

### Local artifact storage on every Worker

Rejected.

Distributed local storage complicates consistency, increases duplication, and makes retention management significantly more difficult.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0006 — Compressed Artifact Format
* ADR-0008 — Worker Artifact Cache
* ADR-0013 — Builder as an Independent Service
