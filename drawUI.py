import pygame as p
import setting as s
import loadimg as l
import chessEngine
import button as b
import playWithMachine as pWM
import time
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

check = True
def drawGameState(screen,gs: chessEngine.State,st):
    screen.blit(boardImg,(0,0))
    drawChessMan(screen,gs.board)
    global check
    if gs.checkEnd()[0]:
        drawEndGame(screen,gs)
        return
    elif gs.checkMate() and check:
        startTime = p.time.get_ticks()
        drawChessMate(screen,gs)
        if p.time.get_ticks() - startTime >= 2000:
            check = False
        
    elif (gs.after and gs.redMove) or (not gs.after and not gs.redMove):
        drawAIThink(screen) if st else None
    
    if gs.selectedCell != ():
        drawValid(screen,gs)
        screen.blit(squareImg, p.Rect(s.GRID[1]+ gs.selectedCell[1]*s.GRID[2],s.GRID[0]+gs.selectedCell[0]*s.GRID[2], s.CELL_SIZE, s.CELL_SIZE))
    drawFoot(screen,gs)
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
    checkimg = l.loadCheckMate()
    screen.blit(checkimg,(s.WIDTH/2 - checkimg.get_width()/2, s.SCREEN_HEIGHT/2 - checkimg.get_height()/2))
    # p.font.init()
    # myFont = p.font.SysFont('Comic Sans MS', 30)
    # textSurface = myFont.render('Checkmate', False, (0, 0, 0))
    # screen.blit(textSurface,(s.WIDTH/2 - textSurface.get_width()/2, s.SCREEN_HEIGHT/2 - textSurface.get_height()/2))

def drawEndGame(screen, gs: chessEngine.State):
    print("end game")
    if gs.checkEnd()[0]:
        winner= 'RED' if gs.checkEnd()[1] =='r' else 'BLACK'
        p.font.init()
        print(winner," WIN")
        myFont = p.font.SysFont('Comic Sans MS', 30)
        textSurface = myFont.render(winner + " WIN", False, (0, 0, 0))
        screen.blit(textSurface,(s.WIDTH/2 - textSurface.get_width()/2, s.SCREEN_HEIGHT/2 - textSurface.get_height()/2))
        

def drawAIThink(screen):
    p.font.init()
    myFont = p.font.SysFont('Comic Sans MS', 30)
    textSurface = myFont.render("ChaCa's thinking...", False, (0, 0, 0))
    screen.blit(textSurface,(s.WIDTH/2 - textSurface.get_width()/2, s.SCREEN_HEIGHT/2 - textSurface.get_height()/2))


def drawTitle(screen, x, y, width, height, text):
    p.font.init()
    tFont = p.font.SysFont('Comic Sans MS', 30)
    
    Title = tFont.render(text, True, (55, 255, 255))
    Rect = Title.get_rect()
    Rect.center = ((x + width/2), (y + height/2))
    screen.blit(Title, Rect)
    return Title
def drawButton(screen, x, y, width, height, text):
    Button = p.Rect(x, y, width, height)
    p.font.init()
    bFont = p.font.SysFont('Comic Sans MS', 30)
    content = bFont.render(text, True, (55,55,55))
    Rect = content.get_rect()
    Rect.center = Button.center
    p.draw.rect(screen, (255, 255, 255), Button)
    screen.blit(content, Rect)
    return Button
    
def drawStart(screen, gs):
    drawTitle(screen, s.WIDTH/2, 100, 0, 0, "Chinese Chess")
    randomBut = drawButton(screen, s.BUTTEXT_X , s.BUTTEXT_Y, s.BUT_TEXT, s.BUT_TEXT/6, "Play with Random")
    chaca = drawButton(screen, s.BUTTEXT_X,  s.BUTTEXT_Y + s.BUT_TEXT/3, s.BUT_TEXT, s.BUT_TEXT/6, "Play with ChaCa")
    test = drawButton(screen, s.BUTTEXT_X , s.BUTTEXT_Y + 2*s.BUT_TEXT/3, s.BUT_TEXT, s.BUT_TEXT/6, "Watch them play")
    solo = drawButton(screen, s.BUTTEXT_X , s.BUTTEXT_Y + s.BUT_TEXT, s.BUT_TEXT, s.BUT_TEXT/6, "Play together")
    
    click = p.mouse.get_pressed()[0]
    if click==1:
        mouse = p.mouse.get_pos()
        if randomBut.collidepoint(mouse):
            time.sleep(0.2)
            return 1
        elif chaca.collidepoint(mouse):
            time.sleep(0.2)
            return 2
        elif test.collidepoint(mouse):
            time.sleep(0.2)
            return 3
        elif solo.collidepoint(mouse):
            time.sleep(0.2)
            return 4
    return -1