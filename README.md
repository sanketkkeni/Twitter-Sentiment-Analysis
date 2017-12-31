# Twitter-Sentiment-Analysis
Objective -> After collecting tweets, perform sentiment analysis in python to determine if the sentiment of the tweets are positive, negative or neutral



#Twitter_tweets_generation.py

-Initially after creating a handshake between our local machine and twitter, we search twitter for any keywords
-Search function returns a maximum of 100 latest tweets
-About 3000 such tweets are obtained and stored in a pickle file after searching for 100 tweets every 5 minutes



#sentiment_analysis.py

-Using the tweets from the above file, sentiment analysis is performed using the textblob library in python
-Based on the polarity of the tweets, the positive, negative or neutral sentiment percentage is shown
