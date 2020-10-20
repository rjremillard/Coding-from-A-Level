"""
Finding paths between two wikipedia pages
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs


def goInto(url):
	get = urlopen(url)
	html = Bs(get.read(), "html.parser")
	for link in html.h1:
		print(link)


while True:
	try:
		goInto("http://" + input("Url\n> http://"))
		break
	except Exception as e:
		print(e)

