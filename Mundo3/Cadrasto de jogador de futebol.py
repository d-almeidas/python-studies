lista=[]
futebol={}

futebol['nome']=str(input('Digite o nome do jogador: '))
partidas=int(input(f'Quantas partidas {futebol["nome"]} jogou? '))
for c in range(0,partidas):
    gol=int(input(f'Quantos gols na partida {c}? '))
    lista.append(gol)
    futebol['gols']=lista
print('-'*40)
print(f'Nome do jogador: {futebol["nome"]}')
print(f'Quantidade de gols: {futebol["gols"]}')
print(f'Total de gols: {sum(lista)}')
print('-'*40)
print(f'O jogador {futebol["nome"]} jogou {partidas} partidas')
for c in range(0,partidas):
    print(f'=> Na partida {c} fez: {lista[c]} gols')
print(f'Foi um total de {sum(lista)} gols')
print('-'*40)

