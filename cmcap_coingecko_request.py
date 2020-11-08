# using the format of 5 pages which I already wrote the cmcap parse file for:
import urllib.request
import urllib.error
import os
import ssl
import datetime
import time
import json

if not os.path.exists("html_files_2"):
	os.mkdir("html_files_2")

if not os.path.exists("json_files_2"):
	os.mkdir("json_files_2")


context = ssl._create_unverified_context()

for i in range(192):


	# requesting p. 1 from coinmarketcap and the first 250 coins from coingecko:
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coinmarketcap" + current_time_stamp)
	f = open("html_files_2/cmcap" + current_time_stamp + ".html", "wb")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
		f.close()

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coingecko " + current_time_stamp)
	f = open("json_files_2/coingecko" + current_time_stamp + ".json", "w")
	try:
		response_1 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=24h%2C7d', context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		json_response_1 = json.load(response_1)
		f.write(json.dumps(json_response_1))
		f.close()
	time.sleep(15)


	# requesting p. 2 from coinmarketcap and coins 251-500 from coingecko:
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coinmarketcap" + current_time_stamp)
	f = open("html_files_2/cmcap" + current_time_stamp + ".html", "wb")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/2/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
		f.close()

	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coingecko " + current_time_stamp)
	f = open("json_files_2/coingecko" + current_time_stamp + ".json", "w")
	try:
		response_2 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=250&page=2&sparkline=false&price_change_percentage=24h%2C7d', context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		json_response_2 = json.load(response_2)
		f.write(json.dumps(json_response_2))
		f.close()
	time.sleep(15)


	# requesting p. 3 from coinmarketcap:
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coinmarketcap" + current_time_stamp)
	f = open("html_files_2/cmcap" + current_time_stamp + ".html", "wb")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/3/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
		f.close()
	time.sleep(15)

	# requesting p. 4 from coinmarketcap:
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coinmarketcap" + current_time_stamp)
	f = open("html_files_2/cmcap" + current_time_stamp + ".html", "wb")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/4/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
		f.close()
	time.sleep(15)

	# requesting p. 5:
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coinmarketcap" + current_time_stamp)
	f = open("html_files_2/cmcap" + current_time_stamp + ".html", "wb")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/5/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
		f.close()
		print("    ")
	time.sleep(840)

