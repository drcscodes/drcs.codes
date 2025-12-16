% Scala Function Basics

## Basic Function Definition

![Scala Basic Function Definition, Programming in Scala, 3ed, page 69](scala-basic-function-definition.png)


## Functions Return Values

Notice the mandatory = between the "header" and "body" 

```Scala
def double(x: Int): Int = 2 * x
```

- Also notice that you don't need {} if body is single expression

A function that doesn't return a useful value is called a procedure and returns the special value () of type Unit. Style guide says always annotate return type of procedures

```Scala
def say(something: String): Unit = {
  println(something)
}
```

## Local Functions

You can nest functions within functions. Here iter can only be called within facIter

```Scala
def facIter(n: BigInt): BigInt = {
  def iter(i: BigInt, accum: BigInt): BigInt = {
    if (i <= 1) accum
    else iter(i - 1, i * accum) }
  require(n >= 0,
      "Factorial only defined for non-negative integers")
  iter(n, 1)
}
```

`require` takes a `Boolean` expression and an optional `String` description. If `Boolean` expression is `false`, throws an `IllegalArgumentException` with the description as the exception message

## Functions are First Class


First class values in a programming language can be

- stored in variables
- passed as arguments to functions, and 
- returned from functions

## Function Literals

Just as other types have literal values, function values can be created with literals

```Scala
val doubleFun: Int => Int = {(x: Int) => {2 * x}}
```

- Notice the type annotation. `doubleFun` is a function with a domain of `Int` and codomain of `Int`

Above is full literal notation. What can be inferred can be left off. Could be written as

```Scala
val doubleFun:Int => Int = x => 2 * x
```
or
```Scala
val doubleFun = (x: Int) => 2 * x
```

## Higher-Order Functions

- A first order function takes non-function value parameters and returns a non-function value
- A higher-order function takes function value parameters or returns a function value
- Function literals are most useful as arguments to higher-order functions `List.filter` takes a function of one parameter of the list's element type and returns a `Boolean`

```Scala
val evens = List(1,2,3,4,5,6,7,8).filter(x => x % 2 == 0)
```

If each parameter appears once in the function literal's body, can use placeholder syntax

```Scala
val evens2 = List(1,2,3,4,5,6,7,8).filter(_ % 2 == 0)
```

## Repeated Parameters

Repeated parameters, or "var-args" parameters, are annotated with a * after the type

```Scala
def max(x: Int, xs: Int*): Int = { xs.foldLeft(x)((x, y) => if (x > y) x else y)
}
```

Must pass a multiple single arguments to a repeated parameter

```Scala
val varArgsMax = max(3, 5, 7, 1)
```

- In application of `max` above, `x` is `3`, `xs` is `Array(5, 7, 1)`

To pass a sequence to a varargs parameter, use `: _*`

```Scala
val seqMax = max(0, List(2, 4, 6, 8, 0): _*)
```

## Functional Function Evaluation

The result of a pure function depends only on its inputs

A pure function is referentially transparent, i.e., a function application can be replaced with the value it produces without changing the meaning of the program

Application of pure functions to their arguments can be understood with the substitution model of evaluation:

1. Evaluate arguments left to right
2. Replace function call with function body, substituting arguments for parameters in body

## Recursive Function Evaluation

```Scala
def fac(n: Int): Int = if (n <= 1) 1 else n * fac(n - 1)
```

Applying the steps of applicative-order evaluation gives:

[5/n]fac(n) ($[v_1/p_1, ...v_n/p_n]expr$ means substitute $v_i$ for $p_i$ in $expr$)

- => fac(5)
- => 5 * fac(4)
- => 5 * 4 * fac(3)
- => 5 * 4 * 3 * fac(2)
- => 5 * 4 * 3 * 2 * fac(1)
- => 5 * 4 * 3 * 2 * 1
- => 5 * 4 * 3 * 2
- => 5 * 4 * 6
- => 5 * 24
- => 120

Notice the expanding-contracting pattern. This mirrors stack usage -- calling `fac` with a large argument will overflow the stack

## Iterative Recursive Functions Evaluation

Recursive calls in tail position are turned into loops (only one stack frame is used). This is called tail call optimization

`facIter` uses an iterative local function whose recursive call is in tail position

```Scala
def facIter(n: BigInt): BigInt = {
  def iter(i: BigInt, accum: BigInt): BigInt =
    if (i <= 1) accum
    else iter(i - 1, i * accum)
  iter(n, 1)
}
```

## Iterative Recursive Functions Evaluation

```Scala
def facIter(n: BigInt): BigInt = {
  def iter(i: BigInt, accum: BigInt): BigInt =
    if (i <= 1) accum
    else iter(i - 1, i * accum)
  iter(n, 1)
}
```

[5/n]facIter(n)

- => iter(5, 1)

[5/i, 1/accum]iter(i, accum)

- => iter(5, 1)
- => iter(4, 5)
- => iter(3, 20)
- => iter(2, 60)
- => iter(1, 120)
- => 120

% Scala Functional Abstraction

## Functional Lists

Scala's list type has an API familiar to Java programmers, and an API modeled on the original cons list in Lisp, which is an elegant representation of linked lists.  Recall that one way to create a list in Scala is to use the `::` operator (pronounced "cons"):

```Scala
scala> var xs = 1::Nil
xs: List[Int] = List(1)

scala> xs = 2::xs
xs: List[Int] = List(2, 1)

scala> xs = 3::xs
xs: List[Int] = List(3, 2, 1)
```
Notice that you add elements to the head of the list.  The special value `Nil` represents an empty node which signals the end of the list, which you can also think of as a list with no elements because it contains on value and doesn't point to a successor node.

## Linked List Structure

The code on the previous slide produces a list that looks like:

```{.graphviz .center caption="A singly-linked list."}
digraph foo {
        rankdir=LR;
        node [shape=record];
        a [label="{ <data> 3 | <ref>  }"]
        b [label="{ <data> 2 | <ref>  }"];
        c [label="{ <data> 1 | <ref>  }"];
        Nil [shape=box];
        a:ref:c -> b:data [arrowhead=vee, arrowtail=dot, dir=both, tailclip=false];
        b:ref:c -> c:data [arrowhead=vee, arrowtail=dot, dir=both, tailclip=false];
        c:ref:c -> Nil      [arrowhead=vee, arrowtail=dot, dir=both, tailclip=false];
}
```

Each node is a cons cell that contains an element, and a link to the rest of the list.  The `head` and `tail` methods return these two components of the first cons cell in the list.

```Scala
scala> xs.head
res2: Int = 3

scala> xs.tail
res3: List[Int] = List(2, 1)
```

## The End of the List

- `isEmpty` is equivalent to comparison to `Nil`.

```Scala
scala> val leer = List()
leer: List[Nothing] = List()

scala> leer.isEmpty
res4: Boolean = true

scala> leer == Nil
res5: Boolean = true
```

## Functional List Idioms

A common functional idiom for processing a List uses only 

- the three primary first-order methods `head`, `tail`, and `isEmpty`
- `if` expressions, and
- recursion

Here's a function to generate a `String` representation of a list:

```Scala
def listToString[T](list: List[T]): String = {
  def toStringHelper(list: List[T], accum: String): String =
    // Nil is the end of a list, base case for recursion
    if (list == Nil) accum
    // Recurse on the tail of the list, accumulate result
    else toStringHelper(list.tail, accum + list.head)
  toStringHelper(list, "")
}
```

As an exercise, use the substitution model to evaluate `listToString(List("R", "E", "S", "P", "E", "C", "T"))` with pencil and paper.

