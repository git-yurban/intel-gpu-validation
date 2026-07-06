# Build Manifest Specification

## Overview

This specification defines the canonical representation of a Build Manifest.

A Build Manifest is the immutable description of a published Build. It identifies the Build, describes the published Artifact Packages that comprise it, and provides the information required by the platform to prepare an Execution Directory.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

* Build Identity Specification
* Artifact Package Specification

---

# Canonical Representation

```yaml
buildManifest:
  schemaVersion: string
  buildIdentity: BuildIdentity
  builder:
    name: string
    version: string
  createdAt: timestamp
  artifactPackages:
    - ArtifactPackage
  metadata: object (optional)
```

---

# Field Definitions

## schemaVersion

### Type

`string`

### Required

Yes

### Description

Version of the Build Manifest specification.

### Constraints

* MUST be present.
* MUST identify the specification version used to produce the manifest.

---

## buildIdentity

### Type

`BuildIdentity`

### Required

Yes

### Description

Unique identifier of the published Build.

### Constraints

* MUST reference exactly one Build.
* MUST NOT change after publication.

---

## builder

### Type

`object`

### Required

Yes

### Description

Identifies the Builder that created the Build Manifest.

### Fields

| Field   | Type   | Required |
| ------- | ------ | -------- |
| name    | string | Yes      |
| version | string | Yes      |

---

## createdAt

### Type

`timestamp`

### Required

Yes

### Description

Publication timestamp of the Build Manifest.

### Constraints

* MUST represent UTC.
* MUST NOT change after publication.

---

## artifactPackages

### Type

`array<ArtifactPackage>`

### Required

Yes

### Description

Collection of published Artifact Packages belonging to the Build.

### Constraints

* MUST contain at least one Artifact Package.
* Every Artifact Package MUST reference the same Build Identity.

---

## metadata

### Type

`object`

### Required

No

### Description

Optional implementation-specific metadata.

Consumers MUST ignore unknown fields.

---

# Validation Rules

A valid Build Manifest MUST satisfy all of the following:

* `schemaVersion` MUST be present.
* `buildIdentity` MUST be present.
* `builder` MUST be present.
* `createdAt` MUST be present.
* `artifactPackages` MUST contain one or more Artifact Packages.
* Every Artifact Package MUST reference the same Build Identity.
* The Build Manifest MUST be immutable after publication.

---

# Compatibility Rules

Future versions MAY:

* Add optional fields.
* Add optional metadata.
* Extend Builder information.

Future versions MUST NOT:

* Remove required fields.
* Change the semantics of required fields.
* Change the meaning of Build Identity.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Consumers SHOULD verify:

* Build Manifest integrity.
* Artifact Package integrity.
* Build Identity consistency.

Integrity verification SHOULD occur before preparing an Execution Directory.

---

# Example

```yaml
buildManifest:
  schemaVersion: "1.0"
  buildIdentity:
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

  builder:
    name: "Intel GPU Builder"
    version: "2.4.1"

  createdAt: "2026-07-03T18:42:17Z"

  artifactPackages:
    - id: runtime-linux
      buildIdentity:
        id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
      type: runtime
      digest: sha256:...
      size: 48231764
      compression: zstd
```

The example values are illustrative only.

---

# Related Contracts

* Build Manifest
* Artifact Package
* Build Identity

---

# Related ADRs

* ADR-0002 — Immutable Build Artifacts
* ADR-0003 — Build and Worker Manifest Model
* ADR-0005 — Artifact Storage
* ADR-0007 — Build Identity
