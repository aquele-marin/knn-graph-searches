import collections
class BreadthFirstSearch():
    def __init__(self, graph) -> None:
        self.graph = graph
        return None

    def searchFor(self, nodeKey):
        self.searchNode = nodeKey

    def Execute(self, rootNodeKey):
        visited, queue = list(), collections.deque([rootNodeKey])
        visited.append(rootNodeKey)

        while queue:

            # Tira um vertex da fila
            vertex = queue.popleft()

            # Se não tiver sido visitado, marca como visitado
            # e coloca na fila
            for neighbour in self.graph.edges[vertex]:
                if self.searchNode in self.graph.edges[vertex]:
                    visited.append(self.searchNode)
                    return [x for x in visited if x not in queue]
                elif neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return visited