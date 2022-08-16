#+TITLE: Functional Programming
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
#+LaTeX_HEADER: \lstset{frame=tb, aboveskip=1mm, belowskip=0mm, showstringspaces=false, columns=flexible, basicstyle={\scriptsize\ttfamily}, numbers=left, frame=single, breaklines=true, breakatwhitespace=true, keywordstyle=\bf}
#+LaTeX_HEADER: \setbeamertemplate{footline}[frame number]
#+LaTeX_HEADER: \hypersetup{colorlinks=true,urlcolor=blue}
#+LaTeX_HEADER: \logo{\includegraphics[height=.75cm]{GeorgiaTechLogo-black-gold.png}}

* Functional Programming in Python

** Functional Features in Python

Functions are first class, meaning they can be

- stored in variables and data structures
- passed as arguments to functions
- returned from functions

** Higher-Order Functions

A higher order function is a function that takes another function as a parameter or returns a function as a value. We've already used one:

#+BEGIN_SRC python
>>> help(sorted)
...
sorted(iterable, key=None, reverse=False)
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.
#+END_SRC

The second parameter, ~key~, is a function. In general, a *sort key* is the part of an object on which comparisons are made in a sorting algorithm.

** Sorting without a ~key~

Say we have a list of tuples, *(name, gpa, major)*:

#+BEGIN_SRC python
>>> import pprint as pp
>>> studs = [("Stan", 2.5, "ISyE"), ("Kyle", 2.2, "CS"),
...          ("Cartman", 2.4, "CmpE"), ("Kenny", 4.0, "ME")]
#+END_SRC

The default sort order is simply elementwise by the default order for each type in the tuple:

#+BEGIN_SRC python
>>> pp.pprint(sorted(studs))
[('Cartman', 2.4, 'CmpE'),
 ('Kenny', 4.0, 'ME'),
 ('Kyle', 2.2, 'CS'),
 ('Stan', 2.5, 'ISyE')]
#+END_SRC

Answer for yourself: what if two students had the same name?

** Sorting with a ~key~

If we want a different sort order, we can define a function that extracts the part of each tuple by which we want to sort.

#+BEGIN_SRC python
>>> def by_gpa(stud):
...     return stud[1]
...
>>> pp.pprint(sorted(studs, key=by_gpa))
[('Kyle', 2.2, 'CS'),
 ('Cartman', 2.4, 'CmpE'),
 ('Stan', 2.5, 'ISyE'),
 ('Kenny', 4.0, 'ME')]
#+END_SRC

~sorted~ is a *higher-order function* because it takes a function as an argument.

** Lambda Functions

The ~by_gpa~ function is pretty simple. Instead of defining a named function, we can define it inline with an anonymous function, a.k.a., a *lambda function*:

#+BEGIN_SRC python
>>> pp.pprint(sorted(studs, key=lambda t: t[1]))
[('Kyle', 2.2, 'CS'),
 ('Cartman', 2.4, 'CmpE'),
 ('Stan', 2.5, 'ISyE'),
 ('Kenny', 4.0, 'ME')]
#+END_SRC

The general form is ~lambda <parameter_list>: <expression>~

The body of a lambda function is limited to a single expression, which is implicitly returned.

** ~map~

Common task: build a sequence out of transformations of elements of an existing sequence. Here's the imperative approach:

#+BEGIN_SRC python
>>> houses = ["Stark", "Lannister", "Targaryen"]
>>> shout = []
>>> for house in houses:
...     shout.append(house.upper())
...
>>> shout
['STARK', 'LANNISTER', 'TARGARYEN']
#+END_SRC

Heres' the functional approach:

#+BEGIN_SRC python
>>> list(map(lambda house: house.upper(), houses))
['STARK', 'LANNISTER', 'TARGARYEN']
#+END_SRC
Note that ~map~ returns an iterator, so we pass it to the ~list~ constructor.

** ~filter~

#+BEGIN_SRC python
>>> nums = [0,1,2,3,4,5,6,7,8,9]
>>> filter(lambda x: x % 2 == 0, nums)
<filter object at 0x1013e87f0>
>>> list(filter(lambda x: x % 2 == 0, nums))
[0, 2, 4, 6, 8]
#+END_SRC

** List Comprehensions

A list comprehension iterates over a (optionally filtered) sequence,
applies an operation to each element, and collects the results of these
operations in a new list, just like ~map~.

#+BEGIN_SRC python
>>> grades = [100, 90, 0, 80]
>>> [x for x in grades]
[100, 90, 0, 80]
>>> [x + 10 for x in grades]
[110, 100, 10, 90]
#+END_SRC
We can also filter in a comprehension:

#+BEGIN_SRC python
>>> [x + 50 for x in grades if x < 50]
[50]
#+END_SRC

Comprehensions are more Pythonic than using ~map~ and ~filter~ directly.

** Dictionary Comprehensions

First, zip:

#+BEGIN_SRC python
words = ["Winter is coming", "Hear me roar", "Fire and blood"]
>>> list(zip(houses, words))
[('Stark', 'Winter is coming'), ('Lannister', 'Hear me roar'), ('Targaryen', 'Fire and blood')]
#+END_SRC

Dictionary comprehension using tuple unpacking:

#+BEGIN_SRC python
>>> house2words = {house: words for house, words in zip(houses, words)}
>>> house2words
{'Lannister': 'Hear me roar', 'Stark': 'Winter is coming', 'Targaryen': 'Fire and blood'}
#+END_SRC

Of course, we could just use the ~dict~ constructor on the ~zip~ object.

#+BEGIN_SRC python
>>> dict(zip(houses, words))
{'Lannister': 'Hear me roar', 'Stark': 'Winter is coming', 'Targaryen': 'Fire and blood'}
#+END_SRC


** ~reduce~

#+BEGIN_SRC python
>>> import functools
>>> functools.reduce(lambda x, y: x + y, [0,1,2,3,4,5,6,7,8,9])
45
#+END_SRC
Confirm this using the standard sum $\Sigma_{i=1}^{n} i = \frac{n(n + 1)}{2}$

Here's factorial:

#+BEGIN_SRC python
>>> functools.reduce(lambda x, y: x * y, [1,2,3,4,5])
120
>>> functools.reduce(lambda x, y: x * y, range(1,6))
120
#+END_SRC

** Generator Functions

You won't be tested on generator functions, but they're too cool not to show you!

#+BEGIN_SRC python
def class_dates(first, last, class_days):
    """Generate dates from first to last whose weekdays are in class_days

    >>> import datetime
    >>> begin = datetime.date(2016, 8, 22)
    >>> end = datetime.date(2016, 8, 25)
    >>> list(class_dates(begin, end, "TR"))
    [datetime.date(2016, 8, 23), datetime.date(2016, 8, 25)]
    """
    day = first
    # e.g., "MWF" => [0, 2, 4]
    class_day_ints = [i for i, letter in enumerate("MTWRFSU")
                           if letter in class_days]
    while day <= last:
        if day.weekday() in class_day_ints:
            yield day
        day += dt.timedelta(days=1)
#+END_SRC

** Exercise

Write comprehension expressions that build the data structures in the [[../exercises/grades.html][Grades]] exercise.
