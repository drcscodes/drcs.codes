
class Pair2[T <: Comparable[T]](val first: T, val second: T) {
  def smaller = if (first.compareTo(second) < 0) first else second
}

class Pair3[T : Ordering](val first: T, val second: T) {

  def smaller = if (implicitly[Ordering[T]].lt(first, second)) first else second
}

//class BadCell[-T](init: T) {
//    private[this] var current = init
//    def get = current
//    def set(x: T) = { current = x }
//}

class Person(val name: String)
class Student(name: String, val id: Int) extends Person(name)

class NameLength extends Function1[Person, Int] {
  def apply(p: Person) = p.name.length
}

class GetId extends Function1[Student, Int] {
  def apply(s: Student) = s.id
}

class GetHashCode extends Function1[AnyRef, Int] {
  def apply(o: AnyRef) = o.hashCode
}

// This won't compile due to variance violation
var getter1: Function1[Person, Int] = new GetId

var getter2: Function1[Person, Int] = new GetHashCode

val studentCreator = new Function1[String, Person] {
  def apply(name: String) = new Student(name, 1)
}

import scala.collection.immutable._

class Fruit
class Apple extends Fruit
class Orange extends Fruit

val appleQ1: Queue[Fruit] = Queue(new Apple, new Apple)
val fruitQ1: Queue[Fruit] = appleQ1.enqueue(new Orange)

val appleQ2: Queue[Apple] = Queue(new Apple, new Apple)
val fruitQ2: Queue[Fruit] = appleQ2.enqueue(new Orange)
