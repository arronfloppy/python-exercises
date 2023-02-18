from knapsack import *

# using a dict with key = itemName and value =( itemWeight, itemValue)
food = {"chips":(1,1), "baguette":(1,2), "salad":(2,2), "burger":(3,3),
     "hotdog":(4,4), "banana":(6,4) }

def test_knapsack():

    for weight in range(1, 17):
        (itemsgr, weightgr, value1gr) = knapsack_greedy(weight,food)
        assert len(itemsgr) > 0
        assert weightgr <= weight
        assert value1gr > 0
        (itemsdp, weightdp, value1dp) = knapsack_dp(weight,food)
        assert len(itemsdp) > 0
        assert weightdp <= weight
        assert value1dp > 0
        # dynamic programming version is almost always better than greedy version
        assert value1dp >= value1gr
   