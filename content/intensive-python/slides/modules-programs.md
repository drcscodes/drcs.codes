#+TITLE: Modules and Programs
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

* Modules and Programs

** Python Programs

Python code organized in

- modules,
- packages, and
- scripts.

We've already used some modules, now we'll learn what they are, how
they're orgainized in packages, and how to write Python programs that
can be run on their own, not just entered in the Python command shell.

** Importing Modules

~import~ing a module means getting names from the module into scope. When you import a module, you can access the modules components with the dot operator as in the previous example.

#+BEGIN_SRC python
>>> import math
>>> math.sqrt(64)
8.0
#+END_SRC

You can also import a module and give it an alias: import <module> as <local-name>

#+BEGIN_SRC python
>>> import math as m
>>> m.sqrt(64)
8.0
#+END_SRC

** Importing into Local Scope

Remember that importing brings names into the scope of the import.
Here we import the math module into one function.

#+BEGIN_SRC python
>>> def hypotenuse(a, b):
...     import math
...     return math.sqrt(a*a + b*b)
...
>>> hypotenuse(3, 4)
5.0
>>> math.sqrt(64)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
#+END_SRC

** Importing Names from a Module

You can choose to import only certain names from a module:

#+BEGIN_SRC python
>>> from math import sqrt
>>> sqrt(64)
8.0
>>> floor(1.2)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'floor' is not defined
#+END_SRC

Or all names from a module:

#+BEGIN_SRC python
>>> from math import *
>>> floor(1.2)
1
>>> sin(0)
0.0
>>> sin(.5 * pi)
1.0
#+END_SRC

Notice that with this syntax you don't have to use a fully-qualified
name, e.g., ~module.name~

** Module Search Path

Just as an operating system command shell searches for executable programs by searching the directories listed in the ~PATH~ environment variable, Python finds modules by searching directories. The module search path is stored in ~sys.path~:

#+BEGIN_SRC python
>>> import sys
>>> from pprint import pprint
>>> pprint(sys.path)
['',
 '/home/chris/miniconda3/lib/python35.zip',
 '/home/chris/miniconda3/lib/python3.5',
 '/home/chris/miniconda3/lib/python3.5/plat-linux',
 '/home/chris/miniconda3/lib/python3.5/lib-dynload',
 '/home/chris/miniconda3/lib/python3.5/site-packages',
 '/home/chris/miniconda3/lib/python3.5/site-packages/setuptools-23.0.0-py3.5.egg']
#+END_SRC

Notice that the current directory, represented by the ~''~ at the beginning of the search path.

Also, note use of ~pprint~.

** Python Scripts

Take a look at the draw.py file. Notice the if statement at the bottom:

#+BEGIN_SRC python
# Is this the main (top-level) module?
if __name__ == '__main__':
    stand()
    head()
    body()
    leftarm()
    rightarm()
    leftleg()
    rightleg()
    # Pause so the user can see the drawing before exiting.
    input('Press any key to exit.')
#+END_SRC

This makes the module a runnable Python program. It's similar to the main function or method from some other programming languages. With it we can import the file as a module to use its functions (or objects or variables), or run it from the command line.

** Shebang!

Another way to run a Python program (on Unix) is to tell the host operating system how to run it. We do that with a "shebang" line at the beginning of a Python program:

#+BEGIN_SRC python
#!/usr/bin/env python3
#+END_SRC

This line says "run python3 and pass this file as an argument." So if you have a program called foo with shebang line as above and which has been set executable (chmod +x foo.py), thse are equivalent:

#+BEGIN_SRC python
$ python3 foo.py
$ ./foo.py
#+END_SRC

** Interactive Programs

The input() function Python reads all the characters typed into the console until the user presses ENTER and returns them as a string:

#+BEGIN_SRC python
>>> x = input()
abcdefg1234567
>>> x
'abcdefg1234567'
#+END_SRC

We can also supply a prompt for the user:

#+BEGIN_SRC python
>>> input('Give me a number: ')
Give me a number: 3
'3'
#+END_SRC

And remember, input() returns a string that may need to be converted.

#+BEGIN_SRC python
>>> 2 * int(input("Give me a number and I'll double it: "))
Give me a number and I'll double it: 3
6
#+END_SRC

** Command Line Arguments

#+ATTR_LaTeX: height=3in
[[file:Argument_Clinic.png]]

#+BEGIN_SRC python
$ python args.py one 2 two + one
#+END_SRC

The ~python~ invocation above contains 6 command line arguments.

** Command-line Arguments in Python

When you run a Python program, Python collects the arguments to the
program in a variable called sys.argv. Given a Python program
(~arguments.py~):

#+BEGIN_SRC python
#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("You've given me nothing to work with.")
else:
    print(sys.argv[1] +"? Well I disagree!")
#+END_SRC

#+BEGIN_SRC python
$ ./arguments.py Pickles
Pickles? Well I disagree!
$ ./arguments.py
You've given me nothing to work with.
#+END_SRC

** Conclusion

[[https://www.youtube.com/embed/kQFKtI6gn9Y][Python Arguments]]
