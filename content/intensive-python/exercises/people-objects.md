---
layout: exercise
title: Treating People as Objects
---

# Exercise: Treating People as Objects

## Introduction

In this exercise you will practice defining and using classes, and performing simple manipulations of collections of objects.

## Problem Description

You need to view some data about people in various ways.

## Solution Description

The [`people.py`](people.py) module has starter code that creates `Person` objects in a list `peeps`. In the [`people.py`](people.py) file:

- Write a `Person` class with:

  - an `__init__` method that takes:
    - a name (str),
    - a birthdate (str) formatted in [ISO 8601](http://www.iso.org/iso/home/standards/iso8601.htm) format,
    - a height in cm (int),
    - a weight in kilograms (float),
  - a `__repr__` method that returns a `str` like `<name, birthdate, height, weight>` field, e.g., `<Stan, 2008-08-13, 150cm, 45kg>`;
  - a `height_inches` method that returns the `Person` object's height in inches (1in = 2.54cm), and
  - a `weight_pounds` method that returns the `Person` object's weight in pounds (1kg = 2.2lb).
  - a `days_unitl` method that takes an age in years and returns the number of days until (or since, as a negative number) this Person turns `age` years old.

Do the following exercises to practice using `Person` objects:

- Write an expression that assigns to `avg_height` the average height of the `Person` objects in `peeps`.

- Write an expression that assigns to `avg_weight` the average weight of the `Person` objects in `peeps`.

  - Bonus: write a function, `avg_by`, that takes a sequence of `Person` objects and a `key` function specifying the attribute of `Person` objects to take the average of, similar to the `key` function of `sorted`.

- Write an expression that assigns to `name2height` a Dict[str, int] that maps `Person` names to their heights.

- Write an expression that assigns to `name2weight` a Dict[str, int] that maps `Person` names to their weights.

  - Bonus: write a function, `dict_builder`, that takes a list of ojects and a  `key_val` function that takes a single parameter that is an element of the list, and returns a tuple that becomes a key-value mapping in a dict returned by `dict_builder`.

- Write an expression that assigns to `peeps_by_age` a list of `Person` objects in `peeps` sorted in descending order by age.

- Write a loop that prints the names and ages until they turn 18 of all the `Person`s in `peeps`.

## Sample Answer

Don't peek until you've tried it yourself!

- [people_answers.py](people_answers.py)