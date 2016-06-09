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
	return int(np.average([value['count'] for value in filter(lambda x: x['code'] == code, data)]))

if __name__=='__main__':

	data = load_json("HeatmapData.json")

	codes = list(set([value['code'] for value in data]))

	f = open('SentimentPerLocation.txt', 'w')
	f.write('[')

	for code in codes:
		if code == 'AE':
			f.write('{lat:'+ str(25.276987) + ', lng:' + str(55.296249) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'PK':
			f.write('{lat:'+ str(32.294445) + ', lng:' + str(72.349724) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'SA':
			f.write('{lat:'+ str(26.195246) + ', lng:' + str(28.034088) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'BE':
			f.write('{lat:'+ str(50.985996) + ', lng:' + str(4.836522) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'PA':
			f.write('{lat:'+ str(8.983333) + ', lng:' + str(-79.516670) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'CY':
			f.write('{lat:'+ str(35.095192) + ', lng:' + str(33.203430) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'TH':
			f.write('{lat:'+ str(13.736717) + ', lng:' + str(100.523186) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'ES':
			f.write('{lat:'+ str(40.419044) + ', lng:' + str(-3.298925) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'TR':
			f.write('{lat:'+ str(41.015137) + ', lng:' + str(28.979530) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'JP':
			f.write('{lat:'+ str(35.685360) + ', lng:' + str(139.753372) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'DZ':
			f.write('{lat:'+ str(36.457741) + ', lng:' + str(7.423325) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'EG':
			f.write('{lat:'+ str(30.047503) + ', lng:' + str(31.233702) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'QA':
			f.write('{lat:'+ str(25.286106) + ', lng:' + str(51.534817) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'GR':
			f.write('{lat:'+ str(38.246639) + ', lng:' + str(21.734573) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'IQ':
			f.write('{lat:'+ str(31.833332) + ', lng:' + str(47.150002) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'KR':
			f.write('{lat:'+ str(37.532600) + ', lng:' + str(127.024612) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'IN':
			f.write('{lat:'+ str(24.780010) + ', lng:' + str(84.981827) +', count: ' + str(get_avergate(code)) + '},')
		elif code == 'YE':
			f.write('{lat:'+ str(12.800000) + ', lng:' + str(45.033333) +', count: ' + str(get_avergate(code)) + '},')
		else:
			location = get_location(code)
			f.write('{lat:'+ str(location.latitude) + ', lng:' + str(location.longitude) +', count: ' + str(get_avergate(code)) + '},')
		
	f.write(']')
	f.close()

