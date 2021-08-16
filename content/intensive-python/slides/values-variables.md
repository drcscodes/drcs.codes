#+TITLE: Values and Variables
#+AUTHOR:
#+EMAIL:
#+DATE:
#+DESCRIPTION:
#+KEYWORDS:
#+LANGUAGE:  en
#+OPTIONS: H:2 toc:nil num:t
#+BEAMER_FRAME_LEVEL: 2
#+COLUMNS: %40ITEM %10BEAMER_env(Env) %9BEAMER_envargs(Env Args) %4BEAMER_col(Col) %10BEAMER_extra(Extra)
#+LaTeX_CLASS: beamer
#+LaTeX_CLASS_OPTIONS: [smaller]
#+LaTeX_HEADER: \usepackage{verbatim, multicol, tabularx,color}
#+LaTeX_HEADER: \usepackage{amsmath,amsthm, amssymb, latexsym, listings, qtree}
#+LaTeX_HEADER: \lstset{frame=tb, aboveskip=1mm, belowskip=0mm, showstringspaces=false, columns=flexible, basicstyle={\footnotesize\ttfamily}, numbers=left, frame=single, breaklines=true, breakatwhitespace=true, keywordstyle=\bf, stringstyle=\color{blue}, commentstyle=\color{green}}
#+LaTeX_HEADER: \setbeamertemplate{footline}[frame number]
#+LaTeX_HEADER: \hypersetup{colorlinks=true,urlcolor=blue}
#+LaTeX_HEADER: \logo{\includegraphics[height=.75cm]{GeorgiaTechLogo-black-gold.png}}

* Values and Variables

** Languages and Computation

