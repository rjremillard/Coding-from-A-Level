# TODO: Dijkstra's, Dijkstra's with paths

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
        return len(self.__list) == 0

    
def dijkstra(adjacency: dict, start) -> dict:
    distances = {}
    visited = []
    queue = PriorityQ()
    # Set values and enqueue
    for node in adjacency.keys():
        if node == start:
            distances[node] = 0
            queue.enqueue(node, 0)
        else:
            distances[node] = float("inf")
            queue.enqueue(node, float("inf"))
    # Start
    while not queue.isEmpty():
        vertex = queue.dequeue()[0]
        visited.append(vertex)
        for node in adjacency[vertex].keys():
            if node not in visited:
                newDist = distances[vertex] + adjacency[vertex][node]
                if newDist < distances[node]:
                    distances[node] = newDist
                    queue.change(node, newDist)
    return distances


if __name__ == "__main__":
    matrix = {
        "A": {"B": 7, "D": 3},
        "B": {"A": 7, "C": 3, "D": 2, "E": 6},
        "C": {"B": 3, "D": 4, "E": 1},
        "D": {"A": 3, "B": 2, "C": 4, "E": 7},
        "E": {"B": 6, "C": 1, "D": 7} 
    }

    print(dijkstra(matrix, "A"))
