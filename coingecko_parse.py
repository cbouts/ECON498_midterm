import json
import pandas as pd 
import glob
import os

if not os.path.exists('coingecko_parsed_files'):
	os.mkdir('coingecko_parsed_files')

df = pd.DataFrame()
for json_file_name in glob.glob('json_files_2/*.json'):
# json_file_name = 'json_files_trial/coingecko20201101164950.json'
	print("parsing" + json_file_name)
	scrape_time = os.path.basename(json_file_name).replace("coingecko","").replace(".json","")
	f = open(json_file_name, "r")
	json_data = json.load(f)
	
	for coin in json_data:
	
		df = df.append({
			    'id': coin['id'],
			    'time': scrape_time,
	      		'symbol': coin['symbol'],
				'name': coin['name'],
				'logo': coin['image'],
				'current_price': coin['current_price'],
				'market_cap': coin['market_cap'],
				'market_cap_rank': coin['market_cap_rank'],
				'total_volume': coin['total_volume'],
				'circulating_supply': coin['circulating_supply'],
				'total_supply': coin['total_supply'],
				'max_supply': coin['max_supply'],
				'ath': coin['ath'],
				'ath_date': coin['ath_date'],
				'atl': coin['atl'],
				'atl_date': coin['atl_date'],
				'roi': coin['roi']
			}, ignore_index=True)

df.to_csv('coingecko_parsed_files/coingecko_dataset.csv')

