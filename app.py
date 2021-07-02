import tweepy
import sys

auth = tweepy.OAuthHandler("LuCZmMxdQxO8eKMAOPSfrjTJc", "O7jytpxR2yrE2kPtP13lzojX4puw4wgMlQLBJFaTK7rIW1x0kA")
auth.set_access_token("1404195853791727617-H5yscWllzJ9Re3P39MxRYNW1882Gqk", "mwIxOyGPhImG2qaPkWeVK03KOFgy9zLKd8ZWiUztSFkYO")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " + sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(5)



except Exception as e:
	print(e)
	sleep(5)
