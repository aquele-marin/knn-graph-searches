import collections
import time
class BestFirstSearch():
    def __init__(self, graph):
        self.graph = graph

    def Execute(self, rootNodeKey, destNodeKey):
        tic = time.perf_counter()
        visited, queue = list(), collections.deque([rootNodeKey])
        visited.append(rootNodeKey)

        while queue:

            # Tira um vertex da fila
            vertex = queue.popleft()
            orderedEdges = []
            
            # Ordena os vizinhos mais próximos do destino
            for neighbour in self.graph.edges[vertex]:
                distance = ((((self.graph.nodes[neighbour].x - self.graph.nodes[rootNodeKey].x)**2) + ((self.graph.nodes[neighbour].y - self.graph.nodes[rootNodeKey].y)**2))**0.5)
                orderedEdges.append((neighbour, distance))

            orderedEdges.sort(key=lambda tup: tup[1])

            for neighbour in orderedEdges:
                if destNodeKey in self.graph.edges[vertex]:
                    visited.append(destNodeKey)
                    toc = time.perf_counter()
                    timeval = toc - tic
                    return timeval, [x for x in visited if x not in queue]
                elif neighbour[0] not in visited:
                    visited.append(neighbour[0])
                    queue.append(neighbour[0])
                    # Se não tiver sido visitado, marca como visitado
                    # e coloca na fila

        toc = time.perf_counter()
        timeval = toc - tic
        return timeval, visited