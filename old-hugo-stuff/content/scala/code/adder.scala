import scala.util.Try
import scala.io.StdIn.readLine

val answer = for {
  x <- Try { readLine("x: ").toInt }
  y <- Try { readLine("y: ").toInt }
} yield x + y

println(s"x + y = $answer")
