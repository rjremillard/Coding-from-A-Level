import threading
from _sha256 import sha256

from itertools import permutations


def breaker(passwd: str, word_list: list = None, verbose: bool = False):
	"""
	Attempts to brute force a solution to the sha256 hash provided
	Will cycle through all alphanumeric combinations until a solution is found, unless a wordlist is provided
		then it will be used instead of a character list.
	Works recursively to keep going through permutations until a solution is found

	n.b. Using a wordlist is extremely recommended
	"""

	CHARACTERS = [chr(i) for i in range(48, 59)]
	CHARACTERS.extend([chr(i) for i in range(65, 91)])
	CHARACTERS.extend([chr(i) for i in range(97, 123)])
	verboseIndex = 0

	if word_list:
		for word in word_list:
			if verbose and verboseIndex == 0:
				# TODO: Fix Verbose
				print(f"\rTrying: {word}", end="")
				verboseIndex = (verboseIndex + 1) % 10
			if word == passwd:
				print(f"Solution: {word}")
				return
		else:
			try:
				newList = []
				for word in permutations(word_list, 2):
					newList.append("".join(word))

				return breaker(passwd, word_list=newList, verbose=verbose)
			except MemoryError:
				# TODO: Fix all memory errors
				print("Memory Error")
				return

	else:
		for char in CHARACTERS:
			if verbose and verboseIndex == 0:
				print(f"\rTrying: {char}", end="")
				verboseIndex = (verboseIndex + 1) % 10
			if char == passwd:
				print(f"Solution: {char}")
				return
		else:
			try:
				newList = []
				for word in permutations(CHARACTERS, 2):
					newList.append("".join(word))

				return breaker(passwd, word_list=newList, verbose=verbose)
			except MemoryError:
				print("Memory Error")
				return


if __name__ == "__main__":
	words = ["pass", "random", "word", "filler"]

	thread = threading.Thread(target=breaker, args=("randompassword", ), kwargs={"word_list": words})
	thread.start()
