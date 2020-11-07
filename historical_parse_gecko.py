import json
import pandas as pd 
import glob
import os
from datetime import datetime
import tzlocal
# import pdb

if not os.path.exists('coingecko_parsed_files'):
	os.mkdir('coingecko_parsed_files')

df = pd.DataFrame()

for json_file_name in glob.glob('historical_json_files/*.json'):
# json_file_name = 'historical_json_files/balancer.json'

	# print("parsing " + json_file_name)
	f = open(json_file_name, "r")
	json_data = json.load(f)
	# print(len(json_data['prices']))
	if len(json_data['prices'])>365:
		for i in (0,365):
			unix_timestamp = json_data['prices'][i][0]
			local_timezone = tzlocal.get_localzone()
			local_time = datetime.fromtimestamp(unix_timestamp/1000, local_timezone)
			date = local_time.strftime("%Y%m%d")
	
			prices = json_data['prices'][i][1]
			market_caps = json_data['market_caps'][i][1]
			total_volumes = json_data['total_volumes'][i][1]
		
			df = df.append({
				'date': date,
				# CONVERT THIS!
				'prices': prices,
				'market_caps': market_caps,
				'total_volumes': total_volumes,
				}, ignore_index=True)
	else:
		print("ERROR: incomplete data for " + json_file_name.replace("historical_json","").replace(".json",""))
	
df.to_csv('parsed_files/historical_coingecko_dataset.csv')
