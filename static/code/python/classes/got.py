class GotCharacter:
    creator = "George R.R. Martin"

    def __init__(self, name=None):
        self.name = name if name else "No one"

class Stark(GotCharacter):
    house = "Stark"
    words = "Winter is coming"
    sigil = "Direwolf"
    home = "Winterfell"

    def __init__(self, name=None):
        # This is how you invoke a superclass method
        super().__init__(name)

    def full_name(self):
        return "{} Stark".format(self.name)

    def holla():
        return f"{house} says {words}"

class Lannister:
    creator = "George R.R. Martin"
    words = "Hear me roar"
    sigil = "Lion"
    home = "Casterly Rock"

    def __init__(self, name=None):
        self.name = name if name else "No one"

    def full_name(self):
        return "{} Lannister".format(self.name)


class Targaryen:
    creator = "George R.R. Martin"
    words = "Fire and blood"
    sigil = "Dragon"
    home = "Valyria"

    def __init__(self, name=None):
        self.name = name if name else "No one"

    def full_name(self):
        return "{} Targaryen".format(self.name)
