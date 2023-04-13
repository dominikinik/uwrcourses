def tabliczka(x1, x2, y1, y2):
    
    kolumny = [i for i in range(x1, x2+1)]
    rzedy = [i for i in range(y1, y2+1)]
    maks = max(len(str(x1*y1)), len(str((x2+1)*(y2+1))))
    
    print(" ".rjust(maks), end=" ".rjust(maks))
    
    for k in kolumny:
        print(str(k).rjust(maks), end=" ")
        
    print()
    for r in rzedy:
        il = [str(r * k).rjust(maks) for k in kolumny]
        il = map(str, il)
        out = str(r).rjust(maks) + " ".rjust(maks) + " ".join(il)
        print(out)


tabliczka(1, 5, -1, 4)
tabliczka(3, 5, 2, 4)
