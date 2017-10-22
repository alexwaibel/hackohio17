#!/usr/bin/python3

import configparser
import praw
import re
import twitter
import watson_developer_cloud
from watson_developer_cloud import PersonalityInsightsV3
import requests
import urllib
import Movie

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
    consum_dictionary = get_consumption_traits(userProf)

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

    action_score = ((1-ope)+ext+consum_dictionary["action"]) / 3
    adventure_score = (con+agr+consum_dictionary["adventure"]) / 3
    animation_score = ((1-con)+(1-ext)+(1-agr)+neu) / 4
    comedy_score = ((1-ope)+ext+agr) / 3
    crime_score = (ope+(1-ext)+(1-agr)) / 3
    documentary_score = (ope+consum_dictionary["documentary"]) / 2
    drama_score = (ext+agr+consum_dictionary["drama"]) / 3
    science_fiction_score = (con+(1-ext)+consum_dictionary["science_fiction"])/3
    fantasy_score = science_fiction_score
    war_score = ((1-ope)+(1-neu)+consum_dictionary["war"])/3
    history_score = ((1-ope)+(1-neu) + consum_dictionary["historical"]) / 3
    romance_score = ((1-ope)+ext+agr+consum_dictionary["romance"])/4
    music_score = (neu+consum_dictionary["musical"])/2
    mystery_score = crime_score
    thriller_score = (action_score + drama_score) / 2
    horror_score = ((1-ext) + (1-agr) + neu + consum_dictionary["horror"]) / 4

    scores = sorted([["action", action_score, 28], ["adventure", adventure_score, 12], ["animation", animation_score, 16],
                     ["comedy", comedy_score, 35], ["crime", crime_score, 80], ["documentary", documentary_score, 99],
                     ["drama", drama_score, 18], ["science-fiction", science_fiction_score, 878], ["fantasy", fantasy_score, 14],
                     ["war", war_score, 10752], ["history", history_score, 36], ["romance", romance_score, 10749], ["music", music_score, 10402],
                     ["mystery", mystery_score, 9648], ["thriller", thriller_score, 53], ["horror", horror_score, 27]],
                    key=lambda x: x[1], reverse=True)
    print(scores)

    movie_db_apikey = "e7552b83b0a1458bf2caadfe42e02de5"
    movie_db_api = "https://api.themoviedb.org"
    movies = list()


    for i in range(1,11):
        url = movie_db_api + "/3/discover/movie?api_key="+movie_db_apikey+"&language=en-US&sort_by=popularity.desc&include_adult=true&include_video=true&page="+str(i)+"&with_genres="+str(scores[0][2])+"|"+str(scores[1][2])+"|"+str(scores[2][2])+"|"+str(scores[3][2])+"&with_original_language=en"
        response = requests.get(url)
        json_data = response.json()
        for i in range(0, 20):
            mymovie = Movie(json_data['results']['title'], json_data['results']['genre_ids'], scores)
            movies.append([("title",json_data['results']['title']), ('genre_ids', json_data['results']['genre_ids'])])

    print(movies)









if __name__ == "__main__":
    main()
