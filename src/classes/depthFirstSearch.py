import time
class DepthFirstSearch():
    def __init__(self,  graph) -> None:
        self.graph = graph


    def Execute(self, startNodeKey, destNodeKey, visited=None):
        tic = time.perf_counter()
        if startNodeKey == None:
            return None, None

        if visited is None:
            visited = list()

        path = self.__execute(startNodeKey, destNodeKey, visited)

        toc = time.perf_counter()
        timeval = toc - tic
        return timeval, path

    def __execute(self, startNodeKey, destNodeKey, visited):
        visited.append(startNodeKey)
        
        if startNodeKey == destNodeKey:
            return visited

        vector = [x for x in list(self.graph.edges[startNodeKey]) if x not in visited]


        for next in vector:
            self.__execute(next, destNodeKey, visited)
            if visited[len(visited)-1] == destNodeKey:
                break

        
        return visited