import rule
from copy import deepcopy
import random
import playWithMachine as pwm
class Move:
    ranksToRows = {0:'10',1:'9', 2:'8', 3:'7', 4:'6', 5:'5', 6:'4', 7:'3', 8:'2', 9:'1'}
    ranksToCols = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
    def __init__(self, board, first, second):
        self.board = deepcopy(board)
        self.startRow = first[0]
        self.startCol = first[1]
        self.endRow = second[0]
        self.endCol = second[1]
        self.chessManMoved = board[self.startRow][self.startCol]
        self.chessCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        
    def getChange(self):
        return self.getPosition(self.startRow, self.startCol) +'-->'+ self.getPosition(self.endRow, self.endCol)
    def getPosition(self, row, col):
        return self.ranksToCols[col] + self.ranksToRows[row]
    def __str__(self):
       return self.chessManMoved + ' ' + self.getPosition(self.startRow, self.startCol) +'-->'+ self.getPosition(self.endRow, self.endCol) 

class State:
    def __init__(self):
        self.board= [
            ['bxe','bma','bvo','bsi','btu','bsi','bvo','bma','bxe'],       # b = black
            ['---','---','---','---','---','---','---','---','---'],        # r = red
            ['---','bph','---','---','---','---','---','bph','---'],        # ma = horse
            ['bch','---','bch','---','bch','---','bch','---','bch'],        
            ['---','---','---','---','---','---','---','---','---'],        # ph = cannon
            ['---','---','---','---','---','---','---','---','---'],        # vo = elephant
            ['rch','---','rch','---','rch','---','rch','---','rch'],        # si = advisor
            ['---','rph','---','---','---','---','---','rph','---'],        # ch = soldier
            ['---','---','---','---','---','---','---','---','---'],
            ['rxe','rma','rvo','rsi','rtu','rsi','rvo','rma','rxe']         # tu = king
        ]
            # ['bxe','---','bvo','bsi','btu','bsi','bvo','---','bxe'],       # b = black
            # ['---','---','---','---','---','---','---','---','---'],        # r = red
            # ['bma','bph','---','---','bph','---','bma','---','---'],        # ma = horse
            # ['bch','---','bch','---','bch','---','---','---','bch'],        
            # ['---','---','---','---','---','---','bch','---','---'],        # ph = cannon
            # ['---','---','rch','---','---','---','---','---','---'],        # vo = elephant
            # ['rch','---','---','---','rch','---','rch','---','rch'],        # si = advisor
            # ['---','rph','rma','---','---','---','rma','rph','---'],        # ch = soldier
            # ['---','---','---','---','---','---','---','---','---'],
            # ['rxe','---','rvo','rsi','rtu','rsi','rvo','---','rxe']         # tu = king
        # ]
 
 
 
        self.redMove = True         #  red move is your
        self.after = False          #  after mean when revese the board, the red move belong to machine
        self.moveLog = []           #  store all the move
        self.store =[]              #  store all the move when click remove button
        self.selectedCell = ()      #  store the selected cell
        self.blackKing = (0,4)      #  store the position of black king
        self.redKing = (9,4)        #  store the position of red king
        self.isStart = False        #  check if the game is start


    #---------------------------------
    #   use to reverse the board before playing
    #---------------------------------
    def reverse(self):
        for i in range(10):
            for j in range(9):
                if self.board[i][j][0] == 'r':
                    self.board[i][j] = 'b'+ self.board[i][j][1:]
                elif self.board[i][j][0]== 'b':
                    self.board[i][j] = 'r'+ self.board[i][j][1:]
        self.blackKing, self.redKing = self.redKing, self.blackKing
        self.after = not self.after
        
    #----------------------------------------------------
    #   This method is used to make a move, it requires a move object as a parameter
    #   It returns nothing, but it will change the board and the moveLog
    #----------------------------------------------------
    def makeMove(self, move: Move):
        
        # create a temp board to check if the movement is valid
        tmpBoard = deepcopy(self.board)
        tmpRedMove = self.redMove
        tmpBlackKing,  tmpRedKing  = self.blackKing, self.redKing
       
        
        # update the temp board
        tmpBoard[move.startRow][move.startCol] = '---'              # empty the start cell
        tmpBoard[move.endRow][move.endCol] = move.chessManMoved     # move the chessman to the end cell

        # update king position
        if move.chessManMoved[1:] == 'tu':
            if tmpRedMove:
                tmpRedKing = (move.endRow, move.endCol)             
            else:
                tmpBlackKing = (move.endRow, move.endCol)

        # check if the movement is valid
        if not rule.validMove(tmpBoard, tmpRedMove, self.after):      
            print("Loi mat tuong")
            return False
        else:

            # update state when the movement is valid            
            self.board = deepcopy(tmpBoard)
            self.redKing, self.blackKing  = tmpRedKing, tmpBlackKing    # update the king position

            
            self.moveLog.append(deepcopy(move))                         # update the moveLog
            
            self.redMove = not self.redMove                             # change the turn
            self.store =[]                                              # can't use the nextMove after make a move
            print(move.getChange(),'---', self.blackKing, self.redKing)
            
    #----------------------------------------------------
    #   This method is used to undo a move
    #   It returns nothing, but it will change the board and the moveLog
    #----------------------------------------------------
    def reMoveReal(self):
        self.reMove()
        self.reMove()
    #----------------------------------------------------
    #   This method is used to undo a undo move
    #   It returns nothing, but it will change the board and the moveLog
    #----------------------------------------------------
    def nextMoveReal(self):
        self.nextMove()
        self.nextMove()
        
    #----------------------------------------------------
    #   This method is used to undo a move
    #   It returns nothing, but it will change the board and the moveLog
    #----------------------------------------------------
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

        self.store.append(deepcopy(self.moveLog.pop()))
        self.redMove = not self.redMove
        print(move.getChange(),'---', self.blackKing, self.redKing)

    #----------------------------------------------------
    #   This method is used to undo a undo move
    #   It returns nothing, but it will change the board and the moveLog
    #----------------------------------------------------
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

        self.moveLog.append(deepcopy(self.store.pop()))
        self.redMove = not self.redMove
        print(move.getChange(),'---', self.blackKing, self.redKing)
    
    #----------------------------------------------------
    #   This method is used to check if a chess man on a cell can move to other cells
    #   It returns a list of valid moves
    #----------------------------------------------------
    def checkValid(self, position):
        x = rule.RuleMove(self.board, position, self.after)
        return x
    
    #----------------------------------------------------
    #   This method check if the king is check
    #   It returns true if the king is check
    #----------------------------------------------------
    def checkMate(self):
        # position = (self.moveLog[-1].endRow, self.moveLog[-1].endCol) if len(self.moveLog)>0 else None
        # if position == None: return False
        x = rule.isThreaten(self.board, self.blackKing, self.redKing, not self.redMove, self.after)
        
        return x
        
        
    
    # ----------------------------------------------------
    # we don't use this because it's too slow
    # def getAllValidMove(self):
    #     listValid = []
    #     listValidMove = []
    #      # == true if red
    #     turn = 'r' if self.redMove else 'b'
        
    #     for row in range(10):
    #         for col in range(9):
    #             if self.board[row][col] != '---' and turn == self.board[row][col][0]:
    #                 chessMan = rule.ChessMan(self.board[row][col]).type
    #                 listValid = chessMan.canMove(self.board, (row,col), self.after)
    #                 for cell in listValid:
    #                     #move = Move(self, (row,col), cell)
    #                     move = Move(self.board,(row,col), cell)
    #                     tmpBoard = deepcopy(self.board)
    #                     tmpredMove = self.redMove
    #                     #statetmpmoveLog = deepcopy(self.moveLog)
    #                     #statetmpstore = deepcopy(self.store)
                        
                        
    #                     tmpblackKing = self.blackKing
    #                     tmpredKing = self.redKing
                        
    #                     tmpBoard[move.startRow][move.startCol] = '---'
    #                     tmpBoard[move.endRow][move.endCol] = move.chessManMoved

    #                     if move.chessManMoved[1:] == 'tu':
    #                         if tmpredMove:
    #                             tmpredKing = (move.endRow, move.endCol)
    #                         else:
    #                             tmpblackKing = (move.endRow, move.endCol)
    #                     # if move.chessCaptured != '---':
    #                     #     for i in statetmp.listSoldier:
    #                     #         if i.position == (move.endRow, move.endCol) and i.live == True and i.team != turn:
    #                     #             i.live = False
    #                     #             break
    #                     # for i in statetmp.listSoldier:
    #                     #     if i.position == (move.startRow, move.startCol) and i.live == True and i.team == turn:
    #                     #         i.changePos((move.endRow, move.endCol))
    #                     #         break

    #                     if rule.ChessMan.validMove(tmpBoard, tmpblackKing, tmpredKing, tmpredMove, self.after):
    #                         listValidMove.append((deepcopy(move)))
    #     return listValidMove

    
    # ----------------------------------------------------
    # This method check if the game is end
    # It returns a tuple (True/False, 'r'/'b'/'')
    # True if the game is end, False if not
    # 'r' if red win, 'b' if black win, '' if no one win
    # ----------------------------------------------------
    def checkEnd(self):
        if State.getAllValid(self.board, self.redMove, self.after) == []:
            return True, 'b' if self.redMove else 'r'
        return False,""
    
    # ----------------------------------------------------
    # This method is used to evaluate the board
    # we don't use this because it's too slow
    # ----------------------------------------------------
    # def evaluate(self):
    #     e = 0
    #     if self.checkEnd()[0]:    
    #         e += 100000 if (self.checkEnd()[1]=='b' and self.after) or (self.checkEnd()[1]=='r' and not self.after)  else 0
    #         e += -100000 if (self.checkEnd()[1]=='b' and not self.after) or (self.checkEnd()[1]=='r' and self.after)  else 0
    #     # for sold in self.listSoldier:
    #     #     if sold.live:
    #     #         chessMan = rule.ChessMan(self.board[sold.position[0]][sold.position[1]]).type
    #     #         if sold.team == 'r':
    #     #             e += chessMan.power + rule.position[sold.name][sold.position[0]][sold.position[1]]
    #     #         else:
    #     #             e -= (chessMan.power + rule.bposition[sold.name][sold.position[0]][sold.position[1]])
    #     for row in range(10):
    #         for col in range(9):
    #             if self.board[row][col] != '---':
    #                 chessMan = rule.ChessMan(self.board[row][col]).type
    #                 if self.board[row][col][0] == 'r':
    #                     e += chessMan.power + rule.position[self.board[row][col][1:]][row][col]
    #                 else:
    #                     e -= (chessMan.power + rule.bposition[self.board[row][col][1:]][row][col])
        
        
    #     return -e if self.after and self.redMove else (-e if not self.after and not self.redMove else e)
                    
    
    
    # ----------------------------------------------------
    # This method is used to get all valid move
    # ----------------------------------------------------
    @staticmethod
    def getAllValid(board, redMove, after):
        
        listCandidate = []
        listValidMove = []
         # == true if red
        turn = 'r' if redMove else 'b'

        for row in range(10):
            for col in range(9):
                if board[row][col] != '---' and turn == board[row][col][0]:   
                    listCandidate = rule.RuleMove(board, (row,col), after)
                    for cell in listCandidate:
                        
                        move = Move(board, (row,col), cell)
                        
                        tmpBoard = deepcopy(board)
                        tmpredMove = redMove
                        
                        tmpBoard[move.startRow][move.startCol] = '---'
                        tmpBoard[move.endRow][move.endCol] = move.chessManMoved

                        if rule.validMove(tmpBoard, tmpredMove, after):
                            #listValidMove.append((deepcopy(move)))
                            listValidMove.append( [(row,col),cell])
        return listValidMove
    # ----------------------------------------------------
    # This method is used to evaluate the board which is Max is black and Min is red
    # It's used in minimax algorithm
    # ----------------------------------------------------
    @staticmethod
    def evaluate(board, redMove, after, c):
        e = 0
        if State.getAllValid(board, redMove, after) ==[]:    
            return 100000 if after else -100000
        if c >=0:
            power = deepcopy(rule.startPower)
            
        elif c >= 14:
            power = deepcopy(rule.midPower)
            
        else:
            power = deepcopy(rule.endPower)

        for row in range(10):
            for col in range(9):
                if board[row][col] != '---':
                    chessMan = board[row][col][1:]
                    if board[row][col][0] == 'r':
                        e = (e - power[chessMan] - rule.belowPosition[chessMan][row][col]) if not after else (e+power[chessMan] +rule.upperPosition[chessMan][row][col])
                    else:
                        e = e + power[chessMan] + rule.upperPosition[chessMan][row][col] if not after else (e- power[chessMan]-rule.belowPosition[chessMan][row][col])
        return e
# ----------------------------------------------------
# This function use to get the next state (board) after a move
# ----------------------------------------------------
def miniNext(board, redMove, after, m): 
        tmpBoard = deepcopy(board)
        move = deepcopy(m)
        # move = [(a,b), (e,d)]
        chessManMoved = tmpBoard[move[0][0]][move[0][1]] 
        
        tmpBoard[move[0][0]][move[0][1]] = '---'
        tmpBoard[move[1][0]][move[1][1]] = chessManMoved

        return tmpBoard