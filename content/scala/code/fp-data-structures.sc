import scala.annotation.tailrec
////////////////////////////////////////////////////////
// Functional Lists

sealed trait FunList[+T]
case object Empty extends FunList[Nothing]
case class Cons[+T](head: T, tail: FunList[T]) extends FunList[T]

object FunList {
  def apply[T](xs: T*): FunList[T] =
    if (xs.isEmpty) Empty
    else Cons(xs.head, apply(xs.tail: _*))
}

val xs = Cons(1, Cons(2, Cons(3, Cons(4, Empty))))
val ys = FunList(1,2,3)

def sum(ints: FunList[Int]): Int = ints match {
  case Empty => 0
  case Cons(x,xs) => x + sum(xs)
}

def product(ds: FunList[Double]): Double = ds match {
  case Empty => 1.0
  case Cons(x, xs) => x * product(xs)
}

sum(FunList(1,2,3))
product(FunList(1,2,3))

// Exercise: write funListToString[T](xs: FunList[T]): String

def foldRight[A, B](xs: FunList[A], z: B)(f: (A, B) => B): B =
  xs match {
    case Empty => z
    case Cons(h, t) => f(h, foldRight(t, z)(f))
  }

//foldRight(FunList(1,2,3), 0)(_ + _)
//f(1, foldRight(FunList(2, 3), 0))(f))
//f(1, f(2, foldRight(FunList(3), 0))(f))
//f(1, f(2, f(3, foldRight(Empty, 0))(f)))
//f(1, f(2, f(3, 0)))
//f(1, f(2, 3))
//f(1, 5)
//6

@tailrec
def foldLeft[A, B](xs: FunList[A], z: B)(f: (B, A) => B): B =
xs match {
    case Empty => z
    case Cons(h, t) => foldLeft(t, f(z, h))(f)
  }

foldLeft(FunList(1,2,3), 0)(_ + _)

val curried: ((Int, Int) => Int) => Int = foldLeft(FunList(1, 2, 3), 0)
curried(_ + _)

def foldLeftSum(xs: FunList[Int]) =
  foldLeft(xs, 0)(_ + _)

def foldRightSum(xs: FunList[Int]) =
  foldRight(xs, 0)(_ + _)


foldLeftSum(FunList(1,2,3))

// Exercise: implement foldRightProduct in terms of foldRight


// Question: is foldRight tail-recursive?


// Exercise: implement foldLeft, which is tail-recursive

// Exercise: implement foldLeftSum in terms of foldLeft


////////////////////////////////////////////////////////
// Functional Trees

sealed trait Tree[+T]
final case class Leaf[T](e: T) extends Tree[T]
final case class Node[T](left: Tree[T], right: Tree[T]) extends Tree[T]

def size[T](t: Tree[T]): Int =
  t match {
    case Leaf(_) => 1
    case Node(left, right) => size(left) + size(right)
  }

def treeToString[T](tree: Tree[T]): String =
  tree match {
    case Leaf(e) => e.toString
    case Node(left, right) =>
      treeToString(left) + "," + treeToString(right)
  }

val oneToFour = Node(Node(Leaf(1), Leaf(2)), Node(Leaf(3), Leaf(4)))

size(oneToFour)
treeToString(oneToFour)



// Exercise: write reverseTree[T](tree: Tree[T]): Tree[T],
// which returns a tree with same elements as tree, but in reverse order

// Fun fact: being able to get this right might get you hired by Google
// https://mikulskibartosz.name/reversing-a-binary-tree-and-other-great-interview-questions-22c407c3d197


//def reverseTree[T](tree: Tree[T]): Tree[T] =


////////////////////////////////////////////////////////
// OO Polymorphism versus pattern matching on ADTs
// Comment out one or the other

// OO Polymorphism:

// 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8<
//sealed trait TrafficLight {
//  def next: TrafficLight
//}
//
//case object Red extends TrafficLight {
//  def next: TrafficLight = Green
//}
//
//case object Green extends TrafficLight {
//  def next: TrafficLight = Yellow
//}
//
//case object Yellow extends TrafficLight {
//  def next: TrafficLight = Red
//}
// 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8<

// Pattern matching on ADTs:

// 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8<
sealed trait TrafficLight
case object Red extends TrafficLight
case object Green extends TrafficLight
case object Yellow extends TrafficLight

def next: TrafficLight =
  this match {
    case Red => Green
    case Green => Yellow
    case Yellow => Red
  }


// 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8< 8<
