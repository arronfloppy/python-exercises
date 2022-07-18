


from binary_search import binary_search


def test_binary_search():
    assert binary_search([1,3,6,8,9,10],3) == 1
    assert binary_search([1,3,6,8,9,10],10) == 5
    assert binary_search([1,3,6,8,9,10],1) == 0
    assert binary_search([1,3,6,8,9,10],9) == 4
    assert binary_search([1,3,6,8,9,10],7) == None
    assert binary_search(list(range(100)),7) == 7
    assert binary_search(list(range(10000)),9999) == 9999