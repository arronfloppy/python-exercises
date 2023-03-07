from puzzle import *


def test_puzzle():
    """  test method. Depending of init parameters, some of the test cases may fail"""
    for i in range(20):
        state = State()
        state = state.shuffle(15)
        puzzle = Puzzle(state,100,7)
        stat = puzzle.findSolution()
        status(stat)
        ret, steps, nodes, initDistance, lastDistance = stat
        assert lastDistance == 0

   

