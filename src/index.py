from src.classes.node import Node
from src.classes.graph import Graph
from src.classes.depthFirstSearch import DepthFirstSearch
class Program:
    def __init__(self) -> None:
        grafo = Graph(nodeType=Node)
        
        no = Node("0", 1, 1)
        noo = Node("1", 2, 2)
        noa = Node("2", 1, 2)
        nou = Node("3", 2, 1)

        grafo.addVertex(no)
        grafo.addVertex(noo)
        grafo.addVertex(noa)
        grafo.addVertex(nou)

        grafo.buildKNNGraph(2)

        busca = DepthFirstSearch(grafo)

        busca.searchFor(noo.key)
        path = busca.Execute(startNodeKey=no.key)