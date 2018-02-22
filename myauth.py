# -*- coding:utf-8 -*-
import tweepy

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
