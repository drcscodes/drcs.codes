---
layout: exercise
title: Dog Module
---

# Dog Module

Write a module named `dog` which has a class named `Dog` with

- an instance variable named `name`
- an instance variable named `breed`
- a constructor/initializer that takes `name` and `breed` parameters and uses them to initialize the instance variables
- a string representation that prints the name and breed of the dog, e.g., `'Chloe the Doberman'`

When your `dog` module is run as a script, it should use the first two command line arguments to your script to pass as the name and breed in the construction of an instance of `Dog`, then print the `Dog` instance using the `print` function. When the `dog` module is imported as a module, it should not print anything. For example:

```sh
>>> import dog
>>> d = dog.Dog("Dante", "Deutscher Schäferhund")
>>> d
Dante the Deutscher Schäferhund
>>> quit()
$ python dog.py Chloe Doberman
Chloe the Doberman
```
