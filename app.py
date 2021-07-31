import tweepy
import sys

auth = tweepy.OAuthHandler("UXcwJfKajYu6azjRjJOzK3rlo", "FR6G9QosK7tqV4lxEMMdNK8nBUc0zlhjo3tBo0qcpDvPJYPXsq")
auth.set_access_token("1404195853791727617-LaE76cY5VQmCU6roYzYkKvIXDbwrdF", "RhSJjDmNs3OJr3Q5oh1ZG8L2Au5grHVx0dpi8BTjvvDoX")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
