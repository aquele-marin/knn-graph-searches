class DepthFirstSearch():
    def __init__(self,  graph) -> None:
        self.graph = graph
        return None

    def Execute(self, startNode=None, visited=None):
        if startNode == None:
            startNode = self.nodes['0']

        if visited is None:
            visited = set()

        startNodeKey = getattr(startNode, self.keyName)
        visited.add(startNodeKey)

        print(startNodeKey)

        for next in self.nodes[startNodeKey] - visited:
            depthSearch(graph, next, visited)
        return visited
        pass