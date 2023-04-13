import random


def opt_dist(l, d):
    if len(l) < d:
        return "xD"
    pom = [1] * d + [0] * (len(l) - d)
    min = len(l)

    for _ in range(len(l) - d + 1):
        licz = 0
        for j in range(len(l)):
            if l[j] != pom[j]:
                licz += 1
        if licz < min:
            min = licz

        pom = [0] + pom[:len(pom)-1]

    return min


wynik = [[0 for _ in range(7)] for _ in range(7)]


def spr_wier(obr):
    for i in range(7):
        if opt_dist(wynik[i], obr[0][i]) > 0:
            return False

    return 1


def spr_kol(obr):
    wynik2 = [[0 for _ in range(7)] for _ in range(7)]
    for i in range(7):
        for j in range(7):
            wynik2[j][i] = wynik[i][j]
    for i in range(7):
        if opt_dist(wynik2[i], obr[1][i]) > 0:
            return False

    return 1


def fiks(row, obr):

    row_blocks = obr[0][row]
    dist = opt_dist(wynik[row], row_blocks)

    if dist == 0:
        return

    naj = 0

    for j in range(7):

        wynik2 = []
        for x in range(7):
            wynik2.append(wynik[x][j])

        wiersz_zmian = opt_dist(wynik[row], row_blocks)
        kolumna_zmian = opt_dist(wynik2, obr[1][j])
        zmiany = kolumna_zmian + wiersz_zmian

        wynik[row][j] ^= 1

        nowa_kolumna = []
        for x in range(7):
            nowa_kolumna.append(wynik[x][j])

        nowa_wiersz_zm = opt_dist(wynik[row], row_blocks)
        nowa_kolumna_zm = opt_dist(nowa_kolumna, obr[1][j])
        nowe_zmiany = nowa_wiersz_zm + nowa_kolumna_zm

        if nowe_zmiany < zmiany:
            naj = j

        wynik[row][j] ^= 1

    wynik[row][naj] ^= 1


def miel(obr):
    licz = 0
    while not spr_wier(obr) or not spr_kol(obr):
        if licz % 10 == 0:
            r_i = random.randint(0, 6)
            r_j = random.randint(0, 6)
            wynik[r_i][r_j] ^= 1

        wiersz = random.randint(0, 6)
        fiks(wiersz, obr)
        if licz % 100 == 0:
            for line in wynik:
                line = ['#' if x == 1 else ' ' for x in line]
                print(*line)

        licz += 1
    for line in wynik:
        line = ['#' if x == 1 else ' ' for x in line]
        print(*line)
    print(licz)


SPRAWDZARKA = [([2, 2, 7, 7, 2, 2, 2], [4, 4, 2, 2, 2, 5, 5]), ([2, 2, 7, 7, 2, 2, 2], [2, 2, 7, 7, 2, 2, 2]), ([
    7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7]), ([7, 5, 3, 1, 1, 1, 1], [1, 2, 3, 7, 3, 2, 1])]

miel(SPRAWDZARKA[0])
