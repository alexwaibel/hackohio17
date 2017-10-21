#!/usr/bin/python3

import configparser
import re
import twitter
from watson_developer_cloud import PersonalityInsightsV3

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


def fetchTweets(api):
    statusText = ""
    statusSet = api.GetUserTimeline(exclude_replies=False, include_rts=False)
    while len(statusSet) > 0:
        lastStatusID = statusSet[len(statusSet) - 1].id
        for status in statusSet:
            statusText += ' ' + status.text
        statusSet = api.GetUserTimeline(exclude_replies=False,
                                        include_rts=False,
                                        max_id=lastStatusID - 1)

    return statusText


def get_traits_dic(prof):
    trait_dic = dict()
    for personalities in prof['personality']:
        trait_dic[personalities['name']] = personalities['raw_score']
        for child in personalities['children']:
            trait_dic[child['name']] = child['raw_score']
    return trait_dic


def main():
    twitterEnabled = config['Twitter'].getboolean('enabled')

    if twitterEnabled:
        twitterApi = authenticateTwitter(config)
        tweetText = fetchTweets(twitterApi)
        # Remove all mentions from tweets.
        tweetText = re.sub('(@[A-Za-z0-9]+)',
                           '', tweetText, flags=re.MULTILINE)
        # Remove all URLs from tweets.
        tweetText = re.sub(r'http\S+', '', tweetText, flags=re.MULTILINE)
        print(tweetText)

    personality_insights = PersonalityInsightsV3(
        version='2017-10-13',
        username='136e3f1c-5154-41bb-8a3a-dda7edb1e118',
        password='TZlDSGcxPVVf')

    #Gets personality breakdown from watson as a JSON(?)
    userProf = personality_insights.profile(tweetText,
                                            content_type='text/plain',
                                            content_language=None,
                                            accept='application/json',
                                            accept_language=None,
                                            raw_scores=True,
                                            consumption_preferences=True,
                                            csv_headers=False)
    trait_dictionary = get_traits_dic(userProf)



if __name__ == "__main__":
    main()
