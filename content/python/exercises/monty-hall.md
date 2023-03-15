---
layout: exercise
title: Monty Hall
---

# Monty Hall

In this exercise you will practice

- random number generation,
- writing loops,
- writing selection structures, and
- simple arithmetic computations.

## Problem Description

The [Monty Hall Problem](https://en.wikipedia.org/wiki/Monty_Hall_problem), based on a famous American TV game show, is a famous exercise in probabilistic thinking. You are shown three doors, behind one of which is a prize. You choose one of the three doors, and the host opens one of the other two doors after checking that it does not contain the prize. You may then choose

1. to stay with your initial choice, or
2. switch to the other unopened door.

The question: which strategy has the highest probability of winning? The answer is so counter-intuitive that even the famous mathematician [Paul Erdös](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s)[^1] had to be shown a [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) [computer simulation before he would believe it](https://www.google.com/books/edition/_/JAIU3iz_f3EC?hl=en&gbpv=1&pg=PA5&dq=which+door+has+the+cadillac).

## Solution Description

Write a program, `monty_hall.py`, that simulates 100 trials of the game described above where the player chooses stay, then 100 trials where the player chooses switch. Report the sum of the wins with each strategy, stay versus switch.

## Tips and Considerations

- You'll need the [random](https://docs.python.org/3/library/random.html) module.

[^1]: My [Erdös Number](https://en.wikipedia.org/wiki/Paul_Erd%C5%91s#Erd%C5%91s_number) is 5 (Charles Isbell -> David Roberts -> Fred Roberts -> [multiple](https://oakland.edu/enp/thedata/erdos2/) -> Paul Erdös)
