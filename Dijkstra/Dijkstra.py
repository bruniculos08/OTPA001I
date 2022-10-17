# Dijkstra algorithm considering a undirected graph

def createAdjMatrix():
    # (1) Path of the file containing the graph edges with weights:
    generalPath = "C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\Dijkstra"

    # (2) Opening the file:
    with open(generalPath + "\\Graph.txt") as file:
        # (2.1) Getting a vector of strings with every row from the file:
        rows = file.readlines()

    # (3) Getting the number of edgers:
    verticesNum = int(rows[0])

    # (4) Starting the adjacency matrix:
    MatrixAdj= [[-1 for i in range(verticesNum)] for j in range(verticesNum)]
    # Note: MatrixAdj[i][j] == -1 means that there is no edge between the vertices vi and vj.
    for i in range(verticesNum):
        # (4.1) The weight between an edge and it self is always 0:
        MatrixAdj[i][i] = 0

    # (5) Placing the edges:
    for i in range(1, len(rows)):
        verticeA, verticeB, weightAtoB = map(int, rows[i].split())
        # (5.1) Suppose the edges are enumerated from 1 to n:
        MatrixAdj[verticeA - 1][verticeB - 1], MatrixAdj[verticeB - 1][verticeA - 1] = weightAtoB, weightAtoB
        
    return MatrixAdj

def Dijkstra(start, end, graph):
    return


if __name__ == "__main__":
    graph = createAdjMatrix()
    for row in graph: 
        print(row)
    pass