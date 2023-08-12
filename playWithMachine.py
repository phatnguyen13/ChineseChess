import random
from copy import deepcopy
#import chessEngine as s
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
    def __init__(self, maxDepth, player):
        self.maxDepth = maxDepth
        self.player = player
        self.nodeExpand = 0

    def playMinimax(self, initialState, depth, isMaximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        state = deepcopy(initialState)
        
        if depth == self.maxDepth or state.checkEnd()[0]:
            return state.evaluate(), None
        self.nodeExpand += 1
        listNextMoves = deepcopy(state.getAllValidMove())
        
        bestValue = float('-inf') if isMaximizingPlayer else float('inf')
        for move in listNextMoves:
            state.makeMove(move)   
            
            evalChild, actionChild = self.playMinimax(state, depth+1, not isMaximizingPlayer, alpha, beta)
            state.reMove()
            print("evalChild: ",evalChild," actionChild: ",actionChild)
            if isMaximizingPlayer and bestValue < evalChild:
                bestValue = evalChild
                bestAction = move
                alpha = max(alpha, bestValue)
                if beta <= alpha:
                    break
            elif not isMaximizingPlayer and bestValue > evalChild:
                bestValue = evalChild
                bestAction = move
                beta = min(beta, bestValue)
                if beta <= alpha:
                    break
        return bestValue, bestAction
        
def playingWithCalCu(state):
    
    minimax = Minimax(3, state.redMove)
    move = minimax.playMinimax(state, 0, state.redMove)[1]
    if move != None:
        print("minimax play")
        return move
    return None