---
layout: exercise
title: Health
---

# Health

## Introduction

In this project you will practice doing basic data analyses using Pandas, Numpy, Matplotlib and Jupyter Notebooks.

## Problem Description

You're interested in the health habits and outcomes in developed nations, particularly the EU and US.

## Solution Description

Download [`health.csv`](health.csv), which contains health-related information derived from data in the [Eurostat](http://ec.europa.eu/eurostat/) [database](http://ec.europa.eu/eurostat/data/database) (Expand the tree to find the data tables). For comparison to the US, I added roughly equivalent statistics for the US. US data come from the following sources:

- https://www.cdc.gov/nchs/data/databriefs/db293.pdf
- https://www.niddk.nih.gov/health-information/health-statistics/overweight-obesity
- https://www.cdc.gov/tobacco/data_statistics/fact_sheets/adult_data/cig_smoking/index.htm
- https://www.cdc.gov/media/releases/2017/p1116-fruit-vegetable-consumption.html
- https://www.cdc.gov/nchs/fastats/exercise.htm

The data file has the following columns:

- ex - percentage of population doing aerobic exercise more than 150 minutes per week
- fv - percentage of population eating at least 5 servings of fruits and vegetables a day
- le - life expectancy at one year (remaining years to live)
- obese - percentage of population with [BMI](https://www.cdc.gov/obesity/adult/defining.html) > 30
- sk - percentage of adults who smoke occasionally or daily ("current smokers")

In the same directory as this data file write a Jupyter Notebook named `health` with the contents described below.

### Jupyter Notebook Sections

Your notebook should have the following parts:

#### Part 1 - Basic Metrics

Make the necessary imports and read the CSV data file into a Pandas DataFrame named `health`. Use the first column from the data file (the countries) as the index column for the DataFrame. Answer the questions below using the DataFrame.

For each of the following, include a Markdown cell with the question followed by a code cell which computes and displays the answer. For example, for the question

- What is 2 \* 3?

You would have a Markdown cell with:

```
What is 2 * 3?
```

followed by a code cell with

```
2 * 3
```

For each of the data columns, what is the average, which country is "best", which is "worst" and how does the US compare (where would US rank compared to EU countries.

- What is the average life expectancy of EU countries in the data set?
- In which country is the life expectancy highest?
- In which country is the life expectancy lowest?
- Where does the US rank in life expectancy compared to EU countries?
- What is the average obesity rate of EU countries in the data set?
- Which country is most obese?
- Which country is least obese?
- Where does the US rank in obesity rate compared to EU countries?
- What is the average smoking rate of EU countries in the data set?
- Which country smokes the most?
- Which country smokes the least?
- Where does the US rank in smoking rate compared to EU countries?
- What is the average vegetable-eating rate of EU countries in the data set?
- Which country eats the most vegetables?
- Which country eats the least vegetables?
- Where does the US rank in fruit and vegetable consumption compared to EU countries?

What do these results tell you about health outcomes in Europe and in the US?

#### Part 2 - Visualization

For each of the following, include a Markdown cell with the question/description and a code cell that produces the visualization. Choose a graphic display that would clearly present the information.

One variable:

- Country life expectancy relative to other countries; which country has highest, second-highest, etc. -- by how much
- Country healthy life expectancy relative to other countries; which country has highest, second-highest, etc. -- by how much
- Country obesity rates relative to other countries; which country is most obese, second-most, etc. -- by how much
- Country smoking rates relative to other countries; which country smokes the most, second-most, etc. -- by how much
- Country vegetable eating rates relative to other countries; which country eats most, second-most, etc. -- by how much
- Country exercise rates relative to other countries; which country exercises most, second-most, etc. -- by how much

What do these plots tell you about the gaps between countries in the data set?

Two variables:

Rather than looking at the measurements by country, look at the measurements relative to other measurements. Each pair of measurements in the data set is paired by country, that is, associated. Plot life expectancy against each of the following variables (life expectancy should be the dependent variable).

- Obesity rate
- Smoking rate
- Vegetable-eating rate
- Exercise-rate

What do these plots tell you about these risk factors?

## Tips and Considerations

- Some data are missing in the data file (as they are in the source data files). See the course slides for tips on how to handle the missing data.

## Discussion

I wrote a script ([create_health_summary.py](create_health_summary.py)) to create the relatively clean dataset for this exercise from these source files downloaded from [Eurostat](http://ec.europa.eu/eurostat/data/database) (they're all [gzip](http://www.gzip.org/) archives, as downloaded from Eurostat). (I then added US data from WHO, CDC, and NIH.) This script is an example of creating a simpler data set from a collection of more complicated data sets.

## Sample Solution

- [health-answers.ipynb](health-answers.ipynb)
