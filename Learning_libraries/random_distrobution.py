import matplotlib.pyplot as plt
import random as ran

# init
fig = plt.figure()
ax1 = fig.add_subplot()

# make random values
lst = [ran.randint(0, 10) for _ in range(5000)]

# plot values
ax1.bar([i for i in range(11)], [lst.count(i) for i in range(11)])

# show
plt.show()
