class Rational1(n: Int, d: Int) {

  require(d != 0, "Denominator can't be negative")

  def numer: Int = n

  def denom: Int = d
}

// n and d are constructor parameters.
// Think of the body of the class as the body of its
// primary constructor.

// n and d are in scope in the constructor,
// but they are not fields.

// The n and d in the bodies of the methods
// numer and denom are caputured as constants.

val r11 = new Rational1(1, 2)

val r12 = new Rational1(1, 0)

// Methods work as expected
print("r1 == " + r1.numer + "/" + r1.denom)

// Constructor parameters are not fields,
// they die after constructor finishes
//print("r1 == " + r1.n + "/" + r1.d)

// Overriding
// val fields
class Rational2(n: Int, d: Int) {

  require(d != 0, "Denominator can't be negative")

  val numer: Int = n
  val denom: Int = d

  // override is a keyword in Scala, and is required
  // when overriding a method.
  override def toString = s"$numer/$denom"
}

val r2 = new Rational2(3, 4)

// Self references
class Rational3(n: Int, d: Int) {
  require(d != 0, "Denominator can't be negative")

  val numer: Int = n
  val denom: Int = d

  // override is a keyword in Scala, and is required
  // when overriding a method.
  override def toString = s"$numer/$denom"

  def add(other: Rational3) =
    new Rational3(
      this.numer * other.denom + other.numer * this.denom,
      this.denom * other.denom
    )
}

val r3Half = new Rational3(1, 2)
val r3Quarter = new Rational3(1, 4)
val r3ThreeQuarters = r3Half.add(r3Quarter)

// private members
class Rational4(n: Int, d: Int) {
  require(d != 0, "Denominator can't be negative")

  // Normalize fractions
  val numer: Int = n / gcd(n, d)
  val denom: Int = d / gcd(n, d)

  // override is a keyword in Scala, and is required
  // when overriding a method.
  override def toString = s"$numer/$denom"

  def add(other: Rational4) =
    new Rational4(
      this.numer * other.denom + other.numer * this.denom,
      this.denom * other.denom
    )

  private def gcd(a: Int, b: Int): Int =
      if (b == 0) a else gcd(b, a % b)
}

val r4Half = new Rational4(1, 2)
val r4Quarter = new Rational4(1, 4)
val r4ThreeQuarters = r4Half.add(r4Quarter)

// Operators
class Rational5(n: Int, d: Int) {
  require(d != 0, "Denominator can't be negative")

  // Slightly more efficient to compute gcd only once
  private val g = gcd(n, d)
  val numer: Int = n / g
  val denom: Int = d / g

  // override is a keyword in Scala, and is required
  // when overriding a method.
  override def toString = s"$numer/$denom"

  // Operator method
  def +(other: Rational5) =
    new Rational5(
      this.numer * other.denom + other.numer * this.denom,
      this.denom * other.denom
    )

  private def gcd(a: Int, b: Int): Int =
      if (b == 0) a else gcd(b, a % b)
}

val r5Half = new Rational5(1, 2)
val r5Quarter = new Rational5(1, 4)

// Infix method call notation makes method call look
// like operator
val r5ThreeQuarters = r5Half + r5Quarter

class Vec(val xs: Double*) {
  def *(scalar: Double): Vec = new Vec(xs.map(_ * scalar):_*)

  def dot(other: Vec): Double = {
    require(this.xs.length == other.xs.length, "vecs must be same size")
    xs.zip(other.xs).map({ case (x, y) => x * y }).sum
  }

  override def toString: String = "Vec(" + xs.mkString(",") + ")"

}

val v1 = new Vec(1, 3, 5)
val v2 = new Vec(2, 4, 6)
v1 * 2
v1 dot v2





























// Length Classes

trait Length {
  def feet: Int
  def inches: Int
  def totalInches: Int
  def +(other: Length): Length
  def -(other: Length): Length
  def *(other: Length): Length
  def /(other: Length): Length
}

class SquareFeet(side1: Length, side2: Length) {
  val squareInches = side1.totalInches * side2.totalInches

  val feet = squareInches / 144.0

  override def toString: String =
    s"<$feet square feet ($squareInches square inches)>"
}

object SquareFeet {
  def apply(side1: Length, side2: Length) = new SquareFeet(side1, side2)
}

object Length {

  private class LengthImpl(val totalInches: Int) extends Length {

    val feet = totalInches / 12

    val inches = totalInches - (feet * 12)

    override def toString: String =
      s"<$feet feet, $inches inches ($totalInches total inches)>"

    def +(other: Length) = new LengthImpl(other.totalInches + this.totalInches)

    def -(other: Length) = new LengthImpl(this.totalInches - other.totalInches)

    def *(other: Length) =
      new LengthImpl((other.totalInches * this.totalInches) / 144)

    def /(other: Length) = new LengthImpl(other.totalInches / this.totalInches)
  }

  def apply(feet: Int, inches: Int): Length = new LengthImpl((feet * 12) + inches)

  def apply(totalInches: Int): Length = new LengthImpl(totalInches)
}

val front = Length(38, 9)
val side = Length(22, 0) + Length(5, 10) + Length(4, 9)
val squareFeet = SquareFeet(front, side)

val vent1 = SquareFeet(Length(16), Length(8))

val crawlToMainFloor = Length(3, 9)
val crawlToGrade = Length(2, 3)

crawlToMainFloor - crawlToGrade
