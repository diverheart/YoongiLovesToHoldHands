import tweepy
import sys

auth = tweepy.OAuthHandler("xVoHiHSAwahBmkMlqx452VB7r", "6xZ85GiHmKqYGKpGrZ4ZjDj1PhSgJAmiRpPFlp5BtQgpjgsL7Y")
auth.set_access_token("1404195853791727617-pVK939VQVZSdNWGK2VlXklGVQhJD4Z", "voBgHcPQeyfOkMmSbkQSaHqYxj1oIC4uEQ18bxcQGmt6Y")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
