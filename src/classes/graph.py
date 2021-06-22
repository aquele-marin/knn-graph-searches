from typing import Any, Type
class Graph:

    totalNodes: int
    nodes: dict
    edges: dict
    nodeType: Type[Any]
    keyName: str

    def __init__(self, keyName: str, nodeType: Type[Any]) -> None:
        self.totalNodes = 0
        self.nodeType = nodeType
        self.keyName = keyName

        # Cria dicionario para o identificador
        self.nodes = dict()

        # Cria dicionario para as arestas
        self.edges = dict()

        pass

    def addVertex(self, vertex) -> bool:
        if self.nodeType != type(vertex):
            print("addVertex: This node type is not supported in this graph")
            return False

        # Adiciona vertex nos dicionários
        self.nodes[str(self.totalNodes)] = vertex

        # Assina o vertex com a chave do grafo
        setattr(vertex, self.keyName, str(self.totalNodes))

        # Cria dicionario para arestas
        self.edges[getattr(vertex, self.keyName)] = dict()

        self.totalNodes = self.totalNodes + 1

        return True

    def vertexExists(self, vertex) -> bool:
        if self.nodeType != type(vertex):
            print("vertexExists: This node type is not supported in this graph")
            return False
        if not hasattr(vertex, self.keyName):
            print("vertexExists: This node is not in this graph")
            return False

        _vertex = self.nodes.get(getattr(vertex, self.keyName), None)
        if _vertex == None:
            print("vertexExists: Vertex doesn't exists")
            return False
        else:
            return True

    def hasAnyVertex(self) -> bool:
        if len(self.nodes) > 0:
            return True
        else:
            return False

    def addEdge(self, source, destination) -> bool:
        if self.nodeType != type(source):
            print("addEdge: This source node type is not supported in this graph")
            return False
        if not hasattr(source, self.keyName):
            print("addEdge: This source node is not in this graph")
            return False

        if self.nodeType != type(destination):
            print("addEdge: This destination node type is not supported in this graph")
            return False
        if not hasattr(destination, self.keyName):
            print("addEdge: This destination node is not in this graph")
            return False

        # [0]        [1]          [2]       [3]           [4] Nodes
        # [1: True]  [0: True]              [0: True]
        # [4: True]
        # [3: True]
        self.edges[getattr(source, self.keyName)][getattr(destination, self.keyName)] = True
        self.edges[getattr(destination, self.keyName)][getattr(source, self.keyName)] = True

        return True

    def edgeExists(self, source, destination) -> bool:
        if self.nodeType != type(source):
            print("edgeExists: This source node type is not supported in this graph")
            return False
        if not hasattr(source, self.keyName):
            print("edgeExists: This source node is not in this graph")
            return False

        if self.nodeType != type(destination):
            print("edgeExists: This destination node type is not supported in this graph")
            return False
        if not hasattr(destination, self.keyName):
            print("edgeExists: This destination node is not in this graph")
            return False

        edge = self.edges.get(getattr(source, self.keyName), None).get(getattr(destination, self.keyName), None)
        if edge == None:
            print("edgeExists: Edge not found")
            return False
        else:
            return True

    def hasAnyEdge(self):
        if len(self.edges) > 0:
            return True
        else:
            return False
    # O(N)
    def removeNode(self, vertex):
        if self.nodeType != type(vertex):
            print("removeNode: This node type is not supported in this graph")
            return False
        if not hasattr(vertex, self.keyName):
            print("removeNode: This node is not in this graph")
            return False

        nodeKey = getattr(vertex, self.keyName)

        self.nodes.pop(nodeKey)

        self.edges.pop(nodeKey)

        for node in self.edges:
            self.edges[node].pop(nodeKey, None)
            
        return True

    def getFirstConnectedVertexIndex(self, vertex):
        if self.nodeType != type(vertex):
            print("getFirstConnectedVertexIndex: This node type is not supported in this graph")
            return None
        if not hasattr(vertex, self.keyName):
            print("getFirstConnectedVertexIndex: This node is not in this graph")
            return None

        return self.nodes[list(self.edges[getattr(vertex, self.keyName)].keys())[0]]

    # O(N)
    def getNextConnectedVertexIndex(self, vertex, currentEdge):
        if self.nodeType != type(vertex):
            print("getNextConnectedVertexIndex: This node type is not supported in this graph")
            return None
        if not hasattr(vertex, self.keyName):
            print("getNextConnectedVertexIndex: This node is not in this graph")
            return None

        if self.nodeType != type(currentEdge):
            print("getNextConnectedVertexIndex: This edge node type is not supported in this graph")
            return None
        if not hasattr(currentEdge, self.keyName):
            print("getNextConnectedVertexIndex: This edge node is not in this graph")
            return None

        if getattr(vertex, self.keyName) == getattr(currentEdge, self.keyName):
            print("getNextConnectedVertexIndex: This edge is this node !")
            return None

        flag = 0
        for edge in list(self.edges[getattr(vertex, self.keyName)]):
            # self.edges[getattr(vertex, self.keyName)][edge]
            if flag == 1:
                return self.nodes[edge]
            if getattr(self.nodes[edge], self.keyName) == getattr(currentEdge, self.keyName):
                flag = 1
            
        if flag == 0:
            print("getNextConnectedVertexIndex: This edge node isn't connected to this node")

        return None

    def printGraph(self):

        for node in self.nodes:
            currentNode = getattr(self.nodes[node], self.keyName)
            print(currentNode)

            for edge in self.edges[currentNode]:
                print(currentNode + " -> " + getattr(self.nodes[edge], self.keyName))

        pass

    def clear(self):
        self.totalNodes = 0
        self.nodes.clear()

        pass