import pygame as p
import setting as s
import loadimg as l
import chessEngine
import button as b
import playWithMachine as pWM
from main import st
chessManImg = l.loadChessMan()
boardImg = l.loadBoard()
lightImg = l.loadLight()
squareImg = l.loadSquare()

def drawValid(screen,gs):
    listValid = gs.checkValid(gs.selectedCell)
    start = s.GRID
    for i in listValid:
        screen.blit(lightImg, p.Rect(start[1]+ i[1]*start[2],start[0]+i[0]*start[2], s.CELL_SIZE, s.CELL_SIZE))
def drawGameState(screen,gs,st):
    screen.blit(boardImg,(0,0))
    drawChessMan(screen,gs.board)
    if gs.selectedCell != ():
        drawValid(screen,gs)
        screen.blit(squareImg, p.Rect(s.GRID[1]+ gs.selectedCell[1]*s.GRID[2],s.GRID[0]+gs.selectedCell[0]*s.GRID[2], s.CELL_SIZE, s.CELL_SIZE))
    if gs.checkMate():
        drawChessMate(screen,gs)
    elif (gs.after and gs.redMove) or (not gs.after and not gs.redMove):
        drawAIThink(screen) if st else None
    if gs.checkEnd():
        drawEndGame(screen,gs)
    # if (gs.after and gs.redMove) or (not gs.after and not gs.redMove):
    #     drawAIThink(screen) if st else None
def drawChessMan(screen,board):
    start = s.GRID
    for i in range(s.DIMENSION+1):
        for j in range(s.DIMENSION):
            chessMan = board[i][j]
            if chessMan != '---':  
                screen.blit(chessManImg[chessMan],p.Rect(start[1]+j*start[2],start[0]+i*start[2],s.CELL_SIZE,s.CELL_SIZE))
def drawFoot(screen, gs: chessEngine.State):
    if gs.moveLog == []:
        return
    startRow = gs.moveLog[-1].startRow
    startCol = gs.moveLog[-1].startCol
    endRow = gs.moveLog[-1].endRow
    endCol = gs.moveLog[-1].endCol
    screen.blit(squareImg, p.Rect(s.GRID[1]+ startCol*s.GRID[2],s.GRID[0]+startRow*s.GRID[2], s.CELL_SIZE, s.CELL_SIZE))
    screen.blit(squareImg, p.Rect(s.GRID[1]+ endCol*s.GRID[2],s.GRID[0]+endRow*s.GRID[2], s.CELL_SIZE, s.CELL_SIZE))
def drawChessMate(screen, gs: chessEngine.State):
    if gs.checkMate() and not gs.checkEnd()[0]:
        p.font.init()
        myFont = p.font.SysFont('Comic Sans MS', 30)
        textSurface = myFont.render('Checkmate', False, (0, 0, 0))
        screen.blit(textSurface,(s.WIDTH/2 - textSurface.get_width()/2, s.SCREEN_HEIGHT/2 - textSurface.get_height()/2))
    else:
        return
def drawEndGame(screen, gs: chessEngine.State):
    if gs.checkEnd()[0]:
        winner= 'RED' if gs.checkEnd()[1] =='r' else 'BLACK'
        p.font.init()
        myFont = p.font.SysFont('Comic Sans MS', 30)
        textSurface = myFont.render(winner + " WIN", False, (0, 0, 0))
        screen.blit(textSurface,(s.WIDTH/2 - textSurface.get_width()/2, s.SCREEN_HEIGHT/2 - textSurface.get_height()/2))
def drawAIThink(screen):
    p.font.init()
    myFont = p.font.SysFont('Comic Sans MS', 30)
    textSurface = myFont.render("ChaCa is thinking...", False, (0, 0, 0))
    screen.blit(textSurface,(s.WIDTH/2 - textSurface.get_width()/2, s.SCREEN_HEIGHT/2 - textSurface.get_height()/2))
