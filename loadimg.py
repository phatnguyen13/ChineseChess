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