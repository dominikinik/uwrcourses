
def B(i, j):
    return 'B_%d_%d' % (i, j)


def storms(rows, cols, triples):
    writeln(':- use_module(library(clpfd)).')
    
    R = len(rows)
    C = len(cols)
    
    bs = [B(i, j) for i in range(R) for j in range(C)]
    
    writeln('solve([' + ', '.join(bs) + ']) :- ')
    writeln('[' + ', '.join(bs) + '] ins 0..1,') #deklaracja zmiennych

    # sumowanie
    for c, val in enumerate(rows):
        rs = [B(c, j) for j in range(C)]
        writeln('sum([' + ', '.join(rs) + '], #=, ' + str(val) + '), ')

    
    for c, val in enumerate(cols):
        cs = [B(j, c) for j in range(R)]
        writeln('sum([' + ', '.join(cs) + '], #=, ' + str(val) + '), ')

    # kwadrat
    for i in range(R - 1):
        for j in range(C - 1):
            A = B(i, j)
            B1 = B(i, j+1)
            C1 = B(i + 1, j)
            D = B(i + 1, j + 1)
            writeln(A + ' + ' + D + ' #= 2 #<==> ' + B1 + ' + ' + C1 + ' #= 2, ')

    # B = 1 => A + C > 1  z wykladu dla kolumny i rzedow 
    for i in range(R):
        for j in range(C - 2):
            A = B(i, j)
            B1 = B(i, j + 1)
            C1 = B(i, j + 2)
            writeln(B1 + ' #= 1 #==> ' + A + ' + ' + C1 + ' #>= 1, ')

    for i in range(C):
        for j in range(R - 2):
            A = B(i, j)
            B1 = B(i, j + 1)
            C1 = B(i, j + 2)
            writeln(B1 + ' #= 1 #==> ' + A + ' + ' + C1 + ' #>= 1, ')
    # znane wartosci
    for triple in triples:
        output.write('%s #= %d, ' % (B(triple[0], triple[1]), triple[2]))

    writeln('')
    writeln('    labeling([ff], [' + ', '.join(bs) + ']).')
    writeln('')
    writeln(':- solve(X), write(X), nl.')
    


def writeln(s):
    output.write(s + '\n')

txt = open('zad_input.txt').readlines()
output = open('zad_output.txt', 'w')

rows = list(map(int, txt[0].split()))
cols = list(map(int, txt[1].split()))
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(list (map(int, txt[i].split())))


storms(rows, cols, triples)