# Data Analysis

## Contents

## Motivation/Choosing Variables of Interests
Before I begin the analysis, I want to make sure that my data contains complete information. To do this, we run the file [cleaning.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cleaning.py). This gives us a terminal output identifying the percentage of observations missing for each main variable in each of our 3 main datasets. This is the output. 

<img width="409" alt="Screen Shot 2020-11-05 at 3 08 00 PM" src="https://user-images.githubusercontent.com/70339619/98393218-fc611900-2026-11eb-97f4-6fcac9333e65.png">

It shows, for example, that 64% of observations for return on investment for coingecko are missing. As it is, this collection of ROI values is not complete enough to use for analysis. Due to time and knowledge constraints, we opt instead to use other variables that have more complete information. These variables include price, market capitalization, and volume. As each of these is centraly important for cryptocurrency analysts, and because we have complete information for these, we focus the rest of our analysis on these variables.

