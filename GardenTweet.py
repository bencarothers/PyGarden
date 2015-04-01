#******************************************#
# Twitter-Enabled Garden Watering
# *****************************************#
import twitter
import time

api = twitter.Api(consumer_key='Z6tyBKfbWTIkbXX1XeOTU3qGF',
                  consumer_secret='MwVDyHYq4Ria4ub3pAmq7D38dgAEtCJKCVgKOMkBimaJpRkZwp',
                  access_token_key='3119886269-GQfctpmBOpY3wodDxO69SoRdDkCRBYNVjiFOcO0',
                  access_token_secret='6wBXAhL2WjYMZw97patQZUSbJ2GjNjbkRftflrwldpGrn')

def waterWatcher():
	status = []
	x = 0
	status = api.GetUserTimeline('X')
	if len(status)>0:
		lastId = status[0].id;
		tweets = [s.text for s in status]
		drip = tweets[0].split()
		if drip[0] == '#waterMe':
			print 'water'
			api.DestroyStatus(lastId)
		elif drip[0] != '#waterMe':		
			print 'delete'
			api.DestroyStatus(lastId)
	else:
		print 'no tweets'

while 1:
	waterWatcher()
	time.sleep(15) #Avoid twitter rate limiting
