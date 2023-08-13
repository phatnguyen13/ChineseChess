import pygame as p
import setting as s
import loadimg as l
import chessEngine
import button as b
import playWithMachine as pWM
import drawUI as draw
st = False
pa = False
def startGame():
    global st
    st= True
    print("start game")
def playAgainGame():
    global pa
    pa = True
    print("play again game")
def setup():
    global pa
    global st
    p.init()
    pa = False
    st = False
    p.display.set_caption('Chinese Chess')
def shutDown():
    p.quit()

def mainLoop():

    screen = p.display.set_mode((s.SCREEN_WIDTH,s.SCREEN_HEIGHT))
    clock = p.time.Clock()
    gs = chessEngine.State()
    run = True
    listClick=[]
    cell =()
    
    objects=()
    backwardBut = b.Button(s.BACKWARD_X, s.BACKWARD_Y, s.BUT_WIDTH, s.BUT_HEIGHT,'re', l.loadButton('backward'), gs.reMoveReal)
    nextstepBut = b.Button(s.NEXTSTEP_X, s.NEXTSTEP_Y, s.BUT_WIDTH, s.BUT_HEIGHT,'ne', l.loadButton('nextstep'), gs.nextMoveReal)
    reverseBut = b.SButton(s.REVERSE_X, s.REVERSE_Y, s.BUT_WIDTH, s.BUT_HEIGHT,'ex', l.loadButton('reverse'), gs.reverse)
    startBut = b.Button(s.START_X, s.START_Y, s.BUT_WIDTH, s.BUT_HEIGHT,'st', l.loadButton('start'), startGame)
    playAgainBut = b.SButton(s.REPLAY_X, s.REPLAY_Y, s.BUT_WIDTH, s.BUT_HEIGHT,'pa', l.loadButton('replay'), playAgainGame)
    
    # objects.append(backwardBut)
    # objects.append(nextstepBut)
    # objects.append(reverseBut)
    # objects.append(startBut)
    objects += (backwardBut,nextstepBut,reverseBut,startBut,playAgainBut)
    print("AI random: 1")
    print("AI minimax: 2")
    print("Play alone: 3")
    print("input 1,3 or 2: ")
    x=input()
    while run:
        global st
        global pa
        draw.drawGameState(screen,gs,st)
        
        for e in p.event.get():
            
            if e.type == p.QUIT:
                run = False
            
            elif e.type == p.MOUSEBUTTONDOWN:
                if st == False: continue
                
                start = s.GRID
                pos = p.mouse.get_pos() 
              
                row = int((pos[1]-start[0])//start[2])
                col = int((pos[0]-start[1])//start[2])
                if row >9 or col >8 or row <0 or col <0:
                    break
                if listClick ==[]:
                    if (gs.redMove and gs.board[row][col][0] == 'b') or (not gs.redMove and gs.board[row][col][0] == 'r'): break
                
                listClick.append((row,col))
                if 0<= row <=9 and 0<= col <=8:
                    if gs.board[listClick[0][0]][listClick[0][1]]=='---':
                        listClick =[]
                    else:
                        gs.selectedCell = listClick[0]
                        
                    if len(listClick) ==2:
                        if listClick[0] == listClick[1]:
                            listClick =[]
                        else:
                            listValid = gs.checkValid(gs.selectedCell)
                            if listClick[1] in listValid:
                                move = chessEngine.Move(gs,listClick[0], listClick[1])
                                gs.makeMove(move)
                                AITurn = True
                                draw.drawGameState(screen,gs,st)
                                clock.tick(s.MAX_FPS)
                                p.display.flip()
                            listClick =[]
                        gs.selectedCell = ()
            # elif gs.after and st:
            #     gs.playWithAI()
            if st:
                # draw.drawAIThink(screen) 
                # clock.tick(s.MAX_FPS)
                # p.display.flip()
                if x=='1':
                    gs.playWithAI()
                elif x=='2':
                    gs.playWithAI2()
                elif x == '3':
                    pass
                #AITurn = not AITurn
        if pa:
            pa = False
            main()    
            
        for o in objects:
            o.process(screen,gs)
        draw.drawFoot(screen,gs)

        clock.tick(s.MAX_FPS)
        p.display.flip()

def main():
    setup()
    mainLoop()
    shutDown()
        
if __name__ == '__main__':
    main()
    