import tweepy
import sys

auth = tweepy.OAuthHandler("dSWD2P25951BAzhCwEiTSKMYn", "GRu4pQpmVzE4TK6Y1gWheEVk1DAy6E3SOhNIf6ARfTajBNkVJD")
auth.set_access_token("1404195853791727617-QUYfHJGCQqjVR02SbmtULsRgh2m7Ui", "Vh0h0bUglWd7XlwkfqK6pUWND3u07S9voW8PDGCNNW0ip")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
