---
layout: "exercise"
title: "Language Dictionary"
---

# Language Dictionary

## Introduction

In this assignment you'll practice

- writing command-line tools, and
- working with dictionaries.

## Problem Description

You want to quickly look up word translations in foreign languges.

## Solution Description

Write a script that takes two command line arguments, a word and a target language, and prints the word from the target language that corresponds to the word provided.  Provide at least the following words, feel free to add your own:


| en          | de              | fr          |
|-------------|-----------------|-------------|
| good bye    | auf wiedersehen | au revoir   |
| hello       | guten tag       | bonjour     |
| to be:      | sein            | être        |
| to have:    | haben           | avoir       |
| to lose:    | verlieren       | perdre      |
| to love     | lieben          | aimer       |
| to practice | üben            | s'entraîner |
| to win      | gewinnen        | gagner      |

## Tips and Considerations

- The user doesn't specify the source language, so you need a way to determine the source language.
  - For a simple version of your language dictionary, you may assume that each word appears in only one languge.  For example, if you have a translation for the Engliish "bread" into the French "pain", you won't also have a translation for the English word "pain" into the French word "douleur."
  - For a challenge, you can allow identical words to appear in multiple languges.
