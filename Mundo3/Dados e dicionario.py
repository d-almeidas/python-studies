from random import randint
from operator import itemgetter

jogadores={}
ranking=[]
for c in range(1,7):
    dado = randint(1, 6)
    print(f' O jogador {c} tirou {dado}')
    jogadores[c]=dado
print('Ranking dos jogadores')
ranking=sorted(jogadores.items(),key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1} lugar: Jogador {v[0]} com {v[1]}')







