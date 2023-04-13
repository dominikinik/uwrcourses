# zamiescilem txt z 1 akapitem starego czlowieka i morze
from random import randrange


def napraw(zdanie, maksslo, makszd):
    wynikowe = []

    data = zdanie.split(" ")
    for i in data:
        if len(i) <= maksslo:
            wynikowe.append(i)
    if len(wynikowe) >= makszd:
        roznica = len(wynikowe)-makszd

        for j in range(roznica):
            index = randrange(len(wynikowe))
            wynikowe.pop(index)
    wynikstr = ""
    for i in wynikowe:
        wynikstr += i
        wynikstr += " "

    print(wynikstr)


def uprosczdanie(dane, maksslowo, makswyrazy):
    for i in range(len(dane)):
        napraw(dane[i], maksslowo, makswyrazy)


with open("test.txt", 'r') as data_file:
    for line in data_file:
        data = line.split(".")
uprosczdanie(data, 5, 10)
