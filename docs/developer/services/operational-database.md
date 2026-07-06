# Operational Database

## Overview

The Operational Database is the platform service responsible for storing and providing access to the platform's mutable Operational State.

It serves as the authoritative source of runtime information describing the current and historical operation of the validation platform.

The Operational Database does not own immutable Architectural Contracts or published artifacts.

---

# Responsibilities

The Operational Database is responsible for:

* Storing mutable Operational State.
* Maintaining Worker Host registration.
* Maintaining Worker Capabilities.
* Recording validation execution state.
* Recording validation results.
* Providing operational queries to platform services.

The Operational Database's architectural responsibility is the authoritative persistence of Operational State.

---

# Architectural Responsibilities

The Operational Database owns:

* Worker Host registration
* Worker Capability
* Validation execution state
* Validation results
* Platform operational metadata

The Operational Database does not own:

* Build generation
* Build Manifests
* Worker Manifests
* Artifact Packages
* Execution Directories
* Execution Environments
* Telemetry

These responsibilities belong to other platform services.

---

# Dependencies

The Operational Database depends on:

* Platform services publishing Operational State

The Operational Database serves:

* Scheduler
* Validation Workers
* Dashboard

Telemetry and Observability systems may correlate Operational State but do not own it.

---

# Inputs

The Operational Database consumes:

| Input                        | Classification            |
| ---------------------------- | ------------------------- |
| Validation Results           | Mutable Operational State |
| Worker Host registration     | Mutable Operational State |
| Worker Capability            | Mutable Operational State |
| Validation execution updates | Mutable Operational State |

The Operational Database does not consume immutable Architectural Contracts as authoritative data.

---

# Outputs

The Operational Database provides:

| Output                  | Classification            |
| ----------------------- | ------------------------- |
| Operational queries     | Mutable Operational State |
| Worker Capability       | Mutable Operational State |
| Validation history      | Mutable Operational State |
| Worker Host information | Mutable Operational State |

The Operational Database is the authoritative source for all Operational State.

---

# Operational State Flow

```text
Platform Services
        │
Publish Operational State
        │
        ▼
Operational Database
        │
Persist
        │
        ▼
Operational Queries
        │
        ├──────────────► Scheduler
        ├──────────────► Validation Workers
        └──────────────► Dashboard
```

The Operational Database is the authoritative owner of mutable Operational State.

---

# Service Boundaries

The Operational Database communicates using mutable Operational State.

It never:

* Builds software.
* Stores Artifact Packages.
* Creates Worker Manifests.
* Executes validation workloads.
* Owns telemetry.

The Operational Database is intentionally isolated from execution and scheduling.

---

# Failure Handling

If the Operational Database is unavailable:

* Platform services cannot reliably persist new Operational State.
* Existing immutable Architectural Contracts remain unaffected.
* Validation execution may continue according to implementation-specific recovery policies.
* Operational failures are reported through platform observability.

Loss of the Operational Database does not invalidate immutable Architectural Contracts.

---

# Scalability

The Operational Database is designed to scale independently.

Operational query throughput and storage capacity may increase independently of:

* Builder
* Artifact Storage
* Artifact Manager
* Scheduler
* Validation Workers

---

# Observability

The Operational Database publishes telemetry describing:

* Database health
* Query performance
* Update throughput
* Storage utilization
* Replication status (if applicable)
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/scheduler.md`
* `docs/developer/services/worker.md`
* `docs/developer/services/dashboard.md`

## Related ADRs

* ADR-0010 — Operational Database
* ADR-0016 — Worker Host Identification
* ADR-0017 — Worker Capability Model
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
* ADR-0022 — Dashboard as a Read-Only Platform Service
