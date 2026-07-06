# Engineering Guidelines

**Document:** 19-engineering-guidelines.md

---

# Purpose

This document defines the engineering standards and development practices for the Intel GPU Validation Lab.

Its purpose is to ensure that every component of the platform is implemented consistently, remains maintainable, and evolves without introducing unnecessary complexity.

These guidelines apply to every repository, service, library, and tool within the project.

---

# Engineering Principles

The project follows several core principles.

## Keep it simple.

Choose the simplest solution that satisfies the requirements.

Avoid adding abstractions before they are needed.

---

## Build reusable components.

Components should solve one problem well.

Avoid coupling unrelated functionality.

---

## Prefer composition over inheritance.

Small composable classes and functions are preferred over deep inheritance hierarchies.

---

## Immutable by default.

Published data should never change.

Examples:

- Build Manifests
- Worker Manifests
- Published artifacts

If data must change, create a new version.

---

## Explicit is better than implicit.

Configuration should be obvious.

Interfaces should be predictable.

Behavior should never depend on hidden side effects.

---

# Python Version

Minimum supported version:

```
Python 3.12
```

All new features should target the current supported version.

---

# Type Hints

Type annotations are required.

Example:

```python
def publish(manifest: BuildManifest) -> None:
    ...
```

Avoid untyped public interfaces.

---

# Dataclasses

Prefer dataclasses for immutable models.

Example:

```python
@dataclass(frozen=True)
class BuildManifest:
    ...
```

Mutable state should be minimized.

---

# Dependency Management

Dependencies should remain minimal.

Before introducing a dependency ask:

- Can the standard library solve this?
- Is the dependency actively maintained?
- Does it reduce complexity?
- Is it widely adopted?

Avoid unnecessary frameworks.

---

# Project Structure

Projects should follow a consistent layout.

```
project/

src/

tests/

docs/

schemas/

pyproject.toml
```

Documentation belongs with the code.

---

# Package Design

Packages should have a single responsibility.

Example:

```
artifact_manager/

worker/

scheduler/

builder/
```

Avoid large utility packages.

---

# Configuration

Configuration belongs outside the code.

Preferred order:

1. Environment variables
2. Configuration files
3. Command-line options

Avoid hard-coded paths.

---

# Logging

Use structured logging.

Every log entry should include:

- Timestamp
- Component
- Worker ID (if applicable)
- Campaign ID (if applicable)
- Log level

Logs should be actionable.

---

# Exceptions

Raise specific exceptions.

Avoid:

```python
except Exception:
```

unless re-raising or logging.

Define project-specific exception types where appropriate.

---

# Error Messages

Errors should describe:

- What failed
- Why it failed
- What was expected

Avoid vague messages.

Example:

```
Unsupported manifest version: expected 1, received 2.
```

---

# Testing

Every new feature requires tests.

Preferred test pyramid:

- Unit tests
- Integration tests
- End-to-end tests

Unit tests should dominate.

---

# Test Data

Avoid static test fixtures when practical.

Generate data programmatically.

Exceptions:

- JSON schema validation
- Golden manifest examples
- Compatibility tests

---

# Code Style

Use:

- Black
- Ruff
- Pylint

Formatting should be automated.

---

# Documentation

Every public package should include:

- README
- API documentation
- Examples

Complex algorithms should include implementation notes.

---

# APIs

REST APIs should be versioned.

Example:

```
/api/v1/
```

Breaking changes require a new API version.

---

# Manifest Evolution

Manifest versions are immutable.

Backward compatibility should be maintained whenever possible.

Breaking schema changes require a new manifest version.

---

# Storage

Artifacts are immutable.

Never modify published objects.

Corrections require publishing a new artifact.

---

# Database

The database stores operational state only.

Never duplicate immutable manifest data.

References are preferred over copies.

---

# Docker Images

Images should be:

- Small
- Reproducible
- Versioned
- Immutable

Avoid runtime package installation.

---

# Security

Never commit:

- Passwords
- Tokens
- Certificates
- Secrets

Use runtime configuration.

---

# Performance

Measure before optimizing.

Avoid speculative optimization.

Optimize based on profiling and production metrics.

---

# Code Reviews

Every review should verify:

- Correctness
- Readability
- Tests
- Documentation
- Backward compatibility
- Simplicity

---

# Commit Messages

Follow a consistent format.

Examples:

```
artifact-manager: implement local cache

worker: add manifest validation

scheduler: implement campaign creation
```

Commits should remain focused.

---

# Release Versioning

Use Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Development builds may include Git SHAs.

---

# Backward Compatibility

Public interfaces should remain stable.

Breaking changes require:

- Documentation
- Version increment
- Migration plan

---

# Design Philosophy

The platform should remain:

- Modular
- Observable
- Testable
- Deterministic
- Recoverable

Operational simplicity is preferred over architectural novelty.

---

# Continuous Improvement

This document is a living standard.

Guidelines should evolve as experience is gained, but changes should be deliberate and documented.

---

# Summary

These engineering guidelines define the standards for building and maintaining the Intel GPU Validation Lab.

By following consistent practices for design, implementation, testing, and documentation, the project can scale in both size and contributors while remaining maintainable and predictable.