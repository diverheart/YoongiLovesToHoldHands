import tweepy
import sys

auth = tweepy.OAuthHandler("dAiOdK1VwkBP8qQ0f7qtv8Qte", "SPeqp310kE9tG9YhBlS7yDtGoEeCVSNBgRbKZNkoboVeXt8Nox")
auth.set_access_token("1404195853791727617-WD6JwrOk89qN7cLKOxO3b1TiFmDzxd", "Bz5HIOzjeslyu1uCvK3260GVRss0EfSMKWNVbyUccF2UU")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
