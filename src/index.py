import random
import sys
import numpy as np
from matplotlib import pyplot as plt

from matplotlib.pyplot import close
from src.classes.node import Node
from src.classes.graph import Graph
from src.classes.depthFirstSearch import DepthFirstSearch
from src.classes.breadthFirstSearch import BreadthFirstSearch
from src.classes.bestFirstSearch import BestFirstSearch
from src.classes.clusteredKNN import KnnClustered
from src.classes.aStar import AStarSearch
class Program:
    def __init__(self, vertexAmount, knn) -> None:
        self.vertexAmount = vertexAmount
        self.knn = knn
        self.graph = Graph(nodeType=Node)
        sys.setrecursionlimit(24000)

    def generateVertexes(self, seed):
        print("Gerando nós")
        random.seed(seed)
        self.graph.nodePositions = dict()
        self.graph.nodeList = list()

        xValues = random.sample(range(0, self.vertexAmount+1), self.vertexAmount)
        yValues = random.sample(range(0, self.vertexAmount+1), self.vertexAmount)

        for i in range(len(xValues)):

            nodeKey = ",".join((str(xValues[i]),str(yValues[i])))
            self.graph.nodePositions[i] = np.array([xValues[i], yValues[i]])
            node = Node(nodeKey, xValues[i], yValues[i])
            
            self.graph.nodeList.append([xValues[i], yValues[i]])
            self.graph.addVertex(node)

    def generateEdges(self):
        print("Gerando arestas")
        self.graph.buildKNNGraph(self.knn)

    def executeTests(self):
        print("Executando testes")
        arrayGraph = self.graph.toArray(['x', 'y'])
        arrayGraph.sort(key=lambda tup: tup[0])
        destNodes = []

        # Escolhe ponto próximo a origem do plano
        node = arrayGraph[0]

        # Escolhe um ponto perto da origem do plano
        destNodes.append(arrayGraph[7])

        # Escolhe um ponto em uma distancia mediana da origem do plano
        destNodes.append(arrayGraph[int(len(arrayGraph)/2)])

        # Escolhe ponto bem longe da origem do plano
        destNodes.append(arrayGraph[len(arrayGraph)-2])

        

        # Executa buscas para cada metodo, fazendo uma busca em curta distãncia, média e longa

        # Executando buscas em profundidade
        print("Executando buscas em profundidade")
        dfsTime = list()
        dfsPath = list()
        for i in range(3):
            search = DepthFirstSearch(self.graph)
            _dfsTime, _dfsPath = search.Execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[i][0]), str(destNodes[i][1]))))
            dfsTime.append(_dfsTime)
            dfsPath.append(_dfsPath)

        # Executando buscas em largura
        print("Executando buscas em largura")
        bfsTime = list()
        bfsPath = list()
        for i in range(3):
            search = BreadthFirstSearch(self.graph)
            _bfsTime, _bfsPath = search.Execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[i][0]), str(destNodes[i][1]))))
            bfsTime.append(_bfsTime)
            bfsPath.append(_bfsPath)

        # Executando buscas por best firsts
        print("Executando buscas por best firsts")
        bestFirstTime = list()
        bestFirstPath = list()
        for i in range(3):
            search = BestFirstSearch(self.graph)
            _bestFirstTime, _bestFirstPath = search.Execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[i][0]), str(destNodes[i][1]))))
            bestFirstTime.append(_bestFirstTime)
            bestFirstPath.append(_bestFirstPath)

        # Executando busca A*
        print("Executando busca A*")
        AStarTime = list()
        AStarPath = list()
        for i in range(3):
            search = AStarSearch(self.graph)
            _AStarTime, _AStarPath = search.execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[i][0]), str(destNodes[i][1]))))
            _AStarPath.reverse()
            
            AStarTime.append(_AStarTime)
            AStarPath.append(_AStarPath)

        print("******** RESULTADOS ********\n\n\n")
        print("BUSCA EM PROFUNDIDADE")
        print("\n\n\n")
        for i in range(3):
            print("TEMPO: " + str(dfsTime[i]))
            print("CAMINHO: ", dfsPath[i])
            print("\n\n\n")

        print("BUSCA POR LARGURA")
        print("\n\n\n")
        for i in range(3):
            print("TEMPO: " + str(bfsTime[i]))
            print("CAMINHO: ", bfsPath[i])
            print("\n\n\n")

        print("BUSCA BEST FIRST")
        print("\n\n\n")
        for i in range(3):
            print("TEMPO: " + str(bestFirstTime[i]))
            print("CAMINHO: ", bestFirstPath[i])
            print("\n\n\n")

        print("BUSCA A*")
        print("\n\n\n")
        for i in range(3):
            print("TEMPO: " + str(AStarTime[i]))
            print("CAMINHO: ", AStarPath[i])
            print("\n\n\n")


        # Gera as imagens com as buscas
        self.graph.plotPath(dfsPath[0], f'./images/{self.graph.totalNodes}K={self.graph.knn}DFSClose.png')
        self.graph.plotPath(dfsPath[1], f'./images/{self.graph.totalNodes}K={self.graph.knn}DFSMedium.png')
        self.graph.plotPath(dfsPath[2], f"./images/{self.graph.totalNodes}K={self.graph.knn}DFSFar.png")

        self.graph.plotPath(bfsPath[0], f"./images/{self.graph.totalNodes}K={self.graph.knn}BFSClose.png")
        self.graph.plotPath(bfsPath[1], f"./images/{self.graph.totalNodes}K={self.graph.knn}BFSMedium.png")
        self.graph.plotPath(bfsPath[2], f"./images/{self.graph.totalNodes}K={self.graph.knn}BFSFar.png")

        self.graph.plotPath(bestFirstPath[0], f"./images/{self.graph.totalNodes}K={self.graph.knn}bestFirstClose.png")
        self.graph.plotPath(bestFirstPath[1], f"./images/{self.graph.totalNodes}K={self.graph.knn}bestFirstMedium.png")
        self.graph.plotPath(bestFirstPath[2], f"./images/{self.graph.totalNodes}K={self.graph.knn}bestFirstFar.png")

        self.graph.plotPath(AStarPath[0], f"./images/{self.graph.totalNodes}K={self.graph.knn}AStarClose.png")
        self.graph.plotPath(AStarPath[1], f"./images/{self.graph.totalNodes}K={self.graph.knn}AStarMedium.png")
        self.graph.plotPath(AStarPath[2], f"./images/{self.graph.totalNodes}K={self.graph.knn}AStarFar.png")

    def generateTimeComparison(self):
        print("Executando analise para as buscas")

        arrayGraph = self.graph.toArray(['x', 'y'])
        arrayGraph.sort(key=lambda tup: tup[0])
        destNodes = []

        # Escolhe ponto próximo a origem do plano
        node = arrayGraph[0]

        # Escolhe um ponto perto da origem do plano
        destNodes.append(arrayGraph[7])

        # Escolhe um ponto em uma distancia mediana da origem do plano
        destNodes.append(arrayGraph[int(len(arrayGraph)/2)])

        # Escolhe ponto bem longe da origem do plano
        destNodes.append(arrayGraph[len(arrayGraph)-2])     

        distance = [[], [], []]


        # Executa cada busca 20 vezes para obter mais relevância estatística
        for j in range(3):
            time = 0
            for i in range(20):
                search = DepthFirstSearch(self.graph)
                _dfsTime, _dfsPath = search.Execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[j][0]), str(destNodes[j][1]))))
                time += _dfsTime
            distance[j].append(time/20)
        
        for j in range(3):
            time = 0
            for i in range(20):
                search = BreadthFirstSearch(self.graph)
                _bfsTime, _ = search.Execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[j][0]), str(destNodes[j][1]))))
                time += _bfsTime
            distance[j].append(time/20)

        for j in range(3):
            time = 0
            for i in range(20):
                search = BestFirstSearch(self.graph)
                _bestFirstTime, _ = search.Execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[j][0]), str(destNodes[j][1]))))
                time += _bestFirstTime
            distance[j].append(time/20)

        for j in range(3):
            time = 0
            for i in range(20):
                search = AStarSearch(self.graph)
                _AStarTime, _ = search.execute(','.join((str(node[0]), str(node[1]))), ','.join((str(destNodes[j][0]), str(destNodes[j][1]))))
                time += _AStarTime
            distance[j].append(time/20)


        # Configurações para exibição do grafo
        labels = ["DFS", "BFS", "BEST FIRST", "A*"]
        x = np.arange(len(labels))
        width = 0.15

        plt.figure()

        plt.bar(x, distance[0], width=width)
        plt.bar(x+0.25,distance[1], width=width)
        plt.bar(x+0.5, distance[2], width=width)

        plt.legend(["Curta distância", "Média distância", "Longa distância"])
        plt.xticks([i + 0.25 for i in range(4)], labels)
        plt.title('Tempos de algoritmos para os casos de teste')
        plt.xlabel('Algoritmos')
        plt.ylabel("Tempo em segundos")
        plt.tight_layout()
        plt.savefig(f'./analisys/{self.graph.totalNodes}K={self.graph.knn}analisys.png')
        plt.close()
