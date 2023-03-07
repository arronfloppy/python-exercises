from set_cover import *

def test_set_cover_greedy():
    #  fully covered set
    U = {1, 2, 3, 4, 5}
    S = { "set1":{1, 2, 3}, "set2" :{2, 4}, "set3":{3, 4}, "set4":{4, 5} }
    assert  ['set1', 'set4'] ==  set_cover_greedy(U, S)

    #  fully covered set
    U = {1, 2, 3, 4, 5, 6}
    S = { "set1":{1, 2, 3}, "set2" :{2, 4}, "set3":{3, 4}, "set4":{4, 5},  "set5":{1, 6} }
    assert  ['set1', 'set4', 'set5'] ==  set_cover_greedy(U, S)

    # partially covered set, 6 is not covered 
    U = {1, 2, 3, 4, 5, 6}
    S = { "set1":{1, 2, 3}, "set2" :{2, 4}, "set3":{3, 4}, "set4":{4, 5} }
    assert  ['set1', 'set4'] ==  set_cover_greedy(U, S)


    