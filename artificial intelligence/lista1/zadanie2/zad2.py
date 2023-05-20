# -*- coding: utf-8 -*-
def naprawa(l):
    l = " " + l
    global slo
    czyjest = [0 for _ in range(len(l))]
    czyjest[0] = 1

    start = [[] for _ in range(len(l))]

    for i in range(1, len(l)):  # zaznaczamy mozliwe slowa startowe
        if l[1:i+1] in slo:
            czyjest[i] = 1
   # print(czyjest)
    for i in range(1, len(l)):
        for j in range(i + 1):
            # print("czy ",j-1,l[j:i+1])
            if czyjest[j - 1] and l[j:i+1] in slo:
                # print(l[j:i+1])
                czyjest[i] = 1
                start[i].append(j)
    # print(start)
    najslowo = [[0, []] for _ in range(len(l))]
    ok = [0 for _ in range(len(l))]
    ok[-1] = 1

    for i in reversed(range(1, len(l))):
        if ok[i]:
            for j in range(len(start[i])):
                slowo = start[i][j]
                # print(start[i][j])
                kontrola = najslowo[i][0] + (slowo - i + 1) ** 2
                if kontrola > najslowo[slowo-1][0]:
                    # print("*")
                    najslowo[slowo - 1] = [kontrola, [slowo] + najslowo[i][1]]
                    # print(najslowo)
                   # print()
                    ok[slowo - 1] = 1

    odp = list(l)
    # print(najslowo)
    for ind in reversed(najslowo[0][1]):
        odp.insert(ind, " ")

    f = open("zad2_output.txt", "a")
    f.write(''.join(odp) + "\n")
    f.close()
   # print(odp)


def wczyt():
    global slo, text
    slo = set(open("r.txt", "r", errors="ignore").read().split("\n"))
    text = open("t.txt", "r").read().split("\n")


def spacje():
    for line in text:
        naprawa(line)


open("zad2_output.txt", "w").close()
wczyt()
spacje()
