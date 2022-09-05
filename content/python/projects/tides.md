---
layout: exercise
title: Tides
---

# Tides

## Introduction

In this assignment you will practice writing Python command-line utilities, obtaining data, file I/O, processing CSV files, and using Python's `datetime` module.

## Problem Description

You are a scuba diving instructor who plans [dive trips](http://proscuba.training/trips.html) to West Palm Beach, FL that include dives at the world famous Blue Heron Bridge. The Blue Heron Bridge is a shore dive that is best done at slack high tide, so planning is essential.

## Solution Description

Write a Python script that accepts command line arguments specifying time windows and days of the week, reads the NOAA tide tables to find high tides that occur on those days and during those time windows, and displays these days and tides to the user on the console.

Your program will use annual tide tables for the Port of Palm Beach (StationId: 8722588) stored in a CSV file, which you can download from [NOAA's Tides and Currents Service](https://tidesandcurrents.noaa.gov/noaatideannual.html?id=8722588).  The current year should be pre-selected and you'll need to choose "TXT" under Format.

If the user supplies less than the required minimum of four command-line arguments, display a usage message such as:

```
Usage:
   find_tides.py tides-file begin-window end-window *days
Where:
   tides-file is the name of a NOAA tide tables TXT file
   begin-window is the earliest acceptable high tide in HH:MM {AM|PM}
   begin-window is the latest acceptable high tide
   *days is one or more days on which to check, in three-letter format
Example:
   find_tides.py wpb-tides-2015.txt '09:30 AM' '11:00 AM' Fri Sat Sun
finds all Fridays, Saturdays, and Sundays on which there is a high
tide between 9:30am and 11:00am in the wpb-tides-2015.txt file
```

A successful run of the program will look something like this:

```
$ python find_tides.py wpb-tides-2016.txt '10:00 AM' '11:00 AM' Sat Sun
2016/03/12	Sat	10:39 AM	2.9		88		H
2016/03/26	Sat	10:57 AM	2.4		73		H
2016/04/09	Sat	10:28 AM	3.1		94		H
2016/04/24	Sun	10:28 AM	2.4		73		H
2016/05/08	Sun	10:09 AM	3.0		91		H
2016/08/20	Sat	10:21 AM	3.4		104		H
2016/09/03	Sat	10:20 AM	3.4		104		H
2016/09/18	Sun	10:01 AM	4.1		125		H
2016/12/03	Sat	10:36 AM	3.2		98		H
2016/12/17	Sat	10:43 AM	3.4		104		H
```


## Tips and Considerations

- Load the NOAA tide table TXT file into your text editor to study its format and content.
- You'll need to ignore/skip the header lines at the top of the NOAA tide table TXT file.
- Take note of the delimiter used in the NOAA annual tide table TXT file.
- You'll want to use [Python's datetime module](https://docs.python.org/3/library/datetime.html), in particular you'll find [datetime.strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime) useful.
- Since the NOAA annual tide table TXT file contains lines with human-readable information, reporting tides to the user is a simple matter of printing lines that match the constraints given by the user on the command line, as in the example above.
