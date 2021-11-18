import tweepy
import sys

auth = tweepy.OAuthHandler("867kNEAIS2WlgwD6b1DVE9OYf", "47Frr58owAi80LJYBl4qYfZN1nMyhleKYZ4QeFGycMqhYfTgJF")
auth.set_access_token("1404195853791727617-i4sjOi2YEw32LOsf47eiHwtpwqBS6f", "CaWYKkkmDDRyeT9omns46GmSzCACYNHzwA0WXPUW2SiPI")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
