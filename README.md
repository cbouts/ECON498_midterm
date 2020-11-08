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
Running this project takes 6 main steps. They are listed and elaborated here.

### Step 1:
Request data by running [cmcap_coingecko_request.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_coingecko_request.py). This file requests the most important data from Coingecko using API and from Coinmarketcap using screen scraping. First, the file creates the folders which will hold html files from Coinmarketcap and the json files from Coingecko: 
```
if not os.path.exists("html_files_2"):
	os.mkdir("html_files_2")

if not os.path.exists("json_files_2"):
	os.mkdir("json_files_2")
```
On my computer, I need to include the line `context = ssl._create_unverified_context()` and write `context=context` after each URL to prevent an "unverified" error. However, many people successfully omit this from their code.

In its current form, the file requests data at 15 minute intervals for the 48 hour time period of interest, resulting in (4 downloads per hour) * (48 hours) = 192 download processes reflected in the beginning for the for loop: `for i in range(192):`. The file then requests the first page of 100 coins from coinmarketcap, the first 250 coins from coingecko, sleeps for 15 seconds, requests the second page of 100 coins from coinmarketcap and coins 250-500 from coingecko, sleeps for 15 seconds, then requests pages 3-5 (coins 300-500) from coinmarketcap (with sleep time of 15 seconds between these requests). After this, the program sleeps for 840 seconds. 

Of course, this can be adapted to fit your needs as is illustrated here:
- To get a different number of observations, you can change 192 to another number in this line of code:
`for i in range(192):`
- The 15 minute intervals are regulated by the 4 lines of code that say `time.sleep(15)` and the one line that says `time.sleep(840)`. Including 4 time.sleep periods of 15 seconds each throughout the program and 1 long 840 second time.sleep period yields 900 total seconds of sleep between the start of one round of downloads and the start of the next round. Note that you should always include some sleep time after your downloads in order to avoid breaking or getting banned from the sites.
- Manipulating these `time.sleep()` and `for i in range():` lines allows you to change the length of the time period of interest, as well as the frequency of your observations.For example, changing `time.sleep(840)` to `time.sleep(540)` while also changing `for i in range(192):` to `for i in range(6):` will yield 6 downloads of the site 10 minutes apart over a 1 hour time period.

Once you've configured the program to match your needs, you simply run it and monitor the terminal output for errors which will be printed without interrupting the program's progress due to the file's "try/except/else" format.


