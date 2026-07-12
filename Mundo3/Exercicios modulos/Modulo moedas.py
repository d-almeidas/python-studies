from Utilidadescdv import moeda
p=float(input('Digite o valor do produto: '))
print(f'A metade de {p} e {moeda.metade(p)}')
print(f'O dobro de {p} e {moeda.dobro(p)}')
print(f'Aumentando 10% de {p} e {moeda.aumentar(p,10)}')
print(f'Diminuindo 13% de {p} e {moeda.diminuir(p,13)}')