---
title: "Purely Functional Libraries in Scala: Composability Meets Trees"
date: 2016-08-02
categories:
- blog
author: Ganesh Raman
tags:
- scala
- functional programming
- trees
- fp
- libraries
---

In the world of Scala, purely functional programming offers a powerful way to write predictable, composable, and reusable code. Libraries like [Cats](https://typelevel.org/cats/) and [Scalaz](https://scalaz.github.io/7/) bring abstractions from category theory and algebraic structures to mainstream developers, enabling us to work with immutable data and pure functions at scale.

One of the strengths of this approach is how it helps structure algorithms over recursive data structures like trees. With higher-order functions like `fold`, we express complex operations declaratively — abstracting away traversal logic and focusing on the *what*, not the *how*.

---

## Modeling a Binary Tree

Let’s define a simple algebraic data type for a binary tree:

```scala
sealed trait Tree[+A]
case class Leaf[A](value: A) extends Tree[A]
case class Branch[A](left: Tree[A], right: Tree[A]) extends Tree[A]
```

This structure is immutable, recursive, and perfect for functional folds.

---

## Folding a Tree

We define a generic fold function to abstract traversal over the tree:

```scala
def fold[A, B](tree: Tree[A])(leafFn: A => B)(branchFn: (B, B) => B): B = tree match {
  case Leaf(v)      => leafFn(v)
  case Branch(l, r) => branchFn(fold(l)(leafFn)(branchFn), fold(r)(leafFn)(branchFn))
}
```

This single function can now be used to:

- Count nodes
- Sum elements
- Find depth
- Map over the tree

---

## Example: Summing Tree Elements

```scala
val tree: Tree[Int] = Branch(Branch(Leaf(1), Leaf(2)), Leaf(3))

val sum = fold(tree)(identity)(_ + _)
// sum: 6
```

By changing the `leafFn` and `branchFn`, we can compute different properties:

### Counting Nodes
```scala
val size = fold(tree)(_ => 1)(_ + _)
// size: 3
```

### Finding Maximum Value
```scala
val max = fold(tree)(identity)(_ max _)
// max: 3
```

---

## Why This Matters

Purely functional libraries encourage this mode of thinking. Instead of managing state and mutable variables, we describe computations as transformations. Libraries like Cats enhance this pattern further with:

- `Foldable` type class
- `Traverse` for effectful computations
- Type-safe abstractions like `Validated`, `Either`, and `IO`

This leads to clearer intent, easier reasoning, and better reuse.

---

## Final Thoughts

Tree folds are just the beginning. Whether you're building interpreters, compilers, or reactive systems, the functional approach to data transformation and abstraction pays off.

> “A little algebra goes a long way.”

In Scala, writing purely functional code is not about avoiding mutation — it’s about embracing compositional thinking. And once you fold a tree functionally, it’s hard to go back.

