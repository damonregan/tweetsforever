import ConfigParser
import tweepy

config = ConfigParser.RawConfigParser()

# You need to change this to point to your oauth.cfg
# containing your oauth credentials
config.read('../oauth.private.cfg')

consumer_key = config.get("consumer", "consumer-key")
consumer_secret = config.get("consumer", "consumer-secret")

access_token = config.get("access", "access-token")
access_token_secret = config.get("access", "access-token-secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

statuses = api.home_timeline()

for status in statuses:
	print status.id
	print status.text
	print status.user.name
	print "\n"