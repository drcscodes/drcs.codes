---
layout: homework
title: hw1 - Generate Sentence
---

# Homework 1 - `generate_sentence` Module

## Introduction

In this assignment you'll practice

- writing functions and modules,
- using lists and dictionaries,
- selective logic (if statements),
- simple text processing, and
- testing modules with doctest.

## General Instructions

**This is an individual assignment.**

Collaboration at a reasonable level will not result in substantially similar code. Students may only collaborate with fellow students currently taking this course, the TA's and the lecturer. Collaboration means talking through problems, assisting with debugging, explaining a concept, etc. You should not exchange code or write code for others.

Notes:

- Include a comment with your name, Canvas login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

You're interested in natural language processing and, having learning about [context free grammars](http://www.ps.uni-saarland.de/~niehren/oz-natural-language-script.html/vorlesung/node49.html) for natural languages, you want to experiment with sentence generation.

## Solution Description

Write a module named `generate_sentence` with functions that can be used to generate noun phrases, verb phrases and sentences in subject-verb-object form. When the module is imported only the functions are defined. When the module is run as a script a sentence is generated and printed to the console.

### `doctest`

The specifications for each function is given as a [docstring](https://www.python.org/dev/peps/pep-0257/) -- which you should include in your code -- and the types of arguments and return values are documented using [type hints](https://docs.python.org/3/library/typing.html).

Because each function will have a docstring that includes usage examples formatted as Python interactive sessions, you can use [doctest](https://docs.python.org/3/library/doctest.html) to test your code using this command line invocation:

```sh
python -m doctest -v generate_sentence.py
```

If all the tests pass, then you'll probably (but not defnitely) get a 100 on this homework.

### Required Functions

**IMPORTANT**: Do not modify the provided docstrings!

```Python
def subject_phrase(nouns, adjectives):
    """Randomly select a noun from a list of nouns and and adjective from a
    list of adjectives and return a noun phrase --
    f"{article} {adjective} {noun}"

    Parameters:
    nouns: List[str] -- a list of single-word nouns, which should be singular
    adjectives: List[str] -- a list of single-word adjectives

    Returns: str -- f"{article} {adjective} {noun}" where the article is chosen
                    randomly from "the" or "a" (an if noun begins with a vowel).

    Usage examples:
    >>> some_nouns = ["woman", "man", "dog", "car"]
    >>> some_adjectives = ["good", "bad", "ugly"]
    >>> sp = subject_phrase(some_nouns, some_adjectives)
    >>> article, adjective, noun =  [w.lower() for w in sp.split(" ")]
    >>> article in ["the", "a", "an"]
    True
    >>> adjective in some_adjectives
    True
    >>> noun in some_nouns
    True
    """

def verb_phrase(subject, adverbs, capabilities, silly = False):
    """From a noun phrase, a list of adverbs, and a dictionary of capabilities
    produce a verb phrase from a randomly selected adverb and a randomly
    selected verb (optionally) from a list of verbs

    Parameters:
    subject: str -- the subject of the verb to be selected from capabilities.
                    Note that this will be a noun phrase, so the last word in
                    subject is the noun that is used as a key in capabilities.
    adverbs: List[str] -- a list of single-word adverbs
    capabilities: Dict[str, List[str]] -- a dict mapping nouns to lists of
                  single-word  verbs that the nouns are capable of doing.
                  Verbs should be conjugated in the third person singular.
    silly: boolean -- if True the verb is chosen randomly from all the
                      capabilities of all the nouns,
                      if False the verb is chosen randomly from only the verbs
                      that are associated with the subject noun in capabilities.

    Returns: str -- f"{adverb} {verb}"

    Usage examples:
    >>> some_adverbs = ["violently", "gently", "loudly", "silently"]
    >>> some_capabilities = {"woman": ["reads", "throws", "eats", "vomits"], \
                             "man": ["reads", "throws", "eats", "vomits"], \
                             "dog": ["chews", "scratches", "licks"], \
                             "car": ["transports", "crushes", "flattens"], \
                             "fidget spinner": ["amuses", "confuses"]}
    >>> noun = "dog"
    >>> vp = verb_phrase(noun, some_adverbs, some_capabilities)
    >>> adverb, verb = [w.lower() for w in vp.split(" ")]
    >>> adverb in some_adverbs
    True
    >>> verb in some_capabilities[noun]
    True
    >>> vp2 = verb_phrase(noun, some_adverbs, some_capabilities, True)
    >>> adverb2, silly_verb = [w.lower() for w in vp2.split(" ")]
    >>> adverb2 in some_adverbs
    True
    >>> silly_verb in ['reads', 'throws', 'eats', 'vomits', 'reads', 'throws', \
                 'eats', 'vomits', 'chews', 'scratches', 'licks', \
                 'transports', 'rolls over', 'amuses', 'confuses', \
                 'crushes', 'flattens']
    True
    """

def object_phrase(verb, adjectives, affordances, silly = False):
    """From a verb and a list of affordances, generate an object phrase with
    a noun that is cabable of receiving the action of the verb, as determined
    by the noun's affordances.

    Parameters:
    verb: str -- the action being performed on the object noun. Conjugated in
                 third person singular.
    affordances: Dict[str, List[str]] -- a dict mapping object nouns to single-word
                                         verbs that can act on the noun.
                                         Verbs should be conjugated in the
                                         third person singular.
    silly: boolean -- if True the noun is chosen randomly from all the
                      keys of affordances,
                      if False the noun is chosen randomly from only the nouns
                      for which the verb appears in their associated values in
                      affordances.


    Returns: str -- f"{adjective} {noun}"

    Usage examples:
    >>> some_affordances = {"dinner": ["eats", "vomits"], \
                            "lunch": ["eats", "vomits"], \
                            "paw": ["scratches", "licks", "chews", "crushes", "flattens"], \
                            "foot": ["scratches", "licks", "chews", "crushes", "flattens"], \
                            "shoe": ["throws", "chews", "crushes", "flattens"], \
                            "man": ["amuses", "confuses", "transports", "crushes", "flattens"], \
                            "woman": ["amuses", "confuses", "transports", "crushes", "flattens"], \
                            "poem": ["reads"]}
    >>> some_adjectives = ["good", "bad", "ugly"]
    >>> op = object_phrase("amuses", some_adjectives, some_affordances)
    >>> article, adjective, noun =  [w.lower() for w in op.split(" ")]
    >>> article in ["the", "a", "an"]
    True
    >>> adjective in some_adjectives
    True
    >>> noun in ["man", "woman"]
    True
    >>> op2 = object_phrase("amuses", some_adjectives, some_affordances, True)
    >>> article2, adjective2, silly_noun =  [w.lower() for w in op2.split(" ")]
    >>> silly_noun in ["dinner", "lunch", "paw", "foot", "shoe", \
                       "man", "woman", "poem"]
    True
    """

def make_sentence(sp, vp, op):
    """Takes a noun phrase to be used as the subject, a verb phrase, and a noun
    phrase to be used as the object and returns a sentece.

    Parameters:
    sp: str -- a noun phrase to be used as the subject
    vp: str -- a verb phrase
    op: str -- a noun phrase to be used as the object

    Returns: str -- a sentence with a capitalized first word and a period for
                    punctuation

    Usage examples:
    >>> make_sentence("the brilliant professor", "engagingly teaches", \
                      "the enraptured class")
    'The brilliant professor engagingly teaches the enraptured class.'
    """
```

### Testing Your Module Interactively

In addition to running the doctests as described above, you can import your `generate_sentence` module in the Python REPL to test your functions as you write and modify them. For example, assuming you're in the same directory as your `generate_sentence.py` file:

```Python
$ python
Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:14:23)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import generate_sentence
>>> some_nouns = ["woman", "man", "dog", "car", "fidget spinner"]
>>> some_adjectives = ["good", "bad", "ugly"]
>>> some_adverbs = ["violently", "gently", "loudly", "silently"]
>>> some_capabilities = {"woman": ["reads", "throws", "eats", "vomits"], \
...                              "man": ["reads", "throws", "eats", "vomits"], \
...                              "dog": ["chews", "scratches", "licks"], \
...                              "car": ["transports", "rolls over"], \
...                              "fidget spinner": ["amuses", "confuses"]}
>>> some_affordances = {"dinner": ["eats", "vomits"], \
...                             "lunch": ["eats", "vomits"], \
...                             "paw": ["scratches", "licks", "chews", "crushes", "flattens"], \
...                             "foot": ["scratches", "licks", "chews", "crushes", "flattens"], \
...                             "shoe": ["throws", "chews", "crushes", "flattens"], \
...                             "man": ["amuses", "confuses", "transports", "crushes", "flattens"], \
...                             "woman": ["amuses", "confuses", "transports", "crushes", "flattens"], \
...                             "poem": ["reads"]}
>>> sp = generate_sentence.subject_phrase(some_nouns, some_adjectives)
>>> sp
'a bad dog'
>>> vp = generate_sentence.verb_phrase("dog", some_adverbs, some_capabilities)
>>> vp
'gently scratches'
>>> op = generate_sentence.object_phrase("scratches", some_adjectives, some_affordances)
>>> op
'the ugly foot'
>>> generate_sentence.make_sentence(sp, vp, op)
'A bad dog gently scratches the ugly foot.'
```

After you modify your module you'll need to restart your Python REPL, or reload it using the `importlib` module:

```Python
>>> import importlib as imp
>>> imp.reload(generate_sentence)
```

### Running your module as a script

When your module is run as a script, it should generate a sentence using the functions you implemented above and print it to the console. If the user provides a single command-line argument of `silly` to the script, the script generates a silly sentence.

```sh
$ python generate_sentence.py
The good woman loudly reads the ugly poem.
$ python generate_sentence.py silly
The obtuse car silently throws the good paw.
```

## Grading

- 50 points for having all required functions that can be called with the right parameters but not necessarily returning correct values
- 10 points for each correctly implemented function named exactly as listed above with docstrings as provided (40 points total)
- 10 points for script functionality which doesn't execute when imported as module
- 10 points for following instructions, e.g., including your name, Canvas and GTID, indenting with four spaces, correctly naming your module and file

## Tips, Considerations and Food for Thought

- You'll need the [random](https://docs.python.org/3/library/random.html) module.
  - What's the purpose of the `random.seed(1)` calls in the docstrings?
- In `verb_phrase` you're using a dictionary normally -- from keys to values. In `object_phrase` you're using a dictionary in reverse -- from values to keys, which is harder. It's awkward, but I've needed to do this many times in my programming career. As you think about your solution, consider:
  - Can there be repeated keys in a dictionary?
  - Can there be repeated values? Or here, can the same word appear among the values for multiple keys?


## Turn-in Procedure

Submit your `generate_sentence.py` file on Canvas as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.
