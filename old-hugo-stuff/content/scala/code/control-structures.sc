// if is an expression in Scala
val first = true
val result = if (!first) "last" else "shake and bake!"

// Recalling how type inference works, what's the type of cal?
val cal = if (true) "magic man" else 42

// while is also an expression
val enough = 3
var i = 1 // has to be a var becuase
val useless = while (i < enough) {
  i += 1
  i
}
// useless has the value (), which is the only value of type Unit.
// The Unit type is analogous to void in Java.

// to is a method on Int which creates a Range.Inclusive object
val forUseless = for (i <- 1 to 5) {
  val dub = i * 2
  println(dub)
}

val dub = "step"
// Filter with an if expression
for (i <- 1 to 10 if i % 2 == 0) {
  // Notice that this dub shadows the dub above
  val dub = i * 2
  println(dub)
}

val doubles = for (i <- 1 to 5) yield {
  val dub = i * 2
  dub
}

val units = for (i <- 1 to 5) yield {
  val dub = i * 2
  println(dub)
}


val love = "sacrifice"
val swipe = love match {
  case "right" => "lame"
  case "boat" => "das"
  case "bug" => "herbie"
  case "dr" => "Gene Simmons"
  case _ => 3
}
// Which type is inferred for swipe?
// What if you change the value of love to match one of the cases?

// Exceptions work similarly to Java, but syntax for catch clause is like
// Scala's match expression.
// Pay attention to
// - the order in which the value of whatKind is echoed vs the println in the finally block
// - the value of whatKind -- is it the value from the catch block or the finally?
val whatKind = try {
  throw new RuntimeException
} catch {
  case e: RuntimeException => "it was a RuntimeException"
  case e: Exception => "it was an Exception"
} finally {
  println("And we gotta ensure resources are closed after unwinding the stack")
  // The value of a finally block is discarded
  "lost"
}

var j = 0
do {
  println(j)
  j += 1
} while (j < 5)
