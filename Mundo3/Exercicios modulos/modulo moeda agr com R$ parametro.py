from Utilidadescdv import moeda
p = float(input(f'Digite o valor do produto R$: '))
print(f'A metade de {moeda.moeda(p)} e {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p,True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} e {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 13% de {moeda.moeda(p)} e {moeda.diminuir(p,13,True)}')