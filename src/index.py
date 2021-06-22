from src.classes.node import Node
from src.classes.graph import Graph
class Program:
    def __init__(self) -> None:
        grafo = Graph(keyName="__serial__" , nodeType=Node)
        
        no = Node("Batata", 12)
        noo = Node("Patata", 18)
        noa = Node("Potato", 18)

        grafo.addVertex(no)
        grafo.addVertex(noo)
        grafo.addVertex(noa)

        grafo.addEdge(no, noo)
        grafo.addEdge(no, noa)

        grafo.printGraph()
