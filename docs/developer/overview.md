# Developer Overview

## Purpose

This document introduces the implementation architecture of the Intel GPU Validation Lab.

It explains how the platform is organized from a developer's perspective and provides guidance for implementing platform services while preserving the architectural principles documented throughout the project.

This document complements, but does not replace, the architecture documentation.

---

# Audience

This document is intended for developers implementing, extending, or maintaining the Intel GPU Validation Lab.

It serves as the entry point to the developer documentation and should be read before the component-specific implementation guides.

---

# Prerequisites

Developers should understand the platform architecture before implementing platform services.

Recommended reading order:

1. `README.md`
2. `docs/system-context.md`
3. `docs/architecture.md`
4. `docs/principles.md`
5. `docs/glossary.md`
6. Architecture Decision Records (ADRs)

Implementation should conform to the documented architecture.

---

# Developer Documentation

The implementation guidance for each platform component is documented separately.

| Document                  | Purpose                                                        |
| ------------------------- | -------------------------------------------------------------- |
| `shared.md`               | Common implementation guidance shared by all platform services |
| `builder.md`              | Builder implementation                                         |
| `artifact-storage.md`     | Artifact Storage implementation                                |
| `artifact-manager.md`     | Artifact Manager implementation                                |
| `scheduler.md`            | Scheduler implementation                                       |
| `worker.md`               | Worker implementation                                          |
| `operational-database.md` | Operational Database implementation                            |
| `telemetry.md`            | Telemetry implementation                                       |
| `dashboard.md`            | Dashboard implementation                                       |

Developers should read this overview before the component-specific guides.

---

# Architecture Philosophy

The Intel GPU Validation Lab follows an **architecture-first** development model.

Architecture defines:

* Responsibilities
* Ownership
* Published objects
* Service interactions
* Engineering principles

Implementation selects technologies while preserving the architecture.

Developers should avoid introducing implementation details that redefine architectural responsibilities.

---

# Platform Overview

## Platform Services

The platform consists of independently deployable services.

| Service              | Responsibility                                                                      |
| -------------------- | ----------------------------------------------------------------------------------- |
| Builder              | Produces Builds and Build Manifests                                                 |
| Artifact Storage     | Stores immutable published artifacts                                                |
| Artifact Manager     | Resolves Build Manifests and prepares Execution Directories                         |
| Scheduler            | Plans validation execution and publishes Worker Manifests                           |
| Work Queue           | Delivers Worker Manifests                                                           |
| Workers              | Prepare Execution Environments, execute validation, and publish Worker Capabilities |
| Operational Database | Owns persistent operational state                                                   |
| Telemetry            | Collects published telemetry                                                        |
| Dashboard            | Presents platform information                                                       |

Every service has a single architectural responsibility.

### Published Objects

Platform services communicate by publishing immutable architectural objects.

| Published Object  | Owner     |
| ----------------- | --------- |
| Build             | Builder   |
| Artifact Package  | Builder   |
| Build Manifest    | Builder   |
| Worker Manifest   | Scheduler |
| Worker Capability | Workers   |

Published objects define the contracts between platform services.

### Communication Model

Platform services communicate through published objects and well-defined interfaces.

Developers should prefer:

* Published contracts
* Stable interfaces
* Loose coupling

Developers should avoid:

* Shared mutable state
* Cross-service implementation dependencies
* Direct access to another service's internal state

---

# Repository Organization

The repository is organized by platform service.

```text
builder/
artifact-storage/
artifact-manager/
scheduler/
worker/
operational-database/
telemetry/
dashboard/
shared/
docs/
```

Each service should evolve independently while maintaining stable architectural contracts.

---

# Shared Components

Common functionality belongs in the `shared/` directory.

Examples include:

* Configuration
* Logging
* Common data models
* Serialization
* Error handling
* Metrics
* Testing utilities

Business logic should remain within the owning service.

---

# Implementation Guidelines

## Configuration

Platform behavior is controlled through configuration.

Configuration should:

* Be explicit
* Be documented
* Be environment specific
* Preserve architectural responsibilities

Configuration must not redefine service ownership or architectural boundaries.

---

## Logging

Every platform service should produce structured, meaningful logs.

Logging should:

* Describe significant events
* Include sufficient operational context
* Support troubleshooting
* Avoid exposing sensitive information

Logging should complement telemetry rather than replace it.

---

## Error Handling

Errors should be:

* Detectable
* Actionable
* Logged with context
* Recoverable where practical

Services should fail predictably and expose sufficient diagnostic information through telemetry.

---

## Observability

Every platform service should publish telemetry describing:

* Health
* Activity
* Performance
* Failures

Telemetry supports operational visibility and troubleshooting.

Telemetry should never become a dependency for platform operation.

---

## Testing

Each service should include testing appropriate to its responsibilities.

Testing may include:

* Unit tests
* Integration tests
* End-to-end validation
* Performance testing

Testing should validate behavior rather than implementation details.

---

## Documentation

Implementation documentation should evolve alongside the code.

Developers should update documentation whenever changes affect:

* APIs
* Configuration
* Deployment
* Operations
* User-visible behavior

Architectural changes require updates to the appropriate ADRs.

---

# Development Workflow

Typical implementation workflow:

```text
Review Architecture
        │
        ▼
Review Relevant ADRs
        │
        ▼
Implement Service
        │
        ▼
Add Tests
        │
        ▼
Update Documentation
        │
        ▼
Submit for Review
```

Documentation and tests are considered part of the implementation.

---

# Extending the Platform

Before extending the platform, consider:

* Can the capability be implemented within an existing service?
* Does the change preserve a single responsibility?
* Does it introduce a new published object?
* Does it establish a new architectural boundary?
* Does it preserve explicit ownership?
* Does it reduce or increase operational complexity?

Architectural changes should be documented with an ADR before implementation.

Implementation should extend the existing architecture rather than introduce parallel concepts or duplicate responsibilities.

---

# Summary

The Intel GPU Validation Lab is designed to evolve through stable architectural contracts and independently deployable services.

Developers should:

* Preserve architectural responsibilities.
* Communicate through published objects.
* Prefer configuration over customization.
* Maintain explicit ownership.
* Keep implementations simple, testable, and maintainable.
* Update documentation as the implementation evolves.

The architecture defines **what** the platform is.

The implementation defines **how** it is built.
