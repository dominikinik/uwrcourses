import queue
import heapq

VISITED = set()


def load():
    goals = set()
    walls = set()
    player_pos = []
    file = open("zad_input.txt ")
    lines = file.readlines()
    i = 0
    for y in lines:
        j = 0
        for x in y:
            if x == 'S':
                player_pos.append((i, j))
            elif x == '#':
                walls.add((i, j))
            elif x == 'G':
                goals.add((i, j))
            elif x == 'B':
                goals.add((i, j))
                player_pos.append((i, j))
            j += 1
        i += 1
    x, y = j, i
    moves = ''
    return player_pos, goals, walls, x-1, y, moves


def finito(state):
    player_pos = state[0]
    goals = state[1]
    for pos in player_pos:
        if pos not in goals:
            return False
    return True


def merge(state):
    player_pos = state[0]
    sorted_pos = sorted(player_pos) 
    for i in range(len(sorted_pos) - 1):
        if sorted_pos[i] == sorted_pos[i + 1]:
            player_pos.remove(sorted_pos[i]) 
            

def new_poss(state):
    walls = state[2]
    odp = []
    for i in range(4):  
        player_pos = []
        moves = state[5]
        for k in state[0]:
            new_pos = (k[0]+x_mof[i], k[1] + y_mof[i])
        
            if new_pos not in walls:
                player_pos.append(new_pos)
            else:
                player_pos.append(k)
        moves+=mofes[i]

        player_pos = sorted(player_pos)
        new_state = [player_pos, state[1], state[2], state[3], state[4], moves]
        if tuple(player_pos) not in VISITED:
            VISITED.add(tuple(player_pos))
            odp.append(new_state)

    return odp


def pom_bfs(state, s_pos):
    goals = state[1]
    walls = state[2]
    Q = queue.Queue()
    Q.put((s_pos, 0))
    visited = [s_pos]
    DISTANCES[s_pos] = 123123

    while not Q.empty():
        current = Q.get()
        pos = current[0]
        dist = current[1]
        if pos in goals:
            DISTANCES[s_pos] = min(DISTANCES[s_pos], dist)

        for i in range(4): 
            new_pos = (pos[0]+x_mof[i], pos[1] + y_mof[i])
        
            if new_pos not in visited and new_pos not in walls:
                visited.append(new_pos)
                Q.put((new_pos, dist + 1))


def dist(state):
    x = state[3]
    y = state[4]
    walls = state[2]
    for i in range(y):
        for j in range(x):
            if (i, j) not in walls:
                pom_bfs(state, (i, j))


def heur(state):
    dist = [DISTANCES[pos] for pos in state[0]]
    return len(state[5]) + max(dist) 

def save(moves):
    output = open("zad_output.txt", "w")
    output.write(moves)
    output.close()
    
def STAR(state):
    Q = []  
    heapq.heappush(Q, (heur(state), state))
    VISITED.add(tuple(state[0]))

    while len(Q) > 0:
        st_from_Q = heapq.heappop(Q)[1]
        merge(st_from_Q)
       
        new_states = new_poss(st_from_Q)
        for s in new_states:
            if finito(s):
                save(s[5])
                return s
            else:
                heapq.heappush(Q, (heur(s), s))



DISTANCES = {}
mofes = ['R', 'L', 'D', 'U']
x_mof =[0, 0, 1, -1]    
y_mof = [1, -1, 0, 0]   
s = load()
dist(s)
STAR(s)

