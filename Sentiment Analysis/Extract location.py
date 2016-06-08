import json
import sys

def load_json(file):
	with open(file) as data_file:    
	    data = json.load(data_file)
	return data

if __name__=='__main__':

	data = load_json("GeoTweets.json")
	file = open("geo.txt", "w")


	for item in data['docs']:
		latitude = item['location']['coordinates'][0]
		longitude = item['location']['coordinates'][1]
		file.write(str(latitude) + " " +str(longitude))
		file.write("\n")
	
	file.close()