import queue
import copy



def load():
    chests = set()
    goals = set()
    walls = set()
    file = open("zad_input.txt")
    lines = file.readlines()
    i = 0
    for y in lines:
        j = 0
        for x in y:
            if x == 'K':
                player_pos = (i, j)
            elif x == 'W':
                walls.add((i, j))
            elif x == 'B':
                chests.add((i, j))
            elif x == 'G':
                goals.add((i, j))
            elif x == '*':
                goals.add((i, j))
                chests.add((i, j))
            j += 1
        i += 1
    x = j
    y = i
    moves = ''
    return player_pos, chests, walls, goals, x, y, moves

def new_poss(state):
    odp = []
    for i in range(4):      
        player_pos = state[0]
        chests = copy.copy(state[1])
        walls = state[2]
        moves = state[6]
        moved = False
        new_pos = (player_pos[0]+X_mof[i], player_pos[1] + y_mof[i])
        new_chest_pos = (player_pos[0]+2*X_mof[i], player_pos[1] + 2 * y_mof[i])
        if new_pos not in walls:
            if new_pos in chests and new_chest_pos not in chests and new_chest_pos not in walls:
                chests.remove(new_pos)
                chests.add(new_chest_pos)
                player_pos = new_pos
                moved = True
            elif new_pos not in chests:
                player_pos = new_pos
                moved = True
        if moved:
            moves+=mofes[i]
            new_state = [player_pos, chests, walls, state[3], state[4], state[5], moves]
            if (player_pos, tuple(chests)) not in VISITED:
                VISITED.add((player_pos, tuple(chests)))
                odp.append(new_state)
    return odp


def finito(state):
    chests = state[1]
    goals = state[3]
    for c in chests:
        if c not in goals:
            return False
    return True
def save(moves):
    output = open("zad_output.txt", "w")
    output.write(moves)
    output.close()

def BFS(state):
    Q = queue.Queue()
    Q.put(state)
    VISITED.add((state[0], tuple(state[1])))
    while not Q.empty():
        new_states = new_poss(Q.get())
        for s in new_states:
            if finito(s):
                save(s[6])
                return s
            else:
                Q.put(s)

VISITED = set()
mofes = ['R', 'L', 'D', 'U']
X_mof =[0, 0, 1, -1]    
y_mof = [1, -1, 0, 0]   
obj = load()
BFS(obj)
