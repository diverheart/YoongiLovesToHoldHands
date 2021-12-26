import tweepy
import sys

auth = tweepy.OAuthHandler("k9cdIm9ZpavDuNMYY0V9dYPCx", "2btkzqiZAQ3SdreBDYNQJjmWzGWsOk6FmkvOPWLKUqvZn49pbp")
auth.set_access_token("1404195853791727617-UDHm5AJ8GgB5KKl376FK7al6fP0EVW", "ynhYEpJORDrfaynNV6PMFg5xMnrUgfnSrwnSp2uxMmY4v")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
