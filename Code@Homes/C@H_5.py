"""
Done two ways:
	- The easy way:         just prints out the most common words (technically correct)
	- The better way:       takes a random wikipedia article and prints most common words
	- The even better way:  I got bored so I made one that actually webscrapes

Also, it has to be said that Thomas has a very strange pastime
"""

import json
import wikipedia
import urllib.request
import random
from bs4 import BeautifulSoup


# *** The easy way ***
# Extracts all words from file
with open("C@H_5_words.json", "r") as f:
	data = json.load(f)["words"]

# Prints all words, up to the limit given, alongside their rank
print("\n".join("%d:  \t%s"
						% (i + 1, data[i]) for i in range(int(input("How many words do you want? (Limit 1000)\n> ")))))


# *** The better way ***
# Get all content from random page
pageObj = wikipedia.page(wikipedia.random()).content

allWords = []
for word in pageObj.split():
	tempWord = word
	# Bad characters
	for char in "!\"£$%^&*()-=,./?:;'@#~\\1234567890":
		tempWord = tempWord.replace(char, "")

	# If not blank string
	if tempWord:
		allWords.append(tempWord)

# map is most efficient method, set is used to remove duplicates
counts = list(map(lambda x: (allWords.count(x), x), set(allWords)))

counts.sort(reverse=True)

print("\n".join("%d  \t%s" % (counts[i][0], counts[i][1]) for i in
						range(int(input("How many words do you want? (Limit %d)\n> " % len(counts))))))


# *** The even better way ***
# Take a random webpage from the file
with open("C@H_5_URLs.json", "r") as f:
	urls = json.load(f)

url = random.choice(urls["urls"])

with urllib.request.urlopen(url) as resp:
	data = resp.read()

soup = BeautifulSoup(data, "html.parser")
text = soup.text

# Get words
wordList = []
for word in text.split():
	# Clean up
	word = "".join(char for char in word if char.isalpha())

	if word:
		wordList.append(word)

# Defo not copied from above
counts = list(map(lambda x: (wordList.count(x), x), set(wordList)))
counts.sort(reverse=True)

print("\n".join("%d  \t%s" % (counts[i][0], counts[i][1]) for i in
						range(int(input("How many words do you want? (Limit %d)\n> " % len(counts))))))
