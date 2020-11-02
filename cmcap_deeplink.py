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
	filename = link.replace('/currencies/', '')
	if os.path.exists("deep_link_html/" + filename + ".html")
		print(filename + ".html already exists.")
		# if statement makes it robust against interruptions, also ensures that we don't re-download the same files once it has looped through the first 500 links.
	else
		print("downloading " + 'link')
		response = urllib.request.urlopen("https://coinmarketcap.com/" + link)
		html = response.read()
		open('deep_link_html/' + filename + '.html.temp', 'wb')
		# .temp is added to prevent writing empty files when we have interruptions (around 32:50 of 10/06). The file is only renamed into the final format after everything is already written properly. temp prevents it from stopping when it messes up.
		f.write(html)
		f.close()
		os.rename("deep_link_html/" + filename + '.html.temp', 'deep_link_html/' + filename + '.html')
		time.sleep(30)

