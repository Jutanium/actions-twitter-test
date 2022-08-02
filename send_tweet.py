import tweepy
import sys

client = tweepy.Client(consumer_secret=sys.argv[1], consumer_key=sys.argv[2], access_token_key=sys.argv[3], access_token_secret=sys.argv[4])
tweet = "I wrote this, and I'm not human!"
url = sys.arv[5]
response = client.create_tweet(text=tweet + " " + url)
print(response)