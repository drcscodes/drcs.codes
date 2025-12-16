abstract class Person(val name: String) {
  def id: Int
  override def toString = s"${getClass.getName}[name=$name]"
}

//val bob = new Person("Bob")

class SecretAgent(iid: Int, codename: String)
    extends Person(codename) {
  def id: Int = ???
  override val name = "secret" // Don’t want to reveal name . . .
  override val toString = "secret" // . . . or class name
}

class Item(val description: String, val price: Double) {

  final override def equals(other: Any) = other match {
      case that: Item =>
        this.description == that.description && this.price == that.price
      case _ => false
    }

  final override def hashCode = (description, price).##

  override def toString = s"$description, price: $price"
}

val i1 = new Item("munkie", 1000)
val i2 = new Item("wrench", 1000)
val i3 = new SecretAgent(7, "Craig")

i1 == i2
i2 == i3
val i4 = i1
val i5 = new Item("munkie", 1000)

i4 == i1
i4 eq i1

i5 == i1
i5 eq i1

// Companion object must be in same source file as class
object Item {

  var itemCount = 0

  // Factory method for creating
  def apply(description: String, price: Double): Item = {
    itemCount += 1
    new Item(description, price)
  }

  def apply(description: String): Item = {
    itemCount += 1
    new Item(description, 1)
  }
}

val item = Item("Key Lime", 3.14)
val item2 = Item("Punkin")

Item.itemCount

// Traits

trait Logger {
  def log(msg: String)
}

trait ConsoleLogger extends Logger {
  def log(msg: String) { println(msg) }
}

abstract class SavingsAccount(var balance: Int) extends Logger {
  def withdraw(amount: Int) {
    if (amount > balance) log("Insufficient funds")
    else balance -= amount
   }
}

trait Timestamping extends ConsoleLogger {
  override def log(msg: String) = super.log(s"${java.time.Instant.now()} $msg")
}
trait Shortening extends ConsoleLogger {
  override def log(msg: String) =
    super.log( if (msg.length <= 18) msg else s"${msg.substring(0, 10)}")
}
trait Shouting extends Logger {
  abstract override def log(msg: String) =
    super.log(msg.toUpperCase)
}



val acct1 = new SavingsAccount(1) with Timestamping with Shortening
acct1.withdraw(2)

val acct2 = new SavingsAccount(1) with Shortening with Timestamping
acct2.withdraw(2)

val acct3 = new SavingsAccount(1) with Shortening with Shouting
acct3.withdraw(2)

// Below won't compile because there is no concrete log method
// for Shouting.log to call
//val acct4 = new SavingsAccount(1) with Shouting with Shortening
//acct4.withdraw(2)
