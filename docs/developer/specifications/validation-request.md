# Validation Request Specification

## Overview

This specification defines the canonical representation of a Validation Request.

A Validation Request describes the validation work to be performed against a published Build. It is the input to the Scheduler and represents the intent to execute validation without prescribing how or where that execution occurs.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

* Build Identity Specification

---

# Canonical Representation

```yaml
validationRequest:
  schemaVersion: string
  requestId: string
  buildIdentity: BuildIdentity
  validationSuite: string
  parameters: object (optional)
  constraints: object (optional)
  requestedAt: timestamp
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

Version of the Validation Request specification.

### Constraints

* MUST be present.
* MUST identify the specification version.

---

## requestId

### Type

`string`

### Required

Yes

### Description

Unique identifier for the Validation Request.

### Constraints

* MUST be unique.
* MUST NOT change after submission.

---

## buildIdentity

### Type

`BuildIdentity`

### Required

Yes

### Description

Identifies the published Build to validate.

### Constraints

* MUST reference one published Build.
* MUST remain unchanged after submission.

---

## validationSuite

### Type

`string`

### Required

Yes

### Description

Identifies the validation workload to execute.

### Constraints

* MUST NOT be empty.

---

## parameters

### Type

`object`

### Required

No

### Description

Optional validation parameters.

Consumers MUST ignore unknown fields.

---

## constraints

### Type

`object`

### Required

No

### Description

Optional execution constraints that influence scheduling.

Examples may include:

* Required capabilities.
* Timeout overrides.
* Scheduling preferences.

The interpretation of constraints is implementation-defined.

---

## requestedAt

### Type

`timestamp`

### Required

Yes

### Description

Timestamp indicating when the Validation Request was created.

### Constraints

* MUST represent UTC.

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

A valid Validation Request MUST satisfy all of the following:

* `schemaVersion` MUST be present.
* `requestId` MUST be present.
* `buildIdentity` MUST be present.
* `validationSuite` MUST be present and non-empty.
* `requestedAt` MUST be present.
* The Validation Request MUST be immutable after submission.

---

# Compatibility Rules

Future versions MAY:

* Add optional fields.
* Extend metadata.
* Introduce additional optional constraints.

Future versions MUST NOT:

* Remove required fields.
* Change the meaning of required fields.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Validation Requests contain no build artifacts.

Consumers SHOULD validate that the referenced Build Identity exists before scheduling.

Authorization policies for submitting Validation Requests are implementation-defined.

---

# Example

```yaml
validationRequest:
  schemaVersion: "1.0"
  requestId: "vr-000001"

  buildIdentity:
    id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"

  validationSuite: "vulkan-conformance"

  constraints:
    requiredCapabilities:
      gpuVendor: Intel
      os: Linux

  requestedAt: "2026-07-03T20:15:00Z"
```

The example values are illustrative only.

---

# Related Contracts

* Validation Request
* Build Identity
* Worker Manifest

---

# Related ADRs

* ADR-0003 — Build and Worker Manifest Model
* ADR-0009 — Scheduler as Control Plane
* ADR-0017 — Worker Capability Model
* ADR-0018 — Capability-Based Scheduling
