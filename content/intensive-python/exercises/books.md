---
layout: exercise
title: Books XML Exercise
---

# Books

## Introduction

In this assignment you will practice writing Python command-line utilities, file I/O, processing XML files, and using Python data structures.

## Problem Description

You're developing a book selling web site. You receive book data in XML format, like [`books.xml`](books.xml), and produce various reports about the books you sell.

## Solution Description

Write a module called `books.py` with the following functions:

```Python
def titles(books):
    """Extract the titles the books XML node and return them in a list.

    Parameters:
    books: xml.etree.ElementTree books node

    Return:
    list[str] -- all the authors of the books in the books node
    """
```

```Python
def book_authors(books):
    """Return a dictonary the authors of the books in the books XML node.

    Parameters:
    books: xml.etree.ElementTree books node

    Return:
    dict[str, list[str]] -- dictionary mapping book titles to lists of of the books'
                            authors
    """
```

```Python
def authors_book(books):
    """Return a dictonary the books written by the authors in the books XML node.

    Parameters:
    books: xml.etree.ElementTree books node

    Return:
    dict[str, list[str]] -- dictionary mapping authors to lists of of their books
    """

```

Use the functions above and the [`books.xml`](books.xml) file to do things like:

- List the titles of all the books written by George R.R. Martin
- List the titles of all the books written by a single author
- List the titles of all the books written by more than one author
- List the names of all the authors who have written more than one book
- List the names of all books cauthored by two given authors
