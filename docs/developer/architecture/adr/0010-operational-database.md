# ADR-0010: Operational Database

**Status:** Accepted

**Date:** 2026-07-02

## Context

The validation platform requires a centralized view of runtime operations to support scheduling, monitoring, reporting, troubleshooting, and dashboard visualization.

Validation Workers, the Scheduler, Builder, Artifact Manager, and other platform services continuously produce operational information that changes throughout the lifetime of the platform.

This operational information is distinct from immutable architectural objects such as Build Manifests and Worker Manifests.

The platform therefore requires a dedicated Operational Database.

---

## Decision

The platform adopts a dedicated **Operational Database** as the authoritative store for mutable operational state.

The Operational Database stores the current and historical operational state of the platform.

It does not own immutable architectural objects or published artifacts.

---

## Responsibilities

The Operational Database is responsible for storing:

* Build execution status
* Validation execution status
* Worker status
* Worker Capability
* Validation results
* Platform operational metrics
* Historical execution records

The Operational Database is not responsible for storing:

* Artifact Packages
* Build Manifests
* Worker Manifests
* Execution Directories
* Build outputs

---

## Data Model

The Operational Database stores mutable operational information.

Typical data includes:

* Active validations
* Completed validations
* Worker registrations
* Worker health
* Build history
* Validation history
* Execution statistics

Schema design is an implementation decision.

---

## Operational Flow

```text id="xyjlwm"
Platform Services
        │
Publish Operational State
        │
        ▼
Operational Database
        │
        ├──────────────┐
        ▼              ▼
Dashboard      Operational Queries
```

The Operational Database is continuously updated as platform state changes.

---

## Ownership

The Operational Database owns:

* Mutable operational state
* Historical operational records
* Runtime status

The Operational Database does not own:

* Published artifacts
* Immutable architectural objects
* Runtime execution environments

Those remain the responsibility of their respective platform services.

---

## Consequences

### Advantages

* Centralized operational visibility.
* Simplified dashboard implementation.
* Historical execution tracking.
* Improved troubleshooting.
* Supports reporting and analytics.

### Disadvantages

* Introduces an additional platform service.
* Requires database infrastructure.
* Requires operational data lifecycle management.

---

## Alternatives Considered

### Distributed operational state

Rejected.

Maintaining operational state independently within each service complicates monitoring, reporting, and cross-service visibility.

### Dashboard queries services directly

Rejected.

Direct service queries increase coupling, duplicate aggregation logic, and make historical reporting more difficult.

### Store immutable architectural objects

Rejected.

Immutable architectural objects remain owned by their authoritative producers and are not part of the Operational Database.

---

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0009 — Scheduler as Control Plane
* ADR-0017 — Worker Capability Model
* ADR-0021 — Telemetry and Observability
* ADR-0022 — Dashboard as a Read-Only Platform Service
