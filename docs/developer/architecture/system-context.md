# System Context

## Purpose

The Intel GPU Validation Lab is a distributed platform for building, scheduling, and executing large-scale GPU validation workloads.

The platform is designed to validate graphics software across heterogeneous hardware and software environments while maintaining deterministic execution, high throughput, and long-term maintainability.

The architecture separates build generation, artifact management, scheduling, execution, operational state, and presentation into independent platform services with clearly defined responsibilities.

---

# Objectives

The platform is designed to:

* Scale to hundreds of Validation Workers.
* Execute millions of validation workloads.
* Support heterogeneous GPU hardware and software configurations.
* Produce deterministic and reproducible validation results.
* Enable independent deployment and evolution of platform services.
* Provide comprehensive operational visibility.

---

# Architectural Principles

The architecture is guided by several fundamental principles:

* Single responsibility.
* Explicit ownership.
* Immutable Architectural Contracts.
* Mutable Operational State.
* Transient Execution Resources.
* Stateless platform services where practical.
* Configuration over customization.

These principles are described in greater detail in `docs/principles.md` and the Architecture Decision Records.

---

# Platform Overview

The platform consists of independent services that collaborate through well-defined Architectural Contracts.

```text
                 Source Code
                      │
                      ▼
                  Builder
                      │
          Publish Build Manifest
          Publish Artifact Packages
                      │
                      ▼
              Artifact Storage
                      │
                      ▼
             Artifact Manager
                      │
Prepare Execution Directory
                      │
                      ▼
                 Scheduler
                      │
      Publish Worker Manifest
                      │
                      ▼
          Transient Work Queue
                      │
                      ▼
             Validation Worker
                      │
      Execute Validation Workload
                      │
                      ▼
        Validation Results
                      │
                      ▼
         Operational Database
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
Telemetry & Observability   Dashboard
```

---

# Platform Services

The platform consists of the following primary services:

| Service              | Responsibility                                         |
| -------------------- | ------------------------------------------------------ |
| Builder              | Produce Builds, Build Manifests, and Artifact Packages |
| Artifact Storage     | Store immutable published Artifact Packages            |
| Artifact Manager     | Prepare Execution Directories                          |
| Scheduler            | Coordinate validation execution                        |
| Validation Worker    | Execute validation workloads                           |
| Operational Database | Store mutable operational state                        |
| Dashboard            | Present operational information                        |

Each service owns exactly one architectural responsibility.

---

# Architectural Data Model

The platform classifies data into three categories:

| Category                          | Examples                                                          |
| --------------------------------- | ----------------------------------------------------------------- |
| Immutable Architectural Contracts | Build Manifest, Worker Manifest, Build Identity, Artifact Package |
| Mutable Operational State         | Validation status, Worker Capability, metrics                     |
| Transient Execution Resources     | Execution Directory, Execution Environment, Worker Artifact Cache |

Each category has a single authoritative owner.

---

# Service Interaction

Platform services communicate through immutable Architectural Contracts.

Runtime execution is coordinated through the Scheduler and executed by Validation Workers.

Operational State is maintained independently from Architectural Contracts.

Presentation is separated from platform operation through the Dashboard.

---

# Intended Audience

This document provides a high-level architectural overview for:

* Platform engineers
* New contributors
* Technical leads
* Architects
* Operations engineers

Implementation details are intentionally omitted and are documented elsewhere.
