import pickle
import os
import time
if not os.path.exists('secret_twitter_credentials.pkl'):
    Twitter={}
    Twitter['Consumer Key'] = """Insert Consumer Key here"""
    Twitter['Consumer Secret'] = """Insert Consumer Secret here"""
    Twitter['Access Token'] = """Insert Access Token here"""
    Twitter['Access Token Secret'] = """Insert Access Token Secret here"""
    with open('secret_twitter_credentials.pkl','wb') as f:
        pickle.dump(Twitter,f)
else:
    Twitter = pickle.load(open('secret_twitter_credentials.pkl','rb'))

import twitter

#Creating a handshake
auth = twitter.oauth.OAuth(Twitter['Access Token'],
                          Twitter['Access Token Secret'],
                          Twitter['Consumer Key'],
                          Twitter['Consumer Secret'])

twitter_api = twitter.Twitter(auth = auth)

#Search term
q = '#Trump' 

number = 100
total_tweets = 3000
filename = "Trump.txt"


search_results = twitter_api.search.tweets(q=q, count=number)
statuses = search_results['statuses']
tweets =[]

for s in search_results['statuses']:
      tweets.append(s['text'])
tweets = set(tweets)
file = open(filename,'wb')
pickle.dump(tweets,file)
print(tweets)
print("Length is: ", len(tweets))  
      
for i in range(50):  
        time.sleep(5*60)
        search_results = twitter_api.search.tweets(q=q, count=number)
        statuses = search_results['statuses']
        tweets =[]
		
        for s in search_results['statuses']:
            tweets.append(s['text'])
			
        tweets = set(tweets) #to remove retweets
        file = open(filename,'rb')        
        tweets_in_file = set(pickle.load(file))
        
        tweets_in_file.update(tweets)
        
        tweets_to_put_in_file = tweets_in_file
        
        file = open(filename,'wb')
        pickle.dump(tweets_to_put_in_file,file) #instead of writing in file at every iteration, we can have 
		#a global list to which we can add the latest tweets searched and dump the entire list to pickle file
		#in the end
        print("Length is: ", len(tweets_to_put_in_file))
        if(len(tweets_to_put_in_file)>total_tweets):
            break
			