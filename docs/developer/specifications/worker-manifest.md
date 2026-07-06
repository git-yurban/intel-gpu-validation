# Worker Manifest Specification

## Overview

This specification defines the canonical representation of a Worker Manifest.

A Worker Manifest is the immutable execution contract produced by the Scheduler and consumed by a Validation Worker. It contains all information required to execute a single validation workload.

The Worker Manifest is the only execution contract consumed by the Validation Worker.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

* Build Identity Specification
* Execution Directory Reference Specification
* Validation Request Specification

---

# Canonical Representation

```yaml
workerManifest:
  schemaVersion: string
  workerManifestId: string
  validationRequestId: string
  buildIdentity: BuildIdentity
  executionDirectory: ExecutionDirectoryReference

  workload:
    validationSuite: string
    parameters: map<string,string> (optional)

  execution:
    timeout: duration (optional)
    retryCount: uint32 (optional)

  createdAt: timestamp

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

Version of the Worker Manifest specification.

---

## workerManifestId

### Type

`string`

### Required

Yes

### Description

Unique identifier for this Worker Manifest.

### Constraints

* MUST be unique.
* MUST be immutable.

---

## validationRequestId

### Type

`string`

### Required

Yes

### Description

Identifies the Validation Request that initiated this execution.

---

## buildIdentity

### Type

`BuildIdentity`

### Required

Yes

### Description

Identifies the published Build to execute.

---

## executionDirectory

### Type

`ExecutionDirectoryReference`

### Required

Yes

### Description

Reference to the prepared Execution Directory.

---

## workload

### Type

`object`

### Required

Yes

### Fields

| Field           | Type               | Required |
| --------------- | ------------------ | -------- |
| validationSuite | string             | Yes      |
| parameters      | map<string,string> | No       |

### Description

Defines the validation workload to execute.

---

## execution

### Type

`object`

### Required

No

### Fields

| Field      | Type     | Required |
| ---------- | -------- | -------- |
| timeout    | duration | No       |
| retryCount | uint32   | No       |

### Description

Optional execution policy.

---

## createdAt

### Type

`timestamp`

### Required

Yes

### Description

Timestamp indicating when the Worker Manifest was created.

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

A valid Worker Manifest MUST satisfy all of the following:

* `schemaVersion` MUST be present.
* `workerManifestId` MUST be present.
* `validationRequestId` MUST be present.
* `buildIdentity` MUST be present.
* `executionDirectory` MUST be present.
* `workload.validationSuite` MUST be present.
* `createdAt` MUST be present.
* The Worker Manifest MUST be immutable after publication.

---

# Compatibility Rules

Future versions MAY:

* Add optional fields.
* Extend execution policy.
* Extend metadata.

Future versions MUST NOT:

* Remove required fields.
* Change the semantics of required fields.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Validation Workers SHOULD verify:

* The referenced Execution Directory is accessible.
* The Build Identity matches the prepared execution resources.
* The Worker Manifest integrity before execution.

Authorization and authentication are implementation-defined.

---

# Example

```yaml
workerManifest:
  schemaVersion: "1.0"

  workerManifestId: "wm-000001"

  validationRequestId: "vr-000001"

  buildIdentity:
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

  executionDirectory:
    id: "execdir-8f6d2b41"

  workload:
    validationSuite: "vulkan-conformance"

  execution:
    timeout: "6h"
    retryCount: 0

  createdAt: "2026-07-03T22:00:00Z"
```

The example values are illustrative only.

---

# Related Contracts

* Worker Manifest
* Validation Request
* Execution Directory Reference

---

# Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0004 — Single Self-Contained Worker Manifest
* ADR-0009 — Scheduler as Control Plane
* ADR-0014 — Transient Work Queue
* ADR-0018 — Capability-Based Scheduling
