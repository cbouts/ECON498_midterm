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
Running this projects takes - steps. They are listed and elaborated here.

### Step 1:

Request data by running [cmcap_coingecko_request.py](https://github.com/cbouts/midterm_project/blob/main/cmcap_coingecko_request.py). This file requests the most important data from Coingecko using API and from Coinmarketcap using screen scraping. First, the file creates the folders which will hold html files from Coinmarketcap and the json files from Coingecko: 
```
if not os.path.exists("html_files_2"):
	os.mkdir("html_files_2")

if not os.path.exists("json_files_2"):
	os.mkdir("json_files_2")
```
On my computer, I need to include the next line because I get an "unverified" error if I do not. However, many people successfully omit this from their code: `context = ssl._create_unverified_context()`. We write this unverified context after each of our URLs to prevent the error: `context=context`. 

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

4. Step 4: 
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
Create a new folder, [data_analysis](https://github.com/cbouts/midterm_project/tree/main/data_analysis). We will now analyze the data on the 3 csvs, so we move them into the new folder because this is where we will be using them. 
#### Step 5A:
Run [cleaning.py](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cleaning.py) --- to determine how much data for each variable is missing. 
#### Step 5B:
Using [coingecko_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/coingecko_dataset.csv) and [cmc_dataset.csv](https://github.com/cbouts/midterm_project/blob/main/data_analysis/cmc_dataset.csv), create Excel graphs to show differences in --
