import twitter

class thirstyGarden:
    ''' A class used to hold the Garden's twitter API login information. '''

    def __init__(self):
        '''Create and return connection to thirstyGarden'''
        self.api = twitter.Api(consumer_key='',
                               consumer_secret='',
                               access_token_key='',
                               access_token_secret=''
                               )
