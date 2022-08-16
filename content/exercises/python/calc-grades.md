---
layout: exercise
title: Grades Report Exercise
---

# Calc Grades

## Introduction

In this assignment you will practice writing Python command-line utilities, file I/O, processing CSV files, and processing Python data structures.

## Problem Description

You're a teacher who needs to calculate final grades and get summary information on students in a class.

## Solution Description

Write a program called `calc_grades.py` that reads student item scores from a CSV file such as [super-grades.csv](super-grades.csv), writes a new CSV file with the same data as the input file with the following additional columns:

- average score for the student,
- letter grade based on grade cutoffs: A: 90, B: 80, C: 70, D: 60;

And an additional row at the end with "Averages" for the student name and the average for each graded item.

After writing the CSV file, the program should print to the console the number of As, Bs, Cs, Ds, and Fs, and the GPA for the class.

Your script should use command-line options `-i` for the input CSV file and `-o` for the output file.

### Sample Output

Given the input file [super-grades.csv](super-grades.csv), this is what running your program should look like:

```sh
$ python calc_grades.py -h
usage: calc_grades.py [-h] -i INFILE -o OUTFILE

Calculate course grades.

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --input-file INFILE
                        Input CSV file containing student names and item
                        scores.
  -o OUTFILE, --output-file OUTFILE
                        Output CSV file for score and grade calculations.
$ python calc_grades.py -i super-grades.csv -o final-grades.csv
Number of As: 3
Number of Bs: 0
Number of Cs: 1
Number of Ds: 1
Number of Fs: 1
Class GPA: 2.50
$ cat final-grades.csv
Student,Exam 1,Exam 2,Exam 3,Average,Grade
Thorny,100,90,80,90.00,A
Mac,88,99,111,99.33,A
Farva,45,56,67,56.00,F
Rabbit,59,61,67,62.33,D
Ursula,73,79,83,78.33,C
Foster,89,97,101,95.67,A
Averages,75.67,80.33,84.83,NA
```

## Tips and Considerations

- Some of this should be [familiar](grades.html).
- Use the Python [argparse](https://docs.python.org/3/howto/argparse.html) module to handle command-line options.

## Sample Solution

Don't peek until you've tried it yourself!

- [calc_grades.py](calc_grades.py)
