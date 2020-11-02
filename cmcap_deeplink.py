import urllib.request
import os
import time
import pandas as pd
import 


if not os.path.exists("deep_link_html"):
	os.mkdir("deep_link_html")

df = pd.read_csv("parsed_files/cmc_dataset.csv")
# make sure you have the right csv here.

print(df['link'])
# loop thorugh links
# testing this is around 8 minutes in 10/06

for link in df['link']:
# figure out how to do this only for the first 500 links
	print('link')
	filename = link.replace('/currencies/', '')
	response = urllib.request.urlopen("https://coinmarketcap.com/" + link)
	html = response.read()
	open('deep_link_html/' + filename  + '.html', 'wb')
	f.write(html)
	f.close()
	time.sleep(30)

