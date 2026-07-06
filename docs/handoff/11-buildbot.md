# Buildbot Integration

**Document:** 11-buildbot.md

---

# Purpose

Buildbot is responsible for compiling software and invoking the Builder to publish immutable artifacts.

It is the only component responsible for producing build outputs.

Once compilation completes successfully, Buildbot transfers control to the Builder.

From that point forward, Buildbot no longer participates in the validation lifecycle.

---

# Responsibilities

Buildbot owns:

- Source checkout
- Dependency preparation
- Compilation
- Unit tests
- Build orchestration
- Invoking the Builder
- Reporting build status

Buildbot does **not** own:

- Artifact storage
- Test scheduling
- Worker management
- Queue management
- Result aggregation

---

# High-Level Architecture

```
Git Repository
       │
       ▼
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
       ▼
   Scheduler
```

Buildbot is responsible only for producing validated build outputs.

---

# Build Pipeline

```
Git Commit

↓

Checkout Source

↓

Install Dependencies

↓

Compile

↓

Run Unit Tests

↓

Invoke Builder

↓

Publish Artifacts

↓

Publish Build Manifest

↓

Build Complete
```

Validation begins only after publication.

---

# Supported Build Types

Typical build configurations include:

- Release
- Debug
- ASan
- UBSan
- TSan
- Nightly
- Merge Request
- Release Candidate

Each build produces an independent Build Manifest.

---

# Builder Invocation

The Builder is executed after a successful build.

Typical inputs:

- Build directory
- Repository name
- Branch
- Full Git SHA
- Build type
- Compiler information

The Builder packages and publishes all required artifacts.

---

# Artifact Publication

The Builder publishes:

- Compressed archives
- Build Manifest

Publication order:

```
Upload archive

↓

Verify upload

↓

Publish Build Manifest
```

The Build Manifest signals that publication is complete.

---

# Build Manifest

Each build generates exactly one Build Manifest.

The manifest contains:

- Build identity
- Artifact list
- Checksums
- Metadata

The Scheduler discovers new builds by reading published Build Manifests.

---

# Scheduler Discovery

The Scheduler periodically scans the artifact repository.

```
MinIO

↓

Build Manifest

↓

Create Scheduler Manifest

↓

Generate Worker Manifests
```

Buildbot never communicates directly with the Scheduler.

---

# Build Identity

Each build receives a deterministic identifier.

Recommended format:

```
mesa-main-4f2c9b8d
```

The identifier is derived from:

- Repository
- Branch
- Git SHA

The full Git SHA remains the authoritative identifier.

---

# Immutable Publication

Published artifacts are immutable.

If a build already exists:

```
Reject publication
```

Artifacts are never overwritten.

---

# Failure Handling

Compilation failure:

```
Stop build
```

Builder failure:

```
Build failed

Artifacts not published
```

Upload failure:

```
Retry publication

No Build Manifest published
```

Workers never observe incomplete publications.

---

# Builder Configuration

Typical configuration includes:

- Artifact storage endpoint
- Compression settings
- Upload concurrency
- Temporary workspace
- Retry limits

Configuration remains independent of Buildbot.

---

# Integration Points

Buildbot communicates only with:

- Source control
- Build environment
- Builder

The Builder communicates with:

- Storage
- Build Manifest generation

The Scheduler discovers published artifacts independently.

---

# Build Metadata

Recommended metadata includes:

- Repository
- Branch
- Full Git SHA
- Build timestamp
- Buildbot build number
- Compiler version
- Operating system
- Architecture
- Build type

This information supports reproducibility and auditing.

---

# Design Principles

## Build once.

Compilation occurs a single time.

---

## Publish once.

Artifacts are immutable.

---

## Discover, don't notify.

The Scheduler discovers new Build Manifests.

No direct integration with Buildbot is required.

---

## Keep CI replaceable.

The platform should not depend on Buildbot-specific APIs.

---

## Builder is independent.

The Builder may be executed from any CI system.

---

# Future Enhancements

Planned improvements include:

- Parallel build publication
- Build signing
- SBOM generation
- Provenance attestation
- OCI image export
- Incremental builds
- Multi-platform builds
- Automatic artifact retention

---

# Summary

Buildbot is responsible for producing validated build outputs and invoking the Builder.

After artifacts are published, Buildbot's responsibility ends.

This loose coupling allows the validation platform to evolve independently of the CI system and makes future migration to alternative build systems straightforward.

---

# Next Document

```
12-database.md
```

This document describes the PostgreSQL schema, persistent metadata, campaign tracking, worker state, and result storage.