---
layout: exercise
title: Matrix Operations
---

# Matrix Operations

## Introduction

In this assignment you will practice:

- manipulating data structures, and
- translating a specification (e.g., a mathematical definition) into code.

## Problem Description

You are writing an application that needs to perform basic operations on matrices.

## Solution Description

Write a module called `matrixops` (which you should save in a file called `matrixops.py`) with the following functions. For each function, be sure to the function design recipe in [Practical Programming: An Introduction to Computer Science using Python 3.6](https://pragprog.com/book/gwpy3/practical-programming-third-edition), Chapter 3 and summarized in our slides on functions, including the type contract using [type hints](https://docs.python.org/3/library/typing.html) and a [docstring](https://www.python.org/dev/peps/pep-0257/).

### `matrix_scalar_mult`

Multiplication of a $m \times n$ matrix $\mathbf{A}$ with a scalar number $x$ is defined as follows:

$$
\mathbf{A}x = \left[\begin{array}{cccc}
               A_{11}x & A_{12}x & \cdots & A_{1n}x \\
               A_{21}x & A_{22}x & \cdots & A_{2n}x \\
               \vdots & \vdots  & \ddots & \vdots \\
               A_{m1}x & A_{m2}x & \cdots & A_{mn}x \\
               \end{array}\right]
$$

Write a function named `matrix_scalar_mult` that takes a matrix parameter named a represented as a list of lists and a number parameter named `x`, and returns a matrix represented as a list of lists with the same dimensions as a and whose elements are the corresponding elements of a multiplied by x. Assume that `a[][]` is rectangular -– each row has the same length -– and that `a[][]`’s dimensions are > 0.

### `marrix_scalar_op`

A matrix can be the left operand of the arithmetic operators \*, /, +, and - with scalar right operands. Multiplication of a matrix with a scalar we saw above can be generalized for any `op` as follows:

$$
   \mathbf{A} \text{ op } x = \left[\begin{array}{cccc}
                  A_{11} \text{ op } x & A_{12} \text{ op } x & \cdots & A_{1n} \text{ op } x \\
                  A_{21} \text{ op } x & A_{22} \text{ op } x & \cdots & A_{2n} \text{ op } x \\
                  \vdots & \vdots  & \ddots & \vdots \\
                  A_{m1} \text{ op } x & A_{m2} \text{ op } x & \cdots & A_{mn} \text{ op } x \\
                  \end{array}\right]
$$

Write a function named `matrix_scalar_op` that takes a matrix parameter named a represented as a list of lists, an `op` function that takes two numbers and returns a number result (e.g., a function named `add` that, with the call `add(1, 2)` would return `3`), and a number parameter named `x`, and returns a matrix represented as a list of lists with the same dimensions as a and whose elements are the corresponding elements of a combined with `x` using `op`, that is $a_{ij}$ `op` `x`. Assume that `a[][]` is rectangular – each row has the same length – and that `a[][]`’s dimensions are > 0.
