from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import pdb

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()

# for one_file_name in glob.glob("historical_html_files/*.html"):
one_file_name = "historical_html_files/0x.html"
print("parse " + one_file_name)
f = open(one_file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()

for day in soup:
	date = soup.find('time_open')
	print(date)

# print(historical_html_files/0x.html)
# table = soup.find("tbody")
# currency_rows = soup.find_all("tr")
# for r in currency_rows:
# 	currency_columns = r.find_all("td")
# 	print(currency_columns[0])
