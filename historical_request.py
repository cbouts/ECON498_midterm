import urllib.request
import urllib.error
import os
import ssl
import datetime
import time
import json
from BS4 import BeautifulSoup

if not os.path.exists("historical_html_files"):
	os.mkdir("historical_html_files")

# if not os.path.exists("historical_json_files"):
# 	os.mkdir("historical_json_files")

context = ssl._create_unverified_context()

if not os.path.exists("html_files_trial/entire.html"):
	os.mkdir("html_files_trial/entire.html")
	for i in range(1):
		print("coinmarketcapdownload")
		f = open("html_files_trial/entire.html", "wb")
		response = urllib.request.urlopen("http://coinmarketcap.com/all/views/all/", context=context)
		html = response.read()
		f.write(html)
		f.close()
		time.sleep(70)

f = open("html_files_trial/entire.html", "r")
soup = BeautifulSoup(f.read(), features='lxml')
coin_link = []
currency_name = []
table = soup.find("table", {"id": "currencies-all"})





