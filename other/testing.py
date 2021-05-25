from timeit import timeit

def map_(l, f):
    return map(f, l)

def iterate(l, f):
    new = []
    for i in l:
        new.append(f(i))
    return new

def iterators(l, f):
    return [f(i) for i in l]

def inPlace(l, f) :
    for i in range(len(l)):
        l[i] = f(l[i])
    return l

def func(x):
    return x ** (x + 1)

lst = list(range(100))

for i in [map_, iterate, iterators, inPlace]:
    print(f"{i.__name__}:\t\t{timeit(lambda: i(lst, func), number=1000)}")
