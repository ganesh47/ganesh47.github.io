---
title: "ADTs, GADTs, and the Architecture of Distributed Computation"
date: 2015-12-30T10:00:00-04:00
categories:
  - blog
author: Ganesh Raman
tags:
  - Haskell
  - ADTs
  - GADTs
  - Distributed Computing
  - Type Systems
  - Apache Spark
  - Hive
  - Abstractions
---

As 2015 draws to a close, Haskell continues to quietly influence how we think about **abstractions, structure, and semantics** in computation — not just locally, but **distributedly**.

Two of Haskell’s most profound type system features — **Algebraic Data Types (ADTs)** and **Generalized Algebraic Data Types (GADTs)** — offer ways to model distributed computations with clarity, safety, and extensibility.

And when used right, these abstractions map beautifully onto real-world data platforms like **Apache Spark** and **Hive**.

---

## What Are ADTs and GADTs?

### ADTs: Building Blocks of Structure

Algebraic Data Types combine **product types** (records/tuples) and **sum types** (enums/variants) into expressive structures.

Example:

```haskell
data Task =
    ReadFile FilePath
  | Transform (String -> String)
  | WriteFile FilePath
```

You can now model an entire job as a **sum of operations** — clean, composable, and enforceable by the compiler.

### GADTs: Adding Type-Level Precision

GADTs allow you to **annotate the return type of each constructor**, enabling more powerful constraints and structure.

```haskell
data Job a where
  LoadCSV   :: FilePath -> Job [Row]
  Filter    :: (Row -> Bool) -> Job [Row] -> Job [Row]
  Aggregate :: ([Row] -> b) -> Job [Row] -> Job b
```

Now, the compiler knows the **types across computation boundaries**, helping you enforce logic that would otherwise require extensive runtime checks.

---

## Thinking Distributedly with ADTs and GADTs

Modeling parallel and distributed compute often involves these concerns:

- How do I represent computation steps?
- How do I express data movement and transformation?
- How do I ensure correctness as I compose?

With ADTs and GADTs, you can model these as **typed ASTs (Abstract Syntax Trees)**. Each node represents a stage — and the **type of each stage constrains what can legally follow**.

This mirrors how systems like Spark or Hive work internally:

- **Spark** builds logical and physical DAGs
- **Hive** generates execution plans from SQL ASTs
- **Tez** composes DAGs for job optimization

Your GADT is a **mini language of computation** — strongly typed, expressive, and easily traversable.

---

## A Realistic Mini DSL for ETL

```haskell
data Pipeline a where
  ReadParquet :: FilePath -> Pipeline [Row]
  FilterRows  :: (Row -> Bool) -> Pipeline [Row] -> Pipeline [Row]
  JoinRows    :: Pipeline [Row] -> Pipeline [Row] -> Pipeline [Row]
  WriteHive   :: TableName -> Pipeline [Row] -> Pipeline ()
```

You can now build a full ETL job as a **data structure**:

```haskell
myJob :: Pipeline ()
myJob =
  WriteHive "users_cleaned" $
    FilterRows (\r -> r.age > 18) $
      ReadParquet "/data/users.parquet"
```

You can:

- Traverse this AST to generate a **Spark job**
- Compile it to **HiveQL**
- Analyze it statically for optimization (e.g., filter pushdown)

This is how **real world orchestration systems** like Airflow or Luigi model tasks — except you now get **type safety for free**.

---

## Why This Works

1. **Data = Computation**  
   Once a program is a value (an ADT or GADT), it can be inspected, transformed, serialized.

2. **Type-Driven Composition**  
   Each transformation knows its input and output types — enabling validation, composition, and optimization.

3. **Backends Become Targets**  
   You can compile your AST to:
   - Spark DAGs
   - Hive queries
   - SQL, Tez, Presto

4. **Program Synthesis and Rewriting**  
   You can write optimizers that rewrite your AST — e.g., push filters closer to reads, combine adjacent operations.

5. **No Runtime Guessing**  
   Errors are caught at compile time — reducing bugs in large data pipelines.

---

## Bridging to Hive, Spark, and Beyond

The real power comes when you take these Haskell-modeled pipelines and **translate them** to concrete systems:

- Your GADT can emit **HiveQL**
- Or generate a **Spark logical plan** via Catalyst DSLs
- Or be serialized to JSON/YAML for orchestration

You can now **describe, validate, and transform jobs before they run** — even simulate or diff changes.

---

## If You’re Curious…

- Look into the `free` and `freer-simple` libraries in Haskell
- Study how `do` notation with Free monads enables embedded DSLs
- Explore projects like **Quasar**, **Fugue**, or **Relude DSLs**
- Try converting a SQL query into a GADT pipeline and compile it to HiveQL

> “When your data pipelines become values, you stop guessing and start transforming.”

In 2015, ADTs and GADTs offer a vision of data compute where **computation is code, code is data, and safety comes from types** — a direction the rest of the distributed computing world is quickly beginning to embrace.

