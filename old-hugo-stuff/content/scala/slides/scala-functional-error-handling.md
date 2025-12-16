% Functional Error Handling

## What's right with exceptions?

Exceptions provide

- a way to consolidate error handling code and separate it from main logic, and
- an alternative to APIs that require callers of functions to know error codes, sentinal values, or calling protocols.

We can preserve both of these advantages while avoiding the disadvantages of exceptions.

## What's wrong with exceptions?

Exceptions

- break referential transparency,
- are not type-safe, and
- functions that throw excpetions are *partial*.

Also, exception syntax is a pain.

## Exceptions break referential transparency.

```Scala
def failingFn(i: Int): Int = {
  val y: Int = throw new Exception("fail!")
  try {
    val x = 42 + 5
    x + y
  } catch {
    case e: Exception => 43
  }
}
```

If `y` were referentially transparent, then we should be able to substitute the value it references:

```Scala
def failingFn2(i: Int): Int = {
  try {
    val x = 42 + 5
    x + ((throw new Exception("fail!")): Int)
  } catch {
    case e: Exception => 43
  }
}
```

But `failingFn2` returns a different result for the same input.

## Type-safety and Partiality

```Scala
def mean(xs: Seq[Double]): Double =
  if (xs.isEmpty)
    throw new ArithmeticException("mean of empty list undefined")
  else
    xs.sum / xs.length
```

`mean(Seq(1,2,3))` returns a value, but `mean(Seq())` throws an exception

- The type of the function, `Seq[Double] => Double`, does not convey the fact that an exception is thrown in some cases.
- `mean` is not defined for all values of `Seq[Double]`.

In practice, partiality is common, so we need a way to deal with it.

## Functional Error Handling in the Scala Standard Library

The Scala standard library defines three useful algebraic data types for dealing with errors:

- `Option`, which represents a value that may be absent,
- `Either`, which represents two mutually-exclusive alternatives, and
- `Try`, which represents success and failure

Note: Chapter 4 of [Functional Programming in Scala](https://www.manning.com/books/functional-programming-in-scala) defines its own parallel versions of `Option` and `Either`, but we'll use the standard library versions. For a deeper understanding do the exercises in the book.

## The `Option` Type

We've seen `Option` before:

```Scala
sealed abstract class Option[+A]
final case class Some[+A](value: A) extends Option[A]
case object None extends Option[Nothing]
```

Using `Option`, `mean` becomes

```Scala
def mean(xs: Seq[Double]): Option[Double] =
  if (xs.isEmpty) None
  else Some(xs.sum / xs.length)
```

## `Option`'s Definition

`Option` defines many methods that mirror methods on [`Traversable`](https://www.scala-lang.org/api/2.12.8/scala/collection/Traversable.html)s.

```Scala
sealed abstract class Option[+A] {
  def isEmpty: Boolean
  def get: A
  
  final def getOrElse[B >: A](default: => B): B =
    if (isEmpty) default else this.get
  
  final def map[B](f: A => B): Option[B] =
    if (isEmpty) None else Some(f(this.get))
  
  final def flatMap[B](f: A => Option[B]): Option[B] =
    if (isEmpty) None else f(this.get)
  
  final def filter(p: A => Boolean): Option[A] =
    if (isEmpty || p(this.get)) this else None
}
```

The key consequence is that you can treat `Option` as a collection, leading to Scala's idioms for handling optional values.

## `Option` Examples

```Scala
case class Employee(name: String, department: String)

def lookupByName(name: String): Option[Employee] = // ... 

val joeDepartment: Option[String] = lookupByName("Joe").map(_.department)
```

![](fpis-4.3.1-option-examples.png){height=65%}

## `Option` Idioms

```Scala
case class Employee(name: String, department: String)

def lookupByName(name: String): Option[Employee] = // ... 

val joeDepartment: Option[String] = lookupByName("Joe").map(_.department)
```

```Scala
val dept: String = 
  lookupByName("Joe").
  map(_.dept).
  filter(_ != "Accounting").
  getOrElse("Default Dept")
```

The `getOrElse` at the end returns `"Default Dept"` if Joe doesn't have a department, or if Joe's department is not `"Accounting"`.

## Dealing with Exception-Oriented APIs

```Scala
scala> import scala.util.Try
import scala.util.Try

scala> Try { "foo".toInt }
res1: scala.util.Try[Int] = Failure(java.lang.NumberFormatException: For input string: "foo")

scala> Try { "1".toInt }
res2: scala.util.Try[Int] = Success(1)
```

## `Either`s

Return error message on failure:

```Scala
def mean(xs: IndexedSeq[Double]): Either[String, Double] = 
  if (xs.isEmpty)
    Left("mean of empty list!")
  else
    Right(xs.sum / xs.length)
```

Return the exception itself on failure:

```Scala
def safeDiv(x: Int, y: Int): Either[Exception, Int] = 
  try Right(x / y)
  catch { case e: Exception => Left(e) }
```



## Closing Thoughts

Rule of thumb: only throw exceptions exceptions in cases where the program could not recover from the exception by catching it.
