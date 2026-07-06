# ADR-0002: Immutable Build Artifacts

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform builds software that is executed across a large fleet of Validation Workers.

To ensure reproducibility, traceability, and deterministic validation, published build outputs must remain stable after publication.

If published artifacts can be modified, validation results become difficult to reproduce, build identity becomes ambiguous, and platform behavior becomes non-deterministic.

The platform therefore requires immutable published build artifacts.

---

## Decision

All published build artifacts are immutable.

Once a build has been successfully published, none of its published artifacts may be modified in place.

Any change to build outputs produces a new Build with a new Build Identity.

Previously published artifacts remain available until removed according to the platform's artifact retention policy.

---

## Scope

This decision applies to every published artifact produced by the Builder, including:

* Executables
* Shared libraries
* Validation binaries
* Runtime assets
* Configuration packaged with the Build
* Symbol files
* Published Artifact Packages

Implementation-specific intermediate build products are outside the scope of this ADR.

---

## Immutability Rules

Published artifacts:

* Are read-only after publication.
* Must never be overwritten.
* Must never be modified in place.
* Must always be referenced by Build Identity.
* May only be removed through the artifact retention process.

A corrected build is published as a new Build rather than modifying an existing one.

---

## Build Lifecycle

```text id="rq1jzo"
Build Source
      │
      ▼
Produce Build
      │
      ▼
Package Artifacts
      │
      ▼
Publish Artifacts
      │
      ▼
Immutable Published Build
```

Immutability begins immediately after successful publication.

---

## Consequences

### Advantages

* Deterministic validation.
* Reproducible builds.
* Reliable Build Identity.
* Safe artifact caching.
* Simplified auditing.
* Simplified rollback.

### Disadvantages

* Increased storage requirements.
* Duplicate artifacts across Builds.
* Requires explicit artifact retention policies.

---

## Alternatives Considered

### Mutable published artifacts

Rejected.

Updating artifacts after publication breaks reproducibility and invalidates historical validation results.

### Partial artifact replacement

Rejected.

Replacing individual artifacts within a published Build creates ambiguity about the Build's identity and contents.

### Rebuild in place

Rejected.

Every published Build should remain a permanent historical record.

Changes require publishing a new Build.

---

## Related ADRs

* ADR-0003 — Build and Worker Manifest Design
* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
* ADR-0007 — Build Identity
* ADR-0008 — Worker Artifact Cache
* ADR-0013 — Builder as an Independent Service
