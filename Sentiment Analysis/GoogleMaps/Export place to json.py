import json
import sys
import tweet_classifier.classifier as classifier
import couchdb

from nltk import wordpunct_tokenize
from nltk.corpus import stopwords
from alchemyapi import AlchemyAPI
from geopy.geocoders import Nominatim
alchemyapi = AlchemyAPI()

def _calculate_languages_ratios(text):
    languages_ratios = {}
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        words_set = set(words)
        common_elements = words_set.intersection(stopwords_set)

        languages_ratios[language] = len(common_elements)

    return languages_ratios

def detect_language(text):
    ratios = _calculate_languages_ratios(text)
    most_rated_language = max(ratios, key=ratios.get)
    return most_rated_language

def load_json(file):
	with open(file) as data_file:    
	    data = json.load(data_file)
	return data

def write_json(file, data):
	with open(file, 'w') as json_file:
		json.dump(data, json_file)

def get_location(country_code):
	geolocator = Nominatim()
	location = geolocator.geocode(country_code)
	print(country_code)
	print((location.latitude, location.longitude))

def create_json(data):
	get_location(data['doc']['place']["country_code"])
	return {'text': data['doc']['text'],'source': data['doc']['source'],'retweeted': data['doc']['retweeted'],
	'profile_image': data['doc']['user']['profile_image_url_https'],'screen_name': data['doc']['user']['screen_name'],
	'created_at': data['doc']['created_at'], 'sentiment': data['sentiment'], 'polarity': data['polarity'], 
	'subjetivity' : data['subjectivity'], 'location' : data['doc']['geo'], 'country_code' : data['doc']['place']["country_code"]}

if __name__=='__main__':

	data = load_json("dbtest.json")
	result = {"docs":[]}

	for item in data['docs']:
		try:
			if item['doc']['place'] is not None:
				text = item['doc']['text']
				language = detect_language(text)

				if language == "english":
					sentiment = classifier.doSentimentAnalysis(text)
					item['sentiment'] = sentiment["sentiment"]
					item['polarity'] = sentiment["polarity"]
					item['subjectivity'] = sentiment["subjectivity"]
				else:
					response = alchemyapi.sentiment("text", text)
					if response["status"] == "OK":
						item['sentiment'] = response["docSentiment"]["type"]
						if item['sentiment'] != "neutral":
							item['polarity'] = float(response["docSentiment"]["score"])
						else:
							item['polarity'] = 'NA'
					else:
						item['sentiment'] = 'NA'
						item['polarity'] = 'NA'
					item['subjectivity'] = 'NA'
				result['docs'].append(create_json(item))

		except KeyError: 
			pass
			
	write_json("PlaceTweets.json",result)

