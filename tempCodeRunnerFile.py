# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while(0):
    N = input()
    if(N == 0): break
    list = map(int, input().split()) #split without arg uses space bar
    result = 0
    for pos in list:
        result = result + (N - pos + 1)
    print(result)