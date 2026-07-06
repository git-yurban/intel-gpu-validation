# Contributing to the Intel GPU Validation Lab

## Purpose

Thank you for contributing to the Intel GPU Validation Lab.

This document describes the development workflow, engineering practices, and documentation requirements used throughout the project.

The project follows an **architecture-first** development approach. Architectural decisions are documented before implementation to maintain a stable and consistent platform design.

---

# Development Principles

All contributions should reinforce the project's architectural principles:

* Single Responsibility
* Explicit Ownership
* Immutable Publication
* Stateless Services
* Capability-Based Scheduling
* Publish, Don't Share
* Configuration Over Customization
* Technology Independence

These principles are documented in `docs/principles.md`.

---

# Before You Start

Before making significant changes, become familiar with the architecture by reading:

1. `docs/system-context.md`
2. `docs/architecture.md`
3. `docs/principles.md`
4. `docs/glossary.md`
5. Relevant Architecture Decision Records (ADRs)

Understanding the architecture is expected before introducing new functionality.

---

# Contribution Workflow

Contributions should follow this sequence:

```text
Understand the Problem
        │
        ▼
Review Existing Documentation
        │
        ▼
Determine if an ADR is Required
        │
        ▼
Implement the Change
        │
        ▼
Add or Update Tests
        │
        ▼
Update Documentation
        │
        ▼
Submit Pull Request
```

Documentation is considered part of every contribution.

---

# Architecture Decision Records

An ADR should be created or updated when a change:

* Introduces a new architectural responsibility
* Changes ownership of an architectural object
* Changes interactions between platform services
* Introduces a new published object
* Alters a core architectural principle

Implementation details do not normally require an ADR.

---

# Pull Requests

Pull requests should be:

* Small
* Focused
* Self-contained
* Well documented

Each pull request should include:

* A clear description of the change
* The motivation for the change
* Documentation updates, when applicable
* Tests appropriate for the change

Architectural changes should reference the relevant ADR.

---

# Testing

Contributions should include testing appropriate to the change.

Examples include:

* Unit tests
* Integration tests
* System tests
* Validation tests

Testing strategy is documented in `docs/testing.md`.

---

# Documentation

Documentation should evolve with the implementation.

Update documentation whenever changes affect:

* Architecture
* APIs
* Configuration
* Deployment
* Operations
* User-visible behavior

Documentation should remain consistent with the Architecture Decision Records.

---

# Domain Terminology

Use the canonical terminology defined in `docs/glossary.md`.

Avoid introducing alternative names for existing architectural concepts.

Examples:

| Preferred            | Avoid      |
| -------------------- | ---------- |
| Build                | Release    |
| Build Manifest       | Descriptor |
| Worker Manifest      | Job        |
| Worker Capability    | Labels     |
| Execution Directory  | Workspace  |
| Validation Execution | Test Run   |

Consistent terminology improves communication and reduces ambiguity.

---

# Configuration

Prefer configuration over customization.

Platform behavior should be configurable whenever practical.

Changes that alter architectural responsibilities should be proposed through an ADR rather than implemented as configuration.

---

# Backward Compatibility

Changes should preserve compatibility whenever practical.

When compatibility cannot be maintained:

* Document the change
* Explain the impact
* Provide a migration strategy

---

# Code Reviews

Reviews should consider:

* Architectural consistency
* Responsibility boundaries
* Ownership
* Simplicity
* Documentation
* Testing
* Maintainability

Implementation quality is important, but architectural consistency takes precedence.

---

# Commit Messages

Commit messages should clearly describe the intent of the change.

Examples:

```text
builder: publish Build Manifest after artifact upload

scheduler: add capability-based Worker selection

worker: prepare Execution Environment before validation

docs: update ADR-0018 scheduling flow
```

---

# Communication

Architectural discussions should reference existing documentation whenever possible.

When introducing a new concept:

* Check whether an existing term already exists.
* Prefer extending the architecture over creating parallel concepts.
* Record significant architectural decisions using an ADR.

---

# Questions

If a proposed change is unclear:

1. Review the relevant ADRs.
2. Review `docs/principles.md`.
3. Review `docs/glossary.md`.
4. Discuss the architectural approach before implementation.

Clarifying architecture early reduces implementation rework.

---

# Summary

The Intel GPU Validation Lab emphasizes:

* Architecture before implementation
* Clear ownership
* Small, focused changes
* Comprehensive documentation
* Consistent terminology
* Long-term maintainability

Every contribution should strengthen the architecture while keeping the platform simple, consistent, and easy to evolve.

---

# Definition of Done

A contribution is considered complete when:

- The implementation satisfies the intended behavior.
- Appropriate tests have been added or updated.
- Documentation has been updated as needed.
- Architectural changes are reflected in the relevant ADRs.
- New terminology has been added to the glossary, if applicable.
- Configuration and operational impacts have been documented.