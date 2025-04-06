---
title: "Understanding YARN's Resource Manager: Scheduling Policies at Scale"
date: 2016-06-22T09:00:00-04:00
categories:
  - blog
author: Ganesh Raman
tags:
  - YARN
  - Resource Manager
  - Scheduling
  - Fair Scheduler
  - Capacity Scheduler
  - Hadoop
  - Distributed Systems
---

As of June 22, 2016, Apache Hadoop YARN (Yet Another Resource Negotiator) continues to power many of the world’s largest data platforms. At the heart of YARN lies the **Resource Manager (RM)** — a global master responsible for **allocating cluster resources** among competing applications.

The RM acts as a **traffic controller** in a busy compute environment, ensuring fairness, efficiency, and adherence to organizational priorities. Understanding how it works — and how its scheduling policies operate — is key to running a balanced and responsive Hadoop cluster.

---

## What the Resource Manager Does

The Resource Manager coordinates cluster activity by:
- Tracking available resources (memory, vCores) across all nodes
- Receiving application requests (from ApplicationMasters)
- Granting containers to applications based on scheduling policy
- Enforcing access controls, queues, and capacity limits

It maintains a **global view of cluster state** and uses that to make resource allocation decisions in real-time.

---

## YARN Scheduling Models

YARN supports multiple built-in scheduling policies:

### 1. **Capacity Scheduler** (Default in many Hadoop distros)
- Designed for **multi-tenant clusters**
- Divides cluster into hierarchical queues
- Each queue is allocated a **minimum capacity** (percentage)
- Supports **elastic resource sharing** across queues when idle

Example use case:
- A bank’s compliance team is guaranteed 25% of the cluster but can use more if others are idle

### 2. **Fair Scheduler** (Popularized by Cloudera)
- Aims to give every application **equal opportunity over time**
- Jobs receive roughly equal share of resources
- Supports **preemption** to reclaim fairness
- Allows **user, pool, and app-level configuration**

Example use case:
- A shared analytics cluster where long-running and ad-hoc jobs coexist

### 3. **FIFO Scheduler** (Rarely used in production)
- Simpler, single-queue, first-come-first-serve model
- No fairness or capacity controls

---

## Resource Allocation Granularity

YARN allocates resources in **containers** — bundles of memory and vCores.

Each container runs on a **NodeManager**, and applications request containers based on their needs:

```json
{ "memory": 4096, "vCores": 2 }
```

The Resource Manager matches these requests against current cluster availability and enforces limits defined by the scheduler.

---

## Priority, Labels, and Placement

Advanced features include:

- **Application priority**: Influence which apps get scheduled first
- **Node labels**: Restrict workloads to specific nodes (e.g., GPU-enabled)
- **Locality-aware scheduling**: Prefer nodes where input data resides
- **Preemption**: Kill or suspend lower-priority tasks to meet fairness goals

---

## Monitoring and Tuning

Administrators can:
- View active queues and utilization via the **ResourceManager UI**
- Use `yarn scheduler` CLI to inspect queue configuratio