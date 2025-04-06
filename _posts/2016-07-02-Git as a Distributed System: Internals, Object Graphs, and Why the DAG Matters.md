---
title: "Git as a Distributed System: Internals, Object Graphs, and Why the DAG Matters"
date: 2016-07-02
categories:
  - blog
author: Ganesh Raman
tags:
  - git
  - DVCS
  - data-structures
  - conflict-resolution
  - DAG
---

When we use Git every day, it feels simple: `git commit`, `git push`, `git merge`. But underneath the CLI, Git is one of the most interesting and elegant distributed systems in active use today. Unlike centralized version control tools, Git is a **Distributed Version Control System (DVCS)** — which means **every clone of a repository is a full copy**, complete with history, metadata, and branching information.

But distributed systems are hard. And Git solves a remarkably complex set of problems through a clever use of **immutable data structures**, **content-addressed storage**, and **Directed Acyclic Graphs (DAGs)**.

## Git as a Distributed System

In Git, there is no "central server" by design. Every developer’s local repository holds:

- The complete commit history
- All branches and tags
- The full working tree and index
- The `.git/objects` database of every snapshot ever recorded

This distributed nature provides **resilience**, **autonomy**, and **speed**. Developers can work offline, review history, and resolve conflicts independently — without relying on a networked server.

What makes this work? Git’s internal model, built around **immutable objects**.

## The Object Model

At its core, Git stores just four kinds of objects:

1. **Blob** – content of a file
2. **Tree** – directory structure
3. **Commit** – snapshot reference and metadata
4. **Tag** – annotated marker of a commit

Every object is **addressed by the SHA-1 hash** of its content. This makes Git fundamentally a **content-addressable file system**, where two identical files (or commits) always resolve to the same hash.

When you commit, Git writes:

- A tree of your file hierarchy
- One or more blobs for file contents
- A commit object that points to the tree and its parent(s)

This structure forms a **DAG** — a Directed Acyclic Graph — of commits. No cycles. No ambiguity. Just a clear, traceable lineage of your code.

## Why the DAG Matters

The DAG is not just a data structure — it’s Git’s **core consistency model**.

- Each commit points to its parent(s), creating a one-way path through history
- Branches are just **named pointers** to commits
- Merges combine two or more DAG paths into a new commit with multiple parents

Because all references are immutable (a commit can’t be changed once written), the DAG remains **acyclic**. This means:

- You can always trace back to the root
- History is never lost — only hidden (until garbage collected)
- Conflicts happen at merge time, not write time

This immutability and acyclic guarantee make Git **reliable in a distributed environment**. It doesn't rely on locks, central databases, or complex synchronization.

## Conflict Resolution and Merging

Conflict resolution in Git is not about locking resources like in traditional SCM systems. Instead, it's **semantic** and **state-based**.

Git uses a **three-way merge algorithm**:

1. Your local branch
2. The remote branch you're merging
3. Their **common ancestor** (computed via DAG traversal)

Because the DAG encodes full history, finding this ancestor is deterministic. Git then computes diffs between each branch and the ancestor to surface conflicts — which you resolve locally.

## Branching and the Power of Isolation

Branches in Git are extremely lightweight. They are just **references to commit hashes**, nothing more. Because all data is local and immutable, creating a new branch is instantaneous. This is a major departure from systems like Subversion, where branching is an expensive operation.

With distributed branching, each user can explore changes independently. Later, Git’s **merge machinery** brings them together. And because the history is embedded in the DAG, we can always trace who made what change and when.

## Conclusion: Distributed, Immutable, Efficient

Git’s design is an elegant solution to the hard problem of **distributed collaboration**. It doesn’t try to hide complexity — it gives you powerful tools built on strong foundations:

- **Content-addressed objects** for consistency
- **Immutable commits** for reliability
- **Directed acyclic graphs** for traceable history
- **Decentralization** for autonomy and speed

Even though it wasn’t designed as a general distributed systems tool, Git embodies many principles that modern distributed databases, consensus systems, and data pipelines borrow from today.

> Git’s DAG is more than a history — it’s a model of truth that scales across people, time, and systems.