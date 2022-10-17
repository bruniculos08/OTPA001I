# Dijkstra algorithm considering a undirected graph

from asyncio.windows_events import INFINITE
from math import *

from numpy import Infinity

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

def dijkstra(start, end, graph, verticesNum):
    start, end = start-1, end-1
    
    # (1) Marks[i] represent the known lowest distance between vertice i and the start vertice: 
    Marks = [int(INFINITE) for i in range(verticesNum)]
    Marks[start] = 0

    # (2) Pre[i] represents the predecessor vertice of vi in the smallest path between vertice i and the start vertice:
    Pre = [-1 for i in range(verticesNum)]
    Pre[start] = [start]
    
    # (3) The value isTemp[i] tells if vi belongs to the Temporary Set of vertices:
    isTemp = [True for i in range(verticesNum)]
    isTemp[start] = False
    
    # (4) This list will cotain the indexes of vertices of the smallest path between the end vertice and the start vertice:
    path = [start]

    # (5) The path always starts with the start vertice and because Mark[start][start] = 0, minMark = start:
    actualVertice = start
    minMark = start

    # (6) The algorithm will finish when the smallest path from the start vertice to the end vertice is computed, what...
    # ... happens when the vertice is removed from the Temporary Set:
    while(isTemp[end] == False):
        
        isTemp[actualVertice] = True

        for i in enumerate(isTemp):
            if(isTemp == False):
                if(Marks[i] > Marks[actualVertice] + graph[i][actualVertice]):
                    
                    Marks[i] = Marks[actualVertice] + graph[i][actualVertice]
                    Pre[i] = actualVertice

                    # () Looking witch one is the vertice with the lowest mark will save us time because if we didn't do that...
                    # ... we would need to search this in the list Marks and because it's a list (and not a dictionary) the time...
                    # ... complexity is O(n), so now we have O(1) to get the vertice with minimum mark:
                    if(isTemp[minMark] == False):
                        minMark = i
                    elif(Marks[i] < Marks[minMark]):
                        minMark = i
                    


        
        

                    
    return path


if __name__ == "__main__":
    graph = createAdjMatrix()
    for row in graph: 
        print(row)
    pass