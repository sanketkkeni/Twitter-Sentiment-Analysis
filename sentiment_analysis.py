import os
import pickle
li = pickle.load( open( "Trump.txt", "rb"))
li = list(li)
from textblob import TextBlob
polarity_list = []

for i in li:
    tb = TextBlob(i)
    polarity_list.append(tb.sentiment.polarity)
    
final_polarities = []

#Isolating polarities from -0.1 to 0.1 and assigning them as neutral
for i in polarity_list:
    if i<-0.1 or i>0.1:
        final_polarities.append(i)
        
no_sentiment = len(polarity_list) - len(final_polarities)

pos_count = 0
neg_count = 0
for i in final_polarities:
    if i<0:
        neg_count = neg_count + 1
    else:
        pos_count = pos_count + 1

print("Positive Sentiment is ", pos_count*100/(pos_count+neg_count+no_sentiment))
print("Negative Sentiment is ", neg_count*100/(pos_count+neg_count+no_sentiment))
print("Neither positivenor negative ", no_sentiment*100/(pos_count+neg_count+no_sentiment))
