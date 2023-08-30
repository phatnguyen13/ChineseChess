import random
from copy import deepcopy
import chessEngine as s
import tensorflow as tf
from keras.models import load_model
from ml import convert as c
import numpy as np



model = load_model('C:\\Users\\OnDoing\\ChineseChess\\ml\\chinese_chess_model_10000.h5')
#model = load_model('C:\\Users\\OnDoing\\ChineseChess\\ml\\chinese_chess_model_10000.h5')
def evaluation(board, redMove, after):
    newBoard = deepcopy(board)
    X_board = c.one_hot_encode(newBoard)
    # for i in (X_board):
    #     print(i)
    
    X_turn = 0 if redMove else 1
    x = np.array([X_board])
    
    xx = np.array([X_turn])
    
    y = model.predict([x,xx])
    return y.flatten()

class Minimax:
    def __init__(self, maxDepth):
        self.maxDepth = maxDepth
        self.nodeExpand = 0
        self.realMove = None
        self.path = []
    def playMinimax(self, board, redMove, after, depth, isMaximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        miniBoard = deepcopy(board)
        #print("listNextMoves: ",listNextMoves)
        listNextMoves = deepcopy(s.State.getAllValid(miniBoard, redMove , after)) # = [ [(),()],[(),()],[(),()] ]
        
        # print(isMaximizingPlayer,"-listNextMove: ",listNextMoves)
        if depth == 0 or listNextMoves == []:
            return evaluation(miniBoard, redMove, after)*(1 if isMaximizingPlayer else -1), None #*(1 if isMaximizingPlayer else -1)      # return value of board which is the score of AI
        self.nodeExpand += 1
        random.shuffle(listNextMoves)

        if isMaximizingPlayer:
            best = float('-inf')
            for move in listNextMoves:
                nextboard = deepcopy(s.miniNext(miniBoard, not isMaximizingPlayer, after, move))
                value, path = self.playMinimax(nextboard, not redMove, after, depth-1, False, alpha, beta)
                #print("max: ",value)
                if value > best:
                    best = value
                    if depth == self.maxDepth:
                        self.realMove = deepcopy(move)
                        
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
            return best, self.path
        else:
            best = float('inf')
            for move in listNextMoves:
                nextboard = deepcopy(s.miniNext(miniBoard, redMove, after, move))
                value, path = self.playMinimax(nextboard, not redMove , after, depth-1, True, alpha, beta)
                #print("min: ",value)
                if value < best:
                    best = value
                    if depth == self.maxDepth:
                        self.realMove = deepcopy(move)
                        
                beta = min(beta, best)
                if alpha >= beta:
                    break
            return best, self.path
            
        
def playingWithCalCu(state):
    
    minimax = Minimax(2) 
    minimax.playMinimax(state.board, state.redMove, state.after, minimax.maxDepth, True)
    move = minimax.realMove

    if move != None:
        m = s.Move(state.board,move[0],move[1])
        return m
    return None


def playWithChaca(state):
    turn = True if state.after else False
    if turn:
        if state.redMove:
            play = None
            play = playingWithCalCu(state)
            if play:
                state.makeMove(play)
            else:
                print("no move")
    else:
        if not state.redMove:

            play = playingWithCalCu(state)
                
            if play:
                state.makeMove(play)
            else:
                print("no move")

