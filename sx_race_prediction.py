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

#gets the ama archives website
response = requests.get("https://archives.amasupercross.com/")
html = response.text
soup = BeautifulSoup(html, "html.parser")

# grabs iframe from archive website and 
# joins the iframe url to main url
iframe = soup.find(id = "ifrm")["src"]
iframe_url = urllib.parse.urljoin("https://archives.amasupercross.com/", iframe)

# creates new request and soup for the iframe request
iframe_response = urllib.request.urlopen(iframe_url)
iframe_soup = BeautifulSoup(iframe_response, "html.parser")

# gets the tables from the iframe
tables = iframe_soup.find_all("table")
# narrows the tables to be just the one from 2018-2015
table = tables[1]
rows = table.find_all("tr")
#removes the first row because it is just formatting
rows.pop(0)


