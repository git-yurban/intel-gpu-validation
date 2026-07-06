# Validation Platform Lifecycle

## Overview

This document describes the end-to-end lifecycle of a validation request within the Intel GPU Validation Platform.

It provides a system-level view of how Builds are published, prepared, scheduled, executed, and reported.

This document is informational and complements the architectural and service documentation.

---

# Goals

The lifecycle is designed to:

* Decouple build publication from validation execution.
* Maximize worker utilization.
* Support reproducible validation.
* Provide immutable execution inputs.
* Preserve complete execution traceability.

---

# Lifecycle Overview

The platform consists of six logical stages:

```text
Build
  │
  ▼
Publication
  │
  ▼
Preparation
  │
  ▼
Scheduling
  │
  ▼
Execution
  │
  ▼
Reporting
```

Each stage produces immutable outputs consumed by the next stage.

---

# Stage 1 — Build

The Builder compiles software and assembles all artifacts required for validation.

Outputs include:

* Build Identity
* Build Manifest
* Artifact Packages

The Builder publishes these artifacts to Artifact Storage.

Once published, a Build is immutable.

**Related Documents**

* Builder Service
* Build Manifest Specification
* Build Identity Specification
* Artifact Package Specification

---

# Stage 2 — Publication

Published Builds become available for validation.

A Validation Request references a published Build Identity and specifies the validation workload to execute.

Validation Requests express *what* should be validated but not *where* or *how* it will execute.

**Related Documents**

* Validation Request Specification
* Scheduler Service

---

# Stage 3 — Preparation

The Artifact Manager prepares an isolated Execution Directory for a specific validation execution.

Preparation may include:

* Retrieving Artifact Packages.
* Verifying package integrity.
* Extracting archives.
* Constructing the execution directory.
* Applying platform-specific preparation.

The prepared Execution Directory is identified by an Execution Directory Reference.

Execution Directories are transient and may be removed after execution.

**Related Documents**

* Artifact Manager Service
* Execution Directory Reference Specification

---

# Stage 4 — Scheduling

The Scheduler continuously evaluates pending Validation Requests.

Scheduling is capability-based.

The Scheduler matches validation requirements with available workers and produces a Worker Manifest.

The Worker Manifest is the immutable execution contract for a single validation workload.

The Scheduler does not execute validation directly.

**Related Documents**

* Scheduler Service
* Worker Manifest Specification
* Worker Capability Model

---

# Stage 5 — Execution

A Validation Worker retrieves its assigned Worker Manifest.

The worker:

1. Resolves the Execution Directory.
2. Validates execution prerequisites.
3. Executes the validation workload.
4. Collects logs and artifacts.
5. Produces a Validation Result.

Workers are intentionally stateless.

Each worker executes one validation workload at a time.

**Related Documents**

* Worker Service
* Validation Result Specification

---

# Stage 6 — Reporting

The Validation Result is published to the Operational Database.

The Validation Result summarizes:

* Execution outcome.
* Timing.
* Aggregate statistics.
* References to execution artifacts.

Detailed logs remain in Artifact Storage.

The Dashboard presents the Operational Database as a read-only view of platform activity.

**Related Documents**

* Dashboard Service
* Operational Database
* Validation Result Specification

---

# Lifecycle Characteristics

The platform is designed around the following principles:

* Immutable published Builds.
* Immutable execution contracts.
* Transient execution environments.
* Capability-based scheduling.
* Stateless workers.
* Read-only operational reporting.

These characteristics support scalability, reproducibility, and operational simplicity.

---

# Failure Handling

Failures may occur during any lifecycle stage.

Examples include:

* Build publication failures.
* Artifact preparation failures.
* Scheduling failures.
* Worker failures.
* Infrastructure failures.
* Validation failures.

Failures are reported through Validation Results and platform telemetry.

Recovery strategies are service-specific.

---

# Traceability

Every validation execution can be traced through the following chain:

```text
Build Identity
        │
        ▼
Validation Request
        │
        ▼
Worker Manifest
        │
        ▼
Execution Directory
        │
        ▼
Validation Result
```

This chain provides complete traceability from build publication to validation outcome.

---

# Related Documents

## Foundation

* Primitive Types
* Domain Types
* Compatibility

## Specifications

* Build Identity
* Build Manifest
* Artifact Package
* Validation Request
* Execution Directory Reference
* Worker Manifest
* Validation Result

## Services

* Builder
* Artifact Manager
* Scheduler
* Worker
* Dashboard

## Architecture

* Architecture
* System Context
* Principles
* Architecture Decision Records (ADRs)
