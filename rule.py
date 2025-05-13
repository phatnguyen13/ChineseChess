from abc import ABC, abstractmethod
from copy import deepcopy
import csv

import sys 
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
# count score at the bottom chess
belowPosition = {'xe':[], 'ma':[], 'vo':[], 'si':[], 'tu':[], 'ph':[], 'ch':[]}
for i in belowPosition.keys():
    name = i+'.csv'
    with open(resource_path(os.path.join('unity', name)), 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for r in range(len(row)):
                row[r] = float(row[r])
            belowPosition[i] += [row]

startPower = {'xe':90, 'ma':40, 'vo':25, 'si':30, 'tu':9000, 'ph':45, 'ch':10}  # power of chess Man at the start of the game
midlePower = {'xe':90, 'ma':40, 'vo':25, 'si':30, 'tu':9000, 'ph':50, 'ch':20}  # power of chess Man at the middle of the game
endPower = {'xe':100, 'ma':50, 'vo':40, 'si':40, 'tu':9000, 'ph':40, 'ch':25}   #  power of chess Man at the end of the game

# count score at the upper chess
upperPosition = {'xe':[], 'ma':[], 'vo':[], 'si':[], 'tu':[], 'ph':[], 'ch':[]}
for i in belowPosition.keys():
    upperPosition[i] = belowPosition[i][::-1]


# this is the class that return list of valid move of CAR (XE)
def canMoveCar(board,position,upSideDown):
    cells =[]
    team = board[position[0]][position[1]][0]
    i = position[0]
    j = position[1]

    for x in range(i+1,10):
        if board[x][j] == '---':
            cells += [(x,j)]
        
        elif board[x][j][0] != team:
            cells += [(x,j)]
            break
        else: break
    for x in range(i-1,-1,-1):
        if board[x][j] == '---':
            cells += [(x,j)]
        elif board[x][j][0] != team:
            cells += [(x,j)]
            break
        else: break
    for y in range(j+1,9):
        if board[i][y] =='---':
            cells += [(i,y)]
        elif board[i][y][0] != team:
            cells += [(i,y)]
            break
        else: break
    for y in range(j-1,-1,-1):
        if board[i][y] =='---':
            cells += [(i,y)]
        elif board[i][y][0] != team:
            cells += [(i,y)]
            break
        else: break
    return cells

# this is the class that return list of valid move of HORSE (MA)
def canMoveHorse(board,position,upSideDown):
    cells =[]
    team = board[position[0]][position[1]][0]
    nowRow = position[0]
    nowCol = position[1]
    if nowCol +1 <9:
        if board[nowRow][nowCol+1]=='---':
            if nowCol+2 < 9 and nowRow+1 < 10 and (board[nowRow+1][nowCol+2] == '---' or board[nowRow+1][nowCol+2][0] != team):
                cells += [(nowRow+1,nowCol+2)]
            if nowCol+2 < 9 and nowRow-1 >= 0 and (board[nowRow-1][nowCol+2] == '---' or board[nowRow-1][nowCol+2][0] != team):
                cells += [(nowRow-1,nowCol+2)]
    if nowCol -1 >=0:
        if board[nowRow][nowCol-1]=='---':
            if nowCol-2 >= 0 and nowRow+1 < 10 and (board[nowRow+1][nowCol-2] == '---' or board[nowRow+1][nowCol-2][0] != team):
                cells += [(nowRow+1,nowCol-2)]

            if nowCol-2 >= 0 and nowRow-1 >= 0 and (board[nowRow-1][nowCol-2] == '---' or board[nowRow-1][nowCol-2][0] != team):
                cells += [(nowRow-1,nowCol-2)]
    if nowRow +1 <10:
        if board[nowRow+1][nowCol]=='---':
            if nowCol+1 < 9 and nowRow+2 < 10 and (board[nowRow+2][nowCol+1] == '---' or board[nowRow+2][nowCol+1][0] != team):
                cells += [(nowRow+2,nowCol+1)]

            if nowCol-1 >= 0 and nowRow+2 < 10 and (board[nowRow+2][nowCol-1] == '---' or board[nowRow+2][nowCol-1][0] != team):
                cells += [(nowRow+2,nowCol-1)]
    if nowRow -1 >=0:
        if board[nowRow-1][nowCol]=='---':
            if nowCol+1 < 9 and nowRow-2 >= 0 and (board[nowRow-2][nowCol+1] == '---' or board[nowRow-2][nowCol+1][0] != team):
                cells += [(nowRow-2,nowCol+1)]
            if nowCol-1 >= 0 and nowRow-2 >= 0 and (board[nowRow-2][nowCol-1] == '---' or board[nowRow-2][nowCol-1][0] != team):
                cells += [(nowRow-2,nowCol-1)]
    return cells

# this is the class that return list of valid move of ELEPHANT (VO)
def canMoveElephant(board,position,upSideDown):
    cells =[]
    team = board[position[0]][position[1]][0]
    i = position[0]
    j = position[1]
    candidate = [(i+2,j+2),(i+2,j-2),(i-2,j+2),(i-2,j-2)]
    if not upSideDown:
        if team == 'b':
            for x in candidate:
                if 0<=x[0]<5 and 0<=x[1]<10:
                    if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            for x in candidate:
                if 4<x[0]<10 and 0<=x[1]<10:
                    if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
                        cells += [x]
    else:
        if team == 'b':
            for x in candidate:
                if 5<=x[0]<10 and 0<=x[1]<10:
                    if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            for x in candidate:
                if 0<=x[0]<6 and 0<=x[1]<10:
                    if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
                        cells += [x]
    return cells

# this is the class that return list of valid move of ADVISOR (SI)
def canMoveAdvisor(board,position,upSideDown):
    cells=[]
    i = position[0]
    j = position[1]
    team = board[position[0]][position[1]][0]
    candidate = [(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
    if not upSideDown:
        if team == 'b':
            for x in candidate:
                if 0<=x[0]<3 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            
            for x in candidate:
                if 7<=x[0]<10 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
    else:
        if team == 'b':
            for x in candidate:
                if 7<=x[0]<10 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            for x in candidate:
                if 0<=x[0]<3 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
    return cells


# this is the class that return list of valid move of KING (TUONG)
def canMoveKing(board,position,upSideDown):
    cells=[]
    i = position[0]
    j = position[1]
    team = board[position[0]][position[1]][0]
    candidate = [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]
    if not upSideDown:
        if team == 'b':
            for x in candidate:
                if 0<=x[0]<3 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            for x in candidate:
                if 7<=x[0]<10 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
    else:
        if team == 'b':
            for x in candidate:
                if 7<=x[0]<10 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            for x in candidate:
                if 0<=x[0]<3 and 3<=x[1]<6:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
    return cells    


# this is the class that return list of valid move of CANON (PHAO)
def canMoveCanon(board,position,upSidedown):
    cells=[]
    i = position[0]
    j = position[1]
    team = board[position[0]][position[1]][0]
    for x in range(i+1,10):
        if board[x][j] == '---':
            cells += [(x,j)]
        else: #meet the stone
            for y in range(x +1,10):
                if board[y][j][0] != team and board[y][j] != '---':
                    cells += [(y,j)]
                    break
                if board[y][j][0] == team:
                    break
            break
    for x in range(i-1,-1,-1):
        if board[x][j] == '---' :
            cells += [(x,j)]
        else: 
            for y in range(x-1,-1,-1):
                if board[y][j][0] != team and board[y][j] != '---':
                    cells += [(y,j)]
                    break
                if board[y][j][0] == team:
                    break
            break
    for y in range(j+1,9):
        if board[i][y] =='---' :
            cells += [(i,y)]
        else:
            for x in range(y+1,9):
                if board[i][x][0] != team and board[i][x] != '---':
                    cells += [(i,x)]
                    break
                if board[i][x][0] == team:
                    break
            break
    for y in range(j-1,-1,-1):
        if board[i][y] =='---' :
            cells += [(i,y)]
        else: 
            for x in range(y-1,-1,-1):
                if board[i][x][0] != team and board[i][x] != '---':
                    cells += [(i,x)]
                    break
                if board[i][x][0] == team:
                    break
            break
    return cells


# this is the class that return list of valid move of SOLDIER (TOT)
def canMoveSoldier(board,position,upSideDown):
    cells=[]
    i = position[0]
    j = position[1]
    team = board[position[0]][position[1]][0]
    
    if not upSideDown:
        if team =='b':
            candidate =[(i+1,j)]
            if i > 4:
                candidate += [(i,j+1),(i,j-1)]
            for x in candidate:
                if 0<=x[0]<10 and 0<=x[1]<9:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]                     #[(),(),(),()]
        else:
            candidate = [(i-1,j)]
            if i<5:
                candidate += [(i,j+1),(i,j-1)]
            for x in candidate:
                if 0<=x[0]<10 and 0<=x[1]<9:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
    else:
        if team =='b':
            candidate =[(i-1,j)]
            if i < 5:
                candidate += [(i,j+1),(i,j-1)]
            for x in candidate:
                if 0<=x[0]<10 and 0<=x[1]<9:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
        else:
            candidate = [(i+1,j)]
            if i>4:
                candidate += [(i,j+1),(i,j-1)]
            for x in candidate:
                if 0<=x[0]<10 and 0<=x[1]<9:
                    if board[x[0]][x[1]][0] != team:
                        cells += [x]
    return cells


#cells list of two tuple [[(),()],...]
def RuleMove(board, position, upsidedown):  #(), upsidedown is after
    chessType = board[position[0]][position[1]][1:]
    cells= []
    if chessType == 'xe':
        cells = canMoveCar(board, position, upsidedown)
    elif chessType == 'ma':
        cells = canMoveHorse(board, position, upsidedown)
    elif chessType == 'ph':
        cells = canMoveCanon(board, position, upsidedown)
    elif chessType == 'tu':
        cells = canMoveKing(board, position, upsidedown)
    elif chessType == 'si':
        cells = canMoveAdvisor(board, position, upsidedown)
    elif chessType == 'ch':
        cells = canMoveSoldier(board, position, upsidedown)
    elif chessType == 'vo':
        cells = canMoveElephant(board, position, upsidedown)
    return cells
 


# this is the class that return list of valid move with some rules of this game 
def validMove(board, turn, after):
    flag = False
    bk =()
    rk= ()
    
    for i in range(0,3):
        for j in range(3,6):
            if board[i][j][1:] == 'tu':
                bk= (i,j) 
    for i in range(7,10):
        for j in range(3,6):
            if board[i][j][1:] == 'tu':
                rk = (i,j)
    if after:
        bk, rk = rk, bk
    if bk[1] == rk[1]:
        for i in range(bk[0]+1,rk[0]+1):
            if board[i][bk[1]] == '---':
                continue
            elif board[i][bk[1]][1:] == 'tu':
                flag = True
                break
            else:
                break
        if flag:
            return False
    if isThreaten(board, bk, rk, not turn, after):
        return False
    return True
    
    
    # check it later


# this is the function check if the king is threatened
def isThreaten(board, bk, rk, turn, after):
    # turn of red, so check if the red king is threatened
    x = bk[0]
    y = bk[1]
    team = 'b' 
    
    if not turn:
        x = rk[0]
        y = rk[1]
        team = 'r' 
    # check if a horse is threatening the king
    ma =[]
    for row in range(10):
        for col in range(9):
            if board[row][col][1:] == 'ma' and board[row][col][0] != team:
                ma += [(row,col)]
    if ma != []:
        candidate = [(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1)]
        for i in ma:
            if i in candidate:
                maChien = canMoveHorse(board, (i[0],i[1]), after)
                if (x,y) in maChien:
                    #print("The king is threatened by a horse")
                    return True
    # check if a car is threatening the king
    xe = []
    for row in range(10):
        for col in range(9):
            if board[row][col][1:] == 'xe' and board[row][col][0] != team:
                xe += [(row,col)]
    if xe != []:
        for i in xe:
            if i[0] == x:
                if i[1] < y:
                    for j in range(i[1],y):
                        if j == y-1:
                            #print("The king is threatened by a car")
                            return True
                        if board[x][j+1] != '---':
                            break
                if i[1] > y:
                    for j in range(y,i[1]):
                        if j == i[1]-1:
                            #print("The king is threatened by a car")
                            return True
                        if board[x][j+1] != '---':
                            break
            if i[1] == y:
                if i[0] < x:
                    for j in range(i[0],x):
                        if j == x-1:
                            #print("The king is threatened by a car")
                            return True
                        if board[j+1][y] != '---':
                            break
                if i[0] > x:
                    for j in range(x,i[0]):
                        if j == i[0]-1:
                            #print("The king is threatened by a car")
                            return True
                        if board[j+1][y] != '---':
                            break
    
    # check if a king is theatening by a canon
    phao = []
    for row in range(10):
        for col in range(9):
            if board[row][col][1:] == 'ph' and board[row][col][0] != team:
                phao += [(row,col)]
    if phao != []:
        stayaway = [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        candidate = [(a,y) for a in range(10) if (a,y) not in stayaway ] + [(x,b) for b in range(9) if (x,b) not in stayaway ]

        for i in phao:
            if i in candidate:
                phaoLenNong = canMoveCanon(board, i, after)
                if (x,y) in phaoLenNong:
                    #print("The king is threatened by a canon")
                    return True
    # check if a king is threatened by a soldier
    tot = []
    for row in range(10):
        for col in range(9):
            if board[row][col][1:] == 'ch' and board[row][col][0] != team:
                tot += [(row,col)]
    if tot != []:
        candidate = [(x,y+1),(x,y-1)] + ([(x-1,y)] if team == 'r' else [(x+1,y)])
        for i in tot:
            if i in candidate:
                totChien = canMoveSoldier(board, i, after)
                if (x,y) in totChien:
                    ##print("The king is threatened by a soldier")
                    return True
    return False
    

    



  
    
  
# class ChessMan():
#     power = 10
    
    
#     def canMove(self,board,position,upSideDown):
#         cells =[]
#         team = board[position[0]][position[1]][0]
#         i = position[0]
#         j = position[1]

#         for x in range(i+1,10):
#             if board[x][j] == '---':
#                 cells += [(x,j)]
            
#             elif board[x][j][0] != team:
#                 cells += [(x,j)]
#                 break
#             else: break
#         for x in range(i-1,-1,-1):
#             if board[x][j] == '---':
#                 cells += [(x,j)]
#             elif board[x][j][0] != team:
#                 cells += [(x,j)]
#                 break
#             else: break
#         for y in range(j+1,9):
#             if board[i][y] =='---':
#                 cells += [(i,y)]
#             elif board[i][y][0] != team:
#                 cells += [(i,y)]
#                 break
#             else: break
#         for y in range(j-1,-1,-1):
#             if board[i][y] =='---':
#                 cells += [(i,y)]
#             elif board[i][y][0] != team:
#                 cells += [(i,y)]
#                 break
#             else: break
#         return cells
#     def __str__(self):
#         return "XE"
# class Ma(AbstractChess):
#     power = 7
#     def canMove(self,board,position,upSideDown):
#         cells =[]
#         team = board[position[0]][position[1]][0]
#         nowRow = position[0]
#         nowCol = position[1]
#         if nowCol +1 <9:
#             if board[nowRow][nowCol+1]=='---':
#                 if nowCol+2 < 9 and nowRow+1 < 10 and (board[nowRow+1][nowCol+2] == '---' or board[nowRow+1][nowCol+2][0] != team):
#                     cells += [(nowRow+1,nowCol+2)]
#                 if nowCol+2 < 9 and nowRow-1 >= 0 and (board[nowRow-1][nowCol+2] == '---' or board[nowRow-1][nowCol+2][0] != team):
#                     cells += [(nowRow-1,nowCol+2)]
#         if nowCol -1 >=0:
#             if board[nowRow][nowCol-1]=='---':
#                 if nowCol-2 >= 0 and nowRow+1 < 10 and (board[nowRow+1][nowCol-2] == '---' or board[nowRow+1][nowCol-2][0] != team):
#                     cells += [(nowRow+1,nowCol-2)]

#                 if nowCol-2 >= 0 and nowRow-1 >= 0 and (board[nowRow-1][nowCol-2] == '---' or board[nowRow-1][nowCol-2][0] != team):
#                     cells += [(nowRow-1,nowCol-2)]
#         if nowRow +1 <10:
#             if board[nowRow+1][nowCol]=='---':
#                 if nowCol+1 < 9 and nowRow+2 < 10 and (board[nowRow+2][nowCol+1] == '---' or board[nowRow+2][nowCol+1][0] != team):
#                     cells += [(nowRow+2,nowCol+1)]

#                 if nowCol-1 >= 0 and nowRow+2 < 10 and (board[nowRow+2][nowCol-1] == '---' or board[nowRow+2][nowCol-1][0] != team):
#                     cells += [(nowRow+2,nowCol-1)]
#         if nowRow -1 >=0:
#             if board[nowRow-1][nowCol]=='---':
#                 if nowCol+1 < 9 and nowRow-2 >= 0 and (board[nowRow-2][nowCol+1] == '---' or board[nowRow-2][nowCol+1][0] != team):
#                     cells += [(nowRow-2,nowCol+1)]
#                 if nowCol-1 >= 0 and nowRow-2 >= 0 and (board[nowRow-2][nowCol-1] == '---' or board[nowRow-2][nowCol-1][0] != team):
#                     cells += [(nowRow-2,nowCol-1)]
#         return cells
#     def __str__(self):
#         return "MA"
# class Voi(AbstractChess):
#     power = 2
#     def canMove(self,board,position,upSideDown):
#         cells =[]
#         team = board[position[0]][position[1]][0]
#         i = position[0]
#         j = position[1]
#         candidate = [(i+2,j+2),(i+2,j-2),(i-2,j+2),(i-2,j-2)]
#         if not upSideDown:
#             if team == 'b':
#                 for x in candidate:
#                     if 0<=x[0]<5 and 0<=x[1]<10:
#                         if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 for x in candidate:
#                     if 4<x[0]<10 and 0<=x[1]<10:
#                         if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         else:
#             if team == 'b':
#                 for x in candidate:
#                     if 5<=x[0]<10 and 0<=x[1]<10:
#                         if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 for x in candidate:
#                     if 0<=x[0]<6 and 0<=x[1]<10:
#                         if board[int((i+x[0])/2)][int((j+x[1])/2)]=='---' and board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         return cells
#     def __str__(self):
#         return "VOI"
# class Si(AbstractChess):
#     power = 1
#     def canMove(self,board,position,upSideDown):
#         cells=[]
#         i = position[0]
#         j = position[1]
#         team = board[position[0]][position[1]][0]
#         candidate = [(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
#         if not upSideDown:
#             if team == 'b':
#                 for x in candidate:
#                     if 0<=x[0]<3 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
                
#                 for x in candidate:
#                     if 7<=x[0]<10 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         else:
#             if team == 'b':
#                 for x in candidate:
#                     if 7<=x[0]<10 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 for x in candidate:
#                     if 0<=x[0]<3 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         return cells
#     def __str__(self):
#         return "SI"
# class Tuong(AbstractChess):
#     power = 100
#     def canMove(self,board,position,upSideDown):
#         cells=[]
#         i = position[0]
#         j = position[1]
#         team = board[position[0]][position[1]][0]
#         candidate = [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]
#         if not upSideDown:
#             if team == 'b':
#                 for x in candidate:
#                     if 0<=x[0]<3 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 for x in candidate:
#                     if 7<=x[0]<10 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         else:
#             if team == 'b':
#                 for x in candidate:
#                     if 7<=x[0]<10 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 for x in candidate:
#                     if 0<=x[0]<3 and 3<=x[1]<6:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         return cells    
#     def __str__(self):
#         return "TUONGs"
# class Phao(AbstractChess):
#     power = 7
#     def canMove(self,board,position,upSidedown):
#         cells=[]
#         i = position[0]
#         j = position[1]
#         team = board[position[0]][position[1]][0]
#         for x in range(i+1,10):
#             if board[x][j] == '---':
#                 cells += [(x,j)]
#             else: #meet the stone
#                 for y in range(x +1,10):
#                     if board[y][j][0] != team and board[y][j] != '---':
#                         cells += [(y,j)]
#                         break
#                     if board[y][j][0] == team:
#                         break
#                 break
#         for x in range(i-1,-1,-1):
#             if board[x][j] == '---' :
#                 cells += [(x,j)]
#             else: 
#                 for y in range(x-1,-1,-1):
#                     if board[y][j][0] != team and board[y][j] != '---':
#                         cells += [(y,j)]
#                         break
#                     if board[y][j][0] == team:
#                         break
#                 break
#         for y in range(j+1,9):
#             if board[i][y] =='---' :
#                 cells += [(i,y)]
#             else:
#                 for x in range(y+1,9):
#                     if board[i][x][0] != team and board[i][x] != '---':
#                         cells += [(i,x)]
#                         break
#                     if board[i][x][0] == team:
#                         break
#                 break
#         for y in range(j-1,-1,-1):
#             if board[i][y] =='---' :
#                 cells += [(i,y)]
#             else: 
#                 for x in range(y-1,-1,-1):
#                     if board[i][x][0] != team and board[i][x] != '---':
#                         cells += [(i,x)]
#                         break
#                     if board[i][x][0] == team:
#                         break
#                 break
#         return cells
#     def __str__(self):
#         return "PHAO"
# class Chot(AbstractChess):
#     power = 2
#     position =[
#         [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
#         [0.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  0.0],
#         [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,  0.0],
#         [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,  0.0],
#         [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,  0.0],
#         [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,  0.0],
#         [0.5,  0.0,  1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0],
#         [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
#         [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
#         [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
#     ]
#     def canMove(self,board,position,upSideDown):
#         cells=[]
#         i = position[0]
#         j = position[1]
#         team = board[position[0]][position[1]][0]
        
#         if not upSideDown:
#             if team =='b':
#                 candidate =[(i+1,j)]
#                 if i > 4:
#                     candidate += [(i,j+1),(i,j-1)]
#                 for x in candidate:
#                     if 0<=x[0]<10 and 0<=x[1]<9:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 candidate = [(i-1,j)]
#                 if i<5:
#                     candidate += [(i,j+1),(i,j-1)]
#                 for x in candidate:
#                     if 0<=x[0]<10 and 0<=x[1]<9:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         else:
#             if team =='b':
#                 candidate =[(i-1,j)]
#                 if i < 5:
#                     candidate += [(i,j+1),(i,j-1)]
#                 for x in candidate:
#                     if 0<=x[0]<10 and 0<=x[1]<9:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#             else:
#                 candidate = [(i+1,j)]
#                 if i>4:
#                     candidate += [(i,j+1),(i,j-1)]
#                 for x in candidate:
#                     if 0<=x[0]<10 and 0<=x[1]<9:
#                         if board[x[0]][x[1]][0] != team:
#                             cells += [x]
#         return cells
#     def __str__(self):
#         return "CHOT"
    
# class Empty(AbstractChess):
#     def canMove(self,board,position,upSideDown):
#         return []   
#     def __str__(self):
#         return "EMPTY"


