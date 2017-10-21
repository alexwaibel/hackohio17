#!/usr/bin/python3

import configparser
import twitter

config = configparser.ConfigParser()
config.read('config.cfg')

# Takes configparser as argument and connects API to account

def authenticateTwitter(config):
    consumerKey = str(config['Twitter']['consumer key'])
    consumerSecret = str(config['Twitter']['consumer secret'])
    accessToken = str(config['Twitter']['access token'])
    accessTokenSecret = str(config['Twitter']['access token secret'])

    twitterApi = twitter.Api(consumer_key=consumerKey,
                             consumer_secret=consumerSecret,
                             access_token_key=accessToken,
                             access_token_secret=accessTokenSecret)
    return twitterApi

def main():
    twitterEnabled = config['Twitter'].getboolean('enabled')

    if twitterEnabled:
        twitterApi = authenticateTwitter(config)

if __name__ == "__main__":
    main()