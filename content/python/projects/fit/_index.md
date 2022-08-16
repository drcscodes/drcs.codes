---
layout: exercise
title: Fit
---

# `fit` Module

## Introduction

In this assignment you'll practice

- writing functions and modules,
- doing arithmetic calculations,
- simple text processing, and
- testing modules with doctest.

## Problem Description

You run a phyical fitness contest modeled after Navy Special Warfare's physical screening test. You get data from contestants that includes times on a run, a swim, push-ups, pull-ups, and sit-ups and you must convert these times and numbers to a single score that can be used to rank fitness contest entries.

## Solution Description

You don't have the data file yet, but you want to be prepared so you wil create a module that caclulates elements of the composite score. Your module will be named `fit` and contain the functions listed below.

### `doctest`

The specifications for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v fit.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

### Required Functions

**IMPORTANT**: Do not modify the provided docstrings!

```Python
def time_seconds(time):
    """Take a time in MM:SS format and return the corresponding number of seconds

    Parameters:
    time: str -- time in MM:SS format

    Return:
    int -- number of seconds of a time specified in MM:SS format

    Usage Examples:
    >>> time_seconds("2:30")
    150
    """
```

```Python
def score(entry):
    """Take a dict containing the data for a participant and calculate a score

    Parameters:
    entry: dict[str -> Any] -- a dictonary containng the fitness test data for
           an entry in the contest

    Return:
    int -- score computed as follows:
           swim in seconds + run insconds - (2 * pushups) - situps - (pullups * 6)

    Usage Examples:
    >>> score({'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'})
    995
    """
```

```Python
def average(data, event):
    """Take a list of dicts of fitness test entries and return the average for
    a single event

    Parameters:
    data: List[dict] -- a list of dictionaries of fitness test data
    event: str -- the name of an event, from the header of the data file

    Return:
    float -- the average score for that event. For run and swim, should be in
             seconds

    Usage Examples:
    >>> average([{'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'}, {'Run': '12:00', 'Push-ups': '100', 'Sit-ups': '100', 'Swim': '12:45', 'Name': 'Drogo', 'Pull-ups': '20'}], "Pull-ups")
    25.0
    """
    scores = []
```

```Python
def winner(data, event):
    """Take a list of dicts of fitness test entries and return the winner of
    event

    Parameters:
    data: List[dict] -- a list of dictionaries of fitness test data
    event: str -- the name of an event, from the header of the data file

    Return:
    (str, int) -- a tuple with the name of the winner of the event and the score
                  they got for that event. Swim and run should be in seconds

    Usage Examples:
    >>> winner([{'Run': '11:10', 'Push-ups': '60', 'Sit-ups': '80', 'Swim': '11:45', 'Name': 'Tyrion', 'Pull-ups': '30'}, {'Run': '12:00', 'Push-ups': '100', 'Sit-ups': '100', 'Swim': '12:45', 'Name': 'Drogo', 'Pull-ups': '20'}], "Pull-ups")
    ('Tyrion', 30)
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `fit` module in the Python REPL to test your functions as you write and modify them. For example, ssuming you're in the same directory as your `fit.py` file:

```Python
Python 3.6.3 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import fit
>>> fit.time_seconds("2:30")
150
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(fit)
```
