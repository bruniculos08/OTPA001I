
vector = [1, 5, 2, 8, 7, 0, -1]

def mergeSort(lista):
    if(len(lista) == 1):
        return lista
    
    end = len(lista)
    middle = end/2

    lista1 = lista[middle+1:end]
    lista2 = lista[0:middle]

    lista1 = mergeSort(lista1)
    lista2 = mergeSort(lista2)

    return mergeSort(lista1, lista2)

def merge(lista1, lista2):
    newList = []
    len1 = len(lista1)
    len2 = len(lista2)
    for i in range(max(len(lista1), len(lista2))):
        if(lista1[i] >= lista2[i]):
            newList.append(lista1[i])
        else:
            newList.append(lista2[i])
    
    return

vector = mergeSort(vector)

print(vector)