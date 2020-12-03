import random


class Question:
	def __init__(self, diff: int):
		self.diff = diff
		self.question, self.answers, self.answer = None, None, None

	def generate(self):
		num1, num2, op = random.randint(1, 10 ** self.diff), random.randint(1, 10 ** self.diff), random.choice('+-*')
		self.question = f"{num1} {op} {num2}"
		self.answer = eval(self.question)
		self.answers = [self.getRandom(num1, num2, op) for _ in range(3)]
		self.answers.append(self.answer)
		random.shuffle(self.answers)
		return self.question, self.answers

	@staticmethod
	def getRandom(num1: int, num2: int, op: str):
		low1, high1 = num1 - 2, num1 + 2
		low2, high2 = num2 - 2, num2 + 2
		while True:
			ans = eval(f"{random.choice(range(low1, high1))} {op} {random.choice(range(low2, high2))}")
			if ans != eval(f"{num1}{op}{num2}"):
				return ans


score = 1
for _ in range(int(input("How many questions>\n> "))):
	questionObj = Question(score)
	question, answers = questionObj.generate()
	answer = int(input(f"Question: {question}\nAnswers:\n" + "\n".join(f"{num + 1}: {answers[num]}" for num in range(4))
														+ "\n> "))
	if answer == answers.index(questionObj.answer) + 1:
		print("Correct")
		score += 1
	else:
		print("Incorrect")
		score -= 1
		if score == 0:
			score = 1

print(f"You finished with a score of: {score}")
