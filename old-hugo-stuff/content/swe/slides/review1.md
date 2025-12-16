% Exam 1 Review
% Scala


## General Scala

- How do you pronouce Scala?
- The main version of Scala compiles to bytecode for which platform?
- How can you run Scala code?
- What is Scala's primary build tool?
- What is the highest supertype of all Scala objects?
- What is the lowest subtype of all Scala objects?
- What is the difference between `==` and `eq`?
- Which packages are implicitly imported in every Scala source file?

## Values, Variables and Control Structures

- What is the value and type of `s` below?

```Scala
val moritz = 1865
val s = {
  "Max"
  moritz
}
```

- What is the value and type of `result` below?

```Scala
val result = if (true) "blue" else 2
```

- What is the difference between a `val` and a `var`?

## Collections

- Write an expression that gives the number of elements in `xs`.

```Scala
val xs = Set( ... )
```

- Write an expression that creates a `Map` referenced by a `val` named `langs` such that

```Scala
scala> langs("Lisp")
res0: String = John McCarthy

scala> langs("Java")
res1: String = James Gosling

scala> langs("Pascal")
res2: String = Niklaus Wirth

scala> langs("Scala")
res3: String = Martin Odersky
```

- Write a for-comprehension that uses `langs` from the previous question to create a `Seq` of the last names of the values in `langs`, that is, `List(McCarthy, Gosling, Wirth, Odersky)`.

## Functions

- Write a function called `mean` that takes a variable number of `Double` parameters and returns their arithmetic mean (sum divided by number of numbers).

- Given `xs: List[Int]`, write an invocation of the `filter` method on `xs` that passes a function literal which selects only the odd numbers in `xs`.

- Write a function named `listToString[T]` that takes a single `List[T]` and returns a string representation of the `List[T]`.  The `listToString` function should have a single expression which calls a nested helper function which is recursive and uses pattern matching to recursively accumulate a string representation.  Your helper function may use an if statement instead of pattern matching for partial credit.

## Classes and Objects

- Write the minimal Scala definition of a (non-case) class named `Item` which has two fields, `name` of type `String` and `hauptstadt` of type `String`.

- Write an `equals` method for the `Item` class above using the recipe we discussed in class.

- Write a `hashCode` method for the `Item` class above using the recipe we discussed in class.

- Write a companion object for the `Item` class above with a factory method that allows us to create an `Item` object with expression like `Item("Key Lime", 3.14)` (leaving off operator `new`).

## Inheritance

Given the `Person` class below, write the minimal non-final subclass of `Person` named `Employee` that adds a mutable `salary: Double` field and initializes the fields defined in `Person`.

```Scala
class Person(val name: String)
```

## Case Classes and Pattern Matching

- Given the classes below, write a function named `next` which takes a single parameter `fußgängerampel: AmpelMann` and returns the next `AmpelMann` in the `Grün -> Rot -> Grün` cycle.  Your `next` function body should be a single `match` expression.

```Scala
sealed trait AmpelMann
case object Grün extends AmpelMann
case object Rot extends AmpelMann
```

## Algebraic Data Types

- Write minimal traits/classes/case classes such that the following function would compile without warning or error, but if you removed one of the cases it would compile with a "match may not be exhaustive" warning.

```Scala
def hauptstadt(land: Bundesland) = land match {
  case land: Berlin => "Berlin"
  case land: Brandenburg => "Potsdam"
  case land: MecklenburgVolpommern => "Schwerin"
  case land: SachsenAnhalt => "Magdeburg"
  case land: Sachsen => "Dresden"
  case land: SchleswigHolstein => "Kiel"
  case land: FreieHansestadtHamburg => "Hamburg"
  case land: HansestadtBremen => "Bremen"
  case land: Niedersachsen => "Hannover"
  case land: NordrheinWestfalen => "Düsseldorf"
  case land: FreistaatThüringen => "Erfurt"
  case land: Hessen => "Wiesbaden"
  case land: RheinlandPfalz => "Mainz"
  case land: Saarland => "Saarbrücken"
  case land: BadenWürttemberg => "Stuttgart"
  case land: FreistaatBayern => "München"
}
```
