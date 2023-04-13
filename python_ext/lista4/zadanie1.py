from random import randrange
import itertools


def remv_powtorki(wej):
    roz = []
    for i in wej:
        if i not in roz:
            roz.append(i)
    return roz


def rozwiazywanie(in1, in2, out):
    zbiorliterek = []
    zbiorliterek.append(in1+in2+out)
    zbiorliterek = remv_powtorki(zbiorliterek[0])
    pomin1 = in1
    pomin2 = in2
    pomout = out
    zbiorpierw = []
    zbiorpierw.append(in1[0])
    zbiorpierw.append(in2[0])
    zbiorpierw.append(out[0])
    st = []
    for i in zbiorliterek:
        pomin1 = pomin1.replace(i, str(1))
        pomin2 = pomin2.replace(i, str(1))
        pomout = pomout.replace(i, str(1))
        st.append(1)

    odpowiedz = dict(zip(zbiorliterek, st))
    odpowiedzi = []

    for i in itertools.product(list(range(10)), repeat=len(zbiorliterek)):
        pomin1 = in1
        pomin2 = in2
        pomout = out
        p = 0
        flag = 0

        for x in zbiorliterek:
            if x in zbiorpierw and i[p] == 0:
                flag = 1
            odpowiedz.update(zip(x, str(i[p])))
            pomin1 = pomin1.replace(x, str(i[p]))
            pomin2 = pomin2.replace(x, str(i[p]))
            pomout = pomout.replace(x, str(i[p]))
            p += 1
        if flag == 0:
            if int(pomin1) + int(pomin2) == int(pomout):
                yield odpowiedz


for i in rozwiazywanie("KIOTO", "OSAKA", "TOKIO"):
    print(i)
