from textblob import TextBlob
from twitter_scraper import get_tweets


username = input('Username: ')

for tweet in get_tweets(username, pages=1):
    blob = TextBlob(tweet['text'])
    print(blob.sentiment)

