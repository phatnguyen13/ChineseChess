import rule
from copy import deepcopy
class Move:
    ranksToRows = {0:'10',1:'9', 2:'8', 3:'7', 4:'6', 5:'5', 6:'4', 7:'3', 8:'2', 9:'1'}
    ranksToCols = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
    def __init__(self, gs, first, second):
        self.board = gs.board
        self.startRow = first[0]
        self.startCol = first[1]
        self.endRow = second[0]
        self.endCol = second[1]
        # self.chessManMovedReal = deepcopy(gs.chessMan[self.startRow][self.startCol])
        # self.chessManCapturedReal = deepcopy(gs.chessMan[self.endRow][self.endCol])
        self.chessManMoved = gs.board[self.startRow][self.startCol]
        self.chessCaptured = gs.board[self.endRow][self.endCol]
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        
    def getChange(self):
        return self.getPosition(self.startRow, self.startCol) +'-->'+ self.getPosition(self.endRow, self.endCol)
    def getPosition(self, row, col):
        return self.ranksToCols[col] + self.ranksToRows[row]
class Soldier:
    def __init__(self, team, position, name):
        self.team = team
        self.position = position
        self.name = name
        self.live = True
        
    def changePos(self, position):
        self.position = position
    def __str__(self):
        return self.name + '(' + self.team + ')' + ' at ' + str(self.position) + ' is live: ' + str(self.live)
        

