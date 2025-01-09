sealed trait MyList[+T]
case object Empty extends MyList[Nothing]
case class Cons[+T](head: T, tail: MyList[T]) extends MyList[T]

