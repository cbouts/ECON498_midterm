import json
import pandas as pd 
import glob
import os


if not os.path.exists('coingecko_parsed_files'):
	os.mkdir('coingecko_parsed_files')

df = pd.DataFrame()
# will need to change the source folder in the line below:
# for json_file_name in glob.glob('json_files_trial/*.json'):
json_file_name = 'json_files_trial/coingecko20201101165039.json'
print(json_file_name)
scrape_time = os.path.basename(json_file_name).replace("coingecko","").replace(".json","")
f = open(json_file_name, "r")
json_data = json.load(f)
# for ["}"] in json_data:
# 	replace("},","},\n")
# print(json_data)

print(json_data[0])
# df = df.append({
      		'id': json_data['id'],
			'time': scrape_time
      		'symbol': json_data['symbol'],
      		'name': json_data['name'],
      		'logo': json_data['image'],
      		'current_price': json_data['current_price'],
      		'market_cap': json_data['market_cap'],
      		'market_cap_rank': json_data['market_cap_rank'],
	      	'total_supply': json_data['total_supply'],
	      	'max_supply': json_data['max_supply'],
      		'ath': json_data['ath'],
      		'ath_date': json_data['ath_date'],
      		'atl': json_data['atl'],
      		'atl_date': json_data['atl_date'],
      		'roi': json_data['roi'],
      		'price_change_percentage_24h_in_currency': json_data['price_change_percentage_24h_in_currency'],
      		'price_change_percentage_7d_in_currency': json_data['price_change_percentage_7d_in_currency']
# 	}, ignore_index=True)

# df.to_csv('parsed_files/coingecko_dataset.csv')


# print(json_data[0])
# # df = df.append({
#       		'id': json_data['id'],
# 			'time': scrape_time
#       		'symbol': json_data['symbol'],
#       		'name': json_data['name'],
#       		'logo': json_data['image'],
#       		'current_price': json_data['current_price'],
#       		'market_cap': json_data['market_cap'],
#       		'market_cap_rank': json_data['market_cap_rank'],
# #       	# 'fully_diluted_valuation': json_data['fully_diluted_valuation'],
# #       	# 'total_volume': json_data['total_volume'],
# #       	# 'high_24h': json_data['high_24h'],
# #       	# 'low_24h': json_data['low_24h'],
# #       	# 'price_change_24h': json_data['price_change_24h'],
# #       	# 'price_change_percentage_24h': json_data['price_change_percentage_24h'],
# #       	# 'market_cap_change_24h': json_data['market_cap_change_24h'],
# #       	# 'market_cap_change_percentage_24h': json_data['market_cap_change_percentage_24h'],
# #       	# 'circulating_supply': json_data['circulating_supply'],
# 	      	'total_supply': json_data['total_supply'],
# 	      	'max_supply': json_data['max_supply'],
#       		'ath': json_data['ath'],
# #       	# 'ath_change_percentage': json_data['ath_change_percentage'],
#       		'ath_date': json_data['ath_date'],
#       		'atl': json_data['atl'],
# #       	# 'atl_change_percentage': json_data['atl_change_percentage'],
#       		'atl_date': json_data['atl_date'],
#       		'roi': json_data['roi'],
# #       	# 'last_updated': json_data['last_updated'],
#       		'price_change_percentage_24h_in_currency': json_data['price_change_percentage_24h_in_currency'],
#       		'price_change_percentage_7d_in_currency': json_data['price_change_percentage_7d_in_currency']
# # 	}, ignore_index=True)


# # # df = df.append({
# # #       	'id': json_data[0],
# # #       	'symbol': json_data[1],
# # #       	'name': json_data[2],
# # #       	'image': json_data[3],
# # # 	    'current_price': json_data[4],
# # # 	    'market_cap': json_data[5],
# # # 	    'market_cap_rank': json_data[6],
# # # 	    'fully_diluted_valuation': json_data[7],
# # # 	    'total_volume': json_data[8],
# # # 	    'high_24h': json_data[9],
# # # 	    'low_24h': json_data[10],
# # # 	    'price_change_24h': json_data[11],
# # # 	    'price_change_percentage_24h': json_data[12],
# # # 	    'market_cap_change_24h': json_data[13],
# # # 	    'market_cap_change_percentage_24h': json_data[14],
# # # 	    'circulating_supply': json_data[15],
# # # 	    'total_supply': json_data[16],
# # # 	    'max_supply': json_data[17],
# # # 	    'ath': json_data[18],
# # # 	    'ath_change_percentage': json_data[19],
# # # 	    'ath_date': json_data[20],
# # # 	    'atl': json_data[21],
# # # 	    'atl_change_percentage': json_data[22],
# # # 	    'atl_date': json_data[23],
# # # 	    'roi': json_data[24],
# # # 	    'last_updated': json_data[25],
# # # 	    'price_change_percentage_24h_in_currency': json_data[26],
# # # 	    'price_change_percentage_7d_in_currency': json_data[27],
# # # 	    'time': scrape_time
# # # 	}, ignore_index=True)

# # print(json_data[0])
# print(df)

# df.to_csv('parsed_files/coingecko_dataset.csv')

