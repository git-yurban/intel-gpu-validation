# Cache

**Document:** 10-cache.md

---

# Purpose

The Cache provides persistent local storage for build artifacts on Worker systems.

Its purpose is to eliminate redundant downloads, reduce execution latency, and maximize hardware utilization.

The Cache is owned exclusively by the Artifact Manager.

Workers never manipulate cache contents directly.

---

# Responsibilities

The Cache owns:

- Local artifact persistence
- Reference counting
- Cache metadata
- Eviction
- Disk usage accounting
- Integrity tracking

The Cache does **not** own:

- Downloads
- Uploads
- Scheduling
- Test execution
- Result storage

---

# High-Level Architecture

```
              Worker
                 │
                 ▼
         Artifact Manager
                 │
                 ▼
               Cache
         ┌───────┼────────┐
         ▼       ▼        ▼
      Metadata Builds  Downloads
```

The Cache exposes a simple interface to the Artifact Manager.

---

# Cache Layout

Recommended layout:

```
cache/

    builds/

    downloads/

    metadata/

    tmp/
```

---

# builds/

Contains extracted execution environments.

Example:

```
cache/

    builds/

        mesa-main-4f2c9b8d/

            lib/

            bin/

            share/
```

Workers execute directly from this directory.

---

# downloads/

Stores compressed archives.

Example:

```
mesa-main-4f2c9b8d.tar.zst
```

Archives may be retained to avoid repeated downloads.

---

# metadata/

Stores cache metadata.

Each cached build has a metadata file.

Example:

```
mesa-main-4f2c9b8d.json
```

---

# Metadata

Metadata records:

```
Build ID

Reference Count

Created

Last Access

Download Size

Extracted Size

Checksum

State
```

The metadata is authoritative.

---

# Build Identity

Every cache entry is identified by a Build ID.

Recommended format:

```
mesa-main-4f2c9b8d
```

The Build ID originates from the Build Manifest.

Filenames are never used as cache keys.

---

# Cache States

Each entry transitions through:

```
Downloading

↓

Downloaded

↓

Verifying

↓

Extracting

↓

Ready

↓

Deleting
```

Incomplete states survive only until recovery.

---

# Cache Lookup

Artifact preparation begins with:

```
Build ID

↓

Metadata lookup

↓

Ready?

↓

Return cached build
```

Downloads occur only on cache misses.

---

# Reference Counting

Each execution increments the reference count.

```
Worker A

↓

+1

Worker B

↓

+1

Reference Count = 2
```

Reference counts prevent active builds from being removed.

---

# Release

After execution:

```
Release

↓

Reference Count--

↓

Reference Count == 0 ?

↓

Eligible for eviction
```

Releasing a build never deletes it immediately.

---

# Eviction Policy

The Cache uses a reference-aware Least Recently Used policy.

Requirements:

- Reference Count == 0
- Oldest Last Access
- Disk pressure

Only inactive entries are considered.

---

# Disk Limits

Recommended configuration:

```
Maximum Cache Size

Minimum Free Space

Maximum Archive Age

Maximum Build Age
```

Cleanup begins automatically when thresholds are exceeded.

---

# Integrity

Every cache entry includes:

- SHA256 checksum
- Build Manifest checksum
- Extraction status

Corrupted entries are removed automatically.

---

# Recovery

Interrupted download:

```
Delete temporary archive
```

Interrupted extraction:

```
Delete incomplete build
```

Corrupted metadata:

```
Rebuild metadata

or

Delete cache entry
```

The Cache should always recover to a consistent state.

---

# Concurrency

Multiple execution threads may request the same build simultaneously.

The Cache guarantees:

```
One download

One extraction

Many readers
```

Duplicate work must never occur.

---

# Cleanup

Cleanup runs periodically.

Typical sequence:

```
Disk pressure

↓

Select candidates

↓

Reference Count == 0

↓

Oldest access

↓

Delete
```

Cleanup should never interrupt running work.

---

# Metrics

Useful metrics include:

- Cache hits
- Cache misses
- Downloads avoided
- Bytes reused
- Bytes downloaded
- Cache size
- Active references
- Cleanup count
- Eviction count

Metrics should be exported through the Artifact Manager.

---

# Public API

Recommended interface:

```python
lookup(build_id)

reserve(build_id)

release(build_id)

store(build)

remove(build_id)

cleanup()

statistics()
```

The Artifact Manager is the sole consumer of this API.

---

# Design Principles

## Cache by Build ID.

Transport filenames are not identifiers.

---

## Never delete active builds.

Reference counts protect running executions.

---

## Downloads occur once.

Cached builds should be reused aggressively.

---

## Recover automatically.

The Cache should tolerate interrupted operations.

---

## Keep metadata authoritative.

Filesystem contents should never be trusted without metadata.

---

# Future Enhancements

Planned improvements include:

- Shared cache
- Content-addressable storage
- Deduplicated builds
- SSD/HDD cache tiers
- Background prefetching
- Predictive eviction
- Remote cache replication
- Compression-aware caching
- Automatic corruption detection

---

# Summary

The Cache provides reliable local persistence for build artifacts.

It minimizes network traffic, accelerates execution, and protects active workloads through reference counting and intelligent eviction policies.

By separating cache management from artifact preparation, the platform remains modular and easier to evolve.

---

# Next Document

```
11-buildbot.md
```

This document describes the integration between Buildbot, the Builder, artifact publication, and Scheduler discovery.