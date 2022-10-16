import tweepy
import json

CONSUMER_KEY = 'JZ55eKoTQdXyYDj669qiZ0DWG'  
CONSUMER_SECRET = 'BJcFL8O5MP7mUBxV6ERoe8g4J4XZMeprP3zdUWxScrjCdhDnV3'
ACCESS_KEY = '1575625171935072256-OTEpNQ3BZEeuh53MrNuXRxfe9ZykRx' 
ACCESS_SECRET = 'tnJ51o8VyZSEXpegZwzDTc5tWj3GKfBDpK8GIEy1C0Ay2' 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def storedData( type, new_data ):
    if( type ) == "read":
        with open( 'DATA_FILE.json','r+' ) as USERDATA:
            file_data = json.load( USERDATA )
            return file_data
    elif( type ) == "write":
        with open( 'DATA_FILE.json','w' ) as USERDATA:
            USERDATA.write( new_data )

def writeJsonData( last_id ):
    stored_new = {
        "info": [
            {
                "id": last_id 
            },
        ]
    }
    sent_data = json.dumps( stored_new, indent = 4 )
    storedData( "write", sent_data )

def getID():
    id_stored = storedData( "read", None )[ "info" ][ 0 ][ "id" ]
    return id_stored

#get data from tingy
stored_id = getID()

mentions = tweepy.Cursor(api.mentions_timeline, since_id = stored_id).items(15)

for mention in mentions:
    print(str(mention.id) + ' -- ' + mention.text)
    #Writes the most recent id in the json file 
    writeJsonData(int(mention.id))
    if mention.id is not stored_id: 
        if 'summoned' in mention.text.lower():
            print("'#summoned' found --> sending bot reply")
            api.update_status(status = 'You Called?', in_reply_to_status_id = mention.id, auto_populate_reply_metadata=True)