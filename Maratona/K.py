from asyncio.windows_events import INFINITE

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
    
def getDecimoTempo(run):
    toSortTempos = []
    for i in range(len(run)):
        toSortTempos.append(run[i]['tempoTotal'])
    n = len(toSortTempos)
    if(n > 10):
        return sorted(toSortTempos)[9]
    else:
        return (max(toSortTempos))

def getMenorVolta(run):
    menor = min(run[0]['listaDeTempos'])
    for i in range(len(run)):
        menor = min(menor, min(run[i]['listaDeTempos']))
    return menor

def getNum(run, menorVolta, decimoTempo):
    num = -1
    tempoTotalDoRecordista = INFINITE
    # Criar outra varial para o de melhor posição
    for i in range(len(run)):
        if(run[i]['tempoTotal'] <= decimoTempo and menorVolta == min(run[i]['listaDeTempos']) and run[i]['tempoTotal'] <= tempoTotalDoRecordista):
            num = run[i]['racer']
            tempoTotalDoRecordista = run[i]['tempoTotal']
            
    return num

result = getNum(run, getMenorVolta(run), getDecimoTempo(run))
if(result != -1):
    print(result)
else:
    print("NENHUM")