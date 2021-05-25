class Stack():
    def __init__(self):
        self.__list = []

    def pop(self):
        return self.__list.pop()
    
    def push(self, other):
        self.__list.append(other)

class Queue():
    def __init__(self):
        self.__list = []
    
    def dequeue(self):
        return self.__list.pop(0)
    
    def enqueue(self, other):
        self.__list.append(other)
    
    def empty(self):
        return len(self.__list) == 0

def dft(matrix, current, visited=[]):
    visited.append(current)
    for i in matrix[current]:
        if i not in visited:
            dft(matrix, i, visited)
    return visited

def bft(adjacency, start):
    queue = Queue()
    visited = []
    otherList = []
    queue.enqueue(start)

    while not queue.empty():
        current = queue.dequeue()
        visited.append(current)
        otherList.append(current)

        for i in adjacency[current]:
            if i not in otherList:
                queue.enqueue(i)
                otherList.append(i)

    return visited

# nodes = input("Space seperated nodes: ").split()
# adjacency = {}
# for node in nodes:
#     adjacency[node] = input(f"Space seperated neighbours of {node}: ").split()

nodes = "ABCDEFG"
adjacency = {
    "A": "BDE",
    "B": "ACD",
    "C": "BG",
    "D": "ABEF",
    "E": "AD",
    "F": "D",
    "G": "C"
}

print(f"DFT: {dft(adjacency, nodes[0])}")
print(f"BFT: {bft(adjacency, nodes[0])}")
