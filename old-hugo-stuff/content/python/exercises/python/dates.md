---
layout: homework
title: Dates
---

# Dates

## Introduction

In this assignment you will practice:

- writing functions,
- documenting functions,
- doing basic operations with values and variables, and
- dealing with date-related data.

## Problem Description

## Solution Description

Write a module called `dates` (which you should save in a file called `dates.py`) with the following functions.  For each function, be sure to the function design recipe in [Practical Programming: An Introduction to Computer Science using Python 3.6](https://pragprog.com/book/gwpy3/practical-programming-third-edition), Chapter 3 and summarized in our slides on [Python functions](../../slides/functions.pdf), including the type contract using [type hints](https://docs.python.org/3/library/typing.html) and a [docstring](https://www.python.org/dev/peps/pep-0257/).

### `days_since_epoch`

> Inspired by Exercise 1 in [Think Python, 2e, Chapter 5](http://greenteapress.com/thinkpython2/html/thinkpython2006.html#sec68)

The `time` funciton of the `time` module in Python's standard library returns the number of seconds since the "epoch", which is arbitrarily defined as midnight, 1 January 1970.  The return value of the `time` function is a `float` that includes a fractional part if your computer's internal clock keeps time in increments smaller than one second.  For example:

```Python
>>> import time
>>> time.time()
1539877438.7275572
```

Write a function named `days_since_epoch` that takes no parameters and returns an `int` value denoting the number of days since the epoch.

**Hints**

- You'll need to calculate how many seconds are in a day.
- You may need to use a type conversion function to ensure that your function returns an `int`.

**Python REPL Examples**

```Python
>>> days_since_epoch()
17822
```


### `weeks_elapsed`

> Inspired by Chapter 3, Exercise 8 in [Practical Programming: An Introduction to Computer Science using Python 3.6](https://pragprog.com/book/gwpy3/practical-programming-third-edition)

Write a function named `weeks_elapsed` that takes two `int` parameters indicating a number of days of elapsed time and returns an `int` value indicating the number of full weeks that would elapse in that number of days.

**Python REPL Examples**

```Python
>>> weeks_elapsed(16)
2
```


### `weekday_from`

Assume that you use numbers to indicate the day of the week. For example, you might use 0 to represent Monday, 1 to represent Tuesday, and so on.  There are always seven days in each week.

Write a function named `weekday_from` that takes two `int` parameters:
- `today` -- the current day, and
- `days` -- a number of days from today

and returns an `int` indicating the weekday on which the day `days` from `today` will fall.  For example, if today is day 2, then 5 days from today will be day 0, 8 days from today will be day 3, and 15 days from today will be day 3.

- Hint: use Python's modulus operator.

**Python REPL Examples**

```Python
>>> weekday_from(2, 15)
3
```

### `is_leapyear`

Leap years are years with one additional day (e,g., 29 February) in order to re-calibrate calendar years to align with astronomical years. In the modern Gregorian calendar leap years are defined as follows:

> Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 were not leap years, but the years 1600 and 2000 were. -- [Introduction to Calendars](http://aa.usno.navy.mil/faq/docs/calendars.php), US Naval Observatory

Write a function `is_leapyear` that takes a single `int` parameter named `year` and returns `True` if the `year` is a leap year, `False` otherwise.

**Python REPL Examples**

```Python
>>> is_leapyear(2016)
True
>>> is_leapyear(2017)
False
```

### `doctest`

We will use [doctest](https://docs.python.org/3/library/doctest.html) to test your module using Python REPL examples similar to the ones provided for each function above.  You may wish to include these test cases in your function docstrings, as well as others that you come up with on your own to test edge cases.  Remember that you can run docstring on your module like this:
