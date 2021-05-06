import random

def randomList(max_: int) -> list:
    tmp = list(range(max_))
    random.shuffle(tmp)
    return tmp

def nearlySorted(max_: int, swapChance: int = .7) -> list:
    tmp = list(range(max_))
    for i in range(max_-1):
        if random.uniform(0, 1) > swapChance:
            tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
    return tmp

def reversedList(max_: int) -> list:
    return list(range(max_, 0, -1))

def fewUnique(length: int, clusters: int) -> list:
    tmp = []
    for i in range(clusters):
        tmp.extend([i] * (length // clusters))
    tmp.extend([i+1] * (length % clusters))
    random.shuffle(tmp)
    return tmp

if __name__ == "__main__":
    print(f"""Testing for max_ = 20, clusters = 4
    random:         {randomList(20)}
    nearlySorted:   {nearlySorted(20)}
    reversed:       {reversedList(20)}
    fewUnique:      {fewUnique(20, 4)}
    """)
