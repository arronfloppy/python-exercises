

def quick_sort(items):
    if len(items) < 2:
        return items
    else:
        pivot = len(items) // 2
        less = [ i for i in items if i < items[pivot]]
        great = [ i for i in items if i > items[pivot]]
        return [*quick_sort(less), items[pivot], *quick_sort(great)]