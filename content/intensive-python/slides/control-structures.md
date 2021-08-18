#+TITLE: Control Structures
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

* Control Structures

** Structured Programming

Any algorithm can be expressed by:

- Sequence - one statement after another
- Selection - conditional execution (not conditional jumping)
- Repetition - loops

We've already seen sequences of statements. Today we'll learn
selection (conditional execution), and repetition.

** The ~if-else~ Statement

Conditional execution:

#+BEGIN_SRC python
if boolean_expression:
    # a single statement executed when boolean_expression is true
else:
    # a single statement executed when boolean_expression is false
#+END_SRC

- ~boolean_expression~ is not enclosed in parentheses
- ~else:~ not required

Example:

#+BEGIN_SRC python
if (num % 2) == 0:
    print("I like " + str(num))
else:
    print("I'm ambivalent about " + str(num))
#+END_SRC

** Blocks

Python is block-structured. Contiguous sequences of statements at the
same indentation level form a block. Blocks are like single statements
(not expressions - they don't have values).

#+BEGIN_SRC python
if num % 2 == 0:
   print(str(num) + " is even.")
   print("I like even numbers.")
else:
    print(str(num) + " is odd.");
    print("I'm ambivalent about odd numbers.")
#+END_SRC

** Multi-way ~if-else~ Statements

This is hard to follow:

#+BEGIN_SRC python
if color == "red":
    print("Redrum!")
else:
    if color == "yellow":
        print("Submarine")
    else:
        print("A Lack of Color")
#+END_SRC

This multi-way if-else is equivalent, and clearer:

#+BEGIN_SRC python
if color == "red":
    print("Redrum!")
elif color == "yellow":
    print("Submarine")
else:
    print("A Lack of Color")
#+END_SRC

** Loops

Algorithms often call for repeated action, e.g. :

- “repeat ... while (or until) some condition is true” (looping) or
- “for each element of this array/list/etc. ...” (iteration)

Python provides two control structures for repeated actions:

- ~while~ loop
- ~for~ iteration statement

** ~while~ Loops

~while~ loops are pre-test loops: the loop condition is tested before the
loop body is executed

#+BEGIN_SRC python
while condition: # condition is any boolean expression
    # loop body executes as long as condition is true
#+END_SRC

Example

#+BEGIN_SRC python
>>> def countdown(n):
...     while n > 0:
...         print(n)
...         n -= 1
...
print('Blast off!')
...
>>> countdown(5)
5
4
3
2
1
Blast off!
#+END_SRC

** ~for~ Statements

~for~ is an *iteration* statement

- iteration means visiting the elements of an iterable data structure

In the for loop:

#+BEGIN_SRC python
>>> animal = 'Peacock'
>>> for animal in ['Giraffe', 'Alligator', 'Liger']:
...     print(animal)
...
Giraffe
Alligator
Liger
>>> animal
'Liger'
#+END_SRC

- ~animal~ is assigned to each element of the iterable list of animals in successive executions of the ~for~ loop's body
- notice that the loop variable re-assigned an existing variable

** ~break~ and ~else~

- ~break~ terminates execution of a loop
- optional ~else~ clause executes only of loop completes without
executing a ~break~ (weird - don't ever write code with ~for~-~else~)

#+BEGIN_SRC python
>>> def sweet_animals(animals):
...     for animal in animals:
...         print(animal)
...         if animal == 'Liger':
...             print('Mad drawing skillz!')
...             break
...     else:
...         print('No animals of note.')
...
>>> sweet_animals(['Peacock', 'Liger', 'Alligator'])
Peacock
Liger
Mad drawing skillz!
>>> sweet_animals(['Peacock', 'Tiger', 'Alligator'])
Peacock
Tiger
Alligator
No animals of note.
#+END_SRC

** Run-time Errors

An error detected during execution is called an exception and is represented at runtime by an exception object. The Python interpreter raises an exception at the point an error occurs. The exception is handled by some exception-handling code. Here we don't handle the ValueError ourselves, so it's handled by the Python shell:

#+BEGIN_SRC python
>>> int('e')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'e'
#+END_SRC

We can handle an exception by enclosing potentially error-raising code
in a try block and handling errors in an except clause.

#+BEGIN_SRC python
try:
    code_that_may_raise_error()
except ExceptionType as e:
    print(str(e))
    code_that_handles_exception()
#+END_SRC

~ExceptionType~ and ~as e~ are optional. If left off, except clause will catch any
exception.

** Exception Handling Example

#+BEGIN_SRC python
>>> def get_number_from_user():
...     input_is_invalid = True
...     while input_is_invalid:
...         num = input('Please enter a whole number: ')
...         try:
...             num = int(num)
...             # Won't get here if exception is raised. '
...             input_is_invalid = False
...         except ValueError:
...             print(num + ' is not a whole number. Try again.')
...    return num
...
>>> get_number_from_user()
Please enter a whole number: e
e is not a whole number. Try again.
Please enter a whole number: 3
3
#+END_SRC

For more information, see [[https://docs.python.org/3/tutorial/errors.html][https://docs.python.org/3/tutorial/errors.html]]
