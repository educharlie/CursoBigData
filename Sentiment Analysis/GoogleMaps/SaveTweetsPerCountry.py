# coding: utf-8
import json
import sys
import numpy as np
from operator import itemgetter
from geopy.geocoders import Nominatim

def load_json(file):
	with open(file) as data_file:    
	    data = json.load(data_file)
	return data

def get_location(country_code):
	geolocator = Nominatim()
	location = geolocator.geocode(country_code)
	return location

def get_avergate(code):
	return int(sum([value['count'] for value in filter(lambda x: x['code'] == code, data)]))

if __name__=='__main__':

	data = load_json("HeatmapData.json")

	codes = list(set([value['code'] for value in data]))

	f = open('TweetsPerCountry.txt', 'w')

	for code in codes:
		if code == 'AE':
			f.write("United Arab Emirates,"+ str(get_avergate(code)))
		elif code == 'PK':
			f.write("Pakistan,"+ str(get_avergate(code)))
		elif code == 'SA':
			f.write("South Africa,"+ str(get_avergate(code)))
		elif code == 'BE':
			f.write("Belgium,"+ str(get_avergate(code)))
		elif code == 'PA':
			f.write("Panama,"+ str(get_avergate(code)))
		elif code == 'CY':
			f.write("Cyprus,"+ str(get_avergate(code)))
		elif code == 'TH':
			f.write("Thailand,"+ str(get_avergate(code)))
		elif code == 'ES':
			f.write("Spain,"+ str(get_avergate(code)))
		elif code == 'TR':
			f.write("Turkey,"+ str(get_avergate(code)))
		elif code == 'JP':
			f.write("Japan,"+ str(get_avergate(code)))
		elif code == 'DZ':
			f.write("Algeria,"+ str(get_avergate(code)))
		elif code == 'EG':
			f.write("Egypt,"+ str(get_avergate(code)))
		elif code == 'QA':
			f.write("Qatar,"+ str(get_avergate(code)))
		elif code == 'GR':
			f.write("Greece,"+ str(get_avergate(code)))
		elif code == 'IQ':
			f.write("Iraq,"+ str(get_avergate(code)))
		elif code == 'KR':
			f.write("Korea,"+ str(get_avergate(code)))
		elif code == 'IN':
			f.write("India,"+ str(get_avergate(code)))
		elif code == 'YE':
			f.write("Yemen,"+ str(get_avergate(code)))
		else:
			location = get_location(code)
			f.write(str(location) + ","+ str(get_avergate(code)))
		f.write("\n")
		
	f.close()

