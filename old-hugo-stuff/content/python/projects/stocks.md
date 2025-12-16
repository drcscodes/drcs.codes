---
layout: exercise
title: Stocks
---

# Stocks

## Introduction

In this project you will practice

- writing classes,
- reading CSV files,
- using control structures, and
- manipulating data structures.

## Problem Description

You need to process daily stock prices that are stored in CSV files. Each stock is stored in a CSV file named after the stock's ticker symbol. For example, the stock prices for Alphabet, Inc are stored in a file named `GOOG.csv`.

## Solution Description

Write a module named `stocks` that includes two classes:

- `Company` with the following instance attributes:

  - `symbol`: `str` -- the official stock ticker symbol
  - `name`: `str` -- the company's name
  - `sector`: `str` -- the company's sector, as defined by [Yahoo Finance](https://finance.yahoo.com/industries)
  - `stock_data`: `dict[datetime, StockData]` -- a dictionary mapping [`datetime`](https://docs.python.org/3/library/datetime.html#datetime-objects) objects to `StockData` objects

  and the following instance methods:

  - `__init__` -- which takes arguments that are used to initialize the values of the instance attribute listed above (except `stock_data`), in the order listed above. Only the `symbol` must be provided when creating a `Company` instance, the other instance attributes (except `stock_data`) should have the value `None` if not provided as arguments to `__init__` when creating a `Company` object.

  - a method which is automatically called whenever a `Company` object is printed or converted to a `str` and returns a string with the company's name and stock symbol in parentheses, e.g., `Alphabet (GOOG)`

  - a method which is automatically called by the Python REPL to print the value of a `Company` object to the console and returns a string with the class name and all the attributes (except `stock_data`) between angle brackets, e.g., `<Company: name=Alphabet, symbol=GOOG, sector=Technology>`

  - `performance` -- which takes an optional start date and optional end date and returns the percentage return (as a `float`, e.g., 20% is .20, 120% is 1.20) from the open price on the start date to the adjusted closing price on the end date, i.e., if you multiply the open price on the start date by the value returned by this function and add that result to the open price on the start date, you get the adjusted closing price on the end date. Dates should be [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) objects with date components but no time components.

    - If the start date is not in `stock_data`, use the next date after the specified start date for which there is data.
    - If the start date is not provided, use the first date in `stock_data`.
    - If the end date is not in `stock_data`, use the last date before the specified end date for which there is data.
    - If the end date is not provided, use the last date in `stock_data`.

- `StockData` with the following instance attributes to store the data found in a record in a stock data CSV file:

  - `open_price`: `float`
  - `high`: `float`
  - `low`: `float`
  - `close`: `float`
  - `adj_close`: `float`
  - `volume`: `int`

  and an instance method that makes instances of `StockData` comparable to each other using the `<` operator based on the values of their `adj_close` attributes.

Finally, your `stocks` module should be runnable as a script that takes three command line arguments: a company's stock symbol, a start date, and an end date.

- The stock symbol, e.g., `GOOG` is required.
- Start date and end date are optional. If either is not supplied, follow the directions for the `Company.performance` method above. Note that if you supply only one date, it's the start date. You can't specify an end date but no start date. Date should be in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (see examples below).

Your script should:

- create a `Company` object with the symbol but no company name or sector,
- read a CSV file in its working directory which is named after the stock symbol (with a .csv ending),
- use the data in the CSV file to populate the `Company` object's `stock_data` dictionary,
- use the `Company` object's `performance` method to find the requested stock return, and
- print a report as in the examples below. Note that the performance reported by the scrip t should be in percentage format, not a `float` as returned by `Company.performance`.

Your `stocks` module not perform any of the script actions listed above when imported as a module.

Your program should work with CSV files formatted and named like the ones you can download from Yahoo Finace, e.g., [Alphabet, Inc historical data](https://finance.yahoo.com/quote/GOOG/history?p=GOOG). For your convenience you may use the following files: [AAPL.csv](../../data/AAPL.csv), [BAC.csv](../../data/BAC.csv), [C.csv](../../data/C.csv), [CSCO.csv](../../data/CSCO.csv), [F.csv](../../data/F.csv), [FB.csv](../../data/FB.csv), [FCAU.csv](../../data/FCAU.csv), [GM.csv](../../data/GM.csv), [GOOG.csv](../../data/GOOG.csv), [JPM.csv](../../data/JPM.csv), [ORCL.csv](../../data/ORCL.csv), [WFC.csv](../../data/WFC.csv).

Here are some sample program runs:

```sh
$ python stocks.py GOOG
Stock performance of None (GOOG) from 2004-08-19 to 2017-09-21: 1777.0%.
$ python stocks.py GOOG 2017-01-01
Stock performance of None (GOOG) from 2017-01-01 to 2017-09-21: 19.7%.
$ python stocks.py GOOG 2015-01-01 2017-09-21
Stock performance of None (GOOG) from 2015-01-01 to 2017-09-21: 77.2%.
```

## Tips and Considerations

- I'm not a finance expert, so if I've misconstrued some aspects of stocks, consider this assignment as practice in following specifications _as written_ rather than using your own domain knowledge.
- You'll want to use [Python's datetime module](https://docs.python.org/3/library/datetime.html), in particular you'll find [datetime.strptime](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime) useful.
