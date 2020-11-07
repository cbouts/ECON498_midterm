from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()

# # for trying to print things, uncomment this: 
# one_file_name = "html_files_trial/cmcap20201101164950.html"
# scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace("copy.html","")
# f = open(one_file_name, "r")
# soup = BeautifulSoup(f.read(), "html.parser")
# f.close()
# currencies_table = soup.find("tbody")
# currency_rows = currencies_table.find_all("tr")
# currency_columns = currency_rows[0].find_all("td")
# print()


for one_file_name in glob.glob("html_files_2/*.html"):
	print(one_file_name)
	scrape_time = os.path.basename(one_file_name).replace("cmcap", "").replace(".html","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()

	currencies_table = soup.find("tbody")
	currency_rows = currencies_table.find_all("tr")

	for r in currency_rows:
		currency_columns = r.find_all("td")
		if len(currency_columns)>10:
			currency_name = currency_columns[2].find("p").text
			currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
			currency_price = currency_columns[3].find("a").text.replace("$","").replace(",","")
			currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace(",","")
			currency_trading_volume_inUSD = currency_columns[7].find("a").text.replace("$","").replace(",","")
			currency_circulating_supply = currency_columns[8].find("p").text.replace("" " + currency_symbol","").replace("$","").replace(",","")
			currency_trading_volume_inCurrency = currency_columns[7].find("p", {"class": "Text-sc-1eb5slv-0 jicUsX"}).text.replace(",","")
			currency_link = currency_columns[2].find("a")["href"]
			currency_logo = currency_columns[2].find("a").find('img')
			df = df.append({
						'name': currency_name,
						'symbol': currency_symbol,
						'time': scrape_time,
						'price': currency_price,
						'market_cap': currency_marketcap,
						'trading_volume-USD': currency_trading_volume_inUSD,
						'trading_volume-currency': currency_trading_volume_inCurrency,
						'circulating_supply': currency_circulating_supply,
						'logo': currency_logo,
						'link': currency_link
					}, ignore_index=True)

df.to_csv("cmc_parsed_files/cmc_dataset.csv")
