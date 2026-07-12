def ficha(nome='<desconhecido>',gols=0):
    print(f'{nome} fez {gols} gols no campeonato')

nome = (input('digite o nome do jogador: '))
if nome == "":
    nome = '<desconhecido>'

gols =(input('digite a quantidade de gols: '))
if gols == "":
    gols = 0
else:
    gols = int(gols)

ficha(nome,gols)

