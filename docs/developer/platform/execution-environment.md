# Execution Environment

## Overview

The Execution Environment defines the isolated runtime in which a validation workload executes.

It combines a prepared Execution Directory with the runtime resources required for execution, providing a deterministic and isolated environment for a single validation workload.

The Execution Environment is a shared platform concept rather than a platform service.

---

# Purpose

The Execution Environment enables the platform to:

* Execute validation workloads in isolation.
* Preserve deterministic execution.
* Prevent interference between workloads.
* Support reliable cleanup after execution.

Each Execution Environment exists only for the lifetime of a single validation workload.

---

# Architectural Role

The Execution Environment provides:

* Runtime isolation.
* Access to a prepared Execution Directory.
* Temporary execution resources.
* Controlled lifecycle management.

The Execution Environment does not:

* Prepare Execution Directories.
* Schedule validation workloads.
* Store Operational State.
* Persist Artifact Packages.

Those responsibilities remain with the appropriate platform services.

---

# Participants

| Component            | Responsibility                              |
| -------------------- | ------------------------------------------- |
| Artifact Manager     | Prepare Execution Directory                 |
| Validation Worker    | Create and manage the Execution Environment |
| Operational Database | Receive validation results                  |

Each participant performs a single architectural responsibility.

---

# Execution Lifecycle

```text
Artifact Packages
        │
        ▼
Artifact Manager
        │
Prepare Execution Directory
        │
        ▼
Execution Directory
        │
        ▼
Validation Worker
        │
Create Execution Environment
        │
Execute Validation Workload
        │
Publish Validation Results
        │
Cleanup
        ▼
Execution Environment Removed
```

The Execution Environment exists only while a validation workload is executing.

---

# Execution Directory

Every Execution Environment contains a prepared Execution Directory.

The Execution Directory:

* Is created by the Artifact Manager.
* Contains the files required for execution.
* Is a transient execution resource.
* Is never a published artifact.

The Validation Worker consumes the Execution Directory but does not prepare it.

---

# Isolation Model

Each validation workload executes in its own isolated Execution Environment.

Isolation prevents:

* File system interference.
* Runtime interference.
* Resource contamination between workloads.

Isolation contributes to deterministic validation results.

---

# Lifecycle

An Execution Environment progresses through the following stages:

1. Creation.
2. Validation execution.
3. Result publication.
4. Cleanup.
5. Destruction.

Execution Environments are never reused between validation workloads.

---

# Design Principles

Execution Environments should be:

* Isolated.
* Deterministic.
* Disposable.
* Reproducible.
* Independent of previous executions.

All execution resources are considered transient.

---

# Failure Handling

If validation execution fails:

* Validation results record the failure.
* Cleanup is still performed.
* Temporary resources are removed.
* The Execution Environment is destroyed.

Cleanup occurs regardless of execution outcome.

---

# Scalability

Execution Environments scale with Validation Workers.

Each Validation Worker manages the lifecycle of the Execution Environments it creates.

The platform supports concurrent Execution Environments across multiple Worker Hosts.

---

# Observability

Platform services publish telemetry describing:

* Execution Environment creation.
* Validation execution.
* Execution duration.
* Cleanup.
* Failures.

Telemetry supports observability but is not part of the Execution Environment itself.

---

# Relationship to Platform Services

The Execution Environment is created and managed by the Validation Worker.

It consumes the Execution Directory prepared by the Artifact Manager.

It produces validation results that become Operational State.

The Execution Environment owns no persistent platform data.

---

# Related Documentation

* `docs/architecture.md`
* `docs/principles.md`
* `docs/glossary.md`
* `docs/developer/services/artifact-manager.md`
* `docs/developer/services/worker.md`

## Related ADRs

* ADR-0005 — Artifact Storage
* ADR-0011 — Execution Environment Isolation
* ADR-0012 — Stateless Workers
* ADR-0020 — Data Classification
