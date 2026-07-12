from time import sleep
time=[]
while True:
    lista = []
    futebol = {}

    futebol['nome']=str(input('Nome do jogador: '))
    partidas=int(input(f'Quantas partidas {futebol["nome"]} jogou: '))
    for c in range(0,partidas):
        gol=int(input(f'Quantos gols na partida {c+1}: '))
        lista.append(gol)
        futebol['gols']=lista

    futebol['gols']=lista[:]
    futebol['total'] =sum(lista)
    time.append(futebol.copy())

    q=str(input('Quer continuar? [S/N] ')).upper()
    if q=='N':
        print('=' * 40)
        print(f'{"Num":<5}{"Nome":<15}{"Gols":<20}{"Total"}')
        print('-' * 40)

        for i, jogador in enumerate(time):
            print(f'{i:<5}{jogador["nome"]:<15}{str(jogador["gols"]):<20}{jogador["total"]}')
        break
while True:
    mostrar=int(input('(999-> Encerrar) Mostrar os dados de qual jogador: '))
    if mostrar == 999:
        print('Encerrado...')
        print('Obrigado volte sempre!')
        sleep(1)
        break
    if mostrar>=0 and mostrar<=len(time):
        print(f'Nome do jogador: {time[mostrar]["nome"]}')
        print(f'Gols do jogador: {time[mostrar]["gols"]}')
        print(f'Total de gols: {time[mostrar]["total"]}')
    else:
        print('Jogador inexistente')