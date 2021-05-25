from random import randint
from math import ceil, log2
import matplotlib.pyplot as plt

def guess(target: int, len_: int) -> int:
    tries, guess = 1, ceil(len_ / 2)
    len_ = ceil(len_ / 2)
    while guess != target:
        len_ = ceil(len_ / 2)
        if guess > target:
            guess -= len_
        else:
            guess += len_
        tries += 1
    return tries

# Actual data
xs = list(range(10, 500000, 500))
ys = []
for i in xs:
    tmp = []
    for _ in range(5):
        tmp.append(guess(randint(0, i), i))
    ys.append(tmp)

plt.plot(xs, ys, "bo")
plt.plot([0, ], [0, ], "bo", label="Guesses")

def mean(x: list) -> int:
    return sum(x) / len(x)

# Averages
avgs = list(map(mean, ys))
plt.plot(xs, avgs, "g", label="Average")

# Log2
ys1 = list(map(log2, xs))
plt.plot(xs, ys1, "r", label="log2")

# Previous 7
ys2 = []
for i in range(7, len(avgs)):
    ys2.append(mean(avgs[i-7: i]))
plt.plot(xs[7:], ys2, "y", label="Mean of 7 prior")

plt.xlabel("Size")
plt.ylabel("Guesses")
plt.legend()
plt.show()

# Prev x average
colours = ["b", "y", "g", "r", "c", "m", "pink", "orange", "peru"]
for farBack in range(1, 10):
    ys3 = []
    for j in range(farBack, len(avgs)):
        ys3.append(mean(avgs[j-farBack: j]))
    plt.plot(xs[farBack:], ys3, colours[farBack-1], label=f"Average of {farBack} prior")

plt.xlabel("Size")
plt.ylabel("Guesses")
plt.legend()
plt.show()
