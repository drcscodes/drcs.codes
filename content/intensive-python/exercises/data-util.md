---
layout: exercise
title: Exercise - Data Util Module
---

# `data_util` Module

## Introduction

In this assignment you'll practice

- writing functions and modules,
- manipulating strings and data structures,
- testing modules with doctest.

## Problem Description

You need to manipulate Python data (and you're not familiar with Python's standard library).

## Solution Description

Create a module named `data_util` that implements the functions described below.

### `doctest`

The specification for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v data_util.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

### Required Functions

Implement the following functions in your `data_util.py` file. For convenience you can simply copy the code below.

**IMPORTANT**: Do not modify the provided docstrings!

```Python
from typing import *

def split(text: str, delim=",") -> List[str]:
    """Return a list of fields in text separated by delim.

    Parameters:
    text: str -- the string to split into fields

    Return:
    List[str] of fields in text

    Usage examples:
    >>> split("foo, bar, baz")
    ['foo', ' bar', ' baz']
    """

def zip(xs: Sequence, ys: Sequence) -> Sequence[Tuple]:
    """Return [(x0, y0), ..., (xn, yn)] where n is 1 - min(len(xs), len(ys))

    Parameters:
    xs: Sequence -- the "left" list
    ys: Sequence -- the "right list

    Return:
    Sequence[Tuple] of pairs of corresponding elements in xs and yx

    Usage examples:
    >>> zip(['a', 'b', 'c', 'd'], [1,2,3])
    [('a', 1), ('b', 2), ('c', 3)]
    """

def zip_with_indexes(xs: Sequence) -> Sequence[Tuple[int, Any]]:
    """Return [(0, x0), ..., (n, xn)] where n is 1 - len(xs)

    Parameters:
    xs: Sequence -- a sequence

    Return:

    List[Tuple[int, Any]] of pairs of indexes in xs and values at
    corresponding index

    Usage examples:
    >>> zip_with_indexes(['a', 'b', 'c', 'd'])
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
    """

def lookup_keys(v: Any, d: Dict) -> Sequence[Any]:
    """Return list of keys in dict d which map to value

    Parameters:
    v: Any -- a value which may be in dictionary d
    d: dict -- a dictionary which may contain the value v

    Return:
    Sequence[Any] of all keys in d that map to v

    Usage examples:
    >>> lookup_keys(1, {'a': 1, 1: 'b', 'c': 2, 'd': 1})
    ['a', 'd']
    """
```

## Sample Solution

- [data_util.py](data_util.py)
