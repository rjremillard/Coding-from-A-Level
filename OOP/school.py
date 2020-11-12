"""Lesson 2, school members"""


class SchoolMember:
	def __init__(self, age: int, name: str):
		self.age, self.name, self.school = age, name, "TGS"


class Employee(SchoolMember):
	def __init__(self, age: int, name: str, job: str):
		super().__init__(age, name)
		self.job = job

	def speak(self):
		print("%s is an employee at %s" % (self.name, self.school))


class Student(SchoolMember):
	def __init__(self, age: int, name: str, year: int):
		super().__init__(age, name)
		self.year = year

	def speak(self):
		print("%s is a student at %s" % (self.name, self.school))


if __name__ == "__main__":
	e1 = Employee(40, "Steve", "Teacher")
	s1 = Student(10, "John", 8)

	e1.speak()
	s1.speak()
