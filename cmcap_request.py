import urllib.request
import os
import ssl
import datetime
import time

if not os.path.exists("html_files"):
	os.mkdir("html_files")

for i in range(192):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files/cmcap" + current_time_stamp + ".html", "wb")
	context = ssl._create_unverified_context()
	response = urllib.request.urlopen("http://coinmarketcap.com/", context=context)
	html = response.read()
	# print(html)
	f.write(html)
	f.close()
	time.sleep(900)

