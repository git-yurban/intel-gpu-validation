# Intel GPU Validation Lab

**Living Engineering Handoff**

Version: 0.1.0

Status: Active Development

Last Updated: July 2026

---

# Executive Summary

## Purpose

The Intel GPU Validation Lab is a distributed test execution platform designed to validate Intel graphics software across hundreds of physical Linux systems.

The platform automates the entire validation pipeline from source code changes to test execution while maximizing hardware utilization and minimizing operational overhead.

Unlike traditional CI systems that statically assign jobs to workers, this project uses dynamic work scheduling and artifact distribution to keep every validation machine continuously productive.

The platform is designed to support:

- Mesa
- Vulkan CTS
- Piglit
- IGT
- Future validation suites

while remaining scalable, fault tolerant, and cloud-native.

---

# Vision

The guiding philosophy of this project is:

> **Build once. Test everywhere.**

Every software component is built exactly once.

Those build outputs become immutable artifacts that are distributed to every worker participating in the validation campaign.

Workers never compile software.

Workers never make scheduling decisions.

Workers simply execute validated workloads.

This separation dramatically improves scalability while reducing complexity.

---

# Project Goals

The project has several primary objectives.

## Scalability

Support hundreds of simultaneously connected Intel GPU systems without requiring architectural redesign.

Horizontal scaling should primarily consist of adding additional workers.

---

## High Hardware Utilization

Workers continuously request additional work.

No worker should remain idle while executable work exists.

Target utilization:

> Greater than 95%

---

## Fault Tolerance

Worker failures are expected.

The scheduler automatically detects abandoned work and redistributes unfinished shards.

No manual intervention should be required.

---

## Deterministic Builds

Every artifact is immutable.

Artifacts are identified by their originating Git revision and accompanying manifest.

Artifacts are never modified after publication.

---

## Reproducibility

Every validation run must be reproducible.

Given:

- Build Manifest
- Worker Manifest
- Test Results

another engineer should be able to reproduce the exact execution environment.

---

# Design Philosophy

Several architectural principles guide every implementation decision.

## Single Responsibility

Each major component owns exactly one responsibility.

| Component | Responsibility |
|----------|----------------|
| Buildbot | Build software |
| Builder | Package artifacts |
| MinIO | Store artifacts |
| Scheduler | Schedule work |
| Redis | Queue shards |
| Worker | Execute tests |
| PostgreSQL | Persist metadata |
| MQTT | Publish telemetry |

Responsibilities intentionally do not overlap.

---

## Immutable Artifacts

Artifacts never change after publication.

If Mesa changes, a completely new artifact is produced.

Workers therefore never need to determine whether an existing artifact has changed.

---

## Stateless Workers

Workers maintain no persistent execution state.

A worker may disappear at any time.

Another worker must be capable of continuing execution using only the manifests and persistent scheduler state.

---

## Scheduler Owns Scheduling

Scheduling decisions belong exclusively to the scheduler.

Workers never decide:

- what to execute
- when to execute
- retry policies
- prioritization

Workers only execute assigned work.

---

## Contracts Before Code

Every subsystem communicates using versioned manifests.

Examples include:

- Build Manifest
- Worker Manifest

These manifests form stable interfaces between independently evolving components.

---

# High-Level Architecture

```
                 Git Push
                     │
                     ▼
                GitLab / GitHub
                     │
                     ▼
                 Buildbot CI
                     │
                     ▼
              Builder Publisher
                     │
                     ▼
      Build Manifest + Artifacts
                     │
                     ▼
                   MinIO
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
    Scheduler              Artifact Manager
         │                       │
         ▼                       ▼
       Redis                 Local Cache
         │
         ▼
     Worker Daemons
         │
         ├──────────► MQTT
         │
         └──────────► PostgreSQL
```

---

# Repository Overview

The repository is organized around responsibilities rather than technologies.

```
common/
```

Shared libraries used throughout the project.

Includes:

- artifact definitions
- storage interfaces
- schemas
- common utilities

---

```
common/artifact_manager/
```

Runtime implementation responsible for:

- downloading artifacts
- cache management
- verification
- extraction
- lifecycle management

---

```
builder/
```

Produces immutable artifacts.

Responsibilities include:

- packaging
- manifest generation
- uploads
- checksum calculation

---

```
scheduler/
```

Owns campaign creation and work scheduling.

Future responsibilities include:

- worker registration
- shard generation
- retries
- queue management

---

```
worker/
```

Executes validation workloads.

Workers:

- download manifests
- prepare artifacts
- execute tests
- upload results
- publish telemetry

---

# Current Project Status

Current implementation phase:

> Foundation

Completed:

- Repository structure
- Manifest models
- Artifact interfaces
- Storage abstraction
- Initial tests
- Documentation
- JSON schemas

In Progress:

- Artifact Manager
- Build Manifest implementation

Upcoming:

- Builder Publisher
- MinIO backend
- Worker cache
- Scheduler

---

# Engineering Philosophy

This repository intentionally prioritizes architecture over rapid implementation.

The objective is not merely to produce working software.

The objective is to produce software that remains maintainable after years of continuous development.

Every commit should leave the repository in a better state than before.

Every abstraction should remove future complexity rather than introduce it.

Long-term maintainability is valued over short-term convenience.

---

# Next Document

Continue with:

```
02-system-architecture.md
```

This document describes every major subsystem, their interactions, ownership boundaries, and communication contracts.