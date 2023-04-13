import functools
import timeit


def doskonale_imperatywna(n):
    odp = []
    for i in range(2, n+1):
        sum = 0
        for j in range(1, i//2+1):
            if i % j == 0:
                sum += j
        if sum == i:
            odp.append(i)
    return odp


def doskonale_skladana(n):
    def rozebranie(x): return [i for i in range(1, x) if x % i == 0]

    doskonalelicz = [i for i in range(1, n+1) if sum(rozebranie(i)) == i]
    return doskonalelicz


def doskonale_funkcyjna(n):
    return list(filter(lambda x: perfecto(x), range(2, n+1)))


def perfecto(x):
    dzielniki = filter(lambda i: x % i == 0, range(1, x))
    return functools.reduce(lambda x, y: x + y, dzielniki) == x


i = 10
while i < 10e5:
    print(i, end=" ")
    print("imperatywna:", timeit.timeit("doskonale_imperatywna(" + str(i)+")",
          setup="from __main__ import doskonale_imperatywna", number=1), end=" ")
    print("skladana:", timeit.timeit("doskonale_skladana(" + str(i)+")",
          setup="from __main__ import doskonale_skladana", number=1), end=" ")
    print("funk:", timeit.timeit("doskonale_funkcyjna(" + str(i)+")",
          setup="from __main__ import doskonale_funkcyjna", number=1), end=" ")
    print()
    i *= 10
