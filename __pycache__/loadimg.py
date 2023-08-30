import pygame as p
import setting as s
def loadChessMan():
    chessMan = {}
    chessName = ['bch', 'bma', 'bph','bxe','bvo','bsi','btu','rch','rma','rph','rxe','rvo','rsi','rtu']
    for i in chessName:
        chessMan[i]= p.transform.scale(p.image.load('img/'+i+'.png'),(s.CELL_SIZE,s.CELL_SIZE))
    return chessMan
def loadBoard():
    board = p.transform.scale(p.image.load('img/board.jpg'),(s.WIDTH,s.HEIGHT))
    return board
def loadLight():
    light = p.transform.scale(p.image.load('img/light.png'),(s.CELL_SIZE, s.CELL_SIZE))
    return light
def loadButton(type):
    button0, button1, button2 = None, None, None
    if type == 'backward':
        button0 = p.transform.scale(p.image.load('img/backward.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button1 = p.transform.scale(p.image.load('img/backwardActive.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button2 = p.transform.scale(p.image.load('img/backwardClick.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button3 = p.transform.scale(p.image.load('img/backwardHover.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
    elif type == 'nextstep':
        button0 = p.transform.scale(p.image.load('img/nextstep.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button1 = p.transform.scale(p.image.load('img/nextstepActive.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button2 = p.transform.scale(p.image.load('img/nextstepClick.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button3 = p.transform.scale(p.image.load('img/nextstepHover.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
    elif type == 'reverse':
        button0 = p.transform.scale(p.image.load('img/exchange.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button1 = p.transform.scale(p.image.load('img/exchangeActive.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button2 = p.transform.scale(p.image.load('img/exchangeClick.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button3 = p.transform.scale(p.image.load('img/exchangeHover.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
    elif type == 'start':
        button0 = p.transform.scale(p.image.load('img/start.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button1 = p.transform.scale(p.image.load('img/startClick.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button2 = p.transform.scale(p.image.load('img/startHover.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button3 = None
    elif type == 'replay':
        button0 = p.transform.scale(p.image.load('img/replay.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button1 = p.transform.scale(p.image.load('img/replayClick.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button2 = p.transform.scale(p.image.load('img/replayHover.png'),(s.BUT_WIDTH, s.BUT_HEIGHT))
        button3 = None
    return [button0, button1, button2, button3]
def loadSquare ():
    square = p.transform.scale(p.image.load('img/squareOrigin.png'),(s.CELL_SIZE, s.CELL_SIZE))
    return square

def loadCheckMate():
    checkMate = p.transform.scale(p.image.load('img/check.png'),(s.CELL_SIZE*3, s.CELL_SIZE*3))
    return checkMate