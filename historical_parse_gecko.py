import json
import pandas as pd 
import glob
import os
from datetime import datetime
import tzlocal

if not os.path.exists('coingecko_parsed_files'):
	os.mkdir('coingecko_parsed_files')

df = pd.DataFrame()

for json_file_name in glob.glob('historical_json_files/*.json'):
# json_file_name = 'historical_json_files/0x.json'
	print("parsing " + json_file_name)
	f = open(json_file_name, "r")
	json_data = json.load(f)
	for i in range(1,365):
		unix_timestamp = json_data['prices'][i][0]
		local_timezone = tzlocal.get_localzone()
		local_time = datetime.fromtimestamp(unix_timestamp/1000, local_timezone)
		date = local_time.strftime("%Y%m%d")
		print(date)
		
		df = df.append({
				'date': datetime.datetime.utcfromtimestamp(unix_timestamp).strftime("%Y%m%d%H%M%S")
				# CONVERT THIS!
				'price': json_data['prices'][i][1]
				'market_caps': json_data['market_caps'][i][1]
				'total_volumes': json_data['total_volumes'][i][1]
			}, ignore_index=True)
	

df.to_csv('parsed_files/historical_coingecko_dataset.csv')
