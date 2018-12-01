from textblob import TextBlob
from twitter_scraper import get_tweets


def analyze(username):
    for tweet in get_tweets(username, pages=1):
        blob = TextBlob(tweet['text'])

        print(blob.sentiment)


def main():
    username = input('Username: ')
    analyze(username)


if __name__ == '__main__':
    main()

