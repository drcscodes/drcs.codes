---
layout: exercise
title: String Fun
---

# String Fun

## Introduction

In this assignment you will practice:

- writing functions,
- documenting functions, and
- manipulating strings.

## Problem Description

You enjoy word play and want to use Python 

## Solution Description

Write a module called `stringfun.py` with the following functions:

```python
def is_anagram(phrase1: str, phrase2: str) -> bool:
    '''Returns True if phrase1 and phrase2 are anagrams.  
    Phrases are anagrams if they contain the same letters (disregarding case)
    in the same numbers.
        
        >>> is_anagram('night', 'thing')
        True
        >>> is_anagram('young lady', 'An Old Guy')
        True 
        >>> is_anagram('sassy mama', 'mama says')
        True
        >>> is_anagram('sassy mama', 'mama say')
        False
        '''
    
def is_palindrome(phrase: str) -> bool:
    '''Returns True if phrase is a palindrome, ignoring case, 
    whitespace and punctuation.
    
    >>> is_palindrome('Radar')
    True
    >>> is_palindrome('Aibohphobia')
    True
    >>> is_palindrome('Red rum, sir, is murder!')
    True
    >>> is_palindrom('taco cat')
    True
    >>> is_palindrome('taco dog')
    False
    '''
```


### `doctest`

Use [doctest](https://docs.python.org/3/library/doctest.html) to test your module using Python REPL examples similar to the ones provided for each function above.  You may wish to include these test cases in your function docstrings, as well as others that you come up with on your own to test edge cases.  Remember that you can run docstring on your module like this:
