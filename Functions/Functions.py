
def func1(num: int) -> int:
	return num ** 3


def func2(num: int) -> list:
	return [num * i for i in range(20)]


def func3(num1: int, num2: int) -> int:
	return num1 + num2


def func4(string: str, letter: str) -> int:
	return string.count(letter)
