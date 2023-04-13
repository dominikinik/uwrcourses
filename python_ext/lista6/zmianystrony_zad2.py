import time
import urllib.request


def difference(a, b):
    a = a.split()
    b = b.split()
    try:
        A = set(a)
        B = set(b)

        str_diff = A.symmetric_difference(B)
        notemp = (len(str_diff) > 0)
        if notemp:
            print(str_diff)
    except:
        print("nieznany znak ")


urls = ['https://www.tvpolsat.info/',
        'https://www.supremenewyork.com/shop/all']
pop = []
for i in urls:
    with urllib.request.urlopen(i) as f:
        pom = f.read().decode('utf-8')
        pop.append(pom)
while True:
    for i in range(len(urls)):
        with urllib.request.urlopen(urls[i]) as f:
            tekst = f.read().decode('utf-8')
        if pop[i] != tekst:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(urls[i])
            print()
            difference(pop[i], tekst)
            pop[i] = tekst
            continue
    time.sleep(10)
