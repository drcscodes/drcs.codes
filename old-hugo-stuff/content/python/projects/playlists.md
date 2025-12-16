---
layout: exercise
title: Playlists
---

# Playlists

## Introduction

In this assignment you will practice data transfer techniques such as
- reading [CSV](https://docs.python.org/3/library/csv.html) files,
- using data structures,
- creating [JSON](https://docs.python.org/3/library/json.html) files, and
- using os tools.

## Problem Description

You have a list of songs in a comma-separated values file and you want to publish it as a playlist to a site that supports the JSPF JSON format for sharing playlists.

## Solution Description

Write a Python program in a file named `csv2jspf.py` that reads a CSV file containing song information and writes the song information to a playlist file in [JSPF](https://www.xspf.org/jspf) JSON format.

### Part 1: Reading the CSV File

1. Create a directory for your solution.
2. Download the [weird-al.csv](weird-al.csv) file to your solution directory to use in testing your program.
3. View the contents of the [weird-al.csv](weird-al.csv) file to determine its structure. Note that the field delimiter is `;`, not `,`.
4. Your program should take a single command-line argument, the name of a CSV song list file to use as input. You may assume that any CSV song list file given to your program will have the same structure as [weird-al.csv](weird-al.csv). You may also assume that any song list file given to your program will have a `.csv` extension.
5. If the file specified on the command line does not exist, report this to the user and exit.
6. Use Python’s standard csv module to parse the file into an appropriate data structure in memory.
  - Note that if you do this right the next part of this homework is trivial, so take a look at the next section when deciding how to structure your playlist data.

### Part 2: Creating the JSPF File

Look at the [JSPF specification](https://www.xspf.org/jspf) (which is given as a couple of easily read examples).  Use the base name of the input file (the part before `.csv`) as the `title` of the playlist, yourself as the `creator`, the tracks in `track` (note the badly-named singular noun for list of tracks) come from the records in the CSV input file,  and write the playlist data to a JSPF-formatted JSON file with the same base name as the input file, but with a `.json` extension. The value associated with the top-level `duration` key in the JSPF playlist is the total running time of the playlist in seconds. 


### Sample JSPF File

If you ran your program on the [weird-al.csv(weird-al.csv) input file we provided, your JSPF file would look something like this:

```
{
  "title": "weird-al",
  "creator": "chris",
  "duration": 1986,
  "track": [
    {
      "title": "A Complicated Song (Parody of \"Complicated\" by Avril Lavigne)",
      "duration": 219,
      "creator": "Weird Al Yankovic",
      "album": "Poodle Hat",
      "location": "https://itunes.apple.com/us/album/a-complicated-song-parody-of-complicated-by-avril-lavigne/206901097?i=206902871",
    },
    {
      "title": "Ebay (Parody of \"I Want It That Way\" by the Backstreet Boys)",
      "duration": 216,
      "creator": "Weird Al Yankovic",
      "album": "Poodle Hat",
      "location": "https://itunes.apple.com/us/album/ebay-parody-of-i-want-it-that-way-by-the-backstreet-boys/206901097?i=206903768",
    },
    {
      "title": "Fat",
      "duration": 217,
      "creator": "Weird Al Yankovic",
      "album": "Even Worse",
      "location": "https://itunes.apple.com/us/album/fat/250500424?i=250500433",
    },
    {
      "title": "Eat It",
      "duration": 200,
      "creator": "Weird Al Yankovic",
      "album": "In 3-D",
      "location": "https://itunes.apple.com/us/album/eat-it/250495308?i=250495319",
    },
    {
      "title": "Smells Like Nirvana",
      "duration": 222,
      "creator": "Weird Al Yankovic",
      "album": "Off the Deep End",
      "location": "https://itunes.apple.com/us/album/smells-like-nirvana/250495074?i=250495085",
    },
    {
      "title": "Amish Paradise (Parody of \"Gangsta's Paradise\" by Coolio)", 
      "duration": 200, 
      "creator": "Weird Al Yankovic", 
      "album": "Bad Hair Day", 
      "location": "https://itunes.apple.com/us/album/amish-paradise-parody-of-gangstas-paradise-by-coolio/206900040?i=206900081",
    }, 
    {
      "title": "White & Nerdy (Parody of \"Ridin'\" By Chamillionaire featuring Krayzie Bone)", 
      "duration": 170, 
      "creator": "Weird Al Yankovic", 
      "album": "Straight Outta Lynwood", 
      "location": "https://itunes.apple.com/us/album/white-nerdy-parody-of-ridin/309731664?i=309732001",
    }, 
    {
      "title": "Party In the CIA (Parody of \"Party In the U.S.A.\" By Miley Cyrus)", 
      "duration": 176, 
      "creator": "Weird Al Yankovic", 
      "album": "Alpocalypse", 
      "location": "https://itunes.apple.com/us/album/party-in-the-cia-parody-of-party-in-the-u-s-a-by-miley-cyrus/438383158?i=438383166",
    }, 
    {
      "title": "Canadian Idiot (Parody of \"American Idiot\" By Green Day)", 
      "duration": 143, 
      "creator": "Weird Al Yankovic", 
      "album": "Straight Outta Lynwood", 
      "location": "https://itunes.apple.com/us/album/canadian-idiot-parody-of-american-idiot-by-green-day/309731664?i=309732012",
    }, 
    {
      "title": "Word Crimes", 
      "duration": 223, 
      "creator": "Weird Al Yankovic", 
      "album": "Mandatory Fun", 
      "location": "https://itunes.apple.com/us/album/word-crimes/891836396?i=891836406",
    }
  ],
}
```

Note that the example above is pretty-printed to look like the [JSPF specification](https://www.xspf.org/jspf) and key-value pairs may appear in any order.

Bonus: Add a `duration` key to the JSPF playlist object whose value is the total running time of the playlist in seconds. 

### Tips and Considerations

- Track duration in the JSPF file is in seconds, but in the input file the track durations are in minutes:seconds format.
- Note the type of the value associated with the `track` key in the JDPF format.
- Using the [CSV](https://docs.python.org/3/library/csv.html) and [JSON](https://docs.python.org/3/library/json.html) modules make this assignment trivial.
