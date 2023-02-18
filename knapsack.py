

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
   
    def find_most_expensive(items, processed, maxWeight):
        """ find the most expensive item that fits """
        # infinite negative cost
        mininf = float("-inf")
        mostExpensiveVal = mininf
        mostExpensiveName = None
        mostExpensiveWeight = mininf

        for item in items.items():
            itemName = item[0]
            itemWeight = item[1][0]
            itemValue = item[1][1]

            if(itemName in processed):
                continue

            if( ((itemValue > mostExpensiveVal) or (itemValue == mostExpensiveVal and
             itemWeight < mostExpensiveWeight)) and itemWeight <= maxWeight):
                mostExpensiveVal = itemValue
                mostExpensiveName = itemName
                mostExpensiveWeight = itemWeight
            


        return mostExpensiveName, mostExpensiveWeight, mostExpensiveVal
    
    # already processed items
    processed = []

    #knapsack content
    itemList = []
    totalWeight = 0
    totalValue = 0

    availableCapacity = maxCapacity

    (itemName, itemWeight, itemValue) = find_most_expensive(items, processed, availableCapacity)

    while itemName:
        availableCapacity -= itemWeight
        itemList.append(itemName)
        totalWeight += itemWeight
        totalValue += itemValue

        processed.append(itemName)
        (itemName, itemWeight, itemValue)= find_most_expensive(items, processed, availableCapacity)

    return (itemList, totalWeight, totalValue)

    
def knapsack_dp(maxCapacity, items):
    """ Given a set of n items numbered from 1 up to n, each with a weight wi and a value vi,
    along with a maximum weight capacity W maximize ∑(i to n) v*x 

    Using dynamic programming to divide the problem in n independent problems.
    Parameters
    ----------
    maxCapacity : int
        max knapsack capacity
    items : dict
        available items as { itemName -> str, (itemWeight -> int, itemValue : int)}
    """
    # we divide the problems in n sub problems
    # trying to find the max value for each knapsack from 1 to maxCapacity weight

    # the knapsack table (dynamic programing is always using a table)
    # each row contains the item name
    # each cell contains knapsack weights from 1 to maxCapacity
    # you can fill each cell with the item at this row, with the item(s) at the row -1 or both
    knapsack = {}
    # the previous row of the table
    prevName = ""

    for name in items :
        knapsack[name] = []
        for weight in range(1,maxCapacity+1) :
            currentContent = []
            currentWeight = 0 
            currentVal = 0 
            if not prevName:
                # the first row
                if items[name][0] <= weight:
                    currentContent.append(name)
                    currentWeight = items[name][0]
                    currentVal = items[name][1]
                knapsack[name].append((currentContent,currentWeight,currentVal))
            else: 
                # the content at row -1
                prevContent = knapsack[prevName][weight-1][0]
                prevWeight = knapsack[prevName][weight-1][1]
                prevVal =  knapsack[prevName][weight-1][2]
                
                if items[name][0] > weight:
                    # cant't fill with current item, using the item at row -1
                    knapsack[name].append((prevContent,prevWeight,prevVal))
                else:
                    # we can fill it with the current item 
                    # if we have some weight available, find the cell for this weight
                    # and add the content to current cell
                    weightAvailable = weight - items[name][0]
                    currentWeight = items[name][0] + ( knapsack[prevName][weightAvailable-1][1] if weightAvailable else 0)
                    currentContent.append(name)
                    if weightAvailable:
                        currentContent.extend(knapsack[prevName][weightAvailable-1][0])
                    for elem in currentContent:
                        currentVal += items[elem][1]
                    # find the max between the current and the previous value
                    if(currentVal < prevVal):
                        knapsack[name].append((prevContent,prevWeight,prevVal))
                    else:
                        knapsack[name].append((currentContent,currentWeight,currentVal))
        prevName = name
    # if any, the last cell contains the result
    return knapsack[prevName][-1] if prevName else ([],0,0)


            





    
