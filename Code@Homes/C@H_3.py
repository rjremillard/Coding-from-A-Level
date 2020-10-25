"""
Takes a URL as input
Gets all links from that URL's HTML
Gets all links from those links' HTML

Warning: takes a long time to run as has to go through a lot of webpages
Note 0: Probably very inefficient but oh well
Note 1: HTTP aren't counted as they're bad and very uncommon, but mainly because they're bad
"""

import re
import matplotlib.pyplot as plt
from urllib.request import urlopen
from urllib.error import URLError
from bs4 import BeautifulSoup as Bs


# ---------
#  Backend
# ---------

# Gets urls from webpage
def getUrls(url_: str) -> list:
	try:
		pageObj = urlopen(url_)

	# Bad url
	except URLError as e:
		print(e)

	else:
		# Get "soup" and return all links
		soup = Bs(pageObj.read(), "html.parser")

		return [i.get("href") for i in soup.find_all("a")]


# Adds all actual links to store
def goThrough(url_: str):
	for link in getUrls(url_):
		# Not None
		if link:
			# If actual link
			if link[:5] in ["/wiki", "https"]:
				# As dicts and lists are global
				store["info"][link[:5]] += 1
				store["all links"].append(link)


# re
HREF = re.compile("href=")

store = {"all links": [], "info": {"/wiki": 0, "https": 0}}

# Url to inspect
url = "https://en.wikipedia.org/wiki/" + input("Url to inspect\n> https://en.wikipedia.org/wiki/")

# I tried a recursive program but it was being difficult
for i in getUrls(url):
	goThrough(url)


# ----------
#  Frontend
# ----------


