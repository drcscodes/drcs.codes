---
layout: exercise
title: Text Utilities
---

# Text Utilities

## Introduction

In this assignment you'll practice

- writing functions and modules,
- doing arithmetic calculations,
- simple text processing,
- manipulating data structures and
- testing modules with doctest.

## Problem Description

You need to do some text processing and decide to write a few utility functions to get started.

## Solution Description

Write a module named `textutil` with the functions specified below.

### `doctest`

The specification for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are given using type hints documented in [PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v textutil.py
```

### Required Functions


```Python
def long_words(text, n):
    """Return the words in text that are longer than n.

    Parameters:
    text: str -- the text of interest

    Return: Sequence[int] -- words in text that are longer than n

    Usage Examples:
    >>> long_words('I do not write good', 3)
    ['write', 'good']
    """

def num_long_words(text, n):
    """Return the number of words in text that are longer than n.

    Parameters:
    text: str -- the text of interest

    Return: int -- the number of words in text that are longer than n

    Usage Examples:
    >>> num_long_words('I do not write good', 3)
    2
    """

def count_if(sequence, predicate):
    """Count the number of elements in sequence that satisfy predicate function.

    Parameters:
    sequence: Sequence -- a sequence of elements of any type
    predicate: Function: Any -> bool -- a function that takes a single parameter and returns a
    bool

    Usage Examples:
    >>> count_if([0, 1, 2, 3, 4], lambda x: x % 2 == 0)
    3
    >>> count_if(['fe', 'fi', 'fo', 'fum'], lambda s: len(s) > 2)
    1
    """

def word_counts(sentence_list):
    """Return a dictionary mapping words in normalized text to their
    counts in the text.

    Parameters:
    sentence_list: List[str] - a list of sentences

    Return: a Dict[str, int] whose keys are words and associated values are
    the number of times the word appears in the sentences in sentence_list

    Usage Examples: (Note technique for testing dict equality.)

    >>> word_counts(["i dont even have any skills", "i have numchuk skills \
    bow hunting skills computer hacking skills"]) == {'have': 2, 'numchuk': 1, \
    'hacking': 1, 'i': 2, 'even': 1, 'computer': 1, 'any': 1, 'bow': 1,\
    'hunting': 1, 'dont': 1, 'skills': 4}
    True
    """

def make_tups(seq1, seq2):
    """Convert seq1 and seq2 to a list of tuples with corresponding elements of
    seq1 and seq2.

    Parameters:
    seq1: Sequence[Any] -- a sequence of elements of any type
    seq2: Sequence[Any] -- a sequence of elements of any type

    Return: Sequence[(Any, Any)] - a sequence of 2-tuples where the ith tuples
    contain the ith elements of seq1 and seq2. Length of returned list is
    length of shortest input seq

    Usage Examples:
    >>> make_tups(['a', 'b', 'c', 'd'], [1, 2, 3])
    [('a', 1), ('b', 2), ('c', 3)]
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `textutil` module in the Python REPL to test your functions as you write and modify them. For example, ssuming you're in the same directory as your `textutil.py` file:

```Python
Python 3.6.1 |Continuum Analytics, Inc.| (default, Jul  2 2016, 17:53:06)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import hw1
>>> hw1.palindrome("a but tuba")
True
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(textutil)
```
