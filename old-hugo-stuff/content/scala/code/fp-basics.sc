class Coffee(val price: BigDecimal = 1)

class CreditCard(val owner: String, val number: String,
  var limit: BigDecimal, var balance: BigDecimal) {

  // Which guideline does this method violate?
  def charge(amount: BigDecimal) = {
    if ((balance + amount) > limit) {
      false
    } else {
      balance -= amount
      true
    }
  }

  override def equals(other: Any) = other match {
    case that: CreditCard =>
      owner == that.owner && number == that.number
    case _ => false
  }
}

class Cafe {
  def buyCoffee(cc: CreditCard): Coffee = {
    val cup = new Coffee()
    cc.charge(cup.price)
    cup
  }
}

class Payments {
  def charge(cc: CreditCard) = ???
}

class BetterCafe {
  def buyCoffee(cc: CreditCard, p: Payments): Coffee = {
    val cup = new Coffee()
    p.charge(cc, cup.price)
    cup
  }
}

case class Charge(cc: CreditCard, amount: BigDecimal) {
  def combine(other: Charge): Charge =
    if (cc == other.cc) Charge(cc, amount + other.amount)
    else throw new Exception("Can't combine charges on different cards.")
}

class FunctionalCafe {

  def buyCoffee(cc: CreditCard): (Coffee, Charge) = {
    val cup = new Coffee()
    (cup, Charge(cc, cup.price))
  }

  def buyCoffees(cc: CreditCard, n: Int): (List[Coffee], Charge) = {
    val purchases: List[(Coffee, Charge)] = List.fill(n)(buyCoffee(cc))
    val (coffees, charges) = purchases.unzip
    (coffees, charges.reduce((c1,c2) => c1.combine(c2)))
  }
}

def coalesce(charges: List[Charge]): List[Charge] =
  charges.groupBy(_.cc).values.map(_.reduce(_ combine _)).toList

