#******************************************#
#       Twitter-Enabled Garden Watering    #
#          Author: Ben Carothers           #
#******************************************#


import twitter
import time
import re
import SprinklerGPIO

# Connect to the Garden's Twitter account
def waterWatcher():
    api = twitter.Api(consumer_key='Z6tyBKfbWTIkbXX1XeOTU3qGF',
                  consumer_secret='MwVDyHYq4Ria4ub3pAmq7D38dgAEtCJKCVgKOMkBimaJpRkZwp',
                  access_token_key='3119886269-GQfctpmBOpY3wodDxO69SoRdDkCRBYNVjiFOcO0',
                  access_token_secret='6wBXAhL2WjYMZw97patQZUSbJ2GjNjbkRftflrwldpGrn')

                       # ---- Represents the number of stations, but I'm currently only operating with one
                       # |
    drip = SprinklerGPIO(1)

    #  Lists all tweets on the user's TimeLine
    status = api.GetUserTimeline('X')

    while len(status) > 0:

        tweets = [s.text for s in status]
        lastTweet = tweets[0].split()

        if lastTweet[0] == '#waterMe':
            drip.setStationStatus(0,1)
            time.sleep(60)
            drip.setStationStatus(0,0)
            api.DestroyStatus(status[0].id)

        elif lastTweet[0] != '#waterMe':
            print 'delete'
            api.DestroyStatus(status[0].id)

    else:
        print 'no tweets'

    time.sleep(15)  # Avoid twitter rate limiting

while 1:
	waterWatcher()
