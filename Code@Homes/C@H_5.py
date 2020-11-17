"""
Done two ways:
	- The easy way:     just prints out the most common words (technically correct)
	- The better way:   takes a random wikipedia article and prints most common words

Also, it has to be said that Thomas has a very strange pastime
"""

import json
import wikipedia


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
