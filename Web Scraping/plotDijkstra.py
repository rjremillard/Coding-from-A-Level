import json

import matplotlib.pyplot as plt

from gettingGraphs import getData
from collections import defaultdict


class PriorityQ():
    def __init__(self):
        self.__list = []

    def enqueue(self, other, priority: int):
        self.__list.append([other, priority])
        self.__list.sort(key=lambda x: x[1])

    def dequeue(self):
        """:return item, priority"""
        return self.__list.pop(0)

    def change(self, other, new):
        for index, item in enumerate(self.__list):
            if item[0] == other:
                self.__list[index][1] = new
                break
        self.__list.sort(key=lambda x: x[1])

    def isEmpty(self) -> bool:
        """:return whether length of queue is 0"""
        return len(self.__list) == 0


# Need the data
with open("Web Scraping\\usData.json", "r") as f:
    data = json.load(f)

# Implement Dijkstra
start = input("Start node ID#: ")
end = input("End node ID#: ")

distances = defaultdict(lambda: [float("inf"), []])
visited = []
queue = PriorityQ()

# Set values
for node in list(data.keys()):
    if node == start:
        distances[node][0] = 0
        queue.enqueue(node, 0)
    else:
        queue.enqueue(node, float("inf"))

while not queue.isEmpty():
    vertex = queue.dequeue()[0]
    visited.append(vertex)
    for node in data[vertex].keys():
        if node not in visited:
            newDist = distances[vertex][0] + float(data[vertex][node])
            if newDist < distances[node][0]:
                distances[node] = [
                    newDist, 
                    distances[vertex][1] + [vertex]
                    ]
                queue.change(node, newDist)

# Get coords
with open("Web Scraping\\usCoords.json", "r") as f:
    coords = json.load(f)

# Plot all roads as a base
for i in data.keys():
    for j in data[i].keys():
        plt.plot(
            [float(coords[i][0]), float(coords[j][0])],
            [float(coords[i][1]), float(coords[j][1])],
            linewidth=.25, color="black"
        )

# Plot path
path = distances[end][1]
path.append(end)
for i in range(len(path)-1):
    plt.plot(
        [float(coords[path[i]][0]), float(coords[path[i+1]][0])],
        [float(coords[path[i]][1]), float(coords[path[i+1]][1])],
        linewidth=.25, color="red"
    )

plt.axis('square')
plt.show()
