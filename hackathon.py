#!/usr/bin/python3

import configparser
import praw
import re
import twitter
from watson_developer_cloud import PersonalityInsightsV3

config = configparser.ConfigParser()
config.read('config.cfg')


# Takes configparser as argument and connects Twitter API to account

def authenticate_twitter(config_file):
    consumer_key = str(config_file['Twitter']['consumer key'])
    consumer_secret = str(config_file['Twitter']['consumer secret'])
    access_token = str(config_file['Twitter']['access token'])
    access_token_secret_user = str(config_file['Twitter']['access token secret'])

    twitter_api = twitter.Api(consumer_key=consumer_key,
                              consumer_secret=consumer_secret,
                              access_token_key=access_token,
                              access_token_secret=access_token_secret_user)
    return twitter_api


# Takes Twitter API as argument and fetches all tweets by user.

def fetch_tweets(api):
    status_text = ""
    status_set = api.GetUserTimeline(exclude_replies=False, include_rts=False)
    while len(status_set) > 0:
        last_status_id = status_set[len(status_set) - 1].id
        for status in status_set:
            status_text += " " + status.text
        status_set = api.GetUserTimeline(exclude_replies=False,
                                         include_rts=False,
                                         max_id=last_status_id - 1)

    return status_text


def get_traits_dic(prof):
    trait_dic = dict()
    for personalities in prof['personality']:
        trait_dic[personalities['name']] = personalities['raw_score']
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


def fetch_reddit_comments(api, user_config):
    reddit_comment_text = ""
    redditor = api.redditor(str(user_config['Reddit']['username']))
    for comment in redditor.comments.new(limit=None):
        reddit_comment_text += " " + comment.body

    return reddit_comment_text


# Takes configparser as argument and connects Reddit API to account.

def authenticate_reddit(user_config):
    client_id = str(user_config['Reddit']['client id'])
    client_secret = str(user_config['Reddit']['client secret'])
    password = str(user_config['Reddit']['password'])
    username = str(user_config['Reddit']['username'])
    reddit_api = praw.Reddit(client_id=client_id,
                             client_secret=client_secret,
                             password=password,
                             user_agent='script by /u/alexwaibel',
                             username=username)
    return reddit_api


def main():

    combined_text = ''
    twitter_enabled = config['Twitter'].getboolean('enabled')
    reddit_enabled = config['Reddit'].getboolean('enabled')

    if twitter_enabled:
        twitter_api = authenticate_twitter(config)
        tweet_text = fetch_tweets(twitter_api)
        # Remove all mentions from tweets.
        tweet_text = re.sub('(@[A-Za-z0-9]+)',
                            '', tweet_text, flags=re.MULTILINE)
        # Remove all URLs from tweets.
        tweet_text = re.sub(r'http\S+', '', tweet_text, flags=re.MULTILINE)
        combined_text += tweet_text

    if reddit_enabled:
        reddit_api = authenticate_reddit(config)
        reddit_comment_text = fetch_reddit_comments(reddit_api, config)

        # Remove URLs from reddit comments.
        reddit_comment_text = re.sub(r'http\S+', '', reddit_comment_text,
                                     flags=re.MULTILINE)
        combined_text += reddit_comment_text

    personality_insights = PersonalityInsightsV3(
        version='2017-10-13',
        username='136e3f1c-5154-41bb-8a3a-dda7edb1e118',
        password='TZlDSGcxPVVf')

    # Gets personality breakdown from watson as a JSON(?)
    user_prof = personality_insights.profile(combined_text,
                                             content_type='text/plain',
                                             content_language=None,
                                             accept='application/json',
                                             accept_language=None,
                                             raw_scores=True,
                                             consumption_preferences=True,
                                             csv_headers=False)
    trait_dictionary = get_traits_dic(user_prof)
    consum_dictionary = get_consumption_traits(user_prof)

    print(trait_dictionary)
    print(consum_dictionary)

    # Rank genres with a score of 0 to 1 inclusive
    ope = trait_dictionary["Openness"]
    con = trait_dictionary["Conscientiousness"]
    ext = trait_dictionary["Extraversion"]
    agr = trait_dictionary["Agreeableness"]
    neu = trait_dictionary["Emotional range"]
    print(ope)
    print(con)
    print(ext)
    print(agr)
    print(neu)

    # action_score = ((1-ope)+ext+consum_dictionary["action"])


if __name__ == "__main__":
    main()
