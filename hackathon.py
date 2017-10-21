#!/usr/bin/python3

import configparser
import praw
import re
import twitter
import watson_developer_cloud
from watson_developer_cloud import PersonalityInsightsV3

config = configparser.ConfigParser()
config.read('config.cfg')

# Takes configparser as argument and connects Twitter API to account

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

# Takes Twitter API as argument and fetches all tweets by user.

def fetchTweets(api):
    statusText = ""
    statusSet = api.GetUserTimeline(exclude_replies=False, include_rts=False)
    while len(statusSet) > 0:
        lastStatusID = statusSet[len(statusSet) - 1].id
        for status in statusSet:
            statusText += " " + status.text
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


def get_consumption_traits(prof):
    consum_traits = dict()
    movie_preferences = prof['consumption_preferences'][4]['consumption_preferences']
    for category in movie_preferences:
        consum_traits[category['consumption_preference_id'][30:]] = category['score']
    return consum_traits


'''
Takes Reddit API and configparser as arguments and fetches all reddit comments
made by the user.
'''

def fetchRedditComments(api, config):
    redditCommentText = ""
    redditor = api.redditor(str(config['Reddit']['username']))
    for comment in redditor.comments.new(limit=None):
        redditCommentText += " " + comment.body

    return redditCommentText

# Takes configparser as argument and connects Reddit API to account.

def authenticateReddit(config):
    clientId = str(config['Reddit']['client id'])
    clientSecret = str(config['Reddit']['client secret'])
    password = str(config['Reddit']['password'])
    username = str(config['Reddit']['username'])
    redditApi = praw.Reddit(client_id=clientId,
                            client_secret=clientSecret,
                            password=password,
                            user_agent='script by /u/alexwaibel',
                            username=username)
    return redditApi

def main():
    twitterEnabled = config['Twitter'].getboolean('enabled')
    redditEnabled = config['Reddit'].getboolean('enabled')

    if twitterEnabled:
        twitterApi = authenticateTwitter(config)
        tweetText = fetchTweets(twitterApi)
        # Remove all mentions from tweets.
        tweetText = re.sub('(@[A-Za-z0-9]+)',
                           '', tweetText, flags=re.MULTILINE)
        # Remove all URLs from tweets.
        tweetText = re.sub(r'http\S+', '', tweetText, flags=re.MULTILINE)

    if redditEnabled:
        redditApi = authenticateReddit(config)
        redditCommentText = fetchRedditComments(redditApi, config)

        # Remove URLs from reddit comments.
        redditCommentText = re.sub(r'http\S+', '', tweetText,
                                   flags=re.MULTILINE)

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
    consum_dict = get_consumption_traits(userProf)



if __name__ == "__main__":
    main()
