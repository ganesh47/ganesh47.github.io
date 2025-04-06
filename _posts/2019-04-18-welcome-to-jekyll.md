---
layout: post
title: "Evolving DSLs, Type Systems, and Learning from Haskell"
date: 2015-07-18T15:34:30-04:00
author: Ganesh Raman
---

When I first began building domain-specific languages (DSLs), I focused on surface-level structure. Syntax. Keywords. Aesthetics. I believed if the language looked clean and intuitive, people would adopt it. And to an extent, that worked — good syntax lowers the barrier to entry.

But over time, something kept gnawing at me. Once users got past the initial novelty, they wanted to express deeper domain logic. Business rules became more complex. Edge cases multiplied. The domain itself kept shifting under our feet. Our once-beautiful DSLs became brittle.

The problem wasn’t the syntax.

It was the **lack of structure underneath the syntax** — a foundation for semantics, evolution, and correctness. What we needed wasn’t more clever parsing. What we needed were **types**.

> “Types are not about catching errors. Types are about making illegal states unrepresentable.”  
> — *Yaron Minsky*

---

## DSLs Beyond Syntax: The MPS Paradigm

This realization led me to explore **JetBrains MPS** — a language workbench designed for creating and evolving DSLs. MPS introduced me to **projectional editing**, where you manipulate the program’s abstract syntax tree (AST) directly, bypassing parsing entirely.

At first, it felt weird. Editors were rigid. You couldn't just “type stuff.” But then I started seeing the upside: MPS allowed me to build **multi-modal DSLs** — mixing tables, diagrams, checkboxes, code, and validation rules — all in one place. It let me build **tooling-first languages**, where constraints, auto-completions, and editor behavior were as much a part of the language as the syntax.

Most importantly, MPS let me define a **custom type system**.

Not just in the sense of “integers and strings,” but with full-blown inference, scoping rules, constraints, and typing logic specific to my domain. I could say things like:

- “A workflow node must have a valid transition target.”
- “A risk model must only be applied to validated instruments.”
- “A fee must not exceed the net revenue of a transaction.”

In my DSLs, **types became a modeling tool**. They enforced rules, not with `if` statements, but with structure. As the DSL evolved, the type system grew with it — guiding users, catching issues, and enabling large-scale refactoring without fear.

This felt powerful. But I knew I was only scratching the surface.

---

## Learning from Haskell: Purity, Composition, and Clarity

To truly internalize how type systems can shape thinking, I turned to **Haskell** — a purely functional language with a famously expressive type system. Haskell has long been a laboratory for programming language design, and its influence can be felt across ecosystems, from Scala to Rust to TypeScript.

At first, Haskell frustrated me. There was no `for` loop. No mutable variables. Errors like `couldn’t match type 'IO' with 'String'` made little sense. But as I stuck with it, something clicked.

Haskell forces you to **design your programs from the outside in**. You start with the types:

```haskell
generateReport :: User -> [Transaction] -> Report
```
You ask: What are the inputs? What are the guarantees? The compiler becomes an ally. If your program compiles, you’ve already proven a large set of invariants. No nulls, no side-effects slipping through, no runtime type mismatches.

“Make illegal states unrepresentable.”
Haskell takes this mantra and bakes it into the core of how you think.
It also taught me the power of composition. In Haskell, small pure functions can be composed like Lego blocks — predictable, testable, and side-effect free. Instead of building large monoliths, you build pipelines of transformations, each type-safe, each testable in isolation.

Haskell’s type classes opened up a world of polymorphism without inheritance. Monads, while memed to death, turned out to be not mystical at all — just a pattern for sequencing computations that carry context (like state, IO, or failure).

Most of all, Haskell taught me this: types are not annotations — they are design constraints. And great constraints make great software.

DSLs as Typed Modeling Environments

Returning to my DSL work with this mindset, I saw the possibilities explode.

