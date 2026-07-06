# Primitive Types

## Overview

This document defines the canonical primitive types used throughout the Intel GPU Validation Platform.

Primitive types describe fundamental data semantics independent of any platform-specific concepts.

Platform-specific concepts are defined in the Domain Types document.

---

# Version

Version: **1.0**

Status: **Frozen**

---

# Design Principles

Primitive types SHALL be:

* Language neutral.
* Serialization independent.
* Stable.
* Backward compatible.
* Universally applicable.

Primitive types define semantics rather than implementation.

---

# Primitive Types

## String

Represents textual information.

### Constraints

* UTF-8 encoded.
* May be empty unless otherwise specified.
* Maximum length is implementation-defined.

---

## Boolean

Represents a logical value.

### Allowed Values

* `true`
* `false`

---

## Integer

Represents a signed integer.

The implementation defines the supported range.

---

## UInt32

Represents an unsigned 32-bit integer.

---

## UInt64

Represents an unsigned 64-bit integer.

---

## Timestamp

Represents a single point in time.

### Semantics

* MUST represent UTC.
* MUST be timezone independent.
* MUST be immutable.

---

## Duration

Represents elapsed time.

### Semantics

* MUST be non-negative.
* Independent of wall-clock time.

---

## Identifier

Represents an opaque unique identifier.

### Semantics

* MUST be unique within its namespace.
* MUST be immutable.
* Consumers MUST NOT derive meaning from its representation.

Platform-specific identifier types are defined in the Domain Types document.

---

## Digest

Represents a cryptographic integrity value.

### Semantics

* Algorithm independent.
* Used to verify integrity.

Platform-specific digest types are defined in the Domain Types document.

---

## URI

Represents a resource identifier.

The URI scheme is implementation-defined.

---

## List<T>

Represents an ordered collection.

### Semantics

* Order MUST be preserved.
* All elements MUST have the same type.

---

## Map<K,V>

Represents key/value pairs.

### Semantics

* Keys MUST be unique.
* Keys MUST have the same type.
* Values MUST have the same type.

---

## Object

Represents a structured collection of named fields.

Objects are defined by their containing specifications.

Generic Objects SHOULD be avoided unless extensibility is required.

---

# Nullability

Fields are non-null unless explicitly documented as optional.

Optional fields MAY be omitted.

Consumers MUST distinguish between:

* Missing field
* Present field with a value

---

# Serialization

Primitive types intentionally do not define serialization formats.

Implementations MAY serialize primitive types using JSON, YAML, Protocol Buffers, binary formats, database records, or other representations while preserving the semantics defined by this document.

---

# Related Documents

* Domain Types
* Compatibility
