from collections import deque

def bfs_search(graph, valueFrom, valueToSearch):
    """  bredth-first-search implementation
    serch first valueToSearch occurence starting from valueFrom in directed graph. Ex:
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

    



