from collections import deque
from numpy import zeros


def save(odp):
    file = open("zad_output.txt", "w")
    for row in odp:
        print(*['#' if x else ' ' for x in row])
        for i in row:
            if i:
                file.write("#")
            else:
                file.write(".")

        file.write("\n")


def poss(n, pattern):

    if n == 0:
        return [[]]
    if len(pattern) == 0:
        return [[0] * n]

    block_len = pattern[0]
    block = [1 for _ in range(block_len)]
    new_n = n - block_len

    if len(pattern[1:]) > 0:
        block += [0]
        new_n -= 1

    akt_poss = [
        block + new_pattern for new_pattern in poss(new_n, pattern[1:])]
    required_len = sum(pattern) + len(pattern) - 1

    if required_len < n:
        return akt_poss + [
            [0] + new_pattern for new_pattern in poss(n - 1, pattern)
        ]
    else:
        return akt_poss


def szuk(rows, columns, nrrows, nrcols):
    height, width = len(rows), len(columns)
    possible_rows = [poss(nrcols, row) for row in rows]
    possible_columns = [poss(nrrows, column) for column in columns]

    odp = zeros((height, width))
    not_fixed = deque()

    def fix_col(y, x):
        possible_columns[x] = [
            column for column in possible_columns[x] if column[y] == odp[y][x]]

    def fix_rows(y, x):
        possible_rows[y] = [
            row for row in possible_rows[y] if row[x] == odp[y][x]]

    def napraw(y, x, current_rows):
        row_point = current_rows[0][x]

        if all(row[x] == row_point for row in current_rows):
            odp[y][x] = row_point
            fix_col(y, x)

        else:

            column_point = possible_columns[x][0][y]

            if all(column[y] == column_point for column in possible_columns[x]):
                odp[y][x] = column_point
                fix_rows(y, x)
            else:

                not_fixed.append((y, x))

    for y in range(height):
        current_rows = possible_rows[y]

        for x in range(width):
            napraw(y, x, current_rows)

    while len(not_fixed) > 0:
        y, x = not_fixed.popleft()
        current_rows = possible_rows[y]
        napraw(y, x, current_rows)

    return odp


def load():
    with open("zad_input.txt") as f:
        pom, rows, cols = [], [], []
        for line in f:
            pom.append(line.split())

        nrrows, nrcols = int(pom[0][0]), int(pom[0][1])

        for i in range(1, nrrows + 1):
            rows.append(list(map(int, pom[i])))

        for i in range(nrrows + 1, len(pom)):
            cols.append(list(map(int, pom[i])))

    return (rows, cols, nrrows, nrcols)


def solve():
    rows, cols, nrrows, nrcols = load()
    odp = szuk(rows, cols, nrrows, nrcols)
    save(odp)


solve()
