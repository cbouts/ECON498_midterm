import json
# import pandas as pd 
# import glob
# import os


json_file_name = "json_files/coingecko20201027235259.json"
f = open(json_file_name, "r")
json_data = json.load(f)
print(json_data)
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
