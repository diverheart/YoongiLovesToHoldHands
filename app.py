import tweepy
import sys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(consumer_key, consumer_secret)
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
