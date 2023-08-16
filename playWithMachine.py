import random
from copy import deepcopy
import chessEngine as s

def playingRandom(state):        
    listMove = deepcopy(state.getAllValidMove())
    for i in listMove:
        print("list move: ",i)
    if listMove != []:
        move = random.choice(listMove)
        print("turn of red: ",state.redMove,"----AI move: ",move.chessManMoved," ",move.getChange())
        return move
    return None



class Minimax:
    def __init__(self, maxDepth):
        self.maxDepth = maxDepth
        self.nodeExpand = 0
        
    def playMinimax(self, board, redmove, after, depth, isMaximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        miniBoard = deepcopy(board)
        listNextMoves = deepcopy(s.State.getAllValid(miniBoard,redmove,after)) # = [ [(),()],[(),()],[(),()] ]
        #print("listNextMoves: ",listNextMoves)
        if depth == self.maxDepth or listNextMoves == []:
            return s.State.evaluate(miniBoard,redmove, after), None
        self.nodeExpand += 1
        
        bestValue = float('-inf') if isMaximizingPlayer else float('inf')
        for move in listNextMoves:
            nextboard = deepcopy(s.miniNext(miniBoard,redmove,after,move))
            
            evalChild, actionChild = self.playMinimax(nextboard,not redmove,after, depth+1, not isMaximizingPlayer, alpha, beta)

            print("evalChild: ",evalChild," actionChild: ",actionChild, "node expand: ", self.nodeExpand)
            if isMaximizingPlayer and bestValue < evalChild:
                bestValue = evalChild
                bestAction = deepcopy(move)
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
            elif not isMaximizingPlayer and bestValue > evalChild:
                bestValue = evalChild
                bestAction = deepcopy(move)
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
        return bestValue, bestAction
        
def playingWithCalCu(state):
    
    minimax = Minimax(3) 
    move = deepcopy(minimax.playMinimax(state.board, state.redMove, state.after, 0, True)[1])
    if move != None:

        m = s.Move(state.board,move[0],move[1])
        return m
    return None


def playWithAI(state, type):
    turn = True if state.after else False
    if turn:
        if state.redMove:
            play = None
            if type == 1:
                play = playingRandom(state)
            elif type ==2:
                play = playingWithCalCu(state)
                
            if play:
                state.makeMove(play)
            else:
                print("no move")
    else:
        if not state.redMove:
            play = None
            if type == 1:
                play = playingRandom(state)
            elif type ==2:
                play = playingWithCalCu(state)
                
            if play:
                state.makeMove(play)
            else:
                print("no move")