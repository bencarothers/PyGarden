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
logger = logging.getLogger("WaterLogged.out")

# Connects to the garden's Twitter account
# using user specific keys and secrets
thirstyGarden = TwitterLogin.thirstyGarden()
api = thirstyGarden.api

def waterWatcher():
    try:
        dripController = SprinklerGPIO.SprinklerGPIO(1)
        tweetsOnTimeline = api.GetUserTimeline('X')

        for x in range(len(tweetsOnTimeline)):
            tweets = [s.text for s in tweetsOnTimeline]
            waterOptions = re.compile(r"#waterMe \d+|#waterMe").search(tweets[0])
            foundOptions = "none found" if waterOptions is None else waterOptions.group().split(" ") 

            if foundOptions[0] == '#waterMe':
                minutes = dripController.waterForXMinutes(0,foundOptions)
                logger.debug("The garden was watered for %d minutes" % minutes)
                api.DestroyStatus(tweetsOnTimeline[0].id)

            else:
                api.DestroyStatus(tweetsOnTimeline[0].id)

        print 'no tweets'
        time.sleep(15)  # Avoid twitter rate limiting

    finally:
        if dripController.getStationStatus(0) == 1:
            dripController.setStationStatus(0,0)

if __name__ == "__main__":
    while 1:
        waterWatcher()

