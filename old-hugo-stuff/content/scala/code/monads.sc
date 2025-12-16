import scala.util.Try
// Functors

List(1, 2, 3).map((x: Int) => x.toString)

Some(1).map(x => x.toString)

None.map(x => x.toString)


// Monads

def toInt(s: String): Option[Int] = {
  try {
    Some(s.toInt)
  } catch {
    // Type annotation on default case to indicate to
    // compiler that we mean to catch all exceptions.
    // Without type annotation, compiler issues warning.
    case _: Throwable => None
  }
}

Some("1").map((s: String) => toInt(s))

Some("one").map((s: String) => toInt(s))

Some("1").flatMap((s: String) => toInt(s))

Some("one").flatMap((s: String) => toInt(s))


List("RESPECT").map(_.toCharArray)
List("RESPECT").flatMap(_.toCharArray)

// For comprehensions

Some(1).foreach(println)
for (x <- Some(1)) println(x)

for (x <- Some(1)) println(x)


Some(1).map(_ + 1)
for (x <- Some(1)) yield x + 1

val sum = for {
    a <- toInt("1")
    b <- toInt("2")
    c <- toInt("3")
} yield a + b + c
sum == Some(6)

toInt("1").flatMap(a => toInt("2").flatMap(b => toInt("3").map(c => a + b + c)))
