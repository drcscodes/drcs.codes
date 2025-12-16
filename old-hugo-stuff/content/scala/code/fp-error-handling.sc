import scala.util.Try

def failingFn(i: Int): Int = {
  val y: Int = throw new Exception("fail!")
  try {
    val x = 42 + 5
    x + y
  } catch {
    case e: Exception => 43
  }
}


// Same as failingFn but "value" of y substituted
// for y
def failingFn2(i: Int): Int = {
  try {
    val x = 42 + 5
    x + ((throw new Exception("fail!")): Int)
  } catch {
    case e: Exception => 43
  }
}

failingFn2(1)

// If y were referentially transparent, this would hold,
// but it doesn't:

// failingFn(1) == failingFn2(1)

def mean(xs: Seq[Double]): Double =
  if (xs.isEmpty)
    throw new ArithmeticException("mean of empty list undefined")
  else
    xs.sum / xs.length

mean(Seq(1,2,3))

// Throws ArithmeticException:
// mean(Seq())


case class PhD(name: String, advisor: String, coAdvisor: Option[String] = None)

val drs = List(
  PhD("Martin Oderksy", "Niklaus Wirth"),
  PhD("Dr. CS", "Charles Isbell"),
  PhD("Charles Isbell", "Rodney Brooks", Some("Paul Viola"))
)

val name2DrTuples = drs.map(dr => (dr.name, dr))
val advisors: Map[String, PhD] = name2DrTuples.toMap

// Defining this function to avoid confusion in sample code due to the fact
// that Map[T].get returns Option[T] but Option[T] returns T
def getAdvisor(name: String): Option[PhD] = advisors.get(name)

// If there is a "Dr. CS" instance of type Option[PhD] (this), then
// Option.map applies the function a => a.name to this.get and wraps it in Some
// Note: getAdvisor returns an Option[PhD] on which map is invoked,
// so this refers to the Option[PhD] instance returned by getAdvisor
getAdvisor("Dr. CS").map((a: PhD) => a.name)

// Here there is no "Dr. J" instance, so getAdvisor returns None
// None.isEmpty is true, so map simply returns None
getAdvisor("Dr. J").map(_.name)

// Like getAdvisor("Dr. CS").map(_.name)
getAdvisor("Dr. CS").map(_.advisor)

// PhD.coAdvisor is an Option[String]
getAdvisor("Dr. CS").map(_.coAdvisor)

// Option.flatMap pulls the value out of the Option[String]
getAdvisor("Dr. CS").flatMap(_.coAdvisor)

getAdvisor("Charles Isbell").map(_.advisor)
getAdvisor("Charles Isbell").map(_.coAdvisor)
getAdvisor("Charles Isbell").flatMap(_.coAdvisor)

val drNames = for (dr <- drs) yield dr.name
val allAdvisors = for {
  dr <- drs
  coAdvisor <- dr.coAdvisor
} yield (dr.name, dr.advisor, coAdvisor)


// Dealing with Exception-oriented APIs
val x = Try(Integer.parseInt("1"))
val y = Try(Integer.parseInt("foo"))

val z = try {
  Right(Integer.parseInt("foo"))
} catch {
  case e: Throwable => Left(e)
}
