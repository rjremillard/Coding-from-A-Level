import random


"""
To make Miss Langstaff happy:
	- Inputs:		keepGoing
	- Outputs:		Errors, Choices, End
	- Procedures:	too many...	
"""


# init variables
money = 1.00
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]

while True:
	keepGoing = input("You have: %.2f\nWould you like to continue? (y / n)\n: " % money).lower()
	if keepGoing == "n":
		break

	elif keepGoing == "y":
		# take money
		money -= .20

		# get rolls
		choices = [random.choice(symbols) for _ in range(3)]
		print("You got : %s" % " ".join(choices))

		# special cases
		if choices[0] == choices[1] == choices[2]:
			if choices == ["Bell", "Bell", "Bell"]:
				money += 5
				print("+5 for three bells!")
			elif choices == ["Skull", "Skull", "Skull"]:
				money = 0
				print("You lost all of your money from three skulls")
				break
			else:
				money += 1
				print("+1 for three of the same")
		elif choices[0] == choices[1] or choices[1] == choices[2] or choices[0] == choices[2]:
			if choices.count("Skull") == 2:
				print("-1 for two skulls")
			else:
				money += .50
				print("+.50 for two of the same")

	else:
		print("Please enter y or n")

# if quit
print("You ended with: %.2f" % money)
