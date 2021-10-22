import tweepy
import sys

auth = tweepy.OAuthHandler("wMGyScjbA7JACSEYSAAkfvUE6", "dm5jK9W1Njt3uEI3oRAwsZQdzECTuCZatT7cJUqkCplLhbgfXu")
auth.set_access_token("1404195853791727617-a0y9Ryd6gIKH3D5x6LB7MLxJxyutii", "XKHdTcCTqMHhazW5BXmxlos5zAW3iz7hGPL5oL7ONR42r")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
