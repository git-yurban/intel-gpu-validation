# Dashboard

**Document:** 15-dashboard.md

---

# Purpose

The Dashboard provides a real-time operational view of the Intel GPU Validation Lab.

It is intended for developers, validation engineers, infrastructure administrators, and release managers.

The Dashboard never controls execution directly.

All operations are performed through the Scheduler API.

---

# Responsibilities

The Dashboard provides visibility into:

- Campaigns
- Workers
- Build status
- Queue health
- Cache utilization
- Test progress
- Historical execution
- Infrastructure health

The Dashboard does **not**:

- Execute tests
- Schedule work
- Publish artifacts
- Modify workers directly

---

# High-Level Architecture

```
                 Browser
                    │
                    ▼
             Dashboard UI
                    │
                    ▼
             Scheduler API
             ┌─────────────┐
             ▼             ▼
       PostgreSQL        MQTT
```

The Dashboard retrieves persistent state through the Scheduler API and receives live updates from MQTT.

---

# Primary Views

The Dashboard consists of several major views:

- Overview
- Campaigns
- Workers
- Builds
- Queue
- Cache
- Results
- System Health

---

# Overview

The landing page provides a high-level summary.

Typical information:

```
Active Campaigns

Idle Workers

Running Workers

Pending Shards

Queue Depth

Cache Hit Rate

Infrastructure Health
```

This page answers the question:

> "Is the lab healthy?"

---

# Campaign View

Displays all campaigns.

Typical columns:

- Campaign ID
- Build ID
- Status
- Progress
- Priority
- Owner
- Started
- Duration

Selecting a campaign displays detailed execution progress.

---

# Campaign Details

Displays:

- Build information
- Test suites
- Progress
- Worker distribution
- Retry count
- Execution timeline
- Result summary

Users can drill down to individual shards.

---

# Worker View

Displays every registered Worker.

Typical information:

- Worker ID
- Hostname
- GPU
- Current State
- Current Shard
- CPU Usage
- Memory Usage
- Cache Usage
- Last Heartbeat

Workers are color-coded by state.

---

# Worker States

Typical states:

```
Offline

Idle

Preparing

Executing

Uploading

Maintenance
```

State changes update in real time.

---

# Build View

Displays published builds.

Information includes:

- Repository
- Branch
- Git SHA
- Build Type
- Publication Time
- Artifact Size

The Dashboard links directly to Build Manifests.

---

# Queue View

Displays Scheduler queues.

Typical metrics:

- Queue depth
- Average wait time
- Claims per second
- Retry queue size

Queue health helps identify bottlenecks.

---

# Cache View

Displays cache statistics.

Typical metrics:

- Cache size
- Cache hit rate
- Downloads avoided
- Active references
- Disk usage

Workers with unhealthy caches are highlighted.

---

# Result View

Displays completed shards.

Information includes:

- Worker
- Duration
- Passed
- Failed
- Skipped
- Retry Count

Detailed logs remain in object storage.

---

# System Health

Displays infrastructure status.

Components include:

```
Scheduler

PostgreSQL

Redis

MinIO

Buildbot

Workers
```

Each component reports:

- Status
- Version
- Uptime

---

# Live Updates

The Dashboard subscribes to Scheduler-published MQTT topics.

Examples:

```
scheduler/events

scheduler/workers

scheduler/campaigns

scheduler/system
```

The Dashboard never communicates directly with Workers.

---

# Search

Supported searches:

- Campaign ID
- Build ID
- Git SHA
- Worker ID
- Hostname
- Test Suite

Search should be instantaneous.

---

# Filtering

Users may filter by:

- Build
- Campaign
- Worker
- GPU
- Branch
- Status
- Build Type

Filters may be combined.

---

# Historical Data

Historical views include:

- Campaign history
- Worker utilization
- Build history
- Failure trends
- Retry statistics

Data is retrieved from PostgreSQL.

---

# Authentication

Recommended roles:

```
Viewer

Engineer

Administrator
```

Permissions are enforced by the Scheduler API.

---

# Performance

The Dashboard should remain responsive with:

- 500 Workers
- 100 Active Campaigns
- Millions of completed shards

Pagination and lazy loading should be used where appropriate.

---

# Design Principles

## Read-only by default.

Operational changes occur through the Scheduler API.

---

## Real-time updates.

MQTT provides live operational visibility.

---

## Scheduler owns all state.

The Dashboard never communicates directly with infrastructure components.

---

## Historical and live data coexist.

Persistent data comes from PostgreSQL.

Live events come from MQTT.

---

# Future Enhancements

Planned improvements include:

- Grafana embedding
- Campaign comparison
- Heat maps
- GPU utilization charts
- Worker topology view
- Failure analysis
- Mobile-friendly UI
- Dark mode

---

# Summary

The Dashboard provides a comprehensive operational view of the validation platform.

By combining persistent state from PostgreSQL with live telemetry from the Scheduler, it offers real-time insight into campaigns, workers, and infrastructure while maintaining a clean separation from the execution path.

---

# Next Document

```
16-security.md
```

This document describes authentication, authorization, secrets management, TLS, service identities, and secure communication between platform components.