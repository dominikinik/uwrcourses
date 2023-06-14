
'''
Losowy agent do Dżungli
'''


import random
import sys
import copy
'''
0123456
..#*#..0
...#...1
.......2
.~~.~~.3
.~~.~~.4
.~~.~~.5
.......6
...#...7  y
..#*#..8  ^
<-x       |
'''         
class Jungle:
    MAXIMAL_PASSIVE = 30
    DENS_DIST = 0.1
    MX = 7
    MY = 9
    traps = {(2, 0), (4, 0), (3, 1), (2, 8), (4, 8), (3, 7)}
    ponds = {(x, y) for x in [1, 2, 4, 5] for y in [3, 4, 5]}
    dens = [(3, 8), (3, 0)]
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    rat, cat, dog, wolf, jaguar, tiger, lion, elephant = range(8)

    def __init__(self):
        self.board = self.initial_board() # None lub (player, nmb) player: 0/1   nmb: liczba odpowiadajaca rankingowi
        self.pieces = {0: {}, 1: {}}#pieces przechowuje pozycje pionkow PIECES[1] DUZE ,   pieces[0] male

        #pieces [1] jest slownikiem
        for y in range(Jungle.MY):
            for x in range(Jungle.MX): #{0: {}, 1: {6: (...)}},  pieces[1]={6: (0, 0), 5: (6, 0)}
                C = self.board[y][x]
                if C:
                    pl, pc = C
                    self.pieces[pl][pc] = (x, y)
        self.curplayer = 0
        self.peace_counter = 0
        self.winner = None
        

    def initial_board(self):
        pieces = """
        L.....T
        .D...C.
        R.J.W.E
        .......
        .......
        .......
        e.w.j.r
        .c...d.
        t.....l
        """

        B = [x.strip() for x in pieces.split() if len(x) > 0]
        T = dict(zip('rcdwjtle', range(8))) #{'r': 0, 'c': 1, 'd': 2, 'w': 3, 'j': 4, 't': 5, 'l': 6, 'e': 7}

        res = []
        for y in range(9):
            raw = 7 * [None]
            for x in range(7):
                c = B[y][x]
                if c != '.':
                    if 'A' <= c <= 'Z':
                        player = 1
                    else:
                        player = 0
                    raw[x] = (player, T[c.lower()])
            res.append(raw)
        return res # zwraca tablice z informacjami jaki gracz i jaka ranga

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return None

    def can_beat(self, p1, p2, pos1, pos2):
        if pos1 in Jungle.ponds and pos2 in Jungle.ponds:
            return True  # rat vs rat
        if pos1 in Jungle.ponds:
            return False  # rat in pond cannot beat any piece on land
        if p1 == Jungle.rat and p2 == Jungle.elephant:
            return True
        if p1 == Jungle.elephant and p2 == Jungle.rat:
            return False
        if p1 >= p2:
            return True
        if pos2 in Jungle.traps:
            return True
        return False

    def pieces_comparison(self):
        for i in range(7,-1,-1):
            ps = []
            for p in [0,1]:
                if i in self.pieces[p]:
                    ps.append(p)
            if len(ps) == 1:
                return ps[0]
        return None
                
    def rat_is_blocking(self, player_unused, pos, dx, dy):        
        x, y = pos
        nx = x + dx
        for player in [0,1]:
            if Jungle.rat not in self.pieces[1-player]:
                continue
            rx, ry = self.pieces[1-player][Jungle.rat]
            if (rx, ry) not in self.ponds:
                continue
            if dy != 0:
                if x == rx:
                    return True
            if dx != 0:
                if y == ry and abs(x-rx) <= 2 and abs(nx-rx) <= 2:
                    return True
        return False

    def draw(self):
        TT = {0: 'rcdwjtle', 1: 'RCDWJTLE'}
        for y in range(Jungle.MY):
            L = []
            for x in range(Jungle.MX):
                b = self.board[y][x]
                if b:
                    pl, pc = b
                    L.append(TT[pl][pc])
                else:
                    L.append('.')
            print(''.join(L))
        print('')

    
    def victory(self, player):
        oponent = 1-player        
        if len(self.pieces[oponent]) == 0: #opponent nie ma juz pionkow
            self.winner = player
            return True

        x, y = self.dens[oponent]
        if self.board[y][x]:
            self.winner = player
            return True
        return False

    def do_move(self, m):
        self.curplayer = 1 - self.curplayer
        if m is None:
            return
        pos1, pos2 = m
        x, y = pos1
        pl, pc = self.board[y][x]

        x2, y2 = pos2
        if self.board[y2][x2]:  # piece taken!
            pl2, pc2 = self.board[y2][x2]
            del self.pieces[pl2][pc2]
            self.peace_counter = 0
        else:
            self.peace_counter += 1    

        self.pieces[pl][pc] = (x2, y2)
        self.board[y2][x2] = (pl, pc)
        self.board[y][x] = None

    ##ruch jest postaci((2,2), (2,1)) gdzie pierwsza para oznacza KOLUMNE, WIERSZ obecnie a druga po ruchu
    def moves(self, player):
        res = []
        for p, pos in self.pieces[player].items():
            x, y = pos
            for (dx, dy) in Jungle.dirs:
                pos2 = (nx, ny) = (x+dx, y+dy)
                if 0 <= nx < Jungle.MX and 0 <= ny < Jungle.MY:
                    if Jungle.dens[player] == pos2:
                        continue
                    if pos2 in self.ponds:
                        if p not in (Jungle.rat, Jungle.tiger, Jungle.lion):
                            continue
                        #if self.board[ny][nx] is not None:
                        #    continue  # WHY??
                        if p == Jungle.tiger or p == Jungle.lion:
                            if dx != 0:
                                dx *= 3
                            if dy != 0:
                                dy *= 4
                            if self.rat_is_blocking(player, pos, dx, dy):
                                continue
                            pos2 = (nx, ny) = (x+dx, y+dy)
                    if self.board[ny][nx] is not None:
                        pl2, piece2 = self.board[ny][nx]
                        if pl2 == player:
                            continue
                        if not self.can_beat(p, piece2, pos, pos2):
                            continue
                    res.append((pos, pos2))
        return res 
    def check_finish(self): #-1: kontynuuj 0:wygrywa 0, 1:wygrywa1, 2:remis
        if self.victory(1):
            if self.victory(0):
                return 2  # Remis
            else:
                return 1  # Wygrana

        elif self.victory(0):
            return 0
        return -1

    def choose_move_random(self,moves,player):
        return random.choice(moves)
    #
    def calculate_strength(self,pieces,player):
         # Liczenie wartości pionków przeciwnika
        score=0
        for p, pos in pieces.items():
            x, y = pos
            skalar = 1
            if pos in Jungle.ponds:
                skalar *= 2 #premiujemy jestli jest w stawie
            elif pos in Jungle.traps: 
                skalar=-1
            score += p*skalar
        return score

    def calculate_distnce(self,pieces,player):
        opponent_den = self.dens[1-player]
        (x_den,y_den) = opponent_den
        score=0
        for p, pos in pieces.items():
            x, y = pos
            score += abs(x_den-x) +abs(y_den-y) 
        return score

    def evaluate(self, player):
        if self.victory(player):
            if self.victory(1 - player):
                return 0  # Remis
            else:
                return 99999#36 * 2  # Wygrana

        elif self.victory(1 - player):
            return -99999

        player_score = 0
        opponent_score = 0
        # Liczenie wartości pionków 
        player_score+= self.calculate_strength(self.pieces[player],player)
        opponent_score+=self.calculate_strength(self.pieces[1-player],1-player)
        # Liczenie odleglosci manhatanskiej. Im wiecej my mamy tym gorzej, im wiecej przeciwnik ma tym lepiej
        player_score-=self.calculate_distnce(self.pieces[player],player) +self.calculate_distnce(self.pieces[1-player],1-player)
        return player_score - opponent_score


    def choose_move_alfa_beta(self, moves, player):
        best_move = None
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')

        for move in moves:
            pieces_copy = copy.deepcopy(self.pieces)
            board_copy = copy.deepcopy(self.board)  
            curr_player_copy=  self.curplayer
            peace_counter_copy=self.peace_counter

            self.do_move(move)
            value = self.minimax_alpha_beta(player, alpha, beta, False,2)

            #undo_move:
            self.pieces=copy.deepcopy(pieces_copy)
            self.board=copy.deepcopy(board_copy)
            self.curplayer=curr_player_copy
            self.peace_counter=peace_counter_copy
            
            if value > best_value:
                best_value = value
                best_move = move

            alpha = max(alpha, best_value)

        return best_move

    def minimax_alpha_beta(self, player, alpha, beta, maximizing_player,depth):
        if depth==0 or self.victory(player) or self.victory(1-player):
            return self.evaluate(player)
        if maximizing_player:
            value = float('-inf')
            for move in self.moves(player):
                pieces_copy = copy.deepcopy(self.pieces)
                board_copy = copy.deepcopy(self.board)  
                curr_player_copy=  self.curplayer
                peace_counter_copy=self.peace_counter
                
                
                self.do_move(move)
                value = max(value, self.minimax_alpha_beta(player, alpha, beta, False,depth-1))
                
                self.pieces=copy.deepcopy(pieces_copy)
                self.board=copy.deepcopy(board_copy)
                self.curplayer=curr_player_copy
                self.peace_counter=peace_counter_copy                
                
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for move in self.moves(1 - player):

                pieces_copy = copy.deepcopy(self.pieces)
                board_copy = copy.deepcopy(self.board)  
                curr_player_copy=  self.curplayer
                peace_counter_copy=self.peace_counter

                self.do_move(move)
                value = min(value, self.minimax_alpha_beta(player, alpha, beta, True,depth-1))
                
                self.pieces=copy.deepcopy(pieces_copy)
                self.board=copy.deepcopy(board_copy)
                self.curplayer=curr_player_copy
                self.peace_counter=peace_counter_copy  

                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    #
    def choose_move_simulation(self,moves,player,N=20000):
        pieces_copy = copy.deepcopy(self.pieces)
        board_copy = copy.deepcopy(self.board)  
        curr_player_copy=  self.curplayer
        peace_counter_copy=self.peace_counter
        
        set_cnt = {move: 0 for move in moves}
        total_moves = 0 
        #w poleceniu jest powiedziane ze ooglnie to to na ktorym ruchu ile symulacji przeprowadzimy nie musi byc rownomierne, 
        #czyli ze jak na jakims ruchu wygralismy juz 2 razy to ma on wieksze prawdopodobienstow by byc wybranym ponownie do przeprowadzenia
        # symulacji niz ruch na ktorym nie wygralismy ani razu, ale bez tej losowosci tez jakos tam dziala
        while total_moves<N:
            for move in moves: 
                self.pieces=copy.deepcopy(pieces_copy)
                self.board=copy.deepcopy(board_copy)
                self.curplayer=curr_player_copy
                self.peace_counter=peace_counter_copy
                self.do_move(move)
                (won, moves_cnt) = finish_game(self,player)
                total_moves +=moves_cnt
                if won==player:
                    set_cnt[move] +=1
                elif won == 2: #remis
                    set_cnt[move]+=0.5
      #      print(set_cnt)
        max_value = max(set_cnt.values())

        #tworzenie listy kluczy które mają największą wartość
        max_value_keys = [key for key, value in set_cnt.items() if value == max_value]
        self.pieces=pieces_copy
        self.board=board_copy
        self.curplayer=curr_player_copy
        self.peace_counter=peace_counter_copy
        # wybieranie losowego elementu z listy kluczy które mają największą wartość
        return random.choice(max_value_keys)


