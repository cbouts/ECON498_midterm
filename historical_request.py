import urllib.request
import urllib.error
import os
import ssl
import datetime
import time
import json
from bs4 import BeautifulSoup
import pandas as pd


context = ssl._create_unverified_context()

# for i in range(1):
# 	print("coinmarketcapdownload")
# 	f = open("html_files_trial/cmcap" + "1" + ".html", "wb")
# 	response = urllib.request.urlopen("http://coinmarketcap.com/all/views/all/", context=context)
# 	# ask: how do I get this to download 500 instead of 200????
# 	html = response.read()
# 	f.write(html)
# 	f.close()
# 	time.sleep(70)

# if not os.path.exists("historical_html_files"):
# 	os.mkdir("historical_html_files")

if not os.path.exists("historical_json_files"):
	os.mkdir("historical_json_files")


f = open("html_files_trial/cmcap1.html", "r")
soup = BeautifulSoup(f.read(), "html.parser")

currency_table = soup.find("tbody")
currency_rows = currency_table.find_all("tr")

for r in currency_rows:
	currency_columns = r.find_all("td")
	name = currency_columns[1].find("a").text
	link = currency_columns[1].find("a")["href"]

	# print("CMC historical " + name)
	# f = open("historical_html_files/" + name.replace(" ","_") + ".html", "wb")
	# try:
	# 	response = urllib.request.urlopen("http://coinmarketcap.com" + link + "historical-data/" + "?start=20191101&end=20201101", context=context)
	# except urllib.error.HTTPError as e:
	# 	print("  HTTPError: {}".format(e.code))
	# except urllib.error.URLError as e:
	# 	print("  URLError: {}".format(e.reason))
	# else:
	# 	html = response.read()
	# 	f.write(html)
	# 	f.close()
	# 	print("  success")


	print("GECKO historical Q1 " + name)
	f = open("historical_json_files/" + name.replace(" ","_") + "Q1.html", "w")
	try:
		response_1 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1572609600&to=1580475600', context=context)
	except urllib.error.HTTPError as e:
	 	print("  HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
	 	print("  URLError: {}".format(e.reason))
	else:
		json_response_1 = json.load(response_1)
		f.write(json.dumps(json_response_1))
		f.close()
		print("  success")
	time.sleep(60)

	print("GECKO historical Q2 " + name)
	f = open("historical_json_files/" + name.replace(" ","_") + "Q2.html", "w")
	try:
		response_2 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1580475601&to=1588248000', context=context)
	except urllib.error.HTTPError as e:
	 	print("  HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
	 	print("  URLError: {}".format(e.reason))
	else:
		json_response_2 = json.load(response_2)
		f.write(json.dumps(json_response_2))
		f.close()
		print("  success")
	time.sleep(60)

	print("GECKO historical Q3 " + name)
	f = open("historical_json_files/" + name.replace(" ","_") + "Q3.html", "w")
	try:
		response_3 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1588248001&to=1596196800', context=context)
	except urllib.error.HTTPError as e:
	 	print("  HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
	 	print("  URLError: {}".format(e.reason))
	else:
		json_response_3 = json.load(response_3)
		f.write(json.dumps(json_response_3))
		f.close()
		print("  success")
	time.sleep(60)

	print("GECKO historical Q4 " + name)
	f = open("historical_json_files/" + name.replace(" ","_") + "Q4.html", "w")
	try:
		response_4 = urllib.request.urlopen('http://api.coingecko.com/api/v3/coins/' + name.replace(" ","%20") + '/market_chart/range?vs_currency=usd&from=1596196801&to=1604235600', context=context)
	except urllib.error.HTTPError as e:
	 	print("  HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
	 	print("  URLError: {}".format(e.reason))
	else:
		json_response_4 = json.load(response_4)
		f.write(json.dumps(json_response_4))
		f.close()
		print("  success")
	time.sleep(60)






