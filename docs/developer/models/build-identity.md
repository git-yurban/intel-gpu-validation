# Build Identity

## Overview

Build Identity is the canonical identifier for a published Build.

It uniquely identifies a Build throughout the platform and provides a stable reference used by Architectural Contracts and platform services.

A Build Identity never changes after publication.

---

# Purpose

Build Identity enables the platform to:

* Uniquely identify a published Build.
* Reference a Build without embedding Build contents.
* Correlate platform activities involving the same Build.
* Support reproducible validation execution.

Every published Build has exactly one Build Identity.

---

# Architectural Role

Build Identity provides:

* Stable identification.
* Cross-service correlation.
* Build reference semantics.

Build Identity does not:

* Describe a Build.
* Contain build outputs.
* Define validation execution.
* Record operational state.

Those responsibilities belong to other Architectural Contracts.

---

# Ownership

| Component | Responsibility           |
| --------- | ------------------------ |
| Builder   | Create Build Identity    |
| Platform  | Reference Build Identity |

The Builder is the authoritative creator of a Build Identity.

The Build Identity never changes after publication.

---

# Lifecycle

```text
Builder
    │
Create Build Identity
    │
Publish Build
    │
    ▼
Referenced by
    ├── Build Manifest
    ├── Validation Request
    ├── Worker Manifest
    └── Validation Result
```

The Build Identity exists for the lifetime of the Build.

---

# Characteristics

A Build Identity should be:

* Globally unique within the platform.
* Stable.
* Immutable.
* Opaque to consumers.
* Suitable for long-term reference.

Consumers should compare Build Identities but should not derive meaning from their representation.

---

# Immutability

A Build Identity is immutable.

Once assigned:

* The identifier never changes.
* The Build it identifies never changes.
* References remain valid throughout the Build lifecycle.

A different Build always requires a different Build Identity.

---

# Design Principles

Build Identity should be:

* Unique.
* Stable.
* Immutable.
* Portable.
* Independent of implementation.

Its representation is an implementation detail; its uniqueness and stability are architectural requirements.

---

# Relationship to Platform Services

The Builder creates the Build Identity.

Platform services reference the Build Identity to correlate Build-related operations.

The Build Identity appears in:

* Build Manifest
* Validation Request
* Worker Manifest
* Validation Result

It serves as the common identifier across the platform.

---

# Related Documentation

* `docs/architecture.md`
* `docs/glossary.md`
* `docs/developer/contracts/build-manifest.md`
* `docs/developer/contracts/validation-request.md`
* `docs/developer/contracts/worker-manifest.md`
* `docs/developer/contracts/validation-result.md`

## Related ADRs

* ADR-0007 — Build Identity
* ADR-0020 — Data Classification
