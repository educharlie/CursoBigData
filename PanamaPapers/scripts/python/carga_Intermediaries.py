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
archivo_csv = 'Intermediaries.csv'
archivo_json = 'json1.json'
rutaServer = 'http://localhost:5984/'
ddbbNombre = 'pp_intermediaries'

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
				, "address": unicode(row["address"])
			    , "valid_until": unicode(row["valid_until"])
				, "country_codes": unicode(row["country_codes"])
				, "countries": unicode(row["countries"])
				, "status": unicode(row["status"])
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