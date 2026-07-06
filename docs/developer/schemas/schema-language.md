# Schema Language

## Overview

This document defines the canonical schema language used by the Intel GPU Validation Platform.

The schema language is the platform's implementation-independent Interface Definition Language (IDL).

Schemas written in this language are the authoritative machine-readable representation of the platform specifications.

Generators consume schema definitions to produce implementation-specific artifacts including JSON Schema, Protocol Buffers, OpenAPI specifications, language bindings, and validation code.

---

# Version

Version: **1.0**

Status: **Frozen**

---

# Goals

The schema language is designed to be:

* Human readable
* Machine readable
* Language neutral
* Serialization independent
* Stable
* Easy to diff
* Easy to generate code from

The schema language defines structure only.

It does not define implementation behavior.

---

# Relationship to Documentation

The documentation hierarchy is:

```text
Foundation
        │
        ▼
Models
        │
        ▼
Specifications
        │
        ▼
Schemas
        │
        ▼
Generated Artifacts
```

Schemas SHALL remain consistent with their corresponding specifications.

---

# File Naming

Every schema SHALL be stored as:

```text
<name>.schema.yaml
```

Examples:

```text
build-identity.schema.yaml

build-manifest.schema.yaml

validation-request.schema.yaml
```

One schema SHALL be defined per file.

---

# Top-Level Structure

Every schema SHALL contain:

```yaml
schema:

description:

dependencies:

type:

fields:

constraints:

examples:
```

Additional top-level sections SHOULD NOT be introduced without updating this document.

---

# Schema Block

The schema block identifies the schema.

Example:

```yaml
schema:
  name: BuildManifest
  version: "1.0"
```

## Rules

The schema name SHALL be unique.

The version SHALL identify the schema version.

---

# Description

Every schema SHALL include a description.

Descriptions explain semantic intent.

Descriptions MUST NOT redefine behavior already specified elsewhere.

---

# Dependencies

Dependencies identify referenced foundation documents.

Example:

```yaml
dependencies:
  - Primitive Types
  - Domain Types
```

Dependencies document conceptual relationships.

They do not imply implementation dependencies.

---

# Object Type

Current supported object type:

```yaml
type: object
```

Future schema kinds MAY be introduced.

---

# Fields

Fields define the structure of the object.

Example:

```yaml
fields:

  buildIdentity:
    type: BuildIdentity
    required: true

  metadata:
    type: Metadata
    required: false
```

## Rules

Field names SHALL be unique.

Field names SHALL be YAML keys.

Field ordering SHOULD remain stable.

---

# Field Properties

Every field SHALL define:

* type
* required

Fields MAY define:

* description

Future properties MAY include:

* default
* deprecated
* since
* validation hints

---

# Field Types

Field types SHALL be one of:

* Primitive Types
* Domain Types
* Schema Types

Generators SHALL resolve Schema Types recursively.

---

# Collections

Collections use generic notation.

Examples:

```yaml
type: List<ArtifactPackage>

type: Map<String,String>
```

Collection syntax SHALL follow the Primitive Types specification.

---

# Required Fields

Required fields SHALL explicitly declare:

```yaml
required: true
```

Optional fields SHALL explicitly declare:

```yaml
required: false
```

Required field lists are derived by generators.

Schemas SHALL NOT duplicate required field information.

---

# Constraints

Constraints document semantic requirements.

Example:

```yaml
constraints:
  - buildIdentity MUST identify exactly one published Build.
```

Constraints are normative.

Generators MAY expose constraints as validation rules where practical.

---

# Examples

Schemas SHOULD include at least one example.

Examples are informative.

Examples MUST NOT introduce additional semantics.

Examples MAY reference other schema types using placeholder notation.

Example:

```yaml
buildIdentity: <BuildIdentity>

artifactPackages:
  - <ArtifactPackage>
```

---

# Compatibility

All schemas inherit the platform compatibility rules defined in:

```text
docs/developer/foundation/compatibility.md
```

Individual schemas SHOULD NOT redefine compatibility behavior.

---

# Serialization

The schema language intentionally does not define serialization formats.

Generators MAY produce:

* JSON Schema
* Protocol Buffers
* OpenAPI
* C++
* C#
* Rust
* Go
* Python
* TypeScript

Additional generators MAY be introduced without modifying schema definitions.

---

# Generator Requirements

Generators SHALL:

* Preserve field ordering.
* Preserve required fields.
* Preserve type information.
* Preserve descriptions where supported.
* Preserve constraints where supported.

Generators MUST NOT introduce additional semantics.

---

# Design Principles

The schema language SHALL remain:

* Stable
* Minimal
* Deterministic
* Implementation independent

New language features SHOULD be introduced only when required by multiple generators.

---

# Related Documents

* Primitive Types
* Domain Types
* Compatibility
* Models
* Specifications
