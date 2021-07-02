import tweepy
import sys

auth = tweepy.OAuthHandler("6odotTB8lJ947JTbPDQJeT9sU", "vrjFYbLNBy4lPK06Q1LI1OcwBaIN27Cy7t2udctTDLBWSAqw0U")
auth.set_access_token("1404195853791727617-pZEwUcsp6kTENeiJwr8uln8Iqazqnh", "fSYC5HfDA8LZG7dX9NvIpL9ksIBWAoNPVCGl9FklwsRC6")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
