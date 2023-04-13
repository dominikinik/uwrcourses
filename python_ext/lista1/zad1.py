from decimal import *
zakupy = [0.2, 0.5, 4.59, 6]


def vat_faktura(lista):
    return sum(lista) * .23


def vat_paragon(lista):
    return sum([l * .23 for l in lista])


getcontext().prec = 11


def vat_faktura2(lista):
    return Decimal(sum(lista)) * Decimal(.23)


def vat_paragon2(lista):
    return sum([Decimal(l) * Decimal(.23) for l in lista])


print(vat_faktura(zakupy))
print(vat_paragon(zakupy))
print(vat_faktura(zakupy) == vat_paragon(zakupy))
print(vat_faktura2(zakupy))
print(vat_paragon2(zakupy))
print(vat_faktura2(zakupy) == vat_paragon2(zakupy))
