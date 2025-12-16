class Rational(n: Int, d: Int) {
  require(d != 0, "Denominator can't be negative")

  private val g = gcd(n, d)
  val numer: Int = n / g
  val denom: Int = d / g

  override def toString = s"$numer/$denom"

  // Operator method
  def +(other: Rational) =
    new Rational(
      this.numer * other.denom + other.numer * this.denom,
      this.denom * other.denom
    )

  private def gcd(a: Int, b: Int): Int =
      if (b == 0) a else gcd(b, a % b)
}

// Implicit conversions

object Rational {
  implicit def int2Rational(i: Int) = new Rational(i, 1)
}

val oneHalf = new Rational(1, 2)

oneHalf + 1

1 + oneHalf

case class Rectangle(width: Int, height: Int)

implicit class RectangleMaker(width: Int) {
  def x(height: Int) = Rectangle(width, height)
}

val myRectangle: Rectangle = 3 x 4

// Implicit parameters

case class Delimiters(left: String, right: String)

def quote(what: String)(implicit delims: Delimiters) =
  delims.left + what + delims.right

object FrenchPunctuation {
  implicit val quoteDelimiters = Delimiters("«", "»")
}

import FrenchPunctuation.quoteDelimiters

quote("Bonjour le monde")

// Context bounds

def smaller[T](a: T, b: T)(implicit ordering: Ordering[T]) =
  if (ordering.lt(a, b)) a else b

def smaller2[T](a: T, b: T)(implicit ordering: Ordering[T]) =
  if (implicitly[Ordering[T]].lt(a, b)) a else b

def smaller3[T: Ordering](a: T, b: T) =
  if (implicitly[Ordering[T]].lt(a, b)) a else b

def smaller4[T](a: T, b: T)(implicit ordering: Ordering[T]) = {
  import ordering.mkOrderingOps
  if (a < b) a else b
}


