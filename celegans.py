import time
import numpy as np
import tweepy

WORM = (
    u'\u2003',
    '~',
    )

def get_zoo():
    rows = 7
    columns = 18
    sparseness = 0.2

    locations = np.random.rand(rows,columns)<sparseness

    tweet_text = u''
    for row in locations:
        for loc in row:
            tweet_text += WORM[loc]
        tweet_text += '\n'
    return tweet_text

try:
    from SECRETS import *
except ImportError:
    import os
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_KEY = os.environ['ACCESS_KEY']
    ACCESS_SECRET = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    tweet_text = get_zoo()
    api.update_status(tweet_text)
    time.sleep(3*60*60)
