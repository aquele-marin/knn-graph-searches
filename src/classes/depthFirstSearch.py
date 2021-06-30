from src.classes.node import Node
class DepthFirstSearch():
    def __init__(self,  graph) -> None:
        self.graph = graph
        self.searchNode = None

    def searchFor(self, nodeKey):
        self.searchNode = nodeKey
        return Node

    def Execute(self, startNodeKey=None,visited=None):
        if self.searchNode == None:
            print("depthFirstSeach.Execute: Searched node key must be addeed")
            return False

        if startNodeKey == None:
            startNode = self.graph.nodes['0'].key

        if visited is None:
            visited = list()

        visited.append(startNodeKey)

        vector = [x for x in list(self.graph.edges[startNodeKey]) if x not in visited]

        for next in vector:
            if next == self.searchNode:
                visited.append(next)
                return visited
            else:
                if not visited[len(visited)-1] == self.searchNode:
                    self.Execute(next,visited)

        return visited