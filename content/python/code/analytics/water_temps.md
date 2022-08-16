# Water Temps

In a Python module named `water_temps.py`, load the data contained in the file `south-atlantic-water-temps.csv`, which is in the `code/analytics` subdirectory of the class web site repository (or download from GitHub: https://raw.githubusercontent.com/datamastery/datamastery.github.io/master/code/analytics/south-atlantic-water-temps.csv) into a Pandas DataFrame named `water_temps`. Use the first column in the data file as the index (row keys) for the data frame.

- Add a column to the `water_temps` DataFrame with the name `avg` and whose values are the average temperature for each location.

- Assign the variable `coldest_jan_temp` the value of the lowest temperature in JAN.

- Assign to the variable `warmest_nov` a Series with the Locations and associated NOV temperatures that are the highest (there will be two). You'll need to fiddle with this one.

After doing these steps you should have something like this (after `from water_temps import *`):

After loading the data, `water_temps` should look like this:

```Python
In [13]: pd.set_option('display.width', 120) # Display wider DataFrames without wrapping

In [67]: water_temps
Out[67]:
                       JAN  FEB  MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC        avg
Location
Chesapeake Bay VA       46   42   44   65   72   78   81   81   79   71   56   49  63.666667
Kiptopeke VA            36   39   46   65   72   78   81   81   79   71   54   44  62.166667
... additional rows elided

In [68]: coldest_jan_temp
Out[68]: 36

In [69]: warmest_nov
Out[69]:
Location
Miami Beach FL     76
Virginia Key FL    76
Name: NOV, dtype: int64
```

Submit your `water_temps.py` file to the quiz assignment on Canvas.
