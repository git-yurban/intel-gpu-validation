# Domain Types

## Overview

This document defines the canonical domain types used throughout the Intel GPU Validation Platform.

Domain types extend the Primitive Types document by providing platform-specific semantics.

Every specification SHOULD use Domain Types instead of raw primitive types whenever possible.

---

# Version

Version: **1.0**

Status: **Frozen**

---

# Dependencies

* Primitive Types

---

# Design Principles

Domain types SHALL be:

* Strongly typed.
* Immutable unless explicitly documented otherwise.
* Language neutral.
* Serialization independent.
* Stable across compatible versions.

---

# Identifier Types

## BuildIdentity

Base Type

`Identifier`

Uniquely identifies a published Build.

---

## ValidationRequestId

Base Type

`Identifier`

Uniquely identifies a Validation Request.

---

## WorkerManifestId

Base Type

`Identifier`

Uniquely identifies a Worker Manifest.

---

## ValidationResultId

Base Type

`Identifier`

Uniquely identifies a Validation Result.

---

## ArtifactPackageId

Base Type

`Identifier`

Uniquely identifies an Artifact Package.

---

## ExecutionDirectoryId

Base Type

`Identifier`

Uniquely identifies a prepared Execution Directory.

---

# Enumeration Types

## ValidationStatus

Base Type

`String`

Allowed Values

* Pending
* Scheduled
* Running
* Passed
* Failed
* Aborted
* InfrastructureFailure

---

## ArtifactPackageType

Base Type

`String`

Allowed Values

* Runtime
* DebugSymbols
* TestAssets
* Documentation
* Tools
* Other

---

## CompressionFormat

Base Type

`String`

Allowed Values

* None
* Zstd
* Gzip
* Zip

---

## WorkerState

Base Type

`String`

Allowed Values

* Offline
* Idle
* Preparing
* Executing
* Publishing
* Busy
* Error

---

## ExecutionOutcome

Base Type

`String`

Allowed Values

* Passed
* Failed
* Aborted
* InfrastructureFailure

---

# Collection Types

## Metadata

Base Type

`Map<String,String>`

Optional implementation-defined metadata.

Consumers MUST ignore unknown entries.

---

## ParameterMap

Base Type

`Map<String,String>`

Platform-defined execution parameters.

---

## EnvironmentVariables

Base Type

`Map<String,String>`

Environment variables supplied to a validation process.

---

# Reference Types

## ExecutionDirectoryReference

Base Type

`ExecutionDirectoryId`

Reference to a prepared Execution Directory.

The reference is opaque and does not expose the storage implementation.

---

## ArtifactReference

Base Type

`URI`

Reference to an externally stored artifact such as logs, crash dumps, screenshots, or performance reports.

---

# Value Types

## CreationTimestamp

Base Type

`Timestamp`

Timestamp indicating object creation.

---

## CompletionTimestamp

Base Type

`Timestamp`

Timestamp indicating object completion.

---

## ArtifactDigest

Base Type

`Digest`

Integrity digest for an Artifact Package.

---

# Common Semantics

All Identifier-based domain types SHALL:

* Be immutable.
* Be opaque.
* Never be reused.
* Never encode business meaning.

Consumers MAY compare identifier values for equality but MUST NOT derive semantics from their representation.

---

# Serialization

Domain types intentionally do not define serialization formats.

Serialization is implementation-specific provided the semantics defined by this document are preserved.

---

# Related Documents

* Primitive Types
* Compatibility
* Build Manifest Specification
* Validation Request Specification
* Worker Manifest Specification
* Validation Result Specification
