import itertools
import collections


def conv(moves):  # tlumaczenie seri 0123 na oczekiwane literki
    res = ""
    for m in moves:
        if m == 0:
            res += "R"
        elif m == 1:
            res += "L"
        elif m == 2:
            res += "D"
        else:
            res += "U"
    return res


def load():  # ladowanie  wejsciu segregacja punktow
    global rows, cols, poss_pos, goals, walls, input
    input = open("zad_input.txt", "r").read().split("\n")
    rows, cols = len(input), len(input[0])

    for i in range(rows-1):
        for j in range(cols):
            if input[i][j] == '#':
                walls.add((j, i))
            elif input[i][j] == 'G':
                goals.add((j, i))
            elif input[i][j] == 'S':
                poss_pos.add((j, i))
            elif input[i][j] == 'B':
                poss_pos.add((j, i))
                goals.add((j, i))


def save(moves):
    print(len(moves))
    print(conv(moves))
    output = open("zad_output.txt", "w")
    output.write(conv(moves))
    output.close()


def new_poss(poss_pos, dir):  # sprawdzanie mozliwych ruchow czy legalne itd
    new_pos = set()

    for pos in poss_pos:
        new_x = pos[0] + x[dir]
        new_y = pos[1] + y[dir]

        if (new_x, new_y) not in walls:
            new_pos.add((new_x, new_y))
        else:
            new_pos.add((pos[0], pos[1]))
    return new_pos


def finito(poss):  # sprawdzamy czy obok nie ma naszego miejsca docelowego
    for pos in poss:
        if pos not in goals:
            return False

    return True


def bfs(poss, moves):
    visi = set()
    queue = collections.deque()
    queue.append((poss, moves))
    visi.add(str(poss))
    min_leng_pos = len(poss)

    while True:
        act = queue.popleft()
        poss, moves = act[0], act[1]

        if finito(poss):  # jesli skonczymy to wypisujemy
            save(moves)
            break

        for i in range(4):  # generujemy mozliwe ruhcy ktore zmniejszaja niepewnosc
            new_pos = new_poss(poss, i)
            if str(new_pos) not in visi:
                if len(new_pos) < min_leng_pos:
                    visi = set()
                    queue.clear()
                    min_leng_pos = len(new_pos)
                visi.add(str(new_pos))
                queue.append((new_pos, moves + [i]))


x, y = [1, -1, 0, 0], [0, 0, 1, -1]  # mozliwe kombiancje ruchow

poss_pos, goals, walls = set(), set(), set()
load()

mofes = ['0', '1', '2', '3']
all = list(itertools.permutations(mofes))
min = 123123
naj_mov_seq, naj_pos, moves = [], [], []


for i in range(len(all)):  # robie losowe ruchy jestem arcymistrzem
    seq = all[i]
    act_pos = poss_pos.copy()
    act_seq, mov = [], []
    for s in seq:
        act_seq += s*len(input)  # pytanie do tej wartosci
    for m in act_seq:
        act_pos = new_poss(act_pos, int(m))
        mov.append(int(m))

    if len(act_pos) < min:
        min = len(act_pos)
        naj_mov_seq = mov
        naj_pos = act_pos

bfs(naj_pos, naj_mov_seq)
