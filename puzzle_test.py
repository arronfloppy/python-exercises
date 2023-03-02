from puzzle import *

state1 = State([["2", "1", "4"],
                 ["3", None, "5"],
                 ["6","7","8"]] )

state2 = State([["3", "1", "2"],
                 [None,"6", "4"],
                 ["7","8","5"]])

puzzle = Puzzle(state2,20)
puzzle.findSolution()
   