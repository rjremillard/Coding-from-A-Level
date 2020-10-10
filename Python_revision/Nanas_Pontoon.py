"""
:: Nana's Pontoon ::
(Basically blackjack)
"""

import random
import tkinter
from itertools import permutations

# Constants
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10,
	'Ace': 11}

ALL_CARDS = [(i, j) for i in VALUES for j in ["Hearts", "Diamonds", "Clubs", "Spades"]]

# Other variables
go, stop = 0, False
player, computer = [], []


def getCard() -> tuple:
	toUse_ = random.choice(ALL_CARDS)
	while toUse_ in player or toUse_ in computer:
		toUse_ = getCard()

	return toUse_


def getSum(who: list) -> int:
	return sum(VALUES[i[0]] for i in who)


# Main
while not stop:
	print("Go: %d" % (go + 1))
	if go:
		goAgain = input("Do you want to keep going (y/n): ")
		if goAgain.lower() != "y":
			break

	# Game
	game = True
	player = [getCard(), getCard()]
	computer = [getCard(), getCard()]
	while game:
		print("Player: %s\nComputer: %s" % (", ".join("%s of %s" % (player[i][0], player[i][1]) for i in range(len(player))),
											", ".join("%s of %s" % (computer[i][0], computer[i][1]) for i in range(len(computer)))))

		# PLayer
		choice = input("Stick or Twist (s or t): ")
		if choice.lower() == "s":
			game = False
		else:
			toUse = getCard()
			player.append(toUse)
			print("You drew: %s of %s" % (toUse[0], toUse[1]))

		if getSum(player) > 21:
			print("You're bust")
			player = [(2, 0)]
			game = False

		# Computer - draws if < 17
		if getSum(player) < 17:
			computer.append((getCard()))

			if getSum(computer) > 21:
				computer = [(2, 0)]
				game = False

	if getSum(player) > getSum(computer):
		print("Player wins")
	elif getSum(player) < getSum(computer):
		print("Computer wins")

	go += 1
