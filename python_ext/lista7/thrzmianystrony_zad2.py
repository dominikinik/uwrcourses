import time
import urllib.request
import threading as thr


def difference(a, b):
    a = a.split()
    b = b.split()
    print(b)
    try:
        A = set(a)
        B = set(b)

        str_diff = A.symmetric_difference(B)
        notemp = (len(str_diff) > 0)
        if notemp:
            print(str_diff)
    except:
        print("nieznany znak ")


def detect(url, czas):
    with urllib.request.urlopen(url) as f:
        pop = f.read().decode('utf-8')
    while True:
     # print(url,'dziala')
        with urllib.request.urlopen(url) as f:
            tekst = f.read().decode('utf-8')
        if pop != tekst:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(url)
            print()
            difference(pop, tekst)
            pop = tekst
            continue
        time.sleep(czas)


def treets(url, czas):
    t = thr.Thread(target=detect, args=[url, czas])
    t.start()


treets('https://www.supremenewyork.com/shop/all', 60)
treets('https://www.tvpolsat.info/', 60)
