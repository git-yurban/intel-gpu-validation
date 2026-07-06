# Builder

**Document:** 04-builder.md

---

# Purpose

The Builder is responsible for converting Buildbot outputs into immutable deployment artifacts.

It serves as the bridge between software compilation and distributed validation.

The Builder never compiles software.

Compilation is performed entirely by Buildbot.

Instead, the Builder:

- Collects build outputs
- Packages artifacts
- Generates manifests
- Calculates checksums
- Publishes artifacts
- Publishes metadata

Once publication completes successfully, the artifacts become immutable.

---

# Responsibilities

The Builder owns:

- Packaging
- Compression
- Checksum generation
- Build Manifest generation
- Uploading artifacts
- Uploading manifests

The Builder does **not** own:

- Scheduling
- Worker assignment
- Test execution
- Result collection
- Cache management

---

# Inputs

The Builder receives completed build outputs from Buildbot.

Typical inputs include:

```
mesa/

vulkancts/

piglit/

igt/

worker/
```

Each component has already been compiled.

The Builder never invokes compilers.

---

# Outputs

For every component, the Builder publishes:

```
Artifact Archive

Build Manifest
```

Example:

```
mesa-main-4f2c9b8d.tar.zst

mesa-main-4f2c9b8d.json
```

These two files represent one immutable build.

---

# Build Pipeline

```
Buildbot

↓

Compiled binaries

↓

Builder

↓

Package

↓

Compress

↓

Calculate SHA256

↓

Generate Manifest

↓

Upload Archive

↓

Upload Manifest

↓

Publish Complete
```

Workers never consume intermediate outputs.

Only fully published artifacts become visible.

---

# Artifact Naming

Artifact names are deterministic.

Recommended format:

```
<component>-<branch>-<git-sha-short>.tar.zst
```

Examples:

```
mesa-main-4f2c9b8d.tar.zst

mesa-feature-raytracing-a71be22f.tar.zst

piglit-main-8c1d94ef.tar.zst
```

Branch names should be sanitized.

Example:

```
feature/vk-sync

↓

feature-vk-sync
```

---

# Manifest Naming

Each artifact archive has a matching Build Manifest.

Example:

```
mesa-main-4f2c9b8d.json
```

The filename identifies the build.

The manifest contains authoritative metadata.

---

# Build Manifest

The Build Manifest describes everything required to consume an artifact.

Typical fields include:

```
manifest_version

build

artifacts

metadata
```

Workers never inspect archive contents.

Workers rely entirely on the Build Manifest.

---

# Compression

Artifacts are packaged using:

```
tar.zst
```

Reasons:

- Fast decompression
- Excellent compression ratio
- Multi-threaded support
- Widely available
- Ideal for repeated downloads

Compression parameters should remain configurable.

---

# Checksum Generation

Every artifact receives a SHA256 checksum.

The checksum is stored inside the Build Manifest.

Workers verify the checksum before extraction.

Corrupted downloads are discarded automatically.

---

# Upload Strategy

Artifacts are uploaded before manifests.

Publication order:

```
Upload archive

↓

Verify upload

↓

Upload manifest

↓

Publication complete
```

Workers never observe partially published builds.

---

# Object Storage Layout

Artifacts are organized by component and branch.

Example:

```
artifacts/

    mesa/

        main/

            mesa-main-4f2c9b8d.tar.zst

            mesa-main-4f2c9b8d.json

        feature-vk-sync/

            mesa-feature-vk-sync-a71be22f.tar.zst

            mesa-feature-vk-sync-a71be22f.json
```

This layout allows easy browsing while remaining deterministic.

---

# Build Metadata

The Build Manifest stores metadata describing the build.

Recommended metadata:

```
Repository

Branch

Full Git SHA

Build timestamp

Builder version

Build type

Architecture

Operating system

Compiler

Compression

Artifact size

SHA256
```

This information enables complete build reproducibility.

---

# Publication Atomicity

Publication must appear atomic.

Workers should never encounter:

- Missing archives
- Missing manifests
- Partial uploads

The Builder should only publish manifests after artifact uploads succeed.

---

# Failure Handling

If any publication step fails:

```
Upload failed

↓

Manifest not published

↓

Build remains invisible

↓

Retry publication
```

The manifest is the publication signal.

---

# Versioning

Every Build Manifest includes:

```
manifest_version
```

Future schema changes should increment the version.

Older workers may reject unsupported versions.

---

# Builder Configuration

Recommended configuration:

```
Artifact bucket

Compression level

Temporary directory

Parallel uploads

Retry count

Upload timeout

Checksum algorithm
```

Configuration should remain independent of Buildbot.

---

# Integration with Buildbot

Buildbot performs compilation.

The Builder performs publication.

Typical workflow:

```
Buildbot Step

↓

Compile Mesa

↓

Compile Vulkan CTS

↓

Compile Piglit

↓

Compile IGT

↓

Invoke Builder

↓

Builder publishes artifacts

↓

Build complete
```

The Builder may be implemented as:

- Python package
- Buildbot step
- Standalone executable
- Docker container

---

# Interaction with Scheduler

The Scheduler discovers newly published Build Manifests.

No direct communication exists.

```
Builder

↓

MinIO

↓

Scheduler discovers manifest

↓

Campaign creation
```

This loose coupling allows both systems to evolve independently.

---

# Design Principles

The Builder follows several principles.

## Build Once

Compilation occurs exactly once.

Artifacts are reused by every worker.

---

## Publish Once

Artifacts are immutable.

Publishing the same build twice should not overwrite existing artifacts.

---

## Fail Safe

Incomplete publications are invisible.

Workers only consume verified artifacts.

---

## Reproducibility

Every published build can be reproduced using:

- Build Manifest
- Git revision
- Build configuration

---

# Future Enhancements

Planned Builder improvements include:

- Delta artifact support
- Artifact signing
- SBOM generation
- OCI image export
- Parallel uploads
- Incremental packaging
- Compression benchmarking
- Automatic artifact retention
- Build provenance
- SLSA compliance

---

# Summary

The Builder transforms compiled software into immutable deployment artifacts.

It is intentionally isolated from scheduling and execution.

Its only responsibility is reliable publication.

This separation enables deterministic builds, efficient distribution and reproducible validation.

---

# Next Document

Continue with:

```
05-artifact-manager.md
```

This document describes artifact downloading, caching, verification, extraction and lifecycle management on worker systems.