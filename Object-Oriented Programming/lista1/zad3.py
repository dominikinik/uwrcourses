# DOMINIK OLEJARZ
# * LISTA 1 PO: ZAD3 LISTY
# py zad3.py


def createarr():
    return [None, None]


def wstaw(tab, x, poz):
    if len(tab) == 0:
        tab.append(poz)
        tab.append(x)
        tab.append(poz)
    elif tab[0] is None and tab[-1] is None:
        tab[0], tab[1] = poz, poz
        tab.insert(1, x)
    else:
        end = tab[-1]
        if poz < tab[0]:
            for _ in range(tab[0] - poz):
                tab.insert(1, 0)
            tab[0] = poz
        elif poz > end:
            for _ in range(poz - end):
                tab.insert(len(tab) - 1, 0)
            tab[-1] = poz

        tab[poz - tab[0] + 1] = x


def znajdz(tab, i):
    if tab[0] <= i <= tab[-1]:
        return tab[i-tab[0]+1]
    else:
        return "xD"


def showall(tab):
    for i in range(tab[0], tab[-1]+1):
        print(znajdz(tab, i), end=", ")
    print()
    print()


tab1 = createarr()
wstaw(tab1, 1, 1)
wstaw(tab1, 2, 2)
wstaw(tab1, 3, -10)
wstaw(tab1, 4, 15)
print(tab1)
showall(tab1)

tab2 = createarr()
wstaw(tab2, 1, -3)
wstaw(tab2, 2, 2)
wstaw(tab2, 3, 20)
print(tab2)
showall(tab2)
