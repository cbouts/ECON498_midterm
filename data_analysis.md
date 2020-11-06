# Data Analysis

## Contents
* [Choosing Variables of Interest](#Choosing Variables of Interest)
* [Summary Statistics](#Summary Statistics)
* [Time-Informed Analysis](#Time-Informed Analysis)
* [Detecting Associations Between Market Cap and Volume](#Detecting Associations)
* [Time-Informed Analysis](#Time-Informed Analysis)



## Choosing Variables of Interest
As the data I have collected is imperfect, I want to make sure that my data contains complete information for the most salient variables. To do this, we run the file [cleaning.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cleaning.py). This gives us a terminal output identifying the percentage of observations missing for each main variable in each of our 3 main datasets. This is the output. 

<img width="409" alt="Screen Shot 2020-11-05 at 3 08 00 PM" src="https://user-images.githubusercontent.com/70339619/98393218-fc611900-2026-11eb-97f4-6fcac9333e65.png">

It shows, for example, that 64% of observations for return on investment for coingecko are missing. As it is, this collection of ROI values is not complete enough to use for analysis. Due to time and knowledge constraints, we opt instead to use other variables that have more complete information. These variables include price, market capitalization, circulating supply, and volume. As each of these is centraly important for cryptocurrency analysts, and because we have complete information for these, we focus the rest of our analysis on these variables.

## Summary Statistics
First, I compiled summary statistics for each coin on each website by running the file [summary_statistics.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/summary_statistics.py). This yielded 6 new csvs: 
- Summary statistics on volume:
  - [volume_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/volume_cmc.csv)
  - [volume_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/volume_gecko.csv)
- Summary statistics on price:
  - [price_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/price_cmc.csv)
  - [price_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/price_gecko.csv)
- Summary statistics on market cap: 
  - [market_cap_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/market_cap_cmc.csv)
  - [market_cap_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/market_cap_gecko.csv)
 - Summary statistics on circulating supply:
  - 

While looking over these files, it becomes intuitively clear that although the sites report on the same information, their reporting differs. To illustrate these differences, the graphs (which come from running the file ------) below compare the mean prices, market caps, and volumes for the coins that feature on the top 500 list during the 48 hour time period.

----


## Time-Informed Analysis

Having established through summary statistics that the reporting varies on the aggregate, we now make use of the time variation in our data to further explore these differences. We would like to somehow look at all 500 coins simultaneously on a multiple line graph that plots a variable of interest (price, market cap, or volume) against the time of observation. However, such a graph would have 1000 lines going through it (one line per coin per site), and would certainly be a nonsensical blob of lines. Having considered this and other potential methods of analysis, it seems that it would be most informative to make these graphs for several individual coins. I make graphs to track each site's reportings of price, volume, and market cap over the 48 hour time period for the coins Bitcoin (ranked first by market cap), Digibyte (ranked around 50th by market cap), Bytom (ranked around 100th by market cap), Adx (ranked around 200th by market cap), and Contracoin (ranked around 300th by market cap). 

using the file ------ and get: 



We see on these charts that ----- 

## Detecting Associations






