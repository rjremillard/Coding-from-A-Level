from Searching import Node, formTree

def preOrder(head: Node) -> list:
     ...
    
def inOrder(head: Node) -> list:
    ...

def preOrder(head: Node) -> list:
    ...

if __name__ == "__main__":
    lst = list(range(10))

    head = formTree(lst)

    print(f"inOrder:    {list(inOrder(head))}")
