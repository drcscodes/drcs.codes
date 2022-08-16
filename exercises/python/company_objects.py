
class Company:
    def __init__(self, ticker, name, sic, sector, addr1, addr2, city, state, zip):
        self.ticker = ticker
        self.name  = name
        self.sic   = sic
        self.sector= sector
        self.addr1 = addr1
        self.addr2 = addr2
        self.city  = city
        self.state = state
        self.zip   = zip

    def __repr__(self):
        return f"{self.ticker}, {self.name}, {self.sector}"


if __name__ == "__main__":
    c = Company("W", "Widgets, INC", "1", "TECH", "1 Main St", "", "Atlanta", "GA", "30332")
    print(str(c))
