import itertools


def znajdzmin(arr, n):

    min = len(arr[0])

    for i in range(1, n):
        if (min > len(arr[i])):
            min = len(arr[i])

    return (min)


def wspolnyprefix(arr, n):

    minlen = znajdzmin(arr, n)
    odp = ""
    for i in range(minlen):

        akt = arr[0][i]

        for j in range(1, n):
            if (arr[j][i] != akt):
                return odp

        odp = odp+akt

    return (odp)


cos = ["Cyprian", "cyberotoman", "cynik", "ceniac", "czule"]
cos = list(map(lambda x: x.lower(), cos))


def podzbiory(s, n):
    return list(itertools.combinations(s, n))


maks = 0
maksstr = ""
cos = podzbiory(cos, 3)
# print(cos)
for i in cos:
    if maks < len(wspolnyprefix(i, len(i))):
        maksstr = wspolnyprefix(i, len(i))
        maks = len(maksstr)
print(maksstr)
