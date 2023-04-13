import csv
import numpy
def solution():
    
    tsv_file = open("wyniki.tsv", encoding='utf-8')
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    partie = {"PiS": 0, "KO": 0, "SLD": 0, "PSL": 0, "KWin": 0, "MN": 0}
    partie_tab = {"PiS", "KO", "SLD", "KWin", "MN"}
    first_row = True
    
    for row in read_tsv:
        if first_row:
            first_row = False
        else:
            ilorazy = numpy.zeros((int(row[2]), 6))
            m = int(row[2])
            k = -1
            while m > 0:
                k += 1
                for i in range(6):
                    ilorazy[k][i] = float(
                        row[i+3].replace(",", ".").replace("–", "0"))/(k+1)
                maks = numpy.amax(ilorazy)
                for j in range(k+1):
                    for i in range(6):
                        if ilorazy[j][i] == maks:
                            ilorazy[j][i] = 0
                            partie[partie_tab[i]] += 1
                            m -= 1
    print(partie)
    tsv_file.close()

solution()
