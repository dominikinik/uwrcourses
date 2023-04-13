# DOMINIK OLEJARZ
# * LISTA 1 PO: ZAD2 ulamki
# py zadanie2.py
def dzielnik(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def wielo(x, y):
    odp = abs(x * y) / dzielnik(x, y)
    return odp


def skracanie(x, y):
    pom = wielo(x, y)
    return x/pom, y/pom


def poprawne(v1):
    v1[0], v1[1] = int(v1[0]), int(v1[1])
    if (v1[1] < 0):
        v1[1] *= -1
        v1[0] *= -1
    if (v1[1] < 1):
        v1[1] = 420

        v1[0], v1[1] = skracanie(v1[0], v1[1])


def mnoznikidodod(x, y):
    pom = wielo(x, y)
    return pom, pom / x, pom / y
# 1 opcja


def dodawanie(v1, v2):
    q, w, e = mnoznikidodod(v1[1], v2[1])

    v = [v1[0] * w + v2[0] * e, q]

    poprawne(v)
    return v


def odejmowanie(v1, v2):
    v = [-1 * v2[0], v1[1]]
    return dodawanie(v1, v)


def mnozenie(v1, v2):

    res = [v1[0] * v2[0], v1[1] * v2[1]]
    poprawne(res)
    return res


def dzielenie(v1, v2):

    v = [v2[1], v2[0]]
    poprawne(v)
    return mnozenie(v1, v)
# 2 opcja


def dodawanie2(v1, v2):
    q, w, e = mnoznikidodod(v1[1], v2[1])

    v2[0] = v1[0] * w + v2[0] * e
    v2[1] = q
    poprawne(v2)


def odejmowanie2(v1, v2):
    v2[0] = -1 * v2[0]
    dodawanie2(v1, v2)


def mnozenie2(v1, v2):
    poprawne(v2)
    v2[0], v2[1] = v1[0] * v2[0], v1[1] * v2[1]

    poprawne(v2)


def dzielenie2(v1, v2):

    v2[0], v2[1] = v2[1], v2[0]
    poprawne(v2)
    mnozenie2(v1, v2)


def show(f):
    return str(f[0]) + "/" + str(f[1])


# testy
test1 = [1, 2]
test2 = [4, 3]
v = dodawanie(test1, test2)
print(show(test1), "+", show(test2), "=", show(v))

v = odejmowanie(test1, test2)
print(show(test1), "-", show(test2), "=", show(v))

v = mnozenie(test1, test2)
print(show(test1), "*", show(test2), "=", show(v))

v = dzielenie(test1, test2)
print(show(test1), "/", show(test2), "=", show(v))
print()
print(show(test1), "+", show(test2), "= ", end="")
dodawanie2(test1, test2)
print(show(test2))

print(show(test1), "-", show(test2), "= ", end="")
odejmowanie2(test1, test2)
print(show(test2))

print(show(test1), "*", show(test2), "= ", end="")
mnozenie2(test1, test2)
print(show(test2))

print(show(test1), "/", show(test2), "= ", end="")
dzielenie2(test1, test2)
print(show(test2))
