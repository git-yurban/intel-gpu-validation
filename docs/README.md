# Intel GPU Validation Lab

## Overview

The Intel GPU Validation Lab is a distributed platform for building, preparing, scheduling, and executing large-scale GPU validation workloads.

The platform is designed to support heterogeneous hardware, reproducible validation execution, and scalable automation while maintaining clear architectural boundaries between platform services.

The architecture follows an **architecture-first** approach. Architectural decisions are documented before implementation using Architecture Decision Records (ADRs), providing a stable foundation for long-term evolution.

---

# Goals

The platform is designed to:

* Scale to hundreds of validation Workers
* Support heterogeneous GPU platforms
* Produce reproducible validation executions
* Maximize Worker utilization
* Publish immutable Build artifacts
* Execute validation using stateless Workers
* Support independent evolution of platform services
* Maintain operational simplicity

---

# Non-Goals

The platform is **not** intended to be:

* A general-purpose CI/CD system
* A source code management platform
* A generic cluster scheduler
* A hardware provisioning system
* A build system for arbitrary software projects

---

# Architecture at a Glance

```
                    +--------------------+
                    |      Builder       |
                    +--------------------+
                              │
                              ▼
                    +--------------------+
                    | Artifact Storage   |
                    +--------------------+
                              │
                              ▼
                    +--------------------+
                    | Artifact Manager   |
                    +--------------------+
                              │
                              ▼
                    +--------------------+
                    |     Scheduler      |
                    +--------------------+
                              │
                              ▼
                    +--------------------+
                    |    Work Queue      |
                    +--------------------+
                              │
                              ▼
                    +--------------------+
                    |      Workers       |
                    +--------------------+
                              │
               ┌──────────────┴──────────────┐
               │                             │
               ▼                             ▼
    +--------------------+        +--------------------+
    | Operational DB     |        |     Telemetry      |
    +--------------------+        +--------------------+
               │                             │
               └──────────────┬──────────────┘
                              ▼
                    +--------------------+
                    |     Dashboard      |
                    +--------------------+
```

Additional architectural details are documented in `docs/architecture.md`.

---

# Core Concepts

| Concept               | Description                                              |
| --------------------- | -------------------------------------------------------- |
| Build                 | Immutable software produced by the Builder               |
| Build Manifest        | Canonical description of a published Build               |
| Worker Manifest       | Published execution plan produced by the Scheduler       |
| Worker Capability     | Published description of a Worker's validation resources |
| Execution Directory   | Prepared filesystem produced by the Artifact Manager     |
| Execution Environment | Isolated runtime environment created by a Worker         |
| Validation Execution  | Execution of a validation workload on a Worker           |

Canonical terminology is defined in `docs/glossary.md`.

---

# Platform Services

| Service              | Responsibility                                              |
| -------------------- | ----------------------------------------------------------- |
| Builder              | Produces published Builds and Build Manifests               |
| Artifact Storage     | Stores immutable published artifacts                        |
| Artifact Manager     | Resolves Build Manifests and prepares Execution Directories |
| Scheduler            | Plans validation execution and publishes Worker Manifests   |
| Work Queue           | Delivers Worker Manifests to Workers                        |
| Workers              | Execute validation and publish Worker Capabilities          |
| Operational Database | Owns persistent operational state                           |
| Telemetry            | Collects published telemetry for observability              |
| Dashboard            | Presents platform information                               |

---

# Repository Layout

```
.
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── SECURITY.md
├── LICENSE
│
├── docs/
│   ├── architecture.md
│   ├── system-context.md
│   ├── principles.md
│   ├── glossary.md
│   ├── architecture/
│   │   └── adr/
│   ├── developer/
│   ├── deployment/
│   ├── apis/
│   └── diagrams/
│
├── builder/
├── scheduler/
├── artifact-manager/
├── worker/
├── dashboard/
├── telemetry/
└── shared/
```

---

# Documentation

| Document                 | Purpose                                                 |
| ------------------------ | ------------------------------------------------------- |
| `docs/system-context.md` | Defines the platform boundary and external interactions |
| `docs/architecture.md`   | High-level architecture overview                        |
| `docs/principles.md`     | Architectural principles                                |
| `docs/glossary.md`       | Canonical domain terminology                            |
| `docs/architecture/adr/` | Architecture Decision Records (ADRs)                    |
| `docs/developer/`        | Component implementation guides                         |
| `docs/apis/`             | Service API specifications                              |
| `docs/deployment/`       | Deployment documentation                                |
| `docs/diagrams/`         | Architecture and sequence diagrams                      |

---

# Development Status

| Phase                     | Status         |
| ------------------------- | -------------- |
| Architecture              | ✅ Complete     |
| Documentation             | 🚧 In Progress |
| Reference Implementation  | ⏳ Planned      |
| Reference Deployment      | ⏳ Planned      |
| Dashboard                 | ⏳ Planned      |
| Telemetry & Observability | ⏳ Planned      |
| Production Readiness      | ⏳ Future       |

---

# Roadmap

The long-term project plan is documented in `ROADMAP.md`.

---

# Contributing

Contribution guidelines are documented in `CONTRIBUTING.md`.

All architectural changes should be documented using Architecture Decision Records (ADRs).

---

# Getting Started

To understand the project, read the documentation in the following order:

1. `docs/system-context.md`
2. `docs/architecture.md`
3. `docs/principles.md`
4. `docs/glossary.md`
5. `docs/architecture/adr/`

After reviewing the architecture, continue with the component-specific documentation in `docs/developer/`.

---

# License

See `LICENSE` for licensing information.


---

```
docs/
├── architecture/      ← System design
├── developer/
│   ├── services/      ← Service responsibilities
│   ├── platform/      ← Shared platform capabilities
│   ├── api/           ← Service interfaces
│   ├── contracts/     ← Data exchanged between services
│   └── models/        ← Shared value objects
└── adr/               ← Architectural decisions
```