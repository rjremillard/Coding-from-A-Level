"""Lesson 1: Dogs and cats"""


class Dog:
	def __init__(self, name: str, age: int):
		self.name, self.age = name, age

	def talk(self, msg: str):
		print("%s says %s" % (self.name, msg))


class DogV2(Dog):
	def reportStatus(self):
		print("%s is %d years old" % (self.name, self.age))


class Cat(DogV2):
	pass


if __name__ == "__main__":
	d1 = DogV2("Steve", 5)
	c1 = Cat("Felix", 4)

	d1.talk("Hi, I'm a dog")
	c1.talk("I am a cat")

	d1.reportStatus()
	c1.reportStatus()
