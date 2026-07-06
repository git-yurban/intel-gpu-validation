# ADR-0020: Data Classification

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform stores and exchanges multiple categories of data throughout build generation, scheduling, validation execution, and operational monitoring.

Different categories of data have different ownership, lifecycles, and architectural responsibilities.

The platform therefore requires a consistent data classification model that defines how data is owned, managed, and evolves throughout the system.

---

## Decision

The platform classifies data into three architectural categories:

* Immutable Architectural Contracts
* Mutable Operational State
* Transient Execution Resources

Each category has distinct ownership, lifecycle, and responsibilities.

---

## Immutable Architectural Contracts

Architectural Contracts define the immutable interfaces and published artifacts exchanged between platform services.

Examples include:

* Build Identity
* Build Manifest
* Worker Manifest
* Artifact Package

Characteristics:

* Immutable
* Versioned
* Authoritatively owned
* Traceable
* Reproducible

Architectural Contracts are the authoritative description of the platform's published artifacts and service interactions.

---

## Mutable Operational State

Operational State describes the current and historical operation of the platform.

Examples include:

* Worker Host registration
* Worker Capability
* Validation execution status
* Validation results
* Platform metrics

Characteristics:

* Mutable
* Continuously updated
* Operationally owned
* Queryable
* Historical

The Operational Database is the authoritative owner of Operational State.

---

## Transient Execution Resources

Transient Execution Resources exist only while validation workloads are prepared and executed.

Examples include:

* Execution Directory
* Execution Environment
* Worker Artifact Cache
* Temporary files

Characteristics:

* Temporary
* Disposable
* Locally owned
* Reproducible
* Never authoritative

Execution Resources may be recreated at any time and are never considered persistent platform data.

---

## Ownership

Each data category has a single authoritative owner.

| Data Category                     | Primary Owner              |
| --------------------------------- | -------------------------- |
| Immutable Architectural Contracts | Producing platform service |
| Mutable Operational State         | Operational Database       |
| Transient Execution Resources     | Validation Worker          |

Ownership is exclusive and responsibilities do not overlap.

---

## Design Principles

Data classification should:

* Define clear ownership.
* Preserve architectural boundaries.
* Separate immutable contracts from mutable runtime information.
* Keep transient execution resources local to the Validation Worker.
* Minimize unnecessary duplication.

---

## Consequences

### Advantages

* Clarifies ownership.
* Simplifies architectural boundaries.
* Improves long-term maintainability.
* Supports deterministic validation.
* Provides a consistent data model across the platform.

### Disadvantages

* Requires disciplined ownership.
* Some data may require transformation when moving between categories.
* Classification must evolve as the platform evolves.

---

## Alternatives Considered

### No formal data classification

Rejected.

Without a common classification model, ownership and lifecycle responsibilities become ambiguous.

### Service-specific data models

Rejected.

A platform-wide classification model provides consistent architectural guidance while allowing implementation flexibility within individual services.

### Treat all platform data equally

Rejected.

Different categories of data have fundamentally different ownership, mutability, and lifecycle requirements.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0010 — Operational Database
* ADR-0011 — Execution Environment Isolation
* ADR-0012 — Stateless Workers
* ADR-0019 — Engineering Guidelines
