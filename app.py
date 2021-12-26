import tweepy
import sys

auth = tweepy.OAuthHandler("gwqXIH4fqmYMv9aZLwk2cXVlI", "W5SE4xoUSG0qw2HUa4XfL7vKjXyAHFrI2P7CqLdcVLm68GWXl9")
auth.set_access_token("1404195853791727617-xo6abiRTbmIboJl4Xvq36XHpK7WvdH", "Mt3RE9sFEUoysCPtGc3gN0zenSmLxW3ZS0soKk6YYrRX0")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
