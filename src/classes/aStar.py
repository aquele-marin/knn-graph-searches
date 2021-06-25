import math
from src.classes.heap import Heap
class AStarSearch:
    def __init__(self, graph):
        self.graph = graph
        self.open = Heap()
        self.localCost = dict()
        self.path = dict()
        
    def __euclidean(self, dest, origin):
        x = abs(dest.x - origin.x)
        y = abs(dest.y - origin.y)
        return math.sqrt(pow(x,2) + pow(y,2))
    
    def execute(self, originKey, destKey):
        node = self.graph.nodes[originKey]
        dest = self.graph.nodes[destKey]
        path = self.__searchPath(node, dest)
        return path
    
    # A* algorithm
    def __searchPath(self, origin, dest):
        self.open.push((0, origin))
        self.localCost[origin.key] = 0
        self.path[origin.key] = None
        while not self.open.empty():
            current = self.open.pop()
            distance = current[0]
            node = current[1]
            if node.key == dest.key:
                break
            for childKey in self.graph.edges[node.key]:
                cost = self.localCost[node.key] + self.__euclidean(node, dest)
                if childKey not in self.localCost or cost < self.localCost[childKey]:
                    self.localCost[childKey] = cost
                    childNode = self.graph.nodes[childKey]
                    totalCost = cost + self.__euclidean(dest, childNode)
                    self.open.push((totalCost, childNode))
                    self.path[childKey] = node.key
        if self.open.empty() and node.key != dest.key:
                return list()
        last = dest.key
        reconstructedPath = list()
        reconstructedPath.append(last)
        while last != origin.key:
                last = self.path[last]
                reconstructedPath.append(last)
        return reconstructedPath