---
layout: "exercise"
title: "Exercise - BMI Module"
---

# `bmi` Module

## Introduction

In this assignment you'll practice

- writing functions and modules,
- manipulating strings,
- converting values to different data types,
- doing arithmetic calculations, and
- testing modules with doctest.

## Problem Description

You want to live a healthy life and use your computer to help you analyze your fitness and health.

## Solution Description

Create a module that provides convenience functions for converting imperial measures to metric equivalents, a function to calculate BMI, and two functions that tell you whether you are overweight or underweight according to government [BMI standards](https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm). Your module will be named `bmi` and contain the functions listed below.

### `doctest`

The specification for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v bmi.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

### Required Functions

Implement the following functions in your `bmi.py` file. For convenience you can simply copy the code below.

**IMPORTANT**: Do not modify the provided docstrings!

```Python
from typing import *

def in2m(inches: float) -> float:
    """Convert inches to meters according to convsersion rule 1m == 39.3701in

    Usage examples:
    >>> abs(in2m(39.3701) - 1) < .01
    True
    """

def lb2kg(pounds: float) -> float:
    """Convert pounds to kilograms according to convsersion rule 1kg == 2.2lb

    Usage examples:
    >>> abs(lb2kg(2.2) - 1) < .01
    True
    """

def bmi(weight: float, height: float) -> float:
    """Return body mass index (BMI) for given weight in kg and height in meters.

    Usage examples:
    >>> abs(bmi(66, 1.72) - 22.309) < .01
    True
    """

def is_overwieght(weight: float, height: float) -> bool:
    """Answer whether the given weight in kg and height in meters is considered
    overweight by government standards (BMI > 25).

    Usage examples:
    >>> is_overwieght(74, 1.72)
    True
    >>> is_overwieght(73, 1.72)
    False
    """

def is_underweight(weight: float, height: float) -> bool:
    """Answer whether the given weight in kg and height in meters is considered
    underweight by government standards (BMI < 18.5).

    Usage examples:
    >>> is_underweight(54, 1.72)
    True
    >>> is_underweight(55, 1.72)
    False
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `bmi` module in the Python REPL to test your functions as you write and modify them. For example, ssuming you're in the same directory as your `bmi.py` file:

```Python
Python 3.5.2 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bmi
>>> bmi.bmi(bmi.lb2kg(114), bmi.in2m(65))
19.010279100284023
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(bmi)
```
