#!/usr/bin/env python
import sys
import time
import tweepy

def divideString(string, ext=140): # Gets a long string unable to be tweeted and returns a list with some substrings (as needed) with 140 or fewer chars.
	number_of_str = int(len(string)/ext) + 1
	strgroup = []
	shortlen = int(len(string)/number_of_str)
	for i in range(number_of_str):
		strgroup.append(removeLatSpaces(string[shortlen*i : (i + 1)*shortlen]))
	return strgroup

def removeLatSpaces(string): # Gets a string and returns the same string w/o any space character at its sides, if exist.
	while string[0] == " ":
		string = string[1:]
	while string[len(string) - 1] == " ":
		string = string[: len(string) - 1]
	return string

fin = open("file.txt", "r") # Opening the source text.
with open('secret.json') as data_file:  # Opening the secret file (contains tokens)
    secret = json.load(data_file)

# Twitter keys for autentication
apiKey = secret["Twitter"]["apiKey"]
apiSecret = secret["Twitter"]["apiSecret"]
accessToken = secret["Twitter"]["accesToken"]
accessTokenSecret = secret["Twitter"]["accesTokenSecret"]

auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

counter = 0
time_between_tweets = 30 			   # Time in secs between consecutive tweets.
time_between_tweeting = 3600 - 30*10   # Time in secs between tweeting.
lines = fin.readlines()

i = 0
while i < len(lines):
	if len(lines[i]) > 140: 		# Long problematic tweet.
		tweetGroup = divideString(lines[i])
		for x in range(len(tweetGroup)):
			tweetStr = str(x + 1) + ": " + tweetGroup[x]
			print(tweetStr)         # TWEET ACTION: UPDATE STATUS
			api.update_status(status=tweetStr)
			time.sleep(time_between_tweets)
		
	else: 							# Short tweet, no extension problem.
		tweetStr = lines[i]
		while len(tweetStr) + len(lines[i+1]) < 140:
			tweetStr += lines[i+1]
			i += 1
		print(tweetStr)
		api.update_status(status=tweetStr)

	time.sleep(time_between_tweets) # Wait after each tweet or after each tweet group.

	counter += 1
	if counter == 10:
		time.sleep(time_between_tweeting) # If we have tweeted 10 times, stop till next tweeting.
		counter = 0

	i += 1