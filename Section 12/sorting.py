"""Contains the following:
    - Bubble
    - Insertion
    - Merge
    - Quick
** All work in place **
"""

def bubble(lst: list) -> list:
    swapped, i = True, 0
    while swapped or i < len(lst):
        swapped = False
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                swapped = True
                lst[j+1], lst[j] = lst[j], lst[j+1]
        i += 1

def insertion(lst: list) -> list:
    for i in range(1, len(lst)):
        current = lst[i]
        pos = i
        while pos > 0 and lst[pos-1] > current:
            lst[pos] = lst[pos-1]
            pos -= 1
        lst[pos] = current

def merge(lst: list) -> list:
    if len(lst) > 1:
        mid = len(lst) // 2

        left = lst[mid:]
        right = lst[:mid]

        merge(left)
        merge(right)

        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

def __partition(lst: list, start: int, end: int) -> int:
    pivot = lst[start]
    leftMark = start + 1
    rightMark = end

    while True:
        while leftMark <= rightMark and lst[leftMark] <= pivot:
            leftMark += 1
        
        while lst[rightMark] >= pivot and rightMark >= leftMark:
            rightMark -= 1

        if rightMark < leftMark:
            break
        else:
            lst[leftMark], lst[rightMark] = lst[rightMark], lst[leftMark]
        
    lst[start], lst[rightMark] = lst[rightMark], lst[start]
    return rightMark

def quick(lst: list, start: int, end: int) -> list:
    if start < end:
        split = __partition(lst, start, end)

        quick(lst, start, split-1)
        quick(lst, split+1, end)
    
def quickHandler(lst: list) -> list:
    quick(lst, 0, len(lst) - 1)
            
if __name__ == "__main__":
    import random
    
    for _ in range(25):
        lst = lambda: list(range(random.randint(2, 50)))
        target = sorted(lst())

        for func in [bubble, insertion, merge, quickHandler]:
            lst_ = lst()
            func(lst_)
            if lst_ != target:
                print("Fail!")
