# Execution Directory Reference Specification

## Overview

This specification defines the canonical representation of an Execution Directory Reference.

An Execution Directory Reference identifies a prepared Execution Directory created by the Artifact Manager. It is embedded in a Worker Manifest and consumed by a Validation Worker to locate the execution resources required for a validation workload.

The Execution Directory itself is a transient execution resource and is not part of this specification.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

None.

The Execution Directory Reference is an independent value object referenced by the Worker Manifest.

---

# Canonical Representation

```yaml
executionDirectoryReference:
  schemaVersion: string
  id: string
  createdAt: timestamp
  expiresAt: timestamp (optional)
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

Version of the Execution Directory Reference specification.

### Constraints

* MUST be present.
* MUST identify the specification version.

---

## id

### Type

`string`

### Required

Yes

### Description

Unique identifier for the prepared Execution Directory.

### Constraints

* MUST uniquely identify one prepared Execution Directory.
* MUST remain unchanged after creation.
* MUST be treated as an opaque value by consumers.

---

## createdAt

### Type

`timestamp`

### Required

Yes

### Description

Timestamp indicating when the Execution Directory Reference was created.

### Constraints

* MUST represent UTC.

---

## expiresAt

### Type

`timestamp`

### Required

No

### Description

Optional expiration timestamp for the referenced Execution Directory.

### Constraints

* If present, MUST represent UTC.
* MUST be later than `createdAt`.

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

A valid Execution Directory Reference MUST satisfy all of the following:

* `schemaVersion` MUST be present.
* `id` MUST be present.
* `createdAt` MUST be present.
* If `expiresAt` is present, it MUST be later than `createdAt`.
* The reference MUST be immutable after creation.

---

# Compatibility Rules

Future versions MAY:

* Add optional fields.
* Extend metadata.

Future versions MUST NOT:

* Remove required fields.
* Change the meaning of required fields.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Execution Directory References identify transient execution resources.

Consumers SHOULD validate that the referenced Execution Directory is available before execution.

The specification does not define authorization or access-control mechanisms.

---

# Example

```yaml
executionDirectoryReference:
  schemaVersion: "1.0"
  id: "execdir-8f6d2b41"
  createdAt: "2026-07-03T21:30:00Z"
  expiresAt: "2026-07-03T23:30:00Z"
```

The example values are illustrative only.

---

# Related Contracts

* Execution Directory Reference
* Worker Manifest

---

# Related ADRs

* ADR-0011 — Execution Environment Isolation
* ADR-0020 — Data Classification
