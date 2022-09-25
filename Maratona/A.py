def removeFrom(lista, elemento):
    newLista = []
    for item in lista:
        if(item != elemento):
            newLista.append(item)
    return newLista


n = int(input())
listaDeAlunos = []
listaDeListaDeNotas = []

for i in range(n):
    nome = input()
    item = list(map(float, input().split(' ')))
    listaDeAlunos.append(nome)
    listaDeListaDeNotas.append(item)

for i, lista in enumerate(listaDeListaDeNotas, 0):
    if(len(lista) > 3): 
        menorNotaProva = min(lista)
        #print(menorNotaProva)
        for nota in lista:
            #print(i)
            if(nota <= menorNotaProva):
                listaDeListaDeNotas[i] = removeFrom(lista, nota) 
            


for i, nome in enumerate(listaDeAlunos):
    soma = float(0)
    k = float(max(2, len(listaDeListaDeNotas[i])))
    #print(listaDeListaDeNotas[i])
    #print(k)
    for nota in listaDeListaDeNotas[i]:
        soma += (nota/k)
    print(f"{nome}: {soma:.1f}")



