from bs4 import BeautifulSoup
import os
import glob
import pandas as pd
import pdb

if not os.path.exists("cmc_parsed_files"):
	os.mkdir("cmc_parsed_files")

df = pd.DataFrame()

for one_file_name in glob.glob("deep_link_html/*.html"):
	print(one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), "html.parser")
	f.close()
	
	tables = soup.find("tbody", {"class": "cmc-details-panel-about__table"})
	rows = soup.find_all("tr")

	if len(tables)==1:
	# cmcap_deeplink.py downloaded the htmls in a way that some have all rows in one order within one tbody, but /n
	# others have four tbodys containing the same rows in a different order. This is the reason for the "if/else" /n
	# structure. within each of these groups of htmls, some coins have incomplete data listed. This program skips over them and notes /n
	# them in the terminal with an error message. this is the reason for the try/except structure.
		try:
			market_rank = rows[2].find("td").text.replace("#","")
			ath = rows[8].find("div").text.replace("$","").replace(",","").replace(" USD","")
			atl = rows[9].find("div").text.replace("$","").replace(",","").replace(" USD","")
			roi = rows[1].find("span").text
			total_supply = rows[6].find("td").text.replace(",","")
			max_supply = rows[7].find("td").text.replace(",","")

			df = df.append({
						'name': one_file_name.replace(".html",""),
						'market_rank': market_rank,
						'ath': ath,
						'atl': atl,
						'roi': roi,
						'total_supply': total_supply,
						'max_supply': max_supply
							}, ignore_index=True)
		except:
			print(" ERROR: WEBSITE HAS INCOMPLETE DATA FOR " + one_file_name.replace(".html",""))
		
	else:
		try:
			market_rank = rows[4].find("td").text.replace("#","")
			ath = rows[13].find("div").text.replace("$","").replace(",","").replace(" USD","")
			atl = rows[14].find("div").text.replace("$","").replace(",","").replace(" USD","")
			roi = rows[15].find("span")
			# roi = rows[15].find("span").text
			total_supply = rows[17].find("td").text.replace(",","")
			max_supply = rows[18].find("td").text.replace(",","")

			df = df.append({
						'name': one_file_name.replace(".html",""),
						'market_rank': market_rank,
						'ath': ath,
						'atl': atl,
						'roi': roi,
						'total_supply': total_supply,
						'max_supply': max_supply
							}, ignore_index=True)
		except: 
			print(" ERROR: WEBSITE HAS INCOMPLETE DATA FOR " + one_file_name.replace(".html",""))

df.to_csv("cmc_parsed_files/cmc_deeplink.csv")






