import matplotlib.pyplot as plt
from .gettingGraphs import getData
from requests import get
from collections import defaultdict

# Get coords
resp = get("https://www.cs.utah.edu/~lifeifei/research/tpq/cal.cnode").text
coords = defaultdict(tuple)
for i in resp.split("\n")[:-1]:
    line = i.split()
    coords[line[0]] = (line[1], line[2])

# Get graph
adjacency = getData("https://www.cs.utah.edu/~lifeifei/research/tpq/cal.cedge")

# Plot graph
for i in adjacency.keys():
    for j in adjacency[i].keys():
        plt.plot(
            [float(coords[i][0]), float(coords[j][0])],
            [float(coords[i][1]), float(coords[j][1])],
            linewidth=.25, color="black"
        )

plt.show()
