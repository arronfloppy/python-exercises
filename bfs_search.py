from collections import deque
""" breadh-first-search tells you if there's a path from A to B
I there's a path, BFS will find the shortest path for an unweighted directed graph.
If you have a problem like "find the shortest X" try modelling your problem as a graph.
For weighted directed graphs use Dijkstra's algorithm """

def bfs_search(graph, valueFrom, valueToSearch):
    """  bredth-first-search implementation
    serch first valueToSearch occurence starting from valueFrom in unweighted directed graph. Ex:
    graph={}
    graph["Marie"] = ["Jean"]
    graph["Jean"] = ["Michel","Louis"]
    graph["Michel"] = [] 
    graph["Louis"] = [] """
    search_queue = deque()
    searched = []
    search_queue.append(valueFrom)
    while search_queue:
        item = search_queue.popleft()
        if item in searched:
            continue
        elif item == valueToSearch:
            return True
        searched.append(item)
        item = graph.get(item)
        if item:
            search_queue += item
    return False

    



