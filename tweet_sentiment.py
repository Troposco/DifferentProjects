#A simple tweets sentiment aggregator#
#Author: TropoSco#
#Date: 27-08-2014#


import sys
import json
import os


os.chdir("Need to be changed")#Changing directory to where the data is stored



#Function that extracts the tweets from the live stream (the language is english by deafult, could be changed)

def tweets(fp,langage = "en"):
    txt = {}
    for i,line in enumerate(fp) :
        if ("text" in json.loads(line).keys()) and (json.loads(line)["lang"].encode('utf-8') == langage):
            txt[i]=json.loads(line)["text"].encode('utf-8')
        else :
            txt[i] = ""
    return txt

twitterStream = open("outputStream.txt")# ouptputStream.txt is where to store the live twitter stream (extracted using the twitter API) 
all_liveStream_tweets = tweets(twitterStream)#The tweets in english
all_liveStream_tweets = [x for x in all_liveStream_tweets.values() if x!='']#removing the empty tweets


#Creating a sentiment dictionnary from the AFINN-111 text file#

afinnfile = open("AFINN-111.txt")

scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)  # Convert the score to an integer
  
  

#Extracting words from the tweets and scoring them using the AFINN-111 base



#The scoring function, the inputs : a tweet (type string) and a dictionnary (type dict) with sentiment scores


def score(tweet, dictionnary):
    res = 0
    for word in tweet.split() :
        if word in dictionnary.keys() :
            res += dictionnary[word]
    return res
    

#Scoring all the tweets

all_scores = []
overallScore = 0

for i,tweet in enumerate(all_liveStream_tweets) :
    score_tweet = score(tweet,scores)
    all_scores.append([i,score_tweet])
    overallScore += score_tweet
    
#Printing 20 positif tweets and the associated scores

j=0
for i,score in all_scores :
    if score > 0 :
        print all_liveStream_tweets[i] , score
        j += 1
    if j>20 :
        break
        
#Printing 20 negatif tweets and the associated scores

j=0
for i,score in all_scores :
    if score < 0 :
        print all_liveStream_tweets[i] , score
        j += 1
    if j>20 :
        break
    















