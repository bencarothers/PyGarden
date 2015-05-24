#******************************************#
#       Twitter-Enabled Garden Watering    #
#                                          #
#          Author: Ben Carothers           #
#******************************************#

from logging.config import fileConfig
import SprinklerGPIO
import TwitterLogin
import logging
import time
import re

fileConfig('logging_config.ini')
logger = logging.getLogger()

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
                waterForXMinutes(foundOptions)
                api.DestroyStatus(tweetsOnTimeline[0].id)

            else:
                api.DestroyStatus(tweetsOnTimeline[0].id)

        print 'no tweets'
        time.sleep(15)  # Avoid twitter rate limiting

    finally:
        if dripController.getStationStatus(0) == 1:
            dripController.setStationStatus(0,0)


def waterForXMinutes(x):
    minutes = .1 if len(foundOptions) < 2 else int(foundOptions[1])
    dripController.setStationStatus(0,1)
    time.sleep(minutes * 60)
    dripController.setStationStatus(0,0)
    logger.debug("The garden was watered for %d minutes" % minutes)

def notifyUser():
    #TODO

while 1:
        waterWatcher()

