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
	


# import urllib.request
# import urllib.error
# import os
# import ssl
# import datetime
# import time
# import json

# if not os.path.exists("html_files"):
# 	os.mkdir("html_files")

# if not os.path.exists("json_files"):
# 	os.mkdir("json_files")
	
# context = ssl._create_unverified_context()

# for i in range(192):


# 	# requesting p. 1 from coinmarketcap:
# 	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
# 	print("coinmarketcap" + current_time_stamp)
# 	f = open("html_files/cmcap" + current_time_stamp + ".html", "wb")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	# requesting p. 1 from coingecko:
# 	print("coingecko " + current_time_stamp)
# 	f = open("json_files/coingecko" + current_time_stamp + ".json", "w")
# 	try:
# 		response_1 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h%2C7d', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_1 = json.load(response_1)
# 		f.write(json.dumps(json_response_1))
# 	time.sleep(15)


# 	# requesting p. 2 from coinmarketcap:
# 	print("coinmarketcap page 2")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/2/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	# requesting p. 2 from coingecko: 
# 	print("coingecko page 2")
# 	try:
# 		response_2 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=2&sparkline=false&price_change_percentage=24h%2C7d', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_2 = json.load(response_2)
# 		f.write(json.dumps(json_response_2))
# 	time.sleep(15)


# 	# requesting p. 3 from coinmarketcap:
# 	print("coinmarketcap page 3")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/3/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	# requesting p. 3 from coingecko:
# 	print("coingecko page 3")
# 	try:
# 		response_3 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=3&sparkline=false&price_change_percentage=24h%2C7d', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_3 = json.load(response_3)
# 		f.write(json.dumps(json_response_3))
# 	time.sleep(15)

# 	# requesting p. 4 from both:
# 	print("coinmarketcap page 4")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/4/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	print("coingecko page 4")
# 	try:
# 		response_4 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=4&sparkline=false&price_change_percentage=24h%2C7d', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_4 = json.load(response_4)
# 		f.write(json.dumps(json_response_4))
# 	time.sleep(15)

# 	# requesting p. 5 from both:
# 	print("coinmarketcap page 5")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/5/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 		f.close()
# 	print("coingecko page 5")
# 	try:
# 		response_5 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=5&sparkline=false&price_change_percentage=24h%2C7d', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_5 = json.load(response_5)
# 		f.write(json.dumps(json_response_5))
# 		f.close()
# 	time.sleep(840)










# import urllib.request
# import urllib.error
# import os
# import ssl
# import datetime
# import time
# import json

# if not os.path.exists("html_files"):
# 	os.mkdir("html_files")

# if not os.path.exists("json_files"):
# 	os.mkdir("json_files")
	
# context = ssl._create_unverified_context()

# for i in range(192):
# 	# requesting from coinmarketcap:
# 	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
# 	print("coinmarketcap" + current_time_stamp)
# 	f = open("html_files/cmcap" + current_time_stamp + ".html", "wb")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	print(" page 2")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/2/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	print(" page 3")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/3/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	print(" page 4")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/4/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 	print(" page 5")
# 	try:
# 		response = urllib.request.urlopen("http://coinmarketcap.com/5/", context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		html = response.read()
# 		f.write(html)
# 		f.close()
	
# 	# requesting from coingecko:
# 	print("coingecko " + current_time_stamp)
# 	f = open("json_files/coingecko" + current_time_stamp + ".json", "w")
# 	try:
# 		response_1 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_1 = json.load(response_1)
# 		f.write(json.dumps(json_response_1))
# 	print(" results 250-499")
# 	try:
# 		response_2 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&sparkline=false', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 	else:
# 		json_response_2 = json.load(response_2)
# 		f.write(json.dumps(json_response_2))
# 	print(" result 500")
# 	try:
# 		response_3 = urllib.request.urlopen('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=1&page=500&sparkline=false', context=context)
# 	except urllib.error.HTTPError as e:
# 		print("HTTPError: {}".format(e.code))
# 		f.close()
# 	except urllib.error.URLError as e:
# 		print("URLError: {}".format(e.reason))
# 		f.close()
# 	else:
# 		json_response_3 = json.load(response_3)
# 		f.write(json.dumps(json_response_3))
# 		f.close()
# 	time.sleep(900)	

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
	

