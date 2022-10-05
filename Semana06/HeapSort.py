def get_parent(i):
    return ((i-1)/2)

def get_left(i):
    return 2*i + 1

def get_right(i):
    return 2*i + 2

def max_heapify(A, i, heap_size):
    left = get_left(i)
    right = get_right(i)

    largest = i
    if left <= heap_size and A[left] > A[largest]:
        largest = left
    
    if right <= heap_size and A[right] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

# A é o vetor, n é o tamanho do vetor
def build_max_heap(A, n):
    for i in range(int(n/2) - 1, -1, -1): # começa na metade e verificandos os filhos deste (que são as folhas)...
        max_heapify(A, i, n-1)            # ... variando i em -1 até que i == -1

def heap_sort(A):
    n = len(A)
    heap_size = n-1
    build_max_heap(A, n)

    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0] # Swap
        heap_size -= 1
        max_heapify(A, 0, heap_size)

    return A
        

vetor = [1, 4, 2, 8, 0]
vetor = heap_sort(vetor)
print(vetor)