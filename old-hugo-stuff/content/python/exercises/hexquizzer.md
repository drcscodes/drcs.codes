---
layout: exercise
title: Hex Quizzer
---

# Hex Quizzer

## Introduction

In this assignment you will practice:

- writing expressions and statements,
- using control structures, and
- working with types.

## Problem Description

You want to get better at converting between decimal and hexadecimal numbers in your head.

## Solution Description

Write a program called `hexquizzer.py` that presents the user with a randomly chosen decimal number in the range [0, 15] and asks the user to provide the hexadecimal representation of that number.  A sample run of the program would look like:

```shell
❯ python3 hexquizzer.py
Press Q to quit.
What is the hexadecimal representation of decimal 13?
C
Incorrect.  Decimal 13 is hexadecimal 0xd.
What is the hexadecimal representation of decimal 13?
D
Correct!
What is the hexadecimal representation of decimal 10?
0xa
Correct!
What is the hexadecimal representation of decimal 7?
0x7
Correct!
What is the hexadecimal representation of decimal 2?
2
Correct!
What is the hexadecimal representation of decimal 2?
2
Correct!
What is the hexadecimal representation of decimal 15?
0xF
Correct!
What is the hexadecimal representation of decimal 1?
q
```

### Tips and Considerations

- Peruse https://docs.python.org/3/library/random.html.
- Look up the documentation for the built-in `int` function.
- Look up the documentation for the built-in `hex` function.
