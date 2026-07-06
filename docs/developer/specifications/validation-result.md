# Validation Result Specification

## Overview

This specification defines the canonical representation of a Validation Result.

A Validation Result records the outcome of a completed validation execution. It is created by a Validation Worker and published to the Operational Database as part of the platform's Operational State.

The Validation Result is the authoritative summary of a validation execution.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

* Build Identity Specification
* Validation Request Specification
* Worker Manifest Specification

---

# Canonical Representation

```yaml
validationResult:
  schemaVersion: string
  resultId: string
  workerManifestId: string
  validationRequestId: string
  buildIdentity: BuildIdentity

  outcome:
    status: string
    startedAt: timestamp
    completedAt: timestamp
    duration: duration

  summary:
    executed: uint32
    passed: uint32
    failed: uint32
    skipped: uint32

  artifacts:
    - name: string
      reference: string

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

Version of the Validation Result specification.

---

## resultId

### Type

`string`

### Required

Yes

### Description

Unique identifier for the Validation Result.

### Constraints

* MUST be unique.
* MUST be immutable.

---

## workerManifestId

### Type

`string`

### Required

Yes

### Description

Identifies the Worker Manifest that produced this result.

---

## validationRequestId

### Type

`string`

### Required

Yes

### Description

Identifies the originating Validation Request.

---

## buildIdentity

### Type

`BuildIdentity`

### Required

Yes

### Description

Identifies the Build that was validated.

---

## outcome

### Type

`object`

### Required

Yes

### Fields

| Field       | Type      | Required |
| ----------- | --------- | -------- |
| status      | string    | Yes      |
| startedAt   | timestamp | Yes      |
| completedAt | timestamp | Yes      |
| duration    | duration  | Yes      |

### Description

Summarizes the execution outcome.

---

## summary

### Type

`object`

### Required

Yes

### Fields

| Field    | Type   | Required |
| -------- | ------ | -------- |
| executed | uint32 | Yes      |
| passed   | uint32 | Yes      |
| failed   | uint32 | Yes      |
| skipped  | uint32 | Yes      |

### Description

Aggregate execution statistics.

---

## artifacts

### Type

`array`

### Required

No

### Description

References to externally stored execution artifacts.

Artifacts may include:

* Logs
* Crash dumps
* Screenshots
* Performance reports

Artifact storage and retrieval are implementation-defined.

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

A valid Validation Result MUST satisfy all of the following:

* `schemaVersion` MUST be present.
* `resultId` MUST be present.
* `workerManifestId` MUST be present.
* `validationRequestId` MUST be present.
* `buildIdentity` MUST be present.
* `outcome` MUST be present.
* `summary` MUST be present.
* `completedAt` MUST be later than or equal to `startedAt`.
* `duration` MUST be consistent with the execution timestamps.

---

# Compatibility Rules

Future versions MAY:

* Add optional fields.
* Extend summary statistics.
* Add additional artifact reference types.

Future versions MUST NOT:

* Remove required fields.
* Change the semantics of required fields.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Validation Results SHOULD contain references to execution artifacts rather than embedding them.

Sensitive execution artifacts SHOULD be protected by the underlying artifact storage implementation.

The specification does not define authentication or authorization mechanisms.

---

# Example

```yaml
validationResult:
  schemaVersion: "1.0"

  resultId: "vr-000001-result"

  workerManifestId: "wm-000001"

  validationRequestId: "vr-000001"

  buildIdentity:
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

  outcome:
    status: "Passed"
    startedAt: "2026-07-03T22:00:00Z"
    completedAt: "2026-07-03T23:42:11Z"
    duration: "1h42m11s"

  summary:
    executed: 42871
    passed: 42860
    failed: 11
    skipped: 0

  artifacts:
    - name: "validation-log"
      reference: "artifact://results/log-12345"
```

The example values are illustrative only.

---

# Related Contracts

* Validation Result
* Worker Manifest
* Validation Request

---

# Related ADRs

* ADR-0009 — Scheduler as Control Plane
* ADR-0010 — Operational Database
* ADR-0020 — Data Classification
* ADR-0022 — Dashboard as a Read-Only Platform Service
