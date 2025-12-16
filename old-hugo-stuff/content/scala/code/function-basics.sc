import scala.annotation.tailrec

// Notice that if the "body" of the function is a single expression,
// we don't need curly braces
def double(x: Int): Int = 2 * x

val ten = double(5)

// Literal function.  Notice the type annotation
val doubleFun: Int => Int = {(x: Int) => {2 * x}}
val doubleFun2= (x: Int) => 2 * x

val evens = List(1,2,3,4,5,6,7,8).filter(x => x % 2 == 0)
val evens2 = List(1,2,3,4,5,6,7,8).filter(_ % 2 == 0)


// Procedures are functions that don't return values.  Always annotate
// return type of Unit
def say(something: String): Unit = {
  println(something)
}

val useless = say("my name")

def max(x: Int, y: Int): Int =
  if (x > y) x
  else y

val simpleMax = max(3, 5)

// Repeated parameters (a.k.a. var-args) syntax
// Inside the function, a repeated parameter is an Array
// Notice that if
def max(x: Int, xs: Int*): Int = {
  // We'll learn this later
  xs.foldLeft(x)((x, y) => if (x > y) x else y)
}
// Must pass a multiple single arguments to a repeated parameter
val varArgsMax = max(3, 5, 7, 1)

// Expand a Seq into multiple single args by appending with : _*
val seqMax = max(0, List(2, 4, 6, 8, 0): _*)


def mean(xs: Double*) = xs


// Default parameters
// For this toy example, locales are US or EU, currency is USD or EURO
// Also note that we're not doing locale-specific group separators, which
// are a bit more complicated
def moneyString(
    dollars: Int,
    cents: Int,
    locale:String ="US",
    currency:String = "USD"): String =
  locale match {
    case "US" =>
      currency match {
        // Note field width and zero-padding in
        // cents using f-interpolator
        case "EURO" => f"$dollars.$cents%02d Euros"
        case "USD" => f"$$$dollars.$cents%02d"
      }
    case "EU" =>
      currency match {
        // Unicode in Scala source is fine
        case "EURO" => f"$dollars,$cents%02d €"
        case "USD" => f"$dollars,$cents%02d USD"
      }
  }

val Pi = 3.14159
val piString = f"$Pi%.2f"

val usDollars = moneyString(3, 2)
// Can leave off args with default paramters in middle of parameter
// list if you specify the remaining args with named parameters
val usDollarsDefaultLocale =
  moneyString(3, 2, currency = "EURO")

val euEuros = moneyString(3, 2, "EU", "EURO")

// Note that return type is mandatory for recursive functions
def fac(n: Int): Int = {
  // Try calling fac with a negative Int
  require(n >= 0,
  "Factorial only defined for non-negative integers")
  if (n <= 1) 1
  else n * fac(n - 1)
}

val fiveBang = fac(5)
// If you uncomment this, you'll get StackOverflow
//val justBang = fac(60000)

def facIter(n: BigInt): BigInt = {
  // @tailrec annotation tells compiler to confirm tail call optimization
  @tailrec
  def iter(i: BigInt, accum: BigInt): BigInt = {
    if (i <= 1) accum
    else iter(i - 1, i * accum)
  }
  require(n >= 0, "Factorial only defined for non-negative integers")
  iter(n, 1)
}

// We'll just let this overflow for simplicity
val bangin = facIter(60000)

