---
layout: homework
title: Movies Part 2 - Analysis
---

# Movies Part 2 - Analysis

## Introduction

In this assignment you'll do some basic analysis of the data you created with your ETL pipeline from Part 1.

## General Instructions

**This is an individual assignment.**

Since this project counts for an exam grade you may not collaborate with your classmates.  You may discuss general concepts related to the assignment, such as how to use the Python libraries in general terms, but you may not discuss any specifics of this assignment with anyone other than the course instructor or the TAs.

Notes:

- Include a comment with your name, login ID, and GTID at the top of all Python files.
- *Do not wait until the last minute* to do this assignment in case you run into problems.
- Pay close attention to whether problems require you to print or return the results! Printing instead of returning or vice versa will result in a point deduction.
- Name all functions as specified in the instructions.
- Unless otherwise stated, you can assume inputs will be valid in this assignment (i.e. error checking is not required).
- In a Python module you must define a value (such as a function) before referencing it. So if you call function A from function B, the definition of function A must come before the definition of function B in the file.


## Problem Description

You work at a movie production company.  Your team has been given the task of creating risk and reward models for science fiction movie proposals.  You have created a CSV file of movie data and you want to do some rough exploratory analysis.

## Solution Description

Download the [`movies.csv`](movies.csv) created by your team's data engineers 

> NOTE: we will grade using the [`movies.csv`](movies.csv) we provide, which may differ slightly from the one your `movies_etl.py` script produced.  Hints below assume our [`movies.csv`](movies.csv).

Write a module in a file named `movies_analysis.py` which performs the following simple analyses:

1. (10 points) Read  [`movies.csv`](movies.csv) into a Pandas DataFrame named `movies` using the first column (tmdb_id) as the index column.
2. (10 points) Remove any movies which don't have revenue or budget data (value for `revenue` or `budget` column is 0).  Remember to assign back to your `movies` DataFrame. (Hint: I ended up with 483 movies.)
    - Use `DataFrame.drop` to delete rows. Pass to the `drop` method a list of row index values, which you could get by selecting the rows of `movies` that have 0 for `revenue` or `budget`.
3. (10 points) Add a column called `return` which contains the ratio of `revenue` to `budget` for each movie.
4. (10 points) Assign to `blockbusters` a DataFrame which contains all the movies with `revenue` greater than $1,000,000,000. (Hint: I got 13.)
5. (10 points) Assign to `highest_revenue` a DataFrame with the movies with the highest revenue.
6. (10 points) Assign to `highest_return` a DataFrame with the movies with the highest return.
7. (10 points) Assign to `losers` a DataFrame with all movies that lost money. (Hint: I got 120 losers.)
8. (10 points) Assign to `revenue_collection` a Series with the average revenue for movies that don't and do belong to a collection, i.e, two rows -- one for False and one for True.
9. (20 points -- this one isn't easy) Assign to `average_revenue_year` a Series whose indices are years and whose values are the average revenue for that year.
    - You'll need to use a `groupby` again but you'll need to transform the `release_date` into a year by `apply`ing a function (a lambda works nicely here) that returns the year portion of a release date.  Hint: `"2018-12-10".split("-")[0]` gives you `'2018'`.
 

Note: you would also do some plots to visualize your data, but we need to be able to autograde this assignment easily.  Feel free to play around.

### Running Your Script

Hard-code `movies.csv` as the name of the CSV file, which will be in the same directory as your module.  You will not get any credit for analyses that aren't stored in the exact variable names we specify above.  We will import your script as a module, so make all of the variables above global to your module.  Do not include any `print` statements in your module.

Here's how your module should work (I've abbreviated most results -- see `DataFrame.head`):

