---
layout: exercise
title: Word Count
---

# Word Count

## Introduction

In this exercise you will practice

- reading text files, and
- using the collections framework.

## Problem Description

## Solution Description

Write a class called `WordCount` with

- a constructor that takes a `String` file name. The constructor should read the contents of the file and initialize a `wordCounts` instance variable which maps from `String` to `int`, where each `String` key is a word that occurs in the file and the corresponding `int` is the number of times the word appears in the file.
- a `getWords` method which returns a `Collection` of the words in the file (with no duplicates).
- a `getCount(String)` method which takes a `String` word and returns an `int` which is the number of times that word appears in the file.

The words should be normalized to lower case.

## Tips and Considerations

- Sample file: [I Have a Dream](i-have-a-dream.txt)
