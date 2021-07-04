from src.classes.node import Node
from src.classes.graph import Graph
from src.classes.depthFirstSearch import DepthFirstSearch
from src.classes.breadthFirstSearch import BreadthFirstSearch
from src.classes.bestFirstSearch import BestFirstSearch
class Program:
    def __init__(self) -> None:
        grafo = Graph(nodeType=Node)
        
        no = Node("0", 1, 1)
        noo = Node("1", 3, 3)
        noa = Node("2", 2, 3) # Se colocar noa = Node("2", 3, 3) o best first search toma o caminho pelo nó "3" pq vai estar mais perto
        nou = Node("3", 3, 2)

        grafo.addVertex(no)
        grafo.addVertex(noo)
        grafo.addVertex(noa)
        grafo.addVertex(nou)

        grafo.buildKNNGraph(2)

        # busca = DepthFirstSearch(grafo)
        # busca = BreadthFirstSearch(grafo)
        busca = BestFirstSearch(grafo)

        busca.searchFor(noo.key)
        path = busca.Execute(rootNodeKey=no.key)
        print(path)