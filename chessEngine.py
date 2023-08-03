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
        # for i in range(10):
        #     for j in range(9):
        #         if self.board[i][j] != '---':
        #             self.chessMan[i][j] = rule.ChessMan(self.board[i][j],(i,j))
    def makeMove(self, move: Move):
        self.board[move.startRow][move.startCol] = '---'
        self.board[move.endRow][move.endCol] = move.chessManMoved
        # del self.chessMan[move.startRow][move.startCol]
        
        # self.chessMan[move.endRow][move.endCol] = deepcopy(move.chessManMovedReal)
        
    
        self.moveLog.append(deepcopy(move))
        self.redMove = not self.redMove
        self.store =[]
        print(move.getChange())
        
    def reMove(self):
        
        if len(self.moveLog) == 0:
            return
        move = deepcopy(self.moveLog[-1]) #g6h8
        self.board[move.startRow][move.startCol] = move.chessManMoved
        self.board[move.endRow][move.endCol] = move.chessCaptured
        # print(move.startRow,'-',move.startCol,'->',move.endRow,'-',move.endCol)
        # self.chessMan[move.startRow][move.startCol] = deepcopy(move.chessManMovedReal)
        # self.chessMan[move.endRow][move.endCol] = deepcopy(move.chessManCapturedReal)
        self.store.append(deepcopy(self.moveLog.pop()))
        self.redMove = not self.redMove
        print(move.getChange())
        
    def nextMove(self):
        if len(self.store) == 0:
            return
        move = deepcopy(self.store[-1])
        self.board[move.startRow][move.startCol] = '---'
        self.board[move.endRow][move.endCol] = move.chessManMoved
        self.moveLog.append(deepcopy(self.store.pop()))
        self.redMove = not self.redMove
        print(move.getChange())
        
    def checkValid(self, position):
        x = rule.ChessMan(self.board[position[0]][position[1]])
        return x.type.canMove(self.board, position)