# Schemas

## Overview

This directory contains the canonical machine-readable schemas for the Intel GPU Validation Platform.

Schemas are derived from the normative specifications located in `docs/developer/specifications/`.

The specifications remain the authoritative definition of the platform. Schemas provide an implementation-ready representation suitable for validation, code generation, serialization, and interoperability.

---

# Purpose

The schema layer exists to:

* Provide machine-readable contract definitions.
* Validate platform messages.
* Enable automated code generation.
* Support interoperability between implementations.
* Eliminate ambiguity during implementation.

Schemas define structure. They do not replace the architectural intent documented elsewhere.

---

# Relationship to Specifications

Every schema corresponds to exactly one specification.

```text
Specification
        │
        ▼
Schema
        │
        ▼
Generated Code
        │
        ▼
Implementation
```

Specifications define:

* Semantics
* Constraints
* Behavioral requirements

Schemas define:

* Fields
* Types
* Cardinality
* Validation rules
* Serialization structure

Schemas MUST remain consistent with their corresponding specifications.

---

# Design Principles

Schemas SHALL be:

* Generated from normative specifications.
* Language neutral.
* Versioned.
* Backward compatible whenever practical.
* Independent of implementation language.

Schemas MUST NOT introduce behavior that is not defined by the corresponding specification.

---

# Directory Structure

```text
schemas/
│
├── README.md
│
├── build-identity.schema.json
├── artifact-package.schema.json
├── build-manifest.schema.json
├── validation-request.schema.json
├── execution-directory-reference.schema.json
├── worker-manifest.schema.json
└── validation-result.schema.json
```

Additional schema formats MAY be generated in the future without changing the normative specifications.

Examples include:

* Protocol Buffers
* OpenAPI
* XML Schema
* Language-specific object models

---

# Versioning

Every schema SHALL declare:

* Schema version.
* Corresponding specification version.

Schema versions SHALL evolve according to the Compatibility document.

---

# Validation

Schemas SHOULD support automated validation.

Validation SHOULD verify:

* Required fields.
* Field types.
* Structural correctness.
* Cardinality constraints.
* Domain type usage where applicable.

Behavioral rules remain the responsibility of implementations.

---

# Code Generation

Schemas MAY be used to generate:

* C++ classes
* C# models
* Rust types
* Go structs
* Python models
* TypeScript interfaces

Generated code MUST preserve the semantics defined by the corresponding specification.

---

# Serialization

Schemas intentionally do not prescribe transport protocols.

Implementations MAY serialize schema instances using:

* JSON
* YAML
* Protocol Buffers
* Binary encodings

provided the semantics defined by the specifications are preserved.

---

# Related Documents

## Foundation

* Primitive Types
* Domain Types
* Compatibility

## Specifications

* Build Identity
* Artifact Package
* Build Manifest
* Validation Request
* Execution Directory Reference
* Worker Manifest
* Validation Result
