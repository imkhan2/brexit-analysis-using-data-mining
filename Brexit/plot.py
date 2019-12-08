import csv
import numpy as np
import matplotlib.pyplot as plt

keywords_for = ["Conservative/Tory", "Leave", "May", "Johnson", "Trump"]
keywords_against = ["May", "Johnson", "Farage", "Corbyn", "Trump"]
media = ["BBC", "Guardian", "Telegraph", "Sun"]
count_for = [0]*6
count_against = [0]*5
media_count = [0]*4
with open("GetOldTweets-python-master/07_2016.csv", "r", encoding="utf-8") as f:
	data = csv.reader(f)
	for row in data:
		record = row
		val =''
		for item in record:
			val += item
		tweets = val.split(";")[4]
		for i in range(len(keywords_against)):
			if '/' in keywords_against[i]:
				if "Conservative".lower() in tweets.lower() or "tory" in tweets.lower() or "tories" in tweets.lower():
					count_against[i] += 1
			if keywords_against[i].lower() in tweets.lower():
				count_against[i] += 1
			if "trump" in tweets.lower(): #and ("tory" in tweets.lower() or "tories" in tweets.lower()):
				count_for[5] += 1
		for i in range(len(media)):
			if media[i].lower() in tweets.lower():
				media_count[i] += 1

fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
#print(count_for)
plt.title("Politician mentions, July 2016")
plt.bar([0, 1, 2, 3, 4], count_against, color="red")
plt.xticks([0, 1, 2, 3, 4], keywords_against)
plt.show()