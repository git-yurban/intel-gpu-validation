# Artifact Manager

## Overview

The Artifact Manager is responsible for preparing Execution Directories from published Artifact Packages.

It retrieves immutable published artifacts through the Artifact Access API, assembles the files required for execution, and produces a transient Execution Directory for use by a Validation Worker.

The Artifact Manager does not execute validation workloads or own published artifacts.

---

# Responsibilities

The Artifact Manager is responsible for:

* Retrieving published Artifact Packages.
* Resolving Build Manifest references.
* Preparing Execution Directories.
* Verifying artifact integrity before preparation.
* Returning an Execution Directory Reference to the Scheduler.

The Artifact Manager's architectural responsibility ends after successfully preparing the Execution Directory and returning its reference.

---

# Architectural Responsibilities

The Artifact Manager owns:

* Execution Directory preparation
* Artifact retrieval
* Execution Directory assembly

The Artifact Manager does not own:

* Build generation
* Published Artifact Packages
* Validation scheduling
* Validation execution
* Operational State

These responsibilities belong to other platform services.

---

# Dependencies

The Artifact Manager depends on:

* Artifact Storage
* Artifact Access API
* Build Manifest

The Artifact Manager serves:

* Scheduler

The Artifact Manager is independent of the Builder, Validation Workers, and the Operational Database.

---

# Inputs

The Artifact Manager consumes:

* Build Manifest
* Published Artifact Packages

These inputs are immutable Architectural Contracts.

---

# Outputs

The Artifact Manager produces:

| Output                        | Classification               |
| ----------------------------- | ---------------------------- |
| Execution Directory           | Transient Execution Resource |
| Execution Directory Reference | Transient platform reference |

Execution Directories are never published artifacts and are never shared between validation workloads.

---

# Preparation Workflow

```text id="u4i7eu"
Scheduler
     │
Request Execution Directory
     │
     ▼
Artifact Manager
     │
Read Build Manifest
     │
Retrieve Artifact Packages
     │
Verify Integrity
     │
Prepare Execution Directory
     │
Return Execution Directory Reference
     ▼
Scheduler
```

The Execution Directory is prepared before scheduling completes.

---

# Service Boundaries

The Artifact Manager communicates using immutable Architectural Contracts and produces transient Execution Resources.

It never:

* Builds software.
* Publishes Artifact Packages.
* Schedules validation.
* Executes validation workloads.
* Owns Operational State.

The Artifact Manager is intentionally isolated from runtime execution.

---

# Failure Handling

If preparation fails:

* No Execution Directory is produced.
* No Execution Directory Reference is returned.
* Validation cannot be scheduled for execution.
* The failure is reported as Operational State.

Execution Directories are created only after successful artifact retrieval and integrity verification.

---

# Scalability

The Artifact Manager is designed to scale independently of the remainder of the platform.

Preparation throughput may increase independently of:

* Builder
* Artifact Storage
* Scheduler
* Validation Workers

---

# Observability

The Artifact Manager publishes telemetry describing:

* Artifact retrieval operations
* Execution Directory preparation
* Integrity verification
* Preparation failures
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/builder.md`
* `docs/developer/services/artifact-storage.md`
* `docs/developer/services/scheduler.md`

## Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
* ADR-0011 — Execution Environment Isolation
* ADR-0013 — Builder as an Independent Service
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
