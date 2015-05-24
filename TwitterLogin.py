import twitter

class thirstyGarden:
    ''' A class used to obfuscate the Garden's twitter API login information. '''

    def __init__(self):
        '''Create and return connection to thirstyGarden'''
        self.api = twitter.Api(consumer_key='Z6tyBKfbWTIkbXX1XeOTU3qGF',
                               consumer_secret='MwVDyHYq4Ria4ub3pAmq7D38dgAEtCJKCVgKOMkBimaJpRkZwp',
                               access_token_key='3119886269-GQfctpmBOpY3wodDxO69SoRdDkCRBYNVjiFOcO0',
                               access_token_secret='6wBXAhL2WjYMZw97patQZUSbJ2GjNjbkRftflrwldpGrn'
                               )
