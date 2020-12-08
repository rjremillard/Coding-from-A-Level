"""
Basic arithmetic quiz, serving a chosen number of questions
The difficulty will increase and decrease with correct and incorrect answers, accordingly
"""

import random


class Question:
	"""For each question, takes a difficulty <diff>: ∈Z+"""
	def __init__(self, diff: int):
		self.diff = diff

	def generate(self):
		"""
		Generates the question string, fake answers, and the actual answer
		The question consists of one operand <op>, of +, -, or *, and two numbers <num1> and <num2>
			where the numbers are randomly chosen from the range of [1, 10^<diff>]

		Plausible answers are chosen by getRandom, added to a list, and then shuffled

		:return _question:  the question string generated
		:return _answers:   the plausible, fake, answers
		:return answer:     the actual answer
		"""
		num1, num2, op = random.randint(1, 10 ** self.diff), random.randint(1, 10 ** self.diff), random.choice('+-*')
		_question = f"{num1} {op} {num2}"
		_answer = eval(_question)
		_answers = [self.getRandom(num1, num2, op) for _ in range(3)]
		_answers = list(set(_answers))
		_answers.append(_answer)
		random.shuffle(_answers)
		return _question, _answers, _answer

	@staticmethod
	def getRandom(num1: int, num2: int, op: str):
		"""
		Takes the question's parts and reconstructs a question with numbers in the range of <num1> ± 2 and <num2> ± 2
			to return a close-ish answer, given it is not the same as the actual answer

		:param num1:    the first number in the equation
		:param num2:    the second number in the equation
		:param op:      the operand for the equation
		:return ans:    the answer to be added to the list
		"""
		low1, high1 = num1 - 2, num1 + 2
		low2, high2 = num2 - 2, num2 + 2
		while True:
			ans = eval(f"{random.choice(range(low1, high1))} {op} {random.choice(range(low2, high2))}")
			if ans != eval(f"{num1}{op}{num2}"):
				return ans


score = 1
for _ in range(int(input("How many questions>\n> "))):
	questionObj = Question(score)
	question, answers, answer = questionObj.generate()
	answerGuess = int(input(f"Question: {question}\nAnswers:\n" + "\n".join(f"{num + 1}: {answers[num]}" for num in range(4)) + "\n> "))
	if answerGuess == answers.index(answer) + 1:
		print("Correct")
		score += 1
	else:
		print("Incorrect")
		score -= 1
		if score == 0:
			score = 1

print(f"You finished with a score of: {score}")
