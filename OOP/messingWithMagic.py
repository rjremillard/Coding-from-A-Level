"""Experimenting with magic (dunder) methods"""


# A date example
class Date:
	def __init__(self, **kwargs):
		"""
		:param kwargs: sec, min, hour, day, month, year
		"""

		for item in ['sec', 'min', 'hour', 'day', 'month', 'year']:
			exec("self.%s = %d" % (item, kwargs[item] if item in kwargs else 0))

	def __str__(self) -> str:
		return ", ".join("%s: %s" % (key, self.__dict__[key]) for key in self.__dict__)

	def __add__(self, other: "Date") -> "Date":
		dic = {}
		for item in ['sec', 'min', 'hour', 'day', 'month', 'year']:
			dic[item] = eval("self.%s + other.%s" % (item, item))

		return Date(**dic)


if __name__ == "__main__":
	date1 = Date(day=10, month=9, year=2020)
	date2 = Date(hour=10, month=7, year=1299)
	print(date1, date2, sep="\n")

	print(date1 + date2)