```
$ ipython
Python 3.7.1 (default, Oct 23 2018, 14:07:42) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import movies_analysis                                                                                                                              

In [2]: movies_analysis.movies.head()                                                                                                                       
Out[2]: 
           imdb_id                         title release_date  belongs_to_collection  runtime    budget    revenue     return
tmdb_id                                                                                                                      
861      tt0100802                  Total Recall   1990-06-01                  False    113.0  10000000  261317921  26.131792
196      tt0099088   Back to the Future Part III   1990-05-25                   True    118.0  40000000  244527583   6.113190
1498     tt0100758  Teenage Mutant Ninja Turtles   1990-03-30                   True     93.0  13500000  202000000  14.962963
1551     tt0099582                    Flatliners   1990-08-10                  False    115.0  26000000   61489265   2.364972
169      tt0100403                    Predator 2   1990-11-20                   True    108.0  35000000   57120318   1.632009

In [3]: movies_analysis.blockbusters.head(3)                                                                                                                
Out[3]: 
           imdb_id                           title release_date  belongs_to_collection  runtime     budget     revenue     return
tmdb_id                                                                                                                          
19995    tt0499549                          Avatar   2009-12-10                   True    162.0  237000000  2787965087  11.763566
38356    tt1399103  Transformers: Dark of the Moon   2011-06-28                   True    154.0  195000000  1123746996   5.762805
24428    tt0848228                    The Avengers   2012-04-25                   True    143.0  220000000  1519557910   6.907081

In [4]: movies_analysis.highest_revenue                                                                                                                     
Out[4]: 
           imdb_id   title release_date  belongs_to_collection  runtime     budget     revenue     return
tmdb_id                                                                                                  
19995    tt0499549  Avatar   2009-12-10                   True    162.0  237000000  2787965087  11.763566

In [5]: movies_analysis.highest_return                                                                                                                      
Out[5]: 
           imdb_id   title release_date  belongs_to_collection  runtime  budget  revenue  return
tmdb_id                                                                                         
14337    tt0390384  Primer   2005-06-02                  False     77.0    7000   424760   60.68

In [6]: movies_analysis.losers.head(3)                                                                                                                      
Out[6]: 
           imdb_id                 title release_date  belongs_to_collection  runtime    budget   revenue    return
tmdb_id                                                                                                            
2612     tt0100201           Mr. Destiny   1990-10-12                  False    110.0  20000000  15379253  0.768963
23535    tt0099277         Class of 1999   1990-04-01                   True     99.0   5200000   2459895  0.473057
3072     tt0099612  Frankenstein Unbound   1990-11-02                  False     82.0  11500000    334748  0.029109

In [7]: movies_analysis.revenue_collection                                                                                                                  
Out[7]: 
belongs_to_collection
False    1.169113e+08
True     3.355701e+08
Name: revenue, dtype: float64

In [8]: movies_analysis.average_revenue_year.head(3)                                                                                                            
Out[8]: 
release_date
1990    6.926583e+07
1991    5.728118e+07
1992    4.527236e+07
Name: revenue, dtype: float64
```

MAKE SURE YOU GET THE VARIABLE NAMES RIGHT!

Also, don't hard-code for the answers above.  First of all, most of them are truncated.  Second, we may use a CSV file with different data (which is easy to do).

## Turn-in Procedure

Submit your `movies_analysis.py` file on Canvas as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

## Verify the Success of Your Submission to Canvas

Practice safe submission! Verify that your HW files were truly submitted correctly, the upload was successful, and that your program runs with no syntax or runtime errors. It is solely your responsibility to turn in your homework and practice this safe submission safeguard.

- After submitting the files to Canvas, return to the Assignment menu option and this homework. It should show the submitted files.
- Download copies of your submitted files from the Canvas Assignment page **placing them in a new folder**.
- Re-run and test the files you downloaded from Canvas to make sure it's what you expect.
- This procedure helps guard against a few things.

    - It helps insure that you turn in the correct files.
    - It helps you realize if you omit a file or files.\footnote{Missing files will not be given any credit, and non-compiling homework solutions will receive few to zero points. Also recall that late homework will not be accepted regardless of excuse. Treat the due date with respect.  Do not wait until the last minute!
(If you do discover that you omitted a file, submit all of your files again, not just the missing one.)
    - Helps find syntax errors or runtime errors that you may have added after you last tested your code.
