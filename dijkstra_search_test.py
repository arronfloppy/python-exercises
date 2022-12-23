from dijkstra_search import dijkstra_search


def test_dijkstra_search():
    graph={}
    graph["Start"]={}
    graph["Start"]["A"] = 6
    graph["Start"]["B"] = 2
    graph["B"]={}
    graph["B"]["A"] = 3
    graph["B"]["Fin"] = 5
    graph["A"]={}
    graph["A"]["Fin"] = 1
    graph["Fin"] = {}
    assert dijkstra_search(graph,"Start", "Fin") == 6
    return True
