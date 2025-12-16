---
layout: exercise
title: Company Scraper
---

# Company Scraper

## Introduction

In this project you will practice

- web scraping, and
- writing CSV files.

## Problem Description

You need to process general information about many companies from many sectors. The only place you can consistently find this information is on the web.

## Solution Description

Write a script called `company_scraper.py` that scrapes data from SEC.gov's Edgar search engine to extract the name and address of each company in a list of companies contained in a text file, and saves the data in a single CSV file.

- The Edgar search results are in URLs such as `https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}`, where `{ticker}` is a company's ticker symbol.
- Use a list of ticker symbols contained in a file such as [tickers.txt](tickers.txt) or [dow-jones.txt](dow-jones.txt)
- Write the company's ticker, name, sector industrial code (SIC), sector name, address line 1, address line 2, city, state, and zip to a CSV file with a header line like:

  `Ticker,Name,SIC,Sector,Addr1,Addr2,City,State,Zip`

Your program should take the name of the tickers file as the first command line argument and the name for the CSV output file as its second command line argument. For example, if you have a list of tickers in the file named `tickers.txt`, then running your script would look like this:

```sh
$ python company_scraper.py tickers.txt company-data.csv
```

would produce a CSV file with these contents:

```
Ticker,Name,SIC,Sector,Addr1,Addr2,City,State,Zip
AAPL,APPLE INC,3571,ELECTRONIC COMPUTERS,ONE INFINITE LOOP,,CUPERTINO,CA,95014
BAC,BANK OF AMERICA CORP /DE/,6021,NATIONAL COMMERCIAL BANKS,BANK OF AMERICA CORPORATE CENTER,100 N TRYON ST,CHARLOTTE,NC,28255
C,CITIGROUP INC,6021,NATIONAL COMMERCIAL BANKS,388 GREENWICH STREET,,NEW YORK,NY,10013
CSCO,"CISCO SYSTEMS, INC.",3576,COMPUTER COMMUNICATIONS EQUIPMENT,170 WEST TASMAN DR,,SAN JOSE,CA,95134-1706
F,FORD MOTOR CO,3711,MOTOR VEHICLES & PASSENGER CAR BODIES,ONE AMERICAN RD,,DEARBORN,MI,48126
FB,Facebook Inc,7370,"SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING, ETC.",1601 WILLOW ROAD,,MENLO PARK,CA,94025
FCAU,Fiat Chrysler Automobiles N.V.,3711,MOTOR VEHICLES & PASSENGER CAR BODIES,25 ST. JAMES? STREET,,LONDON X0,SW1A,1HA
GM,General Motors Co,3711,MOTOR VEHICLES & PASSENGER CAR BODIES,300 RENAISSANCE CENTER,,DETROIT,MI,48265-3000
GOOG,Alphabet Inc.,7370,"SERVICES-COMPUTER PROGRAMMING, DATA PROCESSING, ETC.",1600 AMPHITHEATRE PARKWAY,,MOUNTAIN VIEW,CA,94043
JPM,JPMORGAN CHASE & CO,6021,NATIONAL COMMERCIAL BANKS,270 PARK AVENUE,,NEW YORK,NY,10017
ORCL,ORACLE CORP,7372,SERVICES-PREPACKAGED SOFTWARE,500 ORACLE PARKWAY,MAIL STOP 5 OP 7,REDWOOD CITY,CA,94065
WFC,WELLS FARGO & COMPANY/MN,6021,NATIONAL COMMERCIAL BANKS,420 MONTGOMERY STREET,,SAN FRANCISCO,CA,94163
```

## Tips and Considerations

- I'm not a finance expert, so if I've misconstrued some aspects of stocks, consider this assignment as practice in following specifications *as written* rather than using your own domain knowledge.
- Use Chrome's Developer Tools or Firefox's Firebug to help you find the HTML elements that contain the data.
- Most of the elements that contain the data have distinct class attribute values, so you can easily extract their text content with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (note that BeautifulSoup refers to elements as `tag`s).
- You'll need to use a regular expression to extract the sector name.
