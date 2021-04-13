import math


def bruteForce(num: int) -> bool:
	for i in range(2, num):
		if not num % i:
			return False
	else:
		return True


def sieveOfE(num: int) -> list:
	numbers = [True for _ in range(num+1)]
	for i in range(2, math.floor(math.sqrt(num)) + 1):
		if numbers[i]:
			j = i ** 2
			while j < num:
				numbers[j] = False
				j += i
	return [index+2 for index, prime in enumerate(numbers[2:-1]) if prime]


if __name__ == "__main__":
	x = int(input("Number: "))
	print(f"{x} is {'prime' if bruteForce(x) else 'not prime'}")

	print(f"Primes below {x}: {', '.join(map(str, sieveOfE(x)))}")
