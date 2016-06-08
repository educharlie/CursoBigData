
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "DBkqGTwIt1TWCZEO9qEDdRYwk"
csecret = "V8reWyGI2qLx4ljkLqTcoH7U0lq8O0hKSXkmSJvuQppuVmyVda"
atoken = "731096413380214784-gt4Rz0S3mB0UAY9HfEVYWew8U6lceoe"
asecret = "77VQls4rWl9xXdgs1l9BdwgvaPDp8ls7D259vh5akIeCT"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('panamapapersdbue')
except:
    db = server['panamapapersdbue']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['#panamapapers'])
twitterStream.filter(track=['#panamaleaks'])
twitterStream.filter(track=['panama papers'])
twitterStream.filter(track=['#papelesdepanama'])
twitterStream.filter(track=['papeles de panama'])
twitterStream.filter(locations=[-10.9,36.1,15.5,50.9])

