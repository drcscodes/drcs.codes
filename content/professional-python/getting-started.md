---
title: "Getting Started"
draft: false
layout: "course"
courseName: "Professional Python"
---

# Getting Started

These instructions are for installing the necessary tools and Python components for this course.  We use the Python.org distribution of Python, but if you already have another distribution, such as Anaconda, that will work fine as long as it includes Python >= 3.6, `pip`, and `venv`.

Jump to the section matching the operating system you will be using:

- [macOS](#macos)
- [Windows](#windows)
- [Ubuntu/WSL](#ubuntu-and-wsl2)

Then install

- [Git](/shared/git), and
- [IntelliJ or PyCharm](/shared/intellij).

You may also want to install a [text editor](/shared/text-editors).

## macOS

macOS is a Unix and already has a decent terminal and command-line shell.  There are two ways to install Python.org Python (as opposed to [Anaconda](https://www.anaconda.com/) Python or some other Python distribution):

1. Download and run the macOS installer from [python.org](https://www.python.org/).
2. Install [Homebrew](https://brew.sh/) and use the `brew` command to install Python.

   If you use macOS, I recommend using Homebrew to manage general Unix tools that aren't provided by Apple.  You may use `brew` to install Python, but if you are new to Homebrew you may find using the Python.org installer easier to manage.  A good general strategy is to use the installation method recommended by a tool's publisher.  For example, Python.org provides a package installer for Python, so use it to install Python.  [git-scm.org](https://git-scm.com/) recommends using Homebrew to install Git on macOS, so use Homebrew for Git.  With either of the installation methods above you don't need to install `pip` and `venv` separately.
   
   ```sh
   brew install python3
   ```
   
## Windows

1. Download the Windows installer from [python.org](https://www.python.org/).

   - **IMPORTANT**:On the first installer screen, be sure to check the box to update your PATH environment variable.


That's it.  Now you can run `python` and `pip` in the `cmd` shell or Powershell.  I recommend installing Windows Terminal: https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701, which is a very nice terminal and allows you to run any shell, in separate tabs if you want, including Linux shells.

   > Since many Unix/Linux distributions use Python 2 and Python 3 on the same system, `python` runs Python 2 and you must run Python 3 with `python3`.  On Windows, you run Python 3 with `python`.  Note that if you use the Linux version of Python 3 in WSL you'll need to run it with `python3` but use `python` when you're running Python 3 in a Windows shell like the `cmd` shell or PowerShell.

## Ubuntu and WSL2

If you are using Windows 10 or 11, install WSL2, the Windows Subsystem for Linux, Version 2.  WSL2 provides a very nice Linux environment, including a full Linux kernel and distribution of your choosing (I will use the latest Ubuntu in demonstrations).

> If you have trouble installing WSL2, you most likely need to update your Windows installation.  If you still have trouble, perhaps because you are prevented from updating your computer by an IT department, you can install the Windows version of Python and all the other tools used in this course using the instructions for Windows above.  Python is primarily a Linux/Unix technology, and knowledge of Linux is essential for most modern software development, so I recommend installing WSL2 and becoming familiar with Linux, but you will not miss anything in this course by running the Windows versions of Python and the other tools we'll use.

### Installing WSL2 

> See detailed instructions at https://docs.microsoft.com/en-us/windows/wsl/install-win10#simplified-installation-for-windows-insiders.  Note that Windows 10 with all updates from 2021-07-29 and later should support the simplified install.

1. Start PowerShell in admin mode by typing Windows+R, typing `powershell` in the text box, and running it with Ctrl-Enter.
   - You can also activate the Windows search menu by pressing the Windows key, typing `powershell` into the search box, and selecting "Run as admin" on the right.
2. On the PowerShell command line, enter `wsl --install`.  Accept the defaults to install the latest version of Ubuntu LTS.
3. Install Windows Terminal: https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701

Now you have WSL and a very nice terminal installed.  In a WSL Ubuntu terminal window, install the necessary Python tools with the commands below (each one on its own line):

```sh
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
```

If your system does not have Python 2 installed, you can make Python 3 "the" Python on your system.  You can determine whether Python 2 is installed by trying to run it:

```sh
python -V
```

If you get a message like "command not found" then Python 2 is not installed.  Make Python 3 "the" Python with:

```sh
sudo apt install python-is-python3
```

Now `python` and `python3` are the same and you don't have to remember to append `3` to Python commands.
