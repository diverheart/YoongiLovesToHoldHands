import tweepy
import sys

auth = tweepy.OAuthHandler("n00WocUvtRpLrB8tRJvnNypFV", "JSQnwFVn39sr69WMijdKWaCzmEklUX1Elhw7xYG1eVRUZfjZZD")
auth.set_access_token("1404195853791727617-oHqAQyqVFXVeHKSML7DhFTyIxWY9mI", "U2LH1keSOMXdH9ndr7MsUHedPuXMcYuaalRFJ9g1DhrHX")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
