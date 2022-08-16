# You could probably use another import here:
from pprint import pprint
import datetime as dt
import statistics as stats

# Person class goes here:
class Person:

    def __init__(self, name, birthdate, height, weight):
        """
        a name (str),
        a birthdate (str) formatted in ISO 8601 format,
        a height in cm (int),
        a weight in kilograms (float),
        """
        self.name = name
        self.birthdate = birthdate
        self.height = height
        self.weight = weight

    def __repr__(self):
        """
        returns a str like <name, birthdate, height, weight>,
        e.g., <Stan, 2008-08-13, 150cm, 45kg>;
        """
        return f"<{self.name}, {self.birthdate}, {self.height}, {self.weight}>"

    def height_inches(self):
        """
        returns the Person object’s height in inches (1in = 2.54cm), and
        """
        return self.height / 2.54

    def weight_pounds(self):
        """
        returns the Person object’s weight in pounds (1kg = 2.2lb).
        """
        return self.weight / 2.2

    def days_until(self, target_age):
        """As of today, returns the number of days until this person is
        age years old. Will be 0 if person is exactly age years oldn,
        egative if person is older than age years old.
        """
        birth_date = dt.datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        target_age_days = dt.timedelta(days=target_age*365).days
        current_age_days = (dt.datetime.now().date() - birth_date).days
        return target_age_days - current_age_days

peeps = [Person('Garrison', '1960-05-05', 172, 66),
         Person('Stan', '2008-08-13', 150, 45),
         Person('Kyle', '2008-02-25', 160, 50),
         Person('Cartman', '2008-05-26', 140, 100),
         Person('Kenny', '2008-07-30', 130, 40)]

# Fill in the appropriate expressions in place of the Nones

avg_height = stats.mean([p.height for p in peeps])
print("avg_height: {}cm".format(avg_height))

avg_weight = stats.mean([p.weight for p in peeps])
print("avg_wieght: {}kg".format(avg_weight))

name2heights = {p.name: p.height_inches() for p in peeps}
print("name2heights:")
pprint(name2heights)

name2weights = {p.name: p.weight_pounds() for p in peeps}
print("name2weights:")
pprint(name2weights)

peeps_by_age = sorted(peeps, key=lambda p: p.birthdate)
pprint(peeps_by_age)


print("Days until adult (aged 18):")
for person in peeps:
    print(f"{person.name} turns 18 in {person.days_until(18)} days.")
