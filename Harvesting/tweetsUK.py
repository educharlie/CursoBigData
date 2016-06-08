
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "TZ6zI9Nl6m6PM3vqpsnE9v7f2"
csecret = "zWbZJ6tjMEHzDQZ8fPuqNV2TfbCnuEjYVogizQU7XUIQZXGspx"
atoken = "731099192060477440-3bleGto6UUXJdeED3TuWLER09pRH8Qd"
asecret = "6JNuW3UqlGdnGMW7jPbNUQqnM47wsXpRpd3V0h6x64HdP"
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
    db = server.create('panamapapersdbuk')
except:
    db = server['panamapapersdbuk']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['#panamapapers'])
twitterStream.filter(track=['#panamaleaks'])
twitterStream.filter(track=['panama papers'])
twitterStream.filter(track=['#papelesdepanama'])
twitterStream.filter(track=['papeles de panama'])
twitterStream.filter(locations=[-11.43,49.98,2.2,58.97]) 

