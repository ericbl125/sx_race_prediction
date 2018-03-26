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
import sys
from bs4 import BeautifulSoup
import urllib

def store_races(db):
	# accesses amasupercross.com and parsers the website to read the race locations/names
	# stores the race names into database for future reference
	# db is the object for the database retrieved in main
	response = requests.get("https://archives.amasupercross.com/")
	html = response.text
	soup = BeautifulSoup(html, "html.parser")

	# grabs iframe from archive website and joins the iframe url to main url
	iframe = soup.find(id = "ifrm")["src"]
	iframe_url = urllib.parse.urljoin("https://archives.amasupercross.com/", iframe)

	# creates new request and soup for the iframe portion of webpage
	iframe_response = urllib.request.urlopen(iframe_url)
	iframe_soup = BeautifulSoup(iframe_response, "html.parser")

	# gets the tables from the iframe and selects the one for years 2018-2015
	tables = iframe_soup.find_all("table")
	table = tables[1]

	#gets the rows of the table and removes the first one which is just formatting
	rows = table.find_all("tr")	
	rows.pop(0)
	# gets the string inside the anchor for the race name
	# saves string into the database
	for row in rows:
		race = rows[0].find("td").a.contents[0]
		db.races.insert({"name": race})

# this line will parse the anchor href with the main url
print (urllib.parse.urljoin("https://archives.amasupercross.com/", race))


