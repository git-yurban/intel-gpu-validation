# Worker

**Document:** 08-worker.md

---

# Purpose

The Worker is responsible for executing validation workloads on a physical machine.

Workers are intentionally simple.

They do not make scheduling decisions.

They do not understand campaigns.

They do not build software.

They simply execute work described by a Worker Manifest.

The Worker should remain completely stateless.

---

# Responsibilities

The Worker owns:

- Registration
- Heartbeats
- Requesting work
- Preparing execution environments
- Executing tests
- Uploading results
- Publishing telemetry

The Worker does **not** own:

- Scheduling
- Artifact publication
- Retry logic
- Campaign management
- Queue management

---

# High-Level Architecture

```
              Scheduler
                   │
         Worker Manifest
                   │
                   ▼
                Worker
     ┌─────────────┼──────────────┐
     ▼             ▼              ▼
Registration  Artifact Manager  Executor
     │             │              │
     └─────────────┴──────────────┘
                   │
                   ▼
              Result Upload
```

The Worker orchestrates execution but delegates artifact preparation to the Artifact Manager.

---

# Worker Lifecycle

```
Start

↓

Load configuration

↓

Register with Scheduler

↓

Receive Worker ID

↓

Heartbeat loop starts

↓

Request work

↓

Receive Worker Manifest

↓

Prepare artifacts

↓

Execute shard

↓

Upload results

↓

Release artifacts

↓

Request more work

↓

Repeat
```

Workers continuously process work until shutdown.

---

# Startup

During startup the Worker performs:

1. Load configuration.
2. Verify local directories.
3. Initialize Artifact Manager.
4. Register with Scheduler.
5. Start heartbeat thread.
6. Begin requesting work.

No artifacts are downloaded during startup.

---

# Registration

Each Worker registers once.

Registration information includes:

- Worker version
- Hostname
- Operating system
- Architecture
- CPU
- Memory
- GPU
- Kernel version
- Supported APIs
- Available disk space

The Scheduler records these capabilities for scheduling decisions.

---

# Heartbeats

Heartbeats are sent periodically.

Recommended interval:

```
30 seconds
```

Heartbeat payload includes:

- Current state
- Active shard
- Progress
- Cache usage
- Disk usage
- Memory usage
- Software version

Loss of heartbeats indicates worker failure.

---

# Requesting Work

Workers continuously poll for work.

```
Worker

↓

GET /work

↓

No work?

↓

Sleep

↓

Retry
```

When work is available:

```
Receive Worker Manifest

↓

Begin execution
```

---

# Worker Manifest

The Worker Manifest contains everything required to execute a shard.

Typical contents include:

- Build information
- Artifact URIs
- Checksums
- Environment variables
- Test shard
- Timeouts
- Retry metadata

The Worker never performs additional manifest lookups.

---

# Artifact Preparation

The Worker delegates preparation to the Artifact Manager.

```
ArtifactManager.prepare(worker_manifest)
```

The Artifact Manager:

- Downloads missing artifacts
- Verifies checksums
- Extracts archives
- Reuses cached artifacts
- Returns a prepared execution directory

The Worker never interacts with MinIO directly.

---

# Execution Environment

The Artifact Manager returns a prepared directory.

Example:

```
/var/cache/intel-gpu-validation/extracted/mesa-main-4f2c9b8d/
```

The Worker configures:

- PATH
- LD_LIBRARY_PATH
- VK_DRIVER_FILES
- Environment variables from the Worker Manifest

The execution environment is isolated from the host.

---

# Test Execution

Supported suites include:

- Vulkan CTS
- Piglit
- IGT
- OpenGL CTS
- EGL CTS

Additional suites can be integrated through executor plugins.

---

# Execution States

A Worker transitions through the following states:

```
Starting

↓

Idle

↓

Preparing

↓

Executing

↓

Uploading

↓

Cleaning

↓

Idle
```

State changes are reported in heartbeats.

---

# Result Collection

Upon completion, the Worker collects:

- Exit status
- Execution duration
- Standard output
- Standard error
- Logs
- Generated artifacts
- Crash information (if any)

Results are uploaded to the Scheduler.

---

# Artifact Release

After uploading results:

```
ArtifactManager.release(build_name)
```

Reference counts are decremented.

Artifacts remain cached for future reuse.

---

# Error Handling

Infrastructure failures:

- Download failures
- Checksum failures
- Extraction failures

These are reported immediately.

Test failures:

- Assertion failures
- CTS failures
- Piglit failures

These are reported as test results and are not considered Worker failures.

---

# Recovery

Unexpected Worker termination:

```
Heartbeat expires

↓

Scheduler marks shard abandoned

↓

Shard requeued

↓

Another Worker continues
```

No manual recovery is required.

---

# Local State

Workers intentionally store minimal state.

Persistent directories include:

```
cache/

logs/

configuration/
```

All execution state is reconstructed from the Worker Manifest.

---

# Configuration

Typical configuration options:

- Scheduler URL
- Worker name
- Cache location
- Maximum cache size
- Heartbeat interval
- Concurrent executions
- Log level

Configuration should remain independent of scheduling policies.

---

# Concurrency

Initially:

```
One Worker

↓

One active shard
```

Future versions may support multiple concurrent executors.

The Artifact Manager must remain thread-safe.

---

# Telemetry

Workers publish telemetry through MQTT.

Topics include:

```
worker/status

worker/events

worker/performance

worker/cache
```

Telemetry is informational only.

Execution never depends on MQTT availability.

---

# Metrics

Useful Worker metrics include:

- Shards completed
- Average execution time
- Cache hit rate
- Download time
- Extraction time
- CPU utilization
- GPU utilization
- Disk usage
- Memory usage

These metrics should eventually be exported to Prometheus.

---

# Design Principles

## Workers remain stateless.

No execution state survives process restart.

---

## Workers execute.

They never schedule.

---

## Workers prepare through the Artifact Manager.

Storage implementation details remain hidden.

---

## Workers continuously request work.

No long-lived work assignments exist.

---

## Workers are replaceable.

Any Worker should be capable of executing any compatible shard.

---

# Future Enhancements

Planned improvements include:

- Parallel shard execution
- GPU hang recovery
- Automatic reboot handling
- Self-update
- Predictive artifact prefetching
- NUMA-aware scheduling
- Containerized execution
- Resource isolation
- Plugin-based test runners

---

# Summary

The Worker is intentionally lightweight.

It receives a single self-contained Worker Manifest, prepares the required artifacts through the Artifact Manager, executes the assigned shard, uploads results, and immediately requests additional work.

This simplicity makes Workers easy to scale, easy to replace, and resilient to failures.

---

# Next Document

```
09-storage.md
```

This document describes the storage abstraction, URI resolution, MinIO integration, local caching, and future storage backends.