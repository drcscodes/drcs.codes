---
layout: single
title: Git
---

# Git

This guide provides a brief introduction to [Git](https://git-scm.com/) and [GitHub](https://github.com/)

## Installation

### Linux

You almost certainly have it already. If not,

Debian-based (like Ubuntu):
```sh
sudo apt-get install git
```

Red Hat-based (like Fedora):
```sh
sudo yum install git
```

Note: I haven't used Fedora in many years, so double check that.

### macOS

If you have a Mac, you must use [Homebrew](https://brew.sh/). Then installing git is easy:

```sh
brew install git
```

It's a good idea to update `brew` and your `brew` packages first:

```sh
brew update
brew upgrade
```

### Windows

Download the Git for Windows installer from [Git's official downloads page](https://git-scm.com/downloads) and run it. Then you'll also have `git-bash`, which gives you a Bash shell -- a superior alternative to `cmd` or Power[sic] Shell.

## Single-User Usage

```sh
git config --global user.name "Christopher Simpkins"
git config --global user.email chris.simpkins@gmail.com
git config --global core.editor emacs
```

## Git, GitLab and GitHub

Git is a distributed version control system. GitLab and GitHub are web applications that provide a nice web interface for remote repositories.

More to come ...
