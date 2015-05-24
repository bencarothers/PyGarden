#******************************************#
#       Twitter-Enabled Garden Watering    #
#          Author: Ben Carothers           #
#******************************************#

import SprinklerGPIO
import TwitterLogin
import logging
import time
import re
import datetime

today = datetime.date.today()
LOG_FILENAME = 'waterLog.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    )

# intantiating a class that creates a connection to the Twitter account
# using user specific keys and secrets

thirstyGarden = TwitterLogin.thirstyGarden()
api = thirstyGarden.api

def waterWatcher():
    try:
        dripController = SprinklerGPIO.SprinklerGPIO(1)
        tweetsOnTimeline = api.GetUserTimeline('X')

        for x in range(len(tweetsOnTimeline)):
            tweets = [s.text for s in tweetsOnTimeline]

            waterOptions = re.compile(r"#waterMe \d+|#waterMe")
            foundOptions = waterOptions.search(tweets[0]).group().split(" ")

            if foundOptions[0] == '#waterMe':
                minutes = .1 if len(foundOptions) < 2 else int(foundOptions[1])
                waterForXMinutes(minutes)
                #TODO notify user in some way the garden has been watered
                api.DestroyStatus(tweetsOnTimeline[0].id)
            else:
                #TODO Notify the user a junk tweet was deleted
                api.DestroyStatus(tweetsOnTimeline[0].id)
        else:
            print 'no tweets'

        time.sleep(15)  # Avoid twitter rate limiting

    finally:
        if dripController.getStationStatus(0) == 1:
            dripController.setStationStatus(0,0)

def waterForXMinutes(x):
    dripController.setStationStatus(0,1)
    time.sleep(minutes * 60)
    dripController.setStationStatus(0,0)

while 1:
        waterWatcher()

