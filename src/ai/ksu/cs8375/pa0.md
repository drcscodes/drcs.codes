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

You are a CS 8375 student who needs to install Python, configure it for command line use, and learn how to use a programmer's text editor to create and edit Python source code.

## Solution Description

### Part 1: Python

- Download and install Python 3 on your computer and configure your sytem so you can run Python from the command line. See the instructions on the class web site's Resources page.
- Download and install a programmer's text editor.  You may end up trying out several over the course of the semester before you settle on one. See the Text Editors guide on the class web site's Resources page.
- Create a directory for your CS 8375 coursework somewhere on your hard disk.  We suggest `cs8375`.  Note: avoid putting spaces in file and directory names, since doing so complicates the use of some command line tools.
- Create a `pa0` subdirectory of your CS 8375 coursework directory for your PA0 solution.

On Unix/BASH you can create both of these directories at once with

```sh
$ mkdir -p cs8375/pa0
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
  `python3 nimbly_bimbly.py >> pa0-output.txt`. Don't forget the extra `>` in `>>`. `>>` appends to an existing file, a single `>` overwrites an existing file.

### Part 2: Libraries

AI software development, like most software development, relies on many packages outside the Python standard library.  In this part you will:

- create a virtual environment to keep project-specific dependencies separated from each other, and
- install a few essential and popular libraries for AI.

Follow these steps.  If you're not sure what's going on, see the [Background](#background) section below.

1. Create a virtual environment.  In your `pa0` directory, execute:

```sh
python3 -m venv venv
```

2. Activate your virtual environment.

On a Unix-like OS (e.g., Linux or macOS):
```shell
source venv/bin/activate
```

or in Windows PowerShell:
```shell
venv\bin\activate.ps1
```

3. Install essential and popular AI libraries.  First, download this [`requirements.txt`](../../requirements.txt) file to your `pa0` directory.  Then:

```sh
python3 -m pip install -r requirements.txt
```

4. List the installed packages in your venv and add it to the assignment output report.

```sh
python3 -m pip freeze >> pa0-output.txt
```

You'll notice that the output above differs from the `requirements.txt` file.

### <a id="background">Background</a>

#### Packages

There are two meanings for "package" in Python:

1. Subdirectories into which modules are organized.  See [Python's module documentation](https://docs.python.org/3/tutorial/modules.html#packages) for details.
2. A distribution of 3rd-party software, e.g., Python modules and supporting files, native code, etc.

Here we discuss the second meaning.

#### Installing Packages

The `pip3` command downloads and installs packages.

- Packages come from the [Python Package Index](https://pypi.org/) by default.
- `pip3` is quite flexible, allowing you to install from many kinds of sources. See the [Python package tutorial](https://packaging.python.org/en/latest/tutorials/installing-packages/) for details.

You can invoke `pip3` in two ways, for example, to install `ipython`:

```shell
python3 -m pip install ipython
```

or

```shell
pip3 install ipython
```

#### Virtual Environments

Different Python projects may use different versions of the same package.  To avoid conflicts, use virtual environments.

In the root directory of your Python project, create your virtual environment with:

```shell
python3 -m venv venv
```

This creates a virtual environment in the `venv` subdirectory of your project root directory.  Activate the virtual environment on macOS or Linux with:

```shell
source venv/bin/activate
```

or in Windows PowerShell (if this doesn't work, try `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.  See [venv docs](https://docs.python.org/3/library/venv.html) for details.):

```shell
venv\bin\activate.ps1
```

Deactivate  a virtual environment with (macOS, Linux, or Windows):

```shell
deactivate
```

#### Direnv

To make activating and deactivating easier, I recommend using [direnv](https://direnv.net/).

Put this content into a file called `.envrc` in your project root directory.

```
export VIRTUAL_ENV=venv
layout python3
```

Then give direnv permission to use the `.envrc` file to activate environments by entering the following shell command in your project root directory:

```shell
direnv allow .
```

No whenever you enter this directory, or a subdirectory within it, your Python venv will be activated, and whenever your enter a parent directory, it will be deactivated.

## Turn-in Procedure

Submit your `pa0-output.txt` file to the assignment on D2L.
