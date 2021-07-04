import collections

class BestFirstSearch():
    def __init__(self, graph):
        self.graph = graph
        self.searchNode = None

    def searchFor(self, nodeKey):
        self.searchNode = nodeKey

    def Execute(self, rootNodeKey):
        visited, queue = list(), collections.deque([rootNodeKey])
        visited.append(rootNodeKey)

        while queue:

            # Tira um vertex da fila
            vertex = queue.popleft()
            orderedEdges = []
            # Se não tiver sido visitado, marca como visitado
            # e coloca na fila

            for neighbour in self.graph.edges[vertex]:
                distance = ((((self.graph.nodes[neighbour].x - self.graph.nodes[vertex].x)**2) + ((self.graph.nodes[neighbour].y - self.graph.nodes[vertex].y)**2))**0.5)
                orderedEdges.append((neighbour, distance))

            orderedEdges.sort(key=lambda tup: tup[1])

            # print(orderedEdges)

            for neighbour in orderedEdges:
                if self.searchNode in self.graph.edges[vertex]:
                    visited.append(self.searchNode)
                    return [x for x in visited if x not in queue]
                elif neighbour[0] not in visited:
                    visited.append(neighbour[0])
                    queue.append(neighbour[0])

        return visited


# distance = ((((self.graph.nodes[v].x - self.graph.nodes[vertex].x)**2) + ((self.graph.nodes[v].y - self.graph.nodes[vertex].y)**2))**0.5)