from bfs_search import bfs_search

def test_bfs_search():
    graph={}
    graph["Marie"] = ["Jean", "Victor", "Pierre"]
    graph["Jean"] = ["Michel","Louis"]
    graph["Michel"] = []
    graph["Louis"] = ["Jules", "Ian"]
    graph["Victor"] = []
    graph["Jules"] = []
    #graph["Ian"] = []

    assert bfs_search(graph,"Marie","Ian") == True
    assert bfs_search(graph,"Victor","Ian") == False
    assert bfs_search(graph,"Pierre","Jules") == False