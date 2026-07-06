# ADR-0006: Compressed Artifact Format

**Status:** Accepted

**Date:** 2026-07-02

## Context

Published Artifact Packages contain executables, shared libraries, runtime assets, configuration, and validation resources required for validation execution.

Without packaging, published artifacts become more difficult to transport, cache, verify, and reproduce consistently across Validation Workers.

The platform therefore requires a portable artifact distribution format.

---

## Decision

Published artifacts shall be distributed as immutable compressed Artifact Packages.

Each Artifact Package represents a complete, self-contained unit of publication.

Compression format and archive implementation are implementation decisions and are not defined by the platform architecture.

---

## Artifact Package

An Artifact Package:

* Contains all files required for publication.
* Is immutable once published.
* Is referenced by the Build Manifest.
* Is stored by Artifact Storage.
* May be cached by Validation Workers.

Artifact Packages are the unit of publication, storage, transfer, and caching.

---

## Package Lifecycle

```text id="zwbhvq"
Builder
      │
Create Artifact Package
      │
      ▼
Publish Artifact Package
      │
      ▼
Artifact Storage
      │
      ▼
Artifact Access API
      │
      ▼
Artifact Manager
      │
      ▼
Execution Directory
```

Artifact Packages remain immutable throughout their lifecycle.

---

## Design Principles

Artifact Packages should be:

* Immutable
* Portable
* Self-contained
* Efficient to transfer
* Efficient to cache
* Independent of storage implementation

The architecture intentionally does not define the archive format or compression algorithm.

---

## Consequences

### Advantages

* Reduces storage requirements.
* Reduces network transfer time.
* Simplifies artifact transport.
* Supports efficient Worker caching.
* Improves reproducibility.

### Disadvantages

* Requires package creation during publication.
* Requires decompression during execution preparation.
* Introduces packaging overhead.

---

## Alternatives Considered

### Publish uncompressed directories

Rejected.

Directory-based publication complicates transfer, integrity verification, caching, and storage.

### Publish individual files

Rejected.

Managing large collections of individual files increases operational complexity and weakens reproducibility.

### Standardize a specific archive format

Rejected.

Archive format selection is an implementation decision that may evolve independently of the platform architecture.

---

## Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0008 — Worker Artifact Cache
* ADR-0013 — Builder as an Independent Service

## example:
```bash
{
  "artifacts": [
    {
      "name": "mesa",
      "format": "tar.zst",
      "compression": "zstd",
      "checksum": "...",
      "uri": "..."
    }
  ]
}
```

```bash
tar.zst  → ZstdExtractor
tar.gz   → GzipExtractor
tar.xz   → XzExtractor
```
