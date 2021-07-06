import math
import time
from matplotlib import pyplot as plt

class KnnClustered:
    def __init__(self, graph, k):
        self.graph = graph
        self.k = k
        self.area = 1
        self.rounds = 5
        if(k >= graph.totalNodes):
            self.k = graph.totalNodes-1
        
    def __increaseArea(self):
            self.rounds += 1
            self.area = pow(2,self.rounds)
            
    def __resetArea(self):
        self.area = 1
    
    def __searchSpace(self,x, y):
        knn = set()
        #Define os limites superiores e inferiores da busca
        minX = 0
        maxX = self.graph.totalNodes
        minY = 0
        maxY = self.graph.totalNodes
        if (x - self.area) > 0:
            minX = x - self.area
        if (x + self.area) < maxX:
            maxX = x + self.area
        if (y - self.area) > 0:
            minY = y - self.area
        if (y + self.area) < maxY:
            maxY = y + self.area
        # Adiciona todos os nós da região na lista "neighbors"
        origin = ",".join((str(x),str(y)))
        for a in range(minX, maxX+1):
            for b in range(minY, maxY+1):
                nodeKey = ",".join((str(a),str(b)))
                knn.add(nodeKey)
        try:
            knn.remove(origin)
        except KeyError:
            pass
        return set(knn)

    def __minimumViableSet(self, x, y):
        self.__resetArea()
        nodes = set(self.graph.nodes.keys()).intersection(self.__searchSpace(x, y))
        while len(nodes) < self.k:
            self.__increaseArea()
            nodes = set(self.graph.nodes.keys()).intersection(self.__searchSpace(x, y))
        return list(nodes)
    
    def __euclidianDistance(self,x1,y1, x2, y2):
        x = abs(x2 - x1)
        y = abs(y2 - y1)
        return math.sqrt(pow(x,2) + pow(y,2))
    
    def __kNearestNeighbors(self, x, y):
        viableListWithDistance = dict()
        viableList = self.__minimumViableSet(x, y)
        while len(viableList) > 0:
            nodeKey = viableList.pop()
            node = self.graph.nodes[nodeKey]
            distance = self.__euclidianDistance(x,y,node.x,node.y)
            viableListWithDistance[nodeKey] = distance
        return sorted(viableListWithDistance, key=viableListWithDistance.get)[:3]
    
    def Execute(self):
        tic = time.perf_counter()
        epoch = 0
        for key in self.graph.nodes:
            epoch += 1
            source = self.graph.nodes[key]
            knn = self.__kNearestNeighbors(source.x, source.y)
            for n in knn:
                destination = self.graph.nodes[n]
                self.graph.addEdge(source, destination)
        toc = time.perf_counter()

        timeval = toc - tic
        return timeval