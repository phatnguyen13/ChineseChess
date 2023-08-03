import pygame as p
import setting as s
import loadimg as l
import chessEngine

chessManImg = l.loadChessMan()
boardImg = l.loadBoard()
lightImg = l.loadLight()
def main():
    p.init()   
    screen = p.display.set_mode((s.SCREEN_WIDTH,s.SCREEN_HEIGHT))
    clock = p.time.Clock()
    gs = chessEngine.State()
    for i in range(10):
        for j in range(9):
            if gs.chessMan[i][j] != None:
                print(gs.chessMan[i][j].type) 
    run = True
    listClick=[]
    cell =()
    while run:
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            elif e.type == p.MOUSEBUTTONDOWN:
                start = s.GRID
                pos = p.mouse.get_pos()
                row = (pos[1]-start[0])//start[2]
                col = (pos[0]-start[1])//start[2]
                print(row,'---',col)
                
                
                listClick.append((row,col))
                if gs.board[listClick[0][0]][listClick[0][1]]=='---':
                    listClick =[]
                else:
                    gs.selectedCell = listClick[0]
                    
                if len(listClick) ==2:
                    if listClick[0] == listClick[1]:
                        listClick =[]
                        
                    else:
                        move = chessEngine.Move(gs,listClick[0], listClick[1])
                        gs.makeMove(move)
                        listClick=[]
                    gs.selectedCell = ()
                        
        drawGameState(screen,gs)
        clock.tick(s.MAX_FPS)
        p.display.flip()
        
def drawValid(screen,gs):
    listValid = gs.chessMan[gs.selectedCell[0]][gs.selectedCell[1]].type.canMove(gs.board, gs.selectedCell)
    start = s.GRID
    print(listValid)
    for i in listValid:
        screen.blit(lightImg, p.Rect(start[1]+ i[1]*start[2],start[0]+i[0]*start[2], s.CELL_SIZE, s.CELL_SIZE))
def drawGameState(screen,gs):
    screen.blit(boardImg,(0,0))
    drawChessMan(screen,gs.board)
    if gs.selectedCell != ():
        drawValid(screen,gs)
def drawChessMan(screen,board):
    start = s.GRID
    for i in range(s.DIMENSION+1):
        for j in range(s.DIMENSION):
            chessMan = board[i][j]
            if chessMan != '---':  
                screen.blit(chessManImg[chessMan],p.Rect(start[1]+j*start[2],start[0]+i*start[2],s.CELL_SIZE,s.CELL_SIZE))
                
             
if __name__ == '__main__':
    main()
    