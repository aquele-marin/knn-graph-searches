from src.classes.node import Node
from src.classes.graph import Graph
class Program:
    def __init__(self) -> None:
        grafo = Graph(nodeType=Node)
        
        no = Node("0", "Batata", 12)
        noo = Node("1", "Patata", 18)
        noa = Node("2", "Potato", 18)

        grafo.addVertex(no)
        grafo.addVertex(noo)
        grafo.addVertex(noa)

        grafo.addEdge(no, noo)
        grafo.addEdge(no, noa)

        print(grafo.edgeExists(no, noo))
        print(grafo.edgeExists(no, noa))

        print(grafo.getFirstConnectedVertexIndex(no))
        print(grafo.getNextConnectedVertexIndex(no, noo))

        # print(grafo.removeNode(no))

        grafo.printGraph()