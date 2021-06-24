from typing import Any, Type
import random

import numpy as np
from sklearn.neighbors import kneighbors_graph
from matplotlib import pyplot as plt
class Graph:

    totalNodes: int
    nodes: dict
    edges: dict
    nodeType: Type[Any]

    def __init__(self, nodeType: Type[Any]) -> None:
        self.totalNodes = 0
        self.nodeType = nodeType

        # Cria dicionario para o identificador
        self.nodes = dict()

        # Cria dicionario para as arestas
        self.edges = dict()

        return None

    def addVertex(self, vertex) -> bool:
        if self.nodeType != type(vertex):
            print("addVertex: This node type is not supported in this graph")
            return False
        if not hasattr(vertex, "key"):
            print("addVertex: This node doesn't have a key attribute")
            return False
        if self.nodes.get(vertex.key, None) != None:
            print("addVertex: The key in this node already exists")
            return False

        # Adiciona vertex nos dicionários
        self.nodes[vertex.key] = vertex

        # Cria dicionario para arestas
        self.edges[vertex.key] = dict()

        self.totalNodes = self.totalNodes + 1

        return True

    def vertexExists(self, vertex) -> bool:
        if self.nodeType != type(vertex):
            print("vertexExists: This node type is not supported in this graph")
            return False
        if not hasattr(vertex, "key"):
            print("vertexExists: This node doesn't have a key attribute")
            return False

        _vertex = self.nodes.get(vertex.key, None)
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
        if not hasattr(source, "key"):
            print("addEdge: This source node doesn't have a key attribute")
            return False

        if self.nodeType != type(destination):
            print("addEdge: This destination node type is not supported in this graph")
            return False
        if not hasattr(destination, "key"):
            print("addEdge: This destination node doesn't have a key attribute")
            return False

        # [0]        [1]          [2]       [3]           [4] Nodes
        # [1: True]  [0: True]              [0: True]
        # [4: True]
        # [3: True]

        self.edges[source.key][destination.key] = True
        self.edges[destination.key][source.key] = True

        return True

    def edgeExists(self, source, destination) -> bool:
        if self.nodeType != type(source):
            print("edgeExists: This source node type is not supported in this graph")
            return False
        if not hasattr(source, "key"):
            print("edgeExists: This source node doesn't have a key attribute")
            return False

        if self.nodeType != type(destination):
            print("edgeExists: This destination node type is not supported in this graph")
            return False
        if not hasattr(destination, "key"):
            print("edgeExists: This source node doesn't have a key attribute")
            return False

        firstNode = self.edges.get(source.key, None)
        if firstNode == None:
            print("edgeExists: Source node not found")
            return False
        
        secondNode = self.edges.get(source.key).get(destination.key, None)
        if secondNode == None:
            print("edgeExists: Destination node not found")
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
        if not hasattr(vertex, "key"):
            print("removeNode: This node doesn't have a key attribute")
            return False

        nodeKey = vertex.key

        self.nodes.pop(nodeKey)

        for node in self.edges[nodeKey]:
            self.edges[node].pop(nodeKey)

        self.edges.pop(nodeKey)
        self.totalNodes = self.totalNodes - 1
            
        return True

    def getFirstConnectedVertexIndex(self, vertex):
        if self.nodeType != type(vertex):
            print("getFirstConnectedVertexIndex: This node type is not supported in this graph")
            return None
        if not hasattr(vertex, "key"):
            print("getFirstConnectedVertexIndex: This node doesn't have a key attribute")
            return None

        return self.nodes[list(self.edges[vertex.key].keys())[0]]

    # O(N)
    def getNextConnectedVertexIndex(self, vertex, currentEdge):
        if self.nodeType != type(vertex):
            print("getNextConnectedVertexIndex: This node type is not supported in this graph")
            return None
        if not hasattr(vertex, "key"):
            print("getNextConnectedVertexIndex: This node doesn't have a key attribute")
            return None

        if self.nodeType != type(currentEdge):
            print("getNextConnectedVertexIndex: This edge node type is not supported in this graph")
            return None
        if not hasattr(currentEdge, "key"):
            print("getNextConnectedVertexIndex: This node doesn't have a key attribute")
            return None

        if vertex.key == currentEdge.key:
            print("getNextConnectedVertexIndex: Both nodes have the same key !")
            return None

        flag = 0
        for edge in self.edges[vertex.key]:
            if flag == 1:
                return self.nodes[edge]
            if self.nodes[edge].key == currentEdge.key:
                flag = 1
            
        if flag == 0:
            print("getNextConnectedVertexIndex: This edge node isn't connected to this node")

        return None

    def printGraph(self):

        for node in self.nodes:
            currentNode = self.nodes[node].key
            print(currentNode)

            for edge in self.edges[currentNode]:
                print(currentNode + " -> " + self.nodes[edge].key)

        pass

    def clear(self):
        self.totalNodes = 0
        self.nodes.clear()
        self.edges.clear()

        pass

    def buildKNNGraph(self, n=None):
        if n == None:
            print("buldKNN: Plese reference N nearest neighbors")
            return False

        X = self.toArray(['x', 'y'])
        A = kneighbors_graph(X, n, mode='connectivity')
        matrix = A.toarray()
        matrixLength = len(matrix)

        nodesArray = self._toArray()
        for i in range(matrixLength):
            for j in range(matrixLength):
                if matrix[i][j] == 1.0:
                    self.addEdge(self.nodes[nodesArray[i]], self.nodes[nodesArray[j]])

        print(X)
        plt.scatter([x[0] for x in X], [x[1] for x in X])
        plt.show()

        return True
        
    def _toArray(self):
        return np.array(list(self.nodes))

    def toArray(self, struct = []):
        array = self._toArray()
        newArray = [[] for _ in range(self.totalNodes)]

        for i in range(self.totalNodes):
            for attr in struct:
                newArray[i].append(getattr(self.nodes[array[i]], attr))
            
        return newArray
