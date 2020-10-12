"""
:: Nana's Pontoon ::
(Basically blackjack)
"""

import random

# Constants
VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
	'King': 10,	'Ace': 11}

ALL_CARDS = [(i, j) for i in VALUES for j in ["Hearts", "Diamonds", "Clubs", "Spades"]]

VALUES['0'] = 0

# Other variables
go, stop = 0, False
player, computer = [], []


def getCard() -> tuple:
	toUse_ = random.choice(deck)
	while toUse_ in player or toUse_ in computer:
		toUse_ = random.choice(deck)

	deck.remove(toUse_)

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
		else:
			print("\n--------------- Reset ---------------\n")

	# Game
	game, deck = True, ALL_CARDS
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
			player = [('0',)]
			game = False

		# Computer - draws if < 17
		if getSum(player) < 17:
			computer.append((getCard()))

			if getSum(computer) > 21:
				computer = [('0',)]
				game = False

	if getSum(player) > getSum(computer):
		print("Player wins")
	elif getSum(player) < getSum(computer):
		print("Computer wins")
	else:
		if len(player) > len(computer):
			print("Player wins - more cards")
		elif len(computer) > len(player):
			print("Computer wins - more cards")
		else:
			print("Draw")

	go += 1
