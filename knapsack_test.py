from knapsack import *

# using a dict with key = itemName and value =( itemWeight, itemValue)
food = {"chips":(1,1), "bread":(1,2), "baguette":(1,3), "sandwich" : (2,2), 
 "burger":(3,2), "hotdog":(5,5), "banana":(6,4) }

def test_knapsack():

    for weight in range(1, 17):
        (itemsgr, weightgr, valuegr) = knapsack_greedy(weight,food)
        assert len(itemsgr) > 0
        assert weightgr <= weight
        assert valuegr > 0
        (itemsdp, weightdp, valuedp) = knapsack_dp(weight,food)
        assert len(itemsdp) > 0
        assert weightdp <= weight
        assert valuedp > 0
        # dynamic programming version is almost always better than greedy version
        assert valuedp >= valuegr
   

def test_knapsack_results():

    foodReverse = dict(reversed(food.items()))

    for weight in range(1, 17):
        (itemsgr, weightgr, valuegr) = knapsack_greedy(weight,food)
        assert len(itemsgr) > 0
        assert weightgr <= weight
        assert valuegr > 0
        (itemsgrrev, weightgrrev, valuegrrev) = knapsack_greedy(weight,foodReverse)
        assert len(itemsgrrev) > 0
        assert weightgrrev <= weight
        assert valuegrrev > 0
        itemsgr.sort()
        itemsgrrev.sort()
        #assert  itemsgr == itemsgrrev
        assert weightgr == weightgrrev
        assert valuegr == valuegrrev


        (itemsdp, weightdp, valuedp) = knapsack_dp(weight,food)
        assert len(itemsdp) > 0
        assert weightdp <= weight
        assert valuedp > 0
        (itemsdprev, weightdprev, valuedprev) = knapsack_dp(weight,foodReverse)
        assert len(itemsdp) > 0
        assert weightdprev <= weight
        assert valuedprev > 0
        itemsdp.sort()
        itemsdprev.sort()
        # dynamic programming maximizes value
        # the content may be different
        #assert itemsdp == itemsdprev
        #assert weightdp == weightdprev
        assert valuedp == valuedprev
