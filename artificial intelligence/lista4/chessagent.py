import chess
import random
import math
from copy import deepcopy
import chess.pgn
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
    
}


king_mid = [0, 0,  0,  0,   0,  0,  0, 0,
            0, 0,  0,  0,   0,  0,  0, 0,
            0, 0,  0,  0,   0,  0,  0, 0,
            0, 0,  0,  0,   0,  0,  0, 0,
            0, 0,  0,  0,   0,  0,  0, 0,
            0, 0,  0,  0,   0,  0,  0, 0,
            0, 0,  0, -5,  -5, -5,  0, 0,
            0, 0, 10, -5,  -5, -5, 10, 0]

queen_mid = [-20, -10, -10, -5, -5, -10, -10, -20,
             -10,   0,   0,  0,  0,   0,   0, -10,
             -10,   0,   5,  5,  5,   5,   0, -10,
              -5,   0,   5,  5,  5,    5,   0,  -5,
              -5,   0,   5,  5,  5,   5,   0,  -5,
             -10,   5,   5,  5,  5,   5,   0, -10,
             -10,   0,   5,  0,  0,   0,   0, -10,
             -20, -10, -10,  0,  0, -10, -10, -20]

rook_mid = [10,  10,  10,  10,  10,  10,  10,  10,
            10,  10,  10,  10,  10,  10,  10,  10,
             0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,   0,   0,   0,   0,   0,
             0,   0,   0,  10,  10,   0,   0,   0,
             0,   0,   0,  10,  10,   5,   0,   0]

bishop_mid = [0,   0,   0,   0,   0,   0,   0,   0,
              0,   0,   0,   0,   0,   0,   0,   0,
              0,   0,   0,   0,   0,   0,   0,   0,
              0,  10,   0,   0,   0,   0,  10,   0,
              5,   0,  10,   0,   0,  10,   0,   5,
              0,  10,   0,  10,  10,   0,  10,   0,
              0,  10,   0,  10,  10,   0,  10,   0,
              0,   0, -10,   0,   0, -10,   0,   0]

knight_mid = [-5,  -5, -5, -5, -5, -5,  -5, -5,
              -5,   0,  0, 10, 10,  0,   0, -5,
              -5,   5, 10, 10, 10, 10,   5, -5,
              -5,   5, 10, 15, 15, 10,   5, -5,
              -5,   5, 10, 15, 15, 10,   5, -5,
              -5,   5, 10, 10, 10, 10,   5, -5,
              -5,   0,  0,  5,  5,  0,   0, -5,
              -5, -10, -5, -5, -5, -5, -10, -5]

pawn_mid = [ 0,   0,   0,   0,   0,   0,   0,   0,
            30,  30,  30,  40,  40,  30,  30,  30,
            20,  20,  20,  30,  30,  30,  20,  20,
            10,  10,  15,  25,  25,  15,  10,  10,
             5,   5,   5,  20,  20,   5,   5,   5,
             5,   0,   0,   5,   5,   0,   0,   5,
             5,   5,   5, -10, -10,   5,   5,   5,
             0,   0,   0,   0,   0,   0,   0,   0]

evaluation = {
    'p': pawn_mid,
    'r': rook_mid,
    'b': bishop_mid,
    'n': knight_mid,
    'k': king_mid,
    'q': queen_mid
}

