---
layout: exercise
title: Word Histogram
---

# Word Histogram

## Introduction

In this homework you will practice

- data structures,
- control structures,
- functional programming, and
- using modules that you learn on your own from documentation.

## Problem Descrtiption

You're a curious linguist with computer hacking skills and you want to see if [Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law) holds for texts contained in files lying around on your disk.

## Solution Description

Write a Python module in `word_hist.py` that includes the following functions.  You should copy these function declarations and docstrings verbatim to ensure that we can successfully autograde your submission.

```Python
from typing import *

def normalize_text(text: str) -> str:
    """Return a copy of text in lowercase with punctuation removed.

    Usage Examples:
    >>> normalize_text("Numchuk skills, bow hunting skills, computer hacking skills...")
    'numchuk skills bow hunting skills computer hacking skills'
    """

def mk_word2count(text: str) -> Dict[str, int]:
    """Return a dictionary mapping words in text to their count in text. 
    Be sure to remove newlines in the text!

    Usage Examples: (Note technique for testing dict equality.)

    >>> mk_word2count('the butcher the baker the candlestick maker') == {'butcher': 1, 'baker': 1, 'candlestick': 1, 'the': 3, 'maker': 1}
    True
    """

def dict2tuples(word_dict: Dict[str, int],
                key: Callable[[Tuple], Any]=None) -> List[Tuple[str, int]]:
    """Convert a str:int dictionary to a sorted (in descending order) list of 
    (str, int) tuples, optionally with a key function for sorting the tuples

    Usage Examples:
    >>> dict2tuples({'a': 2, 'b': 5, 'c': 1}, key=lambda t: t[1])
    [('b', 5), ('a', 2), ('c', 1)]
    """

def normalize_counts(tuples: Sequence[Tuple[str, int]],
                     max_value: int=100) -> Sequence[Tuple[str, int]]:
    """Return: sequence of tuples with same first elements as input tuples
    but whose second elements are normalized to the range 0 to
    max_value.

    Usage Examples:
    >>> wctups = [('a', 200), ('the', 180), ('an', 160), ('shenannigans', 50)]
    >>> normalize_counts(wctups, 100)
    [('a', 100), ('the', 90), ('an', 80), ('shenannigans', 25)]
    """

def word_hist(bar_list: Sequence[Tuple[str, int]]) -> List[str]:
    """Create a text-based bar chart from bar_list. Return: List[str] with one
    line per tuple in bar_list. Each string in the returned list has a
    right-aligned label from the first element of the corresponding tuple
    in bar_list, a | character, then a number of Xs equal to the
    second element from the tuple.

    Usage Examples:
    >>> from pprint import pprint
    >>> pprint(word_hist([('a', 10),('the', 9),('an', 8),('shenannigans', 2)]))
    ['           a | XXXXXXXXXX',
     '         the | XXXXXXXXX',
     '          an | XXXXXXXX',
     'shenannigans | XX']
    """
```

### `main`

Structure your main method as we have been taught:

```Python
def main(args):
    # code intended to be executed when run as a script

if __name__=="__main__":
   import sys
   main(sys.argv)
```

The user may supply one to three command line arguments to **your** Python script. The first argument to the `python` interpreter, `sys.argv[0]`, is the name of your script, i.e.,  `args[0] = "word_hist.py"`, so there will be 1 to 4 arguments in `sys.argv`. `sys.argv`, a list of strings, should be passed as-is to the `main()` function to minimize confusion.

  * The first argument will be the file name of Python script (ie. `args[0] = "word_hist.py"`).
  * The second argument, if supplied, must be the name of a text file to read and analyze.
    + If the user supplies a file name on the command line and the file does not exist, you may simple allow the program to exit due to the missing file and let Python report that the file was not found.
    + If the user does not supply a file name on the command line, prompt the user for the file name. If the file does not exist, tell the user the file doesn't exist and prompt the user repeatedly until they enter the name of a file that exists.
  * The third argument, if supplied, is the maximum bar length for the word frequency histogram.
  * The fourth argument, if supplied, is the number of lines of the bar graph to display.

Here's a snippet of code that checks for the existence of a file:

```Python
import os.path
os.path.exists("file_name.txt") # returns True if file_name.txt exists
```

Once you have a valid file name, read the file contents into a string. Here's a snippet of code that opens a file for reading as text and reads the file contents into a `str` variable:

```Python
infile = open(file_name, 'r') # opens file_name as readable file object infile
text = infile.read()          # dumps text data from infile into text variable
infile.close()                # closes infile
```

Once you read the contents of the file into a `str`, use the functions you created above to:

- normalize the text to remove punctuation and make all letters lowercase,
- create a dictionary mapping words from the text to the occurence counts,
- create a list of tuples whose first elements are words from the word count dictionary, and whose second elements are the associated counts -- this list should be sorted in descending order by word count, e.g., largest count first,
- normalize the counts in the list of word count tuples to the maximum bar length of your histogram,
- create a histogram using your `word_hist` function, and
- print the first `num_lines` of the histogram, where `num_lines` is the number of lines of the histogram to display.

Here's a sample program run, using the file [i-have-a-dream.txt](i-have-a-dream.txt):

```sh
$ python hw2.py i-have-a-dream.txt 80 80
           the | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            of | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
            to | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
           and | XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
             a | XXXXXXXXXXXXXXXXXXXXXXXXXXXX
            be | XXXXXXXXXXXXXXXXXXXXXXXXX
            we | XXXXXXXXXXXXXXXXXXXXXXX
          will | XXXXXXXXXXXXXXXXXXXX
          that | XXXXXXXXXXXXXXXXXX
            is | XXXXXXXXXXXXXXXXX
            in | XXXXXXXXXXXXXXXXX
          this | XXXXXXXXXXXXXXX
       freedom | XXXXXXXXXXXXXXX
            as | XXXXXXXXXXXXXXX
          from | XXXXXXXXXXXXX
          have | XXXXXXXXXXXXX
           our | XXXXXXXXXXXXX
          with | XXXXXXXXXXXX
             i | XXXXXXXXXXX
         negro | XXXXXXXXXX
           not | XXXXXXXXXX
           one | XXXXXXXXXX
           let | XXXXXXXXXX
           day | XXXXXXXXX
          ring | XXXXXXXXX
         dream | XXXXXXXX
          come | XXXXXXX
        nation | XXXXXXX
         every | XXXXXXX
           for | XXXXXX
            go | XXXXXX
          back | XXXXXX
         today | XXXXXX
           are | XXXXXX
          must | XXXXXX
     satisfied | XXXXXX
            by | XXXXXX
           you | XXXXXX
         their | XXXXXX
       justice | XXXXXX
          able | XXXXXX
          when | XXXXX
           all | XXXXX
            it | XXXX
        cannot | XXXX
           men | XXXX
         white | XXXX
          long | XXXX
           now | XXXX
           but | XXXX
         there | XXXX
      together | XXXX
          time | XXX
         which | XXX
            on | XXX
         faith | XXX
      children | XXX
       america | XXX
            my | XXX
          free | XXX
         check | XXX
           has | XXX
         shall | XXX
         great | XXX
           new | XXX
         years | XXX
           who | XXX
            an | XXX
          into | XXX
            so | XXX
         black | XXX
          hope | XXX
       hundred | XXX
   mississippi | XXX
            up | XXX
            us | XXX
          down | XXX
         until | XXX
      mountain | XXX
         later | XXX
```

Note that the full output would be very long and words with low rank would have no `X`s.
