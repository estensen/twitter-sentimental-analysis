from twitter_scraper import get_tweets


username = input('Username: ')

for tweet in get_tweets(username, pages=1):
    print(tweet['text'])

