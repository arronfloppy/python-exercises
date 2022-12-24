from collections import deque
""" Dijkstra's algorithms finds the shortest path from A to B for an weighted directed graph.
For unweighted directed graphs use bfs.
Dijkstra's algorithms has for steps:
- find the cheapest node
- update the costs of the neighbors of this node
- repeat for every node in the graph
"""


def dijkstra_search(graph,valueFrom, valueTo):
    """  dijkstra-search implementation
    serch the shortest path from  valueFrom to valueTo in weighted directed graph. Ex:
    graph["Start"]={}
    graph["Start"]["A"] = 6 // 6 is the weight of the edge Start -> A
    graph["Start"]["B"] = 2
    graph["B"]={}
    graph["B"]["A"] = 3
    graph["B"]["Fin"] = 5
    graph["A"]={}
    graph["A"]["Fin"] = 1
    graph["Fin"] = {}
    """
    startNeighbors = graph.get(valueFrom)
    end = graph.get(valueTo,0)
    if not startNeighbors or type(end) != type({}):
        return None

    # infinite cost
    inf = float("inf")

    # the costs dict for every node
    costs = {}

    # the parents dict
    # at each step, each node (key) points out the cheapest parent
    parents = {}

    # alredy precessed node
    processed = []

    # init costs table
    for key,value in startNeighbors.items():
        costs[key] = value
    costs[valueTo] = inf


    def find_cheapest_node():
        lowest_cost = inf
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    node= find_cheapest_node()

    while node:
        # print("Found node" + str(node))
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_cheapest_node()


    return costs.get(valueTo,inf)