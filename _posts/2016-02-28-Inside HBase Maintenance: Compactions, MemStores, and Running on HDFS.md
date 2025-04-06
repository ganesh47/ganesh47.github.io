---
title: "Inside HBase Maintenance: Compactions, MemStores, and Running on HDFS"
date: 2016-02-28T09:00:00-04:00
categories:
  - blog
author: Ganesh Raman
tags:
  - HBase
  - HDFS
  - Compaction
  - Write-Ahead Log
  - Maintenance
  - NoSQL
  - Distributed Systems
---

By late February 2016, Apache HBase had become a staple of the NoSQL world — the go-to system when teams needed **low-latency, high-throughput access to massive, sparse, and semi-structured datasets**.

Built on top of HDFS, HBase combines the consistency of a key-value store with the scalability of the Hadoop ecosystem. But to make that work, especially under constant write and read pressure, HBase relies on a sophisticated set of **maintenance operations** to keep performance healthy and storage efficient.

Let’s explore how HBase manages itself under the hood.

---

## HBase on HDFS: The Basics

HBase is **not a file system**. It’s a **storage engine** that writes immutable files (called HFiles) to **HDFS**, and relies on HDFS for:

- **Durable storage**
- **Block-level replication**
- **Sequential write throughput**
- **Append-only semantics**

This model gives HBase:

- Scale-out durability with cheap commodity hardware
- Simple replication and failover
- High read concurrency

But because HDFS is **append-only**, HBase has to manage updates, deletes, and cleanup **indirectly**, via background maintenance.

---

## Core Maintenance Components

### 1. **Write-Ahead Log (WAL)**

Every write first hits the **WAL**, a durable log stored on HDFS. If a RegionServer crashes, the WAL is replayed to recover data in memory.

- Append-only
- Stored per RegionServer
- Periodically rolled and archived

### 2. **MemStore Flushes**

After being written to the WAL, data enters an **in-memory structure (MemStore)**. Once it reaches a threshold (e.g., 128MB), it's flushed to disk as an immutable **HFile**.

Flush triggers:

- Size threshold exceeded
- Manual flush request
- Region split

Flushed HFiles live in HDFS and are used for reads until they're compacted.

---

## Compaction: The Heart of HBase Maintenance

HBase doesn’t overwrite data — it **appends new versions**. Old data is removed later by **compaction**.

### Types of Compaction:

#### Minor Compaction

- Merges small HFiles into fewer, larger ones
- Reduces file count, improving read performance
- Triggered automatically when HFile count exceeds a threshold

#### Major Compaction

- Merges **all HFiles** in a region into one
- Discards deleted or expired cells (based on TTL)
- Can be triggered manually or on a schedule

### Why Compaction Matters

- Reduces read amplification
- Reclaims disk space
- Cleans up tombstoned (deleted) data
- Improves block cache efficiency

Without compaction, HBase would become **slow and bloated** over time.

---

## Region Splits and Merges

### Splits

When a region becomes too large (e.g., 10GB), it **splits** into two child regions. This:

- Balances load across RegionServers
- Keeps region sizes manageable
- Improves parallelism for reads/writes

### Merges

In rare cases, **adjacent small regions** may be merged to reduce overhead. This is usually admin-initiated.

---

## Bloom Filters and Block Caches

HBase optimizes reads through:

- **Bloom filters**: Quickly skip files that don’t contain a requested key
- **Block cache**: Stores frequently accessed blocks in memory

Compaction helps keep these effective by reducing duplicate key versions and consolidating storage.

---

## Maintenance Schedulers and Tools

- **Compaction policies** (e.g., SizeTiered or DateTiered)
- **Flush thresholds** (configured per column family)
- **Region balancing** across nodes
- **HBase Shell**: For manual triggering of compactions, flushes
- **JMX and Metrics**: For monitoring compaction queues, flush counts, WAL usage

---

## Failure Recovery and Maintenance

Because everything in HBase is **write-ahead logged** and flushed to HDFS:

- Crashed RegionServers recover via WAL replay
- Data is safe even before flush, thanks to WAL
- WAL and HFile replication leverage **HDFS durability**

> Maintenance is continuous. Recovery is implicit.

---

## If You’re Curious…

- Use `hbase shell` to manually flush or compact regions
- Check `/hbase/WALs` and `/hbase/data` in HDFS to explore file layout
- Monitor `compactionQueueSize` in JMX to detect backlogs
- Test read latency before/after major compaction

> “HBase is fast because it works like a log. But it stays fast because it compacts like a pro.”

In 2016, HBase showcases how thoughtful maintenance operations — flushes, compactions, splits — allow a log-structured system to deliver **low-latency reads and consistent writes** at scale, all while riding on the immutable, append-only backbone of HDFS.

