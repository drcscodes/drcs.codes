import java.io.{File, PrintWriter}

import scala.annotation.tailrec

// Functional list processing idiom:
// - Nil (aka list.isEmpty) is base case
// - recurse on list.tail
// - accumulate final result in recursive call
def listToString[T](list: List[T]): String = {
  @tailrec
  def loop(list: List[T], accum: String): String =
    // Nil is the end of a list, so it's a natural base case for recursion
    if (list == Nil) accum
    // Recurse on the tail of the list, build up the accumulator
    else loop(list.tail, accum + list.head)
  loop(list, "")
}

val aretha = listToString(List("R", "E", "S", "P", "E", "C", "T"))

def dubbel(x: String): String = s"two ${x}s"

// This wouldn't compile because dubbel is a method defined with def,
// not an object (i.e., value)
// val wontCompile = dubbel

// To turn the dubbel method in to a Function value, partially apply it
val dubbelFun = dubbel _

val waffle = (x: String) => s"Mmm, $x"

// This is fine because waffle is a function value
val trippel = waffle


// Type of chocolate is a function takign an Int and returning an Int
def belgian(chocolate: String => String, stuff: String): String = {
  s"I want ${chocolate(stuff)}"
}

// Must call belgian with a value
belgian(waffle, "cone")
belgian(trippel, "crown")

// To call belgian with dubbel, must partially apply it to "lift" it
// to a function value

belgian(dubbel _, "mint gum")

// Three equivalent ways of passing a function value
List("Honey", "Boo", "Boo").foreach(x => print(x))
List("Honey", "Boo", "Boo").foreach(print _)
List("Honey", "Boo", "Boo").foreach(print)

// Short-form of fn literal using placeholder syntax:
List("Honey", "Boo", "Boo").foreach(print(_))


def makeDecorator(
    leftBrace: String,
    rightBrace: String): String => String =
  (middle: String) => leftBrace + middle + rightBrace

val squareBracketer: String => String = makeDecorator("[", "]")

squareBracketer("Malcolm")



// Scala syntax for curried functions: multiple param lists
def curry(chicken: String)(howard: String): String =
  s"Love that $chicken from $howard!"

// Above is equivalent to:
def explicitCurry(chicken: String): String => String =
 (howard: String) => s"Love that $chicken from $howard!"

curry("safety")("static types")
explicitCurry("elegance")("isomorphism")

// You can partially apply second parameter list to get
// another function
val eleganceFrom = curry("elegence")_
eleganceFrom("provability")

// Using curried functions for control abstraction

def withPrintWriter(file: File, op: PrintWriter => Unit) = {
  val writer = new PrintWriter(file)
  try {
    op(writer)
  } finally {
    writer.close()
  }
}

withPrintWriter(
  new File("date.txt"),
  writer => writer.println(new java.util.Date)
)


def withPrintWriter(file: File)(op: PrintWriter => Unit) = {
  val writer = new PrintWriter(file)
  try {
    op(writer)
  } finally {
    writer.close()
  }
}

withPrintWriter(new File("date.txt")) { writer =>
  writer.println(new java.util.Date)
}

val assertionsEnabled = true

def myAssert(predicate: () => Boolean) =
   if (assertionsEnabled && !predicate())
    throw new AssertionError

def byNameAssert(predicate: => Boolean) =
  if (assertionsEnabled && !predicate)
    throw new AssertionError



// Abstraction with higher-order functions

def sumInts(a: Int, b: Int): Int = {
  if (a > b) 0
  else a + sumInts(a + 1, b)
}

def sumSquares(a: Int, b: Int): Int = {
  if (a > 0) 0
  else (a * a) + sumSquares(a + 1, b)
}

