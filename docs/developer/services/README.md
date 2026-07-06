# Platform Services

## Purpose

This directory contains the implementation guides for each platform service in the Intel GPU Validation Lab.

Each document describes the responsibilities, interfaces, implementation guidance, and operational considerations for a single service.

These guides complement the architecture documentation and should be read after the core architectural documents.

---

# Before Reading

Developers should first become familiar with the project architecture by reading:

1. `README.md`
2. `docs/system-context.md`
3. `docs/architecture.md`
4. `docs/principles.md`
5. `docs/glossary.md`
6. Architecture Decision Records (ADRs)
7. `docs/developer/overview.md`
8. `docs/developer/shared.md`

The service guides assume familiarity with these documents.

---

# Service Documentation

| Service                   | Description                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------- |
| `builder.md`              | Produces immutable Builds, Artifact Packages, and Build Manifests                                 |
| `artifact-storage.md`     | Stores and serves immutable published artifacts                                                   |
| `artifact-manager.md`     | Resolves Build Manifests and prepares Execution Directories                                       |
| `scheduler.md`            | Plans validation execution and publishes Worker Manifests                                         |
| `worker.md`               | Prepares Execution Environments, executes validation workloads, and publishes Worker Capabilities |
| `operational-database.md` | Owns persistent operational state                                                                 |
| `telemetry.md`            | Collects, stores, and exposes platform telemetry                                                  |
| `dashboard.md`            | Presents operational visibility through a read-only user interface                                |

Each guide focuses on one platform service and follows a common structure.

---

# Common Structure

Every service guide includes:

- Component metadata
- Purpose
- Responsibilities
- Inputs
- Published Objects
- Execution Flow
- Configuration
- Failure Handling
- Observability
- Testing
- Implementation Notes
- Future Evolution
- Summary

This consistent structure makes it easier to understand and compare services across the platform.

---

# Service Relationships

The platform is composed of independently deployable services that communicate through published architectural objects.

Each service:

* Owns its architectural responsibilities.
* Publishes immutable objects when appropriate.
* Consumes published objects from other services.
* Avoids direct ownership of another service's data.
* Evolves independently through stable architectural contracts.

Developers should preserve these boundaries when implementing or extending platform services.

---

# Architectural Responsibility

The implementation guides describe **how each service fulfills its architectural responsibilities**.

They do not redefine the architecture.

Architectural changes should be proposed and documented through the ADR process before implementation.

---

# Summary

Each platform service has a single architectural responsibility and evolves independently within the boundaries established by the project architecture.

Together, these implementation guides provide the engineering details needed to build and maintain the Intel GPU Validation Lab while preserving the architecture documented throughout the project.
