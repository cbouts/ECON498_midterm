import urllib.request
import urllib.error
import os
import ssl
import datetime
import time
import json
from bs4 import BeautifulSoup
import pandas as pd

if not os.path.exists("historical_html_files"):
	os.mkdir("historical_html_files")

# if not os.path.exists("historical_json_files"):
# 	os.mkdir("historical_json_files")

context = ssl._create_unverified_context()

# if not os.path.exists("html_files_trial/entire.html"):
# 	os.mkdir("html_files_trial/entire.html")
# for i in range(1):
# 	print("coinmarketcapdownload")
# 	f = open("html_files_trial/cmcap" + "1" + ".html", "wb")
# 	response = urllib.request.urlopen("http://coinmarketcap.com/all/views/all/", context=context)
# 	html = response.read()
# 	f.write(html)
# 	f.close()
# 	time.sleep(70)

f = open("html_files_trial/cmcap1.html", "r")
soup = BeautifulSoup(f.read(), "html.parser")
coin_link = []
currency_name = []
currency_table = soup.find("tbody")
# currency_table = soup.find("table", {"id": "currencies-all"})
currency_rows = currency_table.find_all("tr")
for r in currency_rows:
	currency_columns = r.find_all("td")
	name = currency_columns[1].find("a").text
	link = currency_columns[1].find("a")["href"]
	print(link)

currency_name.append(name)
coin_link.append(link)

# make the range 500 once you can figure out how to get all 500 on the same page.
for i in range(2):
	f = open("historical_html_files/" + currency_name[i] + ".html", "wb")
	url = "http://coinmarketcap.com" + coin_link[i] + "historical-data/" + "?start=20191101&end=20201101"
	response = urllib.request.urlopen("http://coinmarketcap.com" + link[i] + "historical-data/" + "?start=20191101&end=20201101", context=context)
	html = response.read()
	f.close()
	time.sleep(30)








