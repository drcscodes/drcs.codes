#+TITLE: Data Structures
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

* Data Structures

** Built-in Data Structures

Values can be collected in data structures:

- Lists
- Tuples
- Dictionaries
- Sets

This lecture just an overview. See the [[https://docs.python.org/3.6/library/stdtypes.html][Python documentation]] for
complete details.

** Lists

A list is an indexed sequence of Python objects.

- Create a list with square brackets

#+BEGIN_SRC python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
#+END_SRC

- Create an empty list with empty square brackets or ~list()~ function

#+BEGIN_SRC python
>>> empty = []
>>> leer = list()
#+END_SRC

** Accessing List Elements

Individual list elements are accessed by index.

- First element at index 0

#+BEGIN_SRC python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> boys[0]
'Stan'
#+END_SRC

- Negative indexes offset from the end of the list backwards

#+BEGIN_SRC python
>>> boys[-1]
'Kenny'
#+END_SRC

- Lists are mutable, meaning you can add, delete, and modify elements

#+BEGIN_SRC python
>>> boys[2] = 'Eric'
>>> boys
['Stan', 'Kyle', 'Eric', 'Kenny']
#+END_SRC

** Lists are Heterogeneous

Normally you store elements of the same type in a list, but you can mix element types

#+BEGIN_SRC python
>>> mixed = [1, 'Two', 3.14]
>>> type(mixed[0])
<class 'int'>
>>> type(mixed[1])
<class 'str'>
>>> type(mixed[2])
<class 'float'>
#+END_SRC

- What's the length of the second element of ~mixed~ ?

** Creating Lists from Strings

- Create a list from a string with str's ~split()~ function:

#+BEGIN_SRC python
>>> grades_line = "90, 85, 92, 100"
>>> grades_line.split()
['90,', '85,', '92,', '100']
#+END_SRC

- By default ~split()~ uses whitespace to delimit elements. To use a different delimiter, pass as argument to ~split()~:

#+BEGIN_SRC python
>>> grades_line.split(',')
['90', ' 85', ' 92', ' 100']
#+END_SRC

- The ~list()~ function converts any iterable object (like sequences) to a list. Remember that strings are sequences of characters:

#+BEGIN_SRC python
>>> list('abcdefghijklmnopqrstuvwxyz')
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
'z']
#+END_SRC

- Use the ~split()~ method to separate an email address in to user name and host name.

** List Operators

The ~in~ operator tests for list membership. Can be negated with not:

#+BEGIN_SRC python
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> 'Kyle' in boys
True
>>> 'Kyle' not in boys
False
#+END_SRC

- The + operator concatenates two lists:

#+BEGIN_SRC python
>>> girls = ['Wendy', 'Annie', 'Bebe', 'Heidi']
>>> kids = boys + girls
>>> kids
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Wendy', 'Annie', 'Bebe', 'Heidi']
#+END_SRC

- The * operator repeats a list to produce a new list:

#+BEGIN_SRC python
>>> ['Ni'] * 5
['Ni', 'Ni', 'Ni', 'Ni', 'Ni']
#+END_SRC

** Functions on Lists

Python provides several built-in functions that take list parameters.

- ~len(xs)~ returns the number of elements in the list ~xs~ (more generally, the sequence ~xs~)

#+BEGIN_SRC python
>>> kids
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Wendy', 'Annie', 'Bebe', 'Heidi']
>>> len(kids)
8
#+END_SRC

- ~min(xs)~ returns the least element of ~xs~, ~max(xs)~ returns the greatest

#+BEGIN_SRC python
>>> min([8, 6, 7, 5, 3, 0, 9])
0
>>> max([8, 6, 7, 5, 3, 0, 9])
9
#+END_SRC

- What is ~min(kids)~?

** The ~del~ Statement

The ~del~ statement deletes variables.

- Each element of a list is a variable whose name is formed by indexing into the list with square brackets.

#+BEGIN_SRC python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Kenny']
>>> boys[3]
'Kenny'
#+END_SRC

- Like any variable, a list element can be deleted with ~del~

#+BEGIN_SRC python
>>> del boys[3]
>>> boys
['Stan', 'Kyle', 'Cartman'] # You killed Kenny!
#+END_SRC

- A list variable is a variable, so you can delete the whole list

#+BEGIN_SRC python
>>> del boys
>>> boys
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'boys' is not defined
#+END_SRC

** List Methods

Methods are invoked on an object (an instance of a class) by appending a dot, ~.~, and the method name.

- ~xs.count(x)~: number of occurences of ~x~ in the sequence ~xs~

#+BEGIN_SRC python
>>> surfin_bird = "Bird bird bird b-bird's the word".split()
>>> surfin_bird
['Bird', 'bird', 'bird', "b-bird's", 'the', 'word']
>>> surfin_bird.count('bird')
2
#+END_SRC

- ~xs.append(x)~ adds the single element ~x~ to the end of ~xs~

#+BEGIN_SRC python
>>> boys.append('Butters')
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Butters']
s.extend(t) adds the elements of t to the end of s
>>> boys.extend(['Tweak', 'Jimmy'])
>>> boys
['Stan', 'Kyle', 'Cartman', 'Kenny', 'Butters', 'Tweak', 'Jimmy']
#+END_SRC

** List Methods

- ~xs.remove(x)~ removes the first occurrence of ~x~ in ~xs~, or raises a ~ValueError~ if ~x~ is not in ~xs~

#+BEGIN_SRC python
>>> boys.remove('Kenny')
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Jimmy']
>>> boys.remove('Professor Chaos')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
#+END_SRC

- ~xs.pop()~ removes and returns the last element of the list

#+BEGIN_SRC python
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Jimmy']
>>> boys.pop()
'Jimmy'
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
#+END_SRC

** Slicing

Slicing lists works just like slicing strings (they're both sequences)

- Take the first two elements:

#+BEGIN_SRC python
>>> boys = ['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
>>> boys[0:2]
['Stan', 'Kyle']
#+END_SRC

- Take every second element, starting with the first:

#+BEGIN_SRC python
>>> boys[::2]
['Stan', 'Cartman', 'Tweak']
>>> boys[0:5:2] # same as above
['Stan', 'Cartman', 'Tweak']
#+END_SRC

- Take the second from the end:

#+BEGIN_SRC python
>>> boys[-2]
'Butters'
#+END_SRC

Note that slice operations return new lists.

- What's the value of ~boys[-1:1]~ ?
- What's the value of ~boys[-1:1:-1]~ ?
- What's the value of ~boys[::-1]~ ?

** Aliases

Aliasing occurs when two or more variables reference the same object

- Assignment from a variable creates an alias

#+BEGIN_SRC python
>>> brats = boys
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak']
#+END_SRC

Now boys and brats are aliases.

- Changes to one are reflected in the other, becuase they reference the same object

#+BEGIN_SRC python
>>> brats.append('Timmy')
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
#+END_SRC

** Copies

Operators create copies

#+BEGIN_SRC python
>>> brats + ['Bebe', 'Wendy']
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy', 'Bebe',
'Wendy']
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
#+END_SRC

You have to reassign to the list to make an update:

#+BEGIN_SRC python
>>> brats = brats + ['Bebe', 'Wendy'] # could also use shortcut +=
>>> brats
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy', 'Bebe',
'Wendy']
#+END_SRC

Notice that after the reassignment, ~brats~ is no longer an alias of ~boys~

#+BEGIN_SRC python
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
#+END_SRC

** Slicing Creates Copies (Usually)

- Slice on the right hand side of an assignment creates a copy:

#+BEGIN_SRC python
>>> first_two = boys[:2]
>>> first_two
['Stan', 'Kyle']
>>> first_two[0] = 'Stan the man'
>>> first_two
['Stan the man', 'Kyle']
>>> boys
['Stan', 'Kyle', 'Cartman', 'Butters', 'Tweak', 'Timmy']
#+END_SRC

- Slices on the left hand side allow for flexible assignment

#+BEGIN_SRC python
>>> boys[0:2] = ['Randy', 'Sharon', 'Gerald', 'Sheila']
>>> boys
['Randy', 'Sharon', 'Gerald', 'Sheila', 'Cartman', 'Butters',
'Tweak', 'Timmy']
#+END_SRC

** A Few More List Operations

You can combine the elements of a list to form a string with ~str~'s ~join()~ method.

#+BEGIN_SRC python
>>> aretha = ['R', 'E', 'S', 'P', 'E', 'C', 'T']
>>> "-".join(aretha)
'R-E-S-P-E-C-T'
#+END_SRC

~sorted()~ function returns a new list

#+BEGIN_SRC python
>>> sorted(aretha)
['C', 'E', 'E', 'P', 'R', 'S', 'T']
>>> aretha # Notice original is unchanged
['R', 'E', 'S', 'P', 'E', 'C', 'T']
#+END_SRC

~sort()~ method modifies the list it is invoked on

#+BEGIN_SRC python
>>> aretha.sort()
>>> aretha
['C', 'E', 'E', 'P', 'R', 'S', 'T']
#+END_SRC

** Example: Grades

Start with a list representing a line from a gradebook file

#+BEGIN_SRC python
>>> grades_line = ['Chris', 100, 90, 95]
>>> grades_line
['Chris', 100, 90, 95]
#+END_SRC

Get the sublist containing just the grades by slicing

#+BEGIN_SRC python
>>> grades = grades_line[1:]
>>> grades
[100, 90, 95]
#+END_SRC

Sum the grades using Python's built-in ~sum()~ function

#+BEGIN_SRC python
>>> sum(grades)
285
#+END_SRC

- And get the average by dividing by the number of grades

#+BEGIN_SRC python
>>> sum(grades) / len(grades)
95.0
#+END_SRC

** Tuples

Tuples are like lists, but are immutable.

#+BEGIN_SRC python
Tuples are created by separating objects with commas
>>> pair = 1, 2
>>> pair
(1, 2)
#+END_SRC

Tuples can be used in assignments to "unpack" a sequence

#+BEGIN_SRC python
>>> a, b = [1, 2]
>>> a
1
>>> b
2
#+END_SRC

Tuple assignment can be used to swap values

#+BEGIN_SRC python
>>> b, a = a, b
>>> a, b
(2, 1)
#+END_SRC

** Dictionaries

A dictionary is a map from keys to values.

Create dictionaries with ~{}~

#+BEGIN_SRC python
>>> capitals = {}
#+END_SRC

Add key-value pairs with assignment operator

#+BEGIN_SRC python
>>> capitals['Georgia'] = 'Atlanta'
>>> capitals['Alabama'] = 'Montgomery'
>>> capitals
{'Georgia': 'Altanta', 'Alabama': 'Montgomery'}
#+END_SRC

Keys are unique, so assignment to same key updates mapping

#+BEGIN_SRC python
>>> capitals['Alabama'] = 'Birmingham'
>>> capitals
{'Georgia': 'Altanta', 'Alabama': 'Birmingham'}
#+END_SRC

** Dictionary Operations

Remove a key-value mapping with ~del~ statement

#+BEGIN_SRC python
>>> del capitals['Alabama']
>>> capitals
{'Georgia': 'Atlanta'}
#+END_SRC

Use the ~in~ operator to test for existence of key (not value)

#+BEGIN_SRC python
>>> 'Georgia' in capitals
True
>>> 'Atlanta' in capitals
False
#+END_SRC

Extend a dictionary with ~update()~ method, get values as a list
with values method

#+BEGIN_SRC python
>>> capitals.update({'Tennessee': 'Nashville', 'Mississippi':
'Jackson'})
>>> capitals.values()
dict_values(['Jackson', 'Nashville', 'Atlanta'])
#+END_SRC

** Conversions to ~dict~

Any sequence of two-element sequences can be converted to a ~dict~

A list of two-element lists:

#+BEGIN_SRC python
>>> dict([[1, 1], [2, 4], [3, 9], [4, 16]])
{1: 1, 2: 4, 3: 9, 4: 16}
#+END_SRC

A list of two-element tuples:


#+BEGIN_SRC python
>>> dict([('Lassie', 'Collie'), ('Rin Tin Tin', 'German
Shepherd')])
{'Rin Tin Tin': 'German Shepherd', 'Lassie': 'Collie'}
#+END_SRC

Even a list of two-character strings:

#+BEGIN_SRC python
>>> dict(['a1', 'a2', 'b3', 'b4'])
{'b': '4', 'a': '2'}
#+END_SRC

Notice that subsequent pairs overwrote previously set keys.

** Sets

Sets have no duplicates, like the keys of a ~dict~. They can be iterated
over (we'll learn that later) but can't be accessed by index.

- Create an empty set with ~set()~ function, add elements with ~add()~ method

#+BEGIN_SRC python
>>> names = set()
>>> names.add('Ally')
>>> names.add('Sally')
>>> names.add('Mally')
>>> names.add('Ally')
>>> names
{'Ally', 'Mally', 'Sally'}
#+END_SRC

- Converting to set a convenient way to remove duplicates

#+BEGIN_SRC python
>>> set([1,2,3,4,3,2,1])
{1, 2, 3, 4}
#+END_SRC

** Set Operations

Intersection (elements in ~a~ *and* ~b~)

#+BEGIN_SRC python
>>> a = {1, 2}
>>> b = {2, 3}
>>> a & b # or a.intersetion(b)
{2}
#+END_SRC

Union (elements in ~a~ *or* ~b~)

#+BEGIN_SRC python
>>> a | b # or a.union(b)
{1, 2, 3}
#+END_SRC

** Set Operations

Difference (elements in ~a~ that are not in ~b~)

#+BEGIN_SRC python
>>> a - b # or a.difference(b)
{1}
#+END_SRC

Symmetric difference (elements in ~a~ or ~b~ but not both)

#+BEGIN_SRC python
>>> a ^ b # or a.symmetric_difference(b)
{1, 3}
#+END_SRC

** Set Predicates

A predicate function asks a question with a ~True~ or ~False~ answer.

Subset of:

#+BEGIN_SRC python
>>>a <= b # or a.issubset(b)
False
#+END_SRC

Proper subset of:

#+BEGIN_SRC python
>>> a < b
False
#+END_SRC

** Set Predicates

Superset of:

#+BEGIN_SRC python
>>> a >= b # or a.issuperset(b)
False
#+END_SRC

Proper superset of:

#+BEGIN_SRC python
>>> a > b
False
#+END_SRC

** Closing Thoughts

Typical Python programs make extensive use of built-in data structures and often combine them (lists of lists, dictionaries of lists, etc)

- These are just the basics
- Explore these data structures on your own
- Read the books and Python documentation


This is a small taste of the expressive power and syntactic
convenience of Python's data structures.
