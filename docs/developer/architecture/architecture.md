# Architecture

## Overview

The Intel GPU Validation Lab is composed of independent platform services that collaborate to build, distribute, schedule, execute, and observe GPU validation workloads.

Each service has a single architectural responsibility and communicates through immutable Architectural Contracts.

This separation enables independent development, deployment, scaling, and long-term evolution.

---

# Architectural View

```text
                 Source Code
                      │
                      ▼
                  Builder
                      │
          Publish Build Manifest
          Publish Artifact Packages
                      │
                      ▼
              Artifact Storage
                      │
                      ▼
             Artifact Manager
                      │
Prepare Execution Directory
                      │
                      ▼
                 Scheduler
                      │
      Publish Worker Manifest
                      │
                      ▼
          Transient Work Queue
                      │
                      ▼
             Validation Worker
                      │
      Execute Validation Workload
                      │
                      ▼
         Operational Database
            │             │
            ▼             ▼
Telemetry & Observability Dashboard
```

---

# Platform Services

## Builder

Produces immutable Builds, Build Manifests, and Artifact Packages.

The Builder's architectural responsibility ends after successful publication of the Build Manifest and Artifact Packages.

---

## Artifact Storage

Stores immutable published Artifact Packages and provides access through the Artifact Access API.

Artifact Storage is the authoritative owner of published Artifact Packages.

---

## Artifact Manager

Retrieves published Artifact Packages and prepares Execution Directories for validation.

The Artifact Manager does not execute validation workloads.

---

## Scheduler

Acts as the platform control plane.

The Scheduler assigns validation workloads to Worker Hosts by producing immutable Worker Manifests.

---

## Validation Worker

Executes validation workloads.

Validation Workers prepare Execution Environments, execute assigned workloads, publish validation results, and own transient execution resources.

Validation Workers are stateless platform services.

---

## Operational Database

Stores mutable Operational State describing the current and historical operation of the platform.

It does not own immutable Architectural Contracts.

---

## Dashboard

Provides a unified read-only operational view of the platform.

The Dashboard consumes authoritative information without owning it.

---

# Cross-Cutting Capabilities

The platform provides several capabilities that span multiple services:

* Service Discovery and Addressing
* Telemetry and Observability
* Capability-Based Scheduling
* Configuration Management

These capabilities support platform operation without changing service ownership.

---

# Architectural Principles

The platform architecture is built around the following principles:

* Single responsibility
* Explicit ownership
* Immutable Architectural Contracts
* Mutable Operational State
* Transient Execution Resources
* Deterministic execution
* Independent services
* Configuration over customization

These principles guide architectural evolution and are described in `docs/principles.md`.

---

# Relationship to the ADRs

This document describes the architecture at a system level.

The Architecture Decision Records document the individual architectural decisions that define the platform.

Together, these documents provide the authoritative description of the Intel GPU Validation Lab architecture.
