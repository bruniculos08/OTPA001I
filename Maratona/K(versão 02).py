def getMenorVolta(run):
    menor = min(run[0]['listaDeTempos'])
    for i in range(len(run)):
        menor = min(menor, min(run[i]['listaDeTempos']))
    return menor

n, v = map(int, input().split(' '))
run = {}
for i in range(n):
    result = input().split(' ')
    runner = result[0]
    result = result[1:]
    #print(result)
    run[i] = {'racer' : runner, 'listaDeTempos' : [], 'tempoTotal' : 0}
    for j in range(v):
        minutos, segundos, milisegundos = map(int, result[j].split(':'))
        run[i]['listaDeTempos'].append((minutos*60*1000)+segundos*1000+milisegundos)
        run[i]['tempoTotal'] += (minutos*60*1000)+segundos*1000+milisegundos

recorde = getMenorVolta(run)
# Ordena o dicionario pelo item ['tempoTotal'] do segundo elemento de cada tupla:
run = (sorted(run.items(), key=lambda kv: kv[1]['tempoTotal'])[0:10]) # lenght é n-1 para 0:n
# lamba é uma função que recebe um elemento kv e retorna kv[1]['tempoTotal'], mas note que, nesse caso o dict é uma tupla por isso kv[1]:


#print(run)

num = -1
for item in run:
    #print(item['listaDeTempos'])
    #print(item[1]['listaDeTempos'])
    if min(item[1]['listaDeTempos']) == recorde:
        num = item[1]['racer']
        break
if num == -1:
    print("NENHUM")
else:
    print(num)
        
