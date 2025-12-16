---
layout: exercise
title: Email Utilities
---

# Email Utilites

In this exercise you will practice:

- string manipulation,
- string methods,
- simple boolean expressions, and
- writing functions.

## Introduction

Emails are of the form <username>@<server-name>.  For example, `bob@aol.com` means there is a `bob` user account on the `aol.com` server.  Email address are case insensitive, so `Liger@SweetAnimals.com` is the same as `liger@sweetanimals.com`.  (This is a bit of a simplification, but fits our purpose here.)

## Problem Description

You need to extract user names and server names from email addresses, and compare two emails to determine if they are the same.

## Solution Description

Write three functions:

- `extract_username` which takes an email address `str` and returns the username portion
- `extract_server` which takes an email address `str` and returns the server portion
- `is_same` which takes two email address `str`s and returns the `True` if they are the same, `False` otherwise

### Sample Output

```sh
>>> extract_username('bob@aol.com')
'bob'
>>extract_server('bob@aol.com')
'aol.com'
>>> is_same('Liger@SweetAnimals.com', 'LIGER@SWEETANIMALS.COM')
True
>>> is_same('Liger@SweetAnimals.com', 'LION@SWEETANIMALS.COM')
False
```
