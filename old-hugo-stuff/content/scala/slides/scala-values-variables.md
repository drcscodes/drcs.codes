% Scala Values and Variables

## Values and Variables

- Like Java, every Scala variable has a name and a type
- Variable definitions start with `var` or `val`.  
    - `var`s are reassignable
    - `val`s like Java's `final`

```Scala
var x: Int  = 1
x = 2

val y = 3.14  // Type is Double, inferred by literal
y = 6.28 // Won't compile -- y is a val
```

## Basic Types

Same basic types as Java, but different names:

- Byte, Short, Int, Long, Char
- String
- Float
- Double
- Boolean

Literals same as in Java

## Blocks

Blocks are enclosed in curly braces.  Last expression gives value of the block.

```Scala
val s = {
  1 
  2 
  "buckle my shoe"
}
```

Value of `s` above is `"buckle my shoe"`

## Basic Operators

- Basic arithmetic, logical, relational and bitwise operators like Java's
- All operators are actually methods (more later)
- Precedence based on first character of operator:
    -  (all other special characters) then *,/,% then +,- then : then =,! then <,> then & then ˆ then | then (all letters) then (all assignment operators) 

- Associativity based on last character of operator
    - Operators ending in : invoked on right operand
    - All others invoked on left operand
    
## Object Equality

- All objects have equals methods, just like Java but the equality operators are different
    - `==` same as equals method
    - `eq` is alias testing operator

- We'll discuss implementation of equals and hashCode in a future lecture.

## Basic Sequences

Lists are immutable Sequences of  like-typed elements

```Scala
val xs: List[Int] = List(1, 2, 3)
xs(0) = 42 // Won't compile

// Add elements to head of list with cons operator, ::
val ys = 0::xs
ys == List(0, 1, 2, 3)

// Cons returns a new list
xs != ys

// To "modify" xs, reassign (only works if xs is a var)
xs = 0::xs
```

Arrays are mutable fixed-sized Sequences of  like-typed elements

```Scala
val zs: Array[Int] = Array(1, 2, 3)
zs(0) = 42
zs == Array(42, 2, 3)
```

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

## Conclusion

- In Scala, every value is an object, that is, an instance of a class.
    - Scala compiler makes basic types as efficient as in Java while providing the elegance of the uniform "everything is an object" abstraction

- Scala is statically typed but performs type inference to make simple REPL interactions or scripts as convenient as dynamically-typed langauges like Python

