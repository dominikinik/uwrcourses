# zamiescilem txt z 1 akapitem starego czlowieka i morze
with open('test.txt', 'r') as file:
    data = file.read()


def translate(tekst):
    pop = ""
    translacja = []
    licznik = 0
    for i in tekst:
        if i != pop:
            translacja.append([licznik, pop])
            licznik = 1
            pop = i
        else:
            licznik += 1
            pop = i
    translacja.append([licznik, pop])
    translacja.pop(0)
    return translacja


def detranslate(tekst):
    wynik = ""
    for i in tekst:
        for j in range(i[0]):
            wynik += i[1]
    print(wynik)


# print(translate(data))
detranslate(translate(data))
