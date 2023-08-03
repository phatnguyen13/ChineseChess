from abc import ABC, abstractmethod
class ChessMan:
    def __init__(self,name):
        self.name = name[1:]
        self.team = name[0]
        if self.name =='xe':
            self.type = self.Xe()
        elif self.name == 'ma':
            self.type = self.Ma()
        elif self.name =='vo':
            self.type = self.Voi()
        elif self.name == 'si':
            self.type =self.Si()
        elif self.name == 'tu':
            self.type =self.Tuong()
        elif self.name =='ph':
            self.type =self.Phao()
        elif self.name == 'ch':
            self.type =self.Chot()
        else:
            self.type = self.Empty()
    class AbstractChess(ABC):
        @abstractmethod
        def canMove(self,board):
            pass
    class Xe(AbstractChess):
        def canMove(self,board,position):
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
        def canMove(self,board,position):
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
        def canMove(self,board,position):
            cells =[]
            team = board[position[0]][position[1]][0]
            i = position[0]
            j = position[1]
            candidate = [(i+2,j+2),(i+2,j-2),(i-2,j+2),(i-2,j-2)]
            
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
            return cells
        def __str__(self):
            return "VOI"
    class Si(AbstractChess):
        def canMove(self,board,position):
            cells=[]
            i = position[0]
            j = position[1]
            team = board[position[0]][position[1]][0]
            if team == 'b':
                candidate = [(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
                for x in candidate:
                    if 0<=x[0]<3 and 3<=x[1]<6:
                        if board[x[0]][x[1]][0] != team:
                            cells += [x]
            else:
                candidate = [(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)]
                for x in candidate:
                    if 7<=x[0]<10 and 3<=x[1]<6:
                        if board[x[0]][x[1]][0] != team:
                            cells += [x]
            return cells
        def __str__(self):
            return "SI"
    class Tuong(AbstractChess):
        def canMove(self,board,position):
            cells=[]
            i = position[0]
            j = position[1]
            team = board[position[0]][position[1]][0]
            candidate = [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]
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
            return cells    
        def __str__(self):
            return "TUONGs"
    class Phao(AbstractChess):
        def canMove(self,board,position):
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
                    break
            for x in range(i-1,-1,-1):
                if board[x][j] == '---' and board[x][j][0] != team:
                    cells += [(x,j)]
                else: 
                    for y in range(x-1,-1,-1):
                        if board[y][j][0] != team and board[y][j] != '---':
                            cells += [(y,j)]
                            break
                    break
            for y in range(j+1,9):
                if board[i][y] =='---' and board[i][y][0] != team:
                    cells += [(i,y)]
                else:
                    for x in range(y+1,9):
                        if board[i][x][0] != team and board[i][x] != '---':
                            cells += [(i,x)]
                            break
                    break
            for y in range(j-1,-1,-1):
                if board[i][y] =='---' and board[i][y][0] != team:
                    cells += [(i,y)]
                else: 
                    for x in range(y-1,-1,-1):
                        if board[i][x][0] != team and board[i][x] != '---':
                            cells += [(i,x)]
                            break
                    break
            return cells
        def __str__(self):
            return "PHAO"
    class Chot(AbstractChess):
        def canMove(self,board,position):
            cells=[]
            i = position[0]
            j = position[1]
            team = board[position[0]][position[1]][0]
            
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
            return cells
            
            
        def __str__(self):
            return "CHOT"
    class Empty(AbstractChess):
        def canMove(self,board,position):
            return []   
        def __str__(self):
            return "EMPTY"
            