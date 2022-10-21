# Dijkstra algorithm

from asyncio.windows_events import INFINITE
from math import *
from heapq import *

from numpy import Infinity

def createEdgesDictionary():
    # (1) Path of the file containing the graph edges with weights:
    generalPath = "C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\Dijkstra Improved"

    # (2) Opening the file:
    with open(generalPath + "\\Graph.txt") as file:
        # (2.1) Getting a vector of strings with every row from the file:
        rows = file.readlines()

    # (3) Creating a dictionary to store de edges in the graph:
    graph = {}
    for i in range(0, len(rows)):
        row = rows[i].split(' ')
        # (3.1) The if condition uses a dict for the operator in not, the complexity of this operation is O(1) in a dict:     
        if row[0] not in graph.keys():
            # Obs.: the function keys() is O(1). 
            graph[row[0]] = {}
        elif row[1] not in graph.keys():
            graph[row[1]] = {}
        
        # (3.2) Adding the new edge in the dictionary:
        graph[row[0]][row[1]] = float(row[2])
    
    print(f"graph = {graph}")
    return graph
        

def dijkstra(start, end, graph):
    
    Mark = {}
    Mark_heap = []
    Predecessor = {}

    # (1) Mark[v] represent the known lowest distance between vertice v and the start vertice:
    for vertex in graph.keys():
        Mark[vertex] = INFINITE
    Mark[start] = 0

    # (2) Predecessor[v] represents the predecessor vertice of vi in the smallest path between vertice i and the start vertice:
    Predecessor[start] = start
    
    # (3) The Temporary Set of vertices:
    NotTemporary = set()

    # (4) The path always starts with the start vertice and because Mark[start][start] = 0, minMark = start:
    actualVertice = start
    minMark = start

    # (5) The algorithm will finish when the smallest path from the start vertice to the end vertice is computed, what...
    # ... happens when the vertice is removed from the Temporary Set:
    while(actualVertice != end): # O(|V(G)|²)

        NotTemporary.add(actualVertice)
        
        for vertice in graph[actualVertice]:
            if vertice not in NotTemporary:
                if (vertice not in Mark) or (Mark[vertice] > Mark[actualVertice] + graph[actualVertice][vertice]):

                    Mark[vertice] = Mark[actualVertice] + graph[actualVertice][vertice]
                    Predecessor[vertice] = actualVertice

                    heappush(Mark_heap, (Mark[vertice], vertice))
    
        heapify(Mark_heap)       
        minMark = heappop(Mark_heap)[1]
                    
        if minMark == INFINITE:
           return [], -1
        
        actualVertice = minMark

    # (10) Building the smallest path:
    distance = Mark[end]
    path = [end]
    actualVertice = end
    while(actualVertice != start):
        actualVertice = Predecessor[actualVertice]
        path.append(actualVertice)

    path.reverse()
    return path, distance


if __name__ == "__main__":
    graph = createEdgesDictionary()
    path, distance = dijkstra('A', 'E', graph)
    print(f"path = {path}")
    print(f"distance = {distance}")