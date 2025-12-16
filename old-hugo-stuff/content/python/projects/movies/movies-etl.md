---
layout: homework
title: Movies Part 1 - ETL
---

# Movies Part 1 - ETL

## Introduction

In this assignment you'll create and execute an ETL pipeline for movie data.

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

You work at a movie production company.  Your team has been given the task of creating a risk and reward models for science fiction movie proposals.  As a junior data scientist on the team, you have been given the task of creating a CSV data set which can be easily loaded into a data frame for analysis.

## Solution Description

Write a script called `movies_etl.py` which performs the ETL portion of an analytics pipeline (details in the sections below). Data analytics pipelines are typically organized in distinct phases (which are often subdivided into smaller steps):

1. *Extract* data from sources such as databases, web sites, sensors, etc.
2. *Transform* data into a usable form by filling in missing data, normalizing data, cleaning mislabelled data, etc.
3. *Load* data into a form that can be read by analytics tools, such as a database or data exchange format like CSV.
4. Explore ...
5. Model ...
6. Predict ...
7. Present ...

This assignment focuses on the first three major steps, which are often called "ETL" for short.  You will collect information from [The Movie DB](https://www.themoviedb.org/), transform the data into a usable form (sometimes by collecting additional data form other sources) and load the data into a CSV file that can be easily read by Pandas in Part 2. 

### Step 1: Extract Movie Data

First you'll need an account at [The Movie DB](https://www.themoviedb.org/), then apply for an API key on the [API settings page](https://www.themoviedb.org/settings/api) (you'll need to be logged in to your account to apply for an API key).

#### Get movie data from TMDB

