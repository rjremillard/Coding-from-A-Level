from urllib.request import urlopen
from bs4 import BeautifulSoup as Bs
import matplotlib.pyplot as plt

# Url to inspect
url = input("Url to inspect\n> https://en.wikipedia.org/wiki/")
max = 2


# Recursive function to go into links
def goInto(link: str, n: int) -> dict:
	# Get a tags and make store dict
	aTags, store = Bs(urlopen(link).read(), "html.parser").find_all("a"), {"internal": 0, "external": 0, "errors": 0,
		"links": []}

	print("aTags: %s" % aTags)

	for tag in aTags:
		link = tag.get("a")

		# If no link
		if not link:
			pass

		# If external link
		elif "http" in link:
			store["external"] += 1

		# If internal link
		elif "wiki" in link:
			store["internal"] += 1

		# Just in case
		try:
			store2 = goInto(link, n)
			# Carry over other scores
			store["internal"] += store2["internal"]
			store["external"] += store2["external"]
			store["errors"] += store2["errors"]
			store["links"].extend(store2["links"])

		except Exception as e:
			store["errors"] += 1
			print(e)

	# Make sure doesn't go too far
	if n > max:
		print(store)
		exit()
	else:
		n += 1

	return store


print(goInto("https://en.wikipedia.org/wiki/" + url, 0))
