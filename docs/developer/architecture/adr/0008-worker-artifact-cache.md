# ADR-0008: Worker Artifact Cache

**Status:** Accepted

**Date:** 2026-07-02

## Context

Validation Workers repeatedly execute workloads that reference published Artifact Packages.

Retrieving Artifact Packages from Artifact Storage for every validation workload increases network utilization, execution preparation time, and storage service load.

The platform therefore requires a mechanism to reuse previously retrieved Artifact Packages while preserving artifact immutability and deterministic validation.

---

## Decision

Each Validation Worker maintains a local **Worker Artifact Cache** containing previously retrieved immutable Artifact Packages.

The cache is an execution optimization only.

Artifact Storage remains the authoritative source of all published Artifact Packages.

Validation results must be identical regardless of whether an Artifact Package is retrieved from the local cache or from Artifact Storage.

---

## Cache Model

The Worker Artifact Cache:

* Stores immutable Artifact Packages.
* Is local to the Validation Worker.
* Is private to the Validation Worker.
* Is transient.
* May be recreated at any time.
* Does not modify published Artifact Packages.

Cached Artifact Packages remain identical to their published counterparts.

---

## Cache Lifecycle

```text id="ht3v8v"
Artifact Storage
        │
Retrieve Artifact Package
        │
        ▼
Worker Artifact Cache
        │
Cache Hit / Cache Miss
        │
        ▼
Artifact Manager
        │
Prepare Execution Directory
```

Cache population and eviction are implementation decisions.

---

## Cache Rules

The Worker Artifact Cache:

* Never modifies cached Artifact Packages.
* Never becomes the authoritative artifact source.
* May evict cached Artifact Packages at any time.
* Retrieves missing Artifact Packages from Artifact Storage.
* Preserves artifact integrity.

The cache exists solely to improve execution preparation performance.

---

## Consequences

### Advantages

* Reduces Artifact Storage load.
* Reduces network traffic.
* Improves execution preparation performance.
* Enables efficient reuse of published Artifact Packages.
* Preserves deterministic validation.

### Disadvantages

* Requires local storage.
* Requires cache management.
* Requires cache eviction policies.

---

## Alternatives Considered

### No local cache

Rejected.

Repeated retrieval of identical Artifact Packages unnecessarily increases execution preparation time and network utilization.

### Shared distributed cache

Rejected.

A distributed cache increases architectural complexity, introduces an additional platform dependency, and provides limited benefit for deterministic validation workloads.

### Multiple Validation Workers sharing a cache

Rejected.

The platform assumes a single Validation Worker per Worker Host.

Sharing GPU resources between multiple Validation Workers introduces resource contention, reduces execution determinism, and negatively impacts validation reproducibility.

### Mutable cached Artifact Packages

Rejected.

Cached Artifact Packages must remain identical to their published counterparts to preserve deterministic validation.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
* ADR-0012 — Stateless Workers
* ADR-0016 — Worker Host Identification
