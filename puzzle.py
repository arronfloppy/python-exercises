from collections import deque
import copy
import random
class State:
    """ object containing the actual state of the board (immutable)"""
    def __init__(self, rowList = []):
        self.hash = None
        self.defRows =  [[None, "1", "2"],
                    ["3", "4", "5"],
                    ["6","7","8"]] 
        # list of rows (list of list of cells)
        if rowList:
            self.rowList = rowList
        else:
            self.rowList = self.defRows
        # the cell dictionary containing cell positions for each cell
        self.cellDict = {}
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                    self.cellDict[cell] = (rowIdx,colIdx)
    def __hash__(self) -> int:
        if self.hash:
            return self.hash
        
        hashStr ="0"
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                    hashStr += cell
                else:
                    hashStr += "0"
        self.hash = int(hashStr)
        
        return self.hash

    def __eq__(self, __o: object) -> bool:
        if not __o:
            return False

        return hash(self) == hash(__o)

    def getCellDistance(self,cellPos,anotherCellPos) -> int:
        """ returns the manhattan distance between 2 cells """
        rowIdx,colIdx = cellPos
        anRowIdx,anColIdx = anotherCellPos
        distance = abs(anRowIdx - rowIdx) + abs(anColIdx - colIdx)
        return distance

    def getDistance(self,anotherState) -> int:
        """ returns the distance between two states """
        distance = 0
        for rowIdx, row in enumerate(self.rowList):
            for colIdx, cell in enumerate(row):
                if cell:
                     (anRowIdx,anColIdx) = anotherState.cellDict[cell]
                     distance += self.getCellDistance( (rowIdx,colIdx), (anRowIdx,anColIdx))
        return distance
    
    def shuffle(self, steps: int):
        """ shuffle this state for steps steps
         return the shuffled state """
        shuffled = self
        generated = {}
        for i in range(steps):
            moves = shuffled.getLegalMoves()
            idx = random.randint(0,len(moves)-1)
            move = moves[idx]
            newState = shuffled.moveTo(move)
            if not generated.get(hash(newState)):
                shuffled = newState
                generated[hash(newState)] = True

        return shuffled


    
    def getLegalMoves(self):
        """ returns the list of legal moves for a state """
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
        """ move this State to the new position newPos.
         Returns the new State object """
        cellVal, row, col = newPos
        actualValue = self.rowList[row][col]
        if actualValue:
            raise Exception("Could not move " + cellVal + " to "+ str(row) +"," +str(col) + \
                " ! Already filled with: " + actualValue)
        newState = copy.deepcopy(self)
        newState.hash = None
        assert len(self.rowList) == len(newState.rowList)
        assert len(self.cellDict) == len(newState.cellDict)
        (actRow, actCol) = newState.cellDict[cellVal]
        newState.rowList[actRow][actCol] = None
        newState.rowList[row][col] = cellVal
        newState.cellDict[cellVal] = (row,col)

        return newState

