from knapsack import *

def test_knapsack_greedy():
    # using a dict with name = itemName and value =( itemWeight, itemValue)
    food = {"chips":(1,1), "baguette":(1,2), "salad":(2,2), "burger":(3,2), "hotdog":(4,3), "banana":(6,4) }

    result1 = knapsack_greedy(4,food)
    result2 = knapsack_greedy(5,food)
    result3 = knapsack_greedy(6,food)
    result4 = knapsack_greedy(7,food)

    result = ""

