
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "LoaByBctxbj2WVI5ytQAb30qf"
csecret = "lBJILvlPG6GUm0QmXFo709PRfnyHuFuljDJhaLNpHmUkHjv1G5"
atoken = "100512518-5i4gygjJRlCOOqxWnNGHNyvyr6TwCrJFPBYPTuob"
asecret = "vKoizxeA3MDeiR9vfdAGCnAcwiYtW6oCQ6a5iXiyLmpjH"
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
    db = server.create('panamapapersdbus')
except:
    db = server['panamapapersdbus']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(track=['#panamapapers'])
twitterStream.filter(track=['#panamaleaks'])
twitterStream.filter(track=['panama papers'])
twitterStream.filter(track=['#papelesdepanama'])
twitterStream.filter(track=['papeles de panama'])
twitterStream.filter(locations=[-124.1,29.3,-65.7,49.8]) #USA panamapapersdbus

