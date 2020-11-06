from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import pdb

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()

# for one_file_name in glob.glob("historical_html_files/*.html"):
one_file_name = "historical_html_files/0x.html"
print("parse " + one_file_name)
f = open(one_file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()
currencies_hist_table = soup.find("tbody")
currency_rows = currencies_hist_table.find_all("tr")
print(len(currency_rows)

	
	# currencies_hist_table = soup.find("tbody")
	# currency_rows = currencies_hist_table.find_all("tr")
	# for r in currency_rows:
	# 	currency_columns = r.find_all("td")
	# 	print(currency_rows)
		# print(len(currency_columns))
# 		# printurrency_columns[6].find("div").text.replace(",",""))
# 	# 		currency_columns = r.find_all("td")
# 	# 			# if len(currency_columns)>10:
		# date = currency_columns[0].find("div").text
		# opening_price = currency_columns[1].find("div").text.replace(",","")
		# high_price = currency_columns[2].find("div").text.replace(",","")
		# low_price = currency_columns[3].find("div").text.replace(",","")
		# close_price = currency_columns[4].find("div").text.replace(",","")
		# currency_volume_USD = currency_columns[5].find("div").text.replace(",","")
		# market_cap = currency_columns[6].find("div").text.replace(",","")
	
		# pdb.set_trace()
# 		df = df.append({
# 				'date': date,
# 				'opening_price': opening_price,
# 				'high_price': high_price,
# 				'low_price': low_price,
# 				'close_price': close_price,
# 				'currency_volume_USD': currency_volume_USD,
# 				'market_cap': market_cap
# 			}, ignore_index=True)
	
# df.to_csv("cmc_parsed_files/historical_cmc_dataset.csv")