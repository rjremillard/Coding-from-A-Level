"""cars 'init"""


class Car:
	numCars = 0

	def __init__(self, make, model, price):
		self.make, self.model, self.price, self.sold = make, model, price, False
		Car.numCars += 1

	def sellCars(self):
		if not self.sold:
			self.sold = True
			Car.numCars -= 1
		else:
			raise Exception("Already sold")

	def resetPrice(self, new_price: int):
		self.price = new_price

	def __str__(self):
		return str([self.make, self.model])


if __name__ == "__main__":
	fleet = [Car("Ford", "Focus", 10000), Car("VW", "Beetle", 5600), Car("Lambo", "Aventador", 740000)]

	for car in fleet:
		print(car)
