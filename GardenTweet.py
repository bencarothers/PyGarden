#******************************************#
#       Twitter-Enabled Garden Watering    #
#          Author: Ben Carothers           #
#******************************************#


import twitter
import time
import SprinklerGPIO

#Connect to the Garden's Twitter account
def waterWatcher():
    api = twitter.Api(consumer_key='Z6tyBKfbWTIkbXX1XeOTU3qGF',
                  consumer_secret='MwVDyHYq4Ria4ub3pAmq7D38dgAEtCJKCVgKOMkBimaJpRkZwp',
                  access_token_key='3119886269-GQfctpmBOpY3wodDxO69SoRdDkCRBYNVjiFOcO0',
                  access_token_secret='6wBXAhL2WjYMZw97patQZUSbJ2GjNjbkRftflrwldpGrn')

    status = api.GetUserTimeline('X')

    while len(status) > 0:
        lastId = status[0].id
        tweets = [s.text for s in status]
        lastTweet = tweets[0].split()
        if lastTweet[0] == '#waterMe':
            SprinklerGPIO.setStationStatus(1,1)
            time.sleep(60)
            SprinklerGPIO.setStationStatus(1,1)
            api.DestroyStatus(lastId)
        elif lastTweet[0] != '#waterMe':
            print 'delete'
            api.DestroyStatus(lastId)
    else:
        print 'no tweets'

while 1:
	waterWatcher()
	time.sleep(15) #Avoid twitter rate limiting
