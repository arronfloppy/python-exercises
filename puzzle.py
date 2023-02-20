from collections import deque
import copy

class State:
    def __init__(self, rowList):
        self.rowList = rowList
        self.cellDict = {}
        for rowIdx, row in enumerate(rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                    self.cellDict[cell] = (rowIdx,colIdx)

    def getCellDistance(self,cell,anotherCell):
        rowIdx,colIdx = cell
        anRowIdx,anColIdx = anotherCell
        distance += abs(anRowIdx - rowIdx) + abs(anColIdx - colIdx)
        return distance

    def getDistance(self,anotherState):
        distance = 0
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                     (anRowIdx,anColIdx) = anotherState.cellDict[cell]
                     distance += self.getCellDistance( (rowIdx,colIdx), (anRowIdx,anColIdx))
        return distance
    
    def getLegalMoves(self):
        moves = []
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                    if rowIdx > 0 and not self.rowList[rowIdx -1][colIdx]:
                        moves.append((cell,rowIdx-1,colIdx))
                    elif rowIdx < row.len() -1 and not self.rowList[rowIdx+1][colIdx]:
                        moves.append((cell,rowIdx+1,colIdx))
                    elif colIdx > 0 and not self.rowList[rowIdx][colIdx-1]:
                         moves.append((cell,rowIdx,colIdx-1))
                    elif colIdx < self.rowList.len() -1  and not self.rowList[rowIdx][colIdx+1]:
                         moves.append((cell,rowIdx,colIdx+1))
                       
        return moves

    def moveTo(self,newPos):
        cellVal, row, col = newPos
        actualValue = self.rowList[row][col]
        if actualValue:
            raise Exception("Could not move " + cellVal + " to "+ str(row) +"," +str(col) + \
                " ! Already filled with: " + actualValue)
        self.rowList[row][col] = cellVal
        self.cellDict[cellVal] = (row,col)





class Puzzle:
    defTargetState = State([[None, "1", "2"],
                    ["3", "4", "5"],
                    ["6","7","8"]] )
   
  
    def __init__(self, initState, targetState = defTargetState, maxSteps = 100):
        self.initState = initState
        self.targetState = targetState
        self.currentState = initState
        self.maxSteps = maxSteps

        if self.initState.len() != self.targetState.len():
            raise Exception("initState and targetState dims do not match!")






    

