import tweepy
import csv
import pandas as pd
'''
####input your credentials here
consumer_key = '3Tqtir2fadU96wLBGCO4BxwAH'
consumer_secret = 'B7fIHRVriceO0nUxlP4ZSnTI3WMWeOzy3RmGjm4vvsSJOAweSo'
access_token = '1198683849875709953-2fzVJZrz5363dKR90ugEcupuzkeRqo'
access_token_secret = 'Ecrxo87Rnpmx3wb5QyCA7xaSh3uKOJ2SsRttc8sL5xhGT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('stop_brexit.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#stopbrexit",count=100,
                           lang="en",
                           since="2019-10-03").items():
    #print (tweet.created_at, tweet.text)
    #print(tweet[0])
    #break
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])'''

import got3

tweetCriteria = got3.manager.TweetCriteria().setQuerySearch('#brexit').setSince("2016-07-01").setUntil("2016-08-30").setMaxTweets(100)
tweet = got3.manager.TweetManager.getTweets(tweetCriteria)

for element in tweet:	  
	print(element.geo)