def heuristic(board,ile):
    score = 0
    if board.result()=='1-0':
        return math.inf
    # Ocena wartości figur na planszy
    numfigb=0
    numfigw=0
    for piece_type, value in piece_values.items():
        score += value * len(board.pieces(piece_type, chess.WHITE))
        score -= value * len(board.pieces(piece_type, chess.BLACK))
        numfigb+=len(board.pieces(piece_type, chess.BLACK))
        numfigw+=len(board.pieces(piece_type, chess.WHITE))
    # Ocena pozycji na planszy
    score2=0
    for square, piece in board.piece_map().items():
        piece_type = piece.symbol().lower()
        if piece.color == chess.WHITE:
            score2 += evaluation[piece_type][square]
        else:
            score2 -= evaluation[piece_type][square]

    distance=0
    sum_distance=0
    if numfigb<=3 and numfigw>=5:
        
        black_king=board.pieces(chess.KING,chess.BLACK)
        black_king=black_king.pop()
      

        white_pieces = board.pieces(chess.PAWN, chess.WHITE) | board.pieces(chess.KNIGHT, chess.WHITE) | \
                   board.pieces(chess.BISHOP, chess.WHITE) | board.pieces(chess.ROOK, chess.WHITE) | \
                   board.pieces(chess.QUEEN, chess.WHITE) | board.pieces(chess.KING, chess.WHITE)
        for i in white_pieces:
           
        # Obliczenie odległości od każdej figury do króla przeciwnika
            sum_distance=chess.square_distance(i,black_king)
    return score+score2/(ile/8)-sum_distance*20+board.is_check()*1000
def trim(self, moves, flag,ile):
        best = []
        
        for i in moves:
            new_board = deepcopy(self)
            new_board.push(i)
            score = heuristic(new_board,ile)
            pair = (score, new_board, i)
            best.append(pair)
        
        if flag:
            best.sort(key=lambda x: x[0])
        else:
            best.sort(reverse=True, key=lambda x: x[0])
        return best
def find_best(self,depth,player,ile):
       
        def alphabeta(state, depth, alpha, beta,player, maximizing_player,ile):
            # print("cos2")
          
            #print(solution)
        
            value=-math.inf
 
            if  depth == 0 or state.is_game_over() :
                #print(state.heuristic(ile),depth)
                
                return heuristic(state,ile)

            if player==maximizing_player:
                children = state.legal_moves
                value=-math.inf
            
                for move in children:
                    new_board = deepcopy(state)
                    new_board.push(move)
                    value = max(value, alphabeta(
                        new_board, depth - 1, alpha, beta,1-player,maximizing_player,ile+1))
                    alpha = max(alpha, value)
                    
                    if  alpha>=beta:
                        #print("cut")
                        break
                return value
            else:
                value=math.inf
                children = state.legal_moves
                
                for move in children:
                    new_board = deepcopy(state)
                    new_board.push(move)
                    value = min(value,  alphabeta(
                        new_board, depth - 1, alpha, beta,1-player,maximizing_player,ile+1))
                    beta = min(beta, value)
                    if  alpha>=beta :
                        #print("cut")
                        break
                   
                    
                return value
        
        best_move = None
        best_score = -math.inf
        alpha = -math.inf
        beta = math.inf
        for board in trim(self,self.legal_moves,self.turn,ile):
           # print("cos")
            val = alphabeta(board[1], depth-1, alpha, beta, board[1].turn,player,ile+1)
            if val>=best_score  :
                best_move = board[2]
                best_score=val
        return best_move


    

num=100
wins=0
for i in range(1,num+1):
    board=chess.Board()
    ile=1
    with open(r'C:\Users\dominik\Desktop\Sztuczna inteligencja\lista4\lichess_db_standard_rated_2013-01.pgn') as file:
                game = chess.pgn.read_game(file)

                
                mainline_moves = list(game.mainline_moves())
    while board.is_game_over()==False and ile<140:
        if board.turn==chess.WHITE:
            #moj bot
            if len(mainline_moves)>0 and mainline_moves[0]!= None and    mainline_moves[0] in board.legal_moves :
                
                board.push(mainline_moves[0])
                mainline_moves=mainline_moves[2:]
                #print("cji")
            else:
                moves=find_best(board,3,board.turn,ile)
                board.push(moves)
        else:
            moves=list(board.legal_moves)
            m=random.choice(moves)
            #print(m)
            board.push(m)
        #print(board)
        ile+=1
    
        
    else:
        print(board.result())
    
    if board.result()=='1-0':
        wins+=1
    print(i,wins,ile)