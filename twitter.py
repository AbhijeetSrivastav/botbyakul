#Import the required modules
import tweepy
import time
import os

#Setting the API Keys and tokens
consumer_api_key = os.environ.get('consumer_api_key')
consumer_api_secret = os.environ.get('consumer_api_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

#Creating instance of tweepy authentication handler
auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret)
auth.set_access_token(access_token, access_token_secret)


#Creating instance of tweepy API handler
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Setting the user API
user = api.me()

#List of the terms to query and number of tweets to watch for
searchArr = ['#javascript', '#typescript', '#python']
nTweets = 5000

#Searching for the querries on twitter
for search in searchArr:
    for tweet in tweepy.Cursor(api.search, search).items(nTweets):
        try:
            print(tweet)
            tweet.favorite()
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
