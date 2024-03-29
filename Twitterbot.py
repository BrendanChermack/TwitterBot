import tweepy
import json

CONSUMER_KEY = '[REDACTED]'  
CONSUMER_SECRET = '[REDACTED]'
ACCESS_KEY = '[REDACTED]' 
ACCESS_SECRET = '[REDACTED]' 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def storedData( type, new_data ): #holds data in a json
    if( type ) == "read":
        with open( 'DATA_FILE.json','r+' ) as USERDATA:
            file_data = json.load( USERDATA )
            return file_data
    elif( type ) == "write":
        with open( 'DATA_FILE.json','w' ) as USERDATA:
            USERDATA.write( new_data )

def writeJsonData( last_id ): #writes data to a json
    stored_new = {
        "info": [
            {
                "id": last_id 
            },
        ]
    }
    sent_data = json.dumps( stored_new, indent = 4 )
    storedData( "write", sent_data )

def getID(): #gets the last id from the json
    id_stored = storedData( "read", None )[ "info" ][ 0 ][ "id" ]
    return id_stored

stored_id = getID() #get data from json

mentions = tweepy.Cursor(api.mentions_timeline, since_id = stored_id).items(15)

for mention in mentions:
    print(str(mention.id) + ' -- ' + mention.text)
    writeJsonData(int(mention.id)) #writes the most recent id in the json file 
    if mention.id > stored_id: #tells if the id has pervoiusly been stored
        if 'summoned' in mention.text.lower(): #determins if the bot needs to reply
            print("'#summoned' found --> sending bot reply") #prints to the console when the condition is met
            api.update_status(status = 'You Called?', in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True) #tweets the tweet
