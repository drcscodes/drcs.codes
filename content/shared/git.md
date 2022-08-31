---
layout: exercise
title: Git
---

# Git

This guide provides a brief introduction to [Git](https://git-scm.com/) and [GitHub](https://github.com/)

## Installation

### Linux

You almost certainly have it already. If not,

Debian-based (like Ubuntu):
```sh
sudo apt install git
```

Red Hat-based (like Fedora):
```sh
sudo yum install git
```

Note: I haven't used Fedora in many years, so double check that.

### macOS

If you have a Mac, I recommend [Homebrew](https://brew.sh/). Then installing git is easy:

```sh
brew install git
```

It's a good idea to update `brew` and your `brew` packages first:

```sh
brew update
brew upgrade
```

### Windows

Download the Git for Windows installer from [Git's official downloads page](https://git-scm.com/downloads) and run it. Then you'll also have `git-bash`, which gives you a Bash shell -- a superior alternative to `cmd` or PowerShell.

## Setting Up Git

You need to tell Git who you are and how you want to edit commit messages when committing from the command line and not using the `-m` option.

```sh
git config --global user.name "<your name>"
git config --global user.email <your email address>
git config --global core.editor vi
```

The following will also make working with remotes a bit smoother.

```sh
git config --global --add push.default current
git config --global --add push.autoSetupRemote true
```

## Git, GitLab and GitHub

Git is a distributed version control system. GitLab and GitHub are web applications that provide a nice web interface for remote repositories.  In many courses I demonstrate using GitHub to store course work.

### GitHub

> Note: if you are part of a company or school, you may have a private GitHub server.  For example, if you're a Georgia Tech faculty or student, you can go to [github.gatech.edu](https://github.gatech.edu/) and sign in with your GTID.

1. Go to [GitHub.com](https://github.com/) and sign up for an account.  It's free and you can even have private repositories using a free account.  Don't worry too much if you can't get the username you want -- you can always change it later (unfortunately, due to GitHub's popularity many usernames are taken, often by people who haven't even used GitHub in decades).

2. Click on your profile picture in the upper right corner and select "Settings" from the drop-down menu.

3. On your settings page, on the left side under "Access" select "SSH and GPG keys".

4. Under SSH keys follow the link to the guide to generating SSH keys and follow the instructions for [generating an SSH key pair and adding it to the SSH agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

5. After you have generated your SSH key pair and configured your computer to use it, follow the instructions for [adding a new SSH key to your account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).

After following the steps above you can clone repositories using SSH URLs which, together with the ssh-agent on your computer, relieves you from having to enter your username and password every time you push or pull from your GitHub repositories.

#### Creating a Repository

Since you will want to have a remote repository for collaboration and back-up purposes, the easiest way to create a repository is to create a repository on GitHub and clone it to your local computer (we refer to other computers, e.g. servers like GitHub, as "remote" and your computer as "local").  That way your local clone will already have the remote repository on GitHub set up as `origin`.

1. While logged in to GitHub, in the upper right-hand corner of the page next to your profile picture, click the "+" and select "New repository" from the drop-down menu.

2. On the Create a new repository page: 
    
   - Enter a Repository name (e.g., propython-coursework).
   - Select Public or Private.
   - Check the "Add a README file" checkbox.
   - Select an appropriate .gitignore template, e.g. "Python" if this repository will contain a Python project, "Go" for a Go project, etc.
   - Click the green "Create repository" button.

3. You should now be on the repository page for your new repository.  Click the green "Code" button, select "SSH" in the drop-down menu (assuming you have set up your SSH key), and the copy icon next to the clone URL, which should begin with `git@github.com`.

4. On your local computer, open your Terminal program (or `cmd` or `Powershell` on Windows), navigate to the directory that you want to be the **parent** of the directory holding your local repository clone, and enter `git clone <github-repository-url>`, where `<github-repository-url` is the clone URL you copied to the clipboard in the previous step.

   > Note: I use a common directory structure for clone repositories on all my computers.  I have a `vcs` directory, then a directory for each server which hosts clones, a directory for usernames/org-names matching the ones on the server, then the clones in those directories.  For example, for my `drcscodes` user's `propython-coursework` repository clone I would make the following directory structure and execute `git clone` as follows:
   
   ```shell
   ~/ $ mkdir -p vcs/github.com/drcscodes
   ~/ $ cd vcs/github.com/drcscodes
   ~/vcs/github.com/drcscodes $ git clone git@github.com:drcscodes/propython-coursework.git
   Cloning into 'propython-coursework'...
   ~/vcs/github.com/drcscodes $ cd propython-coursework
   ~/vcs/github.com/drcscodes/propython-coursework $ git remote -v
   origin	git@github.com:drcscodes/propython-coursework (fetch)
   origin	git@github.com:drcscodes/propython-coursework (push)
   ```

   After the commands above I'll have a `~/vcs/github.com/drcscodes/propython-coursework` directory which I can import into PyCharm as a new project.  You can follow the same steps, but substitute your own GitHub username and clone URLs.
