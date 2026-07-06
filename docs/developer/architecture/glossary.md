# Glossary

This glossary defines the architectural terminology used throughout the Intel GPU Validation Lab documentation.

---

## Artifact Access API

The platform interface used to retrieve published Artifact Packages from Artifact Storage.

The API provides access to immutable published artifacts and abstracts the underlying storage implementation.

---

## Artifact Manager

The platform service responsible for preparing Execution Directories from published Artifact Packages.

The Artifact Manager does not execute validation workloads or own artifact storage.

---

## Artifact Package

The immutable, self-contained unit of publication produced by the Builder.

Artifact Packages are stored by Artifact Storage and referenced by Build Manifests.

---

## Artifact Storage

The platform service responsible for storing and providing access to immutable published Artifact Packages.

Artifact Storage is the authoritative owner of published Artifact Packages after publication.

---

## Architectural Contract

An immutable contract exchanged between platform services.

Examples include:

* Build Identity
* Build Manifest
* Worker Manifest
* Artifact Package

Architectural Contracts define published platform behavior and service interactions.

---

## Build

A published software build produced by the Builder.

A Build is uniquely identified by a Build Identity and consists of one or more Artifact Packages described by a Build Manifest.

---

## Build Identity

The globally unique, immutable identifier assigned to a published Build.

A Build Identity never changes throughout the lifetime of the Build.

---

## Build Manifest

The immutable Architectural Contract describing a published Build and its Artifact Packages.

---

## Builder

The platform service responsible for producing Builds, Build Manifests, and Artifact Packages.

The Builder's architectural responsibility ends after successful publication of the Build Manifest and Artifact Packages.

---

## Dashboard

The read-only presentation service that provides a unified operational view of the platform.

The Dashboard consumes authoritative information but never owns it.

---

## Execution Directory

The prepared runtime directory created from published Artifact Packages before validation execution.

Execution Directories are transient resources owned by the Validation Worker.

---

## Execution Environment

The isolated runtime in which a validation workload executes.

An Execution Environment includes the Execution Directory together with the runtime context required for execution.

Execution Environments are transient and are created for a single validation workload.

---

## Immutable Architectural Contract

An Architectural Contract that never changes after publication.

Examples include Build Manifests, Worker Manifests, Build Identities, and Artifact Packages.

---

## Operational Database

The platform service responsible for the authoritative storage of mutable Operational State.

---

## Operational State

Mutable information describing the current or historical operation of the platform.

Examples include Worker Capability, Worker Host status, validation execution status, validation results, and platform metrics.

---

## Platform Service

An independently deployable service with a single well-defined architectural responsibility.

Examples include:

* Builder
* Artifact Storage
* Artifact Manager
* Scheduler
* Validation Worker
* Operational Database
* Dashboard

---

## Scheduler

The platform control plane responsible for assigning validation workloads by producing Worker Manifests.

The Scheduler coordinates work but never executes validation workloads.

---

## Telemetry

Operational information published by platform services describing platform behavior.

Telemetry supports observability but is not authoritative Operational State.

---

## Validation Worker

The stateless platform service responsible for preparing Execution Environments, executing validation workloads, and publishing validation results.

Validation Workers own transient execution resources but do not own persistent platform state.

---

## Worker Artifact Cache

The transient local cache maintained by a Validation Worker containing previously retrieved immutable Artifact Packages.

The cache is an execution optimization and never becomes the authoritative source of published artifacts.

---

## Worker Capability

The declarative description of the execution capabilities of a Worker Host.

Capabilities describe what a Worker Host can execute and are consumed by the Scheduler during capability-based scheduling.

---

## Worker Host

The compute resource that hosts a single Validation Worker.

A Worker Host has a globally unique Worker Host Identity and publishes its Worker Capability to the platform.

---

## Worker Host Identity

The globally unique, immutable identifier assigned to a Worker Host.

The Worker Host Identity uniquely identifies the execution resource throughout its operational lifetime.

---

## Worker Manifest

The immutable Architectural Contract produced by the Scheduler describing a validation workload assigned to a Validation Worker.

A Worker Manifest is the execution contract between the Scheduler and the Validation Worker.
