# Shared Implementation Guidelines

## Purpose

This document defines the implementation conventions shared by all platform services.

The goal is to promote consistency across the codebase while allowing individual services to evolve independently.

These guidelines complement the architectural principles documented elsewhere in the project and apply to every platform service unless explicitly documented otherwise.

---

# Scope

This document applies to:

* Builder
* Artifact Storage
* Artifact Manager
* Scheduler
* Workers
* Operational Database
* Telemetry
* Dashboard

Component-specific behavior is documented in the corresponding developer guide.

---

# Design Philosophy

Shared implementation should:

* Reduce duplication
* Promote consistency
* Simplify maintenance
* Encourage reuse
* Preserve service independence

Shared components should support platform services rather than become a dependency that owns business logic.

---

# Shared Libraries

Common functionality belongs in the `shared/` directory.

Examples include:

* Configuration
* Logging
* Error handling
* Serialization
* Common data models
* Utility functions
* Metrics
* Testing utilities

Business logic should remain within the owning service.

---

# Configuration

Configuration should be:

* Explicit
* Version controlled
* Environment specific
* Human readable
* Fully documented

Configuration should describe behavior rather than architecture.

Configuration must never redefine:

* Service responsibilities
* Ownership
* Published objects
* Architectural boundaries

---

# Logging

Every platform service should produce structured logs.

Logs should include:

* Timestamp
* Service name
* Severity
* Context
* Message

Logging should:

* Support troubleshooting
* Avoid duplication
* Avoid sensitive information
* Remain human readable

Logs should describe what happened, not explain why the architecture exists.

---

# Error Handling

Errors should be:

* Explicit
* Actionable
* Recoverable where practical
* Logged with sufficient context

Avoid:

* Silent failures
* Generic error messages
* Hidden exceptions

Error handling should preserve predictable platform behavior.

---

# Telemetry

Every platform service should publish telemetry.

Telemetry should describe:

* Health
* Activity
* Performance
* Resource utilization
* Failures

Telemetry should be suitable for both operational monitoring and historical analysis.

Telemetry must never become a runtime dependency for core platform functionality.

---

# Metrics

Metrics should be:

* Stable
* Meaningful
* Low cardinality
* Consistently named

Prefer measurements that describe service behavior rather than implementation details.

Examples include:

* Requests processed
* Validation executions
* Queue depth
* Build publication duration
* Artifact preparation duration

---

# Serialization

Published architectural objects should use stable, versioned serialization formats.

Serialization should:

* Be deterministic
* Preserve compatibility
* Support version evolution
* Be independent of implementation language where practical

Serialization formats are implementation decisions.

---

# Versioning

Public interfaces should evolve compatibly whenever practical.

Changes should:

* Preserve compatibility
* Be documented
* Include migration guidance when required

Breaking changes should be deliberate and well documented.

---

# Time

Services should use a consistent representation for:

* Time
* Duration
* Time zones

Timestamps should be unambiguous and suitable for distributed systems.

---

# Identifiers

Identifiers should be:

* Stable
* Globally unique where required
* Immutable
* Opaque to consumers

Consumers should never derive meaning from identifier formats.

---

# Concurrency

Concurrency is an implementation detail.

Shared libraries should:

* Avoid unnecessary synchronization
* Minimize shared mutable state
* Favor immutable data where practical

Concurrency mechanisms should not leak into architectural contracts.

---

# Testing

Shared code should include:

* Unit tests
* Integration tests where appropriate

Testing utilities should simplify component testing without introducing unnecessary dependencies.

---

# Documentation

Shared libraries should be documented.

Documentation should describe:

* Purpose
* Responsibilities
* Public interfaces
* Usage guidance

Implementation details should remain within the source code.

---

# Dependency Management

Shared components should have minimal dependencies.

Before introducing a new dependency, consider:

* Is it necessary?
* Is it actively maintained?
* Does it increase operational complexity?
* Can existing functionality satisfy the requirement?

Dependencies should simplify development rather than complicate deployment.

---

# Backward Compatibility

Changes to shared components should minimize impact on platform services.

Whenever practical:

* Preserve existing interfaces
* Deprecate before removal
* Document incompatible changes

Shared components should evolve conservatively.

---

# Summary

The `shared/` directory exists to provide common implementation capabilities while preserving the independence of individual platform services.

Shared components should reduce duplication, encourage consistency, and simplify development without owning business logic or redefining the platform architecture.
