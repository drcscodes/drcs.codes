case class Person(name: String,
                  isMale: Boolean,
                  children: Person*)

val lara = Person("Lara", false)
val bob = Person("Bob", true)
val julie = Person("Julie", false, lara, bob)

val persons = List(lara, bob, julie)

persons.
  filter(p => !p.isMale).
  flatMap(p => (p.children.
    map(c => (p.name, c.name))))

for (p <- persons; if !p.isMale; c <- p.children)
  yield (p.name, c.name)

// or, even more readable:

for {
 p <- persons if !p.isMale
 c <- p.children
} yield (p.name, c.name)

case class Book(title: String, authors: String*)

val books: List[Book] =
  List(
    Book(
      "Structure and Interpretation of Computer Programs",
      "Abelson, Harold", "Sussman, Gerald J."
    ),
    Book(
      "Principles of Compiler Design",
      "Aho, Alfred", "Ullman, Jeffrey"
    ),
    Book(
      "Programming in Modula-2",
      "Wirth, Niklaus"
    ),
    Book(
      "Elements of ML Programming",
      "Ullman, Jeffrey"
    ),
    Book(
      "The Java Language Specification", "Gosling, James",
      "Joy, Bill", "Steele, Guy", "Bracha, Gilad"
    )
  )

// All books with an author named Gosling
for (b <- books;
  a <- b.authors if a startsWith "Gosling")
  yield b.title

// All books with "Program" in the title
for (b <- books if (b.title indexOf "Program") >= 0)
  yield b.title


// Names of authors who have written at least two books
val as = for (b1 <- books; b2 <- books if b1 != b2;
     a1 <- b1.authors; a2 <- b2.authors if a1 == a2)
  yield a1

Set(as:_*)

val list = List("now", "is", "", "the", "time")
for (element <- list) {
  println(element)
}
for (element <- list) yield {
  element.toUpperCase
}

list.map(e ⇒ e.toUpperCase)
list.map(e => e.length)

list.map(e => e.toCharArray)
list.flatMap(e => e.toCharArray)

for {
  x <- List(1, 2, 3)
  y <- List('a, 'b, 'c)
  z <- List(
} yield (x, y)


List(1, 2, 3).flatMap(x => List('a, 'b, 'c).map(y => (x, y)))
