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

It shows, for example, that 64% of observations for return on investment for coingecko are missing. As it is, this collection of ROI values is not complete enough to use for analysis. Due to time and knowledge constraints, we opt instead to use other variables that have more complete information. These variables include price, market capitalization, and volume. As each of these is centraly important for cryptocurrency analysts, and because we have complete information for these, we focus the rest of our analysis on these variables.

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


While looking over these files, it becomes intuitively clear that although the sites report on the same information, their reporting differs. To illustrate these differences, the graphs (from Excel) below compare the mean prices, market caps, and volumes for the coins that feature on the top 500 list during the 48 hour time period. If the sites' reportings were identical, each dot would fall on the X = Y line.

### Comparison of mean market caps:

![Means_Market_Cap](/data_analysis/Means_Market_Cap.png)

This chart, generated using [market_cap_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/market_cap_cmc.csv) and [market_cap_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/market_cap_gecko.csv) in Excel, plots the mean of Coin Gecko observations of market cap over the 48 hour time period for each coin against the comparable value from Coinmarketcap data. There are a few things to note about this. First, like the similar graphs below, this graph excludes several of the top cryptocurrencies because their presence on the graph distorts the size of the graph in a way that obscures the variation among the vast majority of coins (ie, those not in the top 5 or 10 cryptocurrencies). Second, we see that most dots appear to follow the X = Y line, but there is noticeable variation around this line, especially for the lower ranked currencies. This variation affirms our intuition that the sites report data differently.

### Comparison of mean prices:

![Means_Prices](/data_analysis/Means_Prices_1.png)

Here, we use Excel to plot data from [price_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/price_cmc.csv) and [price_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/price_gecko.csv). This data seems to fit the X = Y line very well, but we should remember that we are looking at a graph in which many observations are stuck together right around the origin. What looks like an X = Y trend here may simply be the results of looking at a cluster of data, followed by 12 relatively expensive coins that seem to follow the X = Y line. To get a better understanding, we zoom in on the coins clustered around the origin.

![Means_Prices_2](/data_analysis/Mean_Price_2.png)

From this perspective, there is obvious noise around the X = Y line, so we have an indication that the sites report prices differently.

### Comparison of mean volumes:

![Means_Volumes_1](/data_analysis/Mean_Volumes_1.png)

Finally, we compare the mean of the sites' measures of volumes over the 48 hour period. We use Excel to plot data from [volume_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/volume_cmc.csv) and [volume_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/volume_gecko.csv). This graph is interesting because it doesn't seem like the observations fit the X = Y line especially for the 6 or so rightmost coins. In particular, it seems that the observations tend to lie above this imaginary line that would indicate uniform (on average) reportng of volumes. If this trend was present across the data, we might infer that for the same coins, Coinmarketcap tends to report values for volume as higher than those reported by Coingecko. To get a better idea of what's going on, we should zoom in on the part of the graph with the highest concentration of coins- that near the origin.

![Means_Volumes_2](/data_analysis/Mean_Volumes_2.png)

In this picture, it's more evident that not all noise around the X = Y line lies above this line. This discredits the inference that Coinmarketcap tends to report values for volume as higher than those reported by Coingecko. Still, it increases our confidence in the notion that Coinmarketcap and Coingecko report on key indicators differently.


## Time-Informed Analysis
Having established through summary statistics that the sites' reporting varies on the aggregate, we now make use of the time variation in our data to further explore these differences. We would like to somehow look at all 500 coins simultaneously on a multiple line graph that plots a variable of interest (price, market cap, or volume) against the time of observation. However, such a graph would have 1000 lines going through it (one line per coin per site), and would certainly be a nonsensical blob of lines. Having considered this and other potential methods of analysis, it seems that it would be most informative to make these graphs for several individual coins. I use the datasets [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv) and [gecko_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/gecko_dataset.csv) to make graphs in Excel tracking each site's reportings of price, volume, and market cap over the 48 hour time period for the coins Bitcoin (BTC, ranked first by market cap), Digibyte (DGB, ranked around 50th by market cap), Bytom (BTM, ranked around 100th by market cap), AdEx (ADX, ranked around 200th by market cap), and ARPA Chain (ARPA, ranked around 300th by market cap). All of these charts can be found in the [data_analysis folder](https://github.com/cbouts/midterm_project/tree/main/data_analysis), and can be understood with the knowledge that observations were gathered every 15 minutes for 48 hours, yielding the 192 observations reflected on the x axis. Coinmarketcap data is in orange and Coingecko data is in blue.

- For BTC:
  - Price: [BTC_price.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/BTC_price.png)
  - Market Cap: [BTC_mc.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/BTC_mc.png)
  - Volume: [BTC_volume.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/BTC_volume.png)
- For DGB:
  - Price: [DGB_price.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/DGB_price.png)
  - Market Cap: [DGB_mc.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/DGB_mc.png)
  - Volume: [DGB_volume.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/DGB_volume.png)
- For BTM:
  - Price: [BTM_price.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/BTM_price.png)
  - Market Cap: [BTM_mc.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/BTM_mc.png)
  - Volume: [BTM_Volume.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/BTM_Volume.png)
- For ADX:
  - Price: [ADX_price.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/ADX_price.png)
  - Market Cap: [ADX_mc.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/ADX_mc.png)
  - Volume: [ADX_volume.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/ADX_volume.png)
- For ARPA:
  - Price: [ARPA_price.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/ARPA_price.png)
  - Market Cap: [ARPA_mc.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/ARPA_mc.png)
  - Volume: [ARPA_volume.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/ARPA_volume.png)


We now examine market cap, price, and volume in turn by looking to these graphs.

#### Market Cap
![BTC_mc](/data_analysis/BTC_mc.png)
![DGB_mc](/data_analysis/DGB_mc.png)
![BTM_mc](/data_analysis/BTM_mc.png)
![ADX_mc](/data_analysis/ADX_mc.png)
![ARPA_mc](/data_analysis/ARPA_mc.png)

Scrolling through these graphs, we notice some variation. For BTC and ADX, Coingecko and Coinmarketcap report roughly the same market cap values over the 48 hours of interest. The DGB graph illustrates that for this coin, Coingecko and Coinmarketcap report very similar market cap values on average, but that there is a higher variance in Coingecko's reporting of market cap. While these 3 graphs suggest that Coingecko and Coinmarketcap report the same market caps on average for given coins, the graphs for BTM and ARPA suggest that Coingecko reports a higher market cap on average for a given coin than Coinmarketcap does. It is reasonable to infer from these graphs that on average, Coingecko's reported market cap values will be either higher than or the same as those reported by Coinmarketcap.

#### Price
![BTC_price](/data_analysis/BTC_price.png)
![DGB_price](/data_analysis/DGB_price.png)
![BTM_price](/data_analysis/BTM_price.png)
![ADX_price](/data_analysis/ADX_price.png)
![ARPA_price](/data_analysis/ARPA_price.png)

#### Volume
![BTC_volume](/data_analysis/BTC_volume.png)
![DGB_volume](/data_analysis/DGB_volume.png)
![BTM_Volume](/data_analysis/BTM_Volume.png)
![ADX_volume](/data_analysis/ADX_volume.png)
![ARPA_volume](/data_analysis/ARPA_volume.png)
## Detecting Associations
The currencies on these sites are ranked by market capitalization. However, market cap is only one of the several most important metrics for cryptocurrency. Arguably, volume and circulating supply are just as salient as market cap. As a result, it's important to know whether, and if so, the extent to which we can use market cap-based rankings by coinmarketcap and coingecko to proxy for volume and circulating supply. 





