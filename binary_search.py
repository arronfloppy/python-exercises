

def binary_search(list, item):
    """ binary search function it searches item in list returns the index or None
Complexity is O(log n) where n is the length of the list"""
    start = 0
    end = len(list) -1
    while start <= end:
        mid = (start + end) // 2
        if item == list[mid] :
            return mid
        elif item < list[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return None