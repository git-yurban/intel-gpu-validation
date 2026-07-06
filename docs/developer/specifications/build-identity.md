# Build Identity Specification

## Overview

This specification defines the canonical representation of a Build Identity.

A Build Identity uniquely identifies a published Build throughout the platform.

The representation of a Build Identity is opaque to platform consumers.

---

# Version

Specification Version: **1.0**

Status: **Frozen**

---

# Dependencies

None.

Build Identity is the foundational model referenced by other specifications.

---

# Canonical Representation

| Field | Type   | Required |
| ----- | ------ | -------- |
| id    | string | Yes      |

The internal format of the identifier is implementation-defined.

Consumers MUST treat the identifier as an opaque value.

---

# Field Definitions

## id

**Type**

```text
string
```

**Required**

Yes

**Description**

Uniquely identifies a published Build.

**Constraints**

* MUST be unique within the platform.
* MUST be immutable.
* MUST NOT be empty.
* MUST remain stable for the lifetime of the Build.

Consumers MUST NOT derive meaning from the identifier.

---

# Validation Rules

A valid Build Identity MUST satisfy all of the following:

* The identifier MUST be present.
* The identifier MUST NOT be empty.
* The identifier MUST uniquely identify one published Build.
* The identifier MUST never be reused for another Build.

---

# Compatibility Rules

Future versions MAY introduce additional optional fields.

The `id` field:

* MUST remain required.
* MUST NOT change semantics.
* MUST NOT be removed.

Consumers MUST ignore unknown fields.

---

# Security Considerations

Build Identities contain no sensitive information.

Consumers SHOULD treat Build Identities as opaque identifiers.

Build Identities MUST NOT encode implementation-specific information that consumers are expected to interpret.

---

# Example

```yaml
buildIdentity:
  id: "f47ac10b-58cc-4372-a567-0e02b2c3d479"
```

The example identifier is illustrative only.

---

# Related Contracts

* Build Manifest
* Validation Request
* Worker Manifest
* Validation Result

---

# Related ADRs

* ADR-0007 — Build Identity
* ADR-0020 — Data Classification
