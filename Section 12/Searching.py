"""Contains the following:
    - Linear search
    - Binary search
    - Recursive binary search

Each takes a list and a target and returns the index of that target, -1 if not found
"""

def linear(lst: list, target: any) -> int:
    for index, item in enumerate(lst):
        if item == target:
            return index
    else:
        return -1

def binary(lst: list, target: any) -> int:
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1

def recursiveBinary(lst: list, target: any) -> int:
    if len(lst) > 1 and lst[0] != target:
        mid = len(lst) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            return recursiveBinary(lst[:mid], target)
        else:
            return recursiveBinary(lst[mid+1:], target)
    else:
        return -1

class Node:
    def __init__(self, data: any):
        self.data = data
        self.left = None
        self.right = None

def addNode(head: Node, data: any):
    if data < head.data:
        if head.left:
            addNode(head.left, data)
        else:
            head.left = Node(data)
    else:
        if head.right:
            addNode(head.right, data)
        else:
            head.right = Node(data)

def formTree(lst: list) -> Node:
    head = Node(lst[len(lst)//2])

    for i in lst:
        addNode(head, i)

    return head

def binaryTreeSearch(head: Node, target: any) -> bool:
    if head.data == target:
        return True
    elif target < head.data:
        if head.left:
            return binaryTreeSearch(head.left, target)
        else:
            return False
    else:
        if head.right:
            return binaryTreeSearch(head.right, target)
        else:
            return False


if __name__ == "__main__":
    # Testing
    import random

    for _ in range(10):
        # Have to use a set so are no repeats
        lst = set()
        for __ in range(random.randint(2, 10)):  # Max size of 10
            lst.add(random.randint(0, 100))
        lst = list(lst)
        lst.sort()

        target = random.randint(0, 100)
        print(f"Testing: {lst} for {target}")

        if target in lst:
            index = lst.index(target)
        else:
            index = -1

        for algo in [linear, binary, recursiveBinary]:
            if algo(lst, target) != index: 
                print("Fail!")
        
        head = formTree(lst)
        if binaryTreeSearch(head, target) != (index != -1): 
            print("Fail!")
