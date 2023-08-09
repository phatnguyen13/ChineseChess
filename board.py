import random
import chessEngine
def playingRandom(state: chessEngine.State):
    turn = state.redMove
    while not state.checkMate():
        move = random.choice(state.getValidMoves())
        state.makeMove(move)
        turn = not turn

    