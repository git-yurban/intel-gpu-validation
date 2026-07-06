# Builder

## Overview

The Builder is responsible for producing published Builds from source code.

It creates immutable Build Manifests and Artifact Packages that become the inputs for validation.

The Builder is an independent platform service whose sole architectural responsibility is build generation and publication.

---

# Responsibilities

The Builder is responsible for:

* Producing Builds.
* Assigning Build Identities.
* Creating Build Manifests.
* Creating Artifact Packages.
* Publishing Build Manifests.
* Publishing Artifact Packages.

The Builder's architectural responsibility ends after successful publication of the Build Manifest and Artifact Packages.

---

# Architectural Responsibilities

The Builder owns:

* Build generation
* Build Identity creation
* Build Manifest creation
* Artifact Package creation

The Builder does not own:

* Artifact Storage
* Execution Directories
* Validation scheduling
* Validation execution
* Operational State

These responsibilities belong to other platform services.

---

# Dependencies

The Builder depends on:

* Source code repositories
* Artifact Storage

The Builder does not depend on the Scheduler, Validation Workers, or the Operational Database to perform build generation.

---

# Inputs

The Builder consumes:

* Source code
* Build configuration
* Build parameters

The representation of these inputs is an implementation decision.

---

# Outputs

The Builder produces:

| Output            | Classification                   |
| ----------------- | -------------------------------- |
| Build Identity    | Immutable Architectural Contract |
| Build Manifest    | Immutable Architectural Contract |
| Artifact Packages | Immutable published artifacts    |

After publication, Artifact Storage becomes the authoritative owner of published Artifact Packages.

---

# Build Workflow

```text
Source Code
     │
     ▼
Build Configuration
     │
     ▼
Builder
     │
Create Build
     │
Assign Build Identity
     │
Create Build Manifest
     │
Create Artifact Packages
     │
Publish
     ▼
Artifact Storage
```

Publication marks the completion of the Builder's architectural responsibility.

---

# Service Boundaries

The Builder communicates through immutable Architectural Contracts.

It never:

* Executes validation workloads.
* Schedules validation.
* Prepares Execution Directories.
* Maintains Worker state.
* Owns Operational State.

The Builder is intentionally isolated from runtime execution.

---

# Failure Handling

If build generation or publication fails:

* No Build is published.
* No Build Manifest is published.
* No Artifact Packages are published.
* The failure is reported as Operational State.

From the perspective of the platform, publication is atomic.

Partial publication is not permitted.

---

# Scalability

The Builder is designed to scale independently of the remainder of the platform.

Build throughput may increase by adding Builder capacity without changing:

* Artifact Storage
* Scheduler
* Validation Workers

---

# Observability

The Builder publishes telemetry describing:

* Build lifecycle events
* Build duration
* Build failures
* Publication events
* Service health

Telemetry supports observability but is not Operational State.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0007 — Build Identity
* ADR-0013 — Builder as an Independent Service
* ADR-0020 — Data Classification
* ADR-0021 — Telemetry and Observability
