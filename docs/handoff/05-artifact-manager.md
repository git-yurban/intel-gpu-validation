# Artifact Manager

**Document:** 05-artifact-manager.md

---

# Purpose

The Artifact Manager is responsible for preparing software for execution on worker systems.

It provides a single interface for:

- Downloading artifacts
- Verifying integrity
- Managing the local cache
- Extracting archives
- Cleaning up unused artifacts

The Worker never interacts directly with object storage.

Instead, the Worker requests a prepared execution environment from the Artifact Manager.

---

# Responsibilities

The Artifact Manager owns:

- Artifact downloads
- Local cache
- Checksum verification
- Archive extraction
- Reference counting
- Cache cleanup
- Cache statistics

It does **not** own:

- Scheduling
- Test execution
- Result collection
- Telemetry
- Build publication

---

# High-Level Architecture

```
                  Worker
                     │
                     ▼
            Artifact Manager
         ┌───────────┼───────────┐
         ▼           ▼           ▼
     Cache      Verification   Storage
         │                       │
         └──────────────┬────────┘
                        ▼
                      MinIO
```

The Worker communicates only with the Artifact Manager.

---

# Artifact Lifecycle

```
Worker requests build

↓

Cache lookup

↓

Artifact present?

 ├── Yes
 │
 │   Increase reference count
 │
 │   Return path
 │
 └── No
     │
     ▼
 Download archive

↓

Verify SHA256

↓

Extract archive

↓

Store in cache

↓

Increase reference count

↓

Return path
```

---

# Local Cache

Each worker maintains its own cache.

Recommended layout:

```
/var/cache/intel-gpu-validation/

    downloads/

    extracted/

    metadata/

    tmp/
```

---

## downloads/

Stores compressed archives.

Example:

```
mesa-main-4f2c9b8d.tar.zst
```

---

## extracted/

Stores extracted artifacts.

Example:

```
mesa-main-4f2c9b8d/

    lib/

    bin/

    share/
```

Workers execute directly from extracted directories.

---

## metadata/

Contains cache metadata.

Example:

```
mesa-main-4f2c9b8d.json
```

Metadata tracks:

- reference count
- last access
- extraction status
- checksum
- size

---

## tmp/

Temporary download location.

Files are removed automatically after successful publication into the cache.

---

# Cache Lookup

Every request begins with a cache lookup.

```
Build Manifest

↓

Build Name

↓

Exists?

↓

Ready?

↓

Return path
```

No download occurs when a valid cached copy exists.

---

# Download Process

Downloads occur only when necessary.

Steps:

```
Create temporary file

↓

Download archive

↓

Verify size

↓

Verify SHA256

↓

Move into downloads/

↓

Extract archive

↓

Move into extracted/

↓

Update metadata
```

Partial downloads are never reused.

---

# Verification

Every download is verified before extraction.

Verification includes:

- SHA256
- File size

Future enhancements:

- Digital signatures
- SBOM verification

Invalid downloads are deleted immediately.

---

# Extraction

Supported format:

```
tar.zst
```

Extraction occurs only once.

Subsequent requests reuse the extracted directory.

---

# Reference Counting

Every prepared artifact receives a reference count.

```
Worker A

↓

+1

Worker B

↓

+1

Worker C

↓

+1

Reference Count = 3
```

Artifacts remain protected while in use.

---

# Release

After execution completes:

```
Worker finished

↓

Release artifact

↓

Reference Count--

↓

Reference Count == 0 ?

↓

Eligible for cleanup
```

Cleanup never removes active artifacts.

---

# Cache Cleanup

Cleanup occurs periodically.

Candidate selection:

```
Reference Count == 0

↓

Oldest Last Access

↓

Disk pressure

↓

Delete
```

This approximates an LRU policy while protecting active artifacts.

---

# Cache Limits

Recommended configuration:

```
Maximum disk usage

Maximum archive age

Maximum extracted age

Minimum free disk space
```

Cleanup begins automatically when limits are exceeded.

---

# Failure Recovery

Interrupted download:

```
Delete temporary file
```

Interrupted extraction:

```
Delete extracted directory
```

Checksum failure:

```
Delete archive

Retry download
```

The cache should never contain partially prepared artifacts.

---

# Thread Safety

Multiple workers may request the same artifact simultaneously.

The Artifact Manager should ensure:

```
One download

Many waiters
```

Only one thread downloads an artifact.

Other requests wait for completion.

---

# Storage Interface

Artifact Manager depends only on the storage abstraction.

Example:

```
Storage

↓

Filesystem

HTTP

MinIO

Mock
```

Storage backends remain interchangeable.

---

# Metrics

Useful metrics include:

```
Cache hits

Cache misses

Download time

Extraction time

Verification failures

Bytes downloaded

Bytes reused

Cache size

Reference count
```

These metrics should eventually feed Prometheus.

---

# Public API

Recommended interface:

```python
prepare(build_manifest) -> Path

release(build_name)

cleanup()

statistics()
```

The Worker should require nothing more.

---

# Design Principles

## Download Once

Each artifact downloads only once.

---

## Extract Once

Extraction occurs only once.

---

## Verify Always

Every download is verified.

---

## Reuse Aggressively

Previously prepared artifacts should always be reused.

---

## Never Trust Local State

Integrity is verified before execution.

---

# Future Enhancements

Planned improvements include:

- Background prefetching
- Parallel downloads
- Delta updates
- Content-addressable storage
- Shared cache
- Compression benchmarking
- Automatic corruption detection
- Remote cache replication

---

# Summary

The Artifact Manager is responsible for the complete lifecycle of artifacts on worker systems.

It hides storage implementation details from the Worker while ensuring every artifact is verified, cached and ready for execution.

By centralizing artifact management, the Worker remains simple and focused exclusively on test execution.

---

# Next Document

Continue with:

```
06-manifests.md
```

This document specifies the Build Manifest and Worker Manifest formats, versioning strategy and compatibility guarantees.