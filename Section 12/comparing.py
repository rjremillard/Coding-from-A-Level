import matplotlib.pyplot as plt
import time
import threading
import re

from collections import defaultdict
import sorting as s
import data

times = defaultdict(list)
sizes = list(range(10, 3000, 50))

def run(f):
    avgTimes = []
    for i in sizes:
        timesX = []
        for _ in range(10):
            x = [j for j in data.randomList(i)]
            s = time.time()
            f(x)
            timesX.append(time.time()-s)
        avgTimes.append(sum(timesX) / 20)
    
    times[f] = avgTimes

t = []
for func in [s.bubble, s.merge, s.insertion, s.quickHandler]:
    thread = threading.Thread(target=run, args=(func,))
    thread.start()
    t.append(thread)

for thread in t:
    thread.join()

for key in times.keys():
    name = re.findall(r"(?<=<function\s)[a-zA-Z]+(?=.*)", str(key))[0]
    plt.plot(sizes, times[key], label=name)

plt.legend()
plt.show()
