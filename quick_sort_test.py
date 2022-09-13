


from quick_sort import quick_sort


def test_quick_sort():
    assert quick_sort([1,5,3,4]) == [1,3,4,5]
    assert quick_sort([1,2,5,3,4,3,9]) == [1,2,3,4,5,9]
    assert quick_sort([9,8,5,3,4,6,2]) == [2,3,4,5,6,8,9]
    assert quick_sort([1,5]) == [1,5]
    assert quick_sort([5,1]) == [1,5]
    assert quick_sort([9,8,5,1,4,6,2]) == [1,2,4,5,6,8,9]