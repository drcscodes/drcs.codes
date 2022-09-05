---
layout: exercise
title: Students
---

# Students

## Introduction

In this assignment you'll practice

- writing classes,
- using `datetime.date` objects in Python,
- using objects, and
- transforming data comprised of objects.

## Problem Description

You are writing a web application to manage a database of students.

## Solution Description

Write a module named `students` with the classes and functions specified below.

### Required Classes and Functions

#### Classes

**`Student`**

Write a class called `Student` with the following instance variables:

- `id: str` -- 9-digit student ID
- `login: str` -- login ID
- `first_name: str`
- `last_name: str`
- `birth_date: datetime.date`
- `major: str`
- `hours: int` -- number of completed semester hours

These instance variables should all be initialized when you create an instance of `Student`.

In addition, implement the following methods:

- A magic method that gives instances of `Student` a `str` representation, whether by passing an instance to the `str()` function or echoing the value of an instance in the REPL.  See the examples below for the format of this string representation.

- A magic method that makes it possible to compare two instances of `Student` for equality using operator `==` -- two instances of `Student` are equal if all of their instance variables are equal,

- A magic method that makes it possible to compare two instances of `Student` using operator `<`. A `Student` is "less than" another if their completed semster hours is less than the other `Student`'s completed semester hours.  If both students have the same hours, then a younger student is "less than" the other.

- An instance method named `age` that that takes no parameters (other than self) and returns the `Student`'s age in years.

  - Note: Be careful about using the `datetime.timedelta` class due to leap years.  It's probably easier to use a different approach.

- An instance method named `year` that takes no parameters (other than self) and returns the year of the student based on the student's number of hours according to the rule that a student with less than 30 hours is a first-year student, a student with $\ge$ 30 and $<$ 60 is a second year student, and so on.


#### Functions

**`mk_students_dict`**

Write a function called `mk_students_dict` which takes a list of `Student` instances and returns a dictionary mapping student IDs to the `Student` instance having that ID.  If the list contains multiple `Student` instances with the same ID, `raise` an exception with the message "Duplicate Student instances with id XXXXXXXXX", where XXXXXXXXX is the duplicate student ID.

**`graduating`**

Write a function called `graduating` which takes a dictionary mapping student IDs to `Student` instances (like the one returned by `mk_students_dict`) and returns a list containing all the instances of `Student` with more than 115 hours.

### `doctest`

Include the [docstring](https://www.python.org/dev/peps/pep-0257/) below as a *module* docstring in your `students` module so that you can test your code using the [doctest](https://docs.python.org/3/library/doctest.html) module.

```sh
python -m doctest -v students.py
```

Take a look at these doctests.  Are there any edge cases that aren't tested?

```Python
>>> import datetime as dt
>>> cartman = Student("123456789", "ecartman3", "Eric", "Cartman", dt.date(2009, 7, 1), "BA", 80)
>>> kenny = Student("223456789", "kmccormick3", "Kenneth", "McCormick", dt.date(2009, 4, 10), "STAC", 80)
>>> stan = Student("323456789", "smarsh3", "Stanley", "Marsh", dt.date(2009, 10, 19), "IE", 85)
>>> kyle = Student("423456789", "kbroflovski3", "Kyle", "Broflovski", dt.date(2009, 5, 26), "CS", 85)
>>> cartman
<Eric Cartman (123456789, ecartman3), a 9 year-old 3rd-year BA major>
>>> str(cartman)
'<Eric Cartman (123456789, ecartman3), a 9 year-old 3rd-year BA major>'
>>> stan == kyle
False
>>> stan2 = Student("323456789", "smarsh3", "Stanley", "Marsh", dt.date(2009, 10, 19), "IE", 85)
>>> stan is stan2
False
>>> stan == stan2
True
>>> cartman < kenny
True
>>> stan < kenny
False
>>> cartman.age()
9
>>> cartman.year()
3
>>> boys = [cartman, kenny, stan, kyle]
>>> boys_dict = {"123456789": cartman, "223456789": kenny, "323456789": stan, "423456789": kyle}
>>> mk_students_dict(boys) == boys_dict
True
>>> bebe = Student("987654321", "bstevens3", "Barabara", "Stevens", dt.date(2009, 5, 5), "EE", 116)
>>> heidi = Student("887654321", "hturner3", "Heidi", "Turner", dt.date(2009, 6, 2), "PHYS", 117)
>>> annie = Student("787654321", "aknitts3", "Annie", "Knitts", dt.date(2010, 1, 25), "ME", 115)
>>> wendy = Student("687654321", "wtestaburger3", "Wendy", "Testaburger", dt.date(2009, 10, 2), "AE", 114)
>>> girls = [bebe, heidi, annie, wendy]
>>> graduating(mk_students_dict(boys + girls))
[<Barabara Stevens (987654321, bstevens3), a 9 year-old 4th-year EE major>, <Heidi Turner (887654321, hturner3), a 9 year-old 4th-year PHYS major>]
>>> try:
...      mk_students_dict([cartman] + boys)
... except Exception as e:
...     print(str(e))
...
Multiple students with 123456789
```

## Tips and Considerations

- Python [`datetime`](https://docs.python.org/3/library/enum.html) module
- [Python exceptions](https://docs.python.org/3/tutorial/errors.html)
