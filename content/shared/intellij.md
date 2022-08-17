---
layout: exercise
title: IntelliJ
---

# IntelliJ/Pycharm

Almost all professional Java and Scala development teams use [IntelliJ IDEA](https://www.jetbrains.com/idea/), an IDE (integrated development environment) for Java and many other languages, including Python and Go.  Most professional Python programmers use PyCharm, or IntelliJ with the Python plugin, which is equivalent to PyCharm.  JetBrains has a well-earned reputation for making the best developer tools.  It is possible to get much of the same functionality with VS Code by installing several plugins, but the quality of the plugins is usually inferior.  Unfortunately, many OSS components are in a perpetual state of partial brokenness.

## Get Started

1. Get IntelliJ Ultimate Edition or PyCharm (if you're focused on Python, you may prefer PyCharm because it won't contain any distractions).
    - As a student or faculty member, you can get all of JetBrains's products free.  The easiest way is to visit [JetBrains's student license page](https://www.jetbrains.com/student/), click "APPLY NOW" and use your university email address.  You'll get an email within a few minutes with instructions on downloading the products in their "Product Pack for Students."

2. Install the Scala plugin in IntelliJ (Preferences -> Plugins).

3. [Learn IntelliJ](https://www.jetbrains.com/help/idea/)

## Add a Few Customizations

These are my personal modifications, which I find make IntelliJ more pleasant to use.

- Editor
  - General
    - Soft Wraps
      - Check "Use Soft Wraps in Editor"
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

## Keyboard Shortcuts

The more you keep your fingers on the keyboard, the faster you'll be.  Be sure to memorize a few basic shortcuts: https://www.jetbrains.com/help/idea/mastering-keyboard-shortcuts.html

And once you feel comfortable you can level-up with [IntelliJ IDEA Pro Tips](https://www.jetbrains.com/help/idea/pro-tips.html).

## Playing Nicely with Emacs

Emacs's keybindings are far different from modern applications, and many of these keybindings cause problems (e.g., M-w in Emacs copies the selection, but in macOS it closes the current window).  I tried Intellij's Emacs keymap and didn't like it.  It may be easier to simply modify Emacs's keybindings to match Intellij's.  Here are some Emacs config files to give you a start:

- For IntelliJ's macOS keymap: [intellij.el](intellij.el)

## Miscellaneous Tips

- Add [JetBrains's .gitignore items](https://raw.githubusercontent.com/github/gitignore/master/Global/JetBrains.gitignore) to your [.gitignore](https://git-scm.com/docs/gitignore) file.
