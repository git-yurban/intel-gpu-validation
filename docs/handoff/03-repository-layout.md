# Repository Layout

**Document:** 03-repository-layout.md

---

# Purpose

This document describes the repository organization for the Intel GPU Validation Lab.

The repository is intentionally organized around **responsibilities**, not technologies.

Every package has a clearly defined owner and purpose.

This organization minimizes coupling while making future development predictable.

---

# Repository Philosophy

The repository follows several guiding principles.

- One package, one responsibility
- Shared code belongs in `common`
- Runtime components remain independent
- Public interfaces are versioned
- Documentation lives alongside implementation
- Tests mirror package structure

A contributor should always know where new code belongs.

---

# Top-Level Layout

```
intel-gpu-validation/

├── .github/
│   └── workflows/
│
├── builder/
│
├── scheduler/
│
├── worker/
│
├── common/
│
├── docs/
│
├── schemas/
│
├── tests/
│
├── docker/
│
├── k8s/
│
├── scripts/
│
├── pyproject.toml
├── README.md
└── Makefile
```

Not every directory exists today.

Some are placeholders for future milestones.

The architecture should be visible from the repository root.

---

# Builder

```
builder/
```

Responsible for publishing build outputs.

Future responsibilities include:

- Package build outputs
- Generate Build Manifest
- Create compressed archives
- Calculate checksums
- Upload artifacts
- Upload manifests

Builder never schedules work.

Builder never communicates with workers.

---

# Scheduler

```
scheduler/
```

Owns scheduling.

Responsibilities include:

- Campaign creation
- Worker registration
- Capability matching
- Shard generation
- Retry logic
- REST API

Scheduler is the only component allowed to make scheduling decisions.

---

# Worker

```
worker/
```

Runs on every validation machine.

Responsibilities include:

- Register with Scheduler
- Download Worker Manifest
- Request artifacts from Artifact Manager
- Execute tests
- Upload results
- Publish telemetry

Workers intentionally remain stateless.

---

# Common

```
common/
```

Contains code shared by multiple components.

Nothing in `common` should depend on Builder, Scheduler or Worker.

Shared packages include:

```
common/

    artifacts/

    artifact_manager/

    naming/

    utils/
```

---

# common/artifacts

Defines the artifact contract.

Responsibilities:

- Models
- Manifest parsing
- Storage interfaces
- Enumerations
- Validation
- JSON schemas

This package answers:

> What is an artifact?

It does not download or manage artifacts.

---

# common/artifact_manager

Implements artifact lifecycle.

Responsibilities:

- Downloads
- Verification
- Extraction
- Cache management
- Cleanup
- Reference counting

This package answers:

> How are artifacts prepared for execution?

---

# common/naming

Recommended future package.

Responsible for deterministic naming.

Examples:

```
artifact_name()

manifest_name()

build_name()

cache_directory()
```

No other package should manually build filenames.

---

# Documentation

```
docs/
```

Repository documentation.

Suggested layout:

```
docs/

    handoff/

    specs/

    adr/

    diagrams/
```

---

## handoff/

Living engineering documentation.

Explains:

- Architecture
- Components
- Design decisions
- Roadmap

---

## specs/

Machine-readable specifications.

Examples:

- Build Manifest
- Worker Manifest
- REST API

---

## adr/

Architecture Decision Records.

Each significant architectural decision receives its own ADR.

Example:

```
ADR-0001

Use MinIO for immutable artifact storage
```

---

## diagrams/

Mermaid and exported architecture diagrams.

Should remain synchronized with documentation.

---

# Schemas

```
schemas/
```

Contains JSON schemas used for validation.

Examples:

```
build-manifest.schema.json

worker-manifest.schema.json
```

Schemas define stable contracts between components.

---

# Tests

```
tests/
```

Tests mirror the package structure.

Example:

```
common/artifacts/

↓

tests/test_manifest.py
```

Avoid deeply nested test hierarchies.

Tests should remain easy to locate.

---

# Docker

```
docker/
```

Future container definitions.

Suggested layout:

```
docker/

    builder/

    scheduler/

    worker/

    dashboard/
```

Each component receives an independent container image.

---

# Kubernetes

```
k8s/
```

Contains deployment manifests.

Future resources include:

- Deployments
- StatefulSets
- Services
- ConfigMaps
- Secrets
- Ingress
- DaemonSets

---

# Scripts

```
scripts/
```

Repository utilities.

Examples:

- Bootstrap development environment
- Format code
- Generate schemas
- Publish artifacts

Scripts should never contain production logic.

---

# Package Dependencies

The dependency graph intentionally flows one direction.

```
                    common
                      ▲
      ┌───────────────┼───────────────┐
      │               │               │
      │               │               │
   Builder       Scheduler       Worker
                                      │
                                      ▼
                             Artifact Manager
```

No runtime component should depend on another runtime component.

Only `common` may be shared.

---

# Import Rules

Allowed:

```
Builder
    ↓
common.artifacts
```

Allowed:

```
Worker
    ↓
common.artifact_manager
```

Not allowed:

```
Worker
    ↓
Scheduler
```

Not allowed:

```
Scheduler
    ↓
Builder
```

Runtime components communicate through APIs, manifests and storage.

Never through direct imports.

---

# Coding Standards

All production code should follow:

- Python 3.12+
- Full type hints
- Ruff clean
- MyPy clean
- Pydantic v2
- pytest

Every public function should include a docstring.

Business logic should remain testable without external services.

---

# Repository Growth

As the project grows, packages should expand internally rather than adding new top-level directories.

Example:

```
common/artifact_manager/

    cache/

    download/

    verify/

    extract/
```

This preserves a clean repository root.

---

# Repository Ownership

| Package | Owner |
|----------|-------|
| builder | Build pipeline |
| scheduler | Scheduling |
| worker | Execution |
| common.artifacts | Artifact contracts |
| common.artifact_manager | Artifact lifecycle |
| docs | Documentation |
| schemas | Stable interfaces |
| tests | Validation |

Ownership should remain exclusive.

If two packages appear to own the same responsibility, the architecture should be reconsidered.

---

# Design Principle

Repository structure should reflect system architecture.

A developer unfamiliar with the project should understand the major components simply by inspecting the repository tree.

Good organization reduces documentation requirements and prevents architectural drift.

---

# Next Document

Continue with:

```
04-builder.md
```

This document describes the Builder subsystem, artifact publication pipeline, manifest generation, and MinIO integration.