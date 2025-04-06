---
title: "Apache Spark on YARN: Rethinking Distributed Processing Beyond MapReduce"
date: 2015-10-02T09:00:00-04:00
categories:
  - blog
author: Ganesh Raman
tags:
  - Apache Spark
  - YARN
  - MapReduce
  - In-Memory Computing
  - Distributed Systems
  - Data Engineering
---

By October 2015, Apache Spark had officially moved from being a promising successor to MapReduce into the **mainstream engine of choice** for many big data workloads.

Built for **speed, general-purpose compute, and developer productivity**, Spark redefined what it meant to process large-scale data — and while it could run on its own cluster manager or Mesos, most enterprises embraced Spark on **YARN** for its integration with the Hadoop ecosystem.

What made Spark so compelling wasn’t just its developer-friendly APIs or its expressive power — it was how **operationally different** it was from MapReduce, and how it leveraged YARN as a resource orchestrator while managing its own intelligent compute pipeline.

---

## The Architectural Shift: From MapReduce to Resilient Distributed Datasets

MapReduce is stateless. Every job writes intermediate data to HDFS between steps. It’s durable, but expensive:

- Lots of disk I/O
- High job latency
- Rigid two-phase structure (Map → Shuffle → Reduce)

Spark changed the game by introducing **Resilient Distributed Datasets (RDDs)**:

- Immutable, partitioned collections of objects spread across the cluster
- Stored in memory by default
- Able to express complex DAGs of transformations

Instead of chaining multiple MapReduce jobs with intermediate HDFS writes, Spark could express entire workflows in memory:

```scala
val rdd = sc.textFile("hdfs://data.txt")
             .flatMap(_.split(" "))
             .map(word => (word, 1))
             .reduceByKey(_ + _)
```

What would’ve taken multiple jobs in MapReduce is now a single DAG in Spark.

---

## Spark on YARN: Who Does What?

When you run Spark on YARN, you’re combining two systems:

- **YARN** handles resource negotiation: CPU, memory, container placement
- **Spark** handles the compute model: scheduling, task execution, data locality

### Flow of Execution:

1. Spark submits an **ApplicationMaster** to YARN (just like other apps)
2. The AM negotiates containers for the **driver** and **executors**
3. Spark driver builds the DAG of stages and tasks
4. Tasks are shipped to executors as JVM threads
5. Executors perform work, cache RDDs, and report back to the driver

> The key here: **Spark manages task execution independently** once containers are allocated. YARN simply launches and monitors containers — it doesn’t orchestrate individual stages.

This separation of concerns allows Spark to run **faster and more intelligently** than traditional YARN-native models like MapReduce.

---

## Operational Differences from MapReduce

### 1. **Long-Running Executors**
MapReduce launches a new JVM per task attempt — Spark uses **long-lived JVMs** (executors), keeping context and data in memory across stages.

This dramatically reduces overhead.

### 2. **In-Memory Caching**
With `persist()` and `cache()`, Spark lets users explicitly keep datasets in RAM. This is huge for iterative algorithms like machine learning.

### 3. **DAG Execution Engine**
Spark builds a **Directed Acyclic Graph** of transformations, optimizing execution paths, reusing shuffle files, and pipelining tasks where possible.

MapReduce only understands map → shuffle → reduce — no optimization in between.

### 4. **Fault Recovery via Lineage**
Instead of writing to disk every step, Spark remembers **how to recompute** lost partitions via RDD lineage. Failures are fast and scoped.

---

## How JVM Makes Spark Possible

Like Hadoop and YARN, Spark is built on the **JVM**, but it pushes the envelope further:

- Leverages **JVM serialization** for efficient task distribution
- Makes heavy use of **off-heap memory** for caching (via Tungsten)
- Uses **code generation** (via Catalyst) to compile SQL queries to bytecode
- Integrates deeply with **GC tuning and thread management**

The JVM isn’t just a convenience — it’s an **execution platform**. Spark embraces it for its introspection, portability, and performance potential.

---

## Spark on YARN in Production

By 2015, many enterprise workloads were shifting to Spark on YARN:

- ETL pipelines replaced multiple MapReduce jobs with a single Spark app
- SQL-on-Hadoop users moved from Hive on MR to Hive on Spark or Spark SQL
- Data scientists embraced PySpark for exploratory analytics

Cluster administrators benefited too:

- **Unified resource governance** via YARN’s schedulers
- **Multi-tenant isolation** with dynamic executor allocation
- **Consistent monitoring** using Hadoop-native tools

---

## Comparing Execution Philosophies

| Feature                  | MapReduce on YARN        | Spark on YARN              |
|--------------------------|--------------------------|----------------------------|
| Compute Model           | Two-phase (Map + Reduce) | DAG + In-Memory RDDs       |
| Task Execution          | New JVM per task         | Long-lived Executors       |
| Intermediate Data       | HDFS                     | Memory (or Disk if needed) |
| Scheduling              | YARN Controlled          | Spark Controlled           |
| Fault Tolerance         | Re-run task, reread data | RDD lineage-based recompute|
| Ideal Workload          | Batch-only               | Batch, ML, Streaming       |

---

## Lessons from the Field

1. **Spark isn’t just faster — it’s fundamentally different**  
   Memory, lineage, and DAGs shift how jobs are written and executed.

2. **YARN is a launchpad, not a scheduler for Spark**  
   Once containers are allocated, Spark controls everything inside.

3. **JVM enables both flexibility and performance**  
   Spark proves that the JVM can support large-scale, low-latency compute.

4. **Replacing MapReduce requires more than performance**  
   Spark’s expressiveness, APIs, and multi-language support are just as critical.

5. **Understanding operational boundaries matters**  
   Spark + YARN is a powerful combo — but tuning requires knowing who controls what.

---

## If You’re Curious…

- Try writing a multi-stage data pipeline in both MapReduce and Spark — compare the effort
- Run Spark in **cluster mode** and **client mode** on YARN and monitor executor placement
- Explore Spark’s **web UI** to see DAGs and task distribution
- Tune a job with dynamic allocation + caching — and watch memory usage

> “If MapReduce brought data processing to the masses, Spark made it feel like programming again.”

In 2015, Spark running on YARN marked the beginning of a new era — **unifying speed, scale, and simplicity** for big data engineering.

And the revolution was just heating up.