def finish_game(game,player): #zwraca pare (0|1|2,moves) mowiaca ktory wygral i ile ruchow               
                              # 2 oznacza ze mamy remis:)
    player_turn = player # mowi ktory gracz wykonuje teraz ruch 
    temp = game.check_finish()
    if temp!=-1:
        return (temp,0)
    moves_cnt = 0
    while game.check_finish()==-1:       
        moves = game.moves(player_turn)
        if moves:
            move = random.choice(moves)
            game.do_move(move)
            moves_cnt+=1
        else:
            if game.moves(1-player_turn) != []: #or game.victory(1-player_turn)
                return (1-player_turn,moves_cnt)
            else:
                return (2,moves_cnt) #remis
        player_turn=1-player_turn
    return (game.check_finish(),moves_cnt)




def own_simulator(game,player): #zwraca pare (0|1|2,moves) mowiaca ktory wygral i ile ruchow               
                              # 2 oznacza ze mamy remis
    player_turn = player # mowi ktory gracz wykonuje teraz ruch 
    temp = game.check_finish()
    if temp!=-1:
        return (temp,0)
    moves_cnt = 0
    while game.check_finish()==-1: 
        moves = game.moves(player_turn)
        if moves:
            if player_turn==0:
                #move = game.random_move(0)
                move = game.choose_move_alfa_beta(moves,0)
            else:
                move = game.choose_move_simulation(moves,1,20000) 
            game.do_move(move)
            moves_cnt+=1
        else:
            if game.moves(1-player_turn) != []: #or game.victory(1-player_turn)
                return (1-player_turn,moves_cnt)
            else:
                return (2,moves_cnt) #remis
        player_turn=1-player_turn

    res = game.check_finish()
    return res



won_1=won_0=draw_cnt=0
for i in range (30):
    game = Jungle()
    player = 0
    won = own_simulator(game,player)
    if won==1:
        won_1+=1
        print("Player 1 won ")
    elif won==0:
        won_0+=1
        print("Player 0 won ")
    else:
        print("draw")
        draw_cnt+=1
print("won 0: "+str(won_0)+ ", won 1: " + str(won_1) +", draw: "+str(draw_cnt))


"""


"""