import json

"""
I didn't find I needed functions for this
"""


stop = False
while not stop:
	# choose what to do
	choice = int(input("Play or check scores: \n1. Scores \n2. Play\n3. Exit\n: "))

	# check scores
	if choice == 1:
		with open("History.json", "r") as f:
			history = json.load(f)

		usrChoice = input("What name do you want to find? ")

		if usrChoice in history:
			print("%s found!\nUsername: %s\nAge: %d\nScores: %s" %
				(usrChoice, history[usrChoice]["username"], history[usrChoice]["age"], ", ".join(history[usrChoice]["scores"])))

		else:
			print("User not found")

	# play
	elif choice == 2:
		score = 0

		# inputs
		name, age, password = input("Name: "), int(input("Age: ")), input("Password: ")
		username = name[:3] + str(age)

		# questions
		topic, diff = input("What topic? (english / maths): ").lower(), int(input("Difficulty? (1-3) "))

		with open("Questions.json", "r") as f:
			questions = json.load(f)

		for q in questions[topic]:
			answers = ", ".join(q[1][:diff+1])

			ans = input("%s\n%s\n: " % (q[0], answers))

			if ans == q[1][q[2]]:
				score += 1
				print("Correct")

			else:
				print("Wrong, it was %s" % q[1][q[2]])

		# final score
		print("You got %d right, which is %d%s" % (score, (score / 5) * 100, "%"))

		with open("History.json", "r") as f:
			history = json.load(f)

		# if they exist
		if name in history:
			history[name]["scores"].append("%s (%d): %d" % (topic, diff, score))

		else:
			history[name] = {
				"age": age,
				"username": username,
				"scores": ["%s (%d): %d" % (topic, diff, score)],
				"password": password
			}

		# put back
		with open("History.json", "w") as f:
			json.dump(history, f)

	# stop
	elif choice == 3:
		stop = True

	else:
		print("Enter a number between 1 and 3 inclusive")
