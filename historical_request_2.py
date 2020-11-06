import urllib.request
import urllib.error
# import requests.error
import os
import ssl
import datetime
import time
import json
import pandas as pd
import requests
import csv, sys


context = ssl._create_unverified_context()

if not os.path.exists("historical_html_files"):
	os.mkdir("historical_html_files")

if not os.path.exists("historical_json_files"):
	os.mkdir("historical_json_files")

# IMPORT THE DEEPLINK CSV TO GET NAMES TO FEED INTO LINKS
col_list = ["ath", "atl", "market_rank", "max_supply", "name", "roi", "total_supply"]
df_1 = pd.read_csv('cmc_parsed_files/cmc_deeplink.csv', usecols=col_list)
df_2 = df_1["name"]
for row in df_2:
	name = row
	geckolink = row.replace("-","%20")
	# print(row)
	# print(geckolink)
	if os.path.exists("historical_html_files/" + name + ".html"):
		print(name + ".html already exists.")
	else:
		print("CMC historical " + name)
		f = open("historical_html_files/" + name + ".html", "wb")
		url = "https://coinmarketcap.com/currencies/" + name + "/historical-data/" + "?start=20191101&end=20201101"
		# pdb.set_trace()
		try:
			response = urllib.request.urlopen(url, context=context)
		except urllib.error.HTTPError as e:
			print("  HTTPError: {}".format(e.code))
		except urllib.error.URLError as e:
			print("  URLError: {}".format(e.reason))
		else:
			html = response.read()
			f.write(html)
			f.close()
			print("  success")
		time.sleep(30)

	if os.path.exists("historical_json_files/" + name + ".json"):
		print(name + ".json already exists.")
	else:
		print("GECKO historical " + name)
		f = open("historical_json_files/" + name + ".json", "w")
		try:
			url = 'https://api.coingecko.com/api/v3/coins/' + geckolink + '/market_chart/range?vs_currency=usd&from=1572609600&to=1604235600'
			# for a test:
			# 	url = 'http://api.coingecko.com/api/v3/coins/' + 'bitcoin' + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600'
			r = requests.get(url)
		except requests.HTTPError as e:
		 	print("  HTTPError: {}".format(e.code))
		else:
			data = r.json()
			f.write(json.dumps(data))
			f.close()
			print("  success")
		time.sleep(70)













