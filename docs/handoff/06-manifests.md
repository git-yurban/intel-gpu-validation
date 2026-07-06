# Manifests

**Document:** 06-manifests.md

---

# Purpose

The Intel GPU Validation Lab communicates through versioned manifests.

Every subsystem communicates using immutable contracts instead of internal APIs.

This separation allows each component to evolve independently.

Two manifest types exist:

- Build Manifest
- Worker Manifest

Each has a single responsibility.

---

# Philosophy

The manifests define the platform API.

They should remain:

- Versioned
- Immutable
- Human-readable
- Machine-readable
- Backwards compatible whenever practical

The manifests are the only shared contract between independent services.

---

# Manifest Lifecycle

```
           Buildbot
               │
               ▼
            Builder
               │
               ▼
        Build Manifest
               │
               ▼
             MinIO
               │
        Scheduler discovers
               │
               ▼
        Worker Manifest
               │
               ▼
             Worker
               │
               ▼
       Artifact Manager
```

Every component communicates through manifests.

---

# Manifest Versioning

Every manifest begins with:

```json
{
    "manifest_version": 1
}
```

Version numbers are monotonically increasing.

Workers should reject unsupported versions.

---

# Build Manifest

## Purpose

The Build Manifest describes an immutable build.

It answers one question:

> "What software was built?"

It does **not** describe:

- workers
- campaigns
- retries
- scheduling

---

## Ownership

Produced by:

Builder

Consumed by:

- Scheduler
- Artifact Manager

Workers never parse artifact metadata directly.

---

## Build Manifest Structure

```
manifest_version

build

artifacts

metadata
```

---

## Build Section

Contains build identity.

Example:

```json
{
    "build": {
        "name": "mesa-main-4f2c9b8d",
        "repository": "mesa",
        "branch": "main",
        "commit": "4f2c9b8d7a13f7e8d1a0b7b2e0d2d4f6c9a1b2c3",
        "created": "2026-07-02T15:32:12Z"
    }
}
```

The build name should be deterministic.

---

## Artifact Section

Each artifact describes:

- component
- object
- compression
- size
- checksum

Example:

```json
{
    "component": "mesa",
    "bucket": "artifacts",
    "object": "mesa/main/mesa-main-4f2c9b8d.tar.zst",
    "compression": "tar.zst",
    "sha256": "...",
    "size": 184732194
}
```

Artifacts are immutable.

---

## Metadata Section

Optional metadata.

Examples:

- architecture
- compiler
- builder version
- operating system
- build type

Metadata exists primarily for debugging and reproducibility.

---

# Worker Manifest

## Purpose

The Worker Manifest describes work.

It answers one question:

> "What should this worker execute?"

It does **not** describe artifacts.

---

## Ownership

Produced by:

Scheduler

Consumed by:

Worker

---

## Worker Manifest Structure

```
manifest_version

build_manifest_uri

shard

environment
```

---

## Build Manifest URI

The Worker Manifest references a Build Manifest.

Example:

```json
{
    "build_manifest_uri":
    "minio://artifacts/mesa/main/mesa-main-4f2c9b8d.json"
}
```

The Worker never receives artifact information directly.

---

## Shard

The scheduler assigns one shard.

Example:

```json
{
    "shard": {
        "suite": "vulkancts",
        "name": "dEQP-VK.pipeline.*"
    }
}
```

Only execution information belongs here.

---

## Environment

Optional execution variables.

Example:

```json
{
    "environment": {
        "MESA_SHADER_CACHE_DISABLE": "1",
        "VK_DRIVER_FILES": "/opt/mesa/icd.json"
    }
}
```

Workers pass these directly into the execution environment.

---

# Why Two Manifests?

Separating build information from execution information provides several benefits.

The Builder owns software.

The Scheduler owns work.

The Worker combines the two.

No duplication exists.

---

# Immutability

Build Manifests never change.

Worker Manifests are immutable after generation.

A retry produces a new Worker Manifest.

---

# Naming

Recommended Build Manifest naming:

```
mesa-main-4f2c9b8d.json
```

Worker Manifests may use UUIDs.

Example:

```
9c42f1c6-fbaf-47b7-bfe2-56d9c1e6e0f7.json
```

---

# Validation

Every manifest must validate against:

```
schemas/

    build-manifest.schema.json

    worker-manifest.schema.json
```

Validation occurs before publication.

Invalid manifests are never uploaded.

---

# Compatibility

Consumers should ignore unknown optional fields.

Required fields must remain stable.

Breaking changes require:

```
manifest_version++

```

---

# Error Handling

Invalid version:

Reject manifest.

Missing required fields:

Reject manifest.

Checksum mismatch:

Reject artifact.

Unknown compression:

Reject artifact.

---

# Design Principles

## Builder owns builds.

## Scheduler owns work.

## Workers execute work.

## Artifact Manager prepares software.

## Manifests remain immutable.

---

# Future Extensions

Possible additions:

- Digital signatures
- SBOM references
- OCI artifact references
- Dependency manifests
- Multi-architecture builds
- Kernel manifests
- Firmware manifests

None should require redesign of existing manifests.

---

# Summary

The manifest system defines the platform API.

Build Manifests describe software.

Worker Manifests describe execution.

Keeping these responsibilities separate minimizes coupling while allowing every subsystem to evolve independently.

---

# Next Document

```
07-scheduler.md
```

This document describes campaign generation, shard scheduling, worker registration, retries, queue management and scheduling algorithms.