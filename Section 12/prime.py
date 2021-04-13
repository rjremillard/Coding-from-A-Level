def bruteForce(num: int) -> bool:
	for i in range(2, num):
		if not num % i:
			return False
	else:
		return True


def sieveOfE(num: int) -> list:
	numbers = list(range(2, num+1))
	for i in range(2, int(num ** .5) + 1):
		if i in numbers:
			for j in range(i**2, num + 1, i):
				if j in numbers:
					numbers.remove(j)
	return numbers


if __name__ == "__main__":
	x = int(input("Number: "))
	print(f"{x} is {'prime' if bruteForce(x) else 'not prime'}")
	print(f"Primes below: {sieveOfE(x)}")
