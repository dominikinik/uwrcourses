def opt_dist(l, d):
    if len(l) < d:
        return "xD"
    pom = [1] * d + [0] * (len(l) - d)
    min = len(l)

    for _ in range(len(l) - d + 1):
        count = 0
        for j in range(len(l)):
            if l[j] != pom[j]:
                count += 1
        if count < min:
            min = count

        pom = [0] + pom[:len(pom)-1]

    return min


print(opt_dist([0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 5))
print(opt_dist([0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 4))
print(opt_dist([0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 3))
print(opt_dist([0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 2))
print(opt_dist([0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 1))
print(opt_dist([0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 0))
