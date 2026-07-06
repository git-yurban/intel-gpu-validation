# System Architecture

**Document:** 02-system-architecture.md

---

# Purpose

This document describes the overall architecture of the Intel GPU Validation Lab.

It defines:

- System components
- Ownership boundaries
- Communication paths
- Data flow
- Failure recovery
- Scaling strategy

The architecture intentionally separates build orchestration, artifact management, scheduling, and execution into independent subsystems.

---

# Architectural Goals

The architecture is designed around several non-negotiable goals.

- Horizontal scalability
- Fault tolerance
- Immutable artifacts
- Stateless workers
- Deterministic execution
- Independent deployment
- Clear ownership boundaries

Every subsystem should remain independently replaceable.

---

# High-Level System Overview

```
                     Git Push
                         │
                         ▼
                  GitLab / GitHub
                         │
                    Webhook Event
                         │
                         ▼
                     Buildbot CI
                         │
                         ▼
                 Builder Publisher
                         │
         ┌───────────────┴────────────────┐
         ▼                                ▼
 Build Manifest                   Artifact Archives
         │                                │
         └───────────────┬────────────────┘
                         ▼
                      MinIO
                         │
             Scheduler discovers builds
                         │
                         ▼
                Campaign Generation
                         │
                  Generate Shards
                         │
                         ▼
                      Redis Queue
                         │
              Workers continuously poll
                         │
                         ▼
                 Artifact Manager
                         │
              Local Artifact Cache
                         │
                         ▼
                 Test Execution
                         │
        ┌────────────────┴───────────────┐
        ▼                                ▼
 PostgreSQL                       MQTT Telemetry
```

---

# Component Overview

The platform consists of seven primary subsystems.

| Component | Responsibility |
|-----------|----------------|
| Buildbot | Build software |
| Builder | Package artifacts and publish manifests |
| MinIO | Immutable artifact storage |
| Scheduler | Campaign management and shard scheduling |
| Redis | Work queue |
| Worker | Execute test shards |
| Artifact Manager | Download, verify, cache and prepare artifacts |

Each subsystem owns one responsibility.

---

# Buildbot

## Purpose

Buildbot compiles software.

It is responsible for transforming source code into executable binaries.

Buildbot does **not** understand:

- workers
- campaigns
- scheduling
- retries

Its only responsibility is producing build outputs.

---

## Inputs

- Git repository
- Branch
- Commit
- Build configuration

---

## Outputs

- Compiled binaries
- Test binaries
- Build logs

These outputs are handed to the Builder.

---

# Builder

## Purpose

The Builder converts compiled outputs into immutable deployment artifacts.

Responsibilities include:

- packaging
- checksum calculation
- manifest generation
- uploads
- publication

---

## Builder Outputs

Example:

```
mesa-main-4f2c9b8d.tar.zst
mesa-main-4f2c9b8d.json
```

Both are uploaded to MinIO.

The manifest becomes the authoritative description of the artifact.

---

# MinIO

## Purpose

MinIO is the permanent artifact repository.

Workers never receive binaries directly from Buildbot.

Instead they download published artifacts from MinIO.

---

## Stored Objects

```
artifacts/

    mesa/

        main/

            mesa-main-4f2c9b8d.tar.zst

            mesa-main-4f2c9b8d.json

        feature-x/

            mesa-feature-x-a71be22f.tar.zst

            mesa-feature-x-a71be22f.json
```

Artifacts are immutable.

---

# Scheduler

## Purpose

The Scheduler owns every scheduling decision.

Workers never choose work.

The Scheduler decides:

- campaign creation
- shard generation
- worker eligibility
- retries
- prioritization
- completion

---

## Inputs

- Build Manifest
- Campaign configuration
- Worker capabilities

---

## Outputs

- Worker Manifest
- Redis work items

---

# Redis

Redis acts exclusively as a distributed work queue.

It is **not** a database.

Redis stores:

- pending shards
- claimed shards
- abandoned shards

Scheduler remains the source of truth.

---

# Worker

Every validation machine runs exactly one Worker daemon.

Workers are intentionally simple.

Worker responsibilities:

- register capabilities
- request work
- download manifests
- prepare artifacts
- execute tests
- upload results
- publish telemetry

Workers remain stateless.

---

# Artifact Manager

The Artifact Manager prepares software for execution.

Responsibilities:

- download artifacts
- cache artifacts
- verify SHA256
- extract archives
- reference counting
- cache cleanup

It does **not** execute tests.

It only prepares execution environments.

---

# PostgreSQL

Persistent metadata storage.

Stores:

- campaigns
- workers
- shards
- results
- history

Unlike Redis, PostgreSQL is authoritative.

---

# MQTT

MQTT carries operational telemetry only.

Examples:

```
worker/heartbeat

worker/status

worker/performance

worker/events
```

Scheduling must never depend on MQTT.

If MQTT becomes unavailable, validation continues.

---

# Communication Flow

The system communicates using immutable contracts.

```
Buildbot
      │
      ▼
Build Manifest
      │
      ▼
Scheduler
      │
      ▼
Worker Manifest
      │
      ▼
Worker
```

No subsystem reaches into another subsystem's internals.

Communication occurs exclusively through manifests, APIs, queues or storage.

---

# Ownership Boundaries

Ownership is intentionally strict.

| Component | Owns |
|-----------|------|
| Buildbot | compilation |
| Builder | packaging |
| MinIO | storage |
| Scheduler | scheduling |
| Redis | queueing |
| Worker | execution |
| Artifact Manager | artifact lifecycle |
| PostgreSQL | persistence |
| MQTT | telemetry |

Violating ownership boundaries introduces coupling and should be avoided.

---

# Failure Recovery

Worker failure:

```
Worker dies

↓

Heartbeat expires

↓

Scheduler marks shard abandoned

↓

Redis requeues shard

↓

Another worker resumes execution
```

No operator intervention required.

---

# Scaling Strategy

The architecture scales horizontally.

Increasing lab capacity requires only:

- additional workers

No scheduler redesign should be necessary.

Workers remain independent.

---

# Future Components

Future additions include:

- REST API
- Web Dashboard
- Prometheus
- Grafana
- Kubernetes Operator
- Multi-site federation

These additions should integrate without changing existing subsystem responsibilities.

---

# Guiding Principle

Every component should be understandable in isolation.

Every interface should be stable.

Every artifact should be immutable.

Every worker should be replaceable.

This philosophy minimizes coupling while maximizing scalability and maintainability.

---

# Next Document

Continue with:

```
03-repository-layout.md
```

This document describes the repository organization, package structure, coding standards, and module responsibilities.