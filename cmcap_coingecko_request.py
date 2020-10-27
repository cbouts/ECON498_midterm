import urllib.request
import urllib.error
import os
import ssl
import datetime
import time
import json

if not os.path.exists("html_files"):
	os.mkdir("html_files")

if not os.path.exists("json_files"):
	os.mkdir("json_files")
	
context = ssl._create_unverified_context()


for i in range(192):
	# requesting from coinmarketcap:
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print("coinmarketcap" + current_time_stamp)
	f = open("html_files/cmcap" + current_time_stamp + ".html", "wb")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
	print(" page 2")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/2/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
	print(" page 3")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/3/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
	print(" page 4")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/4/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
	print(" page 5")
	try:
		response = urllib.request.urlopen("http://coinmarketcap.com/5/", context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		html = response.read()
		f.write(html)
	
	# requesting from coingecko:
	print("coingecko " + current_time_stamp)
	f = open("json_files/coingecko" + current_time_stamp + ".json", "w")
	try:
		response_1 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false', context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		json_response_1 = json.load(response_1)
		f.write(json.dumps(json_response_1))
	print(" results 250-499")
	try:
		response_2 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&sparkline=false', context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		json_response_2 = json.load(response_2)
		f.write(json.dumps(json_response_2))
	print(" result 500")
	try:
		response_3 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=500&sparkline=false', context=context)
	except urllib.error.HTTPError as e:
		print("HTTPError: {}".format(e.code))
	except urllib.error.URLError as e:
		print("URLError: {}".format(e.reason))
	else:
		json_response_3 = json.load(response_3)
		f.write(json.dumps(json_response_3))
	time.sleep(900)	

	# without try/except/else statements:
	# requesting from coinmarketcap:
	# f = open("html_files/cmcap" + current_time_stamp + ".html", "wb")
	# response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
	# html = response.read()
	# f.write(html)
	# response = urllib.request.urlopen("http://coinmarketcap.com/2/", context=context)
	# html = response.read()
	# f.write(html)
	# response = urllib.request.urlopen("http://coinmarketcap.com/3/", context=context)
	# html = response.read()
	# f.write(html)
	# response = urllib.request.urlopen("http://coinmarketcap.com/4/", context=context)
	# html = response.read()
	# f.write(html)
	# response = urllib.request.urlopen("http://coinmarketcap.com/5/", context=context)
	# html = response.read()
	# f.write(html)
	# f.close()

	# requesting from coingecko:
	# print("coingecko " + current_time_stamp)
	# response_1 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false', context=context)
	# json_response_1 = json.load(response_1)
	# response_2 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&sparkline=false', context=context)
	# json_response_2 = json.load(response_2)
	# response_3 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=500&sparkline=false', context=context)
	# json_response_3 = json.load(response_3)
	# f = open("json_files/coingecko" + current_time_stamp + ".json", "w")
	# f.write(json.dumps(json_response_1))
	# f.write(json.dumps(json_response_2))
	# f.write(json.dumps(json_response_3))
	# f.close()
	# time.sleep(900)	


# API LINKS:
	# # first 249 coins:
	# https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false
	# # coins 250-499:
	# https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&sparkline=false
	# # 500th coin:
	# https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=500&sparkline=false
	

