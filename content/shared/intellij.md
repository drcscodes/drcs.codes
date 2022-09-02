---
layout: exercise
title: IntelliJ
---

# IntelliJ/Pycharm

Almost all professional Java and Scala development teams use [IntelliJ IDEA](https://www.jetbrains.com/idea/), an IDE (integrated development environment) for Java and many other languages, including Python and Go.  Most professional Python programmers use PyCharm, or IntelliJ with the Python plugin, which is equivalent to [PyCharm](https://www.jetbrains.com/pycharm).  JetBrains has a well-earned reputation for making the best developer tools.  It is possible to get much of the same functionality with VS Code by installing several plugins, but the quality of the plugins is usually inferior.  Unfortunately, many OSS components are in a perpetual state of partial brokenness.

## Get Started

1. Get [IntelliJ IDEA](https://www.jetbrains.com/idea/) Ultimate or [PyCharm](https://www.jetbrains.com/pycharm) Professional (if you're focused on Python, you may prefer PyCharm because it won't contain any distractions).
    - As a student or faculty member, you can get all of JetBrains's products free.  The easiest way is to visit [JetBrains's student license page](https://www.jetbrains.com/student/), click "APPLY NOW" and use your university email address.  You'll get an email within a few minutes with instructions on downloading the products in their "Product Pack for Students."

2. If you're using IntelliJ, install the appropriate plugins, e.g., Python, Go, Java (in IntelliJ, go to Preferences -> Plugins).

3. Learn [IntelliJ](https://www.jetbrains.com/help/idea/) or [PyCharm](https://www.jetbrains.com/help/pycharm/).

## Customize

1. Create a command-line launcher by clicking Tools | Create Command-line Launcher....  Then you'll be able to launch IntelliJ from a command line with `idea` or PyCharm with `charm`.
   - You can open IntelliJ or PyCharm for any project by navigating to the project's root directory in your OS command shell and typing `idea .` or `charm .`
   - You can use Light Edit mode by invoking IntelliJ or PyCharm with `idea -e` or `charm -e`.  Light Edit mode runs the IDE without plugins, but with all the basic editing, formatting and syntax-aware features.  It's nice for edits of configuration files and other files that don't belong to an IntelliJ or PyCharm project.

2. Add a few customizations.  These are my personal modifications, which I find make IntelliJ more pleasant to use.  Go to IntelliJ | Preferences ... (File | Preferences ... on Windows or Linux) and:

- Editor
  - General
    - Soft Wraps
      - Check "Soft wrap these files:" and enter `*` in the box
        - This will prevent you from ever needing to scroll horizontally.  You can always toggle soft wraps for a particular file in your editor with View | Active Editor | Soft-Wrap.
    - Virtual Space
      - Uncheck all
    - On Save
      - Remove trailing spaces on exit - All
      - Uncheck "Keep trailing spaces on caret line"
      - Check "Remove trailing blank lines at the end of saved files"
      - Check "Ensure every saved file ends with a line break"
  - Smart Keys
    - Uncheck "Insert paired brackets (), [], <>"
    - Uncheck "Insert pair quote"
    - Check "Surround selection on typing quote or brace"
  - Code Style
    - Hard wrap at 80 columns
      - Leave Wrap on Typing unchecked
    - Visual guides: 80, 100
  - Inlay Hints
    - Uncheck the ones that annoy you

- Keymap (Note: these are macOS-specific.)
  - Main Menu
    - File
      - Open...: **CTRL-CMD-O**
  - Plugins
    - Terminal
      - Open in Terminal: **CTRL-F12**

## Keyboard Shortcuts

The more you keep your fingers on the keyboard, the faster you'll be.  Here are some shortcuts that I commit to memory (many of these are explained in [Discover IntelliJ IDEA](https://www.jetbrains.com/help/idea/discover-intellij-idea.html).

> Note: for many commands, especially "switching" commands, adding a SHIFT reverses the direction.

Here are a few shortcuts that I commit to memory.

**macOS**

- File|Open: **CTRL-CMD-O**
  > You can open any file or directory, so you can actually use IntelliJ as a general-purpose text editor.  To open an IDEA project, open the project root directory (e.g., directory with a `.idea` subdirectory).
- File|New|File: ***CTRL-CMD-N***
- Switch between open projects: **CMD-`** (Window|Next Project Window)
- Goto/Toggle Project Pane: **CMD-1**
- Goto Editor: **ESC**
- Open in Terminal: **CTRL-F12**
- Goto/Toggle Terminal: **OPT-F12**
- Switch between open files or tool windows: **CTRL-TAB**
- Find Action: **SHIFT-OPT-A** (for when you don't know a key-binding)

And once you feel comfortable you can level-up with [IntelliJ IDEA Pro Tips](https://www.jetbrains.com/help/idea/pro-tips.html).

## Miscellaneous Tips

- Add [JetBrains's .gitignore items](https://raw.githubusercontent.com/github/gitignore/master/Global/JetBrains.gitignore) to your [.gitignore](https://git-scm.com/docs/gitignore) file(s).
