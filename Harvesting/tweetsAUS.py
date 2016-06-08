
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "nbW4bLHUBsAploByWfFyrITvw"
csecret = "fbQtJu5mmkJwJN17t4FS639BskGM2WNNF85YXjakVgvySfsiG4"
atoken = "69916018-AOsKH8HkgWugWxtKm6dFbLEQkLGOqkLJ40oqI8iCy"
asecret = "mFVyoYQs2rCgd8tGyLpOv6Fk4WQgMxM3UpLh27T20FKmP"
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
    db = server.create('panamapapersdbaus')
except:
    db = server['panamapapersdbaus']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['#panamapapers'])
twitterStream.filter(track=['#panamaleaks'])
twitterStream.filter(track=['panama papers'])
twitterStream.filter(track=['#papelesdepanama'])
twitterStream.filter(track=['papeles de panama'])
twitterStream.filter(locations=[112.7,-38.6,154.2,-10.7])

