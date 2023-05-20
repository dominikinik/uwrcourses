import random
import sys
from collections import defaultdict as dd
import numpy as np
import math 

BOK = 50
SX = -100
SY = 0
M = 8
weights = [
    [20, -3, 11, 8, 8, 11, -3, 20],
    [-3, -7, -4, 1, 1, -4, -7, -3],
    [11, -4, 8, 2, 2, 8, -4, 11],
    [8, 1, 2, -3, -3, 2, 1, 8],
    [8, 1, 2, -3, -3, 2, 1, 8],
    [11, -4, 8, 2, 2, 8, -4, 11],
    [-3, -7, -4, 1, 1, -4, -7, -3],
    [20, -3, 11, 8, 8, 11, -3, 20]
]
def deepcopy(obj):
    res = Board()
    res.board = np.array(obj.board.copy())
    res.fields = obj.fields.copy()
    return res

def initial_board():
    B = [ [None] * M for i in range(M)]
    B[3][3] = 1
    B[4][4] = 1
    B[3][4] = 0
    B[4][3] = 0
    return B

    
class Board:
    dirs  = [ (0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1) ]
    
    
    def __init__(self):
        self.board = initial_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        for i in range(M):
            for j in range(M):
                if self.board[i][j] == None:   
                    self.fields.add( (j,i) )
                                                
    def draw(self):
        for i in range(M):
            res = []
            for j in range(M):
                b = self.board[i][j]
                if b == None:
                    res.append('.')
                elif b == 1:
                    res.append('#')
                else:
                    res.append('o')
            print (' '.join(res)) 
        print            
        
    
    
                                   
    def moves(self, player):
        res = []
        for (x,y) in self.fields:
            if any( self.can_beat(x,y, direction, player) for direction in Board.dirs):
                res.append( (x,y) )
        if not res:
            return [None]
        return res               
    
    def can_beat(self, x,y, d, player):
        dx,dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x,y) == 1-player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x,y) == player
    
    def get(self, x,y):
        if 0 <= x < M and 0 <=y < M:
            return self.board[y][x]
        return None
                        
    def do_move(self, move, player):
        self.history.append([x[:] for x in self.board])
        self.move_list.append(move)
        
        if move == None:
            return
        x,y = move
        x0,y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx,dy in self.dirs:
            x,y = x0,y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x,y) == 1-player:
              to_beat.append( (x,y) )
              x += dx
              y += dy
            if self.get(x,y) == player:              
                for (nx,ny) in to_beat:
                    self.board[ny][nx] = player
                                                     
    def result(self):
        res = 0
        for y in range(M):
            for x in range(M):
                b = self.board[y][x]                
                if b == 1:
                    res -= 1
                elif b == 0:
                    res += 1
        return res
                
    def terminal(self):
        if not self.fields:
            return True
        if len(self.move_list) < 2:
            return False
        return self.move_list[-1] == self.move_list[-2] == None 

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return [None]    
    

    def heuristic(self,ile):
            my_color = 0
            opp_color = 1
            my_tiles = 0
            opp_tiles = 0

            p = 0
            c = 0
            l = 0
            m = 0
            d = 0
            my_cord=[]
            opp_cord=[]
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] == 0:
                        d += weights[i][j]
                        my_cord.append((i,j))
                        my_tiles += 1
                    elif self.board[i][j] == 1:
                        d -= weights[i][j]
                        opp_cord.append((i,j))
                        opp_tiles += 1

                

         
            if my_tiles > opp_tiles:
                p = (100.0 * my_tiles) / (my_tiles + opp_tiles)
            elif my_tiles < opp_tiles:
                p = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
            else:
                p = 0

        
            my_tiles = opp_tiles = 0
            if self.board[0][0] == my_color:
                my_tiles += 1
            elif self.board[0][0] == opp_color:
                opp_tiles += 1
            if self.board[0][7] == my_color:
                my_tiles += 1
            elif self.board[0][7] == opp_color:
                opp_tiles += 1
            if self.board[7][0] == my_color:
                my_tiles += 1
            elif self.board[7][0] == opp_color:
                opp_tiles += 1
            if self.board[7][7] == my_color:
                my_tiles += 1
            elif self.board[7][7] == opp_color:
                opp_tiles += 1
            c = 25 * (my_tiles - opp_tiles)


            my_tiles = opp_tiles = 0
            if self.board[0][0] == None:
                if self.board[0][1] == my_color:
                    my_tiles += 3
                elif self.board[0][1] == opp_color:
                    opp_tiles += 3
                if self.board[1][1] == my_color:
                    my_tiles += 2
                elif self.board[1][1] == opp_color:
                    opp_tiles += 2
                if self.board[1][0] == my_color:
                    my_tiles += 1
                elif self.board[1][0] == opp_color:
                    opp_tiles += 1

            if self.board[0][7] == None:
                if self.board[0][6] == my_color:
                    my_tiles += 3
                elif self.board[0][6] == opp_color:
                    opp_tiles += 3
                if self.board[1][6] == my_color:
                    my_tiles += 2
                elif self.board[1][6] == opp_color:
                    opp_tiles += 2
                if self.board[1][7] == my_color:
                    my_tiles += 1
                elif self.board[1][7] == opp_color:
                    opp_tiles += 1

            if self.board[7][0] == None:
                if self.board[7][1] == my_color:
                    my_tiles += 3
                elif self.board[7][1] == opp_color:
                    opp_tiles += 3
                if self.board[6][1] == my_color:
                    my_tiles += 2
                elif self.board[6][1] == opp_color:
                    opp_tiles += 2
                if self.board[6][0] == my_color:
                    my_tiles += 1
                elif self.board[6][0] == opp_color:
                    opp_tiles += 1

            if self.board[7][7] == None:
                if self.board[6][7] == my_color:
                    my_tiles += 3
                elif self.board[6][7] == opp_color:
                    opp_tiles += 3
                if self.board[6][6] == my_color:
                    my_tiles += 2
                elif self.board[6][6] == opp_color:
                    opp_tiles += 2
                if self.board[7][6] == my_color:
                    my_tiles += 1
                elif self.board[7][6] == opp_color:
                    opp_tiles += 1

            l = -12.5 * (my_tiles - opp_tiles)


            my_tiles = len(self.moves(0))
            opp_tiles = len(self.moves(1))

            if my_tiles > opp_tiles:
                m = (100.0 * my_tiles) / (my_tiles + opp_tiles)
            elif my_tiles < opp_tiles:
                m = -(100.0 * opp_tiles) / (my_tiles + opp_tiles)
            else:
                m = 0
                
            
            ranking=0
            diags = [self.board[::-1,:].diagonal(i) for i in range(-3,4)]
            diags.extend(self.board.diagonal(i) for i in range(3,-4,-1))
            diags=[n.tolist() for n in diags]
            #print(diags)
            for i in range(4):
                z=0
                flag=False
                if flag==False:
                    for o in diags[i*4:(i+1)*4+1]:
                        #print(o)
                        z+=1
                        for a in o:
                            #print(i)
                            if a==my_color:
                                ranking+=3*z
                                
                            else:    
                                flag=True
                                break
            for i in range(4):
                z=0
                flag=False
                if flag==False:
                    for o in diags[i*4:(i+1)*4+1]:
                        #print(o)
                        z+=1
                        for a in o:
                            #print(i)
                            if a==opp_color:
                                ranking-=3*z
                                
                            else:    
                                flag=True
                                break
        
            #print(ranking)        
            if self.terminal():
                return 2*p*1000000
            return 2*ile*p + ((9000 * c) + (382.026 * l) +  (783.922 * m)  + (10 * d)+10*ranking)
    def trim(self, moves, flag, size,ile):
            best = []
            
            for i in moves:
                new_board = deepcopy(self)
                new_board.do_move(i, False)
                score = new_board.heuristic(ile)
                pair = (score, new_board, i)
                best.append(pair)
            if flag:
                best.sort(key=lambda x: x[0])
            else:
                best.sort(reverse=True, key=lambda x: x[0])
            return best

    def find_best(self, depth, player,ile,size):
            
        def alphabeta(state, depth, alpha, beta, maximizing_player, size,ile):
            # print("cos2")
            
            value=-math.inf
            if depth == 0 or state.terminal() or state.moves(False) == [None]:
                return state.heuristic(ile)

            if   maximizing_player:
                children = state.moves(True)
                new_board = deepcopy(state)
                new_board.do_move(move,  True)
                value = alphabeta(
                        new_board, depth - 1, alpha, beta, False, size,ile+1)
                for move in children[1:]:
                    new_board = deepcopy(state)
                    new_board.do_move(move,  True)
                    value = sum(value+alphabeta(
                        new_board, depth - 1, alpha, beta, False, size,ile+1))/2
                    
                return value
            else:
                value=math.inf
                children = state.moves( True)
                value = 1e12
                for move in children:
                    new_board = deepcopy(state)
                    new_board.do_move(move,  True)
                    value = min(value, alphabeta(
                        new_board, depth - 1, alpha, beta, False, size,ile+1))
                    
                return value
        #jestem 000000
        best_move = None
        best_score = -math.inf
        alpha = -math.inf
        beta = math.inf
        mozliwe=self.trim(self.moves(0), player, size,ile)
      
        
        for board in mozliwe:
            #print(player)   
            if ile<60:
                val = alphabeta(board[1], depth, alpha, beta, True, size,ile+1)            
            else:
                val = alphabeta(board[1], depth, alpha, beta, False, size,ile+1)
            if val > best_score:
                best_move = board[2]
                best_score = val
            
            
        return best_move
player = 0
B = Board()
i=0
nr=1000
sum=0
for z in range(1,nr):
    B = Board()
    i=0
    player = 0
    Flag=True
    while True and Flag:
        if B.terminal():
            break
        if not player:
            #B.draw()
            if B.moves(True)==0:
                break
            m = B.random_move(True)
            
            B.do_move(m, True)
        else:
            if B.moves(False)==0:
                break
            best=B.find_best(0,False,i,3)

            B.do_move(best, False)
        player = 1-player
        
        
        i+=1
    
    if B.result()>=0:
        sum+=1
    print ('Result',z,sum,z-sum, B.result(),i)
print ('Result finale', sum, 100*sum/nr)

  
                
