from Utilidadescdv import moeda
p = float(input(f'Digite o valor do produto R$: '))
print(f'A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} e {moeda.dobro(p)}')
print(f'Aumentando 10% de {moeda.moeda(p)} e {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 13% de {moeda.moeda(p)} e {moeda.moeda(moeda.diminuir(13))}')