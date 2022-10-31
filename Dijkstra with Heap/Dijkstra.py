# Dijkstra algorithm

from asyncio.windows_events import INFINITE
from math import *
from heapq import *

#from numpy import Infinity

def createEdgesDictionary():
    # (1) Path of the file containing the graph edges with weights:
    generalPath = "C:\\Users\\bruni\\OneDrive\\Documentos\\GitHub\\OTPA001I\\Dijkstra with Heap"

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
    Predecessor = {}
    isNotTemp = {}
    PriorityQueue = []

    # (1) Mark[v] represent the known lowest distance between vertice v and the start vertice and...
    # ...isNotTemp[v] tells if the vertice has a permanent mark:
    for vertice in graph.keys():
        Mark[vertice] = INFINITE
        isNotTemp[vertice] = False
    Mark[start] = 0

    # (2) Predecessor[v] represents the predecessor vertice of vi in the smallest path between vertice i and the start vertice:
    Predecessor[start] = start

    # (3) The priority queue will be a minimum heap and the minimum value will be the smallest distance discovered on the last...
    # ... iteration, what is always the smallest mark (except when the smallest mark for determined vertice in top of the queue was...
    # ... discovered later and then removed from the queue before):
    heappush(PriorityQueue, (0, start))

    # (4) While the priority queue is not empty:
    while(len(PriorityQueue) != 0):
        # (4.1) Pop the first element off the priority queue, i. e., the element with the smallest mark discovered on the previous iteration:
        item = heappop(PriorityQueue)
        # (4.2) Getting the vertice with the smallest mark according to the priority queue:
        actualVertice = item[1]
        # (4.3) Getting the value of the smallest mark according to the priority queue:
        minMarkPQ = item[0]
        # (4.4) Removing the actual vertice from the Temporary Set:
        isNotTemp[actualVertice] = True

        # (4.5) If the mark of the actual vertice is less than the value we got from the priority queue, it means that the actual value...
        # ... from the priority queue is not the smallest mark value, it happens because the value was inserted in the priority queue as...
        # ... the smallest mark (and as the actual vertice mark) and later the mark was actualized because a smallest distance was found.
        # In this case we do not need to try to find smallest marks using the actual vertice because it has already been done, using a...
        # ... previous item from queue:
        if(Mark[actualVertice] < minMarkPQ):
            continue

        # (4.6) Trying to get new mark for each neighbor of the actual vertice:
        for neighbor in graph[actualVertice]:
            
            # (4.6.1) If the neighbor is already not in the Temporary Set it means that the smallest mark for this neighbor was already found:
            if isNotTemp[neighbor]:
                continue

            # (4.6.2) If Mark[neighbor] > Mark[actualVertice] + graph[actualVertice][neighbor] then we need to actualize the mark for this...
            # ... neighbor, actualize the neighbor's previous vertice and add to the priority queue the tuple (newDist, neighbor) because...
            # ... newDist may be the new smallest mark: 
            newDist = Mark[actualVertice] + graph[actualVertice][neighbor]
            if newDist < Mark[neighbor]:
                Mark[neighbor] = newDist
                heappush(PriorityQueue, (newDist, neighbor))
                Predecessor[neighbor] = actualVertice

                
    # (4.7) If the distance to end vertice still equals infinity, the end vertice is unreachable:
    if Mark[end] == INFINITE:
            return [], -1

    # (4.8) Building the smallest path:
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
    print(f"caminho = {path}")
    print(f"distância = {distance}")