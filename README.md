# ECON4980 Midterm Project

## Contents
* [Introduction](#Introduction)
* [Technologies](#Technologies)
* [Installation](#Installation)

## Introduction
This project downloads and parses salient data on the top 500 cryptocurrencies (ranked by market capitalization) from the websites [coinmarketcap](coinmarketcap.com) and [coingecko](coingecko.com) 192 times over a 48 hour time period. It uses these data to analyze differences in reporting between the two sites. As a bonus, the project also requests and attempts to parse historical data from these websites for the year between November 1, 2019 and November 1, 2020. 

## Technologies
This project was made on Python 3.7, so that or a newer version may be required to run it. 

The programs also use the modules numpy, matplotlib, bs4, pandas, sklearn, tzlocal, and requests. If you don't have these already, you may need to install them by writing:
`pip -m install numpy matplotlib bs4 pandas sklearn tzlocal requests`
in the terminal.

## Installation
To run this project, you will need to install it on your computer. To do this, write
`pip install git+git://github.com/cbouts/midterm_project.git`
in the terminal.

## Usage
Running this projects takes 5 steps. They are listed and elaborated here.

### Step 1:

Request data by running [cmcap_coingecko_request.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_coingecko_request.py). This file requests data from Coingecko using API and from Coinmarketcap using screen scraping. All you need to do is run the program and monitor the terminal output for errors which, because of the file's try/except/else format, will be printed out before the program continues to run. In its current form, the file requests data at 15 minute intervals for the 48 hour time period of interest, resulting in (4 downloads per hour) * (48 hours) = 192 download processes. Of course, this can be adapted to fit your needs as is illustrated here:
- To get a different number of observations, you can change 192 to another number in this line of code:
`for i in range(192):`
- The 15 minute intervals are regulated by the 4 lines of code that say `time.sleep(15)` and the one line that says `time.sleep(840)`. Including 4 time.sleep periods of 15 seconds each throughout the program and 1 long 840 second time.sleep period yields 900 total seconds of sleep between the start of one round of downloads and the start of the next round. Note that you should always include some sleep time after your downloads in order to avoid breaking or getting banned from the sites.
- Manipulating these `time.sleep()` and `for i in range():` lines allows you to change the length of the time period of interest, as well as the frequency of your observations. 

### Step 2: 
Parse the data for the two websites by running the parse files [coingecko_parse.py](https://github.com/cbouts/midterm_project/blob/main/coingecko_parse.py) and [cmcap_parse.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_parse.py). 
3. Step 3: Run - with the coinmarketcap parsed data to request deep link information for each coin that features on the top 500 list over the time period of interest.
4. Step 4: Run the deep link parse file to parse the deep link information to a new csv called -
5. Step 5: Analyze the data on the 3 csvs. Run cleaning.py --- to determine how much data for each variable is missing. Using the CSVs, create Excel graphs to show differences in ----
