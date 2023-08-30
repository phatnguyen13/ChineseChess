import random
from copy import deepcopy
import chessEngine as s
import bookmove as bm
from ml import playwithdeep as pWM
#this is the function generate random move
def playingRandom(state):
    listMove = deepcopy(s.State.getAllValid(state.board, state.redMove, state.after))
    if listMove != []:
        move = random.choice(listMove)
        return s.Move(state.board, move[0], move[1])
    return None

#this is Minimax algorithm
count=0    # keep number step of state (for defind start, mid, end game)
class Minimax:
    def __init__(self, maxDepth):
        self.maxDepth = maxDepth
        self.nodeExpand = 0
        self.realMove = None
        self.path = []
        
    # this is the function to play Minimax
    def playMinimax(self, board, redMove, after, depth, isMaximizingPlayer, c, alpha=float('-inf'), beta=float('inf')):
        global count
        miniBoard = deepcopy(board)
        listNextMoves = deepcopy(s.State.getAllValid(miniBoard, redMove , after)) # = [ [(),()],[(),()],[(),()] ]
        if depth == 0 or listNextMoves == []:
            return s.State.evaluate(miniBoard, redMove, after, c)*(1 if isMaximizingPlayer else -1), None #*(1 if isMaximizingPlayer else -1)      # return value of board which is the score of AI
        self.nodeExpand += 1
        random.shuffle(listNextMoves)
        if isMaximizingPlayer:
            best = float('-inf')
            for move in listNextMoves:
                nextboard = deepcopy(s.miniNext(miniBoard, not isMaximizingPlayer, after, move))
                value, path = self.playMinimax(nextboard, not redMove, after, depth-1, False, c, alpha, beta)
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
                value, path = self.playMinimax(nextboard, not redMove , after, depth-1, True, c, alpha, beta)
                if value < best:
                    best = value
                    if depth == self.maxDepth:
                        self.realMove = deepcopy(move)
                        
                beta = min(beta, best)
                if alpha >= beta:
                    break
            
            return best, self.path
    
# this is the function that call CHACAPRO in UI
def playingWithPro(state):
    
    minimax = Minimax(2) 
    minimax.playMinimax(state.board, state.redMove, state.after, minimax.maxDepth, True, len(state.moveLog))
    move = minimax.realMove

    if move != None:
        m = s.Move(state.board,move[0],move[1])
        return m
    return None

# this is the function that call CHACA in UI
def playingWithCalCu(state):
    minimax = Minimax(2) 
    minimax.playMinimax(state.board, state.redMove, state.after, minimax.maxDepth, True, 0)
    move = minimax.realMove
    if move != None:
        m = s.Move(state.board,move[0],move[1])
        return m
    return None


# this is the entring function of AI which decide which AI will play
def playWithAI(state, type):
    turn = True if (state.after and state.redMove) or (not state.after and not state.redMove) else False
    if turn:
        play = None
        if type == 1:
            play = playingRandom(state)
        elif type ==2:
            play = playingWithCalCu(state)
        elif type ==3:
            play = playingWithPro(state)
        elif type == 5:
            play = pWM.play
        if play:
            state.makeMove(play)


# this is the function to test AI (all win with random machine)
def test(state):
    turn = True if state.after else False
    play = None
    if turn:
        if state.redMove:
            play = None
            play = playingWithPro(state)
            if play:
                state.makeMove(play)
        else:
            play = None
            play = playingRandom(state)
            if play:
                state.makeMove(play)
    else:
        if state.redMove:
            play = None
            play = playingRandom(state)
        else:
            play = None    
            play = playingWithPro(state)
        return play
    
