#sx_race_prediction

# this program computes the likelihood of each
# riders placement in the main event each
# week
# needs to access results website
# parse website for data information
# save data into database 
# compute the likelihood of each riders placement
# saves their respective position in the database

import requests
import urllib

from pprint import pprint
from datetime import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
# import local files
import find_races

# connects to mongodb
# accesses the ama supercross website

client = MongoClient()
db = client.supercross
response = requests.get("https://archives.amasupercross.com/")
html = response.text

# checks if the current year race locations are 
# already saved in the db under "races"
if not db.races.find_one( {"year": datetime.now().year} ):
	find_races.find_races()
	pprint("Added 2018 races")
	pprint(db.races.find_one())
else:
	pprint("Not added: Found")
	pprint(db.races.find_one())

# gets practice times of the given race
def get_practice_times(race_name):
	# Get event name from db.races
	# generate url for the race
	# travel to the race event page
	# open up the first and second practice lap times
	# find min for each individual rider
	# assign rank for fastest to slowest rider
	# save ranking to each riders db.riders document
	return 