Every powerful language has three mechanisms for combining simple ideas to form more complex ideas:([[http://mitpress.mit.edu/sicp/full-text/book/book-Z-H-10.html][SICP 1.1]])

- primitive expressions, which represent the simplest entities the language is concerned with,
- means of combination, by which compound elements are built from simpler ones, and
- means of abstraction, by which compound elements can be named and manipulated as units.

Today we'll begin learning Python's facilities for primitive expresions, combination, and elementary abstraction.

** Values

An expression has a value, which is found by evaluating the expression. When you type expressions into the Python REPL, Python evaluates them and prints their values.

#+BEGIN_SRC python
>>> 1
1
>>> 3.14
3.14
>>> "pie"
'pie'
#+END_SRC

The expressions above are literal values. A literal is a textual representation of a value in Python source code.

- Do strings always get printed with single quotes even if we diefine them with double quotes?

** Types

All values have types. Python can tell you the type of a value with the built-in type function:

#+BEGIN_SRC python
>>> type(1)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("pie")
<class 'str'>
#+END_SRC

- What's the type of '1'?

** The Meaning of Types

Types determine which operations are available on values. For example, exponentiation is defined for numbers (like int or float):

#+BEGIN_SRC python
>>> 2**3
8
#+END_SRC

... but not for ~str~ (string) values:

#+BEGIN_SRC python
>>> "pie"**3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#+END_SRC

** Overloaded Operators

Some operators are overloaded, meaning they have different meanings when applied to different types. For example, + means addition for numbers and concatenation for strings:

#+BEGIN_SRC python
>>> 2 + 2
4
>>> "Yo" + "lo!"
'Yolo!'
#+END_SRC

~*~ means multiplication for numbers and repetition for strings:

#+BEGIN_SRC python
>>> 2 * 3
6
>>> "Yo" * 3
'YoYoYo'
>>> 3 * "Yo"
'YoYoYo'
#+END_SRC

** Expression Evaluation

Mathematical expressions are evaluated using precedence and associativity rules as you would expect from math:

#+BEGIN_SRC python
>>> 2 + 4 * 10
42
#+END_SRC

If you want a different order of operations, use parentheses:

#+BEGIN_SRC python
>>> (2 + 4) * 10
60

#+END_SRC

Note that precedence and associativity rules apply to overloaded versions of operators as well:

#+BEGIN_SRC python
>>> "Honey" + "Boo" * 2
'HoneyBooBoo'
#+END_SRC

- How could we slighlty modify the expression above to evaluate to 'HoneyBooHoneyBoo' ?


** Variables

A variable is a name for a value. You bind a value to a variable using an assignment statement (or as we'll learn later, passing an argument to a function):

#+BEGIN_SRC python
>>> a = "Ok"
>>> a
'Ok'
#+END_SRC

~=~ is the assignment operator and an assignment statement has the form ~<variable_name> = <expression>~

Variable names, or identifiers, may contain letters, numbers, or underscores and may not begin with a number.

#+BEGIN_SRC python
>>> 16_candles = "Molly Ringwald"
  File "<stdin>", line 1
    16_candles = "Molly Ringwald"
             ^
SyntaxError: invalid syntax
#+END_SRC

** Python is Dynamically Typed

Python is dynamically typed, meaning that types are not resoved until run-time. This means two things practically:

1. Values have types, variables don't:
   #+BEGIN_SRC python
   >> a = 1
   >>> type(a)
   <class 'int'>
   >>> a = 1.1 # This would not be allowed in a statically typed language
   >>> type(a)
   <class 'float'>
   #+END_SRC
2. Python doesn't report type errors until run-time. We'll see many examples of this fact.


** Keywords

Python reserves some identifiers for its own use.

#+BEGIN_SRC python
>>> class = "CS 2316"
  File "<stdin>", line 1
    class = "CS 2316"
          ^
SyntaxError: invalid syntax
#+END_SRC

The assignment statement failed becuase class is one of Python's keywords:

#+BEGIN_SRC python
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
#+END_SRC

- What hapens if you try to use a variable name on the list of keywords?
- What happens if you use ~print~ as a variable name?

** Assignment Semantics

Python evaluates the expression on the right-hand side, then binds the expression's value to the variable on the left-hand side. Variables can be reassigned:

#+BEGIN_SRC python
>>> a = 'Littering and ... '
>>> a
'Littering and ... '
>>> a = a * 2
>>> a
'Littering and ... Littering and ... '
>>> a = a * 2
>>> a              # I'm freakin' out, man!
'Littering and ... Littering and ... Littering and ... Littering and ... '
#+END_SRC

Note that the value of ~a~ used in the expression on the right hand side is the value it had before the assignment statement.

What's the type of ~a~?

** Type Conversions

Python can create new values out of values with different types by applying conversions named after the target type.

#+BEGIN_SRC Python
>>> int(2.9)
2
>>> float(True)
1.0
>>> int(False)
0
>>> str(True)
'True'
>>> int("False")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'False'
#+END_SRC

- What happens if you evaluate the expression ~integer('1')~ ?

** Strings

Three ways to define string literals:

- with single quotes: 'Ni!'

- double quotes: "Ni!"

- Or with triples of either single or double quotes, which creates a multi-line string:

    #+BEGIN_SRC Python
    >>> """I do HTML for them all,
    ... even made a home page for my dog."""
    'I do HTML for them all,\neven made a home page for my dog.'
    #+END_SRC

** Strings

Note that the REPL echoes the value with a ~\n~ to represent the newline character. Use the print function to get your intended output:

#+BEGIN_SRC python
>>> nerdy = """I do HTML for them all,
... even made a home page for my dog."""
>>> nerdy
'I do HTML for them all,\neven made a home page for my dog.'
>>> print(nerdy)
I do HTML for them all,
even made a home page for my dog.
#+END_SRC

That's pretty [[http://braverhund.com][nerdy]].

** Strings

Choice of quote character is usually a matter of taste, but the choice can sometimes buy convenience. If your string contains a quote character you can either escape it:

#+BEGIN_SRC python
>>> journey = 'Don\'t stop believing.'
#+END_SRC

or use the other quote character:

#+BEGIN_SRC python
>>> journey = "Don't stop believing."
#+END_SRC

- How does Python represent the value of the variable ~journey~ ?

** String Operations

Because strings are sequences we can get a string's length with ~len()~:

#+BEGIN_SRC python
>>> i = "team"
>>> len(i)
4
#+END_SRC

and access characters in the string by index (offset from beginning – first index is 0) using ~[]~:

#+BEGIN_SRC python
>>> i[1]
'e'
#+END_SRC

Note that the result of an index access is a string:

#+BEGIN_SRC python
>>> type(i[1])
<class 'str'>
>>> i[3] + i[1]
'me'
>>> i[-1] + i[1] # Note that a negative index goes from the end
'me'
#+END_SRC

- What is the index of the first character of a string?
- What is the index of the last character of a string?

** String Slicing

~[:end]~ gets the first characters up to but not including ~end~

#+BEGIN_SRC python
>>> al_gore = "manbearpig"
>>> al_gore[:3]
'man'
#+END_SRC

~[begin:end]~ gets the characters from ~begin~ up to but not including end

#+BEGIN_SRC python
>>> al_gore[3:7]
'bear'
#+END_SRC

~[begin:]~ gets the characters from ~begin~ to the end of the string

#+BEGIN_SRC python
>>> al_gore[7:]
'pig'
>>>
#+END_SRC

- What is the relationship between the ending index of a slice and the beginning index of a slice beginning right after the first slice?

** String Methods

~str~ is a class (you'll learn about classes later) with many methods (a method is a function that is part of an object). Invoke a method on a string using the dot operator.

~str.find(substr)~ returns the index of the first occurence of
~substr~ in ~str~

#+BEGIN_SRC python
>>> 'foobar'.find('o')
1
#+END_SRC

- Write a string slice expression that returns the username from an email address, e.g., for 'bob@aol.com' it returns 'bob'.
- Write a string slice expression that returns the host name from an email address, e.g., for 'bob@aol.com' it returns 'aol.com'.

** Values, Variables, and Expression

- Values are the atoms of computer programs
- We (optionally) combine values using operators and functions to form compound expressions
- We create variables, which are identifiers that name values, define other identifiers that name functions, classes, modules and packages
- By choosing our identifiers, or names, carefully we can create beautiful, readable programs
