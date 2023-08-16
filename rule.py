from abc import ABC, abstractmethod
from copy import deepcopy
import csv
import chessEngine

class AbstractChess(ABC):
        @abstractmethod
        def canMove(self,board):
            pass
position = {'xe':[], 'ma':[], 'vo':[], 'si':[], 'tu':[], 'ph':[], 'ch':[]}
for i in position.keys():
    name = i+'.csv'
    with open ('C:/Users/OnDoing/ChineseChess/unity/'+name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for r in range(len(row)):
                row[r] = float(row[r])
            position[i] += [row]
bposition = {'xe':[], 'ma':[], 'vo':[], 'si':[], 'tu':[], 'ph':[], 'ch':[]}
for i in position.keys():
    bposition[i] = position[i][::-1]
    
class Xe(AbstractChess):
    power = 10
    
    def canMove(self,board,position,upSideDown):
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
    def __str__(self):
        return "XE"
class Ma(AbstractChess):
    power = 7
    def canMove(self,board,position,upSideDown):
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
    def __str__(self):
        return "MA"
class Voi(AbstractChess):
    power = 2
    def canMove(self,board,position,upSideDown):
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
    def __str__(self):
        return "VOI"
class Si(AbstractChess):
    power = 1
    def canMove(self,board,position,upSideDown):
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
    def __str__(self):
        return "SI"
class Tuong(AbstractChess):
    power = 100
    def canMove(self,board,position,upSideDown):
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
    def __str__(self):
        return "TUONGs"
class Phao(AbstractChess):
    power = 7
    def canMove(self,board,position,upSidedown):
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
    def __str__(self):
        return "PHAO"
class Chot(AbstractChess):
    power = 2
    position =[
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [0.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  0.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,  0.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,  0.0],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,  0.0],
        [0.5,  0.0,  1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]
    def canMove(self,board,position,upSideDown):
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
                            cells += [x]
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
    def __str__(self):
        return "CHOT"
    
class Empty(AbstractChess):
    def canMove(self,board,position,upSideDown):
        return []   
    def __str__(self):
        return "EMPTY"


class ChessMan:
    def __init__(self,name):
        self.name = name[1:]
        self.team = name[0]
        if self.name =='xe':
            self.type = Xe()
        elif self.name == 'ma':
            self.type = Ma()
        elif self.name =='vo':
            self.type = Voi()
        elif self.name == 'si':
            self.type =Si()
        elif self.name == 'tu':
            self.type =Tuong()
        elif self.name =='ph':
            self.type =Phao()
        elif self.name == 'ch':
            self.type =Chot()
        else:
            self.type = Empty()
    @staticmethod
    def validMove(board, bk, rk, turn, after):
        nextBoard = deepcopy(board)        
        flag = False
        if bk[1] == rk[1]:
            for i in range(bk[0]+1,rk[0]+1):
                if nextBoard[i][bk[1]] == '---':
                    continue
                elif nextBoard[i][bk[1]][1:] == 'tu':
                    flag = True
                    break
                else:
                    break
            if flag:
                return False
        if ChessMan.isThreaten(nextBoard, bk, rk, not turn, after):
            return False
        return True
    @staticmethod
    def isThreaten(board, bk, rk, turn, after):
        nextBoard = deepcopy(board)
        #listSoldier = deepcopy(board.listSoldier)
        
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
                if nextBoard[row][col][1:] == 'ma' and nextBoard[row][col][0] != team:
                    ma += [(row,col)]
        if ma != []:
            candidate = [(x+1,y+2),(x+1,y-2),(x-1,y+2),(x-1,y-2),(x+2,y+1),(x+2,y-1),(x-2,y+1),(x-2,y-1)]
            for i in ma:
                if i in candidate:
                    maChien = ChessMan(nextBoard[i[0]][i[1]])
                    if (x,y) in maChien.type.canMove(nextBoard,i,after):
                        print("The king is threatened by a horse")
                        return True
        # check if a car is threatening the king
        xe = []
        for row in range(10):
            for col in range(9):
                if nextBoard[row][col][1:] == 'xe' and nextBoard[row][col][0] != team:
                    xe += [(row,col)]
        if xe != []:
            for i in xe:
                if i[0] == x:
                    if i[1] < y:
                        for j in range(i[1],y):
                            if j == y-1:
                                print("The king is threatened by a car")
                                return True
                            if nextBoard[x][j+1] != '---':
                                break
                    if i[1] > y:
                        for j in range(y,i[1]):
                            if j == i[1]-1:
                                print("The king is threatened by a car")
                                return True
                            if nextBoard[x][j+1] != '---':
                                break
                if i[1] == y:
                    if i[0] < x:
                        for j in range(i[0],x):
                            if j == x-1:
                                print("The king is threatened by a car")
                                return True
                            if nextBoard[j+1][y] != '---':
                                break
                    if i[0] > x:
                        for j in range(x,i[0]):
                            if j == i[0]-1:
                                print("The king is threatened by a car")
                                return True
                            if nextBoard[j+1][y] != '---':
                                break
        
        # check if a king is theatening by a canon
        phao = []
        for row in range(10):
            for col in range(9):
                if nextBoard[row][col][1:] == 'ph' and nextBoard[row][col][0] != team:
                    phao += [(row,col)]
        if phao != []:
            stayaway = [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            candidate = [(x,y) for x in range(10) if (x,y) not in stayaway ] + [(x,y) for y in range(9) if (x,y) not in stayaway ]

            for i in phao:
                if i in candidate:
                    phaoLenNong = ChessMan(nextBoard[i[0]][i[1]])
                    if (x,y) in phaoLenNong.type.canMove(nextBoard,i,False):
                        print("The king is threatened by a canon")
                        return True
        # check if a king is threatened by a soldier
        tot = []
        for row in range(10):
            for col in range(9):
                if nextBoard[row][col][1:] == 'ch' and nextBoard[row][col][0] != team:
                    tot += [(row,col)]
        if tot != []:
            candidate = [(x,y+1),(x,y-1)] + ([(x-1,y)] if team == 'r' else [(x+1,y)])
            for i in tot:
                if i in candidate:
                    totChien = ChessMan(nextBoard[i[0]][i[1]])
                    if (x,y) in totChien.type.canMove(nextBoard,i,after):
                        print("The king is threatened by a soldier")
                        return True
        return False