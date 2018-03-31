import requests
from bs4 import BeautifulSoup
import urllib
from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client["supercross"]
response = requests.get("https://archives.amasupercross.com/")
html = response.text

def store_races(rows):
	collection = db["races"]
	
	race_year = datetime.now()
	races = {"year": race_year.year, 
		"races": {}
		}

	for index in range(len(rows)):
		# breaks down the table rows into a single 
		# anchor tag with the race name
		# adds race name to the db.races collection

		# might want to update dictionary to be
		# "Race_City" : "Full_Race_Name"
		# will most likely need import re in order to
		# get just the city name
		col = rows[index].find("td")
		race = col.a.contents[0]	# hard code 0 to keep in proper column of table	
		races["races"]["{}".format(index+1)] = race

	db.races.insert_one(races)
	

	
	return 

def find_races():
	# accesses amasupercross.com and parsers the website to read the race locations/names
	# stores the race names into database for future reference
	# db is the object for the database retrieved in main
	
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
	rows.pop()
	# gets the string inside the anchor for the race name
	# saves string into the database
	store_races(rows)

	return
