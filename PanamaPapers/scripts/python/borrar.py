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
archivo_csv = 'datacsv(1).csv'
archivo_json = 'json1.json'
rutaServer = 'http://10.5.40.165:5984/'
ddbbNombre = 'tmp1'




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
#maximoProcesar = 10 #si se desa procesar un límite

with open(archivo_csv) as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
 	for row in reader:
#		if i == maximoProcesar: # si se desa procesar un límite
#			break # si se desa procesar un límite
		dict = {     'IdJuicio': unicode(row['IdJuicio'])
					#,'NombreMateria': (row['NombreMateria']).strip()
					,'NombreAccion': unicode((row['NombreAccion']).strip())
					,'NombreDelito': unicode((row['NombreDelito']).strip())
					,'FechaSistema': unicode((row['FechaSistema']).strip())
					,'Ciudad': unicode((row['Ciudad']).strip())
					,'Direccion': unicode((row['Direccion']).strip())
					,'AliasJudicatura': unicode((row['AliasJudicatura']).strip())
		}
		array.append(dict)
		i = i + 1
		# Lo guarda en couchdb
		db.save(dict)

# jsonfile.write( json.dumps(array) ) # si se desa guardar el fichero en disco
print 'Termina: ' + unicode(datetime.datetime.time(datetime.datetime.now()))
print 'Procesados: ' + unicode(i) + ' registros'