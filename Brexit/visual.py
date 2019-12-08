import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import *
import csv
import pyfpgrowth
from apyori import apriori
stemmer = SnowballStemmer("english")

def to_words(data):
	letters_only = re.sub("[^a-zA-Z]", " ", data) 
	word = letters_only.lower().split()
	stop = set(stopwords.words("english"))
	web = ['http', 'www', 'ly', 'uk', 'brexit', 'com', 'news', 'vote', 'twitter', 'https']                 
	word = [w for w in word if w not in stop and w not in web]
	#print(word)
	word = [stemmer.stem(w) for w in word]
	return word

tweets = []
with open("GetOldTweets-python-master/07_2016.csv", "r", encoding="utf-8") as f:
	data = csv.reader(f)
	for row in data:
		record = row
		val =''
		for item in record:
			val += item
		tweets.append(val.split(";")[4])
print(tweets[1])
tweets = tweets[1:50001]
words = []

for tweet in tweets:
	words.append(to_words(tweet))

patterns = pyfpgrowth.find_frequent_patterns(words, 2000)
for key in patterns.keys():
	if len(key) >= 2:
		print(key, patterns[key])