# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def searchUntil(history, updateNum, value):
    pos = 0
    for i in range(updateNum-1, -1):
        pos += 1
        if(history[i] == value): return pos
    return -1


while(1):
    N = int(input("Enter N: "))
    if(N == 0): break                   
    
    cmd = map(int, input().split()) 
    num = 0
    used = {}   # or used = dict() 

    for i, v in enumerate(cmd):
        if v in used:
            num += num + i - used[v]    # used v indica qual a posição "extra" em que o comando foi chamado pela ultima vez
        else:
            num += num + i + v 
        used[v] = i
    print(num) 
                


#4
#1 3 1 3

# a b c d e 
# a b c d e e
# a b c d e e c