"""Contains the following:
    - Bubble sort
    - Insertion sort
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

    return lst

def insertion(lst: list) -> list:
    for i in range(1, len(lst)-1):
        pos = i
        while pos > 0 and lst[pos-1] > lst[pos]:
            lst[pos] = lst[pos-1]
            pos -= 1
        lst[pos] = lst[i]
    return lst
            
if __name__ == "__main__":
    import random
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(lst)

    print(f"lst =       {lst}")

    print(f"Bubble:     {bubble(lst)}")
    print(f"Insertion:  {insertion(lst)}")
