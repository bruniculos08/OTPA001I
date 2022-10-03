def mergeSort(lista):
    print(lista)

    if(len(lista) <= 1):
        return lista
    
    end = len(lista)
    middle = int(end/2)

    lista1 = lista[middle:end]
    lista2 = lista[0:middle]

    lista1 = mergeSort(lista1)
    lista2 = mergeSort(lista2)

    return merge(lista1, lista2)

def merge(lista1, lista2):
    newLista = []
    len1 = len(lista1)                  # Como a complexidade de len() é O(1) o algoritmo funciona com a mesma...
    len2 = len(lista2)                  # ... complexidade qual teria se fizessemo passando os tamanhos como argumentos.
    index1, index2 = 0, 0

    while(index1 < len1 and index2 < len2):
        item1 = lista1[index1] 
        item2 = lista2[index2]  
        if(item1 <= item2):
            newLista.append(item1)
            index1 += 1
        else:
            newLista.append(item2)
            index2 += 1
    
    if(index1 == len1): 
        newLista = newLista + lista2[index2:] # Concatena a newLista e a lista1
    else:
        newLista = newLista + lista1[index1:] # Concatena a newLista e a lista2

    return newLista

if __name__ == "__main__":
    vector = [1, 7, 3, 8, 4, 5]
    vector = mergeSort(vector)
    print(vector)
    print("teste")