# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Função que retorna o index da última ocorrência de um elemento em uma lista

def lastOcurrence(list, item):          # O(n)
    last = -1
    if(list == None):                   
        return -1
    for i in range(len(list)):
        if(list[i] == item):
            last = i
    return last


while(1):
    N = int(input("Enter N: "))
    if(N == 0): break
    list = map(int, input().split())        # Split without arg uses space bar | O(n)
    result, extra = 0, 0

    newList = []
                                            # Note que a solução foi semelhante a usar um dicionário
    for pos in list:                        # O(n.m) onde m = len(list) e n = len(newList) 
        aux = lastOcurrence(newList, pos)   # O(n)              
        if(aux != -1):                      # O(1)
            result += len(newList) - aux    # O(n)
        else:
            result += (pos + extra)

        newList.append(pos)                 # O(1)
        if(pos >= 1): extra += 1

    print(result)

#4
#1 3 1 3

# a b c d e 
# a b c d e e
# a b c d e e c