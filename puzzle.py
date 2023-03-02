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

    def getCellDistance(self,cellPos,anotherCell):
        rowIdx,colIdx = cellPos
        anRowIdx,anColIdx = anotherCell
        distance = abs(anRowIdx - rowIdx) + abs(anColIdx - colIdx)
        return distance

    def getDistance(self,anotherState):
        distance = 0
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                     (anRowIdx,anColIdx) = anotherState.cellDict[cell]
                     distance += self.getCellDistance( (rowIdx,colIdx), (anRowIdx,anColIdx))
        return distance
    
    def equals(self, anotherState):
        if not anotherState:
            return False
        if self.getDistance(anotherState) == 0:
            return True
        else:
            return False
        
    
    def getLegalMoves(self):
        moves = []
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                    if rowIdx > 0 and not self.rowList[rowIdx -1][colIdx]:
                        moves.append((cell,rowIdx-1,colIdx))
                    elif rowIdx < len(row) -1 and not self.rowList[rowIdx+1][colIdx]:
                        moves.append((cell,rowIdx+1,colIdx))
                    elif colIdx > 0 and not self.rowList[rowIdx][colIdx-1]:
                         moves.append((cell,rowIdx,colIdx-1))
                    elif colIdx < len(self.rowList) -1  and not self.rowList[rowIdx][colIdx+1]:
                         moves.append((cell,rowIdx,colIdx+1))
                       
        return moves

    def moveTo(self,newPos):
        cellVal, row, col = newPos
        actualValue = self.rowList[row][col]
        if actualValue:
            raise Exception("Could not move " + cellVal + " to "+ str(row) +"," +str(col) + \
                " ! Already filled with: " + actualValue)
        newState = copy.deepcopy(self)
        (actRow, actCol) = newState.cellDict[cellVal]
        newState.rowList[actRow][actCol] = None
        newState.rowList[row][col] = cellVal
        newState.cellDict[cellVal] = (row,col)

        return newState



class Puzzle:
     
    def __init__(self, initState , maxSteps = 100):
        self.initState = initState
        self.targetState =  State([[None, "1", "2"],
                    ["3", "4", "5"],
                    ["6","7","8"]] )
        self.currentState = initState
        self.previousState = None
        self.maxSteps = maxSteps

        if len(self.initState.rowList) != len(self.targetState.rowList):
            raise Exception("initState and targetState dims do not match!")
        if not initState:
            raise Exception("initState cannot be null")
        
        self.initDistance = self.currentState.getDistance(self.targetState)
        self.curentDistance = self.initDistance
        
    def evaluate(self):
        legalMoves = self.currentState.getLegalMoves()
        minDistance = float("inf")
        bestState = None
        for move in legalMoves:
            newState = self.currentState.moveTo(move)
            distance = newState.getDistance(self.targetState)
            if newState.equals(self.previousState):
                continue
            if distance < minDistance :
                bestState = newState
                minDistance = distance
        return (bestState,minDistance)
    
    def printState(self):
        print("---------------------")
        for row in self.currentState.rowList:
            print(row)
        print("distance is " + str(self.curentDistance))
    
    def findSolution(self):
        self.printState()
        while not self.currentState.equals(self.targetState) and self.maxSteps > 0:
            print("Step no: " + str(self.maxSteps))
            bestState, minDistance = self.evaluate()
            self.curentDistance = minDistance
            self.previousState = self.currentState
            self.currentState = bestState
            self.printState()
            self.maxSteps -= 1

    






    

