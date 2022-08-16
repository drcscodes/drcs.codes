class Trooper:
    job = 'Law enforcement'

    def __init__(self, name):
        self.name = name

    # Used by print()
    def __str__(self):
        return "<Officer {}>".format(self.name)

    # Used by REPL
    def __repr__(self):
        # Call other instance methods within the same class by passing
        # self reference
        return str(self)


class SuperTrooper(Trooper):

    job = 'Hilarity'

    def __init__(self, name, is_mustached):
        super().__init__(name)
        if not is_mustached:
            raise ValueError('A Super Trooper must have a mustache')
        self.is_mustached = is_mustached

    # Used by print()
    def __str__(self):
        return "<{} {}>".format(self.name, ":-{" if self.is_mustached else ":-|")

    # Used by REPL
    def __repr__(self):
        return str(self)

    # Makes instances of SuperTrooper orderable
    def __lt__(self, other):
        if self.is_mustached and not other.is_mustached:
            return False
        elif not self.is_mustached and other.is_mustached:
            return True
        else:
            return self.name < other.name

def main(args):
    ts = [Trooper("Thorny"),
          Trooper("Mac"),
          Trooper("Rabbit"),
          Trooper("Farva"),
          Trooper("Foster")]
    print("Regular Troopers:")
    print(ts)
    # Regular Troopers aren't sortable because Trooper doesn't have a
    # __lt__ method. If you uncomment the line below, this script
    # won't run.

    #print(sorted(ts))

    sts = [SuperTrooper("Thorny", True),
           SuperTrooper("Mac", True),
           SuperTrooper("Rabbit", True),
           SuperTrooper("Farva", True),
           SuperTrooper("Foster", False)]
    print("SuperTroopers:")
    print(sts)
    print("SuperTroopers sorted by mustache, then by name:")
    print(sorted(sts))

if __name__=="__main__":
    import sys
    main(sys.argv)
