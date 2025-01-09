% Scala Collections

## Scala Collections

![Abstract classes and traits in `scala.collection`](collections-diagram-213.png){height=60%}

From [https://docs.scala-lang.org/overviews/collections-2.13/overview.html](https://docs.scala-lang.org/overviews/collections-2.13/overview.html)

## Immutable Collections

![Immutable collections in `scala.collection.immutable`](collections-immutable-diagram-213.pdf)

## Mutable Collections

![Mutable collections in `scala.collections.mutable`](collections-mutable-diagram-213.pdf)


## Type Aliases in `scala` and `scala.Predef`

`scala.Predef` provides type aliases for commonly used collections, such as `List` (and constructors `::` and `Nil`), `Set`, and `Map`.

`scala` provides type aliases for `IndexedSeq`, `Seq`, `Iterable` (and `Iterator`) and `Vector`.

All of these alias to collections in `scala.collection.immutable`, so these companion object factories create immutable collections:

```Scala
Iterable("x", "y", "z")
List(1, 2, 3)
Vector(1, 2, 3)
Seq(1.0, 2.0)
IndexedSeq(1.0, 2.0)
Set(1, 2, 3)
Map("x" -> 24, "y" -> 25, "z" -> 26)
```

## Collection-like Classes in `scala`

The `scala` package contains collection-like classes which are not part of the collections framework: `Array` and the TupleN classes.

Arrays are mutable fixed-sized Sequences of like-typed elements which map one-to-one with Java arrays, except Scala arrays are generic.

```Scala
val zs: Array[Int] = Array(1, 2, 3)
zs(0) = 42
zs == Array(42, 2, 3)
```

## Tuples

A tuple is an immutable fixed-size collection of values of mixed types.  The `Tuple` companion object factory method creates instances of classes named `Tuple1` through `Tuple22`, so the largest tuple you can create is 22 elements in size.

Tuples are about convenience:

```Scala
val dog = ("Chloe", 6)
dog._1 == "Chloe"
dog._2 == 6
val (name, age) = dog
name == "Chloe"
age == 6
```

Be careful: if you leave off the parenthesis you don't get destructuring bind:

```Scala
val name, age = dog
name == ("Chloe", 6)
age == ("Chloe", 6)
```

## Idiomatic Functional Lists

List construction:

```Scala
val nums: List[Int] = List(1, 2, 3, 4)

val leer = Nil    // Nil is an empty list constant
val vide = List()
```

Lists are homogeneous (elements have same type) and generic. 

- `List` is not a type -- no raw collections in Scala
- `List[T]` is a generic type, or type constructor
- `List[Int]` is a type because an argument for `T` is provided

Due to type inference, these are equivalent:

```Scala
val nums = List(1, 2, 3, 4)
val nums: List[Int] = List[Int](1, 2, 3, 4)
```

## Basic List Operations

Given `xs == List(1,2,3)`,

- `xs.head` returns the first element of a list: `1`
- `xs.tail` returns a list consisting of all elements except the first: `List(2,3)`
- `xs.isEmpty` returns true if the list is empty: `false`

Using these basic operations and functional list idioms, we can implement insertion sort as:

```Scala
def insertionSort(xs: List[Int]): List[Int] =
  if (xs.isEmpty) Nil
  else insert(xs.head, insertionSort(xs.tail))

def insert(x: Int, xs: List[Int]): List[Int] =
  if (xs.isEmpty || x <= xs.head) x :: xs
  else xs.head :: insert(x, xs.tail)
```

## List Patterns

The `List` constructor can be used for a destructuring bind:

```Scala
scala> val List(a, b, c) = List("apples", "bananas", "kiwis")
a: String = apples
b: String = bananas
c: String = kiwis
```

Recall that you can "cons" an element to the head of a list, so the list above could be constructed like:

```Scala
scala> val fruits = "apples"::"bananas"::"kiwis"::Nil
fruits: List[String] = List(apples, bananas, kiwis)
```

## `con`sing Lists

Recall that `::` is a method that associates to the right, that is, it's invoked on its right operand.

```Scala
scala> val head = "apple"
head: String = apple

scala> val tail = List("bananas", "kiwis")
tail: List[String] = List(bananas, kiwis)

scala> head::tail
res0: List[String] = List(apple, bananas, kiwis)

scala> tail.::(head)
res1: List[String] = List(apple, bananas, kiwis)
```

## Pattern Matching on List Structure

Scala allows infix operators like `::` to be used in pattern matches.  So we could rewrite insertion sort as:

```Scala
def insertionSort(xs: List[Int]): List[Int] = xs match {
  case List()   => List()
  case h :: t => insert(h, insertionSort(t))
}
def insert(x: Int, xs: List[Int]): List[Int] = xs match {
  case List()  => List(x)
  case h :: t => if (x <= h) x :: xs else h :: insert(x, t)
}
```

When you read list pattern matching code in functional languages read `h` as "head" and `t` as "tail".

Now let's look at the most general collections operations: those defined on `Iterable`

## Size-related Methods on `Iterable`

- `xs.isEmpty` Tests whether the collection is empty.
- `xs.nonEmpty` Tests whether the collection contains elements.
- `xs.size` The number of elements in the collection.
- `xs.knownSize` The number of elements, if this one takes constant time to compute, otherwise -1.
- `xs.sizeCompare(ys)` Returns a negative value if xs is shorter than the ys collection, a positive value if it is longer, and 0 if they have the same size. Works even if the collection is infinite, for example LazyList.from(1) sizeCompare List(1, 2) returns a positive value.
- `xs.sizeCompare(n)` Returns a negative value if xs is shorter than n, a positive value if it is longer, and 0 if it is of size n. Works even if the collection is infinite, for example LazyList.from(1) sizeCompare 42 returns a positive value.
- `xs.sizeIs < 42`, `xs.sizeIs != 42`, etc. Provides a more convenient syntax for xs.sizeCompare(42) < 0, xs.sizeCompare(42) != 0, etc., respectively.

## Element Retrieval Methods on `Iterable`  

- `xs.head` The first element of the collection (or, some element, if no order is defined).
- `xs.headOption` The first element of xs in an option value, or None if xs is empty.
- `xs.last` The last element of the collection (or, some element, if no order is defined).
- `xs.lastOption` The last element of xs in an option value, or None if xs is empty.

## Subcollection Methods on `Iterable` 

- `xs.tail` The rest of the collection except xs.head.
- `xs.init` The rest of the collection except xs.last.
- `xs.slice(from, to)` A collection consisting of elements in some index range of xs (from from up to, and excluding to).
- `xs take n` A collection consisting of the first n elements of xs (or, some arbitrary n elements, if no order is defined).
- `xs drop n` The rest of the collection except xs take n.
- `xs takeWhile p` The longest prefix of elements in the collection that all satisfy p.
- `xs dropWhile p` The collection without the longest prefix of elements that all satisfy p.
- `xs takeRight n` A collection consisting of the last n elements of xs (or, some arbitrary n elements, if no order is defined).
- `xs dropRight n` The rest of the collection except xs takeRight n.
- `xs filter p` The collection consisting of those elements of xs that satisfy the predicate p.
- `xs withFilter p` A non-strict filter of this collection. Subsequent calls to map, flatMap, foreach, and withFilter will only apply to those elements of xs for which the condition p is true.
- `xs filterNot p` The collection consisting of those elements of xs that do not satisfy the predicate p.

## Mapping Methods on `Iterable`

- `xs map f` The collection obtained from applying the function f to every element in xs.
- `xs flatMap f` The collection obtained from applying the collection-valued function f to every element in xs and concatenating the results.
- `xs collect f` The collection obtained from applying the partial function f to every element in xs for which it is defined and collecting the results.

## Folding Methods on `Iterable`

- `xs.foldLeft(z)(op)` Apply binary operation op between successive elements of xs, going left to right and starting with z.
- `xs.foldRight(z)(op)` Apply binary operation op between successive elements of xs, going right to left and ending with z.
- `xs reduceLeft op` Apply binary operation op between successive elements of non-empty collection xs, going left to right.
- `xs reduceRight op` Apply binary operation op between successive elements of non-empty collection xs, going right to left.

Convenience Folds

- `xs.sum` The sum of the numeric element values of collection xs.
- `xs.product` The product of the numeric element values of collection xs.
- `xs.min` The minimum of the ordered element values of collection xs.
- `xs.max` The maximum of the ordered element values of collection xs.
- `xs.minOption` Like min but returns None if xs is empty.
- `xs.maxOption` Like max but returns None if xs is empty.

## Zipping Methods on `Iterable`

- `xs zip ys` A collection of pairs of corresponding elements from xs and ys.
- `xs.zipAll(ys, x, y)` A collection of pairs of corresponding elements from xs and ys, where the shorter sequence is extended to match the longer one by appending elements x or y.
- `xs.zipWithIndex` An collection of pairs of elements from xs with their indices.

## Conversion Methods on `Iterable`

- `xs.toArray` Converts the collection to an array.
- `xs.toList` Converts the collection to a list.
- `xs.toIterable` Converts the collection to an iterable.
- `xs.toSeq` Converts the collection to a sequence.
- `xs.toIndexedSeq` Converts the collection to an indexed sequence.
- `xs.toSet` Converts the collection to a set.
- `xs.toMap` Converts the collection of key/value pairs to a map. If the collection does not have pairs as elements, calling this operation results in a static type error.
- `xs.to(SortedSet)` Generic conversion operation that takes a collection factory as parameter.


## Sets and Maps

Sets are immutable by default, so we "add" to them with reassignment

```Scala
var trooperSet = Set("Thorny", "Farva", "Mac", "Mac")
trooperSet == Set("Thorny", "Farva", "Mac")
trooperSet += "Rabbit"
trooperSet.contains("Rabbit")
```

Map elements created with 2-tuples, which are usually created with `->`

```Scala
var majors = Map(
  ("CS", "Computer Science"),
  "CM" -> "Computational Media",
  "EE" -> "Electrical Engineering"
)
majors += "IE" -> "Industrial Engineering"
majors("IE")
majors.getOrElse("AA", "Unknown Major")
```

`->` uses implicit conversion to create `Tuple2` instances.

