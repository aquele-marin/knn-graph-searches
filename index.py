from src.index import Program

print("Você deseja executar a análise para as buscas ? (Muito custosa, levará um tempo)")
print("1 - Sim")
print("2 - Não")

comando = str(input())

print("Executando grafo n = 500 k = 3")
graphProgram = Program(5000, 3)
graphProgram.generateVertexes(200)
graphProgram.generateEdges()

graphProgram.executeTests()
if comando == '1':
    graphProgram.generateTimeComparison()

# print("Executando grafo n = 5000 k = 3")
# graphProgram = Program(5000, 3)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 10000 k = 3")
# graphProgram = Program(10000, 3)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 500 k = 5")
# graphProgram = Program(500, 5)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 5000 k = 5")
# graphProgram = Program(5000, 5)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 10000 k = 5")
# graphProgram = Program(10000, 5)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 500 k = 7")
# graphProgram = Program(500, 7)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 5000 k = 7")
# graphProgram = Program(5000, 7)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()

# print("Executando grafo n = 10000 k = 7")
# graphProgram = Program(10000, 7)
# graphProgram.generateVertexes(200)
# graphProgram.generateEdges()

# graphProgram.executeTests()
# if comando == '1':
#     graphProgram.generateTimeComparison()