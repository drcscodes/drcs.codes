---
layout: exercise
title: Water Temps Analysis
---

# Water Temperatures Analysis

## Introduction

This is a short exercise to give you some practice with NumPy and Pandas.

## Solution Description

In a Python module named `water_temps.py`, load the data contained in the file [`south-atlantic-water-temps.csv`](south-atlantic-water-temps.csv) into a Pandas DataFrame named `water_temps`. Use the first column in the data file as the index (row keys) for the data frame.

- Add a column to the `water_temps` DataFrame with the name `AVG` and whose values are the average temperature for each location.

- Add a row to the `water_temps` DataFrame named `Average` whose values contain the average temperatures for each month.

- Assign the variable `coldest_jan_temp` the value of the lowest temperature in JAN.

- Assign to the variable `warmest_nov` a Series with the Locations and associated NOV temperatures that are the highest (there will be two). You'll need to fiddle with this one.

- Assign to the variable `warm_spots` a DataFrame with all the rows from `water_temps` whose average water emperatures are greater than 70.

After doing these steps you should have something like this (after `from water_temps import *`):

```Python
In [12]: from water_temps import *

In [13]: pd.set_option('display.width', 120) # Display wider DataFrames without wrapping

In [14]: water_temps
Out[14]:
                       JAN  FEB  MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC        AVG
Location
Chesapeake Bay VA       46   42   44   65   72   78   81   81   79   71   56   49  63.666667
Kiptopeke VA            36   39   46   65   72   78   81   81   79   71   54   44  62.166667
... additional rows elided

In [15]: coldest_jan_temp
Out[15]: 36

In [16]: warmest_nov
Out[16]:
Location
Miami Beach FL     76
Virginia Key FL    76
Name: NOV, dtype: int64

In [19]: warm_spots
Out[19]: 
                  JAN  FEB  MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC        AVG
Location                                                                               
Daytona Beach FL   61   59   65   65   72   78   81   81   79   71   71   65  70.666667
Miami Beach FL     71   73   75   65   72   78   81   81   79   71   76   73  74.583333
Stuart Beach FL    67   66   70   65   72   78   81   81   79   71   75   70  72.916667
Virginia Key FL    71   72   74   65   72   78   81   81   79   71   76   73  74.416667
```
