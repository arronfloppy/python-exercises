from recursion import *

def test_fact():
    assert(fact(0) == 0)
    assert(fact(1) == 1)
    assert(fact(5) == 120)
    assert(sum(0) == 0)
    assert(sum(1) == 1)
    assert(sum(4) == 10)