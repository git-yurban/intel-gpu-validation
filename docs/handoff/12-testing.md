# Database

**Document:** 12-database.md

---

# Purpose

PostgreSQL provides the persistent data store for the Intel GPU Validation Lab.

It records operational state, execution history, and scheduling metadata.

The database does not store artifacts or manifests.

Instead, it stores references to immutable artifacts and execution metadata.

---

# Responsibilities

The database owns:

- Campaigns
- Workers
- Shards
- Results
- Retry history
- Execution statistics
- Worker capabilities

The database does **not** own:

- Artifacts
- Build Manifests
- Worker Manifests
- Scheduler Manifests

These remain immutable files in object storage or transient scheduler state.

---

# High-Level Architecture

```
          Scheduler
              │
              ▼
        PostgreSQL
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 Campaigns Workers Results
```

PostgreSQL is the authoritative source for persistent operational data.

---

# Design Principles

The database should contain only information that cannot be reconstructed from manifests or object storage.

This keeps the schema compact and reduces duplication.

---

# Campaigns

A campaign represents one validation request.

Typical fields:

```
Campaign ID

Build ID

Status

Priority

Created

Started

Completed

Owner

Summary
```

The campaign references a Build Manifest but does not embed it.

---

# Workers

Each registered Worker has one record.

Recommended fields:

```
Worker ID

Hostname

Version

Operating System

Kernel

Architecture

CPU

Memory

GPU

Status

Last Heartbeat

Current Shard

Capabilities
```

Workers update these records periodically.

---

# Shards

Each execution unit is tracked independently.

Typical fields:

```
Shard ID

Campaign ID

Suite

Status

Worker ID

Retries

Started

Completed

Duration
```

The Scheduler uses shard state to determine campaign progress.

---

# Results

Each completed shard produces a result record.

Typical fields:

```
Result ID

Shard ID

Worker ID

Exit Status

Passed

Failed

Skipped

Execution Time

Logs URI

Created
```

Large logs and artifacts remain in object storage.

The database stores only references.

---

# Retry History

Retries are tracked independently.

Recommended fields:

```
Retry ID

Shard ID

Attempt

Reason

Timestamp
```

This history supports debugging and flaky test analysis.

---

# Worker Capabilities

Capabilities are normalized for efficient scheduling.

Examples:

- GPU generation
- Vulkan version
- Kernel version
- Debug support
- ASan support

Capability matching occurs in the Scheduler.

---

# Relationships

```
Campaign

↓

Shards

↓

Results

↓

Workers
```

Campaigns contain many shards.

Workers execute many shards.

Results belong to exactly one shard.

---

# State Model

Campaign:

```
Created

↓

Running

↓

Completed

↓

Archived
```

Shard:

```
Queued

↓

Running

↓

Succeeded

or

Failed

or

Retried
```

Worker:

```
Offline

↓

Idle

↓

Preparing

↓

Executing

↓

Uploading
```

---

# Indexing

Recommended indexes:

- Campaign ID
- Build ID
- Worker ID
- Shard Status
- Worker Status
- Last Heartbeat
- Created Timestamp

Indexes should optimize scheduling queries.

---

# Data Retention

Suggested policy:

Campaigns:

```
2 years
```

Results:

```
2 years
```

Worker records:

```
Current + history
```

Logs remain in object storage according to separate retention policies.

---

# Transactions

Scheduling operations should be transactional.

Examples:

- Create campaign
- Register worker
- Assign shard
- Complete shard

This prevents inconsistent scheduling state.

---

# Metrics

Useful database metrics include:

- Active campaigns
- Active workers
- Pending shards
- Completed shards
- Retry rate
- Average execution time
- Database size

These metrics support operational monitoring.

---

# Schema Evolution

Database migrations should be version-controlled.

Recommended tooling:

- Alembic
- SQLAlchemy migrations

Schema changes should preserve backward compatibility whenever practical.

---

# Design Principles

## Store references, not copies.

Avoid duplicating manifest data.

---

## Normalize operational state.

Persistent state should support efficient scheduling.

---

## Immutable build data stays outside the database.

The database references immutable Build IDs.

---

## Optimize for reads.

Scheduling decisions occur frequently.

The schema should prioritize query performance.

---

# Future Enhancements

Planned additions include:

- Historical performance analysis
- Flaky test detection
- Worker maintenance windows
- Campaign templates
- Build provenance tracking
- Machine quarantine history
- Multi-site federation
- Advanced analytics

---

# Summary

PostgreSQL stores the operational state of the validation platform.

By keeping immutable manifests outside the database and storing only references and execution metadata, the schema remains compact, efficient, and easy to evolve.

---

# Next Document

```
13-redis.md
```

This document describes Redis usage for transient work distribution, shard claiming, queue management, and fault recovery.