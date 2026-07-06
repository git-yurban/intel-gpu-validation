# Storage

**Document:** 09-storage.md

---

# Purpose

The Storage subsystem provides a unified interface for storing and retrieving artifacts.

Storage implementations are interchangeable.

Every component interacts with storage through a common interface rather than directly with MinIO, HTTP, or the filesystem.

This abstraction allows the platform to evolve without changing higher-level components.

---

# Responsibilities

The Storage subsystem owns:

- URI resolution
- Artifact downloads
- Artifact uploads
- Object existence checks
- Metadata retrieval
- Streaming large objects

The Storage subsystem does **not** own:

- Caching
- Checksum verification
- Extraction
- Scheduling
- Manifest generation

Those responsibilities belong to the Artifact Manager and Builder.

---

# High-Level Architecture

```
               Builder
                  │
                  ▼
          Storage Interface
                  │
                  ▼
          Storage Resolver
        ┌─────────┼──────────┐
        ▼         ▼          ▼
     MinIO     HTTP      Filesystem
                  │
                  ▼
            Object Storage
```

The Worker interacts with the same interface through the Artifact Manager.

---

# Storage Interface

Every backend implements the same operations.

Recommended interface:

```python
exists(uri)

download(uri, destination)

upload(source, uri)

metadata(uri)

delete(uri)

open(uri)
```

Higher-level components never depend on backend-specific APIs.

---

# URI-Based Access

Artifacts are identified by URIs.

Examples:

```
minio://artifacts/mesa/main/mesa-main-4f2c9b8d.tar.zst

file:///mnt/artifacts/mesa-main-4f2c9b8d.tar.zst

https://artifacts.company.com/mesa-main-4f2c9b8d.tar.zst
```

The URI completely identifies the storage location.

---

# Storage Resolver

The Storage Resolver selects the appropriate backend.

```
URI

↓

Scheme

↓

Backend

↓

Operation
```

Example:

```
minio://...

↓

MinIOStorage
```

---

# Supported Schemes

| Scheme | Backend |
|----------|----------|
| minio:// | MinIOStorage |
| file:// | FilesystemStorage |
| http:// | HTTPStorage |
| https:// | HTTPStorage |
| mock:// | MockStorage |
| s3:// | S3Storage *(future)* |

New backends should require no changes outside the Storage subsystem.

---

# MinIO

MinIO is the primary production backend.

Responsibilities:

- Artifact storage
- Manifest storage
- Immutable objects

Example layout:

```
artifacts/

    mesa/

        main/

            mesa-main-4f2c9b8d.tar.zst

            mesa-main-4f2c9b8d.json
```

Objects are never modified after publication.

---

# Filesystem Storage

Filesystem storage is useful for:

- Local development
- Integration testing
- Offline execution

Example:

```
file:///srv/artifacts/
```

No network connection is required.

---

# HTTP Storage

HTTP storage allows artifacts to be downloaded from standard web servers.

Example:

```
https://artifacts.example.com/
```

This backend is read-only.

Uploads are not supported.

---

# Mock Storage

Mock Storage exists exclusively for testing.

It provides deterministic behavior without external dependencies.

Unit tests should prefer Mock Storage whenever possible.

---

# Streaming

Large artifacts should be streamed.

```
Storage

↓

Chunked transfer

↓

Artifact Manager

↓

Temporary file
```

Streaming minimizes memory usage.

---

# Upload Process

The Builder uploads artifacts.

```
Archive

↓

Temporary object

↓

Verification

↓

Final object
```

Publication becomes visible only after successful upload.

---

# Download Process

The Artifact Manager downloads artifacts.

```
URI

↓

Storage Resolver

↓

Backend

↓

Temporary file

↓

Artifact Manager
```

Downloads always target temporary files.

---

# Metadata

Storage metadata includes:

- Size
- Last modified
- Content type
- ETag (if supported)

Checksums remain part of the Build Manifest rather than storage metadata.

---

# Authentication

Authentication is backend-specific.

Examples:

MinIO

- Access Key
- Secret Key

HTTP

- Bearer Token
- Basic Authentication

Filesystem

- Operating system permissions

The Storage interface hides authentication details.

---

# Configuration

Typical configuration:

```
Default backend

Endpoint

Credentials

Connection timeout

Retry count

Maximum connections
```

Storage configuration remains independent of Worker configuration.

---

# Failure Handling

Recoverable failures:

- Network timeout
- Connection reset
- Temporary server errors

Fatal failures:

- Authentication failure
- Object not found
- Permission denied

The Storage subsystem reports failures but never retries indefinitely.

---

# Performance

The Storage subsystem should support:

- Streaming
- Parallel downloads
- Connection pooling
- HTTP keep-alive
- Multipart uploads

These optimizations remain transparent to higher-level components.

---

# Design Principles

## Storage is interchangeable.

No component depends on MinIO-specific APIs.

---

## URIs are authoritative.

Every artifact is identified by its URI.

---

## Storage is stateless.

No execution state belongs in storage.

---

## Objects are immutable.

Published artifacts are never modified.

---

## Failures are explicit.

Errors are propagated to callers.

---

# Future Enhancements

Planned improvements include:

- Amazon S3
- Azure Blob Storage
- Google Cloud Storage
- OCI Registry support
- Signed URLs
- Content-addressable storage
- Transparent compression
- Artifact replication
- Geo-distributed storage
- Automatic lifecycle management

---

# Summary

The Storage subsystem provides a backend-independent abstraction for artifact storage.

By using URI-based addressing and a common interface, every higher-level component remains independent of the underlying storage technology.

This separation simplifies testing, improves portability, and allows storage implementations to evolve without impacting the rest of the platform.

---

# Next Document

```
10-buildbot.md
```

This document describes Buildbot integration, build pipelines, Builder invocation, artifact publication, and interactions with the Scheduler.