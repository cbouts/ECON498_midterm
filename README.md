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
1. Step 1: request data by running [cmcap_coingecko_request.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_coingecko_request.py). In its current form, the file requests data at 15 minute intervals for the 48 hour time period of interest, resulting in (4 downloads per hour) * (48 hours) = 192 download processes.
2. Step 2: parse the data for the two websites using the parse files ___ and _ . 
3. Step 3: Run - with the coinmarketcap parsed data to request deep link information for each coin that features on the top 500 list over the time period of interest.
4. Step 4: Run the deep link parse file to parse the deep link information to a new csv called -
5. Step 5: Analyze the data on the 3 csvs. Run cleaning.py --- to determine how much data for each variable is missing. Using the CSVs, create Excel graphs to show differences in ----