1. Get a list of the TMDB ids of the 20 top grossing science fiction movies **from the United States** for each year from 1990 to 2018 (that's 580 movies) using the [discover API](https://www.themoviedb.org/documentation/api/discover).  The discover API will give you paginated results, that is, pages of 20 results each.  Get the first page of 20 results for each year, and be sure to pass the parameter which gives you results sorted by revenue in descending order.  A result from the discover API will look like this, from which you'll extract the `id`s:

```json
{'page': 1,
 'results': [{'adult': False,
              'backdrop_path': '/lmZFxXgJE3vgrciwuDib0N8CfQo.jpg',
              'genre_ids': [12, 878, 28, 14],
              'id': 299536,
              'original_language': 'en',
              'original_title': 'Avengers: Infinity War',
              'overview': 'As the Avengers and their allies have continued to '
                          'protect the world from threats too large for any '
                          'one hero to handle, a new danger has emerged from '
                          'the cosmic shadows: Thanos. A despot of '
                          'intergalactic infamy, his goal is to collect all '
                          'six Infinity Stones, artifacts of unimaginable '
                          'power, and use them to inflict his twisted will on '
                          'all of reality. Everything the Avengers have fought '
                          'for has led up to this moment - the fate of Earth '
                          'and existence itself has never been more uncertain.',
              'popularity': 127.094,
              'poster_path': '/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg',
              'release_date': '2018-04-25',
              'title': 'Avengers: Infinity War',
              'video': False,
              'vote_average': 8.3,
              'vote_count': 9499},
             {'adult': False,
              'backdrop_path': '/b6ZJZHUdMEFECvGiDpJjlfUWela.jpg',
              'genre_ids': [28, 12, 14, 878],
              'id': 284054,
              'original_language': 'en',
              'original_title': 'Black Panther',
              'overview': "King T'Challa returns home from America to the "
                          'reclusive, technologically advanced African nation '
                          "of Wakanda to serve as his country's new leader. "
                          "However, T'Challa soon finds that he is challenged "
                          'for the throne by factions within his own country '
                          'as well as without. Using powers reserved to '
                          "Wakandan kings, T'Challa assumes the Black Panther "
                          'mantel to join with girlfriend Nakia, the '
                          'queen-mother, his princess-kid sister, members of '
                          "the Dora Milaje (the Wakandan 'special forces') and "
                          'an American secret agent, to prevent Wakanda from '
                          'being dragged into a world war.',
              'popularity': 50.64,
              'poster_path': '/uxzzxijgPIY7slzFvMotPv8wjKA.jpg',
              'release_date': '2018-02-13',
              'title': 'Black Panther',
              'video': False,
              'vote_average': 7.3,
              'vote_count': 9086},
... 18 additional movies elided
```

2. Because the discover API doesn't give you all the data you want, you'll need to make a call to the [movie details API](https://developers.themoviedb.org/3/movies/get-movie-details) for each movie. A call to the movie details API for the first movie in the list above will give you:

```json
{'adult': False,
 'backdrop_path': '/lmZFxXgJE3vgrciwuDib0N8CfQo.jpg',
 'belongs_to_collection': {'backdrop_path': '/zuW6fOiusv4X9nnW3paHGfXcSll.jpg',
                           'id': 86311,
                           'name': 'The Avengers Collection',
                           'poster_path': '/qJawKUQcIBha507UahUlX0keOT7.jpg'},
 'budget': 300000000,
 'genres': [{'id': 12, 'name': 'Adventure'},
            {'id': 878, 'name': 'Science Fiction'},
            {'id': 28, 'name': 'Action'},
            {'id': 14, 'name': 'Fantasy'}],
 'homepage': 'http://marvel.com/movies/movie/223/avengers_infinity_war_part_1',
 'id': 299536,
 'imdb_id': 'tt4154756',
 'original_language': 'en',
 'original_title': 'Avengers: Infinity War',
 'overview': 'As the Avengers and their allies have continued to protect the '
             'world from threats too large for any one hero to handle, a new '
             'danger has emerged from the cosmic shadows: Thanos. A despot of '
             'intergalactic infamy, his goal is to collect all six Infinity '
             'Stones, artifacts of unimaginable power, and use them to inflict '
             'his twisted will on all of reality. Everything the Avengers have '
             'fought for has led up to this moment - the fate of Earth and '
             'existence itself has never been more uncertain.',
 'popularity': 127.094,
 'poster_path': '/7WsyChQLEftFiDOVTGkv3hFpyyt.jpg',
 'production_companies': [{'id': 420,
                           'logo_path': '/hUzeosd33nzE5MCNsZxCGEKTXaQ.png',
                           'name': 'Marvel Studios',
                           'origin_country': 'US'}],
 'production_countries': [{'iso_3166_1': 'US',
                           'name': 'United States of America'}],
 'release_date': '2018-04-25',
 'revenue': 2046239637,
 'runtime': 149,
 'spoken_languages': [{'iso_639_1': 'en', 'name': 'English'}],
 'status': 'Released',
 'tagline': 'An entire universe. Once and for all.',
 'title': 'Avengers: Infinity War',
 'video': False,
 'vote_average': 8.3,
 'vote_count': 9499}
```

### Step 2: Transform Movie Data

It's usually necessary to clean the extracted data, which may include filling in missing data, fixing mislabelled data, and normalizing data.  Here's we'll gain experience filling in missing data by triangulating with another source.

There are three movies which don't have `runtime` values in The Movie DB.  Use data from [IMDB Datasets](https://www.imdb.com/interfaces/) to fill in those missing runtimes.  You may assume that the [IMDB Datasets](https://www.imdb.com/interfaces/) are in the same directory as your script.

**NOTE: read the gzipped version of the IMDB dataset file using [Python's gzip module](https://docs.python.org/3/library/gzip.html).**

### Step 3: Load Movie Data

Create a cleanly-formatted CSV file with the following header:

```
tmdb_id,imdb_id,title,release_date,belongs_to_collection,runtime,budget,revenue
```

- `tmdb_id` -- the Movie DB id of the movie
- `imdb_id` -- the IMDB id of the movie
- `title` -- the title of the movie
- `release_date` -- the release date of the movie in ISO 8601 format, YYYY-MM-DD
- `belongs_to_collection` - `True` if move is part of a collection, `False` otherwise
- `runtime` -- runtime of the movie in minutes
- `budget` -- budget of the movie, in dollars
- `revenue` -- gross revenue for the movie, in dollars

The first few lines of your `movies.csv` output should look something like this:

```
tmdb_id,imdb_id,title,release_date,belongs_to_collection,runtime,budget,revenue
861,tt0100802,Total Recall,1990-06-01,False,113,10000000,261317921
196,tt0099088,Back to the Future Part III,1990-05-25,True,118,40000000,244527583
1498,tt0100758,Teenage Mutant Ninja Turtles,1990-03-30,True,93,13500000,202000000
1551,tt0099582,Flatliners,1990-08-10,False,115,26000000,61489265
169,tt0100403,Predator 2,1990-11-20,True,108,35000000,57120318
9556,tt0099365,Darkman,1990-08-24,True,96,16000000,48878502
5549,tt0100502,RoboCop 2,1990-06-22,True,117,35000000,45681173
2612,tt0100201,Mr. Destiny,1990-10-12,False,110,20000000,15379253
34086,tt0100666,Spaced Invaders,1990-04-27,False,100,3000000,15369573
19384,tt0099817,Dark Angel,1990-01-26,False,91,7000000,9229401
11309,tt0099740,Hardware,1990-09-14,False,93,1500000,5728953
23535,tt0099277,Class of 1999,1990-04-01,True,99,5200000,2459895
3072,tt0099612,Frankenstein Unbound,1990-11-02,False,82,11500000,334748
27274,tt0099611,Frankenhooker,1990-06-01,False,85,2500000,205068
192074,tt0098996,Aftershock,1990-10-05,False,91,0,0
530,tt0104361,A Grand Day Out,1990-05-18,True,23,0,0
18317,tt0103129,Truly Madly Deeply,1990-11-10,False,106,0,0
30647,tt0098962,12:01 PM,1990-01-01,False,25,0,0
545334,tt0099864,Stephen King's It,1990-11-18,False,180,0,0
218650,tt0099853,Invasion of the Space Preachers,1990-01-01,False,100,100000,0
280,tt0103064,Terminator 2: Judgment Day,1991-07-03,True,137,102000000,520000000
174,tt0102975,Star Trek VI: The Undiscovered Country,1991-12-05,True,113,27000000,96900000
```

### Running Your Script

**IMPORTANT**: your script should cache data so that you aren't making 610 web service API calls each time you run your script, and your script should report what it's doing.  You should save cached results in two JSON files whose names encode the TMDB genre id, years, sort order and kind of data in the file:

- `878-1990-2018-revenue.desc-ids.json` -- a list of movie ids.
- `878-1990-2018-revenue.desc-details.json` -- a list of dictionaries containing the results of a call to the [movie details API](https://developers.themoviedb.org/3/movies/get-movie-details) for each of the ids in the `-ids.json` file described above.

The first time you run your script it will take several minutes and write the following to the console:

```
$ python movies_etl.py YOUR_TMDB_API_KEY
Loading movie ids from themoviedb.org, saving in 878-1990-2018-revenue.desc-ids.json.
Loading movie details from themoviedb.org, saving in 878-1990-2018-revenue.desc-details.json.
Writing data to movies.csv
```

The second time you run your script it should take only a few seconds because of the cache files produced above and write the following to the console:

```
$ python movies_etl.py YOUR_TMDB_API_KEY
Loading movie ids from 878-1990-2018-revenue.desc-ids.json.
Loading movie details from 878-1990-2018-revenue.desc-details.json.
Writing data to movies.csv
```

## Tips and Considerations


- We recommend you use the [requests](http://docs.python-requests.org/en/master/) library for web service API interaction.
- The root TMDB API URL is `https://api.themoviedb.org/3`. Add `/discover/movie` for the discover API or `/movie/{movie_id}` for the movie details API.
- When you're creating requests URLs, watch for double slashes (`//`) in your URLs, such as `https://api.themoviedb.org/3//movie/603`.
- You should only get movies from the `US`. Look at the [Discover (Movies) API docs](https://developers.themoviedb.org/3/discover/movie-discover) to see the simple way to limit your results to moves from a particular region.
- If you get results like `{"status_code": 25, "status_message": "Your request count (41) is over the allowed limit of 40."}` then you need to ensure that you are sleeping for 10 seconds every 40 requests to comply with TMDB's [request rate limiting](https://developers.themoviedb.org/3/getting-started/request-rate-limiting).  See [`time.sleep`](https://docs.python.org/3/library/time.html#time.sleep).
  - You may also notice this effect by seeing 40 results in your CSV output or getting `KeyError`s when you're writing your CSV files.
  - Delete your `-details.json` file to re-download movie details if you get any of the above status messages in your cache file.
  - Becuase you're only making 30 requests with the discover API, you shouldn't hit this limit in that part of your script.

## Grading

This rubric is designed to give you many opportunities for partial credit and to make it easy to grade.  To the extend possible, rubric items are independent.

- (5 points) `moves_etl.py` takes API key as argument
- (5 points) `moves_etl.py` runs without producing run-time error
- (5 points) `moves_etl.py` produces `878-1990-2018-revenue.desc-ids.json` file on first run
- (5 points) `moves_etl.py` produces `878-1990-2018-revenue.desc-details.json` file on first run
- (5 points) `moves_etl.py` uses `878-1990-2018-revenue.desc-ids.json` without making web API calls on subsequent runs
- (5 points) `moves_etl.py` uses `878-1990-2018-revenue.desc-details.json` without making web API calls on subsequent runs
- (5 points) `moves_etl.py` produces '`movies.csv` file
- (5 points) `movies.csv` contains correct header
- (5 points) `movies.csv` contains 580 movie records
- (5 points) `movies.csv` contains 20 movies for each year in [1990,2018]
- (5 points) `movies.csv` contains at least 10 of the top 20 grossing sci-fi movies for each year in [1990,2018]
- (5 points) `tmdb_id`s are correct TMDB ids
- (5 points) `imdb_id`s, when present, are correct IMDB ids
- (5 points) `title`s are all present and correct titles
- (5 points) `release_date`s are all present and correct
- (5 points) `belongs_to_collection`s are all present and correct
- (10 points) `runtime`s are all present and correct (by IMDB, if applicable)
- (5 points) `budget`s are of correct form when present
- (5 points) `revenue`s are of correct form when present

To give you some idea of your progress, here is a "sanity check": [movies_etl_sanity_check.py](movies_etl_sanity_check.py).  After you generate your `movies.csv` file, run this script in the same directory to see if you have the right header and at least 10 of the top 20 movies from each year.  If your output agrees with mine you'll get:

```
$ python movies_etl_sanity_check.py 
Probable lost points:
- 0: contains correct header
- 0: contains at least 10 of the top 20 grossing sci-fi movies for each year in [1990,2018]
```

But since we may get slightly different results depending on when we run our scripts, you could get this and still get a 100% (which is why we're only looking for 10 of the top 20 in each year to agree):
```
$ python movies_etl_sanity_check.py 
1 missing ids for 1995 : {'92698'}
1 missing ids for 2018 : {'465136'}
Probable lost points:
- 0: contains correct header
- 0: contains at least 10 of the top 20 grossing sci-fi movies for each year in [1990,2018]
```

## Turn-in Procedure

Submit your `movies_etl.py` file on Canvas as an attachment.  When you're ready, double-check that you have submitted and not just saved a draft.

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
