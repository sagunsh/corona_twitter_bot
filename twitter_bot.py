import sys
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import tweepy

import requests
from lxml import html


def create_tweet():
    response = requests.get('https://www.worldometers.info/coronavirus/')
    doc = html.fromstring(response.content)
    total, deaths, recovered = doc.xpath('//div[@class="maincounter-number"]/span/text()')

    tweet = f'''Coronavirus Latest Updates
Total cases: {total}
Recovered: {recovered}
Deaths: {deaths}

Source: https://www.worldometers.info/coronavirus/

#coronavirus #covid19 #coronavirusnews #coronavirusupdates
'''
    return tweet


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print('Authentication Successful')
    except:
        print('Error while authenticating API')
        sys.exit(1)

    tweet = create_tweet()
    api.update_status(tweet)
    print('Tweet successful')
