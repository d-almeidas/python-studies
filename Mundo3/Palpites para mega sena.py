from random import randint
from time import sleep

print('='*40)
print('Mega sena'.center(40))
print('='*40)

mega=[]
jogos=int(input('Quantos paliptes de jogos deseja?: '))
for c in range(0,jogos):
    jogon=[]

    while len(jogon)<6:
        comp=randint(1,60)

        if comp not in jogon:
            jogon.append(comp)

    mega.append(jogon)
for pos, jogo in enumerate(mega):
    print(f'Jogo {pos+1}: {jogo}')
    sleep(1)
print('VOLTE SEMPRE!')





