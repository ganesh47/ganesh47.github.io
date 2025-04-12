---
title: "Understanding Linux cgroups: The Foundation of Resource Isolation in LXC"
date: 2017-02-10
author: Ganesh Raman
tags: [linux, containers, lxc, cgroups, system internals, kernel, process-isolation]
categories: [blog]
---
# Understanding Linux cgroups: The Foundation of Resource Isolation in LXC

In Linux, **cgroups** (short for *control groups*) serve as one of the core mechanisms enabling fine-grained resource control and process isolation. They are the backbone of modern container technologies like **LXC (Linux Containers)**, and without them, resource-limited multi-tenant systems would be nearly impossible to implement securely.

## What Are cgroups?

Control groups are a Linux kernel feature that allow me to allocate, prioritize, deny, manage, and monitor the resource usage (CPU, memory, disk I/O, network, etc.) of collections of processes. Unlike traditional UNIX permissions or process trees, cgroups treat resource limits as first-class citizens.

I can think of them as a hierarchical structure where each node defines specific constraints and applies them to the processes or threads attached to that node.

## Key Capabilities of cgroups

As of kernel 4.x, cgroups provide:

- **CPU throttling**: Control how much CPU time a group of processes can consume via `cpu.cfs_quota_us` and `cpu.cfs_period_us` files.
- **Memory limits**: Define hard or soft limits on memory usage; enforce OOM-killing policies using files like `memory.limit_in_bytes` and `memory.oom_control`.
- **Block I/O limits**: Restrict disk bandwidth usage using `blkio.throttle.read_bps_device` and related files.
- **Device access control**: Limit access to specific device files using `devices.allow` and `devices.deny`.
- **Network priority**: Classify traffic using `net_cls.classid` and netfilter rules.

Each of these is implemented as a separate *controller*, which is a kernel module handling a specific type of resource.

## Anatomy of a cgroup

Every cgroup is part of a hierarchy, and each controller can attach to exactly one hierarchy. I can mount these hierarchies just like a virtual filesystem, for example:

```bash
mkdir -p /sys/fs/cgroup/memory/mygroup
mount -t cgroup -o memory memory /sys/fs/cgroup/memory
```

To add a process to a memory-limited cgroup:

```bash
echo $$ > /sys/fs/cgroup/memory/mygroup/tasks
echo 50000000 > /sys/fs/cgroup/memory/mygroup/memory.limit_in_bytes
```

To programmatically interact with cgroups from user space, developers can use system programming APIs like `libcgroup` or directly manipulate the pseudo-files via standard C library calls (`open()`, `write()`, etc.).

## How LXC Uses cgroups

**Linux Containers (LXC)** leverage cgroups to isolate system resources between containers. Alongside **namespaces** (for PID, network, mount, and UTS isolation), cgroups ensure that:

- One container cannot exhaust CPU or memory of the host.
- Disk I/O bandwidth can be split fairly between containers.
- Network traffic shaping can be applied per container.
- Specific devices can be exposed to a container while hiding others.

The LXC configuration file typically maps container resource limits to cgroup parameters. For example:

```ini
lxc.cgroup.memory.limit_in_bytes = 256M
lxc.cgroup.cpu.shares = 512
```

This creates predictable and repeatable environments per container.

## cgroups and Security

While cgroups themselves do not provide *security* in the form of sandboxing or access control, they serve as critical enforcement tools. Combined with capabilities like **seccomp**, **AppArmor**, or **SELinux**, I can create containers that are both isolated and secure.

For example, a process inside a container hitting its memory limit will be OOM-killed without affecting neighboring containers or the host.

## cgroups v2

The newer unified hierarchy model, cgroups v2, simplifies configuration and makes resource constraints more predictable. Instead of having separate mounts for each controller, cgroups v2 uses a single unified tree. Key interfaces include:

- `memory.max`
- `cpu.max`
- `io.max`

The interface is more consistent but requires newer tools and kernel support. Transitioning from v1 to v2 is gradual in many enterprise systems.

## Summary

cgroups form the heart of resource control in Linux. They allow me to define how much of the system a process or container can use, which is crucial for building secure, multi-tenant systems. Together with namespaces, cgroups make LXC a powerful lightweight virtualization tool that continues to power containerization today. From mounting control filesystems to applying limits via shell or C APIs, cgroups give Linux unmatched flexibility in systems programming and resource isolation.

