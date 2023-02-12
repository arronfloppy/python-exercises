

def knapsack_greedy(maxCapacity, items):
    """ Given a set of n items numbered from 1 up to n, each with a weight wi and a value vi,
    along with a maximum weight capacity W maximize ∑(i to n) v*x 

    Using a greedy strategy, putting the most expensive item
    first, the the next most expensive. This is  clearly not an optimal solution.
    For an optimal solution see knapsack_dp

    Parameters
    ----------
    maxCapacity : int
        max knapsack capacity
    items : dict
        available items as { itemName -> str, (itemWeight -> int, itemValue : int)}
    """
   
    def find_most_expensive(items, processed):
         # infinite negative cost
        inf = float("-inf")
        mostExpensiveVal = inf
        mostExpensiveName = None
        mostExpensiveWeight = inf

        for item in items.items():
            itemName = item[0]
            itemValue = item[1][1]
            itemWeight = item[1][0]

            if(itemName in processed):
                continue

            if((itemValue > mostExpensiveVal) or (itemValue == mostExpensiveVal and itemWeight < mostExpensiveWeight)):
                mostExpensiveVal = itemValue
                mostExpensiveName = itemName
                mostExpensiveWeight = itemWeight
            


        return mostExpensiveName, mostExpensiveWeight, mostExpensiveVal
    
    # already processed items
    processed = []

    #knapsack content
    itemList = []

    availableCapacity = maxCapacity

    (itemName, itemWeight, itemValue) = find_most_expensive(items, processed)

    while itemName:
        if( itemWeight <= availableCapacity):
            availableCapacity -= itemWeight
            itemList.append((itemName, itemWeight, itemValue))

        processed.append(itemName)
        (itemName, itemWeight, itemValue)= find_most_expensive(items, processed)

    return itemList

    