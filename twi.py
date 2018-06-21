import tweepy
from textblob import TextBlob
AccessToken="722264914585378816-WxwiK4hH5Gkx4tWaPiDYRhUl2DnVyay"
AccessTokenSecret="aWaOySfIlAkv4H7hLWc1lR1Ji4oDXnYN41Sh6Bv4gD2cE"
ConsumerKey="7eajONFL1UtieKpVc6lNo5dSL"
ConsumerSecret="p5zZAibTdbJlqg0Y2V8tya4HiBSi3EaaDkoAsD2Y87UTosIk2c"
auth=tweepy.OAuthHandler(ConsumerKey,ConsumerSecret)#used for login
auth.set_access_token(AccessToken,AccessTokenSecret)#auth has all needfull now,all keys are there in auth
"""now finally login in twitter database"""
api=tweepy.API(auth)
public=api.search("food")#it is now searching api.search means it has said yes u are logined now search the given
c=0
for i in public:
	print(i.text)
	a=TextBlob(i.text)
	c=c+1
	print(a.sentiment)
print(c)