### Step 2: 
Parse the data.
#### Step 2A:
Run [coingecko_parse.py](https://github.com/cbouts/midterm_project/blob/main/coingecko_parse.py). This creates the folder 'coingecko_parsed_files' which will hold our new coingecko csv:
```
if not os.path.exists('coingecko_parsed_files'):
	os.mkdir('coingecko_parsed_files')
```
It then loops through the files in the json_files_2 folder (the folder which contains all json files from downloading Coingecko). It creates a dataframe for each coin in each file, appending key information to this dataframe with:
```
df = df.append({
      		'id': coin['id'],
		'time': scrape_time,
	      	'symbol': coin['symbol'],
		'name': coin['name'],
		'logo': coin['image'],
		'current_price': coin['current_price'],
		'market_cap': coin['market_cap'],
		'market_cap_rank': coin['market_cap_rank'],
		'total_volume': coin['total_volume'],
		'circulating_supply': coin['circulating_supply'],
		'total_supply': coin['total_supply'],
		'max_supply': coin['max_supply'],
		'ath': coin['ath'],
		'ath_date': coin['ath_date'],
		'atl': coin['atl'],
		'atl_date': coin['atl_date'],
		'roi': coin['roi']
	}, ignore_index=True)
```
These were the indicators I was most interested in, but you can delete some or add some by looking at one of the json files you've downloaded to find the name of the new category of information you're interested in and using the structure `'indicator': coin['indicator']` to add the new information to the `df.append` funciton. 

After looping through all coins in all the Coingecko json files, it exports the dataframe to our new csv:
`df.to_csv('coingecko_parsed_files/coingecko_dataset.csv')`. This csv is here: [coingecko_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/coingecko_dataset.csv). (Note that we've since moved it to the data_analysis folder because it is easier to use for analysis if it's in this folder.)

#### Step 2B:
Run [cmcap_parse.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_parse.py). This creates the folder 'cmc_parsed_files' which will hold our new coingecko csv:
```
if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")
```
It then loops through and reads the files in the html_files_2 folder (the folder which contains all json files from downloading Coingecko). Within this for loop, there is a for loop that causes the program to loop through every row (representing every coin) in the current file. The for loop then picks up key information about the coins with 
```
currency_name = currency_columns[2].find("p").text
currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","")
currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace(",","")
currency_trading_volume_inUSD = currency_columns[7].find("a").text.replace("$","").replace(",","")
currency_circulating_supply = currency_columns[8].find("p").text.replace("" " + currency_symbol","").replace("$","").replace(",","")
currency_trading_volume_inCurrency = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 jicUsX"}).text.replace(",","")
currency_link = currency_columns[2].find("a")["href"]
currency_logo = currency_columns[2].find("a").find('img')
```
These were the indicators I was most interested in, but you can delete some or add some by examining the coinmarketcap.com site, inspecting the table of information, and following the structure I've laid out in my examples above to include the new variables in the code. 

The file then appends this information to a dataframe with:
```
df = df.append({
        	.........
			}, ignore_index=True)
```
After looping through all coins in all the Coinmarketcap html files, it exports the composite dataframe to our new csv:
`df.to_csv('coingecko_parsed_files/cmc_dataset.csv')`. 
This csv is here: [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv). (Note that we've since moved it to the data_analysis folder because it is easier to use for analysis if it's in this folder.)


### Step 3: 
Run [cmcap_deeplink.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_deeplink.py) to request deep link information from coinmarketcap for each coin that features on the top 500 list over the time period of interest. This file first creates the file that will hold these html files:
```
if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")
```
Next, the file reads [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv). Again, I've included `context = ssl._create_unverified_context()` and `context=context`, but you may be able to omit these.
```
df = pd.read_csv("cmc_parsed_files/cmc_dataset.csv")

context = ssl._create_unverified_context()
```
It loops through the links to deep link information for each coin on the csv, and writes information about these coins into html files unless the deep link file for that coin already exists. This ensures that we get only one deep link file per coin. These html files are first written with .temp, which is only removed from the name once everything has been written correctly. A sleep time of 30 seconds occurs after each download to prevent issues with the website. 
```
for link in df['link']:
	filename = link.replace('/currencies/', '')
	if os.path.exists("deep_link_html/" + filename + ".html"):
		print(filename + ".html already exists.")
	else:
		print("downloading " + link)
		response = urllib.request.urlopen("https://coinmarketcap.com/" + link, context=context)
		html = response.read()
		f = open('deep_link_html/' + filename + '.html.temp', 'wb')
		f.write(html)
		f.close()
		os.rename("deep_link_html/" + filename + '.html.temp', 'deep_link_html/' + filename + '.html')
		time.sleep(30)
```
The resultant csv can be found here: [cmc_deeplink.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_deeplink.csv).


### Step 4: 
Parse the deep link information by running [cmcap_deeplink_parse.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_deeplink_parse.py). The file first creates the file that will hold the new csv of deep link information if it does not already exist:
```
if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")
```
The file then creates a data frame and loops through each deep link html file to locate information about the coin and append this to the dataframe which will eventually form a new csv. This file has an interesting structure that can best be understood by looking at it and reading the explanation below:
```
if len(tables)==19:
		try:
			market_rank = rows[2].find("td").text.replace("#","")
			ath = rows[8].find("div").text.replace("$","").replace(",","").replace(" USD","")
			atl = rows[9].find("div").text.replace("$","").replace(",","").replace(" USD","")
			roi = rows[1].find("span").text
			total_supply = rows[6].find("td").text.replace(",","")
			max_supply = rows[7].find("td").text.replace(",","")

			df = df.append({
						'name': one_file_name.replace("deep_link_html/","").replace(".html",""),
						'market_rank': market_rank,
						'ath': ath,
						'atl': atl,
						'roi': roi,
						'total_supply': total_supply,
						'max_supply': max_supply
							}, ignore_index=True)
		except:
			print(" ERROR: WEBSITE HAS INCOMPLETE DATA FOR " + one_file_name.replace(".html",""))
		
	else:
		try:
			market_rank = rows[4].find("td").text.replace("#","")
			ath = rows[13].find("div").text.replace("$","").replace(",","").replace(" USD","").replace(" /","")
			atl = rows[14].find("div").text.replace("$","").replace(",","").replace(" USD","").replace(" /","")
			roi = rows[15].find("span")
			# roi = rows[15].find("span").text
			total_supply = rows[17].find("td").text.replace(",","")
			max_supply = rows[18].find("td").text.replace(",","")

			df = df.append({
						'name': one_file_name.replace("deep_link_html/","").replace(".html",""),
						'market_rank': market_rank,
						'ath': ath,
						'atl': atl,
						'roi': roi,
						'total_supply': total_supply,
						'max_supply': max_supply
							}, ignore_index=True)
		except: 
			print(" ERROR: WEBSITE HAS INCOMPLETE DATA FOR " + one_file_name.replace(".html",""))
```
The deep link htmls downloaded in such a way that some have all rows in one order within one tbody, but others have four tbodies containing the same rows in a different order. This is the reason for the "if/else" structure- some have a table length of 19, while others have a different length. Within each of these groups of htmls, some coins have incomplete data listed. This program skips over them and notes them in the terminal with an error message. This is the reason for the try/except structure.

Like in the other parse files, if you are interested in parsing different information, you can delete some information or add other information by examining the files you've downloaded and following the structure I've used to incorporate the information in your code.

The resultant csv is found here: [cmc_deeplink.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_deeplink.csv). (Note that we've since moved it to the data_analysis folder because it is easier to use for analysis if it's in this folder.)


### Step 5: 
Create a new folder, [data_analysis](https://github.com/cbouts/midterm_project/tree/main/data_analysis). We will now analyze the data on the 3 csvs, so we move them into the new folder because this is where we will be using them. A detailed write-up about the processes used and analysis completed in this step is available at [data_analysis.md](https://github.com/cbouts/midterm_project/blob/main/data_analysis.md).
#### Step 5A:
Run [cleaning.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cleaning.py) to determine how much data for each variable is missing. This file reads each of our 3 CSVs in turn, identifies the percentage of data missing in each column of each CSV, and prints the results in the terminal output. My results for this are presented in [data_analysis.md](https://github.com/cbouts/midterm_project/blob/main/data_analysis.md).
#### Step 5B: 
Run [summary_statistics.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/summary_statistics.py) to get summary statistics for price, market cap, and volume for each coin from each website using [coingecko_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/coingecko_dataset.csv) and [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv). For each csv, the file identifies information about market cap, volume, and price for each coin and identifies the mean, standard deviation, minimum, and maximum. With this information, the file creates 6 new CSVs of summary statistics:
- for Coinmarketcap:
  - [price_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/price_cmc.csv)
  - [volume_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/volume_cmc.csv)
  - [market_cap_cmc.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/market_cap_cmc.csv)
- for Coingecko:
  - [price_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/price_gecko.csv)
  - [volume_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/volume_gecko.csv)
  - [market_cap_gecko.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/market_cap_gecko.csv)
#### Step 5C:
Using the 6 new CSVs from step 5B, create graphs in Excel to show differences in mean market caps, prices, and volumes between the two sites. The new graphs are
- [Means__Prices_1.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/Means_Prices_1.png)
- [Mean_Price_2.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/Mean_Price_2.png)
- [Mean_Volumes_1.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/Mean_Volumes_1.png)
- [Mean_Volumes_2.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/Mean_Volumes_2.png)
- [Means_Market_Cap.png](https://github.com/cbouts/midterm_project/blob/main/data_analysis/Means_Market_Cap.png)

These graphs are analyzed in [data_analysis.md](https://github.com/cbouts/midterm_project/blob/main/data_analysis.md).
#### Step 5D:
Make use of the time dimension of our data by using [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv) and [gecko_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/gecko_dataset.csv) to make graphs in Excel tracking each site's reportings of price, volume, and market cap over the 48 hour time period for the coins Bitcoin (BTC, ranked first by market cap), Digibyte (DGB, ranked around 50th by market cap), Bytom (BTM, ranked around 100th by market cap), AdEx (ADX, ranked around 200th by market cap), and ARPA Chain (ARPA, ranked around 300th by market cap).
The resultant graphs are:
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

These graphs are examined and analyzed in [data_analysis.md](https://github.com/cbouts/midterm_project/blob/main/data_analysis.md).
#### Step 5E:
Look for associations between market cap (the indicator that the sites use to create their rankings) and volume and supply with linear regression by running [linear_regression.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/linear_regression.py). For each website (represented by each CSV, [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv) and [gecko_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/gecko_dataset.csv)), the file uses market cap as data (x values) and regresses price and volume on market cap with a linear regression machine. The results of these regressions (coefficients and intercepts) are printed in the terminal, and they are presented and analyzed in [data_analysis.md](https://github.com/cbouts/midterm_project/blob/main/data_analysis.md).


### Step 6 (BONUS):
#### Step 6A:
Request 1 year of historical data for each site by running the file [historical_request_2.py](https://github.com/cbouts/midterm_project/blob/main/historical_request_2.py). 

As in the first request file, I include `context = ssl._create_unverified_context()` and `context=context`, but you may not need to include these. Additionally, this file requests the most important historical data from Coingecko using API and from Coinmarketcap using screen scraping. First, the file creates the folders which will hold historical html files from Coinmarketcap and the historical json files from Coingecko: 
```
if not os.path.exists("historical_html_files"):
	os.mkdir("historical_html_files")

if not os.path.exists("historical_json_files"):
	os.mkdir("historical_json_files")
```
Unlike the first request file, this file is requesting historical data for a pre-determined list of coins- that is, the coins that featured in the list of the top 500 coins during the 48 hour download period. To get and use this list of coins, we use the the dataset [cmc_deeplink.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_deeplink.csv). Before you do this, you need to move the csv back out of the data_analysis folder so that it is at the same level as the file. The next lines of code read the csv and find the names of the coins we will be requesting historical data for.
```
col_list = ["ath", "atl", "market_rank", "max_supply", "name", "roi", "total_supply"]
df_1 = pd.read_csv('cmc_parsed_files/cmc_deeplink.csv', usecols=col_list)
df_2 = df_1["name"]
```
The next lines create a for loop that will be used for the rest of file to iterate through the coins and manipulate the names of the coins to fit into the request URLs for each coin on each site.
```
for row in df_2:
	name = row
	geckolink = row.replace("-","%20")
```
The if/else structure of the following code ensures that we get historical data for each coin one time from each website. This way, if the program is interrupted, it can be resumed without re-starting the request process. We first request data for the current coin from coinmarketcap, then from coingecko. To do this, we first create and open new html files (for coinmarketcap) and json files (for coingecko). We next use the names that we manipulated in the previous block of code (`"name"` and `"geckolink"`) in urls we've fetched from Coinmarketcap and from Coingecko's API page. The try/except/except/else structure ensures that the program continues running if it encounters url or http errors. 

The file currently requests data from 11/01/2019-11/01/2020. This is fairly straightforward to see in the coinmarketcap request URL: `url = "https://coinmarketcap.com/currencies/" + name + "/historical-data/" + "?start=20191101&end=20201101"`. Here, the dates are formatted as year+month+day. It is less obvious in coingecko's request URL: `url = 'https://api.coingecko.com/api/v3/coins/' + geckolink + '/market_chart/range?vs_currency=usd&from=1572609600&to=1604235600'`. This is because coingecko's link includes the start and stop dates as UNIX timestamps. To get UNIX timestamps for your time period of interest, you can convert dates into UNIX timestamps with the website [epochconverter.com](https://www.epochconverter.com). After the coinmarketcap download, there is a sleep time of 30 seconds. There is an additional 70 seconds sleep time before the for loop restarts for the next coin. This results in a total sleep time of 100 seconds. The start and end dates and sleep times can be changed based on your needs, as described above in step 1.

When you've made all adjustments, run the code and monitor the terminal output for errors.

#### Step 6B:
Parse the files.

I wrote parse files for the historical data from each site, but I could not get them to run after hours of trying. These are the parse files:
- (cmcap_historical_parse_4.py)[https://github.com/cbouts/midterm_project/blob/main/cmcap_historical_parse_4.py]
- (historical_parse_gecko.py)[https://github.com/cbouts/midterm_project/blob/main/historical_parse_gecko.py]

Because I couldn't parse this data, I included the html and json files in the folders [historical_html_files](https://github.com/cbouts/midterm_project/tree/main/historical_html_files) and (historical_json_files)[https://github.com/cbouts/midterm_project/tree/main/historical_json_files].

