import pygame as p
import setting as s
import loadimg as l
import chessEngine
import button as b
import playWithMachine as pWM
import drawUI as draw


st = False
pa = False
robo = False
x = -1
def startGame():
    global st
    st= True
    
def playAgainGame():
    global pa
    pa = True
    
def setup():
    global pa
    global st
    global x
    p.init()
    pa = False
    st = False

def shutDown():
    p.quit()

def mainLoop():

    p.display.set_caption('Chinese Chess')
    screen = p.display.set_mode((s.SCREEN_WIDTH,s.SCREEN_HEIGHT))
    
    gs = chessEngine.State()
    clock = p.time.Clock()
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

    x = -1
    while run:
        global st
        global pa
        global robo


        for e in p.event.get():
            
            
            if x != -1:  
                draw.drawGameState(screen,gs,st)
                for o in objects:
                    o.process(screen,gs)
                #draw.drawFoot(screen,gs)
            if x == -1:
                x  = draw.drawStart(screen, gs)
            if st:
                    # draw.drawAIThink(screen) 
                    draw.drawGameState(screen,gs,st)
                    #draw.drawAIThink(screen) if not gs.redMove and not gs.after and x !=3 else None
                    if x==0:
                        pass
                    elif x == 1:
                        
                        pWM.playWithAI(gs,1)
                    elif x == 2:
                        
                        pWM.playWithAI(gs,2)
                    elif x == 3:
                        robo = True
                        if not gs.redMove and not gs.after:
                            draw.drawFoot(screen,gs)
                            
                        
                        move = pWM.test(gs)
                        if move != None:
                            gs.makeMove(move)
    
                    elif x ==4:
                        pass
                    
                    
            if e.type == p.QUIT:
                run = False
            
            elif e.type == p.MOUSEBUTTONDOWN:
                if st == False or robo: continue
                
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
                                move = chessEngine.Move(gs.board,listClick[0], listClick[1])
                                gs.makeMove(move)
                                AITurn = True

                                draw.drawGameState(screen,gs,st)
                                clock.tick(s.MAX_FPS)
                                p.display.flip()
                            listClick =[]
                        gs.selectedCell = ()
        # if gs.checkMate():
        #     print("checkmake")
        #     draw.drawChessMate(screen,gs)
        if pa:
            pa = False
            main()    

        clock.tick(s.MAX_FPS)
        p.display.flip()
        
def main():
    
    setup()
    
    mainLoop()
    shutDown()
        
if __name__ == '__main__':
    main()
    