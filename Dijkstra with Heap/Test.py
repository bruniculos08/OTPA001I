from heapq import *


Mark = {'A' : 4, 'B' : 2, 'C' : 4, 'D' : 5, 'E' : 6, 'F' : 7, 'G' : 8}
min_heap = []
for item in Mark.items():
    heappush(min_heap, (item[1], item[0]))

heapify(min_heap)
print(min_heap)
print(heappop(min_heap))
print(min_heap)