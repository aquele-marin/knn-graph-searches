from src.classes.node import Node
from src.classes.graph import Graph
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

        # grafo.addEdge(no, noo)
        # grafo.addEdge(no, noa)

        # grafo.toArray(['x', 'y'])
        # print(grafo.edgeExists(no, noo))
        # print(grafo.edgeExists(no, noa))

        # print(grafo.getFirstConnectedVertexIndex(no))
        # print(grafo.getNextConnectedVertexIndex(no, noo))

        grafo.buildKNNGraph(2)
        grafo.printGraph()