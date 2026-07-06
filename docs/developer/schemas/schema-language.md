# Schema Language

## Overview

This document defines the canonical schema language used by the Intel GPU Validation Platform.

The schema language is the platform's implementation-independent Interface Definition Language (IDL).

Schema definitions are the canonical machine-readable representation of the platform specifications.

Generators consume schema definitions to produce implementation-specific artifacts such as JSON Schema, Protocol Buffers, OpenAPI specifications, SDKs, and validation code.

---

# Version

Version: **1.0**

Status: **Frozen**

---

# Goals

The schema language SHALL be:

* Human readable
* Machine readable
* Language neutral
* Serialization independent
* Stable
* Minimal

The schema language defines structure only.

Behavior is defined by the corresponding specification.

---

# Schema Structure

Every schema SHALL use the following structure:

```yaml
schema:
  name:
  version:

description:

dependencies:

type:

fields:

constraints:

examples:
```

---

# Field Definition

Fields are defined using the field name as the YAML key.

Example:

```yaml
fields:

  buildIdentity:
    type: BuildIdentity
    required: true
    description: Published Build.

  metadata:
    type: Metadata
    required: false
```

---

# Field Types

Field types SHALL be one of:

* Primitive Types
* Domain Types
* Schema Types

Collections SHALL use generic notation.

Examples:

```yaml
type: List<ArtifactPackage>

type: Map<String,String>
```

---

# Required Fields

Every field SHALL explicitly specify:

```yaml
required: true
```

or

```yaml
required: false
```

Generators derive required field lists automatically.

---

# Constraints

Constraints define semantic requirements.

Example:

```yaml
constraints:
  - buildIdentity MUST identify exactly one published Build.
```

---

# Examples

Examples are informative.

Examples MAY reference other schema types.

```yaml
buildIdentity: <BuildIdentity>

artifactPackages:
  - <ArtifactPackage>
```

---

# Compatibility

All schemas inherit the platform compatibility rules defined by:

* Foundation Compatibility

Schemas SHOULD NOT redefine compatibility rules.

---

# Design Principles

Generators SHALL preserve:

* Field names
* Field order
* Types
* Required fields
* Descriptions
* Constraints

Generators MUST NOT introduce additional semantics.

---

# Related Documents

* Primitive Types
* Domain Types
* Compatibility
* Models
* Specifications
