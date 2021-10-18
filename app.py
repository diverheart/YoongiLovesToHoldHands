import tweepy
import sys

auth = tweepy.OAuthHandler("iM2hquu2cHhg2ijajflMwgXfz", "lwxuDabWiT2I9TWbWKjnGB7pIlNUTHbaCjfrCqfUCFC8j6JUSu")
auth.set_access_token("1404195853791727617-n5qfhoYip5tV2KxzSh3ZDW3MWTWBmB", "L5Hhki1YD1ySxQJiOrE494TayxjXFTbkbGmiXKgB9dwl9")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
