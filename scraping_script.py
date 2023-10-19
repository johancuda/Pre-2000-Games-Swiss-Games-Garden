import requests
import json
import pandas as pd

def main():

	# TODO : optimize this
	# List of links to get all the gaems
	url_list = ["https://api.swissgames.garden/search/games?page=0&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#",
	"https://api.swissgames.garden/search/games?page=1&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#",
	"https://api.swissgames.garden/search/games?page=2&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#",
	"https://api.swissgames.garden/search/games?page=3&release_year_range%5Bend%5D=2000&release_year_range%5Bstart%5D=1967#"]

	games_dict = dict()


	# Requets json from API and turns it into a dict
	for url in url_list:
		response = requests.get(url)
		api_file = response.json()
		hits = api_file['hits']['hits']

		for idx in hits:

			gameId = idx['_id']

			game = dict()

			game['id'] = gameId
			game['title'] = idx['_source']['title']
			game['year'] = idx['_source']['releases_years'][0]['year']
			games_dict[gameId] = game
		
	# Pretty print
	print(json.dumps(games_dict, indent=4, sort_keys=True))


	# Turns dict into a Dataframe
	df = pd.DataFrame.from_dict(games_dict, orient ='index')

	# Dataframe to excel sheet
	df.to_excel("/Users/johancuda/Documents/UNIL/Synergia/scraping_sgg/test2.xlsx", sheet_name = 'test', index= False)







if __name__ == '__main__':
	main()