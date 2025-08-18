---
template: course
title: Programming Assignment 0
---

# Programming Assignment 0

## Introduction

This assignment gets you started with the basic tools you will need to complete all of your programming assignments.  This project will


- ensure that you have correctly installed Python 3
- give you practice using a text editor to write Python programs, and
- give you practice running Python programs and using command line features.


## Problem Description

You are a CS 3642 student who needs to install Python, configure it for command line use, and learn how to use a programmer's text editor to create and edit Python source code.

## Solution Description

- Download and install Python 3 on your computer and configure your sytem so you can run Python from the command line. See the instructions on the class web site's Resources page.
- Download and install a programmer's text editor.  You may end up trying out several over the course of the semester before you settle on one. See the Text Editors guide on the class web site's Resources page.
- Create a directory for your CS 3642 coursework somewhere on your hard disk.  We suggest `cs3642`.  Note: avoid putting spaces in file and directory names, since doing so complicates the use of some command line tools.
- Create a `pa0` subdirectory of your CS 3642 coursework directory for your PA0 solution.

On Unix/BASH you can create both of these directories at once with

```sh
$ mkdir -p cs3642/pa0
```

Windows uses the same commands for directory navigation and creation, `cd` and `mkdir`, but Windows's `mkdir` command doesn't have the `-p` option.

Note: the `$` is the command prompt on most Unix shells and Windows 10's Ubuntu BASH shell (would be something like `C:\>` in Windows `cmd`), the text after it is what you enter.

- On the command line, go to the `pa0` directory you just created and enter these commands:

```sh
$ python3 --version > pa0-output.txt
```

`>` redirects the output of a program, in this case to the `pa0-output.txt` file. Important note: if the line above doesn't write your Python version to the `pa0-output.txt` file then replace the `>` with `2>` and try again. Some versions of Python, such as the one installed by Anaconda and miniconda, write the Python version to `stderr` instead of `stdout`. `>` redirects `stdout` and `2>` redirects `stderr`. For more informaiton,  [this blog post](http://www.jstorimer.com/blogs/workingwithcode/7766119-when-to-use-stderr-instead-of-stdout) has a nice discussion of the file descriptors `stdin`, `stdout` and `stderr`.

- Open your text editor, create a file in your newly created `pa0` directory named `nimbly_bimbly.py` and save the following Python program in the file:

```Python
print("\u004D\u0065\u006F\u0077 " * 9)
print("...")
print("\u004D\u0065\u006F\u0077\u0021")
```
- In your OS command shell, `cd` to your `pa0` directory and enter `python3 nimbly_bimbly.py` to run the program and see its output on the command line.
- Add the output of your program to `pa0-output.txt` by running\\
  `python3 nimbly_bimbly.py >> hw0-output.txt`. Don't forget the extra `>` in `>>`. `>>` appends to an existing file, a single `>` overwrites an existing file.


## Turn-in Procedure

Submit your `pa0-output.txt` file to the assignment on D2L.
