---
title: "Crash Consistency and File Systems: Insights from the OSDI 2014 Study"
date: 2017-01-10
categories:
- blog
author: Ganesh Raman
tags:
- filesystems
- crash consistency
- osdi
- storage
- research
---

The paper *"All File Systems Are Not Created Equal: On the Complexity of Crafting Crash-Consistent Applications"* by Pillai et al., presented at OSDI 2014, delivers a sobering insight: writing crash-consistent applications is far more complex than developers might assume.

In today’s systems, applications often depend on the underlying file system to preserve consistency in the event of a crash. But as the study shows, the guarantees provided by different file systems vary widely — and these differences can make or break the correctness of applications.

---

## The Core Idea

Applications such as databases and key-value stores implement their own update protocols to ensure that, even in the case of a crash, the stored state remains valid. These protocols often rely on assumptions about *persistence properties* — such as the ordering and durability of writes — provided by the file system.

The problem? These assumptions are often implicit, poorly documented, and inconsistent across different file systems.

---

## Introducing BOB: Block Order Breaker

To test how file systems behave during crash recovery, the authors created BOB (Block Order Breaker), a tool that perturbs block orderings to simulate crashes. BOB exposes how various file systems (like ext4, btrfs, xfs, etc.) actually persist writes to disk.

They discover that no two file systems behave the same — and many do not uphold the persistence properties applications unknowingly depend on. This makes cross-platform crash consistency a minefield.

---

## Enter ALICE: Crash Vulnerability Detection

To identify crash vulnerabilities in real-world software, the team built ALICE (Application-Level Intelligent Crash Explorer), a static analysis tool that scans application code to:

- Detect critical persistence points
- Identify crash-vulnerable sequences
- Map dependencies between I/O and expected consistency behavior

ALICE analyzes the update protocols of systems such as LevelDB, SQLite, Git, ZooKeeper, and QEMU. The result: over **60 crash vulnerabilities** — many with severe data corruption implications.

---

## Why This Matters

Crash consistency is not just a kernel or filesystem problem — it's an application problem. Developers must:
- Understand how their application uses file system primitives
- Know which file systems actually provide the guarantees they need
- Avoid relying on implicit or assumed ordering of fsync, rename, and write operations

This paper is a wake-up call: without disciplined crash-consistency protocols and awareness of file system behavior, data safety is at risk.

---

## Final Thoughts

Modern file systems vary significantly in how they handle persistence. Crash-consistent applications must be explicitly aware of these behaviors — and tools like BOB and ALICE help surface invisible assumptions.

> "All file systems are not created equal — and neither are the applications that run on them."

If your system writes to disk and you care about your data, this paper is essential reading.

[Read the full paper at USENIX OSDI 2014](https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-pillai.pdf)

