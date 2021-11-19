import tweepy
import sys

auth = tweepy.OAuthHandler("CHdEUrpOMh6xSrCz95yYOqmqN", "eL0lZB6ZqlsTIUB5TXeazKvaBSbEtFNFpI2vzQlRZXuX6jOmm7")
auth.set_access_token("1404195853791727617-wVLtoxDwNbOdbEjdg5bWWwn2c7j1Mj", "OITRMwh2dtiGxbrTtOa33AOynqt6NYHgVNqUxegMipS82")
api = tweepy.API(auth)


try:
	tweet="Yoongi is holding your hand " +sys.argv[1] 
	api.update_status(status =(tweet))
	print(tweet)
	sleep(3)
	




except Exception as e:
	print("404")
	sleep(15)
