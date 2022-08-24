# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while(1):
    N = int(input("Enter N: "))
    if(N == 0): break
    list = map(int, input().split()) #split without arg uses space bar
    result = 0
    extra = 0
    for pos in list:
        result += (pos + extra)
        if(pos > 1): extra += 1
    print(result)

#4
#1 3 1 3

# a b c d e
# a b c d e