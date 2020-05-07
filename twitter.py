import tweepy
import time
import os

consumer_api_key = os.environ.get('consumer_api_key')
consumer_api_secret = os.environ.get('consumer_api_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

searchArr = ['#javascript', '#typescript', '#python']
nTweets = 5000

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
