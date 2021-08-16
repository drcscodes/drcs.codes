---
title: "Getting Started"
draft: false
layout: "single"
courseName: "Intensive Python"
---

# Getting Started

## Ubuntu/WSL2

If you are using Windows 10 or 11, install WSL2, the Windows Subsystem for Linux, Version 2.  WSL2 provides a very nice Linux environment, including a full Linux kernel and distribution of yoru choosing (I will use the latest Ubuntu in demonstrations).  You can install the Windows version of Python and all the other tools used in this course, but Python is primarily a Linux/Unix technology and all course demonstrations on Windows will use WSL2.

Install WSL2 (See detailed instructions at https://docs.microsoft.com/en-us/windows/wsl/install-win10#simplified-installation-for-windows-insiders.  Note that Windows 10 with all updates from 2021-07-29 and later should support the simplified install.)

1. Start PowerShell in admin mode by typing Windows+R, typing `powershell` in the text box, and running it with Ctrl-Enter.
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

## macOS

macOS is a Unix and already has a decent terminal and command-line shell.  There are two ways to install Python.org Python (as opposed to [Anaconda](https://www.anaconda.com/) Python or some other Python distribution).

1. Download the macOS installer from [python.org](https://www.python.org/).

or

2. Install [Homebrew](https://brew.sh/) and use Homebrew to install Python:

```sh
brew install python3
```

If you use macOS, I highly recommend using Homebrew to manage Unix tools in general.  With either of the installation methods above you don't need to install `pip` and `venv` separately.  Debian/Ubuntu packages tend to be more modular, which is nice for containerized applications.

## Text Editors and Other Tools

- [Text Editors for Programmers](/intensive-python/text-editors/)
