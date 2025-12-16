sealed abstract class Expr
case class Var(name: String) extends Expr
case class Number(num: Double) extends Expr
case class UnOp(operator: String, arg: Expr) extends Expr
case class BinOp(operator: String, left: Expr, right: Expr) extends Expr

val x = Var("x")
x.name
x == Var("x")
x != Var("y")
x.hashCode == Var("x").hashCode
val plus = BinOp("+", x, Var("y"))
val minus = plus.copy(operator = "-")
minus == BinOp("-", x, Var("y"))

def describe(e: Expr): String = e match {
  case Number(_) => "a number"
  case Var(_)    => "a variable"
}

describe(Var("x"))
// This would cause a MatchError, since describe doesn't have
// a case for BinOp
//describe(BinOp("+", Var("x"), Number(1)))


def simplifyTop(expr: Expr): Expr = expr match {
  case UnOp("-", UnOp("-", e))  => e   // Double negation
  case BinOp("+", e, Number(0)) => e   // Adding zero
  case BinOp("*", e, Number(1)) => e   // Multiplying by one
  case _ => expr
}



val doubleNegX = simplifyTop(UnOp("-", UnOp("-", x)))
x == doubleNegX

def describe(x: Any) = x match {
  case 5 => "five"
  case true => "truth"
  case "hello" => "hi!"
  case Nil => "the empty list"
  case _ => "something else"
}
describe(5)
describe(true)
describe("hello")
describe(Nil)
describe(List(1,2,3))

import math.{E, Pi}

val res = E match {
  case Pi => "strange math? Pi = " + Pi
  case _ => "OK"
}
res == "OK"

val pi = math.Pi
val strange = E match {
  case pi => "E is " + pi
}
strange.substring(0,10) == "E is 2.718"

val xs = List(0,2,4)

val two = xs match {
  case List(0, e, _) => e
  case _ => null
}
two == 2

def tupleDemo(expr: Any) = expr match {
  case (a, b, c) => "matched " + a + b + c
  case _ =>
}
val threeTuple = tupleDemo(("ein ", 3, "-Tupel"))
val nichts = tupleDemo((2, "-Tupel"))

def generalSize(x: Any) = x match {
  case s: String => s.length
  case m: Map[_, _] => m.size
  case _ => -1
}
generalSize("abc")
generalSize(Map(1 -> 'a', 2 -> 'b'))
generalSize(math.Pi)

def arrayTest(a: Any) = a match {
  case ints: Array[Int] => "ints"
  case strs: Array[String] => "strs"
  case _ =>
}

arrayTest(Array(1,2,3))
arrayTest(Array("a","b","c"))

sealed trait Feline
final case class Lion() extends Feline
final case class Tiger() extends Feline
final case class Liger() extends Feline
final case class Cat() extends Feline

def react(feline: Feline) = feline match {
  case feline: Lion => "Run!"
  case feline: Tiger => "Run!"
  case feline: Liger => "Magic!"
  case feline: Cat => "Pet"
}

sealed trait TrafficLight
case object Red extends TrafficLight
case object Green extends TrafficLight
case object Yellow extends TrafficLight

def next(light: TrafficLight) = light match {
  case Red => Green
  case Green => Yellow
  case Yellow => Red
}

