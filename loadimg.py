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
    
    return [button0, button1, button2, button3]