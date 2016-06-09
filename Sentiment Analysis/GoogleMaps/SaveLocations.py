# coding: utf-8
import json
import sys

from geopy.geocoders import Nominatim

def load_json(file):
	with open(file) as data_file:    
	    data = json.load(data_file)
	return data

def get_location(country_code):
	geolocator = Nominatim()
	location = geolocator.geocode(country_code)
	return location

if __name__=='__main__':

	data = load_json("HeatmapData.json")

	f = open('workfile', 'w')
	f.write('[')

	for item in data['docs']:
		print(item["code"])
		if item["code"] == 'AE':
			f.write('{lat:'+ str(25.276987) + ', lng:' + str(55.296249) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'PK':
			f.write('{lat:'+ str(32.294445) + ', lng:' + str(72.349724) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'SA':
			f.write('{lat:'+ str(26.195246) + ', lng:' + str(28.034088) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'BE':
			f.write('{lat:'+ str(50.985996) + ', lng:' + str(4.836522) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'PA':
			f.write('{lat:'+ str(8.983333) + ', lng:' + str(-79.516670) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'CY':
			f.write('{lat:'+ str(35.095192) + ', lng:' + str(33.203430) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'TH':
			f.write('{lat:'+ str(13.736717) + ', lng:' + str(100.523186) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'ES':
			f.write('{lat:'+ str(40.419044) + ', lng:' + str(-3.298925) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'TR':
			f.write('{lat:'+ str(41.015137) + ', lng:' + str(28.979530) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'JP':
			f.write('{lat:'+ str(35.685360) + ', lng:' + str(139.753372) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'DZ':
			f.write('{lat:'+ str(36.457741) + ', lng:' + str(7.423325) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'EG':
			f.write('{lat:'+ str(30.047503) + ', lng:' + str(31.233702) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'QA':
			f.write('{lat:'+ str(25.286106) + ', lng:' + str(51.534817) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'GR':
			f.write('{lat:'+ str(38.246639) + ', lng:' + str(21.734573) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'IQ':
			f.write('{lat:'+ str(31.833332) + ', lng:' + str(47.150002) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'KR':
			f.write('{lat:'+ str(37.532600) + ', lng:' + str(127.024612) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'IN':
			f.write('{lat:'+ str(24.780010) + ', lng:' + str(84.981827) +', count: ' + str(abs(item["count"])) + '},')
		elif item["code"] == 'YE':
			f.write('{lat:'+ str(12.800000) + ', lng:' + str(45.033333) +', count: ' + str(abs(item["count"])) + '},')
		else:
			location = get_location(item["code"])
			f.write('{lat:'+ str(location.latitude) + ', lng:' + str(location.longitude) +', count: ' + str(abs(item["count"])) + '},')

	f.write(']')
	f.close()

