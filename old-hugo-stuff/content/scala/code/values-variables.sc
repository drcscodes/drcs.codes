// Literals and basic types as in Java, but with different names.

// Variable definitions introducted with var or val
// A var is reassignable.  Note type annotation syntax.
var x: Int  = 1
x = 2

// A val is not reassignable, like a final variable in Java.
// Note type inference -- no type annotation, but still static type
val y = 3.14  // Type is Double, inferred by literal

// This would not compile if uncommented because y is a val:
//y = 6.28


// Blocks are sequences of expressions enclosed in {}.
// Last expression is value of the block.
// Also notice the static lexical scoping --
// the y inside the block shadows the y above
val s = {
  val y = 1  //
  y == 1 // These two lines will generate a warning that they are pure expressions
//  2      // in statement position, i.e., they don't produce the value of the block.
  "buckle my shoe"
}


// What's the type and value of y at this point?
val areSame: Boolean = x == y

val favorite = "Tame Impala"

// Triple-quoted String.  stripMargin method removes leading spaces before |
val letItHappen =
  """All this running around
    |Trying to cover my shadow
    |A notion growing inside
    |Now all the others seem shallow
    |All this running around
    |Bearing down on my shoulders
    |I can hear an alarm
    |It must be morning""".stripMargin


val music = s"Play my favorite band, $favorite"
val fave = s"Is my favorite band Tame Impala? Result: ${favorite == "Tame Impala"}"

// List is an immutable Seq
var xs: List[Int] = List(1, 2, 3)
// xs(0) = 42 // Won't compile

// Add elements to head of list with cons operator, ::
val ys = 0::xs
ys == List(0, 1, 2, 3)

// Cons returns a new list
xs != ys

// To "modify" xs, reassign to xs (only works if xs is a var)
xs = 0::xs


// Array is a fixed-size mutable Seq
val zs: Array[Int] = Array(1, 2, 3)
zs(0) = 42
zs == Array(42, 2, 3)

var trooperSet = Set("Thorny", "Farva", "Mac", "Mac")
trooperSet == Set("Thorny", "Farva", "Mac")
trooperSet += "Rabbit"
trooperSet.contains("Rabbit")

var majors = Map(
  ("CS", "Computer Science"),
  "CM" -> "Computational Media",
  "EE" -> "Electrical Engineering"
)
majors += "IE" -> "Industrial Engineering"
majors("IE")
majors.getOrElse("AA", "Unknown Major")

val langs = Map(
  "Lisp" -> "John McCarthy",
  "Java" -> "James Gosling",
  "Pascal" -> "Niklaus Wirth",
  "Scala" -> "Martin Odersky"
)

for ((k, v) <- langs) yield v.split(" ")(1)
