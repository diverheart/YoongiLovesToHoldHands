import tweepy
import sys

auth = tweepy.OAuthHandler("8AYZNYH1JniwxSVdzNgViC4Iz", "EEMO2QjUbYYD5kkBSwdTVyfVaAsMebsBSh5egNeO1xg10RJxuj")
auth.set_access_token("1404195853791727617-U4JMtnx7GYolDtxmvgHpBwnieR4HUt", "DiB9FbFRnHStR0tdhvdf5VyadPWIuyDADZauIW7CJv2ID")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
