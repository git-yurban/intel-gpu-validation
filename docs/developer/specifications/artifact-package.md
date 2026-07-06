# Artifact Package Specification

## Overview

This specification defines the canonical representation of an Artifact Package.

An Artifact Package is the immutable unit of publication, storage, and retrieval within the platform.

Artifact Packages are referenced by Build Manifests and retrieved through the Artifact Access API.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

* Build Identity Specification

---

# Canonical Representation

| Field         | Type          | Required |
| ------------- | ------------- | -------- |
| id            | string        | Yes      |
| buildIdentity | BuildIdentity | Yes      |
| type          | string        | Yes      |
| digest        | string        | Yes      |
| size          | uint64        | Yes      |
| compression   | string        | Yes      |
| metadata      | object        | No       |

---

# Field Definitions

## id

**Type**

`string`

**Description**

Unique identifier for the Artifact Package.

---

## buildIdentity

**Type**

`BuildIdentity`

**Description**

Identifies the published Build that owns the Artifact Package.

---

## type

**Type**

`string`

**Description**

Logical package classification.

Examples include:

* binaries
* debug-symbols
* test-assets
* runtime

The set of supported package types is implementation-defined.

---

## digest

**Type**

`string`

**Description**

Integrity digest for the complete Artifact Package.

The digest algorithm is implementation-defined.

---

## size

**Type**

`uint64`

**Description**

Package size in bytes.

---

## compression

**Type**

`string`

**Description**

Compression format used by the package.

The supported compression formats are implementation-defined.

---

## metadata

**Type**

`object`

**Required**

No

**Description**

Optional implementation-specific metadata.

Consumers MUST ignore unknown metadata fields.

---

# Validation Rules

A valid Artifact Package MUST:

* Contain all required fields.
* Reference exactly one Build Identity.
* Have a non-zero size.
* Provide a digest.
* Be immutable after publication.

---

# Compatibility Rules

Future versions MAY add optional fields.

Required fields:

* MUST NOT change meaning.
* MUST NOT be removed.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Artifact Packages SHOULD support integrity verification before use.

Consumers SHOULD verify the published digest before preparing an Execution Directory.

The specification does not mandate a specific digest algorithm.

---

# Example

```yaml
artifactPackage:
  id: "runtime-linux-x64"
  buildIdentity:
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
  type: "runtime"
  digest: "sha256:..."
  size: 48231764
  compression: "zstd"
```

The example values are illustrative only.

---

# Related Contracts

* Build Manifest

---

# Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0005 — Artifact Storage
* ADR-0006 — Compressed Artifact Format
