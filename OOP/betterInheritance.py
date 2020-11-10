"""Still pets but with better inheritance"""


class Pet:
	def __init__(self, name: str, age: int, _type: str = "unknown"):
		self.name, self.age, self.type = name, age, _type

	def report(self):
		print("%s is a %s and is %d years old" % (self.name, self.type, self.age))

	def talk(self, msg: str):
		print("%s says %s" % (self.name, msg))

	def birthday(self):
		self.age += 1


class Dog(Pet):
	def __init__(self, name: str, age: int, jump: bool):
		super().__init__(name, age, _type="dog")
		self.jump = jump


class Cat(Pet):
	def __init__(self, name: str, age: int):
		super().__init__(name, age, _type="cat")


if __name__ == "__main__":
	d1 = Dog("Fido", 10, True)
	c1 = Cat("Felix", 3)
	u1 = Pet("Steve", 2)

	d1.talk("WOOF WOOF")
	c1.talk("meow")
	u1.talk("hii")

	d1.report()
	c1.report()
	u1.report()
