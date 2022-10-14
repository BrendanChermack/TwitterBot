import tweepy
 
CONSUMER_KEY = 'JZ55eKoTQdXyYDj669qiZ0DWG'  
CONSUMER_SECRET = 'BJcFL8O5MP7mUBxV6ERoe8g4J4XZMeprP3zdUWxScrjCdhDnV3'
ACCESS_KEY = '1575625171935072256-OTEpNQ3BZEeuh53MrNuXRxfe9ZykRx' 
ACCESS_SECRET = 'tnJ51o8VyZSEXpegZwzDTc5tWj3GKfBDpK8GIEy1C0Ay2' 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
        
FILE_NAME = 'last_ID.txt'

def retrieve_last_ID(file_name):
    f_read = open(file_name, 'r')
    since_id = int(f_read.read().strip())
    f_read.close()
    return since_id

#def store_last_ID(since_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(since_id))
    f_write.close()
    return
 
since_id = retrieve_last_ID(FILE_NAME)

mentions = api.mentions_timeline(since_id)

for mention in reversed(mentions):
    #if last_ID != mention.id:
        print(str(mention.id) + '  --  ' + mention.text)
        if '#helloworld'in mention.text.lower():
            print("'Hello World' found! -> nxt step")
      
