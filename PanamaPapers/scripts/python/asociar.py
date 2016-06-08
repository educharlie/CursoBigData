# encoding=utf8  
import sys
import csv
import json
import datetime
import couchdb
import pandas


# Lectura caracteres "especiales" del csv
reload(sys)  
sys.setdefaultencoding('utf8')

# Parametrización
archivo_json = 'dddddd.txt'
rutaServer = 'http://localhost:5984/'
ddbbNombre = 'pp_entities'




# Conexión con couchdb

"""server = couchdb.client.Server(rutaServer)
server.resource.credentials = ('admin', 'admin')

db = server[ddbbNombre]"""

print 'Inicia: ' + unicode(datetime.datetime.time(datetime.datetime.now()))

i = 0
#maximoProcesar = 10 #si se desa procesar un límite

txt = open(archivo_json)
#reader = pandas.read_json(txt, typ='series')

reader = json.loads(txt.read())
print reader[0]

exit() 



# jsonfile.write( json.dumps(array) ) # si se desa guardar el fichero en disco
print 'Termina: ' + unicode(datetime.datetime.time(datetime.datetime.now()))
print 'Procesados: ' + unicode(i) + ' registros'