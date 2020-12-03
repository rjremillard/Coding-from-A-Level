import random


class Question:
	def __init__(self, diff: int):
		self.diff = diff
		self.question, self.answers = None, None

	def generateQuestion(self):
		self.question = f"{random.randint(1, 10 ** self.diff)} {random.choice('+-*')} {random.randint(1, 10 ** self.diff)}"
		tmpAnswer = self.generateAnswer()
		self.answers = {round(tmpAnswer * random.random()) for _ in range(3)} | {tmpAnswer}
		del tmpAnswer
		return self.question, self.answers

	def generateAnswer(self) -> int:
		return eval(self.question)


score = 1
for _ in range(int(input("How many questions>\n> "))):
	question= Question(score)
	q, answers = question.generateQuestion()
	answers = "\n".join(f"{i}: {answers[i]}" for i in range(4))
	answer = int(input(f"Question: {q}\nAnswers: {answers}"))
	if answer == question.generateAnswer():
		print("Correct")
		score += 1
	else:
		print("Incorrect")
		score -= 1
		if score == 0:
			score = 1

print(f"You finished with a score of: {score}")
