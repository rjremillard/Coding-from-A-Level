"""
:: Nana's Pontoon ::
(Basically blackjack)
"""

import random
import tkinter
from itertools import permutations

# Constants
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
	'Ace': (1, 11)}

ALL_CARDS = [(i, j) for i in VALUES for j in ["Hearts", "Diamonds", "Clubs", "Spades"]]

# Other variables
go, stop = 0, False
player, computer = [], []


def getCard() -> tuple:
	toUse_ = random.choice(ALL_CARDS)
	while toUse_ in player or toUse_ in computer:
		toUse_ = getCard()

	return toUse_


# Main
while not stop:
	if go:
		go = input("Do you want to keep going (y/n): ")
		if go.lower() == "y":
			stop = False
		else:
			stop = True

	# Game
	game = True
	player = [getCard(), getCard()]
	computer = [getCard(), getCard()]
	while game:
		print("Player: %s\nComputer: %s" % (", ".join("%s of %s" % (player[i][0], player[i][1]) for i in range(len(player))),
											", ".join("%s of %s" % (computer[i][0], computer[i][1]) for i in range(len(computer)))))

		choice = input("Stick or Twist (s or t): ")
		if choice.lower() == "s":
			game = False
		else:
			toUse = getCard()
			player.append(toUse)
			print("You drew: %s of %s" % (toUse[0], toUse[1]))
