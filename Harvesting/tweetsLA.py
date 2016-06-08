#!python2.7.9
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "kWIkdGZSmthAByKQqGyELooPg"
csecret = "0GjwrD8N5TcKYZTzgGbm5v5nre0xuQzzneDrqt2N35TjEYZEos"
atoken = "73224154-g8h0FSO10iOxZgxVJX4Fwg0gpv8917QgXcp3uXorj"
asecret = "uAnl5SZBdrQVnBup4GsBy3evW2Q1qqDOb2slpqRZ8c0xj"
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
    db = server.create('panamapapersdbla')
except:
    db = server['panamapapersdbla']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['#panamapapers'])
twitterStream.filter(track=['#panamaleaks'])
twitterStream.filter(track=['panama papers'])
twitterStream.filter(track=['#papelesdepanama'])
twitterStream.filter(track=['papeles de panama'])
twitterStream.filter(locations=[-95.1,-55.7,-34.1,23.1])
