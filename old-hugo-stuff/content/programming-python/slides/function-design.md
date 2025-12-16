---
aspectratio: 1610
title: Function Design
---

## Function Design Recipe

1. Examples
    - What a few representative calls to the function look like in the Python REPL.
        - Think from the function *user's* perspective.
        - Examples become doctests in the function's docstring.

2. Header
    - Parameter names and types
    - Return type

3. Description
    - Short paragraph (1 or 2 sentences) describing the function's behavior.

4. Body
    - Implement the algorithm (sequence of statements) that accomplishes the function's task, deriving the function's output (return value) and/or effect from the the function's inputs (arguments).

5. Test
    - Test your function on some representative inputs (try to include edge cases).


## Writing Function Examples

Let's apply this design recipe in the creation of a simple function to calculate the length of the hypotenuse from the lengths of the two legs (the sides that join in a right angle).

First, decide the name of the function.

- Descriptive word(s)
    - Verbs may imply an imperative function called for its effect, not a return value
        - `print("hello")`, `exit()`
    - Nouns may imply a pure function, a return value derived only from the function's arguments with no side effects
        - `type(1)`, `double(2)`

- Avoid Python keywords or names of library functions.
    - Tip:

        ```Python
        >>> import keyword
        >>> keyword.kwlist # lists all the Python keywords
        >>> keyword.iskeyword("foo") # True if "foo" is a keyword
        ```

- Follow Python's [naming conventions](https://www.python.org/dev/peps/pep-0008/).

## Hypotenuse Function Examples

We'll name our function `hypotenuse`. General naming tips:

- Only abbreviate if abbreviation is well-known or obvious
    - If you must, form a new abbreviation by eliminating vowels starting from the right, e.g., `format` $\rightarrow$ `formt` $\rightarrow$ `fmt`
- Some abbreviations are idiomatic, e.g., `i` as an loop variable used as an `int` index
- Length of the name should be inversely proportional to its scope
    - Local variables can be short
    - Modules, functions, and classes should have more descriptive names

Our examples:
```Python
>>> hypotenuse(3, 4)
5
>>> hypotenuse(5, 12)
13
```

## Function Headers

The function header includes the function's name and parameter names.  We add a *type contract*, which we document using Python's new (as of 3.5) [type hints](https://docs.python.org/3/library/typing.html) feature.  Here are a few basic types.  A full explanation is in [PEP 484](https://www.python.org/dev/peps/pep-0484), including a complete list of [types in the `typing` module](https://www.python.org/dev/peps/pep-0484/#the-typing-module)

:::::::::::::: {.columns}
::: {.column width="40%"}
- `int`
- `float`
- `str`
:::
::: {.column width="60%"}
- `List[int]`
- `Tuple[float]`
- `Dict[str, int]`
:::
::::::::::::::

## Hypotenuse Function Header

Deciding on the type contract of `hypotenuse`:

- The sides of a triangle are measured with numbers. What kind of numbers, `int`s, `floats`?
- The return value is also a number.  Is the return type the same type as the parameters?

Since integer values can be represented as `float`s, we settle on the this:

```Python
def hypotenuse(a: float, b: float) -> float:
```

The type contract says: if you pass two values of type `float` in your call to `hypotenuse`, the function will return a value of type `float`.

## Hypotenuse Function Description

The function description states what the functions does.  We place this description in the function's [docstring](https://www.python.org/dev/peps/pep-0257/).  Any string that occurs as the first item in the definition of a module, function, class, or method is a docstring.  By convention we use triple double quotes for docstrings.

```Python
def hypotenuse(a: float, b: float) -> float:
    """Take the lengths of the two legs, a and b, of a right triangle
    and return the length of the hypotenuse.
    """
```

This incomplete but legal version of the function returns `None` because it doesn't have a return statement.

- Tip: We can *stub* the function with a return statement that returns a dummy value, like 0.0, so code that uses our function will work but produce incorrect results.  That way we can get the "plumbing" of our program working before filling in the details of the functions.

## Designing a Function Body

The function body implements an algorithm that produces the functions output (or effect) based on the function's inputs.  The algorithm for calculating a hypotenuse is:

1. Square leg `a`
2. Square leg `b`
3. Sum the squares
4. Take the square root of the sum of the squares.

The last step produces the final result.

Later in the course will learn how to design algorithms.  FOr now we can think of algorithm design intuitively.

The next slide shows the algorithm above translated to Python code.

## Hypotenuse Function Body

```Python
import math

def hypotenuse(a: float, b: float) -> float:
    """Take the lengths of the two legs, a and b, of a right triangle
    and return the length of the hypotenuse.
    """
    a2 = a * a
    b2 = b * b
    sum_squares = a2 + b2
    result = math.sqrt(sum_squares)
    return result
```

Of course this function can be shortened, but this version shows every detail.

## Testing the Hypotenuse Function

We can test our function manually in the REPL or by adding example functions calls to a script.  We should also add the examples we created in step 1 of the function design recipe to the docstring.

```Python
import math

def hypotenuse(a: float, b: float) -> float:
    """Take the lengths of the two legs, a and b, of a right triangle
    and return the length of the hypotenuse.

    >>> hypotenuse(3, 4)
    5
    >>> hypotenuse(5, 12)
    13
    """
    a2 = a * a
    b2 = b * b
    sum_squares = a2 + b2
    result = math.sqrt(sum_squares)
    return result
```

If we do this then we get automated testing for free with [doctest](https://docs.python.org/3/library/doctest.html).
