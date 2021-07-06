import collections
import time
class BreadthFirstSearch():
    def __init__(self, graph) -> None:
        self.graph = graph

    def Execute(self, rootNodeKey, destNodeKey):
        tic = time.perf_counter()
        visited, queue = list(), collections.deque([rootNodeKey])
        visited.append(rootNodeKey)

        while queue:

            # Tira um vertex da fila
            vertex = queue.popleft()

            
            if destNodeKey in self.graph.edges[vertex]:
                visited.append(destNodeKey)

                toc = time.perf_counter()
                timeval = toc - tic
                return timeval, [x for x in visited if x not in queue]

            for neighbour in self.graph.edges[vertex]:
                # Se não tiver sido visitado, marca como visitado
                # e coloca na fila
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    

        toc = time.perf_counter()
        timeval = toc - tic
        return timeval, visited
