import timeit
import math
import functools


def pierwsze_imperatywna(n):
    odp = []
    for i in range(2, n+1):
        pier = True
        for j in range(2, i):
            if i % j == 0:
                pier = False
        if pier:
            odp.append(i)
    return odp


def pierwsze_skladana(n):
    noprime = [niepierwsze for i in range(2, math.floor(math.sqrt(n)+1)) for
               niepierwsze in range(i*2, n+1, i)]
    primes = [i for i in range(2, n+1) if i not in noprime]
    return primes


def pierwsze_funkcyjna(n):
    def pomlis(_list): return lambda x: x not in _list

    l1 = list(map(lambda x: list(range(x*2, n+1, x)),
                  range(2, n+1)))
    l2 = functools.reduce(lambda x, y: x + list(filter(pomlis(x), y)),
                          l1)
    return list(filter(pomlis(l2), range(2, n+1)))


i = 10
while i < 101:
    print(i, end=" ")
    print("imperatywna:", timeit.timeit("pierwsze_imperatywna(" + str(i)+")",
          setup="from __main__ import pierwsze_imperatywna", number=1), end=" ")
    print("skladana:", timeit.timeit("pierwsze_skladana(" + str(i)+")",
          setup="from __main__ import pierwsze_skladana", number=1), end=" ")
    print("funk:", timeit.timeit("pierwsze_funkcyjna(" + str(i)+")",
          setup="from __main__ import pierwsze_funkcyjna", number=1), end=" ")
    print()
    i += 10
