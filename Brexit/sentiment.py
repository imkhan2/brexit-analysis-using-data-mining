import csv
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

tweets = []
with open("GetOldTweets-python-master/05_2017.csv", "r", encoding="utf-8") as f:
	data = csv.reader(f)
	for row in data:
		record = row
		val =''
		for item in record:
			val += item
		tweets.append(val.split(";")[4])
print(tweets[1])
tweets = np.array(tweets[1:])
#print(tweets.shape)

pos, neg, neu = 0, 0, 0
for tweet in tweets:
	score = analyser.polarity_scores(tweet)
	if score['pos']>score['neg']:
		pos += 1
	elif score['neg']>score['pos']:
		neg += 1
	else:
		neu += 1

print((pos*100)/(pos+neg))
print(pos, neg)
a = "Before # Brexit hate crime was local news .. afterwards it's national news with army of retweeters"
print(analyser.polarity_scores(a))
print(analyser.polarity_scores('UK businesses in their deepest downward spiral since 2016, signals PMI data https://t.co/XP6AA2DUfz\xe2\x80\xa6 https://t.co/OVdKup33Fn'))
#print(analyser.polarity_scores("RT @Haggis_UK: Margaret Beckett - There's only one way to bring #brexit to an end.. &amp; it's to stay in the European Union.\xf0\x9f\x91\x8d\n\n#LBC"))
