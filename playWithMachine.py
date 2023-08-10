import random
from copy import deepcopy
def playingRandom(state):
    turn = state.redMove
    listMove = []
    if not turn:
        listMove = deepcopy(state.getAllValidMove())
        if listMove != []:
            move = random.choice(listMove)
            return move
    return None
