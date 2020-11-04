import urllib.request
import urllib.error
# import requests.error
import os
import ssl
import datetime
import time
import json
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pdb
import csv, sys


context = ssl._create_unverified_context()

if not os.path.exists("historical_html_files"):
	os.mkdir("historical_html_files")

if not os.path.exists("historical_json_files"):
	os.mkdir("historical_json_files")

# IMPORT THE CSV
col_list = ["ath", "atl", "market_rank", "max_supply", "name", "roi", "total_supply"]
df_1 = pd.read_csv('cmc_parsed_files/cmc_deeplink.csv', usecols=col_list)
df_2 = df_1["name"]
for row in df_2:
	name = row
	geckolink = row.replace("-","%20")
	# print(row)
	# print(geckolink)

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
	time.sleep(60)

	# print("GECKO historical Q2 " + name)
	# f = open("historical_json_files/" + name + "Q2.json", "w")
	# try:
	# 	url = 'https://api.coingecko.com/api/v3/coins/' + geckolink + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600'
	# 	# for a test:
	# 	# 	url = 'http://api.coingecko.com/api/v3/coins/' + 'bitcoin' + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600'
	# 	r = requests.get(url)
	# except requests.HTTPError as e:
	#  	print("  HTTPError: {}".format(e.code))
	# else:
	# 	data = r.json()
	# 	f.write(json.dumps(data))
	# 	f.close()
	# 	print("  success")
	# time.sleep(60)


# filename = 'cmc_parsed_files/cmc_dataset.csv'
# with open (filename, 'rb') as f:
# 	reader = csv.reader(f)
# 	try:
# 		for row in reader:
# 			4


# f = open("cmc_parsed_files/cmc_dataset.csv", "rb")
# soup = BeautifulSoup(f.read())

# with open('cmc_parsed_files/cmc_dataset.csv') as csvfile:

# for i in range(1):
# 	print("coinmarketcapdownload")
# 	f = open("html_files_trial/cmcap" + "1" + ".html", "wb")
# 	response = urllib.request.urlopen("http://coinmarketcap.com/all/views/all/", context=context)
# 	# ask: how do I get this to download 500 instead of 200????
# 	html = response.read()
# 	f.write(html)
# 	f.close()
# 	time.sleep(70)
# ________________________________________________-
# if not os.path.exists("historical_html_files"):
# 	os.mkdir("historical_html_files")

# if not os.path.exists("historical_json_files"):
# 	os.mkdir("historical_json_files")

# f = open("html_files_trial/cmcap1.html", "r")
# soup = BeautifulSoup(f.read(), "html.parser")

# currency_table = soup.find("tbody")
# currency_rows = currency_table.find_all("tr")

# for c in currency_rows:
# 	currency_columns = c.find_all("td")
# 	name = currency_columns[1].find("a").text
# 	link = currency_columns[1].find("a")["href"]


# 	print("CMC historical " + name)
# 	f = open("historical_html_files/" + name.replace(" ","-") + ".html", "wb")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com" + link + "historical-data/" + "?start=20191101&end=20201101", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("  URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 		f.close()
# 		print("  success")
# # _______________________ Tried the requests format for coingecko below, wasn't sure if I got it right
	
# 	url = 'http://api.coingecko.com/api/v3/coins/' + 'bitcoin' + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600'
# 	r = requests.get(url)
# 	print(r.status_code)


# 	print("GECKO historical Q1 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","-") + "Q1.json", "w")
# 	try:
# 		url = 'http://api.coingecko.com/api/v3/coins/' + link.replace("/","").replace("-","%20") + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600'
# 		# for a test:
# 		# 	url = 'http://api.coingecko.com/api/v3/coins/' + 'bitcoin' + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600'
# 		r = requests.get(url)
# 		# may need context=context
# 	except requests.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	 	# is this correct?? or should I do print(r.status_code) and "except requests.Error"
# 	else:
# 		json_response_2 = json.loads(r)
# 		f.write(json.dumps(json_response_2))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)
# # _____________ will need to change these to match that format:

# 	print("GECKO historical Q2 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","-") + "Q2.json", "w")
# 	try:
# 		response_2 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1580475601&to=1588248000', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_2 = json.load(response_2)
# 		f.write(json.dumps(json_response_2))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

# 	print("GECKO historical Q3 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","-") + "Q3.json", "w")
# 	try:
# 		response_3 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1588248001&to=1596196800', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_3 = json.load(response_3)
# 		f.write(json.dumps(json_response_3))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

# 	print("GECKO historical Q4 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","-") + "Q4.json", "w")
# 	try:
# 		response_4 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1596196801&to=1604235600', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_4 = json.load(response_4)
# 		f.write(json.dumps(json_response_4))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

	


# _________________________________________________________________________


# __________ using urllib for gecko
# 	print("GECKO historical Q1 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","_") + "Q1.html", "w")
# 	try:
# 		response_1 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_1 = json.load(response_1)
# 		f.write(json.dumps(json_response_1))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

# 	print("GECKO historical Q2 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","_") + "Q2.html", "w")
# 	try:
# 		response_2 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1580475601&to=1588248000', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_2 = json.load(response_2)
# 		f.write(json.dumps(json_response_2))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

# 	print("GECKO historical Q3 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","_") + "Q3.html", "w")
# 	try:
# 		response_3 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1588248001&to=1596196800', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_3 = json.load(response_3)
# 		f.write(json.dumps(json_response_3))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

# 	print("GECKO historical Q4 " + name)
# 	f = open("historical_json_files/" + name.replace(" ","_") + "Q4.html", "w")
# 	try:
# 		response_4 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1596196801&to=1604235600', context=context)
# 	except urllib.error.HTTPError as e:
# 	 	print("  HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 	 	print("  URLError: {}".format(e.reason))
# 	else:
# 		json_response_4 = json.load(response_4)
# 		f.write(json.dumps(json_response_4))
# 		f.close()
# 		print("  success")
# 	time.sleep(60)

	# pdb.set_trace()












