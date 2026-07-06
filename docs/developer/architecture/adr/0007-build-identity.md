# ADR-0007: Build Identity

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform publishes immutable Builds that are stored, referenced, prepared, and validated across multiple platform services.

Every published Build must be uniquely identifiable throughout its lifecycle.

Without a stable Build Identity, artifact retrieval, validation reproducibility, auditing, and historical traceability become unreliable.

The platform therefore requires a globally unique Build Identity.

---

## Decision

Every published Build shall have exactly one immutable Build Identity.

The Build Identity uniquely identifies a published Build for its entire lifetime.

A Build Identity is assigned when the Build is published and never changes.

If build contents change, a new Build with a new Build Identity is created.

---

## Scope

The Build Identity is used by platform services including:

* Builder
* Artifact Storage
* Artifact Manager
* Operational Database
* Dashboard

The Build Identity is referenced by the Build Manifest and associated platform metadata.

---

## Identity Rules

A Build Identity:

* Is globally unique.
* Is immutable.
* Identifies exactly one published Build.
* Is never reused.
* Remains valid until the Build is removed through the artifact retention process.

The representation of the Build Identity is an implementation decision.

---

## Lifecycle

```text id="8hx0cn"
Build
    │
Assign Build Identity
    │
    ▼
Publish Build
    │
    ▼
Build Manifest
    │
    ▼
Artifact Storage
    │
    ▼
Validation Platform
```

The Build Identity remains unchanged throughout the lifetime of the published Build.

---

## Consequences

### Advantages

* Enables deterministic Build identification.
* Supports reproducible validation.
* Simplifies auditing.
* Simplifies artifact retrieval.
* Supports long-term traceability.

### Disadvantages

* Every published Build requires a new identity.
* Identity generation must guarantee uniqueness.

---

## Alternatives Considered

### Mutable Build Identity

Rejected.

Changing Build Identity would invalidate references and compromise reproducibility.

### Derive Build Identity from artifact location

Rejected.

Storage location is an implementation detail and should not define architectural identity.

### Reuse Build Identity across multiple Builds

Rejected.

Each published Build must remain uniquely identifiable throughout its lifecycle.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0010 — Operational Database
* ADR-0013 — Builder as an Independent Service
