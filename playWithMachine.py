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
        self.realMove = None
        self.path = []
    def playMinimax(self, board, redMove, after, depth, isMaximizingPlayer, alpha=float('-inf'), beta=float('inf')):
        miniBoard = deepcopy(board)
        #print("listNextMoves: ",listNextMoves)
        listNextMoves = deepcopy(s.State.getAllValid(miniBoard, not isMaximizingPlayer, after)) # = [ [(),()],[(),()],[(),()] ]
        print(not isMaximizingPlayer,"-listNextMove: ",listNextMoves)
        if depth == 0 or listNextMoves == []:
            return s.State.evaluate(miniBoard, not isMaximizingPlayer, after)*(1 if isMaximizingPlayer else -1), None #*(1 if isMaximizingPlayer else -1)      # return value of board which is the score of AI
        self.nodeExpand += 1
        random.shuffle(listNextMoves)
        # bestValue = float('-inf') if isMaximizingPlayer else float('inf')

        # bestScore = float('-inf')
        # for move in listNextMoves:
        #     nextboard = deepcopy(s.miniNext(miniBoard, redMove, after, move))
            
        #     newValue, path = self.playMinimax(nextboard, not redMove , after, depth-1, not isMaximizingPlayer, -beta, -alpha)
        #     newValue *= -1
        #     if newValue > bestScore:
        #         bestScore = newValue
                
                
        #         print ("move: ", move, "value: ", newValue)
        #         if depth == self.maxDepth:
        #             self.realMove = deepcopy(move)
        #             self.path = path + [move]

        #     if bestScore > alpha:
        #         alpha = bestScore
        #     if alpha >= beta:
        #         break
        # return bestScore, self.path
        if isMaximizingPlayer:
            best = float('-inf')
            for move in listNextMoves:
                nextboard = deepcopy(s.miniNext(miniBoard, not isMaximizingPlayer, after, move))
                value, path = self.playMinimax(nextboard, not redMove, after, depth-1, False, alpha, beta)
                if value > best:
                    best = value
                    if depth == self.maxDepth:
                        self.realMove = deepcopy(move)
                        self.path = [move]+ path
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
            return best, self.path
        else:
            best = float('inf')
            for move in listNextMoves:
                nextboard = deepcopy(s.miniNext(miniBoard, not isMaximizingPlayer, after, move))
                value, path = self.playMinimax(nextboard, not redMove , after, depth-1, True, alpha, beta)
                if value < best:
                    best = value
                    if depth == self.maxDepth:
                        self.realMove = deepcopy(move)
                        self.path = [move] + path
                beta = min(beta, best)
                if alpha >= beta:
                    break
            return best, self.path
        
        
        
def playingWithCalCu(state):
    
    minimax = Minimax(2) 
    minimax.playMinimax(state.board, state.redMove, state.after, minimax.maxDepth, True)
    move = minimax.realMove
    print("node: ", minimax.nodeExpand,"path: ", minimax.path)
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