class State:
    def __init__(self):
        self.board=[
            ['bxe','bma','bvo','bsi','btu','bsi','bvo','bma','bxe'],
            ['---','---','---','---','---','---','---','---','---'],
            ['---','bph','---','---','---','---','---','bph','---'],
            ['bch','---','bch','---','bch','---','bch','---','bch'],
            ['---','---','---','---','---','---','---','---','---'],
            ['---','---','---','---','---','---','---','---','---'],
            ['rch','---','rch','---','rch','---','rch','---','rch'],
            ['---','rph','---','---','---','---','---','rph','---'],
            ['---','---','---','---','---','---','---','---','---'],
            ['rxe','rma','rvo','rsi','rtu','rsi','rvo','rma','rxe']
        ]
        # self.chessMan = [[rule.ChessMan(self.board[i][j],(i,j)) if self.board[i][j]!='---' else None for j in range(9)] for i in range(10)]
        # self.chessMan = [[rule.ChessMan('---') for _ in range(8)] for _ in range(9)]
        # for i in range(10):
        #     for j in range(9):
        #         self.chessMan[i][j] = rule.ChessMan(self.board[i][j])
                
        self.redMove = True
        self.moveLog = []
        self.store =[]
        self.selectedCell = ()
        self.blackKing = (0,4)
        self.redKing = (9,4)
        # self.blackCar = [(0,0),(0,8)]
        # self.redCar = [(9,0),(9,9)]
        # self.blackHorse = [(0,1),(0,7)]
        # self.redHorse = [(9,1),(9,7)]
        # self.blackElephant = [(0,2),(0,6)]
        # self.redElephant = [(9,2),(9,6)]
        # self.blackAdvisor = [(0,3),(0,5)]
        # self.redAdvisor = [(9,3),(9,5)]
        # self.blackSoldier = [(3,0),(3,2),(3,4),(3,6),(3,8)]
        # self.redSoldier = [(6,0),(6,2),(6,4),(6,6),(6,8)]
        # self.blackCannon = [(2,1),(2,7)]
        # self.redCannon = [(7,1),(7,7)]
        self.listSoldier = []
        for i in range(10):
            for j in range(9):
                value = self.board[i][j]
                if value != '---':
                    soldier = Soldier(value[0], (i,j), value[1:])
                    self.listSoldier.append(soldier)
        
        # for i in range(10):
        #     for j in range(9):
        #         if self.board[i][j] != '---':
        #             self.chessMan[i][j] = rule.ChessMan(self.board[i][j],(i,j))
    def makeMove(self, move: Move):
        statetmp = State()
        statetmp.board = deepcopy(self.board)
        statetmp.redMove = self.redMove
        statetmp.moveLog = deepcopy(self.moveLog)
        statetmp.store = deepcopy(self.store)
        statetmp.listSoldier = deepcopy(self.listSoldier)
        statetmp.blackKing = self.blackKing
        statetmp.redKing = self.redKing

        statetmp.board[move.startRow][move.startCol] = '---'
        statetmp.board[move.endRow][move.endCol] = move.chessManMoved

        if move.chessManMoved[1:] == 'tu':
            if statetmp.redMove:
                statetmp.redKing = (move.endRow, move.endCol)
            else:
                statetmp.blackKing = (move.endRow, move.endCol)
        if move.chessCaptured != '---':
            for i in statetmp.listSoldier:
                if i.position == (move.endRow, move.endCol):
                    i.live = False
                    break
        for i in statetmp.listSoldier:
            if i.position == (move.startRow, move.startCol):
                i.changePos((move.endRow, move.endCol))
                break

            
        if not rule.ChessMan.validMove(statetmp):
            print("Loi mat tuong")
            return False
        else:
            # self.board[move.startRow][move.startCol] = '---'
            # self.board[move.endRow][move.endCol] = move.chessManMoved
            # if move.chessManMoved[1:] == 'tu':
            #     if self.redMove:
            #         self.redKing = (move.endRow, move.endCol)
            #     else:
            #         self.blackKing = (move.endRow, move.endCol)
            
            self.board = statetmp.board
    
            self.redKing = statetmp.redKing
    
            self.blackKing = statetmp.blackKing
            
            turn = 'r' if self.redMove else 'b'
            
            if move.chessCaptured != '---':
                for i in self.listSoldier:
                    if i.position == (move.endRow, move.endCol) and i.live == True and i.team != turn : 
                        i.live = False
                        break
                
            for i in self.listSoldier:
                if i.position == (move.startRow, move.startCol) and i.live == True and i.team == turn:
                    i.changePos((move.endRow, move.endCol))
                    break
                       
            # del self.chessMan[move.startRow][move.startCol]
            # self.chessMan[move.endRow][move.endCol] = deepcopy(move.chessManMovedReal)
            self.moveLog.append(deepcopy(move))
            self.redMove = not self.redMove
            self.store =[]            
            print(move.getChange(),'---', self.blackKing, self.redKing)
        for i in self.listSoldier:
            print(i)
    def reMove(self):
        
        if len(self.moveLog) == 0:
            return
        move = deepcopy(self.moveLog[-1]) #g6h8
        self.board[move.startRow][move.startCol] = move.chessManMoved
        self.board[move.endRow][move.endCol] = move.chessCaptured
        turn = 'r'if self.redMove else 'b' # == true if red 
        
        if move.chessManMoved[1:] == 'tu':
            if self.redMove:
                self.blackKing = (move.startRow, move.startCol)
            else:
                self.redKing = (move.startRow, move.startCol)
        # ban lai su song
        if move.chessCaptured != '---' :
            for i in self.listSoldier:
                if i.position == (move.endRow, move.endCol) and i.live == False and i.team == turn :
                    i.live = True
                    break
        for i in self.listSoldier:
            if i.position == (move.endRow, move.endCol) and i.live == True and i.team != turn:
                i.changePos((move.startRow, move.startCol))
                break 
        # print(move.startRow,'-',move.startCol,'->',move.endRow,'-',move.endCol)
        # self.chessMan[move.startRow][move.startCol] = deepcopy(move.chessManMovedReal)
        # self.chessMan[move.endRow][move.endCol] = deepcopy(move.chessManCapturedReal)
        self.store.append(deepcopy(self.moveLog.pop()))
        self.redMove = not self.redMove
        print(move.getChange(),'---', self.blackKing, self.redKing)
        for i in self.listSoldier:
            print(i)
        
    def nextMove(self):
        if len(self.store) == 0:
            return
        move = deepcopy(self.store[-1])
        self.board[move.startRow][move.startCol] = '---'
        self.board[move.endRow][move.endCol] = move.chessManMoved
        turn = 'r'if self.redMove else 'b' # == true if red
        if move.chessManMoved[1:] == 'tu':
            if self.redMove:
                self.redKing = (move.endRow, move.endCol)
            else:
                self.blackKing = (move.endRow, move.endCol)
        if move.chessCaptured != '---':
            for i in self.listSoldier:
                if i.position == (move.endRow, move.endCol) and i.live == True and i.team != turn : 
                    i.live = False
                    break
        for i in self.listSoldier:
            if i.position == (move.startRow, move.startCol) and i.live == True and i.team == turn:
                i.changePos((move.endRow, move.endCol))
                break

        self.moveLog.append(deepcopy(self.store.pop()))
        self.redMove = not self.redMove
        print(move.getChange(),'---', self.blackKing, self.redKing)
        
    def checkValid(self, position):
        x = rule.ChessMan(self.board[position[0]][position[1]])
        return x.type.canMove(self.board, position)
    
    def checkMate(self):
        position = (self.moveLog[-1].endRow, self.moveLog[-1].endCol)if len(self.moveLog)>0 else None
        if position == None: return False
        chessMan = rule.ChessMan(self.board[position[0]][position[1]]).type
        listValid = self.checkValid(position)
        turn = not self.redMove    # ==true if red turn
        if isinstance(chessMan, (rule.Xe, rule.Ma, rule.Chot, rule.Phao)):
            
            #  chess mate directly
            for i in listValid:
                if self.board[i[0]][i[1]][1:] =='tu':
                    if turn and self.board[i[0]][i[1]][0] =='b':
                        return True
                    elif not turn and self.board[i[0]][i[1]][0] =='r':
                        return True
            #  chess mate by other chessMan
            else:
                pass
        
        
        return False