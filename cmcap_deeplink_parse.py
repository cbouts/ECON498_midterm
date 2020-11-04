from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()

# # for trying to print things, uncomment this: 
# one_file_name = "deep_link_html/bitcoin.html"
# f = open(one_file_name, "r")
# soup = BeautifulSoup(f.read(), "html.parser")
# f.close()
# tables = soup.find("tbody", {"class": "cmc-details-panel-about__table"})
# row = tables.find_all("tr")
# print()

for one_file_name in glob.glob("deep_link_html/*.html"):
	print(one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	tables = soup.find("tbody", {"class": "cmc-details-panel-about__table"})
	row = tables.find_all("tr")
    market_rank = row[2].find("td").text.replace("#","")
	ath = row[8].find("div").text.replace("$","").replace(",","").replace(" USD","")
	atl = row[9].find("div").text.replace("$","").replace(",","").replace(" USD","")
	roi = row[1].find("span").text
	total_supply = row[6].find("td").text
	max_supply = row[7].find("td").text

# 	df = df.append({
# 						'name': currency_name,
# 						'symbol': currency_symbol,
# 						'time': scrape_time,
# 						'price': currency_price,
# 						'market_cap': currency_marketcap,
# 						'trading_volume-USD': currency_trading_volume_inUSD,
# 						'trading_volume-currency': currency_trading_volume_inCurrency,
# 						'circulating_supply': currency_circulating_supply,
# 						'logo': currency_logo,
# 						'link': currency_link
# 					}, ignore_index=True)

# df.to_csv("cmc_parsed_files/cmc_dataset.csv")






