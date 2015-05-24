#******************************************#
#       Twitter-Enabled Garden Watering    #
#          Author: Ben Carothers           #
#******************************************#

import SprinklerGPIO
import twitter
import logging
import time
import re
import datetime

today = datetime.date.today()
LOG_FILENAME = 'waterLog.out'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    )

# Connect to the Garden's Twitter account
def waterWatcher():
    try:

      #TODO move this a file that isn't tracked by git

        api = twitter.Api(consumer_key='Z6tyBKfbWTIkbXX1XeOTU3qGF',
                      consumer_secret='MwVDyHYq4Ria4ub3pAmq7D38dgAEtCJKCVgKOMkBimaJpRkZwp',
                      access_token_key='3119886269-GQfctpmBOpY3wodDxO69SoRdDkCRBYNVjiFOcO0',
                      access_token_secret='6wBXAhL2WjYMZw97patQZUSbJ2GjNjbkRftflrwldpGrn'
                      )

                                         # -- Represents the number of OSPi stations
                                         # |
        drip = SprinklerGPIO.SprinklerGPIO(1)

        #  Lists all tweets on the user's TimeLine
        status = api.GetUserTimeline('X')

        while len(status) > 0:

            tweets = [s.text for s in status]

            gardenRe = re.compile(r"#waterMe \d+|#waterMe")
            options = gardenRe.search(tweets[0]).group().split(" ")

            if options[0] == '#waterMe':
                drip.setStationStatus(0,1)
                minutes = 1 if len(options) < 2 else int(options[1])
                time.sleep(minutes * 60)
                drip.setStationStatus(0,0)
                logging.debug('The garden was watered for %d minutes on %s' % minutes, today.ctime())
                #TODO notify user in some way the garden has been watered
                api.DestroyStatus(status[0].id)
            else:
                #TODO Notify the user a junk tweet was deleted
                api.DestroyStatus(status[0].id)
        else:
            print 'no tweets'
        time.sleep(15)  # Avoid twitter rate limiting
    finally:
        if drip.getStationStatus(0) == 1:
            drip.setStationStatus(0,0)

while 1:
        waterWatcher()

