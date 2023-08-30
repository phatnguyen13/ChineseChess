import chessEngine
from copy import deepcopy
import rule
import random
import chessEngine as s


khaicuocRed = [
    #Phong ma
    ['pm',
    [(9,1),(7,2)],
    [(9,7),(7,6)]],

    #binh xe
    ['bx',
    [(9,0),(9,1)],
    [(9,8),(9,7)]],
    

    #tan tuong
    ['tt',
    [(9,2),(7,4)],
    [(9,7),(7,4)]],
    
    #tan sy
    ['ts',
    [(9,3),(8,4)],
    [(9,5),(8,4)]],
    
        
    #Binh Phao'
    ['bp',
    [(7,1),(7,5)], 
    [(7,1),(7,4)],
    [(7,1),(7,3)],
    [(7,7),(7,5)],  
    [(7,7),(7,3)], 
    [(7,7),(7,4)]],
    
    ]
khaicuocBlack = [
    #Phong ma
    ['pm',
    [(0,1),(2,2)],
    [(0,7),(2,6)]],
    
    #binh xe
    ['bx',
    [(0,0),(0,1)],
    [(0,8),(0,7)]],
    
    #tan xe

    
    #tan tuong
    ['tt',
    [(0,2),(2,4)],
    [(0,6),(2,4)]],
    
    #tan sy
    ['ts',
    [(0,3),(1,4)],
    [(0,5),(1,4)]],
    
    #Binh Phao'
    ['bp',
    [(2,1),(2,5)], 
    [(2,1),(2,4)],
    [(2,1),(2,3)],
    [(2,7),(2,5)],  
    [(2,7),(2,3)], 
    [(2,7),(2,4)]]
    ]

type = None

# this function will chose a random "khai cuoc" and return a move
def playingBeginning(state):
    global type
    
    listMove, listNotMove = deepcopy(khaicuocBlack), deepcopy(khaicuocRed)
    
    step = len(state.moveLog)/2      #step thu i   
    turn = (state.redMove and state.after) or (not state.redMove and not state.after)
    
    beforeMove = state.moveLog[-1] if state.moveLog != [] else None
    
    if beforeMove != None:
        beforeMove = [(beforeMove.startRow, beforeMove.startCol), (beforeMove.endRow, beforeMove.endCol)]
        for i in listNotMove:
            if beforeMove in i:
                break
        else:
            return None
    listRealMove = []
    if step <= 6: 
        iter = 0

        while iter <6: 
            if type == None or iter %2==0:
                listRealMove = deepcopy(random.choice(listMove))    # chose a khai cuoc
                move = deepcopy(random.choice(listRealMove[1:]))    # chose a move
                type = listRealMove[0]

            else:
                move = deepcopy(random.choice(listRealMove[1:]))

            row = move[0][0]
            col = move[0][0]
            if state.board[row][col] != '---' and turn == True:
                cells = rule.RuleMove(state.board,move[0],state.after)
                if move[1] in cells:
                    return s.Move(state.board,move[0],move[1])
            iter = iter + 1
    return None