class Puzzle:
    """ the Puzzle object """
    def __init__(self, initState , maxSteps = 100, maxDepth = 4):
        self.initState = initState
        self.targetState =  State([[None, "1", "2"],
                    ["3", "4", "5"],
                    ["6","7","8"]] )
        
        # the current State of the Board
        self.currentState = initState
        # the previous State of the Board
        self.previousState = None
        # max steps to find the solution
        self.maxSteps = maxSteps
        # max depth to expand nodes for each batch
        self.maxDepth = maxDepth
        # the current step nb
        self.step = 0
        # cache of expanded States
        self.stateDict = {}
        # already searched States dict
        self.searched = {}

        if len(self.initState.rowList) != len(self.targetState.rowList):
            raise Exception("initState and targetState dims do not match!")
        if not initState:
            raise Exception("initState cannot be null")
        
        self.initDistance = self.currentState.getDistance(self.targetState)
        
    def getDistanceToTarget(self):
        return self.currentState.getDistance(self.targetState)
    
    def printState(self):
        print("---------------------")
        if self.step:
            print("Step no: " + str(self.step))
        else:
            print("Initial state:")
        printState(self.currentState)
        print("distance is " + str(self.getDistanceToTarget()))

    def findPaths(self, startState, parents, states, depth: int):
        """ find the best path starting from startState expanding nodes at max depth.
        parents dict contains the result"""
        depth -= 1
        legalMoves = startState.getLegalMoves()

        for move in legalMoves:
            newState = startState.moveTo(move)
            newStateHash = hash(newState)
            newStateVal =  parents.get(newStateHash)
            if newStateVal:
                # already found this newStateVal in the dictionary
                # if the previous depth is smaller then continue
                stateHash, stateDepth = newStateVal
                if stateDepth <  self.maxDepth - depth:
                    continue
            # updating the parent dict
            parents[newStateHash] = (hash(startState), self.maxDepth - depth)
            # updating the State cache
            states[newStateHash] = newState
            if newState == self.targetState:
                return
            if depth > 0:
                # move to the next level
                self.findPaths(newState, parents, states, depth)

        return

        
    def evaluate(self):
        """ the evaluation function using the following heuristic:
         expand maxDepth levels of nodes, calculate the manhattan distance
         from each node to target node and chose the node with minimum distance
         and depth"""
        parentDict = {}
        self.findPaths(self.currentState, parentDict, self.stateDict, self.maxDepth)
        minDistance = float("inf")
        minDepth = float("inf")
        bestState = None

        # find the best State in parentDict
        for stateHash in parentDict.keys():
            state = self.stateDict.get(stateHash) 
            parentState, stateDepth = parentDict[stateHash]
            distance = state.getDistance(self.targetState)
            if not self.searched.get(stateHash):
                if distance < minDistance or (distance == minDistance and stateDepth < minDepth):
                    bestState = state
                    minDistance = distance
                    minDepth = stateDepth
        
        # we found the best State, now rewinding the State history to currentState
        pathState = bestState
        self.searched[hash(bestState)] = bestState
        states = []
        states.append(pathState)
        while pathState:
            parentStateHash, stateDepth = parentDict[hash(pathState)]
            parentState = self.stateDict[hash(parentStateHash)]

            if self.currentState != parentState:
                pathState = parentState
                states.append(pathState)
            else:
                pathState = None

        states.reverse()
       
        return (states,minDistance)
    
    
    def findSolution(self, printState = False):
        """ the main loop """
        if printState:
            self.printState()
        while self.currentState != self.targetState and self.maxSteps >= self.step:
            states, minDistance = self.evaluate()
            if not states:
                break
            if printState:
                print("Starting batch ---------------------")
            for state in states:
                self.currentState = state
                self.step += 1
                if printState:
                    self.printState()
                
        ret = False
        if self.currentState == self.targetState:
            ret = True
        lastDistance = self.getDistanceToTarget()
        return (ret, self.step, len(self.stateDict),self.initDistance, lastDistance)


state1 = State([["2", "1", "4"],
                 ["3", None, "5"],
                 ["6","7","8"]] )

state2 = State([["3", "1", "2"],
                 [None,"6", "4"],
                 ["7","8","5"]])

state3 = State([["7", "5", "8"],
                 ["6", "3","2"],
                 ["4","1",None]])
statedict = {"state1":state1,"state2":state2,"state3":state3}

def printState(state):
    for row in state.rowList:
        print(row)

def status(stat):
    ret, steps, nodes, initDistance, lastDistance = stat
    msg = "Found solution in "
    if not ret:
        msg = "Could not find solution in "
    print(msg + str(steps) + " steps. Expanded " + str(nodes) + \
          " nodes, initial distance: "+ str(initDistance) + ", last distance: " +str(lastDistance))
    return ret
    
def main():
    print("Welcome to 8 Puzzle solver!")
    print("Enter the first row, cell values separated by spaces,\
 None for empty")
    print("or enter the predefined state name")
    print("or s to shuffle")
    print("or q to quit.")
    print("Hit <enter> when ready:")
    end = False
    rowNb = 1
    initState = None
    rows = []
    while not end and rowNb <=3:
        row = input()
        if row == "q":
            print("Bye!")
            return
        elif row == "s":
            state = State()
            initState = state.shuffle(50)
            break
        state = statedict.get(row)
        if state:
            initState = state
            break
        cells = row.split()
        if "None" in cells:
            cells[cells.index("None")] = None
        rows.append(cells)
        rowNb +=1
        print("Enter the " +str(rowNb) + " row, cell values separated by spaces")
    if rows:
        initState = State(rows)

    puzzle = Puzzle(initState,80,15)
    stat = puzzle.findSolution(True)  
     
    status(stat)


if __name__ == "__main__":
    main()





    

