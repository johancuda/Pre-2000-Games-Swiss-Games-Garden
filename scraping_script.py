import requests
import json
import pandas as pd

def main():

	# TODO : optimize this
	# List of links to get all the games
	url_list = ["https://api.swissgames.garden/search/games?page=0&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#",
	"https://api.swissgames.garden/search/games?page=1&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#",
	"https://api.swissgames.garden/search/games?page=2&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#",
	"https://api.swissgames.garden/search/games?page=3&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#"]

	games_dict = dict()


	# Requets json from API and turns it into a dictionary
	for url in url_list:
		response = requests.get(url)
		api_file = response.json()
		hits = api_file['hits']['hits']

		for idx in hits:

			gameId = idx['_id']

			game = dict()

			game["Entered by"] = ""
			game['Number'] = gameId
			game['Game'] = idx['_source']['title']
			game["Thumbnail"] = ""
			if idx['_source']['medias']:
				game["Cover image"] = "https://api.swissgames.garden"+ idx['_source']['medias'][0]['href']
			else:
				game["Cover image"] = ''
			game["Screenshot 1"] = ""
			game["Screenshot 2"] = ""
			game["Screenshot 3"] = ""
			game['Year'] = idx['_source']['releases_years'][0]['year']
			if 'studios' in idx["_source"]:
				game["Developer studio"] = idx["_source"]['studios'][0]['name']
			else:
				game["Developer studio"] = ""
			game["Publisher"] = ""
			game["Main developer"] = ""
			if 'people' in idx['_source']:
				game["All involved Person (Developers; Programm; Grafik; Musik; usw.)"] = ','.join([person['fullname'] for person in idx['_source']['people']])
			else:
				game["All involved Person (Developers; Programm; Grafik; Musik; usw.)"] = ""
			game['Platform'] = ','.join([platform['platform_name'] for platform in idx['_source']['releases']])
			if 'genres' in idx['_source']:
				game['Genre'] = ','.join([genre['name'] for genre in idx['_source']['genres']])
			else:
				game['Genre'] = ""
			game['Setting'] = ''
			game["Source 1"] = ""
			game["Source 2"] = ""
			game["Source 3"] = ""
			game["Reviews"] = ""
			game["Article"] = ""
			game["Complete"] = ""
			game['Online'] = ''
			games_dict[gameId] = game
		
	# Pretty print
	#print(json.dumps(games_dict, indent=4, sort_keys=True))


	# Turns dict into a Dataframe
	df = pd.DataFrame.from_dict(games_dict, orient ='index')

	# Dataframe to excel sheet
	df.to_excel("./sgg_data.xlsx", sheet_name = 'data', index= False)







if __name__ == '__main__':
	main()