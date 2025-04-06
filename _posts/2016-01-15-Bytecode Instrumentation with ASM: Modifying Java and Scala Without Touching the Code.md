---
title: "Bytecode Instrumentation with ASM: Modifying Java and Scala Without Touching the Code"
date: 2016-01-15T08:30:00-04:00
categories:
  - blog
author: Ganesh Raman
tags:
  - ASM
  - Bytecode
  - Instrumentation
  - Java
  - Scala
  - SBT
  - Performance Monitoring
---

In January 2016, bytecode manipulation isn't just a niche trick — it's a **powerful capability** that lets you inspect, modify, and enhance Java or Scala applications **without altering source code**.

At the heart of this superpower is **ASM**, a lightweight and high-performance Java bytecode framework used by tools like **AspectJ**, **Mockito**, **CGLIB**, and **Kamon**.

Using ASM, you can:

- Inject logging
- Track performance metrics
- Rewrite method bodies
- Add new fields or annotations
- Hook into class loading without reflection

All **without modifying the original source code or build logic**.

---

## Why Bytecode Instrumentation Matters

In distributed systems and production-grade services, we often need:

- **Performance observability**
- **Audit logging**
- **Security enforcement**
- **Dependency tracking**

Rewriting source code manually for each of these is impractical. Bytecode rewriting lets you introduce such behavior **post-compilation**, automatically.

This is especially valuable for **libraries you don’t control** or for injecting behavior across dozens of microservices consistently.

---

## How ASM Works

ASM reads `.class` files and lets you transform them using a visitor-style API.

A minimal example:

```scala
import org.objectweb.asm._

class MyClassVisitor(api: Int, cv: ClassVisitor) extends ClassVisitor(api, cv) {
  override def visitMethod(...): MethodVisitor = {
    val mv = super.visitMethod(...)
    new MyMethodVisitor(Opcodes.ASM5, mv)
  }
}

class MyMethodVisitor(api: Int, mv: MethodVisitor) extends MethodVisitor(api, mv) {
  override def visitCode(): Unit = {
    super.visitCode()
    mv.visitFieldInsn(...)
    // Inject your bytecode logic here
  }
}
```

You can use the ASM `ClassReader` and `ClassWriter` to rewrite compiled classes before the JVM loads them — or as a compile-time transform in your build.

---

## Using ASM with Scala and SBT

You can easily integrate ASM into a **Scala SBT** project using a custom plugin or task:

```scala
// project/plugins.sbt
addSbtPlugin("com.typesafe.sbt" % "sbt-bytecode" % "0.1")
```

Or define your own transform:

```scala
import java.io._
import org.objectweb.asm._

val instrumentClasses = taskKey[Unit]("Rewrite bytecode with ASM")

instrumentClasses := {
  val classFiles = (Compile / classDirectory).value
  val allClasses = (classFiles ** "*.class").get

  allClasses.foreach { file =>
    val reader = new ClassReader(new FileInputStream(file))
    val writer = new ClassWriter(ClassWriter.COMPUTE_FRAMES)
    val visitor = new MyClassVisitor(Opcodes.ASM5, writer)
    reader.accept(visitor, 0)

    val out = new FileOutputStream(file)
    out.write(writer.toByteArray)
    out.close()
  }
}
```

Run it with:

```bash
sbt instrumentClasses
```

This lets you rewrite bytecode as part of your build — without altering any source code.

---

## Practical Use Cases

### 1. **Timing and Tracing**
Inject `System.nanoTime()` at method entry/exit to log durations.

### 2. **Auto-metrics**
Automatically tag methods with metrics using something like Prometheus or Kamon.

### 3. **Debug Logging**
Insert trace logs into specific package methods without touching source.

### 4. **API Deprecation/Enforcement**
Add runtime checks or throw warnings if deprecated APIs are invoked.

---

## Efficiency and Footprint

ASM is extremely fast — it operates at the byte array level, without parsing source or invoking reflection.

- **Compile-time cost**: negligible (<100ms per class)
- **Runtime cost**: zero, since all transformations are done before load
- **Footprint**: single jar (~100KB)

For teams doing observability, tracing, or AOP at scale — this is a game-changer.

---

## If You’re Curious…

- Explore **Kamon** and **New Relic** — they use ASM to instrument JVM code at runtime
- Look at **Scala Macros** vs. **ASM** — compile-time vs. bytecode transform tradeoffs
- Study **AspectJ** and **ByteBuddy** as higher-level alternatives to ASM
- Use `javap -c` to inspect bytecode before/after

> “Bytecode instrumentation gives you runtime control without touching your code.”

In 2016, as Scala and Java systems scale up in size and complexity, tools like ASM let us weave in critical logic **without polluting business code**.

That’s not just clean — it’s powerful, flexible, and production-grade.

