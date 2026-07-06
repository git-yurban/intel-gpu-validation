# ADR-0022: Dashboard as a Read-Only Platform Service

**Status:** Accepted

**Date:** 2026-07-02

## Context

Platform operators require a unified view of validation activity, Worker Hosts, Builds, scheduling, operational state, and telemetry.

Providing this visibility should not couple operational presentation to the platform services responsible for producing or owning that information.

The platform therefore requires a dedicated Dashboard service.

---

## Decision

The platform adopts the **Dashboard** as a read-only presentation service.

The Dashboard presents operational information by consuming authoritative data from platform services.

The Dashboard never becomes the authoritative owner of platform data.

---

## Responsibilities

The Dashboard is responsible for:

* Presenting operational status.
* Visualizing validation activity.
* Displaying Build information.
* Displaying Worker Host information.
* Presenting platform telemetry.
* Providing operational insight.

The Dashboard is not responsible for:

* Build generation.
* Scheduling.
* Validation execution.
* Operational state ownership.
* Telemetry ownership.
* Artifact management.

---

## Data Sources

The Dashboard consumes information from authoritative platform sources, including:

* Operational Database
* Telemetry and Observability systems
* Other authoritative platform services, when appropriate

The Dashboard does not create, modify, or own the information it presents.

---

## Presentation Model

```text id="w6w7cx"
Platform Services
        │
Publish Operational State
        │
        ▼
Operational Database
        │
        ▼
Dashboard
        │
Present Platform Information
```

The Dashboard is a consumer and presenter of platform information.

It never becomes the authoritative source of that information.

---

## Design Principles

The Dashboard should be:

* Read-only
* Independent
* Responsive
* Replaceable
* Focused on operational visibility

Presentation remains independent of platform operation and platform data ownership.

---

## Ownership

Platform services own the information they produce.

The Operational Database owns operational state.

Telemetry remains owned by the originating platform service.

The Dashboard consumes authoritative information and presents a unified operational view without assuming ownership of the underlying data.

---

## Consequences

### Advantages

* Clear separation between operation and presentation.
* Simplifies platform service responsibilities.
* Enables independent Dashboard evolution.
* Improves operational visibility.
* Prevents ownership duplication.

### Disadvantages

* Introduces an additional platform service.
* Depends on authoritative data sources.
* Requires visualization infrastructure.

---

## Alternatives Considered

### Dashboard owns operational state

Rejected.

Operational state belongs in the Operational Database.

### Dashboard queries internal service state directly

Rejected.

Direct coupling increases implementation dependencies and bypasses the platform's authoritative data model.

### Embed dashboards within individual platform services

Rejected.

A unified platform view is better provided by a dedicated presentation service.

---

## Related ADRs

* ADR-0010 — Operational Database
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
