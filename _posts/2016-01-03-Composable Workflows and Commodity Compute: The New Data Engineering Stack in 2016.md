---
title: "Composable Workflows and Commodity Compute: The New Data Engineering Stack in 2016"
date: 2016-01-05T09:00:00-04:00
categories:
  - blog
author: Ganesh Raman
tags:
  - Data Engineering
  - Distributed Systems
  - Composable Workflows
  - Hadoop
  - Spark
  - Data Lakes
  - Distributed File Systems
  - 2016 Trends
---

It’s January 2016, and the field of **data engineering** is almost unrecognizable from where it stood just a few years ago.

What was once the domain of bespoke ETL scripts, hand-tuned SQL pipelines, and high-end hardware has now evolved into a composable, scalable, and open ecosystem built on **distributed systems**, **workflow orchestration**, and **commodity compute**.

We now have the tools to solve truly massive problems — at petabyte scale — without needing proprietary appliances or monolithic databases. And we have them because of three major forces:

---

## 1. Composable Workflows: From Jobs to DAGs

In 2016, workflows are no longer bash scripts wrapped in cron jobs.

We now express complex data movement and transformation as **directed acyclic graphs (DAGs)** — high-level workflows composed of well-defined tasks, orchestrated and monitored at scale.

Examples:

- **Apache Airflow**: Declarative DAGs in Python
- **Luigi**: Pipeline authoring with state awareness
- **Oozie**: XML-based orchestration on Hadoop

Benefits:

- **Modularity**: Reuse tasks across pipelines
- **Observability**: Track lineage, failures, retries
- **Scalability**: Parallelize task execution across clusters

> Workflows became **code**, and pipelines became **programs**.

---

## 2. Distributed Compute: From Clusters to Platforms

Batch processing used to mean squeezing queries into the nightly load window. Now, it’s a matter of defining **compute graphs** and letting the engine scale.

### The Players:

- **Apache Spark**: In-memory, DAG-based execution for batch, SQL, ML
- **Apache Flink**: Low-latency stream and batch unification
- **Tez**: DAG engine underpinning Hive and Pig
- **Presto**: Distributed SQL engine for federated sources

We’re no longer bound by the MapReduce shuffle model. Instead, we define **composable stages**, and the engines **schedule, optimize, and execute** them across nodes.

All of this runs on **commodity machines** — no specialized hardware needed. You just scale out.

---

## 3. Distributed File Systems and the Rise of the Data Lake

At the foundation of this new world is the humble **distributed file system** — primarily HDFS, but increasingly S3, GCS, and other object stores.

With **schema-on-read**, we can:

- Store **raw, semi-structured, and structured data** together
- Define multiple logical views (tables) over the same data
- Apply late-binding transformations

This has led to the rise of the **data lake** — an infinitely extensible, schema-flexible, cost-effective approach to data storage.

> We don’t predefine what’s important — we keep everything and analyze as needed.

---

## The New Stack: Commodity, Open, Evolving

Data engineering in 2016 isn’t about using the right vendor’s tools — it’s about composing the right open-source primitives:

- **Airflow** for orchestration
- **Spark** for distributed compute
- **HDFS / S3** for storage
- **Hive / Presto** for SQL access
- **Kafka** for real-time ingest
- **Parquet / ORC** for efficient storage

Together, they form a **composable architecture** — one where each component is independently scalable, replaceable, and observable.

And critically, these tools run on **commodity Linux nodes** — across cloud, bare metal, or hybrid environments.

---

## How Data Engineering Has Changed

Then (2012–2014):

- ETL via stored procedures
- Vertica / Teradata / Oracle Exadata
- Batch windows and monolithic jobs
- Schema-bound pipelines

Now (2016):

- DAGs and orchestration
- Open source engines
- Distributed compute with fine-grained tasks
- Flexible, schema-on-read models

This isn’t just tooling — it’s a **paradigm shift**.

---

## What This Enables

- **Interactive querying on terabytes of data**
- **Experimentation with real-time data** (Kafka + Spark Streaming)
- **ML pipelines integrated into ETL**
- **Decoupled producer-consumer data contracts**
- **Versioned, reproducible data workflows**

Data is no longer the byproduct of systems — it’s the **foundation** of business decision-making, analytics, and product intelligence.

---

## If You’re Curious…

- Try building a full DAG in Airflow with Spark tasks
- Explore how S3 + Parquet + Presto enables serverless data lakes
- Read "The Hadoop Papers" and contrast them with Spark’s DAG model
- Run a reproducible ML pipeline using Luigi and Spark MLlib

> “Distributed computing is no longer hard — as long as you compose wisely.”

In 2016, data engineering is about **designing with primitives**. And with the right building blocks, solving problems at scale is not only possible — it’s accessible to everyone with commodity compute and good ideas.