Why not model valid transitions as types? Why not model role-based permissions as type constraints? Why not enforce temporal correctness — e.g., no settlement without approval — through the type checker?

A DSL should not be a lightweight scripting veneer. It should be a typed modeling environment, where the language expresses not just what’s possible, but what’s allowed, expected, and guaranteed.

With MPS, I could encode these rules natively. For example:

A “Workflow” concept could have a validate() constraint that checks connections.
A “Transaction” DSL element could have type constraints ensuring mandatory fields are set, calculated fields match rules, and dates follow logical order.
Business-specific expressions (like eligibility rules or tax computations) could use custom type inference for correctness, even when syntax was user-defined.
By embedding type safety into the authoring process, I could turn the DSL into a guarded space — one that lets users explore and model freely, but within domain boundaries.

This, to me, felt like the right direction.

But there was one more dimension to explore — the deep end of type theory.

Dependent Types: Precision at Compile-Time

Enter dependent types — a world where types can depend on values. Languages like Idris, Agda, and Coq operate in this space, where code and proofs coexist.

Here’s a simple example in Idris:

data Vect : Nat -> Type -> Type where
Nil  : Vect 0 a
(::) : a -> Vect n a -> Vect (S n) a
This defines a vector that knows its length at the type level. That means you can enforce, at compile time, that two vectors must be of the same size before zipping them.

Want to prove that reversing a list twice gives you the original list?

In Agda or Coq, you can write that proof, and the compiler will check it for you.

This isn't about code coverage or unit tests. This is about formally verified correctness — about having machine-checked guarantees of the properties your system depends on.

In critical systems — think avionics, crypto, medical devices — this is gold. But even in everyday domains like finance or infrastructure tooling, the core idea is inspiring: build systems where the types prove the behavior.

While I didn’t bring full dependent types into my MPS-based DSLs, the mindset deeply influenced how I designed them. I started asking:

Can we make impossible configurations unrepresentable?
Can we encode temporal rules (e.g., must settle before reporting) into type constraints?
Can we structure the DSL such that business rules emerge as theorems, not runtime checks?
Bringing It All Together

This journey — from building DSLs in MPS to exploring functional purity in Haskell to learning about formal verification with dependent types — has reshaped how I think about software.

Here’s what I believe now:

1. Syntax is the skin, types are the skeleton.
   DSLs must look approachable, yes — but it’s the type system that gives them structure and longevity. As the domain grows more complex, a solid type foundation lets your language evolve safely.

2. Types are not limitations — they are design feedback.
   The more expressive your type system, the more it helps you catch unclear thinking. Haskell taught me that if a function is hard to type, maybe it’s doing too much. The compiler is your first reviewer.

3. Types can encode intention.
   In well-typed systems, reading a type signature tells you what a function does and what it won’t do. A good type is a contract, not just a container.

4. The future of software is typed modeling.
   As systems become more autonomous, interconnected, and critical, we need better models — models that are safe, evolvable, and verifiable. Whether in infrastructure-as-code, finance, IoT, or AI safety — types will be the lens through which we make systems explainable and correct.

If You’re Curious…

Here’s how you can dive deeper:

Try JetBrains MPS: Start with the Fast Track tutorial to build a DSL with real tooling.
Learn Haskell: Read Learn You a Haskell for Great Good! or Real World Haskell. Don't be intimidated — even partial exposure will rewire your thinking.
Explore Dependent Types: Play with Idris or Agda. You don’t need to become a proof theorist. Just getting a taste will elevate your design instincts.
Talks to Watch:
Types as the Calculus of Programs – Philip Wadler
The Unreasonable Effectiveness of Dependent Types – Edwin Brady
Functional Programming is Easier Than You Think – Jessica Kerr
“We shape our tools, and thereafter our tools shape us.”
— Marshall McLuhan

More than ever, I believe this: types are tools for thought. If we learn to wield them with curiosity and care, we can build systems that are not only more powerful — but more correct, maintainable, and humane.
