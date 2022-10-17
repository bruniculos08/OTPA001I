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
        
    return MatrixAdj, verticesNum

def dijkstra(start, end, graph, verticesNum):
    start = start-1
    end = end-1
    
    # (1) Marks[i] represent the known lowest distance between vertice i and the start vertice: 
    Marks = [INFINITE for i in range(verticesNum)]
    Marks[start] = 0

    # (2) Pre[i] represents the predecessor vertice of vi in the smallest path between vertice i and the start vertice:
    Pre = [-1 for i in range(verticesNum)]
    Pre[start] = [start]
    
    # (3) The value isTemp[i] tells if vi belongs to the Temporary Set of vertices:
    isTemp = [True for i in range(verticesNum)]
    isTemp[start] = False

    # (4) The path always starts with the start vertice and because Mark[start][start] = 0, minMark = start:
    actualVertice = start
    minMark = start

    # (5) The algorithm will finish when the smallest path from the start vertice to the end vertice is computed, what...
    # ... happens when the vertice is removed from the Temporary Set:
    while(actualVertice != end):

        # (5.1) Looking for each vertex in the Temporary Set:
        for i in range(verticesNum):
            if(isTemp[i] == True):
                
                # (5.2) If there is a smallest path from the start vertice to vi:
                if(graph[i][actualVertice] != -1 and Marks[i] > Marks[actualVertice] + graph[i][actualVertice]):
                    
                    Marks[i] = Marks[actualVertice] + graph[i][actualVertice]
                    Pre[i] = actualVertice

                    # (5.3) Looking witch one is the vertice with the lowest mark will save us time because if we didn't do that...
                    # ... we would need to search this in the list Marks and because it's a list (and not a dictionary) the time...
                    # ... complexity is O(n), so now we have O(1) to get the vertice with minimum mark:
                if(isTemp[minMark] == False):
                    minMark = i
                elif(Marks[i] < Marks[minMark]):
                    minMark = i

        # (6) If the lowest mark vertice was not actualized it means there is no more edges to search and then...
        # ... there is no path between the start vertice to end vertice:
        if(minMark == actualVertice and isTemp[minMark] == False):
            print(actualVertice + 1)
            return [], -1
                        
        # (7) The new vertice to be analyzed and the next to be removed from the Temporary Set is the vertice with... 
        # ... the lowest mark: 
        actualVertice = minMark
        
        # (8) By definition the actual vertice being analyzed is not in Temporary Set:
        isTemp[minMark] = False

    # (9) The smallest distance between the start vertice to the end vertice is equal to Mark[end]:
    distance = Marks[end]

    # (10) Building the smallest path:
    path = [end+1]
    while(True):
        index = Pre[path[-1]-1]
        path.append(index+1)
        if(index == start):
            break
    path.reverse()

    return path, distance


if __name__ == "__main__":
    graph, verticesNum = createAdjMatrix()
    path, distance = dijkstra(1, 4, graph, verticesNum)
    print(path)
    print(distance)