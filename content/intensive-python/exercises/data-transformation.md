---
layout: exercise
title: Drill - Data Transformation
---

# Drill - Data Transformation

## Introduction

Drills are very short exercises designed to exercise the most basic building blocks of modules and programs.

## Problem Description

Data manipulation applications almost always include tranformation of data from one or more forms into other forms. In this drill you will practice transforming data stored in data structures into equivalent data stored in different data structures. Such transformations are often done to make the data easier to process for a particular application.

## Solution Description

```Python
names = ["Peter", "Lois", "Meg", "Chris", "Stewie", "Brian"]
ages = [41, 40, 16, 17, 1, 18]
```

Assume that the ages in `ages` correpond to the names in `names` by index. Write a Python module which:

- Assigns to the variable `family` a list of tuples in which the first element of each tuple is a name and the second element is the associated age.
- Assigns to the variable `name2age` a dictionary mapping names to ages.
- Assigns to the variable `sorted_family` the elements of `family` sorted by age.
- Assigns to the variable `adults` the members of `family` with an age of 18 or greater.
