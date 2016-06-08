""" 
Panama papers
BigData, curso.
Pobla ficheros en pp_entities, couch_db desde Entities.csv
06-06-2016: Emisión inicial.
Grupo 1.
"""

# encoding=utf8  
import sys
import csv
import json
import datetime
import couchdb


# Lectura caracteres "especiales" del csv
reload(sys)  
sys.setdefaultencoding('utf8')

# Parametrización
archivo_csv = 'Entities.csv'
archivo_json = 'json1.json'
rutaServer = 'http://localhost:5984/'
ddbbNombre = 'pp_entities'

# Conexión con couchdb
server = couchdb.client.Server(rutaServer)
server.resource.credentials = ('admin', 'admin')
# Se recomienda chequear la existencia de la bbdd, para no borrarla por gusto
del server[ddbbNombre]
db = server.create(ddbbNombre)

# en caso de desear escribir el fichero en disco
# jsonfile = open(archivo_json, 'w')

dict = {}
array = [] # para escribir el fichero en disco

print 'Inicia: ' + unicode(datetime.datetime.time(datetime.datetime.now()))

i = 0
#maximoProcesar = 10000 #si se desa procesar un límite

with open(archivo_csv) as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
#		if i == maximoProcesar: # si se desa procesar un límite
#			break # si se desa procesar un límite
		dict = {  'name': unicode(row['name'])
				, 'internal_id': unicode(row['internal_id'])
				, "inactivation_date": unicode(row["inactivation_date"])
			    , "status": unicode(row["status"])
				, "service_provider": unicode(row["service_provider"])
				, "country_codes": unicode(row["country_codes"])
				, "countries": unicode(row["countries"])
				, "node_id": unicode(row["node_id"])
				, "sourceID": unicode(row["sourceID"])
		}
		array.append(dict)
		i = i + 1
		# Lo guarda en couchdb
		db.save(dict)

# jsonfile.write( json.dumps(array) ) # si se desa guardar el fichero en disco
print 'Termina: ' + unicode(datetime.datetime.time(datetime.datetime.now()))
print 'Procesados: ' + unicode(i) + ' registros'