# # ______________ from version before proper indexing:
# df = df.append({
      	# 'id': json_data['id'],
      	# 'symbol': json_data['symbol'],
      	# 'name': json_data['name'],
      	# 'logo': json_data['image'],
      	# 'current_price': json_data['current_price'],
      	# 'market_cap': json_data['market_cap'],
      	# 'market_cap_rank': json_data['market_cap_rank'],
      	# 'fully_diluted_valuation': json_data['fully_diluted_valuation'],
      	# 'total_volume': json_data['total_volume'],
      	# 'high_24h': json_data['high_24h'],
      	# 'low_24h': json_data['low_24h'],
      	# 'price_change_24h': json_data['price_change_24h'],
      	# 'price_change_percentage_24h': json_data['price_change_percentage_24h'],
      	# 'market_cap_change_24h': json_data['market_cap_change_24h'],
      	# 'market_cap_change_percentage_24h': json_data['market_cap_change_percentage_24h'],
      	# 'circulating_supply': json_data['circulating_supply'],
      	# 'total_supply': json_data['total_supply'],
      	# 'max_supply': json_data['max_supply'],
      	# 'ath': json_data['ath'],
      	# 'ath_change_percentage': json_data['ath_change_percentage'],
      	# 'ath_date': json_data['ath_date'],
      	# 'atl': json_data['atl'],
      	# 'atl_change_percentage': json_data['atl_change_percentage'],
      	# 'atl_date': json_data['atl_date'],
      	# 'roi': json_data['roi'],
      	# 'last_updated': json_data['last_updated'],
      	# 'price_change_percentage_24h_in_currency': json_data['price_change_percentage_24h_in_currency'],
      	# 'price_change_percentage_7d_in_currency': json_data['price_change_percentage_7d_in_currency']
# 	}, ignore_index=True)

# print(df)

# df.to_csv('parsed_files/coingecko_dataset.csv')

# _______________ from tom's version:

# if not os.path.exists('coingecko_parsed_files'):
# 	os.mkdir('coingecko_parsed_files')

# df = pd.DataFrame()

# for json_file_name in glob.glob('json_files/*.json'):	
# 	# json_file_name = "json_files/tmdb745721.json"
# 	print(json_file_name)
# 	scrape_time = os.path.basename(json_file_name).replace("coingecko","").replace(".json","")
# 	f = open(json_file_name, "r")
# 	json_data = json.load(f)

# 	# print(json_data)
# 	df = df.append({
# 			'adult': json_data['adult'],
# 			'backdrop_path': json_data['backdrop_path'],
# 			'belongs_to_collection': json_data['belongs_to_collection'],
# 			'budget': json_data['budget'],
# 			'genres': json_data['genres'],
# 			'homepage': json_data['homepage'],
# 			'id': json_data['id'],
# 			'imdb_id': json_data['imdb_id'],
# 			'original_language': json_data['original_language'],
# 			'original_title': json_data['original_title'],
# 			'overview': json_data['overview'],
# 			'popularity': json_data['popularity'],
# 			'poster_path': json_data['poster_path'],
# 			'production_companies': json_data['production_companies'],
# 			'production_countries': json_data['production_countries'],
# 			'release_date': json_data['release_date'],
# 			'revenue': json_data['revenue'],
# 			'runtime': json_data['runtime'],
# 			'spoken_languages': json_data['spoken_languages'],
# 			'status': json_data['status'],
# 			'tagline': json_data['tagline'],
# 			'title': json_data['title'],
# 			'video': json_data['video'],
# 			'vote_average': json_data['vote_average'],
# 			'vote_count': json_data['vote_count']
# 		}, ignore_index=True)

# print(df)

# df.to_csv('parsed_files/coingecko_dataset.csv')



	# 'id': json_data['id'],
 #      	'symbol': json_data['symbol'],
 #      	'name': json_data['name'],
 #      	'logo': json_data['image'],
 #      	'current_price': json_data['current_price'],
 #      	'market_cap': json_data['market_cap'],
 #      	'market_cap_rank': json_data['market_cap_rank'],
 #      	'fully_diluted_valuation': json_data['fully_diluted_valuation'],
 #      	'total_volume': json_data['total_volume'],
 #      	'high_24h': json_data['high_24h'],
 #      	'low_24h': json_data['low_24h'],
 #      	'price_change_24h': json_data['price_change_24h'],
 #      	'price_change_percentage_24h': json_data['price_change_percentage_24h'],
 #      	'market_cap_change_24h': json_data['market_cap_change_24h'],
 #      	'market_cap_change_percentage_24h': json_data['market_cap_change_percentage_24h'],
 #      	'circulating_supply': json_data['circulating_supply'],
 #      	'total_supply': json_data['total_supply'],
 #      	'max_supply': json_data['max_supply'],
 #      	'ath': json_data['ath'],
 #      	'ath_change_percentage': json_data['ath_change_percentage'],
 #      	'ath_date': json_data['ath_date'],
 #      	'atl': json_data['atl'],
 #      	'atl_change_percentage': json_data['atl_change_percentage'],
 #      	'atl_date': json_data['atl_date'],
 #      	'roi': json_data['roi'],
 #      	'last_updated': json_data['last_updated'],
 #      	'price_change_percentage_24h_in_currency': json_data['price_change_percentage_24h_in_currency'],
 #      	'price_change_percentage_7d_in_currency': json_data['price_change_percentage_7d_in_currency']
