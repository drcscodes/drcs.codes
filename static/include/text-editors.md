# Introduction to Text Editors for Young Programmers

Text is the raw material of the craft of programming.  You should become good at manipulating text.  The first thing you should do is pick a good cross-platform text editor and learn it well.  If you haven't already done so, this guide will help you choose one.  The next thing you should do is learn regular expressions, and the next thing after that is learn UNIX and one of its command shells, probably bash.

## Choosing a text editor

![http://xkcd.com/378/](http://imgs.xkcd.com/comics/real_programmers.png)


I used [Emacs](http://www.gnu.org/software/emacs/) for years, then tried [Sublime Text](http://www.sublimetext.com/) and [Atom](https://atom.io/) for class demonstrations, then switched back to Emacs.  I've also tried [Vim](http://www.vim.org/) and know basic vi, but nothing beats Emacs.  Now I use [VS Code](https://code.visualstudio.com/).  Emacs is more powerful, but using VS Code eliminates a great deal of friction due to its massive support network, and it's what most of my students will use.

If you're going to be a software engineer, you should learn basic [Vi(m)](http://www.vim.org/), because it is small, can be used in a terminal and is available on every UNIX platform, Windows, and Mac. [Emacs](http://www.gnu.org/software/emacs/) is the most powerful editor in existence, but it has a steep learning curve.

### **Recommendation for new programmers**: [VS Code](https://code.visualstudio.com/)

## TABS Versus Spaces

![https://www.emacswiki.org/emacs/TabsSpacesBoth](../images/TabsSpacesBoth.png)

Never use TABs in source code.  Always indent with spaces.  The traditional meaning of TAB is to move the cursor to the next multiple of tab width (8 by the Java spec).  If you adopt, as most programming teams do, the convention of using spaces for all indentation and alignment (no TAB characters anywhere), then "tabbing" means inserting the required number of spaces to get to a multiple of tab width.  Since the Java code convention doesn't specify whether TAB characters or spaces are used for indentation, and that indentation should be 4 spaces, and that tabs be set every 8 spaces, it allows for an absurd case where a programmer using a feature-poor editor would be forced to hit the space bar 4 times when indenting to the first level of indentation.  Of course modern editors take care of these sorts of details, but most programmers completely eschew TAB characters to avoid such issues and to ensure that code looks consistent in any editor or display no matter how the tabs are set.  And most programmers set their editors to insert spaces for tabs.  Jamie Zawinski, a famous Emacs, Mozilla and Netscape hacker, has an informative write-up here: [http://www.jwz.org/doc/tabs-vs-spaces.html](http://www.jwz.org/doc/tabs-vs-spaces.html)

> Note: There are some language standards, such as Go's, that specify TABs for indentation.  Always follow your team or community standards, so in Go use TABs.  Most language will have style guides and standard formatting tools so you don't even have to think about it.

## Customizing your text editor

Having a go-to text editor improves your productivity in part because you can set up your editor with your preferred defaults.  Customization is important because many text editors and IDEs are configured with bad defaults.  Good programmers insist on writing code that is clear and consistently formatted.  Having a well-configured text editor helps you do that. At a minimum you should configure your text editor to:

- Indent with spaces instead of TABs
- Set indent (tab) width to 4
- Trim trailing white space at the end of lines
- Add a newline character to the end of files


Here is a minimal starter configuration for VS Code.  To open settings, type Ctrl+, on Windows/Linux, or Cmd-, on macOS.

```json
{
    "editor.wordWrap": "on",
    "editor.minimap.enabled": false,
    "editor.rulers": [
        80,
        100
    ],
    "files.trimTrailingWhitespace": true,
    "files.insertFinalNewline": true,
    "editor.autoClosingBrackets": "never",
    "editor.autoClosingQuotes": "never",
    "workbench.settings.editor": "json",
    "workbench.settings.useSplitJSON": true,
    // Controls tree indentation in pixels.
    "workbench.tree.indent": 16,
}
```
