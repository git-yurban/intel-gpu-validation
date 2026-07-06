# Artifact Storage

## Overview

Artifact Storage is the platform service responsible for storing and providing access to published Artifact Packages.

Artifact Storage becomes the authoritative owner of published Artifact Packages after successful publication by the Builder.

Artifact Storage is independent of build generation, scheduling, and validation execution.

---

# Responsibilities

Artifact Storage is responsible for:

* Receiving published Artifact Packages.
* Persisting published Artifact Packages.
* Providing access to published Artifact Packages through the Artifact Access API.
* Maintaining artifact integrity.
* Managing artifact lifecycle according to platform retention policy.

Artifact Storage's architectural responsibility begins after successful publication of Artifact Packages by the Builder.

---

# Architectural Responsibilities

Artifact Storage owns:

* Published Artifact Packages
* Artifact persistence
* Artifact retrieval
* Artifact retention

Artifact Storage does not own:

* Build generation
* Build Manifests
* Execution Directories
* Validation execution
* Operational State

These responsibilities belong to other platform services.

---

# Dependencies

Artifact Storage depends on:

* Published Artifact Packages from the Builder

Artifact Storage serves:

* Artifact Manager

Artifact Storage is independent of the Scheduler, Validation Workers, and the Operational Database.

---

# Inputs

Artifact Storage consumes:

* Published Artifact Packages

Publication format is defined by the Build Manifest.

---

# Outputs

Artifact Storage provides:

| Output                      | Classification                   |
| --------------------------- | -------------------------------- |
| Published Artifact Packages | Immutable Architectural Contract |
| Artifact Access API         | Platform service interface       |

Artifact Storage never modifies published Artifact Packages.

---

# Artifact Workflow

```text id="7fj91q"
Builder
    │
Publish Artifact Packages
    │
    ▼
Artifact Storage
    │
Persist
    │
    ▼
Artifact Access API
    │
Retrieve
    ▼
Artifact Manager
```

Successful publication transfers authoritative ownership of published Artifact Packages to Artifact Storage.

---

# Service Boundaries

Artifact Storage communicates through immutable published Artifact Packages.

It never:

* Builds software.
* Creates Build Manifests.
* Creates Execution Directories.
* Executes validation workloads.
* Owns Operational State.

Artifact Storage is intentionally isolated from build generation and runtime execution.

---

# Failure Handling

If artifact publication fails:

* Artifact ownership remains with the Builder.
* Artifact Packages are not considered published.
* Artifact retrieval is unavailable for failed publications.
* The failure is reported as Operational State.

From the perspective of the platform, publication is atomic.

Partial publication is not permitted.

---

# Scalability

Artifact Storage is designed to scale independently of the remainder of the platform.

Storage capacity and retrieval throughput may increase independently of:

* Builder
* Scheduler
* Validation Workers

---

# Observability

Artifact Storage publishes telemetry describing:

* Publication events
* Retrieval requests
* Storage utilization
* Integrity verification
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/builder.md`
* `docs/developer/services/artifact-manager.md`

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
* ADR-0013 — Builder as an Independent Service
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
