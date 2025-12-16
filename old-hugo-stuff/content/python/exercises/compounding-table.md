---
layout: exercise
title: Compounding Table
---

# Compounding Table

## Introduction

In this assignment you will practice:

- writing scripts,
- using command-line arguments,
- converting strings to numbers,
- loops,
- simple arithmetic, and
- string formatting.

## Problem Description

You are curious about the future value of an investment given an initial deposit and compounding periodic interest rate.

## Solution Description

Write a script called `compounding_interest.py` that takes three command line arguments, an initial deposit, a periodic interest rate, and a number of periods, and prints a table of the value of the deposit amount over time assuming compounding interest and no withdrawals.  Use the following formula for the deposit amount:

$$
a = p(1 + r)^n
$$

where 
- p is the original amount invested (i.e., the principal), 
- r is the periodic interest rate,
- n is the number of periods and
- a is the amount on deposit at the end of the nth period.

Period is abstract, and the interest rate is assumed to be for the period.  For example, if you want to see a yearly table for 5 years with an annual interest of 6% and an initial deposit of 100 you would use the following command-line script invocation and get the following output:

```shell
❯ python3 compounding_interest.py 100 .06 5
Period          Amount
------          ------
0               100.00
1               106.00
2               112.36
3               119.10
4               126.25
5               133.82
```
