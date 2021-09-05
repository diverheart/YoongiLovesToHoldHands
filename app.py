import tweepy
import sys

auth = tweepy.OAuthHandler("LIaqZ2Mz6vKRd4bNWyiC4Sfzp", "vLvKFzvTb4iIyU14K5cTbZuvyt4fDI1J0quZviZWCaA2zMhAsn")
auth.set_access_token("1404195853791727617-r4Dpg6CGUTOVzHRxe67Zv7ySmYsXKN", "dz9OfZJzK25ZW7LioIqnFr5kvXILFcBtKCPQ0eeO2m11l")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
