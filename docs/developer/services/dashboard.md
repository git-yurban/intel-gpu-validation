# Dashboard

## Overview

The Dashboard is the platform's read-only presentation service.

It provides a unified operational view of Builds, Worker Hosts, validation execution, scheduling, Operational State, and platform telemetry.

The Dashboard consumes authoritative information from platform services without becoming the authoritative owner of any platform data.

---

# Responsibilities

The Dashboard is responsible for:

* Presenting platform status.
* Visualizing validation activity.
* Displaying Build information.
* Displaying Worker Host information.
* Displaying validation results.
* Presenting platform telemetry.
* Providing operational insight.

The Dashboard's architectural responsibility is limited to presentation.

---

# Architectural Responsibilities

The Dashboard owns:

* Presentation
* Visualization
* User interaction

The Dashboard does not own:

* Build generation
* Artifact persistence
* Validation scheduling
* Validation execution
* Operational State
* Telemetry

These responsibilities belong to other platform services.

---

# Dependencies

The Dashboard depends on:

* Operational Database
* Telemetry and Observability

The Dashboard may also consume information from other authoritative platform services when appropriate.

The Dashboard serves:

* Platform operators
* Validation engineers
* System administrators

---

# Inputs

The Dashboard consumes:

| Input             | Classification            |
| ----------------- | ------------------------- |
| Operational State | Mutable Operational State |
| Telemetry         | Operational telemetry     |

The Dashboard consumes authoritative information but does not become its authoritative owner.

---

# Outputs

The Dashboard produces:

| Output                  | Classification |
| ----------------------- | -------------- |
| Platform visualizations | Presentation   |
| Operational dashboards  | Presentation   |
| Reports                 | Presentation   |

The Dashboard does not create new platform data.

---

# Presentation Workflow

```text id="1hfzkg"
Platform Services
        │
        ├──────────────┐
        ▼              ▼
Operational Database  Telemetry
        │              │
        └──────┬───────┘
               ▼
          Dashboard
               │
        Present Information
               ▼
           Platform Operators
```

The Dashboard provides a unified operational view without changing the underlying platform state.

---

# Service Boundaries

The Dashboard communicates using authoritative Operational State and telemetry.

It never:

* Builds software.
* Stores Artifact Packages.
* Schedules validation.
* Executes validation workloads.
* Modifies Operational State.
* Owns telemetry.

The Dashboard is intentionally isolated from platform operation.

---

# Failure Handling

If the Dashboard is unavailable:

* Platform services continue operating normally.
* Validation execution continues.
* Operational State continues to be recorded.
* Telemetry continues to be published.

Dashboard availability affects visibility but not platform operation.

---

# Scalability

The Dashboard is designed to scale independently of the remainder of the platform.

Presentation capacity may increase independently of:

* Builder
* Artifact Storage
* Artifact Manager
* Scheduler
* Validation Workers
* Operational Database

---

# Observability

The Dashboard publishes telemetry describing:

* User activity
* Query performance
* Visualization performance
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/operational-database.md`
* `docs/developer/platform/telemetry.md`

## Related ADRs

* ADR-0010 — Operational Database
* ADR-0019 — Engineering Guidelines
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
* ADR-0022 — Dashboard as a Read-Only Platform Service
