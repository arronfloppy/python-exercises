""" The set cover is a NP-complete problem
From wikipedia:
Given a set of elements {1, 2, …, n} (called the universe) and a collection S of m sets whose union equals the universe,
 the set cover problem is to identify the smallest sub-collection of S whose union equals the universe.
  For example, consider the universe U = {1, 2, 3, 4, 5} and the collection of sets S = { {1, 2, 3}, {2, 4}, {3, 4}, {4, 5} }. 
  Clearly the union of S is U. However, we can cover all of the elements with the following, smaller number of sets: { {1, 2, 3}, {4, 5} }.
 """


def set_cover_greedy(universe, setCollection, checkUnion = False):
    """ universe - a set of elements to cover. setCollection - collection S of m sets whose union equals the universe
    returns  the smallest sub-collection of S whose union equals the universe..
    This is a greedy implementation (aproximation)"""

    elementsToCover = set(universe)
    elementsCovered = set()
    setList = []

    while elementsToCover:
        eltsCovered = set()
        bestSetName = ""
        for setName,elts in setCollection.items():
            setElts = set(elts)
            newEltsCovered = elementsToCover & setElts
            if len(eltsCovered) < len(newEltsCovered):
                eltsCovered = newEltsCovered
                bestSetName = setName
        if(eltsCovered):
            elementsToCover = elementsToCover - eltsCovered
            setList.append(bestSetName)
        else:
            break

    return setList





