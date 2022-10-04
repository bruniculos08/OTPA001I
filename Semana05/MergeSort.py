import time

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
    #len1 = len(lista1)
    #len2 = len(lista2)

    while(lista1 != [] and lista2 != []):
        item1 = lista1[0] 
        item2 = lista2[0] 
        if(item1 <= item2):
            newLista.append(item1)
            lista1.pop(0) # Retira o primeiro item da lista1
        else:
            newLista.append(item2)
            lista2.pop(0) # Retira o primeiro item da lista2
    
    if(lista1 == []): 
        newLista = newLista + lista2 # Concatena a newLista e a lista1
    else:
        newLista = newLista + lista1 # Concatena a newLista e a lista2

    return newLista

if __name__ == "__main__":
    #vector = [1, 7, 3, 8, 4, 5]
    vector = [ i for i in range(10000000000000, 0 , -1) ] + [ i for i in range(1, 10000000000, 2)] 
    vector = mergeSort(vector)
    print(vector)
    print